#!/usr/bin/env python3
"""YouTube transcript sync.

Tracks a list of YouTube sources (playlist / channel / single video) in a
sources.json file, downloads English subtitles for any *new* videos with
``yt-dlp``, converts each new SRT into a clean paragraph-wrapped text file,
and prints a summary of what was added.

Designed to be idempotent and safe to re-run on a cron / launchd schedule.

Commands
--------
    sync   [--only NAME ...] [--check-only]
    list
    add    NAME URL OUTPUT_DIR
    remove NAME

If no subcommand is given, ``sync`` is assumed.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DEFAULT_SOURCES = SKILL_DIR / "sources.json"

TIMESTAMP_RE = re.compile(
    r"\d{2}:\d{2}:\d{2}[,.]\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}[,.]\d{3}"
)
TAG_RE = re.compile(r"<[^>]+>")
INDEX_RE = re.compile(r"^\d+$")
ARCHIVE_FILENAME = ".download-archive.txt"


# ---------------------------------------------------------------------------
# SRT -> plain text conversion
# ---------------------------------------------------------------------------

def srt_to_text(srt_path: Path) -> str:
    """Strip indices, timestamps, HTML tags, and duplicate rolling captions."""
    lines: list[str] = []
    for raw in srt_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or INDEX_RE.match(line) or TIMESTAMP_RE.search(line):
            continue
        line = TAG_RE.sub("", line)
        if not line:
            continue
        # YouTube auto-captions roll forward, repeating the same line as the
        # next caption gets built up. Collapse those.
        if lines and lines[-1] == line:
            continue
        lines.append(line)

    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text).strip()
    return "\n".join(
        textwrap.wrap(text, width=100, break_long_words=False, break_on_hyphens=False)
    )


# ---------------------------------------------------------------------------
# sources.json helpers
# ---------------------------------------------------------------------------

def load_sources(sources_file: Path) -> list[dict]:
    if not sources_file.exists():
        return []
    data = json.loads(sources_file.read_text(encoding="utf-8"))
    return list(data.get("sources", []))


def save_sources(sources_file: Path, sources: list[dict]) -> None:
    sources_file.parent.mkdir(parents=True, exist_ok=True)
    sources_file.write_text(
        json.dumps({"sources": sources}, indent=2) + "\n", encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Core sync logic
# ---------------------------------------------------------------------------

def _archive_ids(archive_file: Path) -> set[str]:
    """Return the set of YouTube IDs recorded in yt-dlp's download archive."""
    if not archive_file.exists():
        return set()
    ids: set[str] = set()
    for line in archive_file.read_text(encoding="utf-8").splitlines():
        parts = line.strip().split()
        if len(parts) >= 2:
            # archive format: "<extractor> <video_id>"
            ids.add(parts[1])
    return ids


def _list_remote_videos(url: str) -> list[tuple[str, str]]:
    """Return [(video_id, title), ...] for every video in the source URL."""
    result = subprocess.run(
        [
            "yt-dlp",
            "--no-update",
            "--flat-playlist",
            "--print",
            "%(id)s\t%(title)s",
            url,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    # Titles like "[Private video]" / "[Deleted video]" indicate unavailable
    # entries — yt-dlp can't fetch them and we shouldn't surface them as "new".
    unavailable = {"[Private video]", "[Deleted video]", "[Members only]"}
    out: list[tuple[str, str]] = []
    for line in result.stdout.splitlines():
        if "\t" not in line:
            continue
        vid, title = line.split("\t", 1)
        vid = vid.strip()
        title = title.strip()
        if vid and title and title not in unavailable:
            out.append((vid, title))
    return out


def _dedupe_en_orig(output_dir: Path) -> None:
    """Collapse `*.en-orig.srt` + `*.en.srt` duplicates into `*.srt`.

    yt-dlp downloads both the manual-caption track and the auto-generated
    track when available. We prefer the manual one (`en-orig`) but fall back
    to `en` when only auto-captions exist.
    """
    for f in list(output_dir.glob("*.en-orig.srt")):
        base = f.name[: -len(".en-orig.srt")]
        en_file = output_dir / f"{base}.en.srt"
        target = output_dir / f"{base}.srt"
        if en_file.exists():
            en_file.unlink()
        f.rename(target)
    # If only `.en.srt` exists (no manual track), promote it.
    for f in list(output_dir.glob("*.en.srt")):
        base = f.name[: -len(".en.srt")]
        target = output_dir / f"{base}.srt"
        if not target.exists():
            f.rename(target)


def sync_source(source: dict, check_only: bool = False) -> dict:
    """Sync one source. Returns dict with ``name``, ``new_count``, ``new_titles``."""
    name = source["name"]
    url = source["url"]
    output_dir = Path(source["output_dir"]).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_file = output_dir / ARCHIVE_FILENAME

    # If the user already had transcripts in this folder before adopting the
    # skill, seed the archive from existing filename `[videoId]` patterns so
    # we don't re-download everything.
    if not archive_file.exists():
        existing_ids: list[str] = []
        for srt in output_dir.glob("*.srt"):
            m = re.search(r"\[([\w-]{11})\]\.srt$", srt.name)
            if m:
                existing_ids.append(m.group(1))
        if existing_ids:
            archive_file.write_text(
                "\n".join(f"youtube {vid}" for vid in sorted(set(existing_ids))) + "\n",
                encoding="utf-8",
            )

    if check_only:
        remote = _list_remote_videos(url)
        seen = _archive_ids(archive_file)
        new = [(vid, t) for vid, t in remote if vid not in seen]
        return {
            "name": name,
            "new_count": len(new),
            "new_titles": [t for _, t in new],
            "new_ids": [v for v, _ in new],
        }

    # Snapshot existing SRT files so we can identify the new ones afterwards.
    before = {p.name for p in output_dir.glob("*.srt")}
    before |= {p.name for p in output_dir.glob("*.en*.srt")}

    cmd = [
        "yt-dlp",
        "--no-update",
        "--ignore-errors",
        "--download-archive",
        str(archive_file),
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-lang",
        "en.*,en",
        "--sub-format",
        "vtt/best",
        "--convert-subs",
        "srt",
        "-o",
        str(output_dir / "%(playlist_index)03d - %(title).100B [%(id)s].%(ext)s"),
        url,
    ]
    subprocess.run(cmd, check=False)

    _dedupe_en_orig(output_dir)

    after = {p.name for p in output_dir.glob("*.srt")}
    new_files = sorted(after - before)

    # yt-dlp's --download-archive only records entries when a *video* download
    # completes. We're --skip-download, so we must update the archive ourselves
    # by scanning new SRT filenames for their `[videoId]` token.
    if new_files:
        existing = _archive_ids(archive_file)
        new_ids: list[str] = []
        for fname in new_files:
            m = re.search(r"\[([\w-]{11})\]\.srt$", fname)
            if m and m.group(1) not in existing:
                new_ids.append(m.group(1))
                existing.add(m.group(1))
        if new_ids:
            with archive_file.open("a", encoding="utf-8") as fh:
                for vid in new_ids:
                    fh.write(f"youtube {vid}\n")

    plain_dir = output_dir / "plain-text"
    plain_dir.mkdir(exist_ok=True)
    new_titles: list[str] = []
    for fname in new_files:
        srt = output_dir / fname
        if not srt.exists():
            continue
        try:
            text = srt_to_text(srt)
        except Exception as exc:  # noqa: BLE001
            print(f"  WARN: could not convert {srt.name}: {exc}", file=sys.stderr)
            continue
        out = plain_dir / (srt.stem + ".txt")
        header = srt.stem
        out.write_text(
            f"{header}\n{'=' * len(header)}\n\n{text}\n", encoding="utf-8"
        )
        new_titles.append(srt.stem)

    return {"name": name, "new_count": len(new_titles), "new_titles": new_titles}


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_sync(args: argparse.Namespace, sources_file: Path) -> int:
    if shutil.which("yt-dlp") is None:
        print("ERROR: yt-dlp not found in PATH. Install it: brew install yt-dlp", file=sys.stderr)
        return 127

    sources = load_sources(sources_file)
    if not sources:
        print("No sources configured. Use the 'add' subcommand first.", file=sys.stderr)
        return 1

    only = set(args.only) if args.only else None
    total_new = 0
    summary: list[dict] = []
    for source in sources:
        if only and source["name"] not in only:
            continue
        print(f"\n=== {source['name']} ===")
        print(f"  url: {source['url']}")
        result = sync_source(source, check_only=args.check_only)
        if result["new_count"]:
            verb = "would download" if args.check_only else "downloaded"
            print(f"  {result['new_count']} new episode(s) {verb}:")
            for t in result["new_titles"]:
                print(f"    + {t}")
        else:
            print("  no new episodes")
        total_new += result["new_count"]
        summary.append(result)

    print(f"\nTotal new across all sources: {total_new}")
    if args.json:
        print(json.dumps({"total_new": total_new, "sources": summary}, indent=2))
    return 0


def cmd_list(_args: argparse.Namespace, sources_file: Path) -> int:
    sources = load_sources(sources_file)
    if not sources:
        print("No sources configured.")
        return 0
    print(f"Tracked sources ({len(sources)}):")
    for s in sources:
        print(f"\n  • {s['name']}")
        print(f"      url:    {s['url']}")
        print(f"      output: {s['output_dir']}")
        archive = Path(s["output_dir"]).expanduser() / ARCHIVE_FILENAME
        if archive.exists():
            n = len(_archive_ids(archive))
            print(f"      synced: {n} episode(s)")
    return 0


def cmd_add(args: argparse.Namespace, sources_file: Path) -> int:
    sources = load_sources(sources_file)
    if any(s["name"] == args.name for s in sources):
        print(f"Source '{args.name}' already exists.", file=sys.stderr)
        return 1
    sources.append(
        {
            "name": args.name,
            "url": args.url,
            "output_dir": str(Path(args.output_dir).expanduser().resolve()),
        }
    )
    save_sources(sources_file, sources)
    print(f"Added '{args.name}' -> {args.output_dir}")
    print("Run 'sync' to download transcripts.")
    return 0


def cmd_remove(args: argparse.Namespace, sources_file: Path) -> int:
    sources = load_sources(sources_file)
    new = [s for s in sources if s["name"] != args.name]
    if len(new) == len(sources):
        print(f"No source named '{args.name}'.", file=sys.stderr)
        return 1
    save_sources(sources_file, new)
    print(f"Removed '{args.name}'. (Downloaded files were left in place.)")
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="youtube-transcripts",
        description="Sync YouTube transcripts incrementally.",
    )
    parser.add_argument(
        "--sources",
        default=str(DEFAULT_SOURCES),
        help=f"Path to sources.json (default: {DEFAULT_SOURCES})",
    )
    sub = parser.add_subparsers(dest="cmd")

    p_sync = sub.add_parser("sync", help="Download new episodes for tracked sources")
    p_sync.add_argument("--only", nargs="*", help="Sync only the named sources")
    p_sync.add_argument(
        "--check-only",
        action="store_true",
        help="List what's new without downloading",
    )
    p_sync.add_argument(
        "--json", action="store_true", help="Also emit a JSON summary at the end"
    )

    sub.add_parser("list", help="List tracked sources")

    p_add = sub.add_parser("add", help="Add a new source")
    p_add.add_argument("name", help="Short identifier (e.g. 'superwall-podcast')")
    p_add.add_argument("url", help="Playlist / channel / video URL")
    p_add.add_argument("output_dir", help="Directory to write transcripts into")

    p_remove = sub.add_parser("remove", help="Remove a source")
    p_remove.add_argument("name")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    sources_file = Path(args.sources).expanduser()

    # Default to `sync` when no subcommand was given.
    if args.cmd is None:
        args.cmd = "sync"
        args.only = None
        args.check_only = False
        args.json = False

    if args.cmd == "sync":
        return cmd_sync(args, sources_file)
    if args.cmd == "list":
        return cmd_list(args, sources_file)
    if args.cmd == "add":
        return cmd_add(args, sources_file)
    if args.cmd == "remove":
        return cmd_remove(args, sources_file)

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())

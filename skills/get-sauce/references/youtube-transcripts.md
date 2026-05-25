# Reference: YouTube transcript sync

This document is the full reference for `scripts/sync.py` — the YouTube transcript sync tool bundled into this skill. Originally adapted from the standalone `youtube-transcripts` skill, captured here so `get-sauce` is fully self-contained.

## What it does

Maintains a local corpus of YouTube transcripts for one or more sources (playlists, channels, or single videos). On every run it:

1. Lists every video in each tracked source
2. Skips videos already downloaded (via `yt-dlp --download-archive`)
3. Downloads English subtitles (manual if available, else auto-generated) as `.srt`
4. Converts each new `.srt` into a clean paragraph-wrapped `.txt` in a `plain-text/` subfolder
5. Prints a summary of newly added episodes

It is designed to be **idempotent and safe to re-run** — perfect for cron / launchd / scheduled-agent polling.

## Prerequisites

- `yt-dlp` installed (`brew install yt-dlp`)
- `python3` (any 3.8+)
- `ffmpeg` (optional, only needed for some subtitle conversions; `brew install ffmpeg`)

## File layout

- `scripts/sync.py` — the entry point (CLI with `sync`, `list`, `add`, `remove` subcommands)
- `sources.json` — list of tracked sources (created automatically on first `add`; sits next to `SKILL.md`)

## Commands

### List tracked sources
```bash
python3 skills/get-sauce/scripts/sync.py list
```

### Add a new source
```bash
python3 skills/get-sauce/scripts/sync.py add \
  <name> <youtube_url> <output_dir>

# Example: track the Superwall Podcast playlist
python3 skills/get-sauce/scripts/sync.py add \
  superwall-podcast \
  "https://www.youtube.com/playlist?list=PL3XL-MsZorn_Nfi3jrPqQtxDk-kxyaaz8" \
  ~/Kanna/youtube-scraping/superwall-podcast-transcripts
```

Supported URL types:
- Playlists: `https://www.youtube.com/playlist?list=...`
- Channels: `https://www.youtube.com/@HandleName` or `.../@HandleName/videos`
- Single videos: `https://www.youtube.com/watch?v=...`

### Sync everything (download new episodes for all sources)
```bash
python3 skills/get-sauce/scripts/sync.py sync
```

### Sync only specific sources
```bash
python3 skills/get-sauce/scripts/sync.py sync \
  --only superwall-podcast another-podcast
```

### Just check for new episodes (no download)
```bash
python3 skills/get-sauce/scripts/sync.py sync --check-only
```

Useful for `cron` jobs that should only notify on new content.

### Emit JSON summary alongside the human output
```bash
python3 skills/get-sauce/scripts/sync.py sync --json
```

### Remove a source (does not delete downloaded files)
```bash
python3 skills/get-sauce/scripts/sync.py remove <name>
```

## Output structure

For each source, files are organized as:

```
<output_dir>/
├── 001 - <Title> [<videoId>].srt        # raw SRT with timestamps
├── 002 - <Title> [<videoId>].srt
├── ...
├── plain-text/
│   ├── 001 - <Title> [<videoId>].txt    # clean paragraph-wrapped text
│   ├── 002 - <Title> [<videoId>].txt
│   └── ...
└── .download-archive.txt                # yt-dlp's archive of completed downloads
```

The `.download-archive.txt` is what enables idempotency. **Don't delete it** unless you want to re-download everything. If you do delete it, `sync.py` will re-seed it from existing `[videoId]` filename tokens on the next run, so no actual re-downloads will happen — just a noisy first run.

## Auto-polling for new episodes

Pick whichever scheduler you prefer.

### Option A — cron (simplest)

```cron
# Check every 6 hours and download new episodes
0 */6 * * * /usr/bin/python3 /Users/$USER/moonlight/sauce/skills/get-sauce/scripts/sync.py sync >> /tmp/get-sauce.log 2>&1
```

### Option B — macOS launchd

Create `~/Library/LaunchAgents/com.user.get-sauce-sync.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.user.get-sauce-sync</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/python3</string>
    <string>/Users/USERNAME/moonlight/sauce/skills/get-sauce/scripts/sync.py</string>
    <string>sync</string>
  </array>
  <key>StartInterval</key><integer>21600</integer> <!-- every 6 hours -->
  <key>StandardOutPath</key><string>/tmp/get-sauce.log</string>
  <key>StandardErrorPath</key><string>/tmp/get-sauce.err</string>
</dict>
</plist>
```

Load it: `launchctl load ~/Library/LaunchAgents/com.user.get-sauce-sync.plist`

### Option C — Claude Code `schedule` skill (recommended for "notify me + Claude can react")

Use the `schedule` skill to run this on a cron. The agent will see any new episodes in the sync output and can react (e.g. summarize them, post to Slack, queue them for the next sauce hunt, etc.):

> /schedule add "Sync sauce transcripts" — every 6 hours — run `python3 skills/get-sauce/scripts/sync.py sync`

### Option D — `loop` skill (for ad-hoc polling in current session)

> /loop 30m run `skills/get-sauce/scripts/sync.py sync --check-only` and tell me if any new episodes appeared

## What this script does NOT do

- It does not download video or audio (transcripts only — keeps disk footprint tiny)
- It does not translate subtitles (English-only by default; modify `--sub-lang` in `sync.py` if needed)
- It does not transcribe audio when no captions exist (use Whisper for that separately)

## Troubleshooting

- **"yt-dlp not found"** — `brew install yt-dlp`. Ensure `/opt/homebrew/bin` (Apple Silicon) or `/usr/local/bin` (Intel) is on PATH.
- **"WARNING: ... requested format is not available"** — usually safe to ignore; yt-dlp will fall back.
- **"Some web client https formats have been skipped"** — also benign; we only need the subtitle track.
- **Pre-2023 videos missing auto-captions** — some old videos genuinely have no captions; the script will log and skip them.
- **yt-dlp out of date** — `brew upgrade yt-dlp` (or `pip install -U yt-dlp`). YouTube changes their API constantly; keep yt-dlp fresh.
- **Playlist index keeps shifting** — if YouTube reorders a playlist, the numeric prefix on filenames may drift for new episodes. The video ID in brackets is the stable identifier.

## Implementation notes (for hacking on `sync.py`)

- `sources.json` lives next to `SKILL.md` (computed as `Path(__file__).resolve().parent.parent / "sources.json"`)
- Manual captions are downloaded under `*.en-orig.srt`, auto-captions under `*.en.srt`. `_dedupe_en_orig()` prefers manual and collapses both into `*.srt`.
- Because we use `--skip-download`, `yt-dlp`'s native `--download-archive` does NOT write entries. The script manually appends `youtube <videoId>` lines after each successful subtitle pull, parsing the `[videoId]` token from the SRT filename.
- "Unavailable" entries (private, deleted, members-only) are filtered from the remote-listing pass so they don't show up as forever-pending "new" episodes.
- SRT-to-text conversion: strips index lines, timestamp lines, HTML tags, and collapses rolling-caption duplicates (YouTube auto-captions emit each line several times as words are appended). Wraps to 100-char paragraphs.

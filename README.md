# Sauce Skills

Agent skill for finding **"the sauce"** — first-hand operator advice from founders, builders, and innovators — by mining transcripts of podcasts, interviews, and long-form talks. Pairs a curated registry of ~120 top startup/founder/VC/app/AI sources with a YouTube transcript sync tool and spawns a wide-context subagent to surface direct quotes (no RAG, no summarization).

## Install

We recommend using the [skills.sh](https://skills.sh) CLI to install:

Install all skills:

```bash
npx skills add anglinb/sauce
```

Install just the `get-sauce` skill:

```bash
npx skills add anglinb/sauce --skill get-sauce
```

## What you get

| Skill | What it does |
|---|---|
| `get-sauce` | Discover candidate sources via grepable registry → download YouTube transcripts → spawn a wide-context subagent that quotes founders verbatim with file-level attribution. Defaults to Superwall Podcast for app/monetization questions, Starter Story for general business. |

## Prerequisites

The `get-sauce` skill depends on a couple of system tools for downloading YouTube transcripts:

- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) — `brew install yt-dlp`
- `python3` (3.8+) — system Python is fine on macOS
- `ffmpeg` (optional, only for some subtitle conversions) — `brew install ffmpeg`

Transcripts are written outside the repo by default (`~/Kanna/youtube-scraping/<source>-transcripts/`) so the repo stays light.

## Example usage

Once installed, just ask Claude something like:

> "Get me the sauce on how indie app founders use UGC to scale to seven figures."

The skill will:

1. Grep its registry (`references/sources.md`) for relevant podcasts/blogs/founders
2. Confirm the right source(s) with you (recommending the obvious default for the domain)
3. Run `scripts/sync.py` to incrementally download / refresh the transcript corpus
4. Spawn a sub-agent that reads the entire corpus and returns quote-backed findings
5. Relay the operators' own words back — no paraphrasing, every claim cited to an episode

## Updating the source registry

The registry of ~120 startup/founder content sources lives at `skills/get-sauce/references/sources.md` in a simple grepable format:

```
Name | url1, url2, x.com/handle | medium-tag, topic-tag, topic-tag, …
```

Open a PR with additions if you have a favorite operator-voice source we're missing.

## License

MIT — see [LICENSE](LICENSE) if present, or treat as MIT by default.

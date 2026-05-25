<p align="center">
  <img src="assets/hero.png" alt="Sauce — distilled operator wisdom from the founders who actually built it" width="100%" />
</p>

# Sauce Skills

Agent skill for finding **"the sauce"** — first-hand operator advice from founders, builders, and innovators — by mining transcripts of podcasts, interviews, conference talks, and long-form interviews. Pairs a curated registry of ~180 top startup/founder/VC/app/AI/conference sources with a YouTube transcript sync tool and a self-evaluating research loop that keeps pulling until the answer is actually good.

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
| `get-sauce` | Discover candidate sources via grepable registry (~180 podcasts, blogs, newsletters, conferences) → download YouTube transcripts → spawn a wide-context subagent that quotes founders verbatim with file-level attribution → critic-evaluates the answer → loops with new sources if it's not good enough. Defaults: Superwall Podcast for app/monetization questions, Starter Story for general business. |

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

1. Grep its registry (`references/sources.md`) for relevant podcasts/blogs/founders/conferences
2. Confirm the right source(s) with you (recommending the obvious default for the domain)
3. Run `scripts/sync.py` to incrementally download / refresh the transcript corpus
4. Spawn a sub-agent that reads the entire corpus and returns quote-backed findings
5. **Run a critic over the answer and loop if it's not good enough** ← see below
6. Relay the operators' own words back — no paraphrasing, every claim cited to an episode or talk

## How the answer keeps improving — the eval loop

Most "research" agents are one-shot: ask question → retrieve → answer → done. The problem: with ~180 sources and imperfect tagging, the first grep pass often picks a corpus that's *plausibly* relevant but the wrong angle. (Ask about UGC and you might get only consumer-app voices when half your question was really about B2B distribution.)

To catch that, `get-sauce` runs a **critic subagent** after the sauce-hunter returns. The critic only sees two things — your **original question** and the **answer** — and scores it on five axes:

| Axis | What it checks |
|---|---|
| **Direct-answer coverage** | Did the answer address what you actually asked, or drift to adjacent topics? |
| **Quote density** | Are claims backed by verbatim operator quotes, or paraphrased-as-fact? |
| **Perspective diversity** | Multiple stages / business models / ideologies — or homogeneous voices? |
| **Tactical specificity** | Real numbers, dollar figures, step-by-step tactics — or abstract advice? |
| **Unresolved gaps** | Lists 2–4 specific sub-questions the corpus did NOT answer |

Then it issues one of three verdicts:

- **`SHIP`** (avg ≥ 8/10) — Relay the answer to you as-is.
- **`AUGMENT`** (5–7/10) — Pull in 1–2 *additional* sources from the registry, re-run the sauce-hunter with a prompt that explicitly targets the unresolved gaps, and re-critique. Cap: **2 augment loops** so cost stays bounded.
- **`REDO`** (< 5/10 or wrong-corpus) — Pivot entirely to different sources. Cap: **1 redo loop**.

When the loop fires, the skill tells you up front before doing it:

> _"First pass found ~70% of what you asked, but it was mostly consumer-app voices and you implied you care about enterprise B2B. Pulling in [Source X] and re-running — give me ~2 min."_

So instead of accepting a half-answer from a half-right corpus, the skill **keeps going until the critic signs off** (or it hits the loop cap, in which case it ships what it has and tells you what's still missing). It's the difference between a one-shot retrieval and an actual research workflow.

## Updating the source registry

The registry of ~180 startup/founder/conference content sources lives at `skills/get-sauce/references/sources.md` in a simple grepable format:

```
Name | url1, url2, x.com/handle | medium-tag, topic-tag, topic-tag, …
```

Open a PR with additions if you have a favorite operator-voice source we're missing.

## License

MIT — see [LICENSE](LICENSE) if present, or treat as MIT by default.

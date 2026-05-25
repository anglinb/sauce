---
name: get-sauce
description: Find "the sauce" on a question by mining transcripts of podcasts, interviews, blogs, and talks from founders and innovators who've actually done the thing. Use when the user asks "how do other founders do X", "what's the sauce on Y", "find me real-world advice on Z", "what have people said about...", or any time the goal is to surface first-hand operator knowledge (not generic web articles or LLM priors). Ships with a grepable registry of ~120 top startup/founder/VC/app/AI sources (Paul Graham, Sam Altman, Naval, Acquired, My First Million, Lenny's, Stripe Press, Y Combinator, a16z, Stratechery, Superwall Podcast, Starter Story, and many more). Defaults: Superwall Podcast for app/paywall/monetization questions, Starter Story for general business/bootstrapping. Bundles its own YouTube transcript sync tool and spawns a wide-context subagent to actually answer the question.
---

# Get Sauce

## What "sauce" means

**Sauce** = the unfiltered, first-hand, "here's what actually worked for me" knowledge that founders, operators, and innovators share in long-form interviews. It's the opposite of generic blog-post advice. The goal of this skill is to find sauce on a question by going directly to source media (podcasts, interviews, founder talks) and reading what real practitioners have said in their own words.

This skill is for questions like:

- "How are other apps handling onboarding paywalls?"
- "What's the sauce on getting first 1,000 users for a B2B SaaS?"
- "How do indie founders price annual subscriptions?"
- "What have profitable bootstrappers said about hiring their first employee?"

It is **not** for questions where the answer is a quick lookup, a fact, or a code change.

## What's in this skill

This skill is fully self-contained. No dependency on any other skill.

```
skills/get-sauce/
├── SKILL.md                          # this file — the workflow
├── scripts/
│   └── sync.py                       # YouTube transcript sync CLI
├── references/
│   ├── sources.md                    # curated registry of ~120 top podcasts,
│   │                                 # blogs, newsletters, channels, founders
│   │                                 # — grepable by topic / medium / name
│   └── youtube-transcripts.md        # full sync.py / yt-dlp reference docs
├── sources.json                      # tracked podcasts/channels registry
│                                     # (auto-created on first `add`; gitignored)
└── .gitignore
```

Two registries to keep straight:

- **`references/sources.md`** — the **discovery** layer. A flat, grepable list of the
  best content in the world about startups, apps, VC, indie, AI, business. Use this to
  figure out *which* source to mine for any given question.
- **`sources.json`** — the **ingestion** layer. Tracks which YouTube playlists/channels
  have been downloaded locally via `sync.py`. Subset of `sources.md` — only YouTube
  things that we've decided to keep on disk for cheap re-reading.

`scripts/sync.py` wraps `yt-dlp` to download English subtitles for any new videos in a playlist/channel/video URL, strips timestamps and HTML tags, collapses rolling-caption duplicates, and writes clean paragraph-wrapped `.txt` files. Idempotent and safe to re-run — each run only pulls episodes not already in the local archive. See `references/youtube-transcripts.md` for the complete CLI reference, implementation notes, and auto-polling setup options.

### Prerequisites

- `yt-dlp` — `brew install yt-dlp`
- `python3` (3.8+) — system Python is fine
- `ffmpeg` (optional, only for some subtitle conversions) — `brew install ffmpeg`

### Where transcripts get stored

Transcripts are large and binary-ish; they should **not** go in this repo. Default storage root is `~/Kanna/youtube-scraping/<short-name>-transcripts/`. The user already has at least one corpus there:

- `superwall-podcast` → `~/Kanna/youtube-scraping/superwall-podcast-transcripts/`

If `sources.json` is empty when you start, you can rehydrate the registry by running `add` against the same `output_dir` — `sync.py` seeds its download archive from existing `[videoId]` filename tokens and skips re-downloading anything already on disk.

## Workflow

### Step 1 — Pin down the question

Restate the user's question in one sentence and confirm it. Sauce-finding is expensive (downloading + reading transcripts), so make sure you're hunting for the right thing.

### Step 2 — Discover candidate sources from the registry

Before asking the user anything, **grep `references/sources.md`** to find which podcasts / blogs / channels / founders are likely to have sauce on the question. This is the "look around the room" step — you should never default to your own memory of who said what when there's a curated registry sitting right there.

```bash
# Grep by topic — start with 2-3 keywords from the question
grep -i "paywall\|monetization\|subscription\|IAP" skills/get-sauce/references/sources.md

# Or by specific person/publication if the user named one
grep -i "naval\|paul graham\|altman" skills/get-sauce/references/sources.md

# Filter by ingestion medium when that matters (see Step 4)
grep -i "| podcast"    skills/get-sauce/references/sources.md
grep -i "| blog"       skills/get-sauce/references/sources.md
grep -i "| youtube"    skills/get-sauce/references/sources.md
grep -i "| newsletter" skills/get-sauce/references/sources.md
```

**Each line in `sources.md` is formatted as:**

    Name | url1, url2, x.com/handle | tag1, tag2, tag3, ...

The **first tag is the medium** (`podcast`, `blog`, `newsletter`, `youtube`, `book-publisher`, `vc-publication`, `x-account`, `community`, `publication`); the rest are topic tags.

**If grep returns nothing or feels too narrow, read the whole file.** It's small (~120 entries) — `cat skills/get-sauce/references/sources.md` and skim it. The tags are imperfect; some sources cover broader ground than their tags suggest. Don't fall back on your own knowledge before reading the registry end-to-end.

### Step 3 — Ask the user to confirm the source(s)

Take the 3–6 most-relevant candidates from Step 2's grep and present them via `AskUserQuestion`. **Always include the right default first** based on the question's domain:

| Question domain | Default recommendation |
|---|---|
| Apps, paywalls, monetization, mobile growth, RevenueCat-style topics | **Superwall Podcast** |
| General business, bootstrapping, indie founders, $1M solo-business case studies | **Starter Story** |
| App subscriptions / IAP economics | **Sub Club Podcast** (or RevenueCat Blog) |
| PM / growth / product careers | **Lenny's Podcast** / **Lenny's Newsletter** |
| Deep dives on legendary companies | **Acquired** |
| Founder biographies & first principles | **Founders Podcast** (David Senra) |
| Bootstrapping / SaaS-without-VC | **Startups for the Rest of Us** / **Bootstrapped Founder** / **MicroConf** |
| VC strategy / fundraising | **20VC** / **YC Library** / **a16z Podcast** |
| Anything else | Top grep matches from Step 2 |

Phrasing example:

> For "<paraphrase of question>" the registry surfaced these as the highest-signal sources. I'd default to **<source>**, but tell me if you want me to mine something specific instead — or "all of them" if you want me to cast a wide net.

Allow multi-select if more than one source makes sense. If the user names someone not in the registry, just use what they said — and consider adding it to `sources.md` for next time.

### Step 4 — Pick the ingestion strategy by medium

`sync.py` only handles **YouTube** (videos with subtitles). The registry covers a wider set of media, so each chosen source needs the right ingestion path:

| Medium tag in `sources.md` | How to ingest |
|---|---|
| `podcast` (with YouTube link) | `sync.py` — most podcasts publish full episodes on YouTube with auto-captions |
| `youtube` | `sync.py` |
| `blog` | `WebFetch` each post. Find the archive/index page first, then fetch posts individually. For multi-page archives, consider grepping the registry for an alt URL (e.g. RSS). |
| `newsletter` | `WebFetch` the public archive (Substack, Beehiiv, etc. all expose one). Paywalled ones (`The Information`, `Stratechery`) require the user's cookies — skip or note the limitation. |
| `book-publisher` (e.g. Stripe Press) | `WebFetch` book summaries/excerpts. Full books are out of scope. |
| `vc-publication` | `WebFetch` the most-relevant essays from their index. |
| `community` (HN, Indie Hackers, Product Hunt) | Skip unless you can find a focused thread; community pages are too noisy for sauce hunting. |
| `x-account` | Best-effort only. Public X profiles have heavy rate-limiting and most threads are short. Note as a limitation; don't rely on X as a primary source. |

Multi-medium sources (e.g. Acquired = podcast + YouTube; Stratechery = blog + newsletter) — pick the medium that's cheapest to ingest in full. YouTube transcripts are nearly always the path of least resistance when available.

### Step 5 — Check what's already downloaded (YouTube path)

If you're going down the `sync.py` path, list current corpora first:

```bash
python3 skills/get-sauce/scripts/sync.py list
```

If a source matching the user's request is already tracked, **just sync it** (incremental — only pulls new episodes):

```bash
python3 skills/get-sauce/scripts/sync.py sync --only <source-name>
```

If it's not tracked yet, add it:

```bash
python3 skills/get-sauce/scripts/sync.py add \
  <short-name> "<youtube_url>" ~/Kanna/youtube-scraping/<short-name>-transcripts
```

Then run `sync --only <short-name>` to download.

**Naming convention:** `kebab-case`, short (e.g. `superwall-podcast`, `starter-story`, `my-first-million`). Reuse the exact `Name` from `sources.md` where possible (lowercased + kebabed) so the two registries stay aligned.

If `sources.json` doesn't yet know about an existing on-disk corpus (e.g. the user's `superwall-podcast` folder), add it pointing at that folder — the script will detect the already-downloaded SRTs by their `[videoId]` filename token and seed the archive instead of re-pulling everything.

See `references/youtube-transcripts.md` for the full CLI surface (additional flags, `--check-only`, `--json`, `remove`, etc.).

### Step 6 — Take a note about the corpus location

After sync completes, write a one-line note in the conversation like:

> 📝 Corpus note: `<source-name>` transcripts live at `<output_dir>/plain-text/` (N episodes total, M new this run). On the next sauce hunt against this source, just run `sync --only <source-name>` first to stay current.

This is so future invocations skip re-discovery and just incrementally update. The persistent source of truth is `skills/get-sauce/sources.json` — gitignored by default, so future sessions can always re-bootstrap by re-running `add` against the existing transcript folders.

### Step 7 — Decide what to feed the subagent

Look at the `plain-text/` directory:

```bash
ls -la <output_dir>/plain-text/ | head
du -sh <output_dir>/plain-text/
wc -w <output_dir>/plain-text/*.txt | tail -1
```

Strategy by corpus size:

- **< ~400K words total** → feed the entire corpus to the subagent. No filtering, no RAG — just pile it in.
- **400K – 1.5M words** → spawn a subagent and have *it* read everything via the Read tool. Tell it to be exhaustive.
- **> 1.5M words** → first do a cheap title/filename filter (filenames include the episode title) to pre-select likely-relevant episodes, then load those in full. Only filter when truly necessary — we want to avoid RAG-style chunking that loses context.

### Step 8 — Spawn the sauce-hunter subagent

Use the `Agent` tool with `subagent_type: "general-purpose"` (or `Explore` if you only need read-and-report). Give it:

1. **The user's exact question** — don't paraphrase; sauce-hunting depends on precise phrasing
2. **Why we care** — context for judgment calls
3. **The corpus path(s)** so it can read transcripts directly
4. **An instruction to quote liberally** — sauce is in the operator's own words, not your summary of their words
5. **Source attribution requirement** — every claim must cite which episode/transcript it came from (filename + ideally a short verbatim quote)

Prompt template:

```
You're hunting for "sauce" — first-hand operator advice — on this question:

  <USER'S EXACT QUESTION>

Context on why this matters: <1-3 sentences>

Source corpus: <ABSOLUTE PATH TO plain-text/ DIRECTORY>
This contains transcripts from <SOURCE NAME>. Each .txt file is one episode;
the filename includes the episode title.

Your job:
1. Read every transcript that could plausibly speak to the question. Err on the
   side of reading more — most files are short. Use Glob + Read directly; do
   NOT do keyword search and stop there.
2. Pull out direct quotes from founders/guests that answer the question.
3. Cluster the findings into themes (e.g. "What worked", "What didn't", "Common
   mistakes", "Numbers people shared").
4. For every claim, cite the source file and include a verbatim quote in
   blockquotes. No paraphrasing-as-fact.
5. End with a 5-bullet "what I'd actually do" synthesis — opinionated, drawn
   only from what the operators said, not your priors.

Length: as long as it needs to be. Quote density > brevity.
```

Run it in the foreground — you need the result to relay it back to the user.

### Step 9 — Relay the result

Pass the subagent's findings through to the user with a short framing intro (which sources, how many episodes, what question was asked). Don't re-summarize — the whole point is to surface the operators' own words.

## Re-using the skill on follow-ups

If the user asks a follow-up against the **same corpus**, skip Steps 2–6 and just spawn a fresh subagent with the new question (Step 8). The corpus is already current as of the most recent sync.

If they ask against a **different domain**, start over from Step 2 but check existing sources first — they may have already been tracked for a previous sauce hunt.

## Maintaining `references/sources.md`

The registry is the discovery engine — keep it current.

- When you finish a sauce hunt using a source that's **not** in the registry, **add it** before moving on. Reuse the format exactly: `Name | url1, url2, x.com/handle | medium-tag, topic-tags…`
- When the user mentions a person/publication you don't recognize, grep before assuming they're not there — the registry has ~120 entries and you won't recall every one.
- Tag the first column conservatively (use existing medium tags); be generous with topic tags so future greps find it.

## Repo hygiene

- ✅ Check in: `SKILL.md`, `scripts/sync.py`, `references/*.md`, `.gitignore`
- ❌ Do not check in: `sources.json` (user-specific paths), downloaded transcripts (live outside the repo at `~/Kanna/youtube-scraping/`)
- The bundled `.gitignore` already excludes `sources.json`.

## Anti-patterns

- ❌ Answering from your own knowledge ("Most founders say…") — the whole skill exists *because* the user wants real source material, not LLM priors.
- ❌ RAG-style snippet retrieval — we have enormous context windows; use them. Snippets lose voice and nuance.
- ❌ Summarizing without quoting. Sauce is in the words, not the gist.
- ❌ Skipping the user's source preference. If they say "I want to hear what Jason Fried thinks", don't go pull Lenny's Podcast.
- ❌ Downloading audio/video. Transcripts only — `sync.py` enforces `--skip-download --write-subs`.
- ❌ Storing transcripts inside the repo. They're large, binary-ish, and constantly growing.

## Further reading

- `references/sources.md` — curated registry of ~120 top startup/founder/VC/app/AI sources. Grep by topic or read end-to-end. **Always check this before falling back on LLM priors about who said what.**
- `references/youtube-transcripts.md` — full `sync.py` CLI reference, output layout, troubleshooting, cron/launchd/`schedule` setup, and implementation notes for hacking on the script.

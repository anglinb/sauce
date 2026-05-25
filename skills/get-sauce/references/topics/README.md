# Topics

Curated, hand-picked source lists organized by domain. The "topics" layer sits **on top of** the master registry at `references/sources.md` and exists because grep is good for discovery but bad for prioritization.

## Topics vs. master registry

| | `sources.md` (master) | `topics/<topic>.md` (curated) |
|---|---|---|
| **Purpose** | Comprehensive discovery | Fast, opinionated starting points |
| **Format** | Flat, pipe-delimited, grepable | Free-form markdown with notes |
| **Sorting** | By medium / loose category | By "where the sauce actually lives" for that domain |
| **Includes things outside the master registry?** | No — registry is the master | **Yes** — domain experts who don't fit the "founder content" frame still belong in their topic file (e.g. pixel artists, niche scientists, retired masters) |
| **Duplicates allowed across topics?** | N/A | **Yes** — the same source can appear in `apps.md`, `monetization.md`, and `ugc.md` if it's relevant to all three |

If a user asks "what's the sauce on X" and X clearly maps to a known topic, **open the topic file directly** — it's faster and higher-signal than a fresh grep. Fall back to the master registry only when no topic file fits.

## When to use a topic file vs. the master registry

```
User question
     │
     ▼
Is there a topics/<domain>.md that maps to it cleanly?
     │
     ├── YES → Read that topic file. Use its curated picks as the
     │         primary candidates. (You may still grep sources.md
     │         for an augment pass if the critic flags gaps.)
     │
     └── NO  → Grep sources.md as usual. After the hunt, consider
               adding a new topic file if this is a domain you'll
               see again.
```

## Adding a new topic

Use the existing files as templates. A topic file should contain:

1. **One-paragraph overview** — what the domain is and where the sauce actually lives (which is often non-obvious; e.g. for pixel art the sauce is on Twitter/blogs, not YouTube)
2. **"Start here" sources** — 3–8 canonical operators/teachers/practitioners, each with:
   - Name
   - URLs (primary site, secondary like Patreon/Twitter, YouTube channel if relevant)
   - One-line description of *what makes them worth mining*
   - **Ingestion notes** — how to actually consume their content (YouTube `sync.py`? WebFetch their blog? Frame-extract a video? Read their Patreon archive?)
   - **Local corpus path** (if applicable) — the absolute on-disk path to the downloaded transcripts, e.g. `~/Kanna/youtube-scraping/superwall-podcast-transcripts/plain-text/`. So an agent can `cat` the corpus directly without re-deriving the path from the ingest command.
   - **Transcript quirks** (optional) — known auto-caption typos for this source that should be normalized when quoting (e.g. `payw wall` → `paywall`).
3. **Adjacent / supporting sources** — communities, tools, conferences, secondary voices
4. **Domain-specific gotchas** — what to skip, what's outdated, what's controversial, what looks like sauce but isn't
5. **Common questions this topic answers well** — so future agents can pattern-match

## Current topics

- [`apps.md`](apps.md) — building, monetizing, and growing consumer mobile apps
- [`ugc.md`](ugc.md) — user-generated content as a marketing/growth channel
- [`pixel-art.md`](pixel-art.md) — pixel art technique, tutorials, and old-school mastery
- [`design-thinking.md`](design-thinking.md) — lateral thinking, analogical reasoning, mental models, and the IDEO-style design-thinking method (the meta-process layer for `skills/analogous-sauce/`)

## Naming convention

- Lower-case kebab-case for file names: `pixel-art.md`, not `PixelArt.md` or `pixel_art.md`
- One topic per file
- File name should be a short noun phrase, not a question

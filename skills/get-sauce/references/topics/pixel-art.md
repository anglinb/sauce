# Topic: Pixel Art

Pixel art is the rare topic where the sauce is NOT on podcasts or YouTube transcripts. It lives in:

1. **Annotated step-by-step image breakdowns** posted to Twitter/X and personal blogs
2. **Patreon and itch.io archives** where artists drop multi-year tutorial collections
3. **Specific frames inside YouTube tutorial videos** — sometimes you literally need to see a frame to understand a technique (see `references/frame-extraction.md`)

This means `sync.py` (which is built for talking-head podcast transcripts) is the *wrong* primary ingestion tool here. Default to `WebFetch` for blogs, screenshots/saved images for Twitter threads, and `yt-dlp` + `ffmpeg` for specific video frames.

## Start here

### Slynyrd (Ray Loring) — `blog, x-account, patreon`
- **Primary site:** `slynyrd.com` — the "Pixelblog" catalogue at `slynyrd.com/pixelblog-catalogue` is the single most generous free pixel-art curriculum on the internet
- **X:** `x.com/rayslynyrd`
- **Patreon:** `patreon.com/slynyrd` (5,200+ patrons, commercial-use assets, downloadable tutorial files)
- **Why:** Annotated step-by-step technique breakdowns — textures, palettes, anti-aliasing, animation, UI/UX in pixel art. Reads like the textbook nobody else wrote. Author of "Pixel Logic" (paid PDF on his site).
- **Ingest:** `WebFetch` individual `slynyrd.com/blog/...` pixelblog entries. They're standalone essays with embedded GIFs — text + image references. For the Patreon archive, the user needs to log in; the agent can't.
- **Best entry points:** Start with `pixelblog-1-color-palettes`, `pixelblog-2-texture`, `pixelblog-5-back-to-basics`.

### Pedro Medeiros / Saint11 — `blog, x-account`
- **Primary site:** `saint11.art` (was previously `saint11.org` — now redirects)
- **X:** `x.com/saint11`
- **Bluesky:** `bsky.app/profile/saint11.art`
- **Why:** Lead artist on **Celeste** and **TowerFall** (Coldblood Inc). 79+ free pixel-art tutorials, each a single annotated 512×512 image you can save and study. Currently making **Neverway**.
- **Ingest:** `WebFetch` `saint11.art/blog/pixel-art-tutorials/` for the index, then fetch each tutorial. Each tutorial *is* an image — the text-rendering models can describe it, but for actual reference you should download the image (right-click save or `curl` the asset URL).
- **Best entry points:** "Jump!" (tutorial #79), the beginner-series articles, the pixel art glossary.

### MortMort — `youtube, x-account`
- **YouTube:** `youtube.com/channel/UCsn9MzwyPKeCE6MEGtMU4gg`
- **Gumroad:** `mnrart.gumroad.com` (paid asset packs + courses)
- **Why:** The best YouTube channel for pixel-art technique tutorials at the beginner-to-intermediate level. Tool-heavy (Aseprite, Blender). Entertaining, well-produced, full step-by-step screen recordings.
- **Ingest:** `sync.py add mortmort "<channel-url>" ~/Kanna/youtube-scraping/mortmort-transcripts` — but be aware: pixel-art YouTube transcripts are LOW signal vs. transcripts of business podcasts. The visual demonstration *is* the sauce. **You will almost certainly need `references/frame-extraction.md`** to grab key frames from his tutorials for any technical question.
- **Best entry points:** Aseprite tool walkthroughs, "How to color pixel art" series.

### Henk Nieborg — `portfolio-site, artstation`
- **Primary site:** `henknieborg.nl/portfolio.html`
- **ArtStation:** `artstation.com/goatboy`
- **Why:** Old-school master. Did all visuals (backgrounds, animations, HUD, intro/outro) on **Lionheart** (Amiga, Thalion) and **The Misadventures of Flink** (Genesis/Mega Drive, Psygnosis). Currently doing pixel art for **Xeno Crisis**. His Amiga/Genesis platformer work is foundational — anyone serious about pixel art studies it.
- **Ingest:** `WebFetch` his portfolio. Most of the "sauce" is in *looking at the work* (frame composition, dithering choices, parallax layer design) more than reading commentary — so save key images locally and reference them. Interview articles on `sega-16.com`, `arcadeattack.co.uk`, `retrovideogamer.co.uk`, and `80.lv` capture his technique commentary in text form — fetch those when you need quotable advice.
- **Best entry points:** Lionheart screenshots, Flink screenshots, the 80.lv "Pixel Art Tips & Tricks from Henk Nieborg" interview.

## Adjacent / supporting sources

- **Lospec (`lospec.com`)** — community-curated pixel-art tutorials, palettes, and rules-of-thumb. Pages like `lospec.com/pixel-art-tutorials/author/slynyrd` aggregate individual artists' work. Good for "find me everything by X."
- **Aseprite docs (`aseprite.org`)** — Aseprite is the de facto tool. Not sauce, but technical reference.
- **PixelDailies / Pixel Joint forums** — community challenges that surface emerging artists. Lower-signal than the named artists above.
- **Brandon James Greer (`youtube.com/@BJGpixel`)** — high-effort YouTube tutorials, slower-paced than MortMort.
- **AdamCYounis (`youtube.com/@AdamCYounis`)** — game-art and pixel-art streamer with multi-hour tutorial VODs. Great for watching technique in real time.

## Domain-specific gotchas

- **YouTube transcripts here are mostly useless** — the verbal commentary is "okay, now I'm going to use the dither tool" while the actually-relevant information is what's happening on screen. **Always prefer frame extraction** over transcript text for technique questions.
- **Patreon archives are paywalled.** If the user is a patron, they can pull down archives manually and point you at the local folder. The agent cannot scrape Patreon.
- **Style ≠ technique.** A lot of "pixel art tutorials" online are about a particular aesthetic (NES limits, 4-color, etc.). When the user asks about pixel art generally, prefer the named artists above — they teach the underlying skill, not a single aesthetic.
- **Old-school context matters for Nieborg.** His work was constrained by hardware (16 colors, 4-color sprites, specific tile sizes). When relaying his techniques, flag the constraints so a modern artist doesn't blindly imitate without context.

## Common questions this topic answers well

- "How do I do good textures in pixel art?"
- "How do I pick a palette?"
- "Why does my pixel art look stiff / muddy / amateurish?"
- "What's the difference between AA and dithering?"
- "How did the artist of Celeste / Lionheart / Flink actually approach character animation?"
- "I want to see a specific frame of MortMort's video on X — how?"

## When you need to see a specific frame

For pixel art especially, sometimes the agent or user needs to literally view a specific frame inside a tutorial video — e.g. "show me the exact moment in MortMort's color tutorial where he layers the second shade." Read [`references/frame-extraction.md`](../frame-extraction.md) — it covers downloading the video (or just a segment) and pulling a frame with `ffmpeg`.

## See also

- [`references/frame-extraction.md`](../frame-extraction.md) — when you need a real image, not a transcript
- `references/sources.md` — does not currently include the pixel-art canon; this topic file is the authoritative source

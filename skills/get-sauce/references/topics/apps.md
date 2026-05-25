# Topic: Apps

Building, monetizing, growing, and marketing consumer mobile apps. The sauce here lives almost entirely in podcast interviews with indie app founders and in vertical-product conferences. Blogs and Twitter are noisy; long-form interviews are dense.

## Start here

### Superwall Podcast — `podcast, youtube`
- **Primary:** `youtube.com/playlist?list=PL3XL-MsZorn_Nfi3jrPqQtxDk-kxyaaz8`
- **Why:** Long-form interviews with indie app founders making $100k–$2M/year. Heavy on growth tactics, paywall design, and UGC. The highest-density app-monetization corpus on YouTube.
- **Ingest:** `sync.py add superwall-podcast "<URL>" ~/Kanna/youtube-scraping/superwall-podcast-transcripts`.
- **Local corpus path:** `~/Kanna/youtube-scraping/superwall-podcast-transcripts/plain-text/` (40 episodes, ~390K words as of last sync). Already downloaded — read directly without re-syncing if it's fresh enough.
- **Transcript quirks to normalize:** YouTube auto-captions consistently mangle a handful of technical terms. When quoting, mentally substitute: `payw wall` → `paywall`, `Arpoo` → `ARPU`, `Surf UI` → `SwiftUI`, `Chatt` → `ChatGPT`, `Tik Tok` → `TikTok`. Don't reproduce the typos in your final answer; normalize them.

### Sub Club Podcast — `podcast`
- **Primary:** `subclub.co/podcasts`
- **Why:** Subscription economics, IAP, retention curves, lifecycle marketing. Run by RevenueCat. More B2B/wholesale-energy than Superwall but the IAP analysis is sharper.
- **Ingest:** Search YouTube for "Sub Club podcast" episode list — most episodes are uploaded.

### RevenueCat Blog — `blog`
- **Primary:** `revenuecat.com/blog`
- **Why:** Annual "State of Subscriptions" report has the only credible cross-app benchmarks (paywall conversion %, trial-to-paid, churn). Reference-grade data, not opinion.
- **Ingest:** `WebFetch` individual posts. Don't try to ingest the whole archive — it's huge and most posts are mid.

### Business of Apps Summit (formerly App Promotion Summit) — `conference, youtube`
- **Primary:** `apppromotionsummit.com`
- **YouTube:** `youtube.com/channel/UCg2NMpWp3jI3zYg_R4NZIaQ`
- **Why:** ASO, paid UA, attribution, lifecycle marketing — all from working operators. Strong on the *paid* growth side where Superwall is light.
- **Ingest:** `sync.py add` against the channel URL.

### NGL / Hunter Isaacson talks (Superwall ep 36) — `podcast-episode`
- **Why:** NGL hit 150M MAU using the Instagram graph. The single highest-leverage interview on "what is product-led growth for consumer apps really."
- **Ingest:** Already in superwall-podcast corpus.

## Adjacent / supporting sources

- **Marc Lou (`marclou.com`, `x.com/marc_louvion`)** — indie AI-app shipping, micro-SaaS, Next.js boilerplates. Twitter is where the actual play-by-play happens.
- **Pieter Levels (`levels.io`, `x.com/levelsio`)** — godfather of indie-as-business. Blog posts on revenue transparency are the canonical references.
- **My First Million** — for app *ideas* (not execution). Episodes tagged with "app", "AI app", "consumer", "TikTok" — usually 1–2 sharp tactical observations per ep.
- **Greg Isenberg** — YouTube channel for trending consumer app concepts. Treat as ideation input, not tactical depth.
- **Superwall Blog (`superwall.com/blog`)** — paywall-design case studies; lighter than the podcast but useful for one-off questions.

## Domain-specific gotchas

- **App Store Connect docs are NOT sauce.** They're authoritative but generic. Don't conflate "official" with "operator-grade."
- **"AI app" content is moving fast** — episodes from 2024 are already outdated on tactics (TikTok algorithm has shifted twice since). Cite recency.
- **"50/50 founder-creator splits" is one operator's playbook (Casper / Payout)** — don't generalize it; multiple Superwall guests explicitly reject it.
- **CPM/CPI/ROAS benchmarks vary 5–10× across app categories.** Always cite the operator's category when relaying a number — never strip context.

## Common questions this topic answers well

- "How do I structure my paywall for a new consumer subscription app?"
- "What CPM should I pay UGC creators for a launch?"
- "How do I get my first 10k installs without ad spend?"
- "What conversion rate should I expect for an AI app at $30/year?"
- "Should I run paid ads from day 1?"

## See also

- [`ugc.md`](ugc.md) — overlap is heavy when the question is about app marketing via short-form
- `references/sources.md` — full grep for `app`, `paywall`, `IAP`, `monetization`, `ASO`

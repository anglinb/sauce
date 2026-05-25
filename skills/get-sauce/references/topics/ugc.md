# Topic: UGC (User-Generated Content as a growth channel)

UGC = paying or partnering with creators to make short-form video content (TikTok, Reels, Shorts) that drives installs/signups for your product. The sauce here is very narrowly distributed — maybe a dozen operators in the world have repeatedly hit 100M+ views and lived to write the playbook. Most of them are on the Superwall Podcast or Sub Club. Generic "TikTok marketing" content from influencer-marketing agencies is *not* sauce.

## Start here

### Superwall Podcast — `podcast, youtube`
- **Primary:** `youtube.com/playlist?list=PL3XL-MsZorn_Nfi3jrPqQtxDk-kxyaaz8`
- **Why:** The single best-curated corpus on UGC tactics anywhere. Episodes with Anand (Flame), Dris (Methods/Cluely), Matt (Jenny AI), Jay (Nomad Table), Hunter Isaacson (NGL), Bloom, Dillian (Halo AI) — between them they've shipped 1B+ UGC views and tell you exactly how.
- **Ingest:** `sync.py add superwall-podcast …`.
- **Local corpus path:** `~/Kanna/youtube-scraping/superwall-podcast-transcripts/plain-text/` (40 episodes, ~390K words).
- **Transcript quirks:** auto-caption typos to normalize when quoting — `payw wall` → `paywall`, `Tik Tok` → `TikTok`, `Arpoo` → `ARPU`. Don't reproduce typos in the final answer.

### Sub Club Podcast — `podcast`
- **Why:** Less UGC-specific than Superwall but covers the *measurement* side (attribution, blended CAC) better.
- **Ingest:** YouTube search "Sub Club podcast" → sync.

### My First Million (UGC-tagged episodes) — `podcast, youtube`
- **Why:** Less about how to *make* UGC, more about *seeing the patterns* before they're saturated. Shaan + Sam regularly call winning consumer apps 6 months before MFM-listener saturation hits.
- **Ingest:** `sync.py add my-first-million`. Then filter to episodes whose titles mention "TikTok", "UGC", "creator", "AI app".

### Codie Sanchez — `youtube`
- **Primary:** `youtube.com/@codiesanchez`
- **Why:** Adjacent — she's about Main Street boring-business acquisition, but her short-form playbook is one of the cleanest examples of "B2B can use UGC too." Useful when the question is "but my product isn't a consumer app, does this apply?"

### Greg Isenberg — `youtube, podcast`
- **Primary:** `youtube.com/@gregisenberg`
- **Why:** Ideation-grade. Less "here's a creator-pay structure that works" and more "here are 5 niche UGC patterns you haven't noticed yet." Pair with Superwall for theory-to-practice.

## Adjacent / supporting sources

- **TikTok Creative Center (`ads.tiktok.com/business/creativecenter`)** — official-but-actually-useful: top-performing ads by category. Not sauce, but a reference for what "good" looks like.
- **Business of Apps Summit talks** — see `topics/apps.md`. UGC measurement and post-iOS-14.5 attribution is well covered here.
- **NoiseLab / Nick Weber talks** — 2.5B views/year operator. Find him on Superwall ep 13. The "30¢ install at scale via 50,000 creators" playbook.

## Domain-specific gotchas

- **"Copy this format" advice is contradictory by operator.** Casper (Payout, Superwall ep 6) says "swap numbers, keep structure" works fine. Matt (Jenny AI, ep 21) says frame-for-frame copying *does not work* and you need format-evolution. Resolve by: copy structure, never surface details.
- **Sub-$1 CPM is real but requires infrastructure** — you need batch creator outreach (Methods/Dris uses email-bursts from ~1,000 Gmails). Don't quote "$1 CPM" without that context.
- **Watch-past-3s ≠ conversion.** Targeting watch-time can produce 1M-view duds. Anand (Flame, ep 10) says always check comments for "what's the app?" — if the question's not in the comments, the video isn't converting.
- **TikTok algorithm "fingerprints" Apple IDs** — multiple Superwall guests learned this the hard way. Account-farming requires separate Apple IDs *and* separate proxy IPs per phone.
- **Don't say the name of the app aloud in a UGC video.** Casper (Payout, ep 6) — universal across multiple operators.

## Common questions this topic answers well

- "How do indie founders use UGC to scale apps to seven figures?"
- "What's a fair creator pay structure for app UGC?"
- "How many creators do I need to launch a UGC campaign?"
- "What hook formats are working on TikTok for AI apps?"
- "How do I take winning organic creatives and run them as paid ads?"

## See also

- [`apps.md`](apps.md) — heavy overlap when the question is consumer-app marketing
- `references/sources.md` — full grep for `UGC`, `TikTok`, `viral`, `creator`

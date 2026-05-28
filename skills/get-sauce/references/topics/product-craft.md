# Topic: Product Craft (How the Best Companies Plan, Build, and Ship)

How excellent product companies actually plan features, build them, iterate, and release them to the world. **Not** product-led *growth* (PLG = freemium GTM motion — see `virality.md` for that). This topic is about the upstream craft: roadmap process, prototyping, dogfooding, design-partner programs, and the staged-release discipline that lets companies ship ambitious products without breaking trust — Stripe's Private Preview → Public Preview → GA pattern, Anthropic/OpenAI's "research preview" as a release strategy, Linear's no-PM cycles, Vercel's preview-deployment culture.

The sauce lives in three pockets:

1. **Company-specific shipping playbooks** — Stripe (release phases), Linear (the Linear Method), Figma (multiplayer-first, big-vs-little feature decentralization), Notion (engineers-as-PMs, horizontal product), Vercel (preview-deployments-as-product-process), Anthropic/OpenAI (research preview as a release stage). These are the canonical living examples.
2. **Frameworks** — Amazon's Working Backwards / PR-FAQ, Basecamp's Shape Up (six-week cycles, appetite, betting), Marty Cagan / SVPG (the product trio), Teresa Torres (continuous discovery / opportunity solution trees), Pixar's Brain Trust (iteration/critique culture).
3. **The voices** — Lenny Rachitsky (as the central nervous system), Shreyas Doshi (principles), John Cutler (org systems thinking), Julie Zhuo (design-as-leadership), Kunal Shah (Delta-4), Paul Graham ("Founder Mode" via Brian Chesky).

The frameworks contradict each other — Linear's "no PMs, no A/B tests, no OKRs" is the opposite of Cagan's "product trio." Both ship great product. The right answer depends on org size, founder taste, and product category. Read multiple before forming a view.

## Start here

### Stripe — release phases as a discipline — `documentation, blog, podcast-episode`
- **Primary (the doc the user is asking about):** `docs.stripe.com/release-phases` — Stripe's own definition of **Private Preview** (invite-only, breaking changes expected, direct product-team support) → **Public Preview** (open opt-in, some breaking changes) → **GA** (stable, no breaking changes). The canonical primary source.
- **Companion blog:** `stripe.dev/blog/introducing-stripes-new-public-preview-release-channel` — the team explaining the mechanics: `.preview` API versions, beta SDK suffixes, why opting-in matters.
- **Roadmap in practice:** `stripe.com/roadmap` — items publicly tagged `[Q1, private preview]` / `[Q2, public preview]` / `[Q3, GA]`. Look here to see the pattern *in motion*, not just defined.
- **Versioning policy:** `docs.stripe.com/sdks/versioning` — companion doc on how preview vs. GA versions evolve.
- **Jeff Weinstein (Stripe Atlas product lead) on Lenny's Podcast — "Building product at Stripe: craft, metrics, and customer obsession"** — `lennysnewsletter.com/p/building-product-at-stripe-jeff-weinstein`. The most operational "how we ship" Stripe episode on Lenny's. Study Group, customer obsession, craft.
- **David Singleton (Stripe CTO) — "Extreme Product Design" on SaaStr Podcast #636** — `saastr.com/extreme-product-design-building-things-people-actually-use-with-stripe-cto-david-singleton/`. The 24-hour user feedback loop, EPD framework, five principles. Closest thing to the CTO publicly explaining Stripe's iteration cadence.
- **Inside Stripe's Engineering Culture (Pragmatic Engineer)** — `newsletter.pragmaticengineer.com/p/stripe` (Part 1) and `newsletter.pragmaticengineer.com/p/stripe-part-2` (Part 2 — API-change review process, directly relevant to how previews get hardened). Subscriber-gated but worth it.
- **Building Products at Stripe (Ken Norton + Michael Siliski)** — `bringthedonuts.com/essays/building-products-at-stripe/`. Defines Stripe "product shaping" — strategy → PRD written as user stories with curl snippets. Highly cited.
- **Patrick Collison on Dwarkesh Podcast** — `dwarkesh.com/p/patrick-collison`. Full transcript on site. Patrick on multi-decade APIs, beauty, Stripe culture.
- **Stripe Operating Principles** — `stripe.com/jobs/culture` (Users First, Create with Craft and Beauty, Move with Urgency and Focus).
- **Stripe Sessions** — already in master registry as conference. Pattern-in-practice anchor: `stripe.com/blog/everything-we-announced-at-sessions-2026` enumerates launches by preview stage (e.g., Stripe Projects launching in private preview with thousands on waitlist + 32 design-partner providers).
- **Cheeky Pint (John Collison's podcast)** — `cheekypint.transistor.fm/`. Reverse-direction sauce: watch how John probes other founders on shipping process.
- **Increment magazine archive** — `increment.com/`. Stripe's quarterly engineering magazine, 19 issues from Apr 2017 – Nov 2021. Free archive; reflects the taste even when not directly about Stripe.

### Linear — the Linear Method — `blog, podcast, publication`
- **Primary:** `linear.app/method` — Linear's public articulation of their build philosophy: cycles, specs, taste, opinionated software. The canonical written source.
- **Karri Saarinen on Lenny's Newsletter — "How Linear builds product"** — `lennysnewsletter.com/p/how-linear-builds-product` (Sep 26, 2023). Deep-dive into Linear's no-PM, taste-over-metrics, no-A/B-tests model. Widely cited canon.
- **Karri on Lenny's Podcast — "Inside Linear: Building with taste, craft, and focus"** — `lennysnewsletter.com/p/inside-linear-building-with-taste`. Audio companion.
- **Karri on First Round In Depth — "Why craft and focus still win"** — `review.firstround.com/podcast/inside-linear-why-craft-and-focus-still-win-in-product-building/`. Sharper on hiring + quality bar.
- **Karri's personal site** — `karrisaarinen.com/`. Essays: "Starting Linear," "On Taste, Jiro's Dream," "Your Product Needs a Soul."
- **Tuomas Artman (Linear CTO) on Pragmatic Engineer** — `newsletter.pragmaticengineer.com/p/linear`. The engineering-side counterpart: sync engine, quality, low-process culture.
- **Tuomas on localfirst.fm #15** — `localfirst.fm/15`. Deep technical/process talk on Linear's sync engine and rethinking MVPs.

### Figma — multiplayer + decentralized big-vs-little — `podcast`
- **Yuhki Yamashita (Figma CPO) on Lenny's Podcast — "An inside look at how Figma builds product"** — `lennyspodcast.com/an-inside-look-at-how-figma-builds-product-yuhki-yamashita-cpo-of-figma/`. The canonical Figma process episode: operationalizing quality, against OKRs, storytelling-as-PM.
- **Dylan Field on Lenny's Podcast (live at Config 2024) — "Intuition, simplicity, and the future of design"** — `lennysnewsletter.com/p/dylan-field-live-at-config`. Dylan on taste, intuition, and product decision-making.
- **Sho Kuwamoto (Figma VP Product) — "What working at Figma taught me about customer obsession"** — `lennysnewsletter.com/p/what-working-at-figma-taught-me-about`. **Big-vs-little features framework** — decentralized small-feature decisions, deliberate big-feature process. Most operationally useful Figma write-up.
- **Figma Config** — already in master registry as conference. Anchor playlist for design-and-product talks.

### Notion — engineers do product, horizontal — `podcast`
- **Ivan Zhao (Notion CEO) on Lenny's Podcast — "Notion's lost years"** — `lennysnewsletter.com/p/inside-notion-ivan-zhao`. Ivan rarely podcasts; covers staying small to move fast, horizontal product philosophy, McLuhan-influenced tool-shaping worldview.
- **Akshay Kothari (Notion COO) on Stanford Product Pathways** — `productpath.stanford.edu/leaders/akshay`. The operational counterpart: how Notion scales without traditional PMs.

### Vercel — preview deployments as culture — `podcast`
- **Guillermo Rauch on Lenny's Podcast — "Everyone's an engineer now"** — Lenny's episode covering v0, preview-driven culture, democratizing builders. (Apple/Spotify: `open.spotify.com/episode/4vZMjciYdBflVaqtEif1ZB`.)
- **Guillermo on Accel — "Bold visions delivered incrementally"** — `accel.com/podcast-episodes/vercels-guillermo-rauch-on-bold-visions-for-the-future-delivered-incrementally`. The most explicit articulation of Vercel's incremental-shipping / preview-deploy culture. **Required if you want to understand "preview-deployments as product process," not just as a CI feature.**

### AI labs — "research preview" as a release stage — `blog, policy-document`
- **OpenAI — "Introducing ChatGPT"** — `openai.com/index/chatgpt/`. The original "research preview" framing; canonical text for *iterative-deployment-as-strategy*. The launch post that legitimized "research preview" as a release stage in modern AI product culture.
- **Anthropic — Responsible Scaling Policy (v3)** — `anthropic.com/responsible-scaling-policy`, announcement: `anthropic.com/news/responsible-scaling-policy-v3`. The staged-release / safety-gated deployment philosophy in its most articulated form. Pair with the ChatGPT launch post to see two adjacent versions of "release in stages, learn in public."
- **Caveat:** the AI-lab "research preview" framing is *partly* genuine staged-release and *partly* expectation-setting / legal cover. Don't take the framing fully at face value — there's product-positioning work happening too.

### Amazon Working Backwards / PR-FAQ — `book`
- **Book:** *Working Backwards: Insights, Stories, and Secrets from Inside Amazon* by Colin Bryar & Bill Carr (2021) — `workingbackwards.com/`. The definitive insider account of the PR-FAQ ritual: write the press release *before* you build the thing. Six-pagers read in silence at the start of meetings.
- **Caveat:** PR-FAQ works because Amazon's culture forces silent reading + writing 6-pagers. Without that ritual it becomes a checkbox. Don't cargo-cult the artifact without the ritual.

### Basecamp / Shape Up — `book, talk`
- **Free book online:** `basecamp.com/shapeup`. Ryan Singer's methodology — six-week cycles, appetite-driven scoping (not estimation), betting table, shaping. The clearest articulation of "bet on bets, not on backlog."
- **Ryan Singer with Lenny (2025)** — `youtube.com/watch?v=GF-yUANql0c`. The current-era walkthrough.
- **Ryan Singer's site:** `ryansinger.co/`.
- **Caveat:** Shape Up requires actually *pausing* between cycles. Most companies adopt the six-week cycle and skip the cooldown — that's not Shape Up, that's just a 6-week sprint. The cooldown is the methodology.

### Marty Cagan / SVPG — `book, blog`
- **Primary:** `svpg.com/`. Start-here essay collection: `svpg.com/product-management-start-here/`. Vision-defining piece: `svpg.com/a-vision-for-product-teams/`.
- **Books:** *Inspired*, *Empowered*, *Transformed* — `svpg.com/books/`. The **product trio** (PM/design/eng working together) is the SVPG operating model.
- **Why:** The most institutionally adopted modern PM philosophy. Even orgs that don't follow it have read it.
- **Caveat:** The "product trio" (Cagan) and "no-PM" (Linear) are *opposite* prescriptions. Both ship great product. The choice is downstream of org size, founder taste, and product category — not a "right answer."

### Brian Chesky / Airbnb — "Founder Mode" — `podcast, essay`
- **Brian Chesky on Lenny's Podcast — "Brian Chesky's new playbook"** — `lennysnewsletter.com/p/brian-cheskys-contrarian-approach`. The canonical "founder mode" interview (Nov 12, 2023): one roadmap, CEO-as-CPO, ripping up the typical PM structure.
- **Paul Graham — "Founder Mode" essay** — `paulgraham.com/foundermode.html`. The essay that coined the term, anchored on Chesky's YC talk.
- **Caveat:** "Founder Mode" is a real pattern but is anti-correlated with delegating well. Many "founder mode" success stories are survivorship-biased. Read it as a description of a leadership stance, not a universal recipe.

### Teresa Torres — Continuous Discovery Habits — `book, blog`
- **Primary:** `producttalk.org/`. Opportunity Solution Tree canonical post: `producttalk.org/opportunity-solution-trees/`. Book landing: `producttalk.org/continuous-discovery-habits/`.
- **Why:** The reference for weekly customer-interview cadence. The clearest modern articulation of "discovery is a habit, not a phase."

## Adjacent / supporting sources

- **Lenny Rachitsky — Lenny's Newsletter** (already in master registry, but here are the *craft-anchored* evergreens): "How the biggest consumer apps got their first 1,000 users" — `lennysnewsletter.com/p/how-the-biggest-consumer-apps-got`; "Getting better at product strategy" — `lennysnewsletter.com/p/getting-better-at-product-strategy`. The central nervous system of modern PM content. Most of the operator interviews above live here.
- **Shreyas Doshi — Substack** — `shreyasdoshi.substack.com/`. Anchor essays: `shreyasdoshi.substack.com/p/influence-power-and-product-management`, `shreyasdoshi.substack.com/p/the-product-builders-true-journey`. Frameworks: Impact/Execution/Optics, LNO tasks, 10-30-50, Know/Think/Feel/Do.
- **John Cutler — The Beautiful Mess** — `cutlefish.substack.com/`. Anchor guest post on Lenny's: `lennysnewsletter.com/p/what-differentiates-the-highest-performing`. Systems-thinking lens on product orgs — rare voice covering org dynamics, not features.
- **Julie Zhuo — The Year of the Looking Glass** — `juliezhuo.com/`, Medium: `medium.com/the-year-of-the-looking-glass`. Design-as-leadership; how to grow design orgs.
- **Kunal Shah — Delta-4 theory** — `kunalshahtalks.com/post/kunal-shah-delta-4-theory`. Best long-form: `lennysnewsletter.com/p/kunal-shah-on-winning-in-india-second`. Sharp principles: Delta-4, second-order thinking, UBP > USP.
- **Casey Winters** (already added in `virality.md`). Craft-anchored picks: `caseyaccidental.com/p/the-strategy-vs-product-mindset`, `caseyaccidental.com/p/caseys-guide-to-finding-product-market-fit`.
- **Brian Balfour** (already registered) — `brianbalfour.com/four-fits-growth-framework`. Channel-product-market-model fits as the strategic lens upstream of craft.
- **GitLab Handbook — Product Development** — `handbook.gitlab.com/handbook/product-development/`. Most useful section: Product Development Flow — `handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/`. Radically transparent process, publicly auditable. Treat as a reference, not a model to copy.
- **Pixar Brain Trust / Ed Catmull — *Creativity, Inc.*** — HBR canonical: `hbr.org/2008/09/how-pixar-fosters-collective-creativity` (Catmull's own 2008 piece). The iteration/critique culture chapters: "The Braintrust" and "Honesty and Candor." (Already mentioned in `design-thinking.md` but specifically relevant here for *critique rituals*.)
- **Tobi Lütke (Shopify) on The Observer Effect** — `theobservereffect.org/tobi.html`. The richest written interview on Tobi's mental models, meetings philosophy, low-process engineering culture. Plus Knowledge Project #152 "Calm Progress" — `fs.blog/knowledge-project-podcast/tobi-lutke-2/` and #41 "Trust Battery" — `fs.blog/knowledge-project-podcast/tobi-lutke/`.
- **Ken Kocienda — *Creative Selection*** — `creativeselection.io/`. The outside-looking-in canonical text on Apple's demo-driven, "creative selection" process under Jobs. The closest the public ever gets to Apple's interior process.
- **First Round Review** (already registered as publication). Specifically: "How Stripe Built One of Silicon Valley's Best Engineering Teams" — `review.firstround.com/how-stripe-built-one-of-silicon-valleys-best-engineering-teams/` (Greg Brockman on founding-engineer-era hiring + culture).
- **Acquired podcast** (already in master registry) — particularly the NVIDIA, TSMC, and ARM episodes for *long-arc product strategy*; the LVMH episode for *status/scarcity-as-product*. Not direct craft, but the Acquired "playbook" segments often surface craft lessons.

## Domain-specific gotchas

- **"Private preview" / "research preview" is a release-pacing tool, not a permission to ship junk.** Stripe gates them on design-partner feedback loops and explicit breaking-change tolerance. Anthropic gates research previews behind safety review (RSP). Don't confuse "we're shipping a preview" with "we're shipping unfinished work."
- **The Linear Method is famous for "no PMs, no A/B testing, no OKRs."** Applies cleanly to small, high-taste teams with founder-CEO close to product. Does *not* trivially port to enterprise SaaS with 50 PMs. Don't apply prescriptively to orgs over ~50 product people.
- **Shape Up requires the org to actually pause/reflect between cycles.** Most companies adopt the six-week cycle and skip the cooldown — that's not Shape Up, that's just a 6-week sprint. The cooldown is load-bearing.
- **The product trio (Cagan) and no-PM (Linear) are opposite prescriptions.** Both ship great product. Choice is downstream of org size, founder taste, product category. Not a debate to "resolve."
- **PR-FAQ at Amazon assumes silent-reading meetings + 6-pager culture.** Without that ritual, the PR-FAQ becomes a checkbox. Don't cargo-cult the artifact.
- **"Founder Mode" is anti-correlated with delegating well.** It's a leadership stance, not a universal recipe. Many stories are survivorship-biased.
- **Vercel's "preview-deployments-as-product-development" works because frontend artifacts are visually self-evident.** Doesn't trivially port to backend services or pure-data products where the "preview" needs framing/narration.
- **AI labs' "research preview" framing is partly expectation-setting / legal cover.** Don't take it fully at face value. The pattern is real (staged release) *and* the framing is positioning.
- **"Stripe ships 1,300 PRs a week" is a consequence of culture, not a goal to copy.** Engineering throughput without taste produces a mess.
- **Beware "company X does Y therefore we should too."** Linear/Figma/Stripe processes work *given* their hiring bar, founder taste, and product category. Process is downstream of those; copying process without copying upstream conditions usually fails.
- **Continuous discovery (Torres) vs. one-roadmap (Chesky) are not actually opposites** — they answer different questions. Torres: *how do we keep learning from customers?* Chesky: *how do we maintain coherence at scale?* You can do both. Treat them as orthogonal.

## Common questions this topic answers well

- "How does Stripe do private previews?"
- "What's the Linear Method and should I copy it?"
- "How does Figma build product without traditional PMs?"
- "What's Shape Up and how does it differ from sprints?"
- "What's the working-backwards / PR-FAQ process?"
- "How does Brian Chesky's 'founder mode' work in practice?"
- "Should I use continuous discovery (Torres) or one-roadmap (Chesky)?"
- "How do I structure a beta / design-partner program?"
- "How do the AI labs decide when to ship a research preview?"
- "What's the canonical book on product management?"
- "How do I ship like Stripe — what's the actual process?"
- "What does 'craft' even mean in a product context?"
- "How do I design a critique ritual that makes the work better, not worse?"

## See also

- [`apps.md`](apps.md) — for app-specific shipping discipline
- [`virality.md`](virality.md) — craft and viral mechanics share a common ancestor (a product worth sharing), but the literatures rarely cross-reference each other
- [`cold-outbound.md`](cold-outbound.md) — design-partner programs are a *specific cold outreach motion* worth running well; the operators in that file know how
- [`design-thinking.md`](design-thinking.md) — much of "product craft" is downstream of *analogical inspiration* (Chesky's "Disney Cruise" Airbnb workshop, the Pixar Brain Trust, IDEO process). When craft feels stale, go there
- `references/sources.md` — full grep for `product`, `craft`, `PM`, `design`, `process`, `Stripe`, `Linear`, `Figma`, `engineering-culture`

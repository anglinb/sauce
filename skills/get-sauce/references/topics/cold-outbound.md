# Topic: Cold Outbound (Cold Email + LinkedIn DMs)

Systematically reaching strangers — usually by email or LinkedIn DM, sometimes by phone — to start sales conversations. The sauce here is **deeply fragmented** because the practice splits into three almost-incompatible schools that constantly argue with each other:

1. **The classic SDR-org canon** — Aaron Ross (*Predictable Revenue*), Trish Bertuzzi (*The Sales Development Playbook*), Pete Kazanjy (*Founding Sales*). The vocabulary every modern sales org inherited: SDRs, sequences, cadences, ICP, the funnel.
2. **The modern operator-by-example school** — Josh Braun, Jason Bay (Outbound Squad), Will Allred (Lavender), Belal Batrawy, Sam Nelson. Daily teardowns, public benchmark data, language-pattern obsessed. Mostly publishes on LinkedIn and YouTube.
3. **The infrastructure + AI-augmented wave (2024-2026)** — Smartlead, Apollo, Lavender, Clay, Botdog, Jordan Crawford (Blueprint GTM), Adam Robinson (RB2B). Domain warmup, mailbox rotation, signal-based triggers, LLM-personalization at volume. This is where the action is *right now*.

Plus a sidecar: the **founder-led / LinkedIn-as-distribution school** — Justin Welsh, Daniel Priestley, Alex Hormozi's *$100M Leads* — for indie founders and high-ticket consultants where the playbook is "you, posting publicly, then DMing inbound interest" rather than 1,000-account sequenced outbound.

The three schools **disagree** on the most important question (personalize hard vs. send volume) and the right answer depends on AOV, list quality, and team capacity. Read all three before forming a view.

## Start here

### Botdog blog — `blog`
- **User-anchor:** `botdog.co/blog-posts/linkedin-outreach-strategy` (Nov 2025) — full LinkedIn outreach strategy: profile optimization → ICP → tooling → 70-word-max messages → ChatGPT personalization prompts → follow-up cadence. Practical end-to-end playbook.
- **Companion data piece:** `botdog.co/blog-posts/linkedin-acceptance-rates` — **16,492 invitations analyzed**. Key finding: 88% of accepts happen within 7 days; blank connection requests *outperform* requests with notes. Rare primary data on a topic everyone speculates about.
- **Sequence playbook:** `botdog.co/blog-posts/linkedin-outreach-sequence-2026` — current cadence + acceptance-trigger logic.
- **Why:** Botdog is one of a handful of LinkedIn-automation vendors publishing operator-grade content backed by their own platform data. Treat the blog as a primary source on LinkedIn DM mechanics, not as marketing.
- **Ingest:** `WebFetch` individual posts. No YouTube corpus — text-only.

### Lavender — `blog, vendor-publication`
- **Primary:** `lavender.ai/blog`
- **Anchor:** `lavender.ai/blog/building-your-own-sales-email-benchmarks` — Lavender's **231,818-email benchmark report**. Department-level reply rates, copy-pattern impact data. 20.5% reply rate average for Lavender users vs. the 3-5% industry baseline from Apollo.
- **Method essay:** `lavender.ai/blog/how-to-build-a-cold-email-personalization-process` — the canonical "personalization school" essay.
- **Why:** The only operator publishing reply-rate data at billions-of-emails scale with quantified findings (e.g., "informative tone reduces replies 26%"). Will Allred (Lavender COO) does daily public teardowns on LinkedIn — `linkedin.com/in/williamallred/`.

### Jason Bay — Outbound Squad — `podcast, youtube`
- **Primary:** `outboundsquad.com`, podcast: `outboundsquad.com/podcast/`
- **Anchor episode:** "Analyzing 85M+ cold emails to find what's working" — `outboundsquad.com/podcast/jason-bay-393`
- **Why:** Trained 20k+ reps. Data-rich tactical playbooks on cold email/cold call openers. Outbound Squad was formerly "Blissful Prospecting" — older content under that name still circulates.
- **Ingest:** YouTube channel for the podcast exists; `sync.py` against it if you want the full corpus.

### Josh Braun — `podcast, blog, course`
- **Primary:** `joshbraun.com`
- **Podcast:** `joshbraun.com/podcast-episodes/` (Inside Selling)
- **Course:** `academy.joshbraun.com/p/badass-b2b-growth-guide`
- **Why:** Anti-pushy-sales canon. "Poke the bear," defusing skepticism, language patterns for cold outreach that don't sound like sales. Best source when the user's question is "my cold emails sound like cold emails — how do I fix that?"

### Aaron Ross — *Predictable Revenue* — `book, blog`
- **Primary:** `predictablerevenue.com`
- **Book:** *Predictable Revenue* (2011) — the genesis text. Coined "Cold Calling 2.0" at Salesforce: specialized prospectors (SDRs as a role), referral-based intro emails, the math of outbound pipeline.
- **Guide:** `predictablerevenue.com/guides/outbound/`
- **Why:** Every modern SDR org's org chart is a direct descendant of this book. Required reading before disagreeing with it.

### Trish Bertuzzi — Bridge Group — `book, blog`
- **Primary:** `bridgegroupinc.com`, blog: `blog.bridgegroupinc.com`
- **Book:** *The Sales Development Playbook* (2016) — TOPSSD framework (Strategy, Specialization, Recruiting, Retention, Execution, Leadership).
- **Why:** The most authoritative operator on *building and managing* an SDR organization. Benchmark data from hundreds of B2B teams. Best source when the question is "how should I structure my outbound team?" rather than "what should my email say?"

### Pete Kazanjy — *Founding Sales* — `book, community`
- **Primary:** `foundingsales.com` (full book free online), `foundingsales.com/table-of-contents`
- **Why:** The definitive founder-led-sales handbook. Free. Foundational 0→1 text for any founder who has to do their own sales before hiring AEs. Pete also runs **Modern Sales Pros** — 16k-member invite-only community for sales ops/leadership.

### Jordan Crawford — Blueprint GTM — `newsletter, podcast-episode`
- **Primary:** `blueprintgtm.com`, Substack: `edge.blueprintgtm.com`
- **Anchor episode:** GTMnow ep. 133 — `gtmnow.com/gtm-133-build-your-ai-outbound-machine-with-chatgpt-jordan-crawford/`
- **Why:** Pioneered signal/data-led outbound — job-board scraping, "Permissionless Value Prop" (PVP), "Permissionless Qualification Score" (PQS). The closest thing to a canonical "this is how outbound changed with LLMs" operator. Openly critical of generic intent data.

### Alex Hormozi — *$100M Leads* — `book, youtube`
- **Primary:** `acquisition.com/books/leads`, YouTube: `youtube.com/@AlexHormozi`
- **Anchor episode:** The Game podcast ep. 590 — Part 5: Cold Outreach
- **Why:** "Core 4" framework places cold outreach alongside warm/content/paid as one of four lead-gen primitives. Volume-first, mass-market lens — closer to high-ticket coaching than enterprise SaaS, but the chapter on cold outreach mechanics is unusually direct.
- **Caveat:** Hormozi's tactics assume a B2C-ish high-ticket offer (coaching, agency services). Don't blindly apply to enterprise software.

### Justin Welsh — `newsletter, course`
- **Primary:** `justinwelsh.me`
- **Anchor product:** The LinkedIn Operating System course — `learn.justinwelsh.me/linkedin`
- **Newsletter:** "Saturday Solopreneur"
- **Why:** Built $8M+ solo using LinkedIn organic. The LOS course is the canonical LinkedIn-as-distribution playbook for founders/solopreneurs. **Not** about cold DMs — about *inbound generated from public posting* — but it's the right reference when the user's "cold outbound" question is really "I'm a solo founder, how do I get B2B attention." Pair with Daniel Priestley (`danielpriestley.com`, *Key Person of Influence*) for the high-ticket-consulting angle.

## Adjacent / supporting sources

- **Apollo.io** — `apollo.io/blog`, `apollo.io/academy`. Biggest free B2B database + heavy benchmark content. Reply-rate baseline (3-5%) widely cited — `apollo.io/insights/whats-the-expected-reply-rate-for-a-well-run-outbound-cold-email-campaign`.
- **Smartlead.ai** — `smartlead.ai/blog`. Infra-first POV: multi-mailbox rotation, warmup, deliverability *first*, copy *second*. Cornerstone: `smartlead.ai/blog/email-deliverability-guide` + `smartlead.ai/blog/spf-dkim-dmarc`.
- **Instantly.ai** — `instantly.ai/blog`. Agency-volume playbooks: dedicated domains, 30-day warmup cadences, AI reply management. `instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/`.
- **Quickmail** — `quickmail.com/blog`. Built by deliverability obsessives. Anchor: `quickmail.com/cold-email/deliverability`.
- **Adam Robinson / RB2B** — `newsletter.rb2b.com/p/the-cold-email-system-behind-42-of-our-revenue` (transparent breakdown of 300K+ sends/month) and `newsletter.rb2b.com/p/3-words-max-the-new-rules-of-cold-email-that-print-money` (how Google's 2024 AI spam filters killed previously-working copy). Closest thing to a public "burner domain" practitioner essay.
- **Clay** — `clay.com/blog-category/outbound-plays`. Operator-grade plays for the data-enrichment + AI-personalization workflow.
- **Common Room** — `commonroom.io/product/signals/`. Signal-based outbound vendor. **Free reference:** the 100+ Signals spreadsheet co-curated with Leslie Venetz (find via Common Room blog).
- **Warmly** — `warmly.ai/p/article/how-to-start-signal-based-marketing-from-zero-to-pipeline`. Website-deanonymization + signal-based trigger-event playbook.
- **HeyReach** — `heyreach.io/blog`. Agency-focused LinkedIn multi-account automation.
- **PhantomBuster** — `phantombuster.com/blog/outbound-sales/linkedin-outreach-guide/`. Most-trafficked LinkedIn automation primer; treat as 101-level.
- **Sam Nelson** — `sdrleader.com`, Substack `samnelson.substack.com`. Ran Outreach's SDR org; "triple tap" sequencing concept.
- **Belal Batrawy** — `linkedin.com/in/belbatrawy`, training arm `learntosell.io`. "Mic Drop Method" cold-call opener. **Note:** "Death to Fluff" is a hashtag/community he leads, not a standalone domain.
- **Kyle Coleman** — `linkedin.com/in/kyletcoleman/`, Copy.ai author page `copy.ai/author/kyle-coleman`. Ex-Clari SDR→CMO, now CMO at Copy.ai. The GTM-AI intersection voice.
- **GTMnow (formerly Sales Hacker)** — `gtmnow.com`. The OG B2B-sales-media flywheel. Max Altschuler's *Hacking Sales* (2016) is the canonical "modern outbound stack" text — `gtmnow.com/hacking-sales/`.
- **Pavilion (Sam Jacobs)** — `joinpavilion.com`. Paid leader community; sister to GTMnow culturally. The closed-door playbook side of the B2B sales conversation.
- **Outreach blog** — `outreach.ai/resources/blog`. First-party content from the largest sales-engagement platform. Cadence theory canon: `outreach.ai/resources/blog/sales-cadence`.
- **Salesloft blog** — `salesloft.com/resources/blog`. Counterweight to Outreach; "Cadence" mental model, signal-based prospecting via Rhythm/Conductor AI.
- **Growth Unhinged (Kyle Poyar) — "Outbound playbook for 2025"** — `growthunhinged.com/p/an-outbound-playbook-for-2025`. Widely-shared synthesis essay on the AI-outbound inflection.

## Domain-specific gotchas

- **The personalization-vs-volume debate is real and unresolved.** Lavender / Will Allred argue for 50-200 hyper-researched emails/day with 20%+ reply rates. Smartlead / Adam Robinson / Vaibhav Namburi argue for 1,000-5,000 lightly-personalized sends/day with 1-3% reply rates but 10x absolute conversations. **Neither is wrong** — the right answer depends on AOV (high AOV justifies hyper-personalization; low AOV requires volume), list quality (clean = lower volume threshold), and team capacity. Read both schools before recommending one.
- **The 3-5% reply rate is the realistic baseline** (Apollo's platform data). 20%+ is achievable but requires Lavender-grade personalization or extreme list quality. If someone quotes a number outside 1-20%, push back.
- **Post-2024 Google/Microsoft spam rules changed the game.** Authentication (SPF/DKIM/DMARC) is non-negotiable. Domain warmup, inbox rotation, low bounce rates (<2%) are now table stakes, not optimizations. The "spray and pray from one Gmail" era is over. Smartlead's `spf-dkim-dmarc` guide is the primer.
- **LinkedIn enforces invitation caps** (~100-200/week safely before account flags). Botdog's `linkedin-acceptance-rates` post documents real platform behavior. Naive automation = account-burning. Botdog/HeyReach/Expandi handle this; rolling-your-own scripts don't.
- **Blank LinkedIn connection requests outperform requests with notes** (per Botdog's 16k-invitation data). Counterintuitive — most LinkedIn-outreach advice still says "always personalize the note." Cite the data, not the folk wisdom.
- **Indie/bootstrapper voices are skeptical of cold outbound.** Pieter Levels, Marc Lou, Arvid Kahl advocate audience-led / SEO / community-led growth instead. If a user is a solo founder asking about cold outbound, surface this disagreement explicitly — Justin Welsh / Daniel Priestley / Hormozi present the "yes, do it" case; Levels/Kahl/Lou present the "no, don't" case. Both are credible.
- **Hormozi's volume-first playbook does not transfer to enterprise SaaS.** $100M Leads assumes a high-ticket B2C-ish offer (coaching, agency, info-product). Enterprise SaaS with $50K+ ACVs almost always wins with ABM-style 50-account focus, not 10,000-email blasts.
- **B2B vs. B2C legal regimes differ.** Cold outbound to *businesses* is largely legal under CAN-SPAM (US) with caveats. Cold outbound to *consumers* triggers GDPR (EU), CASL (Canada), TCPA (US calls/SMS). The playbooks here are B2B-specific. Don't cross-apply.
- **The "Sales Hacker" brand archive is fractured.** Original Sales Hacker (Max Altschuler) → acquired by Outreach (some content moved) → re-acquired and rebranded as **GTMnow** under GTMfund. When citing pre-2022 Sales Hacker content, check whether the URL still resolves.
- **Cold calling is the most-omitted leg of cold outbound.** Email + LinkedIn dominate modern content but voice still works (Bay, Braun, Batrawy all teach it). If a user assumes "cold outbound = cold email only," correct that.
- **Vendor-published blogs (Smartlead, Apollo, Lavender) have a clear bias** toward their own tool category. The data is real; the conclusions skew. Cross-read.

## Common questions this topic answers well

- "How do I do cold outbound as a solo founder?"
- "What reply rate should I expect from cold email?"
- "Should I personalize manually or scale with AI?"
- "What's the modern cold email infrastructure stack (warmup, domains, sequencer)?"
- "How does LinkedIn outreach actually work in 2026?"
- "Is cold outbound dead?"
- "What's the canonical book on building an SDR org?"
- "How do I avoid the spam folder?"
- "Should I add a note to my LinkedIn connection requests or not?"
- "What's a signal-based outbound play?"
- "Is Apollo or Smartlead or Instantly better for my situation?"
- "How do I structure my cold email sequence — how many touches, what cadence?"

## See also

- [`apps.md`](apps.md) — when the question is consumer-app marketing, not B2B sales
- [`ugc.md`](ugc.md) — UGC and cold outbound are the two main paid-distribution alternatives for early-stage B2C/B2B; sometimes the right answer is "neither, do content"
- [`virality.md`](virality.md) — cold outbound is the B2B inverse of consumer virality: paying for distribution one conversation at a time. The "magic number" instinct (Slack's 2k messages) ports here as "first 10 customer conversations" for founder-led sales
- [`design-thinking.md`](design-thinking.md) — when stuck on a sales question, the analogy-from-different-industry move often unlocks (e.g., "how does Costco's membership team handle cold acquisition?")
- `references/sources.md` — full grep for `sales`, `B2B`, `SDR`, `outbound`, `LinkedIn`, `cold-email`, `deliverability`

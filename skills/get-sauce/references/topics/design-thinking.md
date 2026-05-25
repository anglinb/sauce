# Topic: Design Thinking, Lateral Thinking, and Analogical Reasoning

How to *generate* new ideas — not "design" in the visual-UI sense, but the broader craft of structured creativity: lateral thinking, analogy-from-distant-domain, first-principles reframing, mental models, integrative thinking, and the IDEO-style design-thinking method. The sauce here is for people who want to **steal the deep pattern from a totally unrelated industry** and apply it to their own problem.

The sauce lives in three pockets:
1. **Long-running thinker blogs and books** (Munger, de Bono, James Webb Young, Steven Johnson, David Epstein) — these are the canonical "how do good ideas actually get made" texts.
2. **Founder-biography podcasts** (Founders / David Senra, Acquired) — analogies-from-history are the entire point of these shows. Senra explicitly tells listeners "I read these books so you can steal patterns from people who died 100 years ago."
3. **Design-process voices** (IDEO alumni, Stanford d.school, Don Norman, Brian Chesky on cross-industry inspiration) — for the structured method side: how analogies get turned into prototypes.

## Start here

### Founders Podcast (David Senra) — `podcast, youtube`
- **Primary:** `founderspodcast.com`, `youtube.com/@FoundersPodcast`
- **Why:** The single highest-density source on **analogies from history**. Every episode is one founder's biography distilled into transferable patterns. Senra's whole thesis is "the patterns repeat across centuries and industries — Estée Lauder is Steve Jobs is Sol Price is Rick Rubin." If the user is asking "what's analogous to X," this is where to look.
- **Ingest:** `sync.py add founders-podcast "<YouTube channel URL>" ~/Kanna/youtube-scraping/founders-podcast-transcripts`. Episodes are long (~90 min) — corpus gets big fast; consider title-filtering first.
- **Best episodes for cross-domain analogies:** anything on Estée Lauder, Sol Price (Costco precursor), Rick Rubin, Ed Thorp, Claude Hopkins (advertising → applies to everything), Edwin Land (Polaroid), James Dyson, Enzo Ferrari, P.T. Barnum.

### Acquired — `podcast, youtube`
- **Primary:** `acquired.fm`, `youtube.com/@AcquiredFM`
- **Why:** Deep-dive company histories. The "playbook" segment at the end of each episode is explicitly designed for cross-industry transfer. Use when the user is thinking about *an industry* (luxury, payments, retail, gaming) and wants the structural analogy.
- **Ingest:** `sync.py add acquired …`. Same caveat — long episodes, title-filter first.
- **Best episodes for analogies:** LVMH (luxury → status goods), Hermès (scarcity as strategy), Costco (membership flywheel), NVIDIA (platform lock-in), Berkshire (capital allocation), TSMC (specialization), Nintendo (constraint as creativity), Visa (network bootstrapping), Standard Oil (vertical integration).

### Charlie Munger / "Poor Charlie's Almanack" + Farnam Street — `book, blog`
- **Primary:** `fs.blog`, `x.com/farnamstreet`
- **Why:** The canonical "latticework of mental models" school of thinking. Munger's whole pitch: borrow the big ideas from every major discipline (biology, psych, physics, math) and stack them as analogy-filters on every problem. Farnam Street (Shane Parrish) is the curated modern interpreter — long-form essays applying mental models to business and life.
- **Ingest:** `WebFetch` the FS essay archive (`fs.blog/blog`) — index pages, then individual posts. Read the mental-models series and the "inversion" / "second-order thinking" / "Occam's razor" essays.

### Edward de Bono — `book, author`
- **Primary:** `debonogroup.com`, key books: *Lateral Thinking*, *Six Thinking Hats*, *Po: Beyond Yes and No*
- **Why:** Coined "lateral thinking." His method — provocation, random-word stimulus, escape from dominant patterns — is the **most explicitly trainable** analogy technique that exists. The Six Thinking Hats is a structured way to force perspective-shifting on a problem.
- **Ingest:** Book summaries and excerpts via `WebFetch`; structured exercises on debonogroup.com. Skip the modern fluff — go for the 1970s–80s primary texts.

### Steven Johnson — `book, blog, podcast`
- **Primary:** `stevenberlinjohnson.com`, key book: *Where Good Ideas Come From*
- **Why:** Best modern treatment of "the adjacent possible" and how innovations actually emerge — coral-reef ecosystems of ideas, slow hunches, exaptation (one species' feature becoming useful in a totally different context). The vocabulary is exactly what you want for analogy-driven ideation.
- **Ingest:** `WebFetch` blog; book summaries.

### James Webb Young — *A Technique for Producing Ideas* — `book`
- **Why:** 1939, 60 pages, free PDF online. The original "an idea is nothing more or less than a new combination of old elements" thesis. Whole method is: gather raw material → digest → forget → idea appears → cold-light evaluation. Every modern creativity book is a footnote to this.
- **Ingest:** `WebFetch` the PDF or annotated summaries.

### David Epstein — *Range* — `book, podcast, newsletter`
- **Primary:** `davidepstein.com`, newsletter `Range Widely`
- **Why:** The case for generalists, late specialization, and **analogical reasoning as a superpower**. Chapter 4 ("Learning, Fast and Slow") and Chapter 5 ("Thinking Outside Experience") are basically a defense of "look at distant domains to solve your problem." Cites the Innocentive crowdsourcing research showing outsiders solve problems insiders couldn't.
- **Ingest:** `WebFetch` newsletter archive; book summaries; podcast appearances (Lenny, Tim Ferriss, EconTalk).

### IDEO + Tom & David Kelley — `book, blog, youtube`
- **Primary:** `ideo.com/journal`, `dschool.stanford.edu`, books: *Creative Confidence*, *The Art of Innovation*, *Change by Design* (Tim Brown)
- **Why:** The institutional home of "design thinking" as a method — empathize → define → ideate → prototype → test. Their **analogical-research playbook** ("look at how nurses handle handoff in an ICU when designing a software handoff") is the most operationalized version of cross-domain inspiration anywhere.
- **Ingest:** `WebFetch` IDEO Journal and d.school resources page. Books via summaries.

### 99% Invisible — `podcast, youtube`
- **Primary:** `99percentinvisible.org`
- **Why:** Roman Mars + producers spend 30–50 min digging into how *one weird thing* in the built world came to be (the highway sign font, the shape of a fire hydrant, why airline boarding music exists). Pure analogy fuel — every episode is "here's a design decision in a domain you've never thought about." Treat it as **input randomness for de Bono-style provocation**.
- **Ingest:** `sync.py add 99-percent-invisible …`. Or just spot-listen by title — episodes are highly cherry-pick-able.

### Brian Chesky / Airbnb founder talks — `x-account, talks`
- **Primary:** `x.com/bchesky`, his talks at YC, Figma Config, Founders Forum
- **Why:** Most public founder who's vocal about analogical inspiration. The famous "design Airbnb like the Disney Cruise" workshop, "we wanted Airbnb to feel like a magazine, not an app," "we modeled the host onboarding on Apple Genius Bar training." Brian is the modern poster-child for *steal from a totally different industry on purpose*.
- **Ingest:** Hunt YouTube for Chesky talks (Stripe Sessions, YC Startup School, Figma Config, Lenny's pod). `sync.py` the playlists where they exist.

## Adjacent / supporting sources

- **Don Norman — *The Design of Everyday Things*** — foundational; less about analogy specifically, more about the empathic-observation half of design thinking. Pair with IDEO.
- **Roger Martin — *The Opposable Mind*** — "integrative thinking" = holding two contradictory models in mind and synthesizing a third. Adjacent to analogy because the synthesis often comes from a third domain.
- **Ed Catmull — *Creativity, Inc.*** — Pixar's process for protecting nascent ideas from organizational antibodies. Less about *finding* ideas, more about *keeping them alive* once you've borrowed them.
- **Austin Kleon — *Steal Like an Artist*** — pop-format but earnest. Short. Good gateway drug for people who flinch at the word "stealing."
- **Mason Currey — *Daily Rituals*** — what 161 creative people actually did with their days. Use when the analogy you want is *process*, not *product*.
- **Naval Ravikant — `nav.al`, `x.com/naval`** — "first principles," "skills compound," and a recurring riff on borrowing from physics/biology/philosophy into startups.
- **Visualize Value (Jack Butcher) — `x.com/visualizevalue`** — mental-models-as-visual-diagrams. Good for *seeing* an analogy clearly once you've identified it.
- **My First Million (analogy-heavy episodes)** — Shaan and Sam constantly do "what's the [old industry] of [new industry]?" — useful as a corpus of *worked examples* of the move.
- **Andy Matuschak — `andymatuschak.org`** — "tools for thought" essays. Adjacent because the field is itself analogical (spaced repetition borrowed from cognitive psych into note-taking).
- **The Idea Factory (Jon Gertner) — Bell Labs history** — how Bell Labs deliberately mixed disciplines to force analogical transfer. Read as a case study, not a how-to.

## Domain-specific gotchas

- **"Design thinking" as a corporate buzzword has been hollowed out.** Skip anything tagged "design thinking workshop facilitator" or McKinsey/Deloitte derivatives. Stick to primary sources: IDEO founders, d.school, Don Norman.
- **Analogies from history are powerful but the operator was working with different constraints.** Always check: what's the same about the situation, and what's different? Senra's biographies are *patterns*, not playbooks — translate, don't transplant.
- **De Bono's later "Six Hats certification" industry is mostly noise.** Read the original *Lateral Thinking* (1970) and *Six Thinking Hats* (1985). Skip the certified-facilitator content.
- **"First principles thinking" has been claimed by everyone.** When Elon says it, he means *physics-from-the-bottom-up* (cost of raw materials). When startups say it, they often mean "ignore conventional wisdom" — different thing. Both are useful but don't conflate.
- **The analogy is a hypothesis, not a proof.** Drop-shipping ≈ app distribution is a *prompt*, not a conclusion. The skill in analogical reasoning is the second move — "okay, what's the same, what's different, what does the difference *predict*?"
- **Distant analogies (a different industry) outperform near analogies (a competitor)** for novel ideation — this is from the Innocentive / Kettering research David Epstein cites. If a user is stuck, push *further* from their domain, not closer.

## Common questions this topic answers well

- "What's the analogy for [my problem] from a totally different industry?"
- "How do I systematically look for inspiration outside my domain?"
- "What's an old/historical version of this problem and how did people solve it?"
- "What mental models or thinking frameworks should I use here?"
- "Brian Chesky said Airbnb was 'designed like a Disney Cruise' — how do I do that move?"
- "How does IDEO actually find their cross-domain inspiration?"
- "What's the difference between lateral thinking and first-principles thinking?"
- "How do I generate 10 wildly different ideas instead of 10 variations of the same idea?"

## See also

- [`apps.md`](apps.md) — when the analogy needs to land in a consumer-app context
- [`ugc.md`](ugc.md) — UGC is itself an analogy ("traditional advertising but the creator is the channel"); operators here are good at the "borrow from a related discipline" move
- `references/sources.md` — full grep for `mental-models`, `philosophy`, `founders`, `tech-history`, `deep-dives`, `essays`, `design`
- **`skills/analogous-sauce/SKILL.md`** — the **primary consumer** of this topic file. That skill applies a battery of "lenses" (different market, different era, different scale, biological, black-market, childhood, …) to a user's problem and uses *this* topic as its sauce corpus to ground each lens in real practitioner language.

---
name: analogous-sauce
description: Zoom out from the user's problem and find ideas by analogy — "you're thinking about app distribution, let's go look at drop-shipping / record labels / drug dealers / vending machines." Applies a battery of ideation lenses (different market, different era, different scale, biological, black-market, childhood, adjacent profession, reverse, …) to a user's stuck problem, picks 2–4 of the most generative analogies, then invokes the `get-sauce` skill against each analogous domain (and against the curated `design-thinking` topic for meta-process) to pull *real practitioner language* from the analogous world back into the user's problem. Use when the user is stuck on a problem, says "we need a different angle," "give me wildly different ideas," "what would X look like in Y," "how would [other industry] solve this," or wants to break out of category-bound thinking. NOT for execution-level questions (use get-sauce directly) or for "give me 5 variations" within the same frame (use a normal ideation prompt).
---

# Analogous Sauce

## What this skill is for

The user has a problem and is stuck inside the **frame** of their own category. Same-industry inspiration produces same-industry ideas. The move that breaks this is **analogical reasoning** — find a structurally similar problem in a *different* domain, learn from how *that* domain solved it, and translate the pattern back.

Concrete examples of the move:

- *App distribution* → look at **drop-shipping** (logistics-light retail), **record labels** (taste-making distribution), **vending machines** (placement = destiny), **drug dealers** (zero-marketing word-of-mouth), **Hollywood agents** (talent representation as distribution).
- *Onboarding a new user* → look at **fraternity rush week**, **military boot camp**, **a magician's opening trick**, **a therapist's first session**, **how casinos onboard whales**.
- *Pricing a SaaS* → look at **how 17th-century opera houses tiered seats**, **gym membership psychology**, **airline yield management**, **car-dealer financing**, **how the cartels structured drug pricing across distribution layers**.
- *Building a community* → look at **religious congregations**, **AA meetings**, **knitting circles**, **MMO guilds**, **dive bars**, **CrossFit boxes**.

This skill is **NOT** "give me 5 variations of my idea" (that's stuck in the same frame). It's "give me 5 *frames* I haven't considered, grounded in what people in those frames actually said."

## What this skill does, end-to-end

1. **Restate the problem** so we're hunting for the right thing.
2. **Extract the underlying job/pattern** — strip the user's category off.
3. **Apply a battery of lenses** to that abstracted job to generate analogous domains.
4. **Pick 2–4** analogous domains with the user's input.
5. **Pull sauce from the `design-thinking` topic** to ground the analogy-making process itself.
6. **For each picked analogy, invoke `get-sauce`** against that analogous domain.
7. **Synthesize the cross-pollination** — for each analogy, surface 3–6 transferable patterns *with verbatim quotes from operators in the analogous domain*, and translate each into the user's domain.

## Workflow

### Step 1 — Restate the problem and extract the pattern

Ask the user to confirm the problem in one sentence, then **abstract it one level up** — strip the noun-of-art off and re-express it as a generic job.

Examples of the abstraction move:

| User's framing | Abstracted job (the analogy hook) |
|---|---|
| "How do I distribute my app" | "How do I get my product into the hands of strangers at low marginal cost" |
| "How do I price my SaaS subscription" | "How do I extract differentiated value from a heterogeneous customer base for an intangible good" |
| "How do we keep retention up" | "How do I make people keep showing up to a thing they're not contractually required to attend" |
| "How do I get more App Store reviews" | "How do I get satisfied users to publicly testify, when their default is silence" |
| "How do I find my first 100 customers" | "How do I locate the small population of people who care most, before I've earned the right to broadcast" |

Confirm the abstraction with the user before proceeding. The abstraction is the **lens-fitting**: if it's wrong, every analogy will be wrong.

### Step 2 — Apply the lenses

Run the abstracted job through each of the following lenses. For each lens, generate 2–4 candidate analogous domains. Cast wide on this pass — quantity over judgment. We narrow in Step 3.

#### The lens battery

1. **Different-industry lens** — what industry has the same structural job? Apply to *every* major sector: retail, finance, healthcare, education, media, fashion, food, real estate, energy, transport, hospitality, government, military, religion, entertainment, sports.

2. **Different-era lens** — how did people solve this job in 1900? 1500? Antiquity? Often the *constraints were tighter*, so the solutions were leaner. (Roman roads → CDNs. Medieval guilds → SaaS onboarding. Door-to-door encyclopedia salesmen → enterprise SDR motion.)

3. **Different-scale lens** — how does this job play out at three radically different scales? A single person solving it for themselves; a small team / village / shop; a planet-scale system (Google, the US gov, evolution). Each scale reveals different constraints.

4. **Biological / natural lens** — how does *nature* solve this job? Evolution, ecosystems, swarm behavior, immune systems, mycelium networks, predator-prey dynamics. "How does an ant colony do load balancing." Distant analogies from biology are unreasonably effective.

5. **Adjacent-profession lens** — how would a [profession outside the user's world] approach this? A magician, a journalist, a stand-up comedian, a chef, a sniper, an emergency-room nurse, a hostage negotiator, a librarian, a midwife, a tour guide, a Pixar story editor, a museum curator, a wedding planner.

6. **Black-market / illegal-industry lens** — illegal industries can't advertise, can't enforce contracts, can't use mainstream rails — so they evolve *brutally efficient* solutions to distribution, retention, trust, and pricing. Drug dealers, smugglers, counterfeiters, pirate streaming sites, illegal gambling. Treat as inspiration, not endorsement; the constraints are the lesson.

7. **Childhood / amateur lens** — how would a 7-year-old solve this? How would a hobbyist with no resources do it? Strips professional cruft. Often surfaces what's actually load-bearing.

8. **Reverse / inversion lens** (de Bono) — what's the opposite problem, and how is it solved? If the job is "retain users," the opposite is "make a user leave" — study churn from the *attacker* side. If the job is "drive growth," the opposite is "stay tiny on purpose" (cf. 37signals / Pieter Levels).

9. **Game-design lens** — what if this job were a video-game mechanic? What's the player's loop? Where's the reward schedule? What's the boss fight? Game designers have ruthless intuition for the engagement-and-difficulty curves underneath every behavioral problem.

10. **Constraint-flip lens** — what would solve this if [the resource you have most of] were suddenly zero, or [the resource you have least of] were infinite? "What if you had no engineers but infinite money." "What if you had no money but a 6-figure email list." Forces you to find a different solution path.

11. **Genre-shift lens** — re-imagine the problem as a different *narrative* genre. What's the horror-movie version of this onboarding? The romantic-comedy version? The Western? The murder-mystery? Surprisingly generative; uncovers tonal possibilities most product thinking misses.

12. **Anti-domain lens** — pick a domain that has the *most opposite* values to the user's, and look at how *they* handle the analogous job. (Luxury fashion ↔ Wal-Mart. Monastery ↔ Las Vegas. Hospital ICU ↔ stand-up comedy club. Often the contrast reveals what's truly load-bearing vs. just convention.)

Output the lens-pass as a structured grid:

```
ABSTRACTED JOB: <one-sentence job from Step 1>

LENS                       | CANDIDATE ANALOGIES
---------------------------+------------------------------------------------
Different industry         | drop-shipping, record labels, vending machines, ...
Different era              | door-to-door sales, medieval guild, ...
Different scale            | personal homepage, neighborhood bulletin, Google index
Biological                 | seed dispersal, mycorrhizal networks, ...
Adjacent profession        | librarian, hostage negotiator, magician
Black-market               | drug dealers, smugglers, ...
Childhood / amateur        | lemonade stand, school book fair
Reverse / inversion        | how do I get UNINSTALLED → study churn attackers
Game-design                | quest-giver mechanic, daily-login reward, ...
Constraint-flip            | what if I had no engineers?
Genre-shift                | onboarding-as-horror-movie, ...
Anti-domain                | if the user is luxury → study Wal-Mart, etc.
```

You will *not* mine all of these — most are throwaway prompts. But generating the full grid first prevents premature commitment to the obvious analogies.

### Step 3 — Pick 2–4 with user input

Surface the **5–8 most generative** candidate analogies (your judgment; do not exhaust the user with the full grid). Use `AskUserQuestion` to let them choose 2–4 to actually mine.

Phrasing example:

> Your stuck problem abstracts to: *"how do I get my product into strangers' hands at low marginal cost."* Here are 6 analogies that the lens-pass surfaced as most generative. I'd default to **drop-shipping** (industry) and **drug dealers** (black-market) — both are unreasonably good at "distribution-with-zero-marketing." Pick 2–4 to mine, or say "all" if you want a wide net.
>
> - Drop-shipping
> - Record labels (taste-maker distribution)
> - Hollywood agents (talent representation)
> - Drug dealers (word-of-mouth at scale)
> - Vending machines (placement = destiny)
> - Mycorrhizal networks (biological)

Recommend defaults explicitly. "All of them" is allowed but expensive — flag the cost.

### Step 4 — Pull the meta-sauce on analogical thinking (one-time)

**Before** mining the user's chosen analogies, invoke the `get-sauce` skill against the `design-thinking` topic to load up on *how to actually do this move well*. This is the meta-pass — it grounds the rest of the workflow in real practitioner language about analogical reasoning, not your priors.

Concretely:

1. Read `~/moonlight/sauce/skills/get-sauce/references/topics/design-thinking.md` directly. (It's curated for exactly this purpose.)
2. Spawn the `get-sauce` workflow with this question:

   > *"How do experienced founders, designers, and thinkers actually use analogies from distant domains to solve their problems? Specifically: how do they pick which analogy to pursue, when does the analogy break down, and what's the move that turns 'cute observation' into 'real product decision'?"*

3. Use **Founders Podcast**, **Acquired**, **IDEO/d.school**, and **Brian Chesky talks** as the default corpus (these are flagged in the topic file).
4. Run get-sauce's full loop (sauce-hunter → critic → optional augment).

The output of this pass is **process sauce** — quotes and tactics about *how* to make analogies work. Keep it in your context for the rest of the workflow; cite it in Step 7 when translating analogies into recommendations.

> Don't skip this step even if you "know how analogies work." The user gets way more value when the analogy-translation move itself is grounded in Chesky-said-X / Munger-said-Y / IDEO-said-Z than in your priors. This is the same anti-pattern that motivates `get-sauce` in the first place — apply it to ourselves.

### Step 5 — For each picked analogy, invoke `get-sauce`

Loop over the 2–4 analogies the user picked. For each one:

1. **Treat the analogous domain as the actual sauce target.** "Drop-shipping" is now the topic of the sauce hunt, not "app distribution."

2. **Check `references/topics/` first** — there may already be a curated topic file for that domain. If not, fall back to grepping `references/sources.md`.

3. **Compose a sauce-hunt question** that's expressed *in the analogous domain's vocabulary* — not the user's. Examples:

   | User's actual problem | Analogy | Sauce-hunt question (in analogy's vocabulary) |
   |---|---|---|
   | App distribution | Drop-shipping | "How do successful drop-shippers acquire customers at near-zero CAC?" |
   | Onboarding | Magician's opening trick | "What do master magicians say about the structure of a great opener?" |
   | Pricing SaaS | Opera-house seating | "How did opera houses historically segment audiences via seat tiering?" |
   | Retention | AA meetings | "What do AA organizers say about why people keep showing up?" |

4. **Invoke `get-sauce`** end-to-end against that question. If a relevant topic file exists, use it; otherwise grep the master registry; otherwise the user may need to nominate a source.

5. **If no sauce corpus exists** for the analogous domain in the registry, do **one** of:
   - `WebSearch` + `WebFetch` for primary-source interviews/essays in the analogous domain
   - Ask the user if they know a podcast/book/operator in that domain
   - Skip and note as a limitation. Don't fall back on LLM priors about that domain — that defeats the whole skill.

6. **Note any new sources discovered** and consider contributing them back to the registry per `get-sauce`'s "How to contribute" section.

### Step 6 — For each analogy, build the translation table

For each mined analogy, build a **translation table** mapping patterns from the analogous domain back to the user's domain:

```
ANALOGY: Drop-shipping
ABSTRACTED JOB: low-CAC distribution of products you don't make yourself

PATTERN IN ANALOG               | QUOTE                                    | TRANSLATES TO IN USER'S DOMAIN
--------------------------------+------------------------------------------+----------------------------------
"Winning product > winning ad"  | <Operator quote, file cite>              | "Your paywall conversion ceiling
                                |                                          |  is set by the product, not
                                |                                          |  the funnel"
"Test 50 SKUs in week 1"        | <Operator quote, file cite>              | "Ship 50 onboarding variants
                                |                                          |  in week 1, not 5"
"The customer is the algorithm" | <Operator quote, file cite>              | "TikTok organic is the new
                                |                                          |  AliExpress storefront"
...                             | ...                                      | ...
```

Three rules:

1. **The pattern must be a verbatim quote**, not your summary of the operator. Cite the file (per `get-sauce` discipline).
2. **The translation must be defensible** — explicitly check: what's the same about the situation? What's different? Does the difference invalidate the analogy?
3. **Flag where the analogy breaks down.** Every analogy fails somewhere. Saying *"this maps cleanly except for X, where the user's domain has constraint Y that drop-shippers don't"* is more useful than a perfect-sounding translation.

### Step 7 — Synthesize and relay

Compose the final answer:

1. **One-paragraph framing**: what the abstracted job was, which analogies you mined, why those.
2. **Per-analogy section**: the translation table (Step 6), plus a "what specifically I'd try first" 2–3 bullet recommendation drawn from the operator quotes.
3. **Meta-synthesis**: across all analogies, what *converging* patterns showed up? (Convergence across distant domains is the strongest signal that you've hit a real underlying structure.) What *contradicting* patterns? (Contradictions are forks the user has to choose between.)
4. **Process meta-note** (from Step 4): one or two quotes from Chesky / Munger / IDEO / Senra about how to *evaluate* whether the analogy actually applies — give the user the tool to second-guess your translation.
5. **Where the analogies break**: which translations the user should *not* trust, and why.

Don't re-summarize operators' words — quote them. The framing is a wrapper around their actual language.

## When to use this skill vs. `get-sauce` directly

| Situation | Use |
|---|---|
| "How are *other founders in my exact space* doing X?" | `get-sauce` directly |
| "What's the playbook on paywall design for apps?" | `get-sauce` directly |
| "I'm stuck — give me a totally different angle on this problem" | **this skill** |
| "What's [my problem] look like through the lens of [some other industry]?" | **this skill** |
| "Help me ideate without being trapped in my own category" | **this skill** |
| "Give me 5 variations of my idea" | Neither — that's a regular ideation prompt |

The diagnostic: if you can name a podcast/founder who's literally solved this exact problem, use `get-sauce`. If the user needs *re-framing* before they even know what to look for, use this.

## Anti-patterns

- ❌ **Skipping Step 1's abstraction.** If you don't strip the user's category off, every analogy will be a near-neighbor and you'll generate same-industry ideas in costume. The abstraction is the move.
- ❌ **Picking near analogies.** "App distribution is like website distribution" — too close. The Innocentive research is unambiguous: *distant* domains outperform near ones for novel ideation. Push further.
- ❌ **Generating analogies but not mining them.** A list of "we should look at how X does it" is not the deliverable. The deliverable is **operator quotes from domain X translated into the user's domain.** That requires `get-sauce`-grade source mining for each analogy.
- ❌ **Falling back on LLM priors about the analogous domain.** If you don't have real source material on drop-shipping, you'll generate generic "drop-shipping intuitions" — which is exactly what `get-sauce` exists to prevent. Either find primary sources or flag the gap.
- ❌ **Pretending the analogy is perfect.** Every analogy fails. Naming the failure mode is part of the value.
- ❌ **Stopping at one analogy.** Convergence across 2–4 distant analogies is the strongest signal that the underlying structure is real. One analogy is just a clever observation.
- ❌ **Letting the user pick "all 12 lenses".** This is a bait-and-switch; you'll generate shallow translations for all of them. Push back: 2–4 deep beats 12 shallow.

## Repo hygiene

This skill is **dependent on** the `get-sauce` skill in the same repo (`skills/get-sauce/`). It assumes:

- `skills/get-sauce/SKILL.md` is the canonical sauce-hunting workflow.
- `skills/get-sauce/references/topics/design-thinking.md` is the meta-process source (Step 4).
- `skills/get-sauce/references/topics/*.md` and `skills/get-sauce/references/sources.md` are the discovery layers for each analogy in Step 5.

If `get-sauce` is missing, this skill cannot run — say so, link the user to install it, and stop.

## Further reading

- `skills/get-sauce/SKILL.md` — the underlying sauce-hunt workflow this skill calls.
- `skills/get-sauce/references/topics/design-thinking.md` — the curated meta-sauce topic on analogical reasoning, lateral thinking, and design-thinking method.
- Edward de Bono, *Lateral Thinking* — the canonical primer on the kind of move this skill operationalizes.
- David Epstein, *Range*, ch. 4–5 — the empirical case for distant-analogy ideation.
- Steven Johnson, *Where Good Ideas Come From* — "the adjacent possible" and "exaptation."
- Brian Chesky's talks on Airbnb's cross-industry inspiration ("design Airbnb like a Disney Cruise") — operationalized analogical thinking by a working founder.

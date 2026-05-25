# Sauce Sources

Curated registry of the best startup / founder / VC / tech / indie / app content on the
internet. Use this file to **discover** which podcast, blog, newsletter, channel, or
public figure is likely to have sauce on a given topic — before you decide what to
sync via `scripts/sync.py` or fetch via `WebFetch`.

## Format

Each non-comment line is one source:

    Name | url1, url2, x.com/handle | tag1, tag2, tag3, ...

- **Name** — human-readable identifier
- **URLs** — comma-separated; primary first, then secondary (e.g. X handle, YouTube)
- **Tags** — comma-separated; **the first tag is the medium** (`podcast`, `blog`,
  `newsletter`, `youtube`, `book-publisher`, `vc-publication`, `x-account`), the
  rest describe topics/domains

Lines starting with `#` or `##` are comments and not part of the data.

## How to discover sources

```bash
# Find anything tagged with a topic you care about
grep -i "paywall\|monetization\|subscription" skills/get-sauce/references/sources.md

# Find a specific person or publication
grep -i "naval\|paul graham\|altman" skills/get-sauce/references/sources.md

# Filter by medium
grep -i "| podcast" skills/get-sauce/references/sources.md
grep -i "| blog"    skills/get-sauce/references/sources.md
grep -i "| youtube" skills/get-sauce/references/sources.md

# Find every founder-interview source
grep -iE "(founder-interviews|founders|biographies)" skills/get-sauce/references/sources.md

# When the list is small enough, just read the whole thing
cat skills/get-sauce/references/sources.md
```

If you can't find a good source via grep, read the file end-to-end before bothering the
user — the tags are imperfect and some sources cover more ground than their tags imply.

# ──────────────────────────────────────────────────────────────────────────────
# Podcasts
# ──────────────────────────────────────────────────────────────────────────────
Acquired | acquired.fm, youtube.com/@AcquiredFM, x.com/AcquiredFM | podcast, youtube, tech-history, deep-dives, M&A, strategy, big-tech, founders
My First Million | mfmpod.com, youtube.com/@MyFirstMillionPod, x.com/MFMPod | podcast, youtube, business-ideas, indie, AI, consumer, side-hustle, Shaan-Puri, Sam-Parr
Napkin Math | napkinmath.fm, youtube.com/@NapkinMathFM | podcast, youtube, startups, founders, SaaS, AI, bootstrapping, business-ideas, Sabba-Keynejad, Charlie-Ward, VEED, Ramen-Club
Lenny's Podcast | lennyspodcast.com, lennysnewsletter.com/podcast | podcast, youtube, PM, product, growth, careers, founders, interviews
Indie Hackers Podcast | indiehackers.com/podcast, x.com/IndieHackers | podcast, bootstrapping, indie, MRR, side-projects, solo, SaaS, founders
This Week in Startups | thisweekinstartups.com, youtube.com/@ThisWeekIn, x.com/Jason | podcast, youtube, VC, news, fundraising, Calacanis, interviews
How I Built This | npr.org/podcasts/510313/how-i-built-this | podcast, founders, origin-stories, NPR, Guy-Raz, brand-building, interviews
Masters of Scale | mastersofscale.com | podcast, scaling, Reid-Hoffman, founders, network-effects, interviews
The Tim Ferriss Show | tim.blog/podcast | podcast, interviews, mental-models, lifestyle, founders, performance, deep-conversations
The Knowledge Project | fs.blog/knowledge-project-podcast | podcast, mental-models, decision-making, Shane-Parrish, leadership, philosophy
Invest Like the Best | joincolossus.com/episodes, x.com/patrick_oshag | podcast, investing, founders, capital-allocation, business-quality, deep-research
20VC | 20vc.com, x.com/HarryStebbings | podcast, VC, founders, fundraising, term-sheets, interviews, enterprise
All-In Podcast | allinpodcast.co, youtube.com/@allin, x.com/theallinpod | podcast, youtube, tech-news, VC, politics, macro, debate, Chamath, Sacks
Founders Podcast | founderspodcast.com, foundersnotes.com, x.com/FoundersPodcast | podcast, biographies, history, classics, David-Senra, legendary-founders
SaaStr Podcast | saastr.com/podcasts | podcast, SaaS, B2B, enterprise, scaling, Jason-Lemkin, sales
Bootstrapped Founder | thebootstrappedfounder.com/podcast | podcast, bootstrapping, Arvid-Kahl, audience-building, indie, SaaS, exits
Startups for the Rest of Us | startupsfortherestofus.com | podcast, SaaS, bootstrapping, Rob-Walling, MicroConf, TinySeed, indie
Y Combinator Podcast (Lightcone) | youtube.com/@ycombinator, x.com/ycombinator | podcast, youtube, YC, startups, advice, fundraising, founders, Garry-Tan
a16z Podcast | a16z.com/podcasts | podcast, VC, tech, AI, biotech, future, enterprise, founders
Superwall Podcast | youtube.com/playlist?list=PL3XL-MsZorn_Nfi3jrPqQtxDk-kxyaaz8 | podcast, youtube, apps, paywalls, monetization, IAP, SDK, mobile, subscriptions, founders, RevenueCat
Sub Club Podcast | subclub.co/podcasts, x.com/subclubhq | podcast, apps, subscriptions, IAP, app-monetization, RevenueCat, mobile
Logan Bartlett Show | youtube.com/@loganbartlettshow, x.com/loganbartshow | podcast, youtube, tech, VC, founders, scaling, interviews
The Diary of a CEO | thediaryofaceo.com, youtube.com/@TheDiaryOfACEO | podcast, youtube, founders, scaling, leadership, Steven-Bartlett, mental-health
Hard Fork | nytimes.com/column/hard-fork | podcast, AI, tech-news, NYT, Casey-Newton, Kevin-Roose
Pivot | nymag.com/podcasts/pivot | podcast, tech-news, opinion, Kara-Swisher, Scott-Galloway, media
Lex Fridman Podcast | lexfridman.com, youtube.com/@lexfridman, x.com/lexfridman | podcast, youtube, AI, scientists, founders, long-form, philosophy
Below the Line with James Beshara | jamesbeshara.com | podcast, founders, deep-conversations, philosophy, builders, creators
The Tropical MBA | tropicalmba.com/podcast | podcast, bootstrapping, location-independent, lifestyle-business, indie
DTC Podcast | dtcpod.com | podcast, DTC, ecommerce, brands, marketing, Shopify
Mostly Metrics (podcast + newsletter) | mostlymetrics.com, x.com/CJGustafson22 | podcast, newsletter, SaaS, CFO, metrics, ARR, finance, public-companies
Default Alive | youtube.com/@defaultaliveshow | podcast, youtube, indie, bootstrapping, MRR
Greg Isenberg (Startup Ideas) | youtube.com/@gregisenberg, x.com/gregisenberg | podcast, youtube, startup-ideas, communities, consumer, AI, niches
Lenny & Friends Summit | lennysnewsletter.com | podcast, youtube, PM, growth, product, conferences

# ──────────────────────────────────────────────────────────────────────────────
# Solo blogs / personal essayists
# ──────────────────────────────────────────────────────────────────────────────
Paul Graham | paulgraham.com, x.com/paulg | blog, YC, startups, essays, philosophy, hackers, programming, founders, fundraising
Sam Altman | blog.samaltman.com, x.com/sama | blog, x-account, AI, OpenAI, YC, startups, future, AGI, fundraising, leadership
Naval Ravikant | nav.al, x.com/naval | blog, x-account, wealth, happiness, startups, philosophy, leverage, angel-investing, AngelList
Patrick McKenzie (patio11) | kalzumeus.com, bitsaboutmoney.com, x.com/patio11 | blog, SaaS, pricing, banking, fintech, dev, conversion, Stripe, sales
Pieter Levels | levels.io, x.com/levelsio | blog, x-account, nomad, indie, MRR, AI, bootstrapping, solo, micro-SaaS, building-in-public
Marc Andreessen | pmarca.substack.com, a16z.com, x.com/pmarca | blog, x-account, VC, future, tech, software-eats-the-world, manifesto, AI, a16z
Ben Thompson | stratechery.com, x.com/benthompson | blog, newsletter, analysis, platform, aggregation-theory, strategy, media, big-tech
Ben Horowitz | a16z.com/author/ben-horowitz | blog, CEO, hard-things, management, founders, VC, a16z, leadership
Fred Wilson | avc.com, x.com/fredwilson | blog, VC, USV, NYC, web3, early-stage, daily-blogging
Brad Feld | feld.com, x.com/bfeld | blog, VC, Foundry-Group, Boulder, board-dynamics, term-sheets, mental-health
DHH (David Heinemeier Hansson) | dhh.dk, world.hey.com/dhh, x.com/dhh | blog, x-account, Basecamp, Rails, bootstrapping, opinionated, profitable, remote, anti-VC
Jason Fried | jasonfried.com, world.hey.com/jason, x.com/jasonfried | blog, Basecamp, bootstrapping, remote, profit, REWORK, calm-company
Joel Spolsky | joelonsoftware.com, x.com/spolsky | blog, dev, management, Stack-Overflow, Trello, software, hiring, classics
Andrew Chen | andrewchen.com, x.com/andrewchen | blog, growth, marketplaces, network-effects, a16z, consumer, retention
Tomasz Tunguz | tomtunguz.com, x.com/ttunguz | blog, SaaS, metrics, VC, benchmarks, fundraising, B2B
Lenny Rachitsky | lennysnewsletter.com, x.com/lennysan | newsletter, PM, growth, product, hiring, careers, B2B
Sahil Lavingia | sahillavingia.com, x.com/shl | blog, Gumroad, indie, creator-economy, art, transparency, calm
Justin Jackson | justinjackson.ca, x.com/mijustin | blog, bootstrapping, marketing, MegaMaker, Transistor, MRR, niches
Rob Walling | robwalling.com, x.com/robwalling | blog, MicroConf, SaaS, bootstrapping, indie, exits, TinySeed
April Dunford | aprildunford.com, x.com/aprildunford | blog, positioning, marketing, B2B, sales, messaging, GTM
Byrne Hobart | thediff.co, x.com/byrnehobart | newsletter, finance, tech, macro, M&A, capital-allocation, deep-research
Packy McCormick | notboring.co, x.com/packym | newsletter, strategy, web3, business, deep-dives, narrative, AI
Mario Gabriele | generalist.com, x.com/mariogabriele | newsletter, founders, deep-dives, VC, profiles, strategy
Eric Newcomer | newcomer.co, x.com/EricNewcomer | newsletter, VC-news, scoops, fundraising, Silicon-Valley
Nathan Latka | nathanlatka.com, x.com/nathanlatka | blog, podcast, SaaS, metrics, founders, public-revenue, ARR
Marc Lou | marclou.com, x.com/marc_louvion | blog, x-account, indie, ship-fast, AI, micro-SaaS, Next.js, boilerplates, MRR
Daniel Vassallo | dvassallo.com, x.com/dvassallo | blog, small-bets, indie, portfolio, leaving-bigco, freelancing
Arvid Kahl | thebootstrappedfounder.com, x.com/arvidkahl | blog, bootstrapping, audience, SaaS, exit, indie, content
Steph Smith | stephsmith.io, x.com/stephsmithio | blog, podcast, trends, content, marketing, exploding-topics, a16z
Sahil Bloom | sahilbloom.com, x.com/SahilBloom | newsletter, business, mental-models, growth, finance, wealth
Shaan Puri | shaanpuri.com, x.com/ShaanVP | blog, x-account, business-ideas, MFM, AI, consumer, content
Sam Parr | x.com/theSamParr | x-account, media, hustle, MFM, audience-building, Hampton
Tim Ferriss | tim.blog, x.com/tferriss | blog, podcast, lifestyle, productivity, interviews, mental-models, founders
Greg Isenberg | greg.isenberg.com, x.com/gregisenberg | blog, podcast, communities, startup-ideas, consumer, AI
Andrej Karpathy | karpathy.ai, x.com/karpathy | blog, x-account, AI, ML, OpenAI, Tesla, founders, deep-learning
Simon Willison | simonwillison.net, x.com/simonw | blog, AI, sqlite, datasette, tools, building-in-public, OSS
Reid Hoffman | reidhoffman.org, x.com/reidhoffman | blog, networks, scale, LinkedIn, Greylock, AI, blitzscaling
Andy Matuschak | andymatuschak.org, x.com/andy_matuschak | blog, learning, tools-for-thought, design, research
Ryan Hoover | ryanhoover.com, x.com/rrhoover | blog, x-account, Product-Hunt, indie, community, launches, consumer
Hiten Shah | hitenism.com, x.com/hnshah | blog, SaaS, products, KISSmetrics, Crazy-Egg, FYI, B2B
Patrick Collison | patrickcollison.com, x.com/patrickc | blog, x-account, Stripe, fintech, progress-studies, infra, founders
John Collison | x.com/collision | x-account, Stripe, fintech, founders, payments
Brian Chesky | x.com/bchesky | x-account, Airbnb, design, founder-mode, marketplaces, hospitality
Drew Houston | x.com/drewhouston | x-account, Dropbox, founders, productivity, B2B
Elad Gil | eladgil.com, x.com/eladgil | blog, scaling, angel-investing, AI, hyper-growth, High-Growth-Handbook
Aaron Levie | x.com/levie | x-account, Box, enterprise-SaaS, founders, AI, witty
Auren Hoffman | safegraph.com/blog, x.com/auren | blog, x-account, data, B2B, hiring, scaling, SafeGraph
Brian Norgard | x.com/BrianNorgard | x-account, consumer, growth, mobile, Tinder, distribution
David Sacks | x.com/DavidSacks | x-account, enterprise-SaaS, PayPal-mafia, Yammer, distribution, All-In

# ──────────────────────────────────────────────────────────────────────────────
# YouTube channels (not already listed as podcasts)
# ──────────────────────────────────────────────────────────────────────────────
Y Combinator | youtube.com/@ycombinator | youtube, YC, startups, advice, founders, Startup-School, partners
Starter Story | starterstory.com, youtube.com/@starterstoryinc, x.com/starterstory | youtube, blog, bootstrapping, indie, case-studies, side-business, founders, $1M-solo
Noah Kagan | youtube.com/@noahkagan, x.com/noahkagan | youtube, AppSumo, indie, bootstrapping, founders, marketing, sales
Codie Sanchez | youtube.com/@codiesanchez, x.com/Codie_Sanchez | youtube, small-business, acquisition, boring-businesses, contrarian, Main-Street
TK Kader | youtube.com/@TKKader | youtube, SaaS, GTM, B2B, founders
Ali Abdaal | youtube.com/@aliabdaal, x.com/AliAbdaal | youtube, productivity, business, creators, YouTube-growth

# ──────────────────────────────────────────────────────────────────────────────
# Newsletters / Publications
# ──────────────────────────────────────────────────────────────────────────────
Stratechery | stratechery.com, x.com/stratechery | newsletter, analysis, platform, aggregation, strategy, Ben-Thompson, paywall
The Generalist | generalist.com, x.com/thegeneralist | newsletter, founders, deep-dives, VC, profiles, strategy
Not Boring | notboring.co, x.com/notboringco | newsletter, strategy, web3, business, deep-dives, narrative
Newcomer | newcomer.co, x.com/EricNewcomer | newsletter, VC-news, scoops, fundraising, Silicon-Valley
The Diff | thediff.co, x.com/byrnehobart | newsletter, finance, tech, macro, M&A, capital-allocation
Lenny's Newsletter | lennysnewsletter.com | newsletter, PM, growth, careers, product, B2B
Every | every.to, x.com/every | newsletter, essays, business, AI, productivity, builders, deep-essays
Sub Club | subclub.co | newsletter, podcast, apps, subscriptions, IAP, app-monetization, RevenueCat
RevenueCat Blog | revenuecat.com/blog, x.com/RevenueCat | blog, apps, subscriptions, IAP, mobile, subscription-economy, State-of-Subscriptions
Mostly Metrics | mostlymetrics.com | newsletter, podcast, SaaS, CFO, metrics, ARR, finance, public-companies
The Pragmatic Engineer | newsletter.pragmaticengineer.com, x.com/GergelyOrosz | newsletter, engineering, eng-management, big-tech, scaling, hiring
Stripe Press | press.stripe.com | book-publisher, history, growth, business, infrastructure, classics, science, progress-studies
First Round Review | review.firstround.com, x.com/firstround | publication, founders, lessons, hiring, leadership, scaling, PM, B2B
The Information | theinformation.com, x.com/theinformation | publication, tech-news, scoops, paywalled, enterprise
Hacker News | news.ycombinator.com | community, tech, startups, dev, discussion, YC
YC Library | ycombinator.com/library, x.com/ycombinator | publication, YC, essays, partners, startup-advice, fundraising, hiring, classics
YC Startup School | startupschool.org | publication, YC, curriculum, founders, lessons, free
Future / a16z | future.com, a16z.com/future, x.com/a16z | publication, tech-essays, AI, crypto, biotech, VC
USV (Union Square Ventures) | usv.com, x.com/usv | vc-publication, VC, early-stage, web3, network-effects, Fred-Wilson
Sequoia Capital Insights | sequoiacap.com/insights | vc-publication, VC, founders, scaling, lessons, Arc, market-research
Greylock Perspectives | greylock.com/blog | vc-publication, VC, AI, enterprise, founders, Reid-Hoffman
Bessemer Atlas | bvp.com/atlas | vc-publication, cloud, SaaS, benchmarks, IPO, public-comps
Benedict Evans | ben-evans.com, x.com/benedictevans | newsletter, tech-analysis, mobile, platforms, statistics, presentations
SaaStr | saastr.com | publication, podcast, conference, SaaS, B2B, scaling, Jason-Lemkin
MicroConf | microconf.com | publication, conference, SaaS, bootstrapping, indie, Rob-Walling
IndieHackers (community) | indiehackers.com, x.com/IndieHackers | community, podcast, bootstrapping, indie, MRR, side-projects, transparency
Product Hunt | producthunt.com, x.com/ProductHunt | community, launches, indie, products, consumer, makers
Hampton | joinhampton.com, x.com/joinhampton | community, founders, peer-groups, Sam-Parr, private
Trends.vc | trends.vc | newsletter, trends, niches, opportunities, market-research, Dru-Riley
Exploding Topics | explodingtopics.com, x.com/explodingtopics | publication, trends, search-data, niches, Steph-Smith
Trung Phan | trungphan.substack.com, x.com/TrungTPhan | newsletter, x-account, tech, asia, memes, business
Polina Marinova Pompliano | thepost.substack.com, x.com/polina_marinova | newsletter, founders, profiles, profiles-in-history
Khe Hy | radreads.co, x.com/khemaridh | newsletter, knowledge-work, productivity, leaving-bigco, finance
Visualize Value | visualizevalue.com, x.com/visualizevalue | x-account, design, mental-models, branding, Jack-Butcher

# ──────────────────────────────────────────────────────────────────────────────
# Conferences (operator-grade talks, mostly published on YouTube)
# ──────────────────────────────────────────────────────────────────────────────
# Conferences are an underrated sauce source — talks are usually 20–45 min of
# tactical, in-the-trenches content from founders and engineers. Most of the
# entries below publish their talks to YouTube and can be ingested by sync.py.
# The second URL is the YouTube channel/playlist you'd point sync.py at.

# --- AI / ML / agents / LLM ---
AI Engineer (Summit / World's Fair / Code Summit) | ai.engineer, youtube.com/@aiDotEngineer | conference, youtube, AI, agents, LLM, dev-tools, evals, RAG, MCP, Latent-Space, Swyx
OpenAI DevDay | openai.com/devday, youtube.com/@OpenAI, youtube.com/playlist?list=PLOXw6I10VTv_o0ZLpFu2IQyQOho1l-v7y | conference, youtube, AI, OpenAI, API, agents, multimodal, dev-tools, keynote
Ray Summit (Anyscale) | anyscale.com/ray-summit, youtube.com/playlist?list=PLzTswPQNepXm3Q-PpP619ThIW5EX6Cah8 | conference, youtube, AI, MLOps, distributed-systems, inference, vLLM, fine-tuning, Anyscale
LangChain Interrupt | interrupt.langchain.com, youtube.com/@LangChain | conference, youtube, AI, agents, LangChain, LangGraph, production-LLM, evals, deployment
Anthropic / Claude Engineer events | anthropic.com/events, youtube.com/@anthropic-ai | conference, youtube, AI, Claude, agents, prompt-engineering, MCP, safety
NVIDIA GTC | nvidia.com/gtc, youtube.com/@NVIDIA | conference, youtube, AI, GPU, infrastructure, CUDA, robotics, computer-vision, Jensen-Huang
Google I/O | io.google, youtube.com/@GoogleDevelopers | conference, youtube, AI, Gemini, Android, web, cloud, Google
Microsoft Build | build.microsoft.com, youtube.com/@MicrosoftDeveloper | conference, youtube, AI, Copilot, Azure, .NET, dev-tools, enterprise
AWS re:Invent | reinvent.awsevents.com, youtube.com/@AWSEventsChannel | conference, youtube, AI, cloud, infrastructure, AWS, Bedrock, agents, databases
Snowflake Summit | snowflake.com/summit, youtube.com/@SnowflakeInc | conference, youtube, AI, data, warehouse, analytics, MLOps
Databricks Data + AI Summit | databricks.com/dataaisummit, youtube.com/@Databricks | conference, youtube, AI, data, MLOps, Spark, lakehouse, enterprise
MLOps World | mlopsworld.com, youtube.com/@MLOpsWorld | conference, youtube, AI, MLOps, production-ML, deployment, monitoring
The AI Conference (Ben Lorica) | aiconference.com, youtube.com/@TheAIConference | conference, youtube, AI, LLM, agents, applied-ML, Gradient-Flow

# --- Developer / engineering ---
QCon / InfoQ Dev Summit | infoq.com/qcon, youtube.com/@InfoQ | conference, youtube, dev, eng, architecture, distributed-systems, SRE, eng-leadership, platform
GOTO Conferences | gotopia.tech, youtube.com/@GOTO- | conference, youtube, dev, eng, architecture, dev-tools, programming-languages, classics
LeadDev | leaddev.com, youtube.com/@LeadDev | conference, youtube, dev, eng, eng-leadership, eng-management, careers, org-design
React Conf | conf.react.dev, youtube.com/@ReactConfOfficial | conference, youtube, dev, react, frontend, JavaScript, Meta
React Conferences (GitNation) | gitnation.org, youtube.com/@ReactConferences | conference, youtube, dev, react, frontend, JavaScript, TypeScript, Node
Next.js Conf / Vercel Ship | nextjs.org/conf, youtube.com/@VercelHQ | conference, youtube, dev, react, Next.js, web-platform, edge, AI-SDK
ViteConf | viteconf.org, youtube.com/@vitejs | conference, youtube, dev, JavaScript, tooling, frontend, Vite, build-tools
JSConf | jsconf.com, youtube.com/@jsconf | conference, youtube, dev, JavaScript, frontend, Node
PyCon US | pycon.org, youtube.com/@PyConUS | conference, youtube, dev, python, data, web
GopherCon | gophercon.com, youtube.com/@GopherAcademy | conference, youtube, dev, Go, golang, infrastructure
RustConf | rustconf.com, youtube.com/@RustVideos | conference, youtube, dev, rust, systems-programming, performance
KubeCon + CloudNativeCon (CNCF) | events.linuxfoundation.org/kubecon-cloudnativecon-north-america, youtube.com/@cncf | conference, youtube, dev, eng, kubernetes, cloud-native, devops, SRE, observability
DockerCon | docker.com/dockercon, youtube.com/@DockerInc | conference, youtube, dev, containers, devops, microservices
HashiConf | hashicorp.com/conferences/hashiconf, youtube.com/@HashiCorp | conference, youtube, dev, infrastructure, Terraform, Vault, devops
GitHub Universe | githubuniverse.com, youtube.com/@GitHub, youtube.com/playlist?list=PL0lo9MOBetEF_de7yKAWpnMkTsKH6aJ4P | conference, youtube, dev, eng, AI, Copilot, devops, security, OSS
Strange Loop (archived) | thestrangeloop.com, youtube.com/@strangeloopconf | conference, youtube, dev, eng, programming-languages, distributed-systems, classics, FP
SREcon (USENIX) | usenix.org/srecon, youtube.com/@usenix | conference, youtube, dev, SRE, eng, reliability, observability, postmortems

# --- Startup / founder / VC ---
SaaStr Annual | saastr.com/saastr-annual, youtube.com/@saastr | conference, youtube, founders, startup, SaaS, B2B, sales, GTM, Jason-Lemkin
MicroConf | microconf.com, youtube.com/@MicroConf | conference, youtube, founders, startup, SaaS, bootstrapping, indie, Rob-Walling
Lenny & Friends Summit | lennyssummit.com, youtube.com/playlist?list=PL2fLjt2dG0N4z9w9pkeMgdPq2xcpME_N2 | conference, youtube, founders, startup, PM, product, growth, careers, Lenny-Rachitsky
Y Combinator Startup School | startupschool.org, youtube.com/@ycombinator | conference, youtube, founders, startup, YC, advice, fundraising, hiring, Garry-Tan
TechCrunch Disrupt | techcrunch.com/events/tc-disrupt, youtube.com/@techcrunch | conference, youtube, founders, startup, VC, fundraising, news, pitch-competitions
Web Summit | websummit.com, youtube.com/channel/UCJtkHqH4Qof97TSx7BzE5IQ | conference, youtube, founders, startup, VC, Lisbon, global, tech-news
Slush | slush.org, youtube.com/channel/UCv2JYTjV80AuHODJO0R6EnQ | conference, youtube, founders, startup, VC, Helsinki, Europe, deep-tech
Collision | collisionconf.com, youtube.com/@CollisionConf | conference, youtube, founders, startup, VC, tech-news, Toronto, sister-of-Web-Summit
All-In Summit | allinsummit.com, youtube.com/@allin | conference, youtube, founders, VC, macro, debate, Chamath, Sacks, Friedberg, Calacanis
Acquired Conference (Acquired Live) | acquired.fm, youtube.com/@AcquiredFM | conference, youtube, founders, deep-dives, history, business-strategy, Ben-Gilbert, David-Rosenthal
First Round CEO Summit (recorded talks) | review.firstround.com, youtube.com/@FirstRoundCapital | conference, youtube, founders, leadership, scaling, CEO, B2B
South Park Commons events | southparkcommons.com, youtube.com/@SouthParkCommons | conference, youtube, founders, founder-in-residence, deep-tech, AI, technical
LAUNCH Festival | launchfestival.com, youtube.com/@thisweekin | conference, youtube, founders, startup, VC, Calacanis, pitch
Acquired Conferences (Hometown / Annual Live) | acquired.fm, youtube.com/@AcquiredFM | conference, youtube, founders, deep-dives, business-history

# --- Product / design / vertical tech ---
Stripe Sessions | stripe.com/sessions, youtube.com/playlist?list=PLcoWp8pBTM3CYTQho8i-a_lzx4cq7-ePh | conference, youtube, fintech, payments, AI, agents, MCP, dev-tools, Stripe, internet-economy
Twilio SIGNAL | signal.twilio.com, youtube.com/@twilio | conference, youtube, dev, communications, AI, customer-engagement, voice, messaging
Cloudflare Connect | cloudflare.com/connect, youtube.com/@Cloudflare | conference, youtube, dev, infrastructure, edge, security, AI, workers
Figma Config | config.figma.com, youtube.com/channel/UCQsVmhSa4X-G3lHlUtejzLA | conference, youtube, design, product, PM, UX, Dylan-Field, Figma
Adobe MAX | max.adobe.com, youtube.com/@AdobeCreativeCloud | conference, youtube, design, creative, AI, video, Adobe, Photoshop
Mind the Product (#mtpcon) | mindtheproduct.com, youtube.com/c/MindtheProductTV | conference, youtube, product, PM, ProductTank, careers, leadership
INBOUND (HubSpot) | inbound.com, youtube.com/@hubspot | conference, youtube, marketing, growth, sales, content, HubSpot, B2B
Dreamforce (Salesforce) | salesforce.com/dreamforce, youtube.com/@salesforce | conference, youtube, enterprise, SaaS, CRM, sales, Salesforce, AI
Money 20/20 | money2020.com, youtube.com/channel/UCip4CIpmM13NOAH-j9GiAzg | conference, youtube, fintech, payments, banking, stablecoins, open-finance
Shoptalk | shoptalk.com, youtube.com/@Shoptalk | conference, youtube, ecommerce, DTC, retail, brands, Shopify
MozCon | moz.com/mozcon, youtube.com/@MozHQ | conference, youtube, marketing, SEO, content, growth
Business of Apps Summit (App Promotion Summit) | apppromotionsummit.com, youtube.com/channel/UCg2NMpWp3jI3zYg_R4NZIaQ | conference, youtube, apps, mobile, ASO, UA, paywall, monetization, growth
VidCon | vidcon.com, youtube.com/@vidcon | conference, youtube, creator-economy, YouTube, TikTok, creators, brand-deals
Podcast Movement | podcastmovement.com, youtube.com/@PodcastMovement | conference, youtube, creator-economy, podcasting, audio, monetization
SXSW (interactive) | sxsw.com, youtube.com/@sxsw | conference, youtube, founders, creator-economy, culture, tech-meets-culture, Austin

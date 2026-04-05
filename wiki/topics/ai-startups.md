---
title: AI Startups
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["AI startups", "AI companies", "vertical AI", "vertical AI agents", "AI agents", "LLM startups", "AI SaaS", "building with AI", "AI moats", "AI defensibility"]
related: ["[[Startup Ideas]]", "[[Product-Market Fit]]", "[[Sales and Distribution]]", "[[Pricing]]", "[[Growth]]", "[[Vibe Coding]]", "[[Design]]"]
sources: ["Lt-vertical-ai-agents-could-be-10x-bigger-than-saas", "Lg-why-vertical-llm-agents-are-the-new-1-billion-saas-opportunities", "Mx-the-7-most-powerful-moats-for-ai-startup", "MQ-startup-ideas-you-can-now-build-with-ai", "My-every-ai-founder-should-be-asking-these-questions", "MS-state-of-the-art-prompting-for-ai-agents", "MW-andrej-karpathy-software-is-changing-again", "L7-how-new-technology-creates-new-businesses", "LH-tarpit-ideas-the-sequel", "M3-how-to-use-ai-in-your-startup", "M5-ai-revolution-why-this-is-the-best-time-to-start-a-startup", "M8-how-to-get-ai-startup-ideas", "Kb-the-truth-about-building-ai-startups-today-lightcone-podcast-ep-1", "LD-10-people-ai-billion-dollar-company", "MB-how-ai-is-changing-enterprise", "MM-the-next-breakthrough-in-ai-agents-is-here", "MO-windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-the-future-of-coding", "MP-how-ai-coding-agents-will-change-your-job", "MR-ai-apps-are-broken-here-s-how-to-fix-them", "Mt-the-fde-playbook-for-ai-startups-with-bob-mcgrew", "MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters", "Mq-how-this-25-year-old-built-a-675m-legal-ai-startup-with-no-legal-experience", "N0-unpopular-ideas-that-became-billion-dollar-businesses"]
speakers_referenced: ["Jared Friedman", "Gary Tan", "Harj Taggar", "Diana Hu", "Jake Heller", "Andrej Karpathy", "Jordan Fisher", "Tom Blomfield", "Dalton Caldwell", "Michael Seibel", "Paul Buchheit", "Gustaf Alstromer", "Pete Koomen", "Brad Flora", "Aaron Levie", "Varun Mohan", "Michael Truell", "Bob McGrew", "Max Junestrand", "David Lieb", "Amjad Masad"]
---

# AI Startups

The YC canon on AI startups centers on one thesis: vertical AI agents represent a category at least as large as SaaS, potentially 10x larger. Friedman estimates there will be 300+ billion-dollar vertical AI agent companies, mirroring the 300+ SaaS unicorns produced over the prior 20 years ([Vertical AI agents could be 10x bigger than SaaS](https://www.ycombinator.com/library/Lt-vertical-ai-agents-could-be-10x-bigger-than-saas)).

## The Vertical AI Agent Thesis

Friedman draws a direct parallel to SaaS history. SaaS emerged when XMLHttpRequest enabled rich web applications in 2004-2005, making it possible to move desktop software to the browser. LLMs represent an equivalent paradigm shift: where SaaS companies sold software that helped people do work, vertical AI agents do the work itself ([Vertical AI agents could be 10x bigger than SaaS](https://www.ycombinator.com/library/Lt-vertical-ai-agents-could-be-10x-bigger-than-saas)).

The economic implication is dramatic. SaaS companies captured roughly 1% of customer wallet share because they sold tools. AI agent companies capture 4-10% because they replace labor costs. Tan cites Aoka, which sells AI customer support for HVAC companies: ServiceTitan captures 1% of gross transaction value, but Aoka captures 4-10% by replacing the customer support function ([The 7 most powerful moats for AI startups](https://www.ycombinator.com/library/Mx-the-7-most-powerful-moats-for-ai-startup)).

## Ideas That AI Unlocks

Taggar identifies a category of ideas that failed pre-AI but are now viable. His own company, TripleByte, was a recruiting marketplace that required years to build evaluation capability manually. Merror, a current YC company, replicated the same evaluation using LLMs on day one ([Startup ideas you can now build with AI](https://www.ycombinator.com/library/MQ-startup-ideas-you-can-now-build-with-ai)).

Friedman identifies "full-stack startups" -- companies that do the work rather than sell software for it -- as another category that failed in the 2010s due to poor gross margins but may now succeed because AI agents replace the human operations layer. Atrium (full-stack law firm) failed; Legora (AI legal tools) is succeeding. The difference: agents do the knowledge work that previously required hiring large teams ([Startup ideas you can now build with AI](https://www.ycombinator.com/library/MQ-startup-ideas-you-can-now-build-with-ai)).

## Moats for AI Companies

The Lightcone hosts apply Hamilton Helmer's Seven Powers framework to AI startups ([The 7 most powerful moats for AI startups](https://www.ycombinator.com/library/Mx-the-7-most-powerful-moats-for-ai-startup)):

**Speed** is the dominant early moat. Cursor shipped features on one-day sprint cycles during 2023-2024. No large company can match that pace. Varun from Windsurf states: at the beginning, the only moat startups have is speed.

**Process power** is the primary defensibility for vertical AI agents at scale. The hackathon version of any AI agent takes a weekend to build. The production version that handles tens of thousands of requests reliably takes years. The last 5-10% of reliability is "painstaking drudgery work" that big-company engineers find unappealing.

**Switching costs** take a new form in AI. Traditional SaaS switching costs involved data migration. AI switching costs involve the lengthy customization of agent logic -- deep integration into enterprise workflows that took months of forward-deployed engineering.

**Counterpositioning** operates through pricing models. Incumbent SaaS companies charge per seat. If their AI agents succeed, they reduce the number of seats and thus their own revenue. Founder-controlled incumbents like Intercom may navigate this; non-founder-controlled companies likely cannot.

**Network effects** manifest as data flywheels. Usage generates evals, evals improve prompts, better prompts improve the product, and better products generate more usage. Cursor uses every keystroke and mouse click to train its autocomplete models.

## The Forward-Deployed Engineer Model

Tan traces this model to Palantir, where engineers -- not salespeople -- sat next to FBI agents and government analysts to understand their workflows, then built software overnight. The same model now defines the best AI startups. Founders sit with customers, observe workflows, codify them into prompts and evals, and return with working demos in days ([State-of-the-art prompting for AI agents](https://www.ycombinator.com/library/MS-state-of-the-art-prompting-for-ai-agents)).

Happy Robot closed seven-figure contracts with the top three logistics brokers using this model. Giga ML won Zapier's customer support contract by building the most impressive demo. The forward-deployed engineer model combined with AI enables startups to close enterprise deals that previously required large sales teams.

## Prompting and Evals as Core IP

Friedman states that evals -- not prompts -- are the crown jewels of vertical AI agent companies. Parahelp agreed to open-source their prompt because "without the evals, you don't know why the prompt was written the way that it was" ([State-of-the-art prompting for AI agents](https://www.ycombinator.com/library/MS-state-of-the-art-prompting-for-ai-agents)).

Metaprompting -- using one LLM to improve another's prompts -- has emerged as a standard technique. Tan describes it as "the LLM version of test-driven development." Founders use larger models (Claude 3.5, GPT-4o) to generate and refine prompts, then deploy the refined prompts on faster, cheaper models for production.

## Software 3.0

Karpathy frames the shift as a third era of software. Software 1.0 is traditional code. Software 2.0 is neural network weights. Software 3.0 is prompts written in English that program LLMs ([Andrej Karpathy: Software is changing again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again)). He argues LLMs are best understood as operating systems, not utilities -- they are complex software ecosystems, not commodities. The ecosystem is circa 1960s computing: expensive, centralized, accessed via time-sharing.

Karpathy warns against over-indexing on full autonomy. He advocates "partial autonomy apps" with an "autonomy slider" -- like Cursor, which offers tab completion (low autonomy) through full agentic mode (high autonomy). "It's less Iron Man robots and more Iron Man suits that you want to build."

## The Technology Shift Pattern

Caldwell and Seibel argue that every major technology shift creates a window where people who understand new tools first can create outsized value ([How new technology creates new businesses](https://www.ycombinator.com/library/L7-how-new-technology-creates-new-businesses)). The internet, eBay, open source, cloud compute, the iPhone App Store, Shopify, and Twitch each produced this effect. AI follows the same pattern but with unprecedented demand. Levie (CEO of Box) told YC's AI retreat: "This is the first time no one's saying no. Everyone is saying yes" ([AI Revolution](https://www.ycombinator.com/library/M5-ai-revolution-why-this-is-the-best-time-to-start-a-startup)).

YC batches since summer 2023 have averaged 10% week-on-week growth across the entire batch. Companies are hitting $1M ARR within six months. Buchheit notes that "once intelligence is truly on tap, it is a force multiplier for founders with strong senses of agency." The growth companies overwhelmingly sell AI agents to businesses, where the technical challenge of making LLMs perform at human-equivalent quality is the moat.

## Finding AI Startup Ideas

Friedman, Hu, Taggar, and Tan share frameworks ([How to get AI startup ideas](https://www.ycombinator.com/library/M8-how-to-get-ai-startup-ideas)). **Look within** -- the strongest ideas come from founders with deep domain experience (Salient from Tesla finance ops, Diode from dual EE/CS expertise, DataCurve from a Cohere internship). **Go undercover** -- one founder got a remote medical billing job to understand the workflow, then automated it. **Follow the outsourcing signal** -- any job being sent to BPOs overseas is a target. **Shadow domain experts** -- sit next to someone in an unfamiliar industry for a few hours.

Caldwell and Seibel note that classic [[Startup Ideas|tarpit ideas]] may no longer be tarpits if AI makes them newly solvable, but founders must explain why rather than ignoring prior failures ([Tarpit ideas: the sequel](https://www.ycombinator.com/library/LH-tarpit-ideas-the-sequel)).

## AI Is Changing Enterprise

Levie (CEO of Box) argues that enterprise customers do not want a model -- they want an outcome. Customer support conversations answered, healthcare transcription flowing into an EHR, automated contract workflows. The model getting more intelligent is a net positive for application builders because "what the customer actually wants to buy is software that will plug into my ERP system, that will power the workflow" ([How AI is changing enterprise](https://www.ycombinator.com/library/MB-how-ai-is-changing-enterprise)).

He draws a direct parallel to cloud computing. On-prem software was a $50B market, but SaaS expanded TAMs by 10x because lower cost-to-try expanded the addressable customer base from ten thousand enterprises to millions of businesses. AI will repeat this pattern. The cost of intelligence converges toward the cost of bare metal; the value accrues to the software layer above it. Levie predicts the total software market could be five times larger in a decade because AI enables software to do work previously done by humans or not done at all -- translation, contract review, lead generation that companies never staffed for.

Enterprise adoption as of early 2025 is roughly 10% for general chat assistants and 1% for anything resembling agents. The CEO of Goldman Sachs publicly described AI generating S-1 filings in minutes. Levie notes this is the opposite of cloud adoption where banking CEOs said "we'll never go to the cloud." AI adoption in enterprise is driven by competitive pressure: a non-AI-first company cannot hire the next AI-native generation, and competitors will produce more output.

## The 10-Person Billion-Dollar Company

Sam Altman predicted unicorns with ten or fewer employees. The Lightcone hosts debate this against the Jevons Paradox ([10 People + AI = Billion Dollar Company?](https://www.ycombinator.com/library/LD-10-people-ai-billion-dollar-company)). Historically, each wave of efficiency (open source, SaaS, cloud) did not reduce company size; it increased the number of companies by lowering the barrier to getting started. Taggar concludes: "Even if it means slightly more people can take their idea and turn it into something and get their first thousand users, the human capital will come, the actual financial capital will come, and we'll just get more of these things."

The hosts argue that taste and craftsmanship requirements rise as building becomes easier. The baseline for YC admission is now much higher than a decade ago. Friedman argues that learning to code remains essential because "learning how to code will literally make you smarter" -- LLMs themselves learned to think logically by reading code on GitHub.

## AI Tarpit Ideas and the Wrapper Debate

The first Lightcone episode identifies AI tarpits: copilot-for-X platforms where customers sign up and pay but never actually use the product ([The truth about building AI startups today](https://www.ycombinator.com/library/Kb-the-truth-about-building-ai-startups-today-lightcone-podcast-ep-1)). Tan warns against chat interfaces that put the burden on users to know how to speak to a computer. The real value lies in packaging LLM capabilities into familiar UIs that do the knowledge work directly.

The "GPT wrapper" meme is dismissed by both Levie and Tan. Levie draws the analogy: all SaaS software is a "database wrapper," but the business logic, workflow, and UX atop the database is where value accrues. Tan concurs from the Manus analysis: successful wrappers are distinguished by intuitive UI, proprietary evals, fine-tuning, and multi-agent orchestration -- not by building a foundation model ([The next breakthrough in AI agents is here](https://www.ycombinator.com/library/MM-the-next-breakthrough-in-ai-agents-is-here)).

## AI-Native Application Design

Koomen argues that most AI applications are "horseless carriages" -- they bolt AI into legacy interfaces rather than redesigning for what AI can do ([AI apps are broken -- here's how to fix them](https://www.ycombinator.com/library/MR-ai-apps-are-broken-here-s-how-to-fix-them)). The Gmail draft-writing feature illustrates the problem: the system prompt is hidden, generic, and produces output that sounds like no individual human. The fix is to expose and let users edit the system prompt -- shifting from one-size-fits-all software to user-programmable AI.

Koomen frames this as a fundamental shift in software design. Traditional software required developers to synthesize all user needs into a common feature set. AI enables software the user can program using natural language. The developer's role shifts from writing all the business logic to building the tools (labeling, archiving, drafting, scheduling) that agents can call. See [[Design]] for more on the [[Vibe Coding]] implications.

## The FDE Playbook for AI

McGrew (former CRO of OpenAI, early Palantir executive) describes the forward-deployed engineer model as "doing things that don't scale at scale" ([The FDE playbook for AI startups](https://www.ycombinator.com/library/Mt-the-fde-playbook-for-ai-startups-with-bob-mcgrew)). At Palantir, FDEs went to customer sites and built gravel-road prototypes solving the customer's top-five priority problems. The product engineering team then paved those gravel roads into generalized product features.

The model has two roles: Echo (embedded analyst with domain expertise who manages relationships and discovers use cases) and Delta (engineer who prototypes rapidly). McGrew emphasizes the Echo must be a "heretic" -- someone who knows the domain but recognizes its insufficiency. The Delta must be a rapid prototyper, not a craftsman. With AI agents, there is no incumbent product, which is why the FDE model is exploding: there is enormous product discovery to do. Over 100 YC startups now hire for "forward deployed engineer" roles, up from zero three years ago.

## Will OpenAI Kill All Startups?

Caldwell and Seibel address the fear that foundation model companies will capture all AI value ([Will OpenAI kill all startups?](https://www.ycombinator.com/library/Ie-dalton-michael-will-openai-kill-all-startups)). They dismiss the AGI debate as outside the scope of practical founder advice and instead draw on history: every major technology shift -- farming, electricity, the internet, mobile, cloud -- created more startup opportunities, not fewer. Startups are relatively advantaged versus incumbents during rapid shifts.

They distinguish [[Company Culture|cargo culting]] AI (saying "we have AI" to raise money) from genuinely using AI to improve retention, quality, or willingness to pay. The latter is real and comparable to the mobile app shift that nearly killed Facebook when it moved too slowly. Seibel analogizes: "Uber was a consequence of the iPhone. Second-order effects like this from LLMs are going to be amazing."

Two groups of founders are well-positioned: domain experts in ML who see predictions becoming reality, and tinkerers who embrace LLMs the way early iPhone jailbreakers embraced mobile. Founders motivated primarily by making money fast are not attracted to AI -- which Caldwell considers a positive signal. Until the large companies solve AGI (their primary goal), using existing tools to solve customer problems represents a vast opportunity they are not pursuing.

## Using AI Internally

Every new startup should use LLMs internally regardless of whether AI is the product. An HOA management company in YC uses LLMs to make all operations more efficient ([How to use AI in your startup](https://www.ycombinator.com/library/M3-how-to-use-ai-in-your-startup)). Alstromer draws a parallel to the cloud migration of the early 2010s: legacy software rebuilt AI-native will be much better. Flora warns against superficial pivots: "Just switching your idea over to something that makes calls to OpenAI is not going to change your fate as a startup."

Zepto (YC S21) illustrates AI-internal adoption at scale: the Indian quick-commerce company uses LLMs for automated customer support (over 50% of tickets resolved by generative chatbot), ad relevance engines trained on Llama, and supply chain forecasting -- all while the core product is grocery delivery, not AI ([How Zepto became India's fastest growing startup](https://www.ycombinator.com/library/ML-how-zepto-became-india-s-fastest-growing-startup)).

## Contrarian Bets in AI

The Lightcone hosts observe that the two-year window of obvious AI ideas is closing ([Unpopular ideas that became billion-dollar businesses](https://www.ycombinator.com/library/N0-unpopular-ideas-that-became-billion-dollar-businesses)). Taggar notes that finding vertical AI agent ideas is no longer as easy as "pick a workflow to automate" because multiple startups now compete in each vertical and no recent model release has created a step-function change. The next wave of winners will come from contrarian insights -- ideas that feel dangerous, seem to have a graveyard of predecessors, or require going deep into unsexy domains. DoorDash, Uber, and Coinbase all entered crowded, legally ambiguous spaces and won by making a contrarian bet the market rejected.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [Vertical AI agents could be 10x bigger than SaaS](https://www.ycombinator.com/library/Lt-vertical-ai-agents-could-be-10x-bigger-than-saas) | Jared Friedman, Gary Tan | 300+ vertical AI unicorns predicted; SaaS history as template |
| [Why vertical LLM agents are the new $1B SaaS opportunities](https://www.ycombinator.com/library/Lg-why-vertical-llm-agents-are-the-new-1-billion-saas-opportunities) | Jake Heller | Casetext: 10 years of incremental progress, then GPT-4 changed everything |
| [The 7 most powerful moats for AI startups](https://www.ycombinator.com/library/Mx-the-7-most-powerful-moats-for-ai-startup) | Lightcone hosts | Seven Powers applied to AI; speed as the dominant early moat |
| [Startup ideas you can now build with AI](https://www.ycombinator.com/library/MQ-startup-ideas-you-can-now-build-with-ai) | Lightcone hosts | Failed ideas revived by AI; full-stack startups; follow curiosity |
| [State-of-the-art prompting for AI agents](https://www.ycombinator.com/library/MS-state-of-the-art-prompting-for-ai-agents) | Lightcone hosts | Evals as crown jewels; metaprompting; forward-deployed engineer model |
| [Andrej Karpathy: Software is changing again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) | Andrej Karpathy | Software 3.0; LLMs as operating systems; partial autonomy apps |
| [Every AI founder should be asking these questions](https://www.ycombinator.com/library/My-every-ai-founder-should-be-asking-these-questions) | Jordan Fisher | Two-year resilience test; sycophancy vs. honesty in AI products |
| [How new technology creates new businesses](https://www.ycombinator.com/library/L7-how-new-technology-creates-new-businesses) | Dalton Caldwell, Michael Seibel | Technology shifts create founder opportunities; weirdos on the internet |
| [Tarpit ideas: the sequel](https://www.ycombinator.com/library/LH-tarpit-ideas-the-sequel) | Dalton Caldwell, Michael Seibel | Classic tarpits may be unlocked by AI; Copilot for X is common not tarpit |
| [How to use AI in your startup](https://www.ycombinator.com/library/M3-how-to-use-ai-in-your-startup) | YC Partners | Every startup should use AI internally; cloud migration analogy |
| [AI Revolution](https://www.ycombinator.com/library/M5-ai-revolution-why-this-is-the-best-time-to-start-a-startup) | YC Partners, Paul Buchheit | 10% week-on-week batch average; evals as moat; agency as force multiplier |
| [How to get AI startup ideas](https://www.ycombinator.com/library/M8-how-to-get-ai-startup-ideas) | YC Partners | Look within, go undercover, follow outsourcing, shadow domain experts |
| [The truth about building AI startups today](https://www.ycombinator.com/library/Kb-the-truth-about-building-ai-startups-today-lightcone-podcast-ep-1) | Lightcone hosts | AI tarpits, copilot-for-X trap, workflow automation as real opportunity |
| [10 People + AI = Billion Dollar Company?](https://www.ycombinator.com/library/LD-10-people-ai-billion-dollar-company) | Lightcone hosts | Jevons Paradox; taste and craftsmanship matter more; learn to code |
| [How AI is changing enterprise](https://www.ycombinator.com/library/MB-how-ai-is-changing-enterprise) | Aaron Levie | Enterprise wants outcomes not models; TAM expands 5x; intelligence cost to zero |
| [The next breakthrough in AI agents is here](https://www.ycombinator.com/library/MM-the-next-breakthrough-in-ai-agents-is-here) | Gary Tan | Manus multi-agent system; wrapper debate; chain-of-thought injection |
| [Windsurf CEO](https://www.ycombinator.com/library/MO-windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-the-future-of-coding) | Varun Mohan | Weekend pivot; evals as hill to climb; moat as a verb |
| [How AI coding agents will change your job](https://www.ycombinator.com/library/MP-how-ai-coding-agents-will-change-your-job) | Tom Blomfield, David Lieb | Software engineering jobs transform; best time to be a founder |
| [AI apps are broken](https://www.ycombinator.com/library/MR-ai-apps-are-broken-here-s-how-to-fix-them) | Pete Koomen | Horseless carriage problem; expose system prompts; user-programmable AI |
| [Cursor CEO](https://www.ycombinator.com/library/MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters) | Michael Truell | Replace coding with something better; taste is irreplaceable; paid power users metric |
| [The FDE playbook for AI startups](https://www.ycombinator.com/library/Mt-the-fde-playbook-for-ai-startups-with-bob-mcgrew) | Bob McGrew | FDE model from Palantir; Echo/Delta roles; doing things that don't scale at scale |
| [How this 25-year-old built a $675M legal AI startup](https://www.ycombinator.com/library/Mq-how-this-25-year-old-built-a-675m-legal-ai-startup-with-no-legal-experience) | Max Junestrand | Legora: legal AI replacing fragmented point solutions; GPT-3.5 as catalyst |
| [Unpopular ideas that became billion-dollar businesses](https://www.ycombinator.com/library/N0-unpopular-ideas-that-became-billion-dollar-businesses) | Lightcone hosts | Two-year window closing; contrarian bets required; DoorDash/Uber/Coinbase examples |
| [Will OpenAI kill all startups?](https://www.ycombinator.com/library/Ie-dalton-michael-will-openai-kill-all-startups) | Dalton Caldwell, Michael Seibel | History of tech shifts; cargo culting vs. real AI; second-order effects |

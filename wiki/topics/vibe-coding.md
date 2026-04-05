---
title: Vibe Coding
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["vibe coding", "AI coding", "AI-assisted coding", "coding with AI", "LLM coding", "prompt-driven development", "AI coding agents", "Cursor", "Windsurf", "Replit Agent"]
related: ["[[AI Startups]]", "[[Product Development]]", "[[Design]]", "[[Founder Mindset]]", "[[Hiring]]"]
sources: ["MN-how-to-get-the-most-out-of-vibe-coding", "MW-andrej-karpathy-software-is-changing-again", "ME-vibe-coding-is-the-future", "MO-windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-the-future-of-coding", "MP-how-ai-coding-agents-will-change-your-job", "Lq-now-anyone-can-code-how-ai-agents-can-build-your-whole-app", "LD-10-people-ai-billion-dollar-company", "MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters", "Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students"]
speakers_referenced: ["Tom Blomfield", "Andrej Karpathy", "Gary Tan", "Jared Friedman", "Harj Taggar", "Diana Hu", "Varun Mohan", "David Lieb", "Amjad Masad", "Michael Truell"]
---

# Vibe Coding

Karpathy coined the term "vibe coding" in a tweet that became a major meme, giving a name to the practice of building software by prompting AI models rather than writing code directly ([Andrej Karpathy: Software is changing again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again)). Blomfield, a YC partner, spent a month experimenting with vibe coding and produced a practitioner's playbook ([How to get the most out of vibe coding](https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding)).

## When to Use It

Karpathy describes vibe coding as ideal for building "something super duper custom that doesn't appear to exist and you just want to wing it because it's a Saturday." He built an iOS app in Swift -- a language he cannot program in -- in a single day. His MenuGen app (menu.app) was working on his laptop in hours, though making it production-ready (authentication, payments, deployment) took another week.

Blomfield recommends Replit or Lovable for non-coders, and Cursor, Windsurf, or Claude Code for developers. Tools like Lovable excel at UI generation but struggle with precise backend logic modifications.

## Best Practices

**Plan before coding.** Work with the LLM to write a comprehensive plan in a markdown file. Step through it section by section. Explicitly mark features as "won't do" or "ideas for later." After completing each section, commit to Git, then mark it complete in the plan ([How to get the most out of vibe coding](https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding)).

**Use version control religiously.** Blomfield advises starting every new feature from a clean Git state. When the AI goes on a "vision quest," `git reset --hard` and start over. Multiple failed fix attempts accumulate "layers and layers of bad code." If a fix eventually works after several attempts, reset and feed only that solution into a clean codebase.

**Write tests.** LLMs write good tests but default to low-level unit tests. Blomfield prefers high-level integration tests that simulate a user clicking through the app. Tests catch regressions when LLMs make unnecessary changes to unrelated logic.

**Write instructions.** Cursor rules, Windsurf rules, or Claude markdown files shape LLM behavior. Some YC founders have written hundreds of lines of instructions for their AI coding agents.

**Switch models.** Different models succeed where others fail. Blomfield finds Gemini best for codebase indexing and implementation plans, Sonnet 3.7 best for implementing code changes. YC batch founders report running Cursor and Windsurf simultaneously on the same project, picking the better output.

**Use screenshots and voice.** Pasting screenshots into coding agents demonstrates UI bugs or imports design inspiration. Voice input via tools like Aqua enables 140 words-per-minute input, roughly double typing speed.

## Keeping AI on the Leash

Karpathy warns against over-reliance on agentic coding. A 10,000-line diff is not useful -- the human is still the bottleneck for verification. He advocates small, incremental chunks where the generation-verification loop spins fast. Vague prompts increase the probability of failed verification; concrete prompts increase the probability of successful verification ([Andrej Karpathy: Software is changing again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again)).

He draws an analogy to Tesla Autopilot: a perfect 30-minute demo in 2013 made self-driving seem imminent, but 12 years later the problem remains unsolved. "When I see things like 'oh, 2025 is the year of agents,' I get very concerned. This is the decade of agents."

## The Code Is the Easy Part

Karpathy's MenuGen experience illustrates a broader pattern: vibe coding the application logic took hours, but making it production-ready -- authentication, payments, DNS, hosting -- took a week. The DevOps layer requires clicking through browser UIs and following instructions that should be automated. This gap represents a startup opportunity: building infrastructure that agents can use directly.

## YC Batch Data

The Lightcone hosts surveyed the current YC batch on vibe coding practices ([Vibe coding is the future](https://www.ycombinator.com/library/ME-vibe-coding-is-the-future)). One quarter of founders reported that more than 95% of their codebase was AI-generated. Cursor is the dominant tool, with Windsurf as a fast follower. Claude Sonnet 3.5 remains the most-used model for code generation, with reasoning models (O1, O3) gaining ground for debugging. DeepSeek R1 is mentioned as a viable contender. Gemini's long context window makes it useful for dumping an entire codebase and asking for a fix.

Founders describe a shift in identity. The founder of Outlet states: "The role of software engineer will transition to product engineer. Human taste is now more important than ever." Another: "I am far less attached to my code now, so my decisions on whether we decide to scrap or refactor code are less biased since I can code three times as fast." One founder reports a 100x speed-up from one month ago to now. Several describe running multiple Cursor windows in parallel, prompting different features simultaneously.

## Two Classes of Engineer

Taggar (who ran TripleByte and conducted more technical interviews than perhaps anyone alive) observes that vibe coding creates two divergent profiles: the product engineer with taste who ships fast, and the systems architect who can scale to a billion users ([Vibe coding is the future](https://www.ycombinator.com/library/ME-vibe-coding-is-the-future)). The tools are terrible at debugging. Humans must still descend into the code to find logic errors. The Lightcone hosts draw the Picasso analogy: Picasso was a classically trained realist painter before he became an abstract artist. The best vibe coders will still need deep technical understanding to judge whether AI output is good or bad.

Hiring is changing. Stripe and Gusto pioneered "build a to-do list app in three hours" interviews over whiteboard algorithms. Taggar predicts this will evolve further: the screen may become "how well do you use these tools?" combined with code review and systems design. Tan argues the AI coding agents "will bullshit you just like a human employee will, if you're not technical enough to call them out." Being classically trained enough to catch AI errors remains a superpower.

## The Windsurf Story

Varun Mohan pivoted Windsurf from GPU virtualization to AI coding over a single weekend ([Windsurf CEO](https://www.ycombinator.com/library/MO-windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-the-future-of-coding)). The initial product was materially worse than GitHub Copilot but free. Within two months, they trained custom autocomplete models that could fill in the middle of code -- a capability Copilot lacked at the time. Dell and JP Morgan Chase became early enterprise customers.

Mohan describes the insight lifecycle: "Every single insight that we have is a depreciating insight." Speed is the only early moat. He advocates building rigorous evals before adding complexity: "Why would we add the AST parsing if it's unnecessary? I want the simplest code that ends up doing the most impact." Windsurf indexes entire codebases using a combination of keyword search, RAG, abstract syntax tree parsing, and GPU-accelerated real-time ranking -- moving beyond pure vector-database RAG because embeddings alone miss too many results in large codebases.

## The Cursor Story

Truell and three MIT co-founders initially built a co-pilot for CAD (mechanical engineering) before pivoting to coding ([Cursor CEO](https://www.ycombinator.com/library/MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters)). The CAD work taught them model training at scale and inference infrastructure, but the science was not ready for 3D and they were not personally passionate about the domain. They returned to coding because "building a company's hard and so you may as well work on the thing that you're really excited about."

The key product decision was building a full editor rather than a VS Code extension. They knew from Copilot's history that even ghost-text autocomplete required changes to the editor itself; future AI features would require far more control. Truell describes paid power users (AI usage 4-5 days per week) as the north star metric. He warns against optimizing for the demo: "With AI it's easy to take a couple of examples and put together a video where it looks like you have a revolutionary product." Cursor does over half a billion model calls per day on its own inference.

Truell states that taste is the irreplaceable skill: "defining what do you actually want to build" -- not just visual taste but taste for how logic works. More and more of programming's "human compilation step" will go away, but the judgment of what is useful never will.

## Replit Agent and Personal Software

Masad (CEO of Replit) frames the current moment as "1984 brought personal computing; 2024 brings personal software" ([Now anyone can code](https://www.ycombinator.com/library/Lq-now-anyone-can-code-how-ai-agents-can-build-your-whole-app)). Replit Agent uses a multi-agent system with a ReAct-like loop, custom retrieval (not just RAG), and memory management to build and deploy complete web apps from a prompt. One user built an app he had envisioned for 15 years in 15 minutes.

Masad argues the path to functional AGI is "almost a brute force problem" -- building specialized agent systems for each domain and eventually folding them into end-to-end models. He still advocates learning to code: "It is far more leverage to know how to code than ever before." Tan compares the moment to Mickey Mouse in Fantasia -- "this incredible menagerie of being able to build whatever the heck you want whenever you want."

## The Future of Software Engineering Jobs

Blomfield and Lieb project that current software engineering roles will not exist in five to ten years ([How AI coding agents will change your job](https://www.ycombinator.com/library/MP-how-ai-coding-agents-will-change-your-job)). Blomfield built a 35,000-line recipe app with interactive voice agent writing zero lines of code. A third to half of YC companies now primarily write code via AI tools, up from approximately zero two batches ago. Blomfield invokes the combine harvester analogy: food productivity went up 10x while the number of farmers per kilogram dropped by 1000x. Software will follow.

Lieb counters that these tools give "high agency individuals superpowers." The best time in history to start a company is now. Smaller teams mean better [[Design]] because ownership is clear: "one person or a very small group of people can really be the owners of a high quality experience."

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [How to get the most out of vibe coding](https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding) | Tom Blomfield | Practitioner's playbook: plan, Git, tests, switch models, refactor |
| [Andrej Karpathy: Software is changing again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) | Andrej Karpathy | Coined term; partial autonomy; keep AI on leash; decade of agents |
| [Vibe coding is the future](https://www.ycombinator.com/library/ME-vibe-coding-is-the-future) | Lightcone hosts | 25% of batch >95% AI-generated; product engineer shift; debugging still human |
| [Windsurf CEO](https://www.ycombinator.com/library/MO-windsurf-ceo-betting-on-ai-agents-pivoting-in-48-hours-and-the-future-of-coding) | Varun Mohan | Weekend pivot; depreciating insights; eval-driven development |
| [Cursor CEO](https://www.ycombinator.com/library/MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters) | Michael Truell | Replace coding; taste is irreplaceable; follow the scaling line |
| [Now anyone can code](https://www.ycombinator.com/library/Lq-now-anyone-can-code-how-ai-agents-can-build-your-whole-app) | Amjad Masad | Personal software era; multi-agent with custom retrieval; 15-year idea in 15 minutes |
| [How AI coding agents will change your job](https://www.ycombinator.com/library/MP-how-ai-coding-agents-will-change-your-job) | Tom Blomfield, David Lieb | Combine harvester for code; best time to start a company; high-agency superpowers |
| [10 People + AI = Billion Dollar Company?](https://www.ycombinator.com/library/LD-10-people-ai-billion-dollar-company) | Lightcone hosts | Jevons Paradox; still learn to code; coding makes you smarter |
| [Michael Truell at AI Startup School](https://www.ycombinator.com/library/Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students) | Michael Truell | Origin story; CAD pivot; all of coding will flow through models |

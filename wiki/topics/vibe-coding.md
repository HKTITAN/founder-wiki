---
title: Vibe Coding
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["vibe coding", "AI coding", "AI-assisted coding", "coding with AI", "LLM coding", "prompt-driven development"]
related: ["[[AI Startups]]", "[[Product Development]]", "[[Design]]"]
sources: ["MN-how-to-get-the-most-out-of-vibe-coding", "MW-andrej-karpathy-software-is-changing-again"]
speakers_referenced: ["Tom Blomfield", "Andrej Karpathy"]
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

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [How to get the most out of vibe coding](https://www.ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding) | Tom Blomfield | Practitioner's playbook: plan, Git, tests, switch models, refactor |
| [Andrej Karpathy: Software is changing again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again) | Andrej Karpathy | Coined term; partial autonomy; keep AI on leash; decade of agents |

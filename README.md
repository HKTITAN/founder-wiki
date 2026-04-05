# founder-wiki

The compiled startup knowledge base — LLM-queryable wiki of founder wisdom.

## What is this?

Inspired by [Karpathy's LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595) and [Farzapedia](https://x.com/FarzaTV/status/2040563939797504467), this project compiles raw startup content (videos, essays, transcripts) into a structured, interlinked wiki that any LLM agent can navigate and query.

Instead of RAG over raw documents, an LLM **incrementally builds and maintains a persistent wiki** — the knowledge is compiled once and kept current, not re-derived on every query.

> "Every business has a raw/ directory. Nobody's ever compiled it. That's the product." — [@tammireddy](https://x.com/tammireddy)

## Why not just ask an LLM?

An LLM already "knows" generic startup advice from its training data. founder-wiki adds:

- **Citation chains** — exact quotes with specific sources, not hallucinated summaries
- **Continuous updates** — new content absorbed as it's published
- **Cross-source synthesis** — the same topic woven together from 10+ different talks
- **Long tail** — obscure podcast comments and old blog posts the model may not have encoded
- **Evolution over time** — how thinking changed, not a flattened composite
- **Structure** — navigable by stage, topic, framework, speaker

## Architecture

Three layers, following Karpathy's pattern:

```
raw/                           # Immutable source layer
  _sources.json                # Master manifest
  videos/{slug}.md             # Video transcripts
  posts/{slug}.md              # Blog posts

wiki/                          # LLM-compiled, LLM-maintained
  _index.md                    # Agent entry point
  _backlinks.json              # Reverse link index
  _absorb_log.json             # Absorption progress
  {directories}/               # Emerge from the data

AGENTS.md                      # Schema — tells any agent how the wiki works
```

The wiki is **concept-centric, not person-centric**. Articles are organized by topic, framework, and stage. Speakers are attribution, not the organizing principle. "Product-Market Fit" is the synthesized doctrine on PMF across all speakers, not "what Dalton thinks about PMF."

Wiki structure follows **guided emergence**: directory types are suggested in AGENTS.md, but the LLM creates whatever articles and categories the data demands. Links, backlinks, and the index all emerge organically from absorption.

## Source Material

### Current: Y Combinator Library
~350 videos + ~70 blog posts from [ycombinator.com/library](https://www.ycombinator.com/library). Startup School lectures, Dalton & Michael series, partner talks, PG essays, founder stories.

### Future Extensions
- South Park Commons and similar founder communities
- Operator blogs and Twitter threads
- Podcast transcripts, books, essays from the broader founder ecosystem

## Use Cases

- **Founder Decision Support** — query during real strategic decisions with cited sources
- **Leadership Coaching** — structured coaching content for managers and execs
- **"Get Roasted"** — submit your pitch/idea, get feedback grounded in documented thinking
- **Career Trajectory Explorer** — understand how people navigated transitions
- **Queryable Depth** — synthesized understanding beyond what any single tweet or episode captures

## How to Query

Point any LLM agent at this repo. It reads `AGENTS.md` to understand the structure, starts at `wiki/_index.md`, and navigates to relevant articles. No RAG, no embeddings — just structured markdown.

## Related

This project emerged from the broader exploration in [wiki-of-you](https://github.com/VishalRohra/wiki-of-you), which documents the Karpathy/Farzapedia pattern, candidate profiles, selection criteria, and the full brainstorm of use cases.

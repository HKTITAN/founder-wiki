# Founder Wiki — Agent Schema

A compiled, queryable knowledge base of startup and founder wisdom. Built using the LLM Knowledge Base pattern (Karpathy) — raw sources are compiled by an LLM into a structured, interlinked wiki of markdown files. No RAG, no embeddings. The agent navigates structured markdown via an index.

## Architecture

Three layers:
- `raw/` — Immutable source transcripts and posts. One .md per source. Never modify after ingest.
- `wiki/` — LLM-compiled articles. The knowledge base. The LLM owns this layer entirely.
- `AGENTS.md` — This file. Schema and conventions.

## Directory Map

```
raw/
  _sources.json          # Master manifest of all ingested sources
  videos/{slug}.md       # Video transcripts with YAML frontmatter
  posts/{slug}.md        # Blog posts with YAML frontmatter

wiki/
  _index.md              # Master catalog — the agent's entry point
  _backlinks.json        # Reverse link index (auto-generated)
  _absorb_log.json       # Tracks which raw entries have been absorbed
  {directories}/         # Emerge from absorption (see below)
```

## Guided Emergence

**The LLM decides what articles to create, what to link, and how to organize.** The directory types below are suggestions, not constraints. Create new directories freely if the data demands it.

Suggested starting directory types:
- `topics/` — Broad topic articles synthesized from multiple sources (e.g., hiring, pricing, PMF)
- `frameworks/` — Named mental models and frameworks (e.g., tarpit idea framework, schlep blindness)
- `stages/` — Stage-of-journey overview articles (e.g., idea stage, finding PMF, scaling)
- `speakers/` — Speaker profile/routing pages (lightweight — list what they've discussed, link to topic articles)
- `series/` — Video series overview pages (e.g., Dalton & Michael, Startup School 2024)

But if the data suggests other categories (e.g., `case-studies/`, `mistakes/`, `metrics/`), create them.

## Operations

### Query

1. Read `wiki/_index.md` — scan for relevant articles using aliases in parentheses
2. Read 3-8 relevant wiki articles, following `[[wikilinks]]` 1-2 links deep
3. Check `wiki/_backlinks.json` if you need to find highly-connected topics
4. Synthesize answer with citations to specific sources
5. **NEVER read raw/ entries.** The wiki IS the knowledge base.
6. If the wiki doesn't cover it, say so. Don't guess.
7. Query is **read-only** — don't modify wiki files.

### Absorb (add new source to the wiki)

1. Read the raw/ entry
2. Read `wiki/_index.md` to understand current structure
3. Understand what the source means — not just "what facts does it contain" but "what does this tell us?"
4. For each topic/framework the entry touches:
   a. If an article exists: **re-read it fully**, then integrate the new material so the article reads as a coherent whole. Never just append.
   b. If no article exists and there's enough material (3+ meaningful sentences): create one in the appropriate directory
5. Connect to patterns — when the same theme surfaces across multiple sources, that deserves its own article
6. Update speaker page if needed
7. Update `wiki/_index.md` with any new articles (include aliases)
8. Mark source as absorbed in `wiki/_absorb_log.json`

**Anti-cramming:** If you're adding a third paragraph about a sub-topic to an existing article, that sub-topic probably deserves its own page.

**Anti-thinning:** Creating a page is not the win. Enriching it is. Every time you touch a page, it should get richer.

**Checkpoint every 15 entries:**
1. Rebuild `wiki/_index.md` with all articles and aliases
2. Rebuild `wiki/_backlinks.json`
3. New article audit: if zero new articles in the last 15, you're cramming
4. Quality audit: pick 3 most-updated articles. Re-read each as a whole piece:
   - Does it tell a coherent story, or is it a chronological dump?
   - Is it organized by theme, not by speaker or date?
   - Does it use attribution ("Dalton describes PMF as...") not assertion?
   - Would a reader learn something non-obvious?
   - If it reads like an event log, rewrite it.
5. Check if any articles exceed 100 lines and should be split
6. Check directory structure — create new directories if needed

### Cleanup

Audit and enrich existing articles:
- Is each article theme-driven or diary-driven? Restructure if needed.
- Are wikilinks correct and bidirectional?
- Any articles over 100 lines that should be split?
- Any topics mentioned across 3+ articles that lack their own page?
- Any stubs that should be enriched or merged?

### Breakdown

Find and create missing articles:
- Survey: bare directories, bloated articles, high-reference backlink targets without articles
- Extract concrete entities (the concrete noun test: "X is a ___")
- Rank by reference count, create in priority order
- Every new article should link back to existing articles that mention it

## Writing Standards

### The Golden Rule

**This is not Wikipedia about the thing. This is the synthesized founder wisdom on the thing.**

A page about "Hiring" isn't a generic article about hiring. It's the accumulated, cross-referenced advice from everyone who's spoken about hiring in the source material — with attribution, citations, and connections to related topics.

### Voice

Wikipedia-style. Flat, factual, encyclopedic. State what was said and by whom. Direct quotes from source material carry the emotional weight.

**Never use:** em dashes, peacock words ("legendary," "visionary," "groundbreaking," "deeply"), editorial voice ("interestingly," "importantly," "it should be noted"), rhetorical questions, progressive narrative ("would go on to," "embarked on"), qualifiers ("genuine," "raw," "profound").

**Do:** Lead with the subject, state facts plainly. One claim per sentence. Short sentences. Simple past or present tense. Attribution over assertion ("Dalton describes PMF as..." not "PMF is..."). Let facts imply significance. Dates and specifics replace adjectives.

**One exception:** Direct quotes carry the speaker's voice. The article is neutral. The quotes do the feeling.

### Article Format

```yaml
---
title: Article Title
type: topic | framework | stage | speaker | series | ...
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
aliases: ["PMF", "product market fit", "finding PMF"]
related: ["[[Other Article]]", "[[Another]]"]
sources: ["source-slug-1", "source-slug-2"]
speakers_referenced: ["Dalton Caldwell", "Michael Seibel"]
---

# Article Title

{Content organized by theme, not chronology or speaker}

## Sections as needed

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| source-slug | Speaker Name | One-line summary of what this source contributed |
```

### Key Principles

- Articles are **concept-centric**, not speaker-centric. Speakers are attribution.
- Cross-referencing the same idea across different speakers is the core value.
- Use **attributed synthesis**: weave multiple speakers' views into one coherent article. Don't just list "Speaker A says X, Speaker B says Y."
- Use `[[wikilinks]]` for all cross-references between articles.
- **Maximum 2 direct quotes per article.** Pick the lines that hit hardest.
- **Aliases in frontmatter are critical** — this is how queries match to articles.
- Every article must have a Source Talks table listing which raw entries contributed.
- Don't create one article per video/post. Synthesize across sources.
- Don't create topic articles with fewer than 3 sources contributing. Wait until enough material exists — or fold it into a broader article.

### Structure by Article Type

| Type | Organize by |
|------|------------|
| topic | Thematic sections (definition, common mistakes, practical advice, related frameworks) |
| framework | The model itself, how to apply it, examples, limitations |
| stage | What to focus on, common mistakes, how to know you're ready to move on |
| speaker | Topics they've covered (as links), brief background, key talks |
| series | What the series covers, structure, key topics touched |

### Length Targets

| Type | Lines |
|------|-------|
| Topic (few sources) | 30-60 |
| Topic (many sources) | 60-100 |
| Framework | 30-60 |
| Stage | 50-80 |
| Speaker | 20-40 |
| Series | 20-30 |
| Minimum (anything) | 15 |

## Source Material

### Current: Y Combinator Library
~350 videos + ~70 blog posts from ycombinator.com/library. Includes Startup School lectures, Dalton & Michael series, partner talks, PG essays, founder stories.

### Future Extensions
- South Park Commons and similar founder communities
- Operator blogs and Twitter threads (Shreyas, DHH, Sahil, etc.)
- Additional podcast transcripts, books, essays
- New source types go in `raw/{source-type}/` — the wiki layer is source-agnostic

---
title: Growth
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["growth", "startup growth", "growth rate", "weekly growth", "user growth", "compound growth", "scaling", "growth team", "retention", "product-market fit"]
related: ["[[Early-Stage Tactics]]", "[[Product Development]]", "[[Fundraising]]", "[[Financial Survival]]", "[[Hiring]]"]
sources: ["8s-startup-growth", "95-default-alive-or-default-dead", "96-do-things-that-don-t-scale", "8w-the-hardest-lessons-for-startups-to-learn", "4p-before-growing-your-startup", "59-how-to-set-up-hire-and-scale-a-growth-strategy-and-team", "6k-growth-for-startups", "6l-how-to-improve-conversion-rates", "89-how-to-succeed-with-a-startup", "LV-how-to-improve-cohort-retention"]
speakers_referenced: ["Paul Graham", "Sam Altman", "Anu Hariharan", "Gustaf Alstromer", "David Lieb"]
---

# Growth

Graham defines a startup as a company designed to grow fast ([Startup = Growth](https://www.ycombinator.com/library/8s-startup-growth)). Everything else about startups -- the [[Fundraising]], the exits, the culture -- follows from this single characteristic. "Startup = Growth" is the foundational equation.

## Growth as Compass

Graham argues that every founder should know their growth rate at all times, and that it should be measured as a ratio (percentage), not an absolute number ([Startup = Growth](https://www.ycombinator.com/library/8s-startup-growth)). A constant number of new customers per month means the growth rate is actually decreasing.

Picking a weekly growth rate target and optimizing for it turns the bewilderingly complex problem of running a startup into a single optimization problem. During YC, 5-7% weekly growth is good. 10% is exceptional. 1% is a sign something is wrong.

## The Math of Compound Growth

Small differences in weekly growth rate produce qualitatively different outcomes:
- 1% weekly = 1.7x per year
- 5% weekly = 12.6x per year
- 10% weekly = 142x per year

This exponential math is why the startup ecosystem (VCs, acquisitions, high failure rates) exists at all. It is why investors think in power laws, and why a startup that compounds at 5% weekly for 4 years reaches a scale that linear businesses never approach. This math also explains why [[Early-Stage Tactics]] like the [[Do Things That Don't Scale]] approach matter -- even small initial user bases compound into large numbers.

## The S-Curve

Growth has three phases ([Startup = Growth](https://www.ycombinator.com/library/8s-startup-growth)). The first phase is slow -- the founders are figuring out what they are doing. The second phase is rapid growth, which is the defining period. The third phase is maturity, when growth slows as the company approaches the limits of its market.

## Growth as Evolutionary Pressure

Focusing on a weekly growth target does more than measure progress. Graham argues it actually discovers better [[Startup Ideas]] through evolutionary pressure ([Startup = Growth](https://www.ycombinator.com/library/8s-startup-growth)). When founders commit to hitting a growth number every week, they are forced to find the tactics that work and discard those that do not. The idea itself evolves toward product-market fit.

## Don't Grow Before the Product Is Loved

Altman argues that focusing on growth before making a product people love is a foundational error ([Before growing your startup](https://www.ycombinator.com/library/4p-before-growing-your-startup)). The result is a "leaky bucket" -- users come in but do not stay and will not return. If the product is loved, users become a free marketing and sales force through word of mouth. Facebook had obsessive word-of-mouth from the start. Airbnb slogged for 1,000 days before discovering how to make their product loved, then grew exponentially.

Growing around a mediocre product creates a worse problem at scale: "Once your company is a big moving battleship, it becomes really hard to be nimble and quickly make the aggressive changes you need." Altman warns founders not to paper over a weak product by raising capital for growth -- "the problems will still be there, with higher expectations."

## When Growth Is Absent

In "[[Default Alive or Default Dead]]," Graham introduces a simple diagnostic: given current expenses and current revenue growth, will the startup reach profitability on the money it has? If not, the company is "default dead," and the founders need either faster growth or lower burn ([Default Alive or Default Dead](https://www.ycombinator.com/library/95-default-alive-or-default-dead)).

He argues that there is "surprisingly little connection between how much a startup spends and how fast it grows." Fast growth comes from [[Product Development]] that achieves product-market fit, not from spending. [[Hiring]] more people to solve a growth problem usually makes things worse -- a point connected to [[Financial Survival]] and burn rate discipline.

## Formalizing Growth: Teams and Process

Hariharan and Alstromer synthesize advice from 25 growth experts at Facebook, Airbnb, Uber, Stitch Fix, and others on building growth programs ([How to set up, hire, and scale a growth strategy and team](https://www.ycombinator.com/library/59-how-to-set-up-hire-and-scale-a-growth-strategy-and-team)).

**When to invest.** Do not hire a growth team before proving retention. A "leaky bucket" renders growth spending wasteful. Stitch Fix hired a retention-focused PM to run experiments improving retention before investing in new user acquisition. Three tests for good retention: (1) long-term retention is stable and parallel to the x-axis, (2) retention benchmarks favorably within your vertical, and (3) newer cohorts perform better than older ones.

Retention benchmarks by vertical (month 12 or year 2 medians): social networks 55%, on-demand 22%, travel 29%, e-commerce 16%, subscription 33%.

**Team composition.** The initial Year 1 growth team: 1 growth PM + 2-3 engineers + 1-2 data scientists. Most companies made their first growth hire at about 15 engineers. The growth PM is typically the 3rd or 4th PM on the team. 60% of growth experts interviewed were former startup founders.

**Absolute goals.** The growth team's goal must be an absolute number (e.g., "achieve 5M first-time room nights this year"), never a percentage change. The CEO must be aligned when setting the goal. 100% of experts emphasized this.

**Growth channels.** About 70% of experts cited referrals as the top channel in the first year. Channels are identified by examining existing user behavior: how do customers solve this problem today? How do best users use the product?

**Experimentation.** A company at scale runs approximately 1 experiment per growth engineer per week. Only a third of experiments produce positive results. Growth teams build internal experiment dashboards and run biweekly peer review. The key heuristic: "Don't test things you wouldn't ship to everybody."

**Where the team sits.** Facebook pioneered the separate growth department. Other companies (Uber, Airbnb, Slack) merged growth into product. At scale, growth teams can exceed 100 people: roughly 50% engineers, 10% PMs, 10-15% data scientists, 10% product marketing, 10-15% designers, 5% researchers.

## Growth Channels

Alstromer identifies two main growth strategies at scale: product growth (conversion rate optimization) and growth channels (external platforms where users discover products) ([Growth for startups](https://www.ycombinator.com/library/6k-growth-for-startups)).

**Conversion rate optimization.** Every step of the product experience is a funnel. At Airbnb, four pages (homepage, search results, listing, booking) constituted the entire conversion path, and only 1-2% of visitors completed it. Growth teams optimize each step by fixing content mismatches, broken browser support, authentication friction, onboarding flows, and purchase conversion. Hale adds a framework for thinking about conversion: identify the "magic moment" (when the user first understands the product's value) and make the call to action as close to that moment as possible ([How to improve conversion rates](https://www.ycombinator.com/library/6l-how-to-improve-conversion-rates)).

**Growth channels.** Most big companies rely on only one or two channels. TripAdvisor and Pinterest grew through SEO. Airbnb grew through referrals. The choice depends on the product: rare behaviors (insurance, doctor visits) drive users to Google; social products require viral loops and referrals; products with paying customers can invest in paid advertising (Google, Facebook, Instagram). The cardinal rule: do not spend on paid marketing before having revenue ([Growth for startups](https://www.ycombinator.com/library/6k-growth-for-startups)). See [[Pricing]] for how price determines which acquisition strategies are viable.

## Cohort Retention: The Definitive Measure

Lieb provides the deepest treatment of cohort retention measurement in the YC library ([How to improve cohort retention](https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention)). The method tracks what fraction of new users (grouped by acquisition date) keep using the product over time. Three elements must be defined: how to group cohorts (typically by week or month of first use), what action counts as "active" (not just opening the app -- something correlated with real value), and the time period for measurement (daily for social apps, weekly for utilities, quarterly for travel).

**The only thing that matters is whether the curve gets flat.** A product that retains 20% of users forever is healthier than one that retains 75% at week three but trends to zero. Google Photos retained only 20% of users initially, but that flat curve gave Lieb confidence that they would eventually reach a billion users -- and they did in four years.

**Common ways to fool yourself:** (1) Picking too large a time period (quarterly instead of weekly) makes curves artificially flat. Lieb admits Bump did this -- switching from weekly to quarterly to make retention look better for investors. (2) Picking too easy an action (app opens instead of meaningful usage). Google+ counted users who saw a notification bell in Gmail as "active." (3) Looking at a single data point instead of the full curve shape. (4) Using "is paying" alone -- users stop using a product before they cancel their subscription.

**How to improve retention:** Improve the product itself (new use cases, reduced latency, simpler flows). Acquire better users -- targeting the wrong audience can tank retention even with a good product. Improve onboarding and activation. Build network effects where each new user makes the product better for existing users. The Holy Grail is cohort curves that not only flatten but increase over time.

## Competitive Advantage Over Time

Altman argues that every startup needs a plan for long-term competitive advantage -- network effects, economies of scale, or defensible technology ([How to succeed with a startup](https://www.ycombinator.com/library/89-how-to-succeed-with-a-startup)). Startups beat big companies in three situations: ideas that sound bad but are good (one "yes" from an investor beats needing every layer of a big company to agree), fast-changing markets (more decisions compound in the startup's favor), and big platform shifts (big companies turn the battleship too slowly). These windows create the conditions for explosive growth.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [Startup = Growth](https://www.ycombinator.com/library/8s-startup-growth) | Paul Graham | Startup = Growth; weekly rate as compass; S-curve; compound math |
| [Default alive or default dead](https://www.ycombinator.com/library/95-default-alive-or-default-dead) | Paul Graham | Growth trend as input to alive/dead calculation |
| [Do things that don't scale](https://www.ycombinator.com/library/96-do-things-that-don-t-scale) | Paul Graham | Compound growth from small initial user bases |
| [The hardest lessons for startups to learn](https://www.ycombinator.com/library/8w-the-hardest-lessons-for-startups-to-learn) | Paul Graham | Release early to start the growth clock |
| [Before growing your startup](https://www.ycombinator.com/library/4p-before-growing-your-startup) | Sam Altman | Don't grow before the product is loved; leaky bucket problem |
| [How to set up, hire, and scale a growth strategy and team](https://www.ycombinator.com/library/59-how-to-set-up-hire-and-scale-a-growth-strategy-and-team) | Anu Hariharan, Gustaf Alstromer | Growth teams, retention-first, absolute goals, experimentation at scale |
| [Growth for startups](https://www.ycombinator.com/library/6k-growth-for-startups) | Gustaf Alstromer | Retention as PMF measure, growth channels, conversion funnels, paid growth rules |
| [How to improve conversion rates](https://www.ycombinator.com/library/6l-how-to-improve-conversion-rates) | Kevin Hale | Knowledge gap framework, magic moment, seven questions for any page |
| [How to succeed with a startup](https://www.ycombinator.com/library/89-how-to-succeed-with-a-startup) | Sam Altman | Competitive advantage, startups vs. big companies, platform shifts |
| [How to improve cohort retention](https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention) | David Lieb | Flat curves matter most; three elements of measurement; common self-deceptions |

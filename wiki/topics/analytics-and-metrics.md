---
title: Analytics and Metrics
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["analytics", "metrics", "KPIs", "measuring product", "startup analytics", "data-driven", "retention metrics"]
related: ["[[Product-Market Fit]]", "[[Growth]]", "[[Product Development]]"]
sources: ["8H-analytics-for-startups", "8C-how-to-measure-your-product", "6k-growth-for-startups", "5l-how-not-to-fail", "KR-key-startup-metrics", "KT-consumer-startup-metrics"]
speakers_referenced: ["Ilya Volodarsky", "Suhail Doshi", "Gustaf Alstromer", "Jessica Livingston", "Tom Blomfield"]
---

# Analytics and Metrics

The YC canon treats measurement as inseparable from [[Product Development]]. Volodarsky (Segment co-founder) argues that analytics serves three functions: testing [[Product-Market Fit]], focusing the team on the right problems, and operating data-driven teams at scale ([Analytics for startups](https://www.ycombinator.com/library/8H-analytics-for-startups)).

## The Growth Formula

Doshi (Mixpanel founder) breaks growth into five measurable components: page/app visits, signups, valuable actions taken, users returning, and users spreading the product. These five levers explain nearly all growth and can diagnose any problem in the business. He warns against overcomplicating metrics: "Just picking three to five things as your North Star and really simplifying it will do more good for you" ([How to measure your product](https://www.ycombinator.com/library/8C-how-to-measure-your-product)).

## Three Core Metrics

Volodarsky recommends tracking three metrics from day one:

**Acquisition:** New signups per week, segmented by organic vs. invited users. Set weekly goals and track progress on a visible dashboard.

**Retention:** Cohort analysis -- what percentage of users from a given week are still active N weeks later? A product with PMF shows a retention curve that flattens. A product without PMF shows a curve that declines to zero. Volodarsky suggests targeting at least 20-30% retention at the four-week mark.

**Revenue:** Weekly new revenue, measured as MRR for subscription businesses or transaction value for commerce businesses.

Livingston simplifies further: "You make what you measure. Pick a number you want to grow, and focus on that. The best metric to choose is good old fashioned revenue" ([How not to fail](https://www.ycombinator.com/library/5l-how-not-to-fail)).

## Choosing Your Retention Metric

Alstromer explains that the retention metric must represent real value delivery. Airbnb measures bookings (annually). Instagram measures daily opens. Gusto measures payroll runs (biweekly). The metric must match expected usage frequency. Measuring the wrong action or the wrong time window produces misleading results ([Growth for startups](https://www.ycombinator.com/library/6k-growth-for-startups)).

## Making Data Visible

Volodarsky strongly recommends putting metrics on a TV dashboard in the office. "This is kind of the difference between being a data-driven team and not a data-driven team." The next wave of employees will also orient around visible metrics. Complementing the dashboard, founders should send regular update emails to advisors that synthesize performance and identify where the business is struggling.

## Practical Tactics

Doshi recommends measuring three things in order: (1) Do people understand what the product is? (measured by signup rate from landing page), (2) Is it easy to get started? (measured by completion of first valuable action), and (3) Are people coming back? (measured by retention). He shares that Mixpanel did not implement a "forgot password" feature for 18 months because the team ruthlessly prioritized actions that mattered to the core experience.

Volodarsky describes the "43-minute founder email" -- an automated email sent shortly after signup from a founder's personal address, welcoming the user and offering direct help. Segment received hundreds of thousands of responses to this email over years.

## B2B Metrics Deep Dive

Blomfield adds two metrics essential for B2B SaaS: net dollar retention and gross margin ([Key startup metrics](https://www.ycombinator.com/library/KR-key-startup-metrics)).

**Net dollar retention** measures whether a cohort of paying customers generates more or less revenue over time. If ten customers each paying $10K/month produce $110K twelve months later (after churn and upsells), that is 110% NDR. Early B2B SaaS should target 125-150% NDR. Below 100% means the business is filling a leaky bucket.

**Gross margin** -- revenue minus cost of goods sold -- has become critical for AI companies where foundation model API costs are a significant variable cost. Blomfield warns that hiding behind free OpenAI credits masks real costs. Operationally intensive businesses (grocery delivery, house painting) may have 5-15% gross margins, making it far harder to sustain growth. Scaling negative unit economics requires enormous capital and a concrete plan to flip margins, as Monzo did by moving from -30 pounds per customer to +30 pounds.

Every investor update should include three numbers at the top: revenue, burn rate (monthly costs minus revenue), and runway (months of cash remaining). Blomfield states: "If they're not at the top of your investor updates, honestly, I always assume this founder has something to hide."

## Consumer Metrics Deep Dive

For consumer startups, Blomfield identifies different priorities ([Consumer startup metrics](https://www.ycombinator.com/library/KT-consumer-startup-metrics)):

**Growth rate benchmarks:** 15% month-over-month is good (5x per year). 10% is okay (3x per year). 5% is unlikely to reach breakout success.

**Organic vs. paid growth:** The best consumer companies get 80%+ of growth organically through viral loops and network effects. A 50/50 split is acceptable. Below 50% organic is dangerous because ad platforms extract maximum value from competing companies, driving margins to zero.

**The magic moment:** A user behavior that predicts long-term retention. Facebook: adding 7 friends in the first 10 days. Monzo: adding 3 friends from the phone book. Once identified, re-engineer the onboarding flow to push users toward this moment as fast as possible.

**Net Promoter Score:** For new consumer companies, Blomfield argues +50 NPS is a minimum baseline. Monzo hovered at +75 to +80. Tesla is at +96. Old incumbents like banks and cell phone companies are often at zero or negative -- a signal of disruption opportunity. Consistency of measurement is critical; changing when or where the question is asked will invalidate comparisons.

## Vanity Metrics

Blomfield warns against metrics that look impressive but do not tie to business success: GMV, gross transaction value, registered users, page views. A Middle Eastern neo-bank reported 50% growth in gross transaction value every two weeks while revenue was flat for months -- the founders were signing bigger customers with massive cashback rebates. One YC founder sent ten monthly investor updates with zero revenue as the top-line number. Blomfield calls this impressive rather than shameful: "She kept herself honest."

## The KPI Trap in Pivoting

Flora describes running Color Lovers for eighteen months post-YC without a main KPI. The company tried ads, software, contests -- "all kinds of crazy non-repeatable things" -- without tracking whether any worked. Once they pivoted to Creative Market (a design asset marketplace), the KPI was clear: are people buying, and is that number growing? Flora recommends founders who cannot immediately identify their main KPI should consider whether they need to [[Pivoting|pivot]] ([Pivot stories](https://www.ycombinator.com/library/Iy-yc-s-group-partners-share-their-favorite-pivot-stories)).

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [Analytics for startups](https://www.ycombinator.com/library/8H-analytics-for-startups) | Ilya Volodarsky | Funnel setup, three core metrics, TV dashboards, 43-minute email |
| [How to measure your product](https://www.ycombinator.com/library/8C-how-to-measure-your-product) | Suhail Doshi | Growth formula, simplify to 3-5 metrics, understand-start-return framework |
| [Growth for startups](https://www.ycombinator.com/library/6k-growth-for-startups) | Gustaf Alstromer | Retention as PMF measure, cohort analysis methodology |
| [How not to fail](https://www.ycombinator.com/library/5l-how-not-to-fail) | Jessica Livingston | Revenue as best metric; growth prevents denial |
| [Key startup metrics](https://www.ycombinator.com/library/KR-key-startup-metrics) | Tom Blomfield | NDR, gross margin, revenue/burn/runway in every update |
| [Consumer startup metrics](https://www.ycombinator.com/library/KT-consumer-startup-metrics) | Tom Blomfield | Magic moments, NPS, organic vs. paid, unit economics |
| [Pivot stories](https://www.ycombinator.com/library/Iy-yc-s-group-partners-share-their-favorite-pivot-stories) | Brad Flora | No main KPI = should consider pivoting |

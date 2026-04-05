---
title: Product Development
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["product development", "building product", "feature prioritization", "MVP", "product process", "iteration", "shipping", "minimum viable product", "lean MVP"]
related: ["[[Early-Stage Tactics]]", "[[Growth]]", "[[Product-Market Fit]]", "[[Talking to Users]]"]
sources: ["8p-how-to-prioritize-features", "8w-the-hardest-lessons-for-startups-to-learn", "4e-guide-to-product-development", "4D-yc-s-essential-startup-advice", "6f-how-to-plan-an-mvp", "8a-the-5-things-that-kill-startups-post-seed-rounds", "DT-dalton-michael-simple-products-that-became-big-companies", "8C-how-to-measure-your-product", "Ig-dalton-michael-things-that-don-t-scale-the-software-edition"]
speakers_referenced: ["Emmett Shear", "Paul Graham", "Michael Seibel", "Suhail Doshi", "Dalton Caldwell", "Paul Buchheit"]
---

# Product Development

The YC canon on product development is dominated by one principle: release early and iterate. Graham writes, "I've seen a lot of startups die because they were too slow to release stuff, and none because they were too quick" ([The Hardest Lessons for Startups to Learn](https://www.ycombinator.com/library/8w-the-hardest-lessons-for-startups-to-learn)).

## The MVP

Seibel defines an MVP as "something ridiculously simple -- the first thing you can give to the very first set of users you want to target, in order to see if you can deliver any value at all" ([How to plan an MVP](https://www.ycombinator.com/library/6f-how-to-plan-an-mvp)). Most MVPs should be buildable in weeks, not months. Airbnb launched without payments and without a map view; Nate was working part-time. Twitch launched as Justin.tv with one channel and barely recognizable video quality. Stripe (then /dev/payments) had no bank deals and the founders would visit your office to integrate it for you.

Seibel offers four hacks for building an MVP quickly: time-box the spec (what can you build in three weeks?), write the spec down (so you notice when you change it), cut features aggressively, and do not fall in love with the MVP. "You wouldn't fall in love with a paper you wrote in the first grade."

For hard tech, biotech, or heavily regulated industries, the MVP may start as nothing more than a simple website explaining what you do. Seibel notes these "heavy MVPs" can paradoxically be faster than lean MVPs because the website takes days, not weeks.

## Release Early, Iterate Fast

Graham argues that the primary job of a startup is to pump out features, collect user feedback, and iterate ([The Hardest Lessons for Startups to Learn](https://www.ycombinator.com/library/8w-the-hardest-lessons-for-startups-to-learn)). Waiting for perfection is a form of procrastination. The product will always feel unfinished -- the question is whether users find it useful enough to keep coming back. This connects directly to the [[Early-Stage Tactics]] principle that startups die from slowness, not speed.

## The Two-Week Cycle

Shear describes the development process at Twitch (then Justin.tv): strict two-week cycles where no item could last into the next cycle ([How to Prioritize Features](https://www.ycombinator.com/library/8p-how-to-prioritize-features)). If a feature was too large, it was broken into smaller chunks. This created constant shipping cadence and prevented scope creep.

Within each cycle, the team set three goals (e.g., increase content creation, acquire new users, improve retention) and selected features that mapped to those goals. Features were graded Easy/Medium/Hard for engineering effort, and the team used consensus-based prioritization.

## Slow Product Development Kills

Seibel identifies slow product development as one of the five things that kill startups post-seed ([The 5 things that kill startups post seed rounds](https://www.ycombinator.com/library/8a-the-5-things-that-kill-startups-post-seed-rounds)). Common causes: no process for deciding what to build, no sprints or deadlines, no written specs, engineers excluded from product decisions, no metrics, stopped talking to customers, and "fake Steve Jobs" product founders who believe they know what customers want without asking.

Preventive measures: have a repeatable product development cycle, always collect qualitative and quantitative feedback, write specs, use product management software, include the whole team in brainstorms (especially under eight people), give all team members access to customers and data, and manage motivation as a multiplier on talent. The product lead's job is not deciding what to build -- it is making sure that what the team decides to build actually ships.

## The 90/10 Solution

Buchheit, inventor of Gmail, introduced the principle of getting 90% of the benefit for 10% of the work ([Things that don't scale, the software edition](https://www.ycombinator.com/library/Ig-dalton-michael-things-that-don-t-scale-the-software-edition)). Gmail itself began as a hack -- Buchheit put his own email into a Google Groups UI because he did not want to use Outlook. He built features only as he needed them: writing emails, then multi-user support. Gmail's invite system was not a growth hack -- it was a constraint because they ran out of hard drive space. Caldwell calls this the software edition of [[Do Things That Don't Scale]].

## Analytics-First

Shear argues that no feature should be released without releasing the analytics for it ([How to Prioritize Features](https://www.ycombinator.com/library/8p-how-to-prioritize-features)). Before building, the team defined the specific measurable result they wanted.

Doshi from Mixpanel reduces product measurement to three questions: is the product easy to understand (do people sign up?), is it easy to get started (do they complete the first action?), and are people coming back ([How to measure your product](https://www.ycombinator.com/library/8C-how-to-measure-your-product))? He recommends picking three to five North Star metrics. Even thousand-person companies get this wrong by overcomplicating measurement -- "all data is contestable." See [[Growth]] for how weekly growth rate serves as the ultimate arbiter.

## Hold the Problem Tightly

Seibel draws a sharp line between iterating on the solution and pivoting: "Hold the problem you're solving tightly, hold the customer tightly, hold the solution you're building loosely" ([How to plan an MVP](https://www.ycombinator.com/library/6f-how-to-plan-an-mvp)). If the screwdriver does not help the mechanic, keep the mechanic, keep the problem, fix the screwdriver. This connects to [[Talking to Users]] -- ask about problems, not features.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [6f-how-to-plan-an-mvp](https://www.ycombinator.com/library/6f-how-to-plan-an-mvp) | Michael Seibel | MVP definition, time-boxing, Airbnb/Twitch/Stripe day-one examples |
| [8p-how-to-prioritize-features](https://www.ycombinator.com/library/8p-how-to-prioritize-features) | Emmett Shear | Two-week cycles, three goals, Easy/Medium/Hard, analytics-first |
| [8w-the-hardest-lessons-for-startups-to-learn](https://www.ycombinator.com/library/8w-the-hardest-lessons-for-startups-to-learn) | Paul Graham | Release early; pump out features; don't wait for perfection |
| [8a-the-5-things-that-kill-startups-post-seed-rounds](https://www.ycombinator.com/library/8a-the-5-things-that-kill-startups-post-seed-rounds) | Michael Seibel | Slow product development as killer; process and motivation |
| [DT-dalton-michael-simple-products-that-became-big-companies](https://www.ycombinator.com/library/DT-dalton-michael-simple-products-that-became-big-companies) | Dalton Caldwell, Michael Seibel | Simple products beat feature-rich broken ones |
| [8C-how-to-measure-your-product](https://www.ycombinator.com/library/8C-how-to-measure-your-product) | Suhail Doshi | Three questions for product measurement; 3-5 North Stars |
| [Ig-dalton-michael-things-that-don-t-scale-the-software-edition](https://www.ycombinator.com/library/Ig-dalton-michael-things-that-don-t-scale-the-software-edition) | Dalton Caldwell, Michael Seibel | 90/10 solution; Gmail origin story |
| [4D-yc-s-essential-startup-advice](https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice) | Y Combinator | Build something people want, talk to users |

---
title: "Segment: From Classroom Tool to Customer Data Platform"
type: case-study
created: 2026-04-18
last_updated: 2026-04-18
aliases: ["Segment", "Segment case study", "Segment.io", "analytics.js", "Peter Reinhardt Segment", "customer data platform"]
related: ["[[Product-Market Fit]]", "[[Pivoting]]", "[[Peter Reinhardt]]", "[[Startup Ideas]]", "[[Simple Products]]"]
sources: ["86-how-to-start-a-startup-finding-product-market-fit"]
speakers_referenced: ["Peter Reinhardt"]
---

# Segment: From Classroom Tool to Customer Data Platform

Segment (YC S11) is a customer data platform that helps companies collect data from mobile apps and websites and route it to analytics, marketing, and data warehouse tools. Co-founded by [[Peter Reinhardt]], Ilia, Calvin, and Ian, the company grew from four people to 150 in three and a half years after finding [[Product-Market Fit]]. Segment's story is one of the most detailed case studies of the PMF search process in the YC canon -- including two failures, a near-death experience, and a breakthrough from 580 lines of code [1].

## Attempt 1: The Classroom Lecture Tool (ClassMetric)

Segment's original product was designed for exactly the kind of lecture in which Reinhardt was speaking [1]. The problem: professors standing in front of a class had no idea whether students understood the material. The solution: give students a button to push -- "I'm confused" or "I get it" -- with a real-time graph visible to the professor.

The team wrote "hundreds of thousands of lines of code." They went to Stanford and Berkeley campuses, ambushing professors after class. "We pounced on this professor right after Berkeley" [1]. Professors agreed to test it for a few lectures, "sort of out of pity" [1].

The team believed this was product-market fit. It was not. When they stood in the back of the classroom and looked at student screens, "none of them were using the product" [1]. Students had opened their laptops and immediately turned to other things. The technology itself was the distraction. "Basically, putting a laptop into the classroom was the most distracting thing you could conceivably do" [1].

The deeper signal had been visible earlier: professors did not actively want the tool. They agreed to test it, but that is "not the same thing as product market fit where they're like, 'Holy crap, that solves this problem that I have'" [1].

Four weeks after investors signed checks from YC Demo Day, Reinhardt called them back: "By the way, it turns out this is a terrible idea. We're going to do something else. Do you want your money back?" Most investors did not take their money back, saying they had invested for the team [1].

## Attempt 2: The Analytics Tool

The team pivoted to an analytics tool, reasoning that they should have been able to detect their own lack of PMF through data rather than physically standing in classrooms [1].

They read "The Lean Startup" and went out to talk to customers. Again and again, potential customers were "vaguely interested" -- willing to meet for coffee, willing to receive product updates. "And so we thought, 'This must be it, right? This must be product market fit where people are interested in what we're doing.' Again, this is not product market fit. This is idle interest. Very, very big difference" [1].

Based on this idle interest, the team spent six months writing code. Reinhardt went on one sales trip and found potential customers were happy with Mixpanel and Google Analytics but had edge-case feature requests. "I tricked myself into believing that these little edge cases were actually a really wide gap" [1].

The team kept almost reaching PMF. "If we just ship one more feature, one more thing, we're going to get to product market fit. Again, bad idea" [1].

By December 2012, after a year and a half, $500,000 had been spent with nothing to show. The founders met with Paul Graham at YC. Walking around the cul-de-sac on Pioneer Way, Graham stopped, looked at them, and said: "So just to be clear, you've spent half a million dollars and you have nothing to show for it" [1]. They had $100,000 left -- one more shot.

## The Breakthrough: Analytics.js

The breakthrough came from the least likely source -- a tiny internal tool the team had built during YC's first week [1]. When evaluating analytics tools (Kissmetrics, Google Analytics, Mixpanel), the founders noticed that while the outputs differed, the input data was the same. Rather than choosing one tool, they wrote roughly 100 lines of code to send data to all three simultaneously, translating between their APIs [1].

This library was improved incrementally over months. Later, when trying to sell their own analytics tool, the team kept hitting the objection: "I already have Mixpanel installed." Co-founder Ilia suggested adding their own analytics tool as a fourth destination in the library, using it as a growth hack to overcome the sales objection [1].

Something unexpected happened: people loved the library but did not want the analytics service. "The library is fantastic. I just don't really want to use your analytics service" [1]. The library accumulated GitHub stars and pull requests -- "the first time we'd ever felt like people were just finding this thing and doing something with it" [1].

The day after the Graham meeting, co-founder Ian proposed: "Remember that analytics JS library that has been idling on GitHub? I think that could be a big business" [1]. Reinhardt's reaction: "You've got to be kidding me. That's the worst idea I've ever heard. First of all, it's open source, and second of all, it's 580 lines of code. So who the heck is going to pay for that?" [1].

To kill the idea, Reinhardt proposed a test: build a landing page, put it on Hacker News, and see if anyone signs up [1].

It went straight to the top. 300 upvotes on Hacker News. Thousands of GitHub stars. People reached out on LinkedIn demanding beta access: "What does a brother have to do to get bumped up on your beta list?" [1].

"Full stop. Like, compare this to everything previously. Everything changed" [1]. Every metric went haywire. The team no longer had to search for what to build next -- thousands of users told them exactly what integrations they needed. "It flips from being something that you're like pushing against the customer to all of a sudden the customer is running away with it and you're like wait, hold on, it's not quite ready yet" [1].

## The Business Underneath the Open Source

The open source library alone did not fully solve the problem [1]. The real pain point was organizational: marketing teams kept bringing engineering departments contracts with new analytics tools (email marketing, Adobe Analytics) and demanding implementation. Engineers had roadmaps to execute and resented the interruption. The hosted version of Segment let engineers do a single implementation while marketers pushed buttons in Segment's interface to route data wherever they needed [1].

The open source version still required engineer involvement for each new tool. The hosted version eliminated that. "In some ways we got lucky that the open source version doesn't fully solve the problem" [1].

## Subsequent PMF Discoveries

Segment found product-market fit twice more after the initial breakthrough [1]:

**Redshift integration.** The team noticed all business-tier customers were using the S3 integration. Reinhardt visited five customers in New York and asked what they were doing with the data. Five out of five described the same workflow: a data engineering team taking S3 data, converting to CSV, managing schema translation, and uploading to Amazon Redshift. By the third identical answer, Reinhardt knew what to build. The Redshift integration launch caused "almost every metric in the business to go nuts" [1].

**The customer reaction test.** Five months before the lecture, Reinhardt pitched five product ideas to a large customer. Four received polite interest: "That's great. I totally understand what the value is." On the fifth, the customer interrupted, turned to a colleague, and started scheduling follow-up meetings with multiple teams. "That is the feeling of product market fit" [1].

## Pricing Discovery

Segment underpriced for a long time because the founders conflated code complexity with business value [1]. A sales adviser pushed Reinhardt to ask for $120,000 per year. "I'm like, 'That's crazy.'" The adviser threatened to quit. Reinhardt asked, turned red, and the customer negotiated down to $18,000. Over time, the ask became normal. Some customers now pay over $100,000 per year [1]. "The size of the business problem has almost nothing to do with the amount of code written" [1].

## Vision vs. Market

Reinhardt draws a consistent lesson across all three attempts [1]. With the lecture tool and the analytics tool, the team started with a vision of the future and tried to build a product to match. With analytics.js, they started with a "tiny little library" that solved a real problem and had "no vision associated with it whatsoever at the beginning" [1]. The market does not care about vision. "The market wants what it wants, and it will win every time" [1].

## References

1. [How to Start a Startup: Finding Product-Market Fit](https://ycombinator.com/library/86-how-to-start-a-startup-finding-product-market-fit) -- [[Peter Reinhardt]] (2017)

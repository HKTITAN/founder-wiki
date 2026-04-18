---
title: Enterprise Sales
type: topic
created: 2026-04-05
last_updated: 2026-04-18
aliases: ["enterprise sales", "selling to enterprises", "B2B sales", "enterprise deals", "elephant hunting", "complex sales", "building for the enterprise", "enterprise software"]
related: ["[[Growth]]", "[[Product-Market Fit]]", "[[Series A Fundraising]]", "[[Scaling and Later-Stage Operations]]", "[[Selling to Startups]]", "[[Why Now]]", "[[Simple Products]]", "[[Box: From Consumer Cloud Storage to Enterprise Platform]]"]
sources: ["4m-enterprise-sales-for-hackers", "6a-on-starting-and-scaling-direct-mail-automation-startup-lob", "73-how-to-start-a-startup-building-for-the-enterprise"]
speakers_referenced: ["Ryan Junee", "Harry Zhang", "Kevin Hale", "Aaron Levie"]
---

# Enterprise Sales

This article covers two distinct aspects of enterprise sales: the mechanics of selling to large companies (Junee's "enterprise sales for hackers" framework), and the strategy of building enterprise software companies (Levie's lessons from Box).

## Building for the Enterprise (Aaron Levie)

Aaron Levie, CEO and co-founder of Box, describes the decision to pivot from consumer to enterprise as painful but ultimately transformative [3]. Box started in 2005 as a consumer file-sharing product. Consumers paid at most $9.99 per month, and the founders could see that Google, Facebook, Apple, and Microsoft would eventually give everyone free storage [3]. On the enterprise side, companies were spending millions or tens of millions of dollars on legacy software that Box could deliver for hundreds of thousands -- a 10 to 20x cost improvement [3].

The decision took longer than it should have. "It actually took us a surprising amount of time to come to the conclusion that we needed to go into the enterprise because we still were like, 'Well, yeah, but what if we could serve advertising on the files or something?'" [3]. The advertising model failed the common-sense test: "You really don't want to see ads when you're looking at your tax documents" [3].

### Why Enterprise Software Was Broken

Levie catalogs the failures of traditional enterprise software circa 2005-2007 [3]:

- **Slow innovation.** Enterprises wanted predictability, so vendors shipped product updates once a year or once every three years. This repelled talent and slowed innovation.
- **Complex technology.** The incentive structure rewarded feature density over simplicity because the buyer (CIO) did not bear the complexity cost -- the end user did.
- **Sales-driven distribution.** Product adoption required salespeople because customers could not access the technology on their own.
- **Proprietary, closed systems.** Platforms did not integrate with each other.
- **Customer bears the risk.** Customers bought licenses upfront regardless of actual usage. "You'd see all the time enterprises that would spend $10 million on software and never install it" [3].
- **Security as aftermarket.** Customers bought infrastructure, then software, then security software to secure the software. The customer was responsible for assembling it all.

### The New Enterprise Model

Box built the inverse of each failing [3]:

- **Simple, end-user-focused technology.** "If you were in classic enterprise software, you would have looked at our product and you would have thought it was a toy" [3]. That simplicity was the disruption.
- **Product-led adoption.** End users pulled the technology into organizations. Sales closed big deals but did not drive initial adoption. Slack is "the perfect quintessential example of a viral enterprise software product" [3].
- **Available to all sizes.** Small businesses, startups, and Fortune 500 companies could all use the product.
- **Security baked in.** The vendor bore responsibility for security.
- **Vendor bears the risk.** Subscription model means the customer stops paying if the product does not work.
- **Open systems.** Integration with other enterprise software.

Box grew to 71,000 customers and 63% of the Fortune 500, "generated mostly because people just at work wanted to bring in better technology" [3].

### Eight Lessons for Building Enterprise Software

Levie distills eight lessons from twelve years at Box [3]:

**1. Start insanely simple.** Resist the instinct to build many features. "You're going to be successful by nailing one use case that just happens to be a use case that everybody has a massive problem with" [3]. That single use case becomes the wedge to expand. Gusto (formerly Zen Payroll) is Levie's model: started with payroll only, then expanded to broader HR services. "Even when you're bigger, you still have to make sure you're really, really focused on keeping things dead simple" [3]. See [[Simple Products]] for the broader principle.

**2. Ride a major technology tailwind.** Box benefited from three mega trends: mobile ubiquity, dropping cost of computing, and internet connectivity. All three were disruptive to incumbents selling traditional enterprise software. "Try and find what are the technology trends that you think incumbents are not going to be able to respond well to, because they are either economically, strategically, or from a talent standpoint not able to leverage those technology trends in the same way that you can" [3]. PlanGrid rode the iPad into the construction industry -- "a pretty dead simple idea" that timed the mobile wave in field-worker environments [3]. See [[Why Now]] for Garry Tan's complementary framework.

**3. Make the product sell itself.** "Your product, in a perfect world, should really literally sell itself" [3]. Box invested heavily in sharing functionality so the software would spread virally. "Sales really should be used to close big deals, not to drive product adoption. And that's a big distinction" from the traditional enterprise software model [3].

**4. Listen to innovative customers, but don't build what they ask for.** The first 5-10% of customers on the innovation bell curve will "see things even before you will about how your technology could be used." Spend significant time with them, but do not build the specific features they request. Instead, "connect the dots between multiple requests or multiple ideas to build a solution that people didn't really even think about previously" [3]. Building exactly what customers ask for creates "this mess of technology" serving different industries with different UX [3]. Salesforce's approach -- modular components that can be mixed and matched -- is the alternative [3].

**5. Never trade user experience for enterprise features.** "Every single one of those decision points, we have made sure that we always favor the end user over the enterprise" [3]. This means losing deals. Over ten years, Box lost "tens of millions of dollars of business because we said no to certain customers." But the companies that went to competitors with more features "ended up being unsuccessful with those products and had to eventually come back to us" [3]. The caveat: "The key point here is you have to be right" [3].

**6. Find asymmetric advantages.** Big incumbents are locked into specific business models with tens of thousands of employees. "If you can find points of differentiation and disruption that they can't respond to, because either it is too expensive for them to respond to or strategically it doesn't make as much sense, that is how you ultimately remain disruptive" [3]. Amazon Web Services disrupted traditional server makers so thoroughly that "twelve years later, they still have not responded" [3].

**7. "People don't know what they want until you show it to them."** Levie invokes Steve Jobs: if Box had asked a hundred IT people to design the ideal document management system, "not in a hundred attempts would our solution have been sort of designed because everybody was so used to the idea that technology has to be really complex" [3].

**8. Understand the disruption opportunity.** Most enterprise technology is still legacy. Every company knows it needs to modernize. "If you're a media company, you're freaking out because of Netflix. If you're a life sciences company, you're freaking out because of 23andMe" [3]. This creates an "unbelievable amount of opportunity" for startups building modern enterprise software.

### Discovering Enterprise Pain Points

When asked how founders without enterprise experience can identify pain points, Levie recommends interviewing roughly a hundred people who work in large companies [3]. "Just walk me through your day. What are all the places where you are less effective, less efficient, having to do repetitive or redundant work? And don't ask for technology problems" [3]. Patterns will emerge. "As soon as you find that gap, that's where you know you can build a company" [3].

### Technology Tailwinds in 2017

Levie identifies AI combined with cheap computing as the most powerful compound trend [3]. Google's new image and video recognition API, available as a simple API call, "would have taken like a hundred engineers five years ago to go build" [3]. The opportunity: "What's the new set of problems that we could use those solutions and build software for?" -- security cameras, image search, data analysis [3].

### Build vs. Buy

Levie's rule: "Anything that is not your core competency, you need to be using the best-in-class outside solution for" [3]. The definition of core competency is not static. Twelve years ago, Box built its own storage infrastructure because no alternative existed. Today, they use Amazon without hesitation. "The moment that the rest of the market catches up and commoditizes something that you used to be good at, you need to get away from that part of the market as fast as possible" [3].

## The People in the System (Ryan Junee)

Ryan Junee argues that enterprise sales requires the same skill set as hacking -- the founder just needs to reframe the problem. Where a computer system is a network of hardware and software, a large enterprise is a network of people and processes. The emergent behavior of a corporation results from incentives and structured rules among its constituent people, much like the output of a computer system results from structured rules and data flows [1].

Enterprise sales, then, involves understanding and influencing the components (people) of the system to produce the desired behavior (buying your product). Every system (company) is different, requiring a systematic approach [1].

This section focuses on early-stage companies selling to Fortune 500 companies in high-touch, complex sales with $1M+ deals -- often called "elephant hunting" [1]. It assumes the company has found [[Product-Market Fit]] or is close to it. For the contrasting approach of starting with smaller customers, see [[Selling to Startups]].

### Champion

A champion is an ally within the target company who has deep familiarity with the pain the product solves. "When you give your pitch, you will find the champion nodding along and completing your sentences for you" [1]. Champions will do everything they can to get the product deployed. Their influence depends on seniority -- line-level champions are useful, but director-level and above are necessary. Champions may become so excited they want to quit and join the startup (Junee reports this happening multiple times). "These people are gold. Find them early and build strong relationships quickly" [1].

### Detractor

The opposite of a champion. Detractors oppose deployment for various reasons: it threatens their job, they are invested in a competing product, or they built the current solution. The strategy is to stay off their radar and rally enough support from champions and other parts of the organization to overpower them [1].

## References

1. [Enterprise Sales for Hackers](https://www.ycombinator.com/library/4m-enterprise-sales-for-hackers) -- Ryan Junee (n.d.)
2. [On Starting and Scaling Direct Mail Automation Startup Lob](https://ycombinator.com/library/6a-on-starting-and-scaling-direct-mail-automation-startup-lob) -- [[Harry Zhang]] (n.d.)
3. [How to Start a Startup: Building for the Enterprise](https://ycombinator.com/library/73-how-to-start-a-startup-building-for-the-enterprise) -- Aaron Levie (2017)

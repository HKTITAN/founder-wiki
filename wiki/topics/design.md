---
title: Design
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["design", "product design", "startup design", "design for founders", "design taste", "designer founders"]
related: ["[[Product Development]]", "[[Founder Mindset]]", "[[Vibe Coding]]"]
sources: ["MK-why-every-founder-should-care-about-design", "7G-design-for-startups-part-1", "7H-design-for-startups-part-2", "Lj-why-design-matters-lessons-from-stripe-lyft-and-airbnb", "MR-ai-apps-are-broken-here-s-how-to-fix-them", "MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters", "MP-how-ai-coding-agents-will-change-your-job", "LO-how-nothing-founder-carl-pei-built-a-multi-million-dollar-smartphone-brand-in-just-2-years", "Jv-building-a-better-mobile-app", "Ls-twitter-vs-x-product-lessons-for-startup-founders"]
speakers_referenced: ["Raphael Schaad", "Aaron Epstein", "Garry Tan", "Katie Dill", "Pete Koomen", "Michael Truell", "Tom Blomfield", "David Lieb", "Carl Pei"]
---

# Design

YC's Gary Tan has called good design in early-stage startups "a lost art." Schaad, head of Calendar at Notion and founder of Cron (acquired by Notion), argues that designers are uniquely qualified to start companies because design is fundamentally about figuring out what people want -- the core YC ethos of "make something people want" ([Why every founder should care about design](https://www.ycombinator.com/library/MK-why-every-founder-should-care-about-design)).

## Why Design Matters for Founders

Schaad frames successful products as requiring three overlapping qualities: desirability (design), viability (business), and feasibility (technology). Design maps directly to desirability -- understanding what users want and how they want to interact with it.

He extends the common definition: "Design is not just how it looks, but how it works. I would even take this a step further. Design is how it looks, how it works, but design is how it's built." The technology choices, loading states, latency, and framework selection are all part of the design. Users can feel end-to-end design quality.

## Acquiring Design Taste

Schaad offers three recommendations for engineers and founders who want to develop design sensibility:

1. **Learn by doing.** Producing bad designs teaches why good designs work. Understanding the constraints a designer faced reveals the reasoning behind design decisions.

2. **Surround yourself with well-designed objects.** Physical and digital. Refuse to tolerate poorly designed things. Evaluate every interaction -- doorknobs, software interfaces -- for whether the experience works.

3. **Read design books.** Schaad recommends three: Grid Systems (layout and text), The Elements of Typographic Design (type as interface element), and The Design of Everyday Things (conveying mental models through UI).

Taste is acquired, not learned. Schaad describes it as going through life with a design lens: "Is this a pleasant experience? Is this a reliable design? Is this a lasting design?" In software, this extends to muscle memory, keyboard shortcuts, and adaptive interfaces that improve with use.

## Designers as Founders

Historically, designers did not control the means of production. Software changes this: designers can now build the objects they envision. Schaad's own path from MIT Media Lab to founding Cron illustrates the pattern -- being comfortable in the medium you are building in gives a "huge advantage."

In the AI era, design shifts from nouns (buttons, text fields, sidebars) to verbs (autocomplete, summarize, send an agent). Static prototypes break down because they cannot represent time-dependent, data-driven interactions. Designers who can prototype in code -- or who use AI tools to skip from sketch to working prototype -- gain an edge.

## The Sketch-to-Code Pipeline

Schaad's design process starts with paper sketches. Paper affords total flexibility -- no constraints from design tools or code editors. A sketch captures the insight; the medium does not limit the idea. From sketch, he moves directly to code rather than through intermediate design tools, because he wants to feel whether the interaction works in the real medium.

AI accelerates this pipeline. A sketch can be photographed, uploaded to an AI tool, and turned into a working prototype -- skipping the intermediate Figma step entirely. This makes sketching more valuable, not less: "The value of a sketch actually becomes very important again when you can skip that entire step."

## Design as Trust

Dill, head of design at Stripe (previously Airbnb and Lyft), argues that design plays a distinct role in companies that require high user trust ([Why design matters](https://www.ycombinator.com/library/Lj-why-design-matters-lessons-from-stripe-lyft-and-airbnb)). Stripe handles money, Airbnb involves staying in strangers' homes, Lyft involves riding in strangers' cars. In each case, design details -- a typo, a lost form state, a clumsy layout -- erode the trust that makes the business model work. "If they haven't gotten that detail, what other detail aren't they getting right?"

Dill traces this to the founding teams. Airbnb's founders sweated every detail of the trust experience -- how money was exchanged, how guests and hosts communicated, how listings were visually presented. Stripe's founders cared about every detail of the developer experience. The early design investment built confidence that compounded as these companies scaled.

## Founders Should Do Design Themselves

Tan (former YC partner, Posterous co-founder) taught himself design and spent ten YC batches doing design office hours with more than a thousand founders. His core argument: founders do not need formal design training, but they must understand product design, interaction design, and visual design well enough to do the work themselves pre-Series A ([Design for startups](https://www.ycombinator.com/library/7G-design-for-startups-part-1)).

Tan defines design as making things other people can use. He breaks the discipline into three roles: product manager (prioritization, personas, user stories), interaction designer (flows, wireframes, usability), and visual designer (color, typography, polish). At the earliest stage, one founder fills all three roles. Tan recommends sketching wireframes on paper before building, using real customer quotes to guide prioritization, and testing with five users to find the biggest usability failures.

## When to Hire Designers

Tan provides a staging guide for design hiring ([Design for startups, part 2](https://www.ycombinator.com/library/7H-design-for-startups-part-2)): pre-seed through pre-Series A, a cofounder handles design with occasional consulting help. By Series A, hire the first dedicated designer. By Series B, build a team -- having ten engineers and one designer creates a nightmare for the designer. He warns that the best designers at large companies are accustomed to working alongside other designers and may reject offers from startups that lack a design culture.

For sourcing, Tan recommends Dribbble, Behance, and design school pipelines (CMU, RISD, Parsons, Stanford). For budget-constrained startups, platforms like 99designs or Fiverr can surface talented designers in the early stages of their careers worldwide. The key hiring signal: empathy and communication skill matter more than portfolio polish.

## The AI Horseless Carriage Problem

Koomen argues most AI applications are "horseless carriages" -- they bolt AI into legacy interfaces without redesigning for what AI enables ([AI apps are broken](https://www.ycombinator.com/library/MR-ai-apps-are-broken-here-s-how-to-fix-them)). Gmail's AI draft feature illustrates the failure: a hidden, generic system prompt produces output that sounds like no individual human, and the prompt is roughly as long as the draft itself. The fix requires a new design paradigm: expose system prompts so users can teach the AI how they work. Instead of asking "how do I slot AI into my product," designers should ask "how would I design this tool from scratch to offload as much repetitive work from the user as possible?"

Lieb predicts that smaller AI-enabled teams will produce better-designed products because they eliminate the inter-team interfaces where ownership breaks down ([How AI coding agents will change your job](https://www.ycombinator.com/library/MP-how-ai-coding-agents-will-change-your-job)). When one person or a small group owns the entire experience, the product improves.

## Taste as the Irreplaceable Skill

Truell (Cursor CEO) identifies taste as the one skill AI will not replace: "defining what do you actually want to build" ([Cursor CEO](https://www.ycombinator.com/library/MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters)). He means not just visual taste but taste for how logic works -- the product judgment that determines what is useful. As AI automates more of the "human compilation" step of programming, the taste for what to build and how it should behave becomes the entire job. See also [[Vibe Coding]] for how this plays out in practice.

## Design in Hardware: The Nothing Case Study

Carl Pei built Nothing to $600M annualized revenue in two years by centering design differentiation ([How Nothing founder Carl Pei built a multi-million dollar smartphone brand](https://www.ycombinator.com/library/LO-how-nothing-founder-carl-pei-built-a-multi-million-dollar-smartphone-brand-in-just-2-years)). His co-founder Jasper Bagger from Teenage Engineering taught him: "For every product you make, imagine if a user sees it for two seconds and then has to sketch a defining feature." The Glyph interface (LED patterns on the phone's back) emerged from this principle -- creating an iconic visual signature.

Pei advises hardware founders to be 90% Tim Cook (operations, survival, volume) and 10% Johnny Ive (design risk), increasing the design percentage only as volumes prove the business model. He describes his favorite Apple detail as the volume knob UI on the original iPad with gyroscope-responsive brushed metal reflections: "If Apple cares about such a minute detail, I'll trust them completely because they've really thought through everything else." Design details build trust. See [[Biotech and Deep Tech]] for more on hardware startup challenges.

## Mobile App Design

Epstein and Siegel review five YC startup mobile apps, surfacing principles specific to mobile contexts ([Building a better mobile app](https://www.ycombinator.com/library/Jv-building-a-better-mobile-app)):

**Context matters.** Consider the physical environment: is the user walking, driving, or sitting? Are they holding the phone with one hand? Touch targets should be at least 60 pixels square -- anything smaller fails the "thumb test."

**Get to the aha moment fast.** BlueDot's EV charging app launches directly to a map showing nearby stations -- "points for interaction design." Conversely, BoldVoice's onboarding asked too many questions (language, motivation, referral source) before the user could try a lesson. Each unnecessary step costs users.

**Platform standards.** Stick to native navigation patterns. Non-standard interactions (custom sidebars, novel scrolling) confuse users. Wrapping tab names across two lines, using too-thin icon strokes, and inconsistent animations all signal a web app masquerading as native.

**Color as information.** Use color functionally, not decoratively. Primary CTAs should have a distinct color from secondary actions. If availability status matters (as with charging stations), encode it visually on the map rather than forcing users to tap each icon.

**Watch users in the real world.** Siegel's strongest recommendation: "Get it into users' hands as quickly as possible and ask them to use it and just write down where they trip up." For BlueDot, this means mounting the app on a car dashboard and driving.

## The Engagement Trap

Blomfield and Lieb analyze Twitter/X's evolution as a cautionary tale for consumer product founders ([Twitter vs. X: Product lessons for startup founders](https://www.ycombinator.com/library/Ls-twitter-vs-x-product-lessons-for-startup-founders)). The shift from a chronological feed of chosen topics to an algorithmic engagement-optimized feed illustrates a common failure: optimizing for a single metric (time spent) while degrading user satisfaction.

Blomfield reports: "I'm sure that my engagement is up and my happiness when I go and resume my life is lower." The pattern repeats across social networks -- Facebook's News Feed, Instagram's algorithmic shift, TikTok skipping straight to "show all possible content and let algorithms figure out what the human brain wants to see." Each platform started with tight social connections and evolved toward algorithmic engagement farms.

The product design lesson: founder-CEOs have "moral authority" to resist metric-only optimization. When a product team chases a single number, "you're probably going to lead yourself down one of these rabbit holes." Steve Jobs's willingness to say no to features, even when some decisions were wrong, gave Apple a consistent product identity.

On naming, Blomfield observes: "When your product gets the verb, you've won" -- people said "tweet," "Google it," "Monzo me." Abandoning that for a meaningless letter was, in the hosts' view, indefensible.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| [Why every founder should care about design](https://www.ycombinator.com/library/MK-why-every-founder-should-care-about-design) | Raphael Schaad | Design = desirability; taste is acquired; sketch-to-code pipeline |
| [Design for startups](https://www.ycombinator.com/library/7G-design-for-startups-part-1) | Garry Tan | Founders should learn design; product/interaction/visual breakdown; wireframe-first |
| [Design for startups, part 2](https://www.ycombinator.com/library/7H-design-for-startups-part-2) | Garry Tan | When to hire designers; sourcing; interview techniques |
| [Why design matters](https://www.ycombinator.com/library/Lj-why-design-matters-lessons-from-stripe-lyft-and-airbnb) | Katie Dill | Design as trust; details signal care; Stripe/Airbnb/Lyft examples |
| [AI apps are broken](https://www.ycombinator.com/library/MR-ai-apps-are-broken-here-s-how-to-fix-them) | Pete Koomen | Horseless carriage problem; expose system prompts; user-programmable AI |
| [Cursor CEO](https://www.ycombinator.com/library/MU-cursor-ceo-going-beyond-code-superintelligent-ai-agents-and-why-taste-still-matters) | Michael Truell | Taste is irreplaceable; visual and logic taste both matter |
| [How AI coding agents will change your job](https://www.ycombinator.com/library/MP-how-ai-coding-agents-will-change-your-job) | Tom Blomfield, David Lieb | Smaller teams = better design; clear ownership improves quality |
| [Nothing founder Carl Pei](https://www.ycombinator.com/library/LO-how-nothing-founder-carl-pei-built-a-multi-million-dollar-smartphone-brand-in-just-2-years) | Carl Pei | 90% Tim Cook, 10% Johnny Ive; iconic design in 2 seconds; design builds trust |
| [Building a better mobile app](https://www.ycombinator.com/library/Jv-building-a-better-mobile-app) | Aaron Epstein, David Siegel | Mobile context; 60px touch targets; aha moment; platform standards; watch users |
| [Twitter vs. X: Product lessons for startup founders](https://www.ycombinator.com/library/Ls-twitter-vs-x-product-lessons-for-startup-founders) | Tom Blomfield, David Lieb | Engagement trap; metric-only optimization; founder authority; naming |

---
title: Startup Legal Mechanics
type: topic
created: 2026-04-18
last_updated: 2026-04-18
aliases: ["startup mechanics", "incorporation", "forming a startup", "Delaware C Corp", "83(b) election", "stock purchase agreement", "Clerky", "startup formation", "startup legal", "C Corp", "incorporating a startup"]
related: ["[[Equity Split]]", "[[Seed Fundraising]]", "[[Co-Founders]]", "[[Hiring at Early Stage]]", "[[Kirsty Nathoo]]"]
sources: ["JR-how-to-start-a-startup-startup-mechanics"]
speakers_referenced: ["Kirsty Nathoo"]
---

# Startup Legal Mechanics

[[Kirsty Nathoo]], Managing Director of Finance at Y Combinator, has worked with thousands of companies through all stages of their life, from incorporation to exits. She presents the basic mechanical and legal issues that nearly all startups face in their earliest days [1]. None of this is glamorous, but getting it wrong creates expensive problems that surface at the worst possible moments -- during fundraising rounds or acquisitions.

## When to Incorporate

Incorporation creates a separate legal entity that pays its own taxes, holds its own assets and liabilities, signs its own contracts, and can sue and be sued independently of the founders [1].

The timing question has two failure modes [1]:

**Too soon**: The founders are still throwing around ideas, treating the project as a side project, uncertain about long-term commitment, or unsure about their co-founder relationship. In these situations, incorporating adds administrative burden without benefit [1].

**Too late**: The founders have created significant IP (especially with multiple people contributing), built a product ready to charge for, or entered a situation where personal liability protection matters. At this point, not having a corporate entity creates risk [1].

Stripe Atlas, a YC company product, helps founders form a company, get a bank account, and start accepting payments [1].

## Delaware C Corp: The Default

In the US, the standard structure for a venture-backed startup is a Delaware C Corporation. Nathoo is emphatic: "Investors can only really invest in C Corps" [1]. Other structures (LLCs, etc.) may seem appealing based on advice from non-startup lawyers, but they create conversion headaches later.

Why Delaware specifically [1]:
- Delaware corporate law is highly developed and well understood by all startup lawyers
- Investors expect Delaware companies
- Delaware law provides the most flexibility for issuing shares
- Best privacy protections for owners
- Founders can incorporate in Delaware without being US citizens or physically present in the US

Nathoo's advice: "There's no point trying to do something different. Just go with the herd on this" [1].

## The Connecticut Lawyer Horror Story

A YC company came in as an LLC formed in Connecticut because the founders' friends were Connecticut lawyers. When they needed to convert to a Delaware C Corp, they used those same Connecticut lawyers. Three funding rounds later, a Valley law firm discovered the conversion had been done incorrectly and was legally invalid. The fix took six months, involved four law firms, and cost $500,000 [1].

The moral: use Silicon Valley lawyers who understand startup corporate law, or use Clerky [1].

## How to Incorporate

Incorporation is a two-step process [1]:

**Step 1**: File formation documents with Delaware (about 24 hours to process).

**Step 2**: Adopt bylaws, create a board, appoint directors and officers, assign IP to the company, and issue shares to founders.

Two recommended paths [1]:

**Lawyers**: Costs $3,000-$5,000 plus filing fees. Most Valley startup lawyers defer fees until the company raises money. Best for non-standard situations or high-touch needs.

**Clerky** (YC company): A platform that generates all formation documents through a simple interface. Costs a few hundred dollars plus filing fees. Documents are signed on the platform and stored there. This is where YC sends companies that have been accepted but have not yet incorporated [1].

## Assigning Equity

The equity conversation forces co-founders to discuss expectations and commitment levels. It surfaces issues early -- such as whether one founder expects to work part-time [1].

Nathoo argues for near-equal splits among co-founders. Founders commonly push back with reasons like: "I thought of the idea," "I built the prototype," "I closed the first $20K in sales," or "I started three months before my co-founder" [1].

Nathoo's response: "Everything is ahead of you. This is the early days of the company. If you've worked on it for three months, you've probably got five, ten, fifteen years of this company ahead of you, if it's going to be a success. So think about forwards, not backwards" [1]. See [[Equity Split]] for the full treatment of this topic.

The only potentially valid reason for a slight imbalance is preventing founder deadlock on votes. But Nathoo notes: "If you're at the point where the founders are having to vote their shares to make decisions, then there's probably something more fundamentally broken in the relationship" [1].

Equity split is the number one reason YC sees co-founders break up. Resentment builds in stressful environments when splits feel unfair, and the resulting dispute often consumes so much energy that the company itself struggles to survive [1].

## Stock Purchase Agreements and Paperwork

Founders buy their shares via a stock purchase agreement, typically exchanging a few dollars of cash deposited from their personal bank account into the company bank account [1]. The transaction must be properly documented.

Another YC company horror story: founders incorporated, set up shares, then had to merge into a new company. The share swap appeared to work, but new lawyers discovered years later that the original share purchases had never been properly papered. The founders did not legally own the original shares, which meant the swap was invalid, which meant they did not own the new shares either. Everything done since -- including multiple funding rounds -- was legally questionable [1].

## Vesting

Vesting means earning the right to permanent ownership of shares over time. The standard schedule is four-year vesting with a one-year cliff [1]:

- **Day 1 to Day 365**: All shares are subject to the company's repurchase option
- **Day 365 (the cliff)**: 25% of shares vest immediately
- **Months 13-48**: An additional 1/48th of total shares vest each month
- **End of Year 4**: 100% of shares are vested

If a founder leaves, the company repurchases unvested shares at the original purchase price [1].

Three reasons vesting matters [1]:

1. **Protection for remaining founders**: Without vesting, a co-founder who leaves after six months retains the same ownership as founders who work for another decade. "Meanwhile, the ex-founder is sitting on a beach, drinking cocktails" [1].

2. **Skin in the game**: Creates incentive to stay and work hard. Investors care about this because they are investing in the founders [1].

3. **Sets an example for employees**: Founders cannot credibly require employee vesting while exempting themselves [1].

## The 83(b) Election

The single most important piece of tax paperwork in the incorporation process. Without it, founders are taxed on the increase in value of their shares every time shares vest -- potentially creating enormous personal and company tax liabilities [1].

Filing the 83(b) election with the IRS within 30 days of the share purchase eliminates this problem [1]. It is the one thing in the incorporation process that cannot be fixed retroactively. Nathoo has seen both funding rounds and acquisition deals fall apart because proof of 83(b) filing was missing and the buyer or investor was spooked by potential tax liabilities [1].

"Follow the instructions. Either when you're dealing with lawyers or when you're dealing with Clerky, they will give you instructions about how to complete the form. They will give you instructions about where to send it, how to do it. Just follow those instructions and all will be fine" [1].

## Fundraising Mechanics

### Priced Rounds vs. SAFEs

Startups can raise money on priced rounds (shares sold at a specific price) or unpriced/convertible rounds (money now, shares later). In the US, the typical sequence is: raise first money on SAFEs, then raise a priced round (Series A) later [1].

**SAFE** stands for Simple Agreement for Future Equity. It is a YC-created instrument that is genuinely simple -- a few pages long, no lawyers required, signable and trackable on Clerky [1]. The investor gives money now in exchange for the right to receive shares at a future priced round, with a valuation cap that rewards them for investing at an earlier, riskier stage.

**Example walkthrough** [1]: A company with 9 million founder shares raises $400K on SAFEs with a $4M cap. Later, it raises a $2M Series A at an $8M pre-money valuation. The SAFE conversion price uses the $4M cap ($0.44/share), while Series A investors pay based on the $8M valuation ($0.89/share). The SAFE investor gets twice as many shares per dollar as the Series A investor -- their reward for investing earlier.

**Priced round example** [1]: The same company raises $2M at $8M pre-money. Price per share = $8M / 9M shares = $0.89. The investor buys 2.25M shares. Post-money valuation is $10M. Each founder goes from 33% to 26.7% ownership. The investor holds 20%.

### Dilution

Dilution is inevitable. The key metric is the area of your slice, not the percentage [1]. "In the early days you have a massive slice of a very small pie. And then as the company grows, the size of the pie grows, but your slice becomes smaller" [1].

A common early mistake: selling too much equity at a low valuation when the company does not need the money. Most early spending goes to hiring, but if the company is still finding [[Product-Market Fit]], hiring may be premature [1].

### Get the Money in the Bank

Nathoo emphasizes a practical point that founders overlook: a commitment is not cash. "You've got to keep working on your investors until the money is in the bank" [1].

## Hiring Mechanics

### Contractors vs. Employees

Both contractors and employees assign IP to the company. The key differences [1]:

**Contractors**: Set their own hours, work on defined projects with end goals, use their own equipment, are not involved in day-to-day operations. The company pays them directly with no tax withholding. At year-end, the company issues a Form 1099. Contractors do not need US work authorization if working remotely [1].

**Employees**: Use company equipment, work company hours, have less autonomy, require more supervision. The company withholds taxes and pays them to the IRS, state, and sometimes city agencies. At year-end, the company issues a Form W-2. Employees must have US work authorization [1].

For payroll, Nathoo recommends using a payroll service provider rather than calculating withholdings manually. Gusto (a YC company) is the most commonly used by YC startups [1].

California law requires that employees be paid at least minimum wage. Unpaid labor producing work for the company is not legal [1].

### Employee Equity

Startups should give employees equity to incentivize alignment and compensate for below-market cash salaries [1].

**Rule of thumb**: Reserve approximately 10% of the company for the first 10 employees, on a sliding scale (employee #1 gets more than employee #10) [1]. For the first 5 employees, Nathoo suggests the 7-8% range [1].

All employee equity should vest on the same standard schedule as founder equity. This protects the company if a hire does not work out [1].

Companies typically issue stock options (the right to buy shares in the future at today's price) rather than outright shares to employees. This avoids immediate tax consequences for the employee [1].

**Communication matters**: Founders must understand equity themselves before explaining it to employees. Always communicate both the number of shares and the percentage of the company they represent. One without the other is meaningless [1].

### Spending Responsibly

Company funds belong to the company. Nathoo tells a story of a founder who took company money to Las Vegas, "had a great time according to Facebook," and was fired. Criminal charges were possible [1].

## References

1. [How to Start a Startup: Startup Mechanics](https://ycombinator.com/library/JR-how-to-start-a-startup-startup-mechanics) -- [[Kirsty Nathoo]] (2014)

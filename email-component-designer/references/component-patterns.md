# Designing Email Marketing Components

This document defines the design standards for creating email marketing components for our brand. Every component should feel premium, intentional, sales-focused, and visually engaging. We are not creating plain informational blocks — we are creating conversion-driven email sections that make customers want to click, shop, and act.

---

## 1. Brand Colour Usage

### 1.1 Use Colours From the Logo Folder

When designing any email component, first check the `logo/` folder.

Use the logo assets to extract or infer the brand colour scheme. The logo colours should guide:

- Background colours
- Button colours
- Accent colours
- Border colours
- Badge colours
- Gradient choices
- Highlight text
- Decorative elements

The email should feel connected to the brand visually, not like a generic template.

### 1.2 Build a Colour Palette Before Designing

Before creating components, define a simple palette based on the logo:

```txt
Primary Colour:
Secondary Colour:
Accent Colour:
Dark Background:
Light Background:
Text Colour:
CTA Colour:
```

---

## 2. Design Philosophy — Sell, Don't Tell

**NEVER output plain text on a flat background.** That is not a component — that is a paragraph. Every email block must be a visual experience that drives action.

### 2.1 Every Component Must Have Visual Depth

A single component should layer multiple visual elements together. Think like a designer, not a copywriter. Combine:

- **Badges / Tags** — "LOYALTY MEMBER", "EXCLUSIVE", "VIP ACCESS" — styled as pill shapes or ribbon banners
- **Data points / Stats** — Show numbers prominently: points balances, savings amounts, member tier, order counts. Numbers sell. Use large bold type with supporting micro-labels
- **Progress indicators** — Bars, steps, tier trackers. Show the customer where they are and where they could be
- **Visual dividers & accents** — Decorative lines, dots, diamond separators, gradient borders. Break up sections with intention
- **Micro-icons via HTML/CSS** — Use CSS shapes (circles, triangles, stars via borders), unicode symbols, or box-drawing characters as lightweight visual elements
- **Colour blocking** — Split sections into distinct colour zones. Use contrasting panels side-by-side or stacked
- **Urgency elements** — Countdown-style layouts, "limited time" ribbons, expiry dates styled as stamps
- **Social proof cues** — Star ratings in HTML, review counts, "X customers bought this" counters
- **Layered containers** — Cards within cards. Inset panels with different backgrounds. Bordered highlight boxes inside the main block

### 2.2 The Purple Cow Rule — Headlines Must Stop the Scroll

Apply Seth Godin's Purple Cow theory: if a customer sees a regular cow they glance once, if they see a purple cow they stare. **Your headline IS the purple cow.**

Headlines must be:

- **Large but email-safe** — target `54px` – `62px` for mobile-friendly impact. `72px`+ can work on desktop but risks breaking or cramping on mobile email clients. The headline should feel dominant without overflowing the viewport. Err on the side of `58px` as a sweet spot — still billboard-scale but won't choke a 375px screen
- **The dominant visual element** — the headline should take up more visual weight than everything else combined. It should feel like 60-70% of the component's visual impact lives in the headline alone
- **High contrast** — white on dark, or bold brand colour on light. Never muted, never subtle
- **Tight letter-spacing** — use negative letter-spacing (`-2px` to `-3px`) for that punchy, compressed, editorial feel
- **Short and blunt** — 2-4 words max per line. Punchier than a tagline. Think billboard, not paragraph
- **Isolated with massive breathing room** — minimum `36px` margin above and below the headline. The headline lives in its own visual zone, completely separated from supporting elements. There should be obvious empty space between the headline and anything else

### 2.2.1 Visual Hierarchy — The 3-Tier Size System

Every component has three distinct size tiers. The gaps between tiers must be **dramatic**, not gradual:

| Tier | Role | Size Range | Example |
|------|------|-----------|---------|
| **Tier 1 — The Headline** | The scroll-stopper. The purple cow. | `54px` – `62px` | "YOUR PERKS ARE ONLINE" |
| **Tier 2 — Data & Stats** | Supporting visual anchors (points, prices, numbers) | `22px` – `48px` | "2,450 points", "$24 saved" |
| **Tier 3 — Labels & Body** | Micro-copy, labels, descriptions, CTAs | `10px` – `16px` | "Points available", "Shop now" |

**The ratio matters.** Tier 1 should be **4-5x larger** than Tier 3. If your headline is `48px` and your labels are `12px`, that's only a 4x ratio — acceptable but not impactful. If your headline is `72px` and labels are `11px`, that's ~6.5x — now the hierarchy is unmissable.

**Never let Tier 2 elements compete with Tier 1.** If the points balance is `48px` and the headline is `54px`, they visually merge. The headline must always dwarf everything beneath it.

**Anti-patterns for headlines:**
- Anything under `54px` — that's a subheading, not a headline
- Same visual weight as surrounding elements — if the headline doesn't overpower everything else, resize it
- Less than `30px` margin separating the headline from supporting content — cramped layouts kill hierarchy
- Long sentences that wrap to 3+ lines — edit the copy, don't shrink the font
- Competing with nearby visual noise — if the headline gets lost next to stats/badges/cards, give it more space or make it bigger

### 2.3 Sell the Outcome — Think Like a Strategist, Not a Layout Engine

Before writing a single line of HTML, stop and ask: **"What is the goal of this component? What does the customer gain, and how do I make them feel it?"**

You are not arranging information into boxes. You are building a visual argument that makes someone act. Every component must answer one question for the customer: **"What's in it for me?"**

#### 2.3.1 Show the Transformation, Not the Feature

Never just list what something is. Show what it does for the customer. Make the value tangible and visual:

- **Show the before and after** — If the customer saves money, show what they would have paid versus what they actually pay. Use visual contrast: muted/crossed-out "without" values next to bold/highlighted "with" values. The contrast between the two is what sells — the customer's eye should immediately see the gap between the old reality and the new one.
- **Quantify the gain** — Don't say "save money." Show the exact dollar amount, percentage, or quantity they're getting. Abstract benefits don't convert. Concrete numbers do.
- **Make accumulation visible** — If value grows over time (points, savings, streak, tier progress), show the trajectory. Use progress bars, running totals, milestone markers, or "you've earned X so far" counters. People are motivated by seeing how far they've come and how close they are to the next reward.
- **Create a contrast moment** — Every component should have at least one moment where the customer sees the difference between being a member vs. not, buying now vs. later, or the regular price vs. their price. This contrast is the emotional hook.

#### 2.3.2 Visual Pop — Elements Must Lift Off the Page

Flat elements on flat backgrounds are invisible. Every card, stat, or feature block must have visual separation and depth:

- **Contrast against the background** — If the outer background is dark, inner cards should be noticeably lighter (or vice versa). A card that is one shade off the background is wallpaper, not a component. The difference should be immediately obvious.
- **Use borders with intention** — Borders aren't decoration. Use a visible accent-coloured left border or top border to draw the eye to a card. A `3-4px` solid brand-colour left border makes a card pop far more than a `1px` subtle border all around.
- **Shadow and elevation via colour** — Email clients don't support `box-shadow` reliably. Fake depth by using a slightly lighter background on cards, a strong left or top accent border, and generous inner padding. The card should feel like it's sitting on top of the background, not embedded in it.
- **Highlight the number, not the container** — The most important data point in each card should be the loudest visual element. Use brand colour for the number, white or high-contrast for the label. Don't let the card's border or background steal attention from the data inside it.
- **Colour-code value** — Use a specific accent colour (e.g., brand green, gold) exclusively for "value" elements: savings amounts, discounts, rewards, points. When customers see that colour, they should instantly associate it with "I'm getting something."

#### 2.3.3 Break the Pattern — Never Repeat the Same Card Three Times

When a component has multiple items (perks, products, features), **each card must feel visually distinct** even if they share a family resemblance. Repeating the exact same card layout, border, background, and structure three times in a row creates visual monotony — by the third card, the reader is skimming, not engaging.

Techniques to break repetition:

- **Vary the layout** — If one card is text-left/stat-right, make the next card full-width, or stack the stat above the text. Alternate between horizontal and vertical arrangements.
- **Vary the accent** — Rotate border positions (left border on one, top border on another, no border but a different background on a third). Use different accent colours for different value types.
- **Vary the density** — One card can be detailed with a price comparison, another can be a simple bold stat with a one-liner. Not every card needs the same amount of information.
- **Use a summary strip** — Instead of three identical cards, lead with a compact perks summary (a single row of icons or stats), then expand only the most compelling perk into a full card. Not everything needs equal visual weight.
- **Group, don't list** — If perks are related, consider grouping them visually (e.g., a single card with three columns) rather than stacking three separate cards. Lists feel like documentation. Grouped layouts feel like a dashboard.

#### 2.3.4 Copy Must Be Airtight

Every word in an email component gets scrutinised more than web copy because there's no navigation, no context, no second page. The reader has only what's in front of them.

- **Never contradict yourself** — If the copy says "no minimum spend" but there IS a minimum spend, the customer notices. Read every line and check: is this literally true? If a perk requires $95 spend, say "Spend $95+ and shipping's on us" — don't say "no minimum."
- **Match the CTA to the audience** — If the badge says "Member" but the CTA says "Start Earning Points", the reader feels confused. Are they already in or not? Determine the audience before writing the CTA:
  - **Existing members:** "Shop Member Perks", "Check My Rewards", "Use Your Points"
  - **Prospects / new signups:** "Join Now", "Start Earning", "Unlock Your Perks"
  - **Re-engagement:** "Your Points Are Waiting", "Come Back & Save"
- **One voice per component** — Don't switch between addressing the customer ("your perks") and describing the program ("members get"). Pick one and commit.

#### 2.3.5 Frame It as a Dashboard, Not a Brochure

The most effective loyalty/member components don't say "here are your benefits." They say "here is your value right now." The difference is personal vs. generic.

- **Lead with the member's status** — Before listing perks, anchor the component with who they are: "You're a Rewards Member" or "Gold Member Since 2023." This makes everything that follows feel personalised, even if it's the same for every member.
- **Show unlocked perks as a summary** — After the status anchor, show a compact line or row of what they currently have access to. Think of it like a dashboard header: "Your perks: $5 vouchers · 5% sports · free shipping over $95". This gives the reader the full picture instantly before any detail cards.
- **Then expand selectively** — Below the summary, only expand into detail cards for the perks that need a visual proof point (like a price comparison or progress bar). Not every perk needs its own card — some are better as a line item in the summary.
- **Make it feel like their account, not a flyer** — The component should feel like the customer opened their rewards account, not like they received a generic ad. Use "your", "you've earned", "your price" — not "members receive", "loyalty program offers".

#### 2.3.6 Tell a Story With Structure

The component's layout should guide the customer through a narrative arc, not dump information:

1. **Hook** — The headline grabs attention and states the promise (Tier 1)
2. **Proof** — Data, stats, or visual evidence that the promise is real (Tier 2). This is where you show savings, comparisons, progress, or rewards
3. **Payoff** — The CTA that lets them act on the promise. By the time they reach the button, they should already be convinced

Every element in the component either advances this story or it shouldn't be there. If a card or stat doesn't contribute to the "what's in it for me" narrative, remove it.

#### 2.3.7 Context-Aware Selling

Different types of components have different selling mechanics. Before designing, identify what category the component falls into and apply the right strategy:

- **Savings / Discount components** — The customer needs to see what they're NOT paying. Show the original alongside the reduced. Make the gap between the two feel like a win.
- **Loyalty / Rewards components** — The customer needs to see accumulation and progress. Show what they've earned, what's coming next, and what they'll unlock. The feeling is "I'm building towards something."
- **Product / Feature components** — The customer needs social proof and emotional resonance. Show ratings, reviews, bestseller badges, or "X people bought this." The feeling is "other people love this."
- **Urgency / Promotion components** — The customer needs scarcity. Show time limits, stock levels, or expiry. The feeling is "I'll miss out if I wait."
- **Welcome / Onboarding components** — The customer needs to see what they just gained access to. Show the full spread of benefits in a way that feels like unwrapping a gift.

Don't apply a one-size-fits-all template. Think about what emotional lever the component needs to pull, and design for that.

### 2.4 Component Composition Rules

Every email component must include **at minimum 3 of these layers**:

1. A **headline** that follows the Purple Cow Rule (massive, dominant, scroll-stopping)
2. A **visual element** (badge, stat, progress bar, icon, colour block)
3. A **data point** (number, percentage, points, tier)
4. A **CTA or action nudge** (button, link, "tap to activate")
5. A **supporting line** that adds urgency or exclusivity

### 2.5 Think Like a Luxury Brand Email

Study how brands like Apple, Nike, Aesop, and high-end retailers compose their emails:

- Generous white space around key elements
- Oversized numbers for impact
- Minimal but intentional colour use
- Every pixel earns its place

### 2.6 Colour Contrast — The Purple Cow Is a Different Colour

The Purple Cow theory doesn't just apply to size — it applies to colour. A purple cow stands out because it's a **different colour** than every other cow in the field. If your entire component uses one colour family, nothing stands out. Everything blends into soup.

#### 2.6.1 The Two-Colour Rule

Every component must use **at least two distinct colour families** that create tension:

- **Structural colour** — The brand's primary colour. Used for backgrounds, borders, labels, body text tints. This is the "field" — the normal cows.
- **Pop colour** — A contrasting colour pulled from the brand palette (secondary, accent, or complementary). Used **sparingly** and **only on the elements that need to stop the eye**: the headline, the savings number, the key stat, the CTA. This is the purple cow.

The pop colour should appear on no more than 2-3 elements in the entire component. If everything is the pop colour, nothing pops.

#### 2.6.2 Where Pop Colour Goes

Apply the pop colour to the moments of highest value or surprise:

- The **savings amount** or **"your price"** number — the thing the customer gains
- The **headline** or a key word within the headline
- The **CTA button** — the action you want them to take
- A **badge or ribbon** that signals exclusivity

#### 2.6.3 Where Pop Colour Does NOT Go

- Backgrounds of cards (that's structural)
- Body copy (that's informational)
- Labels and micro-copy (that's supporting)
- Borders and dividers (that's structural)
- Multiple elements in the same card (dilutes the pop)

#### 2.6.4 Monochrome Is an Anti-Pattern

If you step back and squint at the component and it reads as "one colour", it has failed. Test this: if you described the component's colours to someone, would you say more than one colour name? "Green and gold" passes. "Dark green, medium green, light green, green accent" fails — that's one colour at different brightnesses.

**Common monochrome traps:**
- Using the brand's primary colour for backgrounds, borders, accents, stats, and buttons (everything is green)
- Using white only for text and the brand colour for everything else (two-tone, not two-colour)
- Tinting every element with the same hue at different opacities

**How to fix it:** Look at the brand's logo. Most logos contain at least two colour families. If the logo has green and gold, use green structurally and gold for pop. If the logo has blue and orange, use blue structurally and orange for pop. The logo already solved this problem — extract both colours, don't just use one.

### 2.7 Image-to-Component Flow — No Hard Breaks

When a component sits directly below an image, the transition between the two must feel seamless. A jarring colour change between the bottom of an image and the top of the next component breaks the visual flow and makes the email feel like a stack of disconnected blocks instead of one continuous design.

#### 2.7.1 When This Rule Applies

Only apply this when you are confident the component comes directly after an image:

- The user explicitly says the component sits below an image
- You are building the email top-down and you just placed or discussed an image above this component
- The user provides an image and asks for a component to go underneath it

Do NOT assume an image is above the component if the user hasn't mentioned one. This rule is contextual, not universal.

#### 2.7.2 Pre-Design Flow — Component Below an Image

When you know the component sits below an image, execute this flow **before doing anything else**. No design suggestions, no layout options, no HTML, no "while we wait" ideas. Your first response to the user must be the output of this flow and nothing else.

```
START

READ .env file in project root

IF .env contains a Klaviyo API key:
    RESPOND to user with ONLY:
        "I found a Klaviyo API key. I can pull your template to
         automatically detect the image-to-component colour transition
         so the design blends seamlessly. Which template is this
         component for?"
    STOP. Wait for user response. Do not suggest designs.

    WHEN user provides template name/ID:
        CALL Klaviyo API: GET /api/templates/{id}
        PARSE HTML for all background-color values in top-to-bottom order
        FIND the image section
        EXTRACT background-color of the section directly after the image
        SET component_bg = that colour
        See references/image-generation-blending.md for full process

ELSE IF .env does not exist OR no API key found:
    RESPOND to user with ONLY:
        "What is the bottom/dominant colour of your image? I'll match
         the component's background to that colour so it flows
         seamlessly into the next section."
    STOP. Wait for user response. Do not suggest designs.

    WHEN user provides colour:
        SET component_bg = user's colour

END IF

— You now have component_bg. You may begin designing. —

BEFORE presenting design options, ALSO ask:
    "I can generate a prompt suffix for your image generation model
     that makes the image fade into {component_bg} at the bottom edge —
     so the blend is baked into the image itself. Want me to generate that?"

IF user says yes:
    READ references/image-generation-blending.md
    OUTPUT the prompt suffix with {component_bg} as the target colour

NOW proceed to design the component using component_bg as the background.
```

**The rule is simple: no component_bg, no design work.** Everything before the dotted line must complete before anything after it begins. Do not fill the wait time with suggestions, options, or "in the meantime" ideas. The user's answer determines the background colour, which determines the entire visual direction. Designing without it is a wasted iteration.

#### 2.7.3 Design Guidance for the User

When asking about the image colour, also nudge the user toward best practice:

- Suggest they use an image that fades or blends to a solid colour at the bottom edge — this makes the transition effortless
- If their image has a busy or multi-coloured bottom edge, suggest adding a subtle gradient overlay at the base of the image that fades into a solid colour
- If the image has a clean solid background (e.g., a product shot on white or a lifestyle shot with a dark background), matching is straightforward — just pick up that colour

#### 2.7.4 What This Looks Like in Practice

**Bad:** A lifestyle image with a dark navy bottom edge, followed by a component with a bright white background. The hard horizontal line screams "these are two separate blocks."

**Good:** The same image, but the component below uses a dark navy background that matches the image's bottom edge. The text and content appear to float over a continuous background. The reader doesn't notice a transition — they just keep scrolling.

### 2.8 Anti-Patterns — Never Do These

- Plain text on a solid background with nothing else
- A heading + subheading + divider and nothing more
- Generic layouts that could belong to any brand
- Walls of body text without visual anchors
- Components that don't make the customer feel something
- **Monochrome soup** — an entire component built from one colour family at different shades

---

## 3. Contextual Reference Files

When building components that relate to specific business features, consult the relevant reference file for accurate details. Never invent placeholder data when real business data exists.

| Component Type | Reference File |
|---|---|
| Loyalty, rewards, points, tiers, member perks | `references/rewards-program.md` |
| Image generation for email (blending into components) | `references/image-generation-blending.md` |
| Klaviyo native blocks (non-HTML built-in components) | `references/klaviyo-blocks.md` |
| Klaviyo template best practices | `references/template-best-practices.md` |

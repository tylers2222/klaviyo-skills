# Klaviyo Built-In Blocks & Layout

These are the native drag-and-drop components available in Klaviyo's email template editor. They require no custom HTML — they are pre-built, styled through the editor's style panel, and work reliably across all email clients.

When planning an email from top to bottom, **not every section needs to be a custom HTML component.** These blocks are tools in the kit. Use them to add structure, breathing room, and variety between custom-designed sections. An email that alternates between custom HTML components and native blocks feels more natural and less heavy than wall-to-wall custom code.

---

## Blocks

### Content Blocks

| Block | What It Does | When to Use It |
|---|---|---|
| **Text** | Rich text block with full formatting (bold, italic, links, colour, alignment). Supports personalisation tags. | Body copy, disclaimers, short announcements, personalised greetings. Use between heavier visual components to give the reader a break. |
| **Image** | Single image block. Supports alt text, linking, and sizing. | Hero images, product shots, lifestyle photos, brand imagery. The workhorse of email visuals. |
| **Split** | Two-column side-by-side layout within a single block. Each side can hold text or images independently. | Product + description pairs, image + CTA combos, before/after comparisons. Good for breaking single-column monotony. |
| **Button** | Standalone CTA button. Fully styleable — colour, border radius, padding, font, width. | Primary and secondary CTAs. Use Klaviyo's native button over image-based buttons for accessibility, A/B testing, and dark mode compatibility. |
| **Header Bar** | Pre-built top navigation bar. Can include links, menu items, and styling. | Top of email — brand navigation, category links (Shop, Sale, New Arrivals). Sets the frame before the hero. |
| **Drop Shadow** | Adds a shadow effect between sections. Creates visual separation and depth. | Place between two sections that share similar background colours to create the illusion of layered panels. Adds depth without custom CSS hacks. |
| **Divider** | Horizontal line separator. Styleable — colour, thickness, width, padding. | Breaking up text-heavy sections, separating content groups. Cleaner than whitespace alone when you need a visible boundary. |
| **Social Links** | Pre-built social media icon row (Facebook, Instagram, Twitter, YouTube, etc.). | Footer or sign-off section. Use Klaviyo's native block instead of manual image links — it auto-formats and stays consistent. |
| **Spacer** | Empty vertical space block. Height is adjustable. | Creating breathing room between components. More reliable than margin/padding hacks in custom HTML. Use generously — whitespace sells. |

### Dynamic / Data Blocks

| Block | What It Does | When to Use It |
|---|---|---|
| **Product** | Pulls product data dynamically — image, title, price, description, link. Can show items from a catalogue or based on customer behaviour. | Product recommendation sections, "you might also like" rows, cart reminders. Pulls live data so it's always current. |
| **Coupon** | Generates and displays a unique or static coupon code. Integrates with Klaviyo's coupon system. | Discount offers, welcome series incentives, win-back campaigns. The code is live and trackable — no manual code management. |
| **Table** | Structured data table. Rows and columns with styling. | Order summaries, comparison charts, pricing tables, feature lists. Use when data needs to be scannable in a grid format. |
| **Review Quote** | Displays a customer review or testimonial. Styleable quote block. | Social proof sections. Drop one between a product showcase and a CTA to add credibility. More effective than writing "customers love us" in body copy. |
| **Video** | Embeds a video thumbnail with a play button that links to the hosted video. | Product demos, brand stories, tutorials. Email clients don't play inline video — this creates a clickable thumbnail that drives to the video. |

### Code Block

| Block | What It Does | When to Use It |
|---|---|---|
| **HTML** | Raw HTML block. Accepts any valid email HTML. | Custom-designed components (loyalty dashboards, complex layouts, branded sections). This is where the components built from `references/component-patterns.md` guidelines get pasted. |

---

## Layout

| Block | What It Does | When to Use It |
|---|---|---|
| **Columns** | Splits a section into multiple columns (2, 3, or 4). Each column is an independent container for blocks. | Multi-product rows, feature grids, side-by-side comparisons. Use for horizontal layouts that need more than two columns (Split only does two). |
| **Section** | A container that groups blocks together. Controls background colour, padding, borders, and display conditions (show/hide by device or segment). | Every logical group of content should be its own section. Sections are the structural backbone — use them to define colour zones, control spacing, and set conditional visibility. |

---

## How to Use These in Email Planning

When planning an email flow from top to bottom, think of the email as a sequence of **sections**, where each section is either:

1. **A native block** — simple, reliable, no code required
2. **A custom HTML component** — designed for high-impact moments (loyalty dashboards, price comparisons, branded hero content)

Not every section needs custom HTML. A well-planned email might look like:

```
Section 1:  Header Bar (native) — logo + nav links
Section 2:  Image (native) — hero image
Section 3:  HTML (custom) — loyalty dashboard component
Section 4:  Spacer (native) — breathing room
Section 5:  Product (native) — dynamic product recommendations
Section 6:  Drop Shadow (native) — visual separator
Section 7:  Review Quote (native) — social proof
Section 8:  Button (native) — secondary CTA
Section 9:  Divider (native) — separator before footer
Section 10: Social Links (native) — social icons
Section 11: Text (native) — footer / unsubscribe / legal
```

Custom HTML is the heavy artillery. Native blocks are the connective tissue. Use both.

### When to Use Native Over Custom

- **Spacers over margin hacks** — Spacer blocks render consistently across clients. Custom HTML margin/padding can collapse in Outlook.
- **Buttons over HTML buttons** — Native buttons are A/B testable, dark-mode compatible, and accessible out of the box.
- **Product blocks over hardcoded product cards** — Product blocks pull live catalogue data. Hardcoded cards go stale.
- **Drop shadows over border tricks** — The drop shadow block creates clean depth between sections without CSS workarounds.
- **Review quotes over styled text** — The review block has built-in quote formatting. Styling a text block to look like a review is unnecessary work.
- **Social links over image grids** — Native social blocks auto-format, update globally, and include proper link tracking.

### When Custom HTML is Worth It

- **Branded visual components** — Loyalty dashboards, member status panels, points progress bars. Anything that needs to feel like a branded experience, not a template.
- **Price comparison layouts** — Before/after pricing, member vs. non-member prices, crossed-out values. Native blocks can't do this.
- **Complex multi-element cards** — Cards that combine stats, badges, progress bars, and CTAs in a single visual unit.
- **Anything that follows the design guidelines in `references/component-patterns.md`** — If it needs the Purple Cow Rule, the 3-Tier hierarchy, or visual pop, it's custom HTML territory.

---
name: Email Component Designer
description: This skill should be used when the user asks to "build an email component", "design an email section", "create a Klaviyo template", "make a loyalty component", "design a hero section", "plan an email layout", "build a product card for email", or mentions designing, building, or planning email marketing components for Klaviyo. Also triggers when the user references email design, email HTML, Klaviyo blocks, or email template structure.
version: 0.1.0
---

# Email Component Designer

Design and build conversion-driven email marketing components for Klaviyo. This skill produces premium, sales-focused HTML components and full email layout plans that follow brand guidelines, visual hierarchy principles, and Klaviyo best practices.

## Core Workflow

When triggered, follow this sequence:

### 1. Load Brand Context

Check the project root for a `logo/` folder. Read the logo assets to extract the brand colour palette. Define:

```
Primary Colour (structural):
Secondary Colour:
Pop/Accent Colour:
Dark Background:
Light Background:
Text Colour:
CTA Colour:
```

The logo contains the answer. Extract at least two distinct colour families — one structural, one for pop. Refer to `references/component-patterns.md` section 2.6 for the Two-Colour Rule.

### 2. Check for Klaviyo API Access

```
READ .env file in project root

IF .env contains a Klaviyo API key:
    Store key for template operations
    Klaviyo API is available for:
        - Pulling existing templates (GET /api/templates/{id})
        - Listing all templates (GET /api/templates)
        - Extracting background colours from template HTML
        - Image-to-component colour matching

ELSE:
    No API access — rely on user-provided information
```

### 3. Determine Component Context

```
IF user mentions component sits below an image:
    EXECUTE image-flow gate (see section below)
    DO NOT propose designs until gate completes

ELSE IF user asks to plan a full email:
    READ references/klaviyo-blocks.md for native block options
    Plan the email as a mix of native blocks and custom HTML components

ELSE:
    Proceed to design using brand palette and design guidelines
```

### 4. Design the Component

Consult `references/component-patterns.md` for all design rules. Key principles:

- **Purple Cow Rule** — Headlines at `54px`–`62px`, dominant, high-contrast, isolated with breathing room
- **3-Tier Size System** — Tier 1 (headline `54-62px`), Tier 2 (data `22-48px`), Tier 3 (labels `10-16px`)
- **Two-Colour Rule** — Structural colour for backgrounds/borders, pop colour for value moments only
- **Sell the Outcome** — Show transformations (before/after pricing), quantify gains, make accumulation visible
- **Break the Pattern** — Never repeat the same card layout three times
- **Dashboard Not Brochure** — For loyalty/member components, frame as "your value right now" not "here are benefits"
- **Context-Aware Selling** — Different component types need different emotional levers (savings, loyalty, urgency, social proof)

### 5. Output

Write final HTML to `latest_html_write.html` in the project root.

---

## Image-to-Component Flow Gate

When the component sits below an image, execute this before any design work:

```
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

ELSE IF .env does not exist OR no API key found:
    RESPOND to user with ONLY:
        "What is the bottom/dominant colour of your image? I'll match
         the component's background to that colour so it flows
         seamlessly into the next section."
    STOP. Wait for user response. Do not suggest designs.

    WHEN user provides colour:
        SET component_bg = user's colour

END IF

— component_bg is now set. May begin designing. —

BEFORE presenting design options, ALSO ask:
    "I can generate a prompt suffix for your image generation model
     that makes the image fade into {component_bg} at the bottom edge —
     so the blend is baked into the image itself. Want me to generate that?"

IF user says yes:
    READ references/image-generation-blending.md
    OUTPUT the prompt suffix with {component_bg} as the target colour

NOW proceed to design the component using component_bg as the background.
```

No component_bg, no design work.

---

## Contextual References

When building components that relate to specific features, consult the relevant reference file. Never invent placeholder data when real business data exists.

| Component Type | Reference File |
|---|---|
| All email components — design rules, visual hierarchy, selling strategy | `references/component-patterns.md` |
| Klaviyo native blocks — planning full email layouts | `references/klaviyo-blocks.md` |
| Klaviyo template best practices — branding, mobile, accessibility | `references/template-best-practices.md` |
| Image generation blending — prompt suffix for seamless transitions | `references/image-generation-blending.md` |
| Business-specific loyalty/rewards program data | `references/rewards-program.md` |

### Scripts

- **`scripts/extract_logo_palette.py`** — Extract dominant colours from logo PNG files. Run against the `logo/` folder to generate a brand colour palette programmatically.

### Assets

- **`assets/`** — Store example layouts, component screenshots, or reference images for design direction.

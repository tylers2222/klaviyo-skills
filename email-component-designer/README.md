# Email Component Designer — Claude Code Skill

A Claude Code skill that designs and builds conversion-driven email marketing components for Klaviyo. It produces premium, sales-focused HTML components and full email layout plans using your brand's actual assets, colour palette, and business data.

## What It Does

- Extracts your brand colour palette from logo files automatically
- Designs email components following visual hierarchy, selling psychology, and email best practices
- Plans full email layouts mixing custom HTML components with Klaviyo's native drag-and-drop blocks
- Connects to the Klaviyo API to pull existing templates and detect image-to-component colour transitions
- Generates image generation prompt suffixes that make hero images blend seamlessly into the component below

## Setup

### 1. Install the Skill

Copy the `email-component-designer/` folder into your project's `.claude/skills/` directory:

```
your-project/
├── .claude/
│   └── skills/
│       └── email-component-designer/
│           ├── SKILL.md
│           ├── references/
│           ├── scripts/
│           └── assets/
```

### 2. Add Your Logo

Create a `logo/` folder in your project root and add your brand's logo as PNG files. The skill reads these to extract your colour palette.

```
your-project/
├── logo/
│   ├── logo-dark.png
│   └── logo-light.png
```

You can also run the palette extraction script manually:

```bash
python3 .claude/skills/email-component-designer/scripts/extract_logo_palette.py ./logo/
```

Requires Pillow (`pip3 install Pillow`).

### 3. Set Up Klaviyo API Access (Optional)

Create a `.env` file in your project root with your Klaviyo private API key:

```
klaviyo_api_key=pk_your_private_api_key_here
```

This enables the skill to:
- Pull existing templates from your Klaviyo account
- Automatically detect background colours for image-to-component blending
- List all templates so you can reference them by name

The API key needs the `templates:read` scope at minimum. You can generate one in Klaviyo under **Settings > API Keys**.

If no `.env` or API key is found, the skill will fall back to asking you for colours manually. Everything still works — the API just automates the colour detection.

### 4. Add Your Business Data (Optional)

Replace `references/rewards-program.md` with your own business-specific data. This file is consulted when building loyalty, rewards, or membership components so the skill uses real program details instead of placeholders.

The file ships with example content. Replace it with your actual rewards structure:

```markdown
# Rewards Rules

1. For every 200 points accumulated, get a $5 gift voucher
2. 5% Off all sports products in-store at all times
3. Free shipping on all orders over $95
```

## How to Use

Once installed, Claude Code will automatically trigger this skill when you ask to build email components. Examples:

- "Build a loyalty rewards component for our email"
- "Design a hero section for a sale email"
- "Plan the full layout for a welcome email"
- "Create a product showcase component"
- "I need a component below the hero image for our rewards program"

### Image-to-Component Blending

When you mention that a component sits below an image, the skill will:

1. Check for a Klaviyo API key
2. If found, ask which template to pull, then extract the exact transition colour automatically
3. If not found, ask you for the image's bottom colour
4. Offer to generate a prompt suffix for your image generation model that fades the image into the component's background colour

### Full Email Planning

When planning a full email, the skill references Klaviyo's native blocks (spacers, dividers, product blocks, review quotes, etc.) alongside custom HTML components. Not every section needs custom HTML — the skill plans a mix.

## File Structure

```
email-component-designer/
├── SKILL.md                              # Core skill — workflow and design process
├── README.md                             # This file
├── references/
│   ├── component-patterns.md             # Design rules (Purple Cow, 3-Tier hierarchy,
│   │                                     #   selling strategy, colour contrast, image flow)
│   ├── image-generation-blending.md      # Prompt suffix for seamless image transitions
│   ├── klaviyo-blocks.md                 # Klaviyo's native drag-and-drop blocks
│   ├── rewards-program.md               # Business loyalty/rewards data (replace with yours)
│   └── template-best-practices.md       # Klaviyo template best practices
├── scripts/
│   └── extract_logo_palette.py          # Extract brand colours from logo PNGs
└── assets/                              # Store example layouts or reference images
```

## Design Principles

The skill enforces these design rules (documented in detail in `references/component-patterns.md`):

- **Purple Cow Rule** — Headlines must stop the scroll. `54-62px`, high contrast, isolated with breathing room.
- **3-Tier Size System** — Dramatic size gaps between headline, data, and labels. No visual competition.
- **Two-Colour Rule** — Every component uses a structural colour and a pop colour. Monochrome is an anti-pattern.
- **Sell the Outcome** — Show transformations (before/after pricing), not features. Quantify gains with real numbers.
- **Break the Pattern** — Never repeat the same card layout three times. Vary layout, accent, and density.
- **Dashboard Not Brochure** — Loyalty components frame as "your value right now", not "here are benefits".
- **Image Flow** — Components below images must match the image's bottom edge colour. No hard breaks.

## Output

All final HTML is written to `latest_html_write.html` in the project root. Copy this into Klaviyo's HTML block in the drag-and-drop editor.

## Requirements

- Claude Code
- Python 3 + Pillow (for palette extraction script only)
- Klaviyo account + API key (optional, for template pulling)

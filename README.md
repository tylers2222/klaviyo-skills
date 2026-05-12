# Klaviyo Skills for Claude Code

A collection of open-source [Claude Code](https://claude.com/claude-code) skills for designing and building email marketing campaigns in Klaviyo.

Built by [@tylers2222](https://github.com/tylers2222) — a programmer who got tired of vanilla email templates and decided to teach Claude how to build components that actually sell.

## What Are Skills?

Skills are modular packages that extend Claude Code with specialised knowledge and workflows. Drop a skill into your project's `.claude/skills/` directory and Claude automatically picks it up — no config, no setup beyond what the skill's README describes.

Think of them as onboarding guides that turn Claude from a general-purpose assistant into a domain expert.

## Available Skills

| Skill | Description |
|---|---|
| [**email-component-designer**](./email-component-designer/) | Design and build conversion-driven email components for Klaviyo. Enforces visual hierarchy (Purple Cow Rule), selling psychology (show the transformation, not the feature), brand colour extraction from logos, Klaviyo API integration for template colour matching, and image-to-component blending prompts. |

## Installation

Copy the skill folder into your project:

```
your-project/
├── .claude/
│   └── skills/
│       └── email-component-designer/
│           ├── SKILL.md
│           ├── references/
│           ├── scripts/
│           └── assets/
├── logo/
│   └── your-logo.png
└── .env
```

See each skill's own README for specific setup instructions (API keys, brand assets, etc.)

## Contributing

These skills were built iteratively — designing components, noticing what Claude got wrong, and updating the instructions until it stopped making those mistakes. Contributions that follow the same pattern are welcome.

### Adding a New Skill

1. Create a folder under the repo root: `your-skill-name/`
2. Add a `SKILL.md` with YAML frontmatter (`name`, `description`) and the skill body
3. Add `references/` for detailed docs, `scripts/` for utilities, `assets/` for templates
4. Add a `README.md` explaining setup and usage
5. Keep `SKILL.md` lean (~1,500-2,000 words) — push detailed content into `references/`
6. Open a PR

### Improving an Existing Skill

The best improvements come from using the skill and noticing where it falls short:

- Claude skipped a step? Strengthen the gating language.
- Output looked wrong? Add the fix to the design rules.
- Missing a Klaviyo feature? Add it to the blocks reference.

Open an issue describing what went wrong and what you expected, or submit a PR with the fix.

### Skill Structure Convention

```
skill-name/
├── SKILL.md              # Required — core workflow (triggers, steps, references)
├── README.md             # Required — setup guide for users
├── references/           # Detailed docs loaded by Claude as needed
├── scripts/              # Utility scripts (palette extraction, validation, etc.)
└── assets/               # Templates, examples, images used in output
```

## Design Philosophy

These skills are opinionated. They were built around a few core beliefs about email marketing:

- **Plain text on a background is not a component.** Every section must have visual depth, data points, and a selling mechanism.
- **Headlines are billboards, not labels.** If it doesn't stop the scroll, it's too small.
- **Show the transformation, not the feature.** Crossed-out prices, before/after comparisons, progress bars — make the customer feel the value.
- **Two colours minimum.** Monochrome is an anti-pattern. Extract both colour families from the logo.
- **Automate before asking.** If the Klaviyo API can answer the question, don't ask the user.

## License

MIT

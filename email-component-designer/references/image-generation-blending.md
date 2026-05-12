# Image Generation — Component Blending Suffix

This file contains a prompt suffix to append to any image generation prompt when the image will sit directly above an email component. The suffix instructs the image generation model to fade the bottom edge of the image into a specific colour, creating a seamless flow between the image and the component below it.

---

## When to Use This

Append this suffix to your image generation prompt when:

- The image will sit directly above an email component
- You know the background colour of the component that follows the image
- The goal is a seamless, flowing email where the image bleeds into the next section

Do NOT use this when:

- The image sits between two other images
- The image is a standalone asset not used in an email layout
- You don't yet know what component follows the image

---

## How to Get the Target Colour — Automated via Klaviyo API

**Do not ask the user for the colour if you can determine it automatically.** The Klaviyo API has the answer. Follow this process in order:

### Step 1: Pull the template from Klaviyo

Ask the user which template the image is for (or use the template already being discussed in the session). Then call:

```
GET https://a.klaviyo.com/api/templates/{id}
Authorization: Klaviyo-API-Key {key from .env file}
revision: 2024-10-15
```

The API key is stored in the `.env` file at the project root.

### Step 2: Parse the template HTML for component order

Extract every `background-color` declaration from the HTML in top-to-bottom order. Map each one to its position in the document and identify whether it contains an `<img>` tag. This gives you the full component stack:

```
Section 1: BG #FFFFFF  [has image]
Section 2: BG #e8a832  [no image — text component]
Section 3: BG #0F1F0F  [has image]
Section 4: BG #001802  [no image — text component]
```

### Step 3: Find the image's position and read the next component's background colour

Locate the section that contains the image being generated (or the image slot the user is filling). The **next section's `background-color`** is your target blend colour. Extract it automatically.

### Step 4: If the next component has an image hosted on Klaviyo's CDN, download it and sample the top edge

If the component below is also an image, download it via its CDN URL and sample the top 5 rows of pixels to get the dominant colour. Use Python with Pillow:

```python
from PIL import Image
from collections import Counter

img = Image.open('/tmp/next_component_image.png')
w, h = img.size
top_colors = []
for y in range(0, 5):
    for x in range(0, w, max(1, w//30)):
        px = img.getpixel((x, y))
        top_colors.append(px[:3])
dominant = Counter(top_colors).most_common(1)[0][0]
hex_colour = '#{:02x}{:02x}{:02x}'.format(*dominant)
```

### Step 5: Only ask the user as a last resort

If the API key is not available, the template doesn't exist yet, or you genuinely cannot determine the next component's colour, then ask:

> "What background colour is the component below this image? I need to blend the image's bottom edge into it."

But this should be the exception, not the default. **Automate first, ask second.**

---

## The Prompt Suffix

Append the following to the end of any image generation prompt, replacing `{COLOUR}` with the target hex colour and `{COLOUR_NAME}` with a human-readable description of that colour:

```
IMPORTANT — Bottom edge blending requirement:
The bottom 15-20% of this image must gradually fade into a solid {COLOUR_NAME} colour ({COLOUR}). This fade should be a smooth, natural gradient — not a hard line or an obvious overlay. The content of the image (subjects, text, objects) should sit in the upper 75-80% of the frame, leaving the bottom portion clear for the colour fade. The very bottom edge of the image must be a clean, solid {COLOUR} so it can sit flush against a {COLOUR} background with zero visible seam. Think of it as the image dissolving into the background below it.
```

---

## Examples

### Dark green component below (`#0F1F0F`)
```
Create a lifestyle photo of premium sports nutrition products arranged on a dark surface with dramatic lighting and green accent tones.

IMPORTANT — Bottom edge blending requirement:
The bottom 15-20% of this image must gradually fade into a solid very dark green colour (#0F1F0F). This fade should be a smooth, natural gradient — not a hard line or an obvious overlay. The content of the image (subjects, text, objects) should sit in the upper 75-80% of the frame, leaving the bottom portion clear for the colour fade. The very bottom edge of the image must be a clean, solid #0F1F0F so it can sit flush against a #0F1F0F background with zero visible seam. Think of it as the image dissolving into the background below it.
```

### White component below (`#FFFFFF`)
```
Create a clean product flat-lay of supplement bottles on a bright, airy background.

IMPORTANT — Bottom edge blending requirement:
The bottom 15-20% of this image must gradually fade into a solid white colour (#FFFFFF). This fade should be a smooth, natural gradient — not a hard line or an obvious overlay. The content of the image (subjects, text, objects) should sit in the upper 75-80% of the frame, leaving the bottom portion clear for the colour fade. The very bottom edge of the image must be a clean, solid #FFFFFF so it can sit flush against a #FFFFFF background with zero visible seam. Think of it as the image dissolving into the background below it.
```

### Gold/amber component below (`#e8a832`)
```
Create a bold promotional banner image with fitness imagery and warm golden lighting.

IMPORTANT — Bottom edge blending requirement:
The bottom 15-20% of this image must gradually fade into a solid warm gold colour (#e8a832). This fade should be a smooth, natural gradient — not a hard line or an obvious overlay. The content of the image (subjects, text, objects) should sit in the upper 75-80% of the frame, leaving the bottom portion clear for the colour fade. The very bottom edge of the image must be a clean, solid #e8a832 so it can sit flush against a #e8a832 background with zero visible seam. Think of it as the image dissolving into the background below it.
```

---

## Template Reference

After pulling a template via the Klaviyo API, map the image-to-component transitions in a table:

| Image | Bottom Edge Colour | Next Component BG | Blend Status |
|---|---|---|---|
| Hero image | (sampled from bottom edge) | (parsed from next section) | Match / Hard break |
| Secondary image | (sampled) | (parsed) | Match / Hard break |

Use the target blend colour from the "Next Component BG" column when generating the image prompt suffix.

#!/usr/bin/env python3
"""
Extract dominant colours from logo PNG files to build a brand colour palette.

Usage:
    python3 extract_logo_palette.py <path_to_logo_folder>

Example:
    python3 extract_logo_palette.py ./logo/

Outputs a colour palette with hex values extracted from all PNG files in the folder.
Requires Pillow: pip3 install Pillow
"""

import sys
import os
from collections import Counter

try:
    from PIL import Image
except ImportError:
    print("Pillow is required. Install with: pip3 install Pillow")
    sys.exit(1)


def extract_colours(image_path, num_colours=10, min_saturation=30):
    """Extract dominant non-white, non-black colours from an image."""
    img = Image.open(image_path).convert("RGB")
    w, h = img.size

    # Sample pixels (every 4th pixel for performance on large images)
    pixels = []
    step = max(1, min(w, h) // 200)
    for y in range(0, h, step):
        for x in range(0, w, step):
            pixels.append(img.getpixel((x, y)))

    # Filter out near-white, near-black, and very desaturated colours
    filtered = []
    for r, g, b in pixels:
        # Skip near-white
        if r > 240 and g > 240 and b > 240:
            continue
        # Skip near-black
        if r < 15 and g < 15 and b < 15:
            continue
        # Skip very grey (low saturation)
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        if max_c - min_c < min_saturation and max_c > 50:
            continue
        # Quantize to reduce noise (round to nearest 8)
        qr = (r // 8) * 8
        qg = (g // 8) * 8
        qb = (b // 8) * 8
        filtered.append((qr, qg, qb))

    return Counter(filtered).most_common(num_colours)


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def get_colour_name(r, g, b):
    """Rough colour name based on dominant channel."""
    max_c = max(r, g, b)
    if max_c == 0:
        return "black"

    # Check for gold/amber
    if r > 180 and g > 130 and b < 100:
        return "gold/amber"
    # Check for brown
    if r > 100 and g > 50 and g < r and b < g:
        return "brown"

    if r > g and r > b:
        if g > b + 30:
            return "orange/yellow"
        return "red"
    elif g > r and g > b:
        if r > b + 30:
            return "yellow-green"
        return "green"
    elif b > r and b > g:
        if r > g + 30:
            return "purple"
        return "blue"
    else:
        return "neutral"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_logo_palette.py <path_to_logo_folder>")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"Error: {folder} is not a directory")
        sys.exit(1)

    # Find all PNG files
    png_files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(".png")
    ]

    if not png_files:
        print(f"No PNG files found in {folder}")
        sys.exit(1)

    print(f"Scanning {len(png_files)} PNG file(s) in {folder}\n")

    # Aggregate colours across all files
    all_colours = Counter()
    for png in png_files:
        print(f"  Reading: {os.path.basename(png)}")
        colours = extract_colours(png)
        for colour, count in colours:
            all_colours[colour] += count

    # Get top colours
    top = all_colours.most_common(8)

    print("\n" + "=" * 50)
    print("EXTRACTED BRAND PALETTE")
    print("=" * 50)

    colour_families = {}
    for i, (rgb, count) in enumerate(top):
        hex_val = rgb_to_hex(rgb)
        name = get_colour_name(*rgb)
        print(f"  {i+1}. {hex_val}  RGB({rgb[0]}, {rgb[1]}, {rgb[2]})  [{name}]  ({count} samples)")

        if name not in colour_families:
            colour_families[name] = hex_val

    print("\n" + "-" * 50)
    print("SUGGESTED PALETTE ASSIGNMENTS")
    print("-" * 50)

    families = list(colour_families.items())
    if len(families) >= 1:
        print(f"  Primary (structural):  {families[0][1]}  [{families[0][0]}]")
    if len(families) >= 2:
        print(f"  Pop/Accent:            {families[1][1]}  [{families[1][0]}]")
    if len(families) >= 3:
        print(f"  Secondary:             {families[2][1]}  [{families[2][0]}]")

    # Suggest dark/light backgrounds
    darkest = min(top, key=lambda x: sum(x[0]))
    lightest = max(top, key=lambda x: sum(x[0]))
    print(f"  Dark Background:       {rgb_to_hex(darkest[0])}")
    print(f"  Light Background:      #ffffff or {rgb_to_hex(lightest[0])}")
    print(f"  Text:                  #ffffff (on dark) / #1a1a1a (on light)")
    if len(families) >= 1:
        print(f"  CTA:                   {families[0][1]}  [primary]")

    print()


if __name__ == "__main__":
    main()

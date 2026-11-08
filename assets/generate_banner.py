#!/usr/bin/env python3
"""Generate assets/banner.png (1280x640) — the org social-preview card.

Same brand language as the platform OG card (scripts/og-image.py in the
nuniversity.github.io repo): blue→purple vertical gradient, white rounded
"NU" badge, DejaVu typography.

Run with any Python that has Pillow (the platform repo keeps one in .venv):
    /path/to/nuniversity.github.io/.venv/bin/python assets/generate_banner.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
OUT = Path(__file__).resolve().parent / "banner.png"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

TOP = (59, 130, 246)       # site blue
BOTTOM = (147, 51, 234)    # site purple

CHIP_ROW_1 = ["49 courses", "1,300+ lessons", "1,658 exam questions"]
CHIP_ROW_2 = ["10 interactive tools", "7 educational games", "0 ads · 0 tracking"]


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


def draw_chip(draw, chip, text_x, y, font) -> None:
    w = draw.textlength(chip, font=font)
    draw.rounded_rectangle(
        (text_x, y, text_x + w + 40, y + 54), radius=27,
        fill=(255, 255, 255, 36), outline=(255, 255, 255, 70), width=2,
    )
    draw.text((text_x + 20, y + 11), chip, font=font, fill=(255, 255, 255))
    return text_x + w + 40 + 20  # next x


def main() -> None:
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        px_row = tuple(int(TOP[i] + (BOTTOM[i] - TOP[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = px_row

    draw = ImageDraw.Draw(img, "RGBA")

    # Brand badge
    badge_font = load_font("DejaVuSans-Bold.ttf", 60)
    draw.rounded_rectangle((72, 66, 232, 166), radius=26, fill=(255, 255, 255))
    tw = draw.textlength("NU", font=badge_font)
    draw.text((152 - tw / 2, 78), "NU", font=badge_font, fill=TOP)

    # Identities, top-right (keeps the bottom clean for chips)
    foot_font = load_font("DejaVuSans.ttf", 30)
    gh = "github.com/nuniversity"
    site = "nuniversity.pages.dev"
    draw.text((W - 72 - draw.textlength(gh, font=foot_font), 86), gh,
              font=foot_font, fill=(255, 255, 255, 220))
    draw.text((W - 72 - draw.textlength(site, font=foot_font), 128), site,
              font=foot_font, fill=(224, 242, 254))

    # Title + tagline
    title_font = load_font("DejaVuSans-Bold.ttf", 108)
    draw.text((76, 226), "Nuniversity", font=title_font, fill=(255, 255, 255))
    sub_font = load_font("DejaVuSans.ttf", 44)
    draw.text((80, 372), "Learn, Code, and Grow", font=sub_font, fill=(226, 232, 240))

    # Stats chips — two deliberate rows of three
    chip_font = load_font("DejaVuSans-Bold.ttf", 28)
    x, y = 76, 458
    for chip in CHIP_ROW_1:
        x = draw_chip(draw, chip, x, y, chip_font)
    x, y = 76, 532
    for chip in CHIP_ROW_2:
        x = draw_chip(draw, chip, x, y, chip_font)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

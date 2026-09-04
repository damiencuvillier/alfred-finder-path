#!/usr/bin/env python3
# Render flag emojis to PNG (Apple Color Emoji) so they can be used as
# image links in the README: images inside <a> get no underline on GitHub.
from PIL import Image, ImageFont, ImageDraw
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "flags"); os.makedirs(OUT, exist_ok=True)
FLAGS = {"en":"🇬🇧","fr":"🇫🇷","de":"🇩🇪","es":"🇪🇸","it":"🇮🇹","pt":"🇵🇹","ja":"🇯🇵","zh":"🇨🇳","el":"🇬🇷"}
font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 160)  # bitmap strike size
for code, emoji in FLAGS.items():
    im = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((100, 100), emoji, font=font, embedded_color=True, anchor="mm")
    bbox = im.getchannel("A").getbbox()
    im = im.crop(bbox)
    im.thumbnail((96, 96), Image.LANCZOS)
    im.save(os.path.join(OUT, f"{code}.png"))
    print("→ assets/flags/%s.png %s" % (code, im.size))

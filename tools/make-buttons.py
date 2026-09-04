#!/usr/bin/env python3
"""Render assets/download/<lang>.png: workflow icon with a two-row download
button underneath (label / filename). One image per language, floated right
in the READMEs and fully clickable. Rendered @2x for retina."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import DOWNLOAD as LABELS, CJK

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "download"); os.makedirs(OUT, exist_ok=True)
ICON = Image.open(os.path.join(ROOT, "workflow", "icon.png")).convert("RGBA")
FILE = "Copy-Finder-Path.alfredworkflow"

S = 2                              # retina scale
W = 240 * S                        # image width
ICON_W = 128 * S
GAP = 12 * S
BTN_TOP_H, BTN_BOT_H = 40 * S, 32 * S
R = 10 * S
INDIGO, DARK, WHITE = (94, 92, 230, 255), (58, 58, 64, 255), (255, 255, 255, 255)

bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 17 * S, index=1)
cjk = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 17 * S)
mono = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 10 * S)

def arrow(d, cx, cy, size, fill):
    s = size
    d.rectangle([cx - s * 0.18, cy - s * 0.5, cx + s * 0.18, cy + s * 0.05], fill=fill)
    d.polygon([(cx - s * 0.5, cy), (cx + s * 0.5, cy), (cx, cy + s * 0.5)], fill=fill)

for code, label in LABELS.items():
    H = ICON_W + GAP + BTN_TOP_H + BTN_BOT_H
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    im.paste(ICON.resize((ICON_W, ICON_W), Image.LANCZOS), ((W - ICON_W) // 2, 0))
    d = ImageDraw.Draw(im)
    y0 = ICON_W + GAP
    # button background: rounded, top part indigo, bottom part dark
    # one rounded shape, split by a straight horizontal line (no inner radius)
    d.rounded_rectangle([0, y0, W - 1, H - 1], radius=R, fill=DARK)
    top = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(top).rounded_rectangle([0, y0, W - 1, H - 1], radius=R, fill=INDIGO)
    top.paste((0, 0, 0, 0), [0, y0 + BTN_TOP_H, W, H])
    im.alpha_composite(top)
    d = ImageDraw.Draw(im)
    # top: arrow + label
    f = cjk if code in CJK else bold
    tw = d.textlength(label, font=f)
    aw = 14 * S
    x = (W - (aw + 10 * S + tw)) / 2
    arrow(d, x + aw / 2, y0 + BTN_TOP_H / 2, aw, WHITE)
    d.text((x + aw + 10 * S, y0 + BTN_TOP_H / 2), label, font=f, fill=WHITE, anchor="lm")
    # bottom: filename
    d.text((W / 2, y0 + BTN_TOP_H + BTN_BOT_H / 2), FILE, font=mono, fill=(220, 220, 225, 255), anchor="mm")
    im.save(os.path.join(OUT, f"{code}.png"))
    print(f"→ assets/download/{code}.png")

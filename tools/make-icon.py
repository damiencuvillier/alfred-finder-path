#!/usr/bin/env python3
"""Generate workflow/icon.png (512x512) for the Copy Finder Path workflow.
Clipboard with a bold slash — "path to clipboard"."""
from PIL import Image, ImageDraw, ImageFont
import os

S = 4                      # supersampling
N = 512 * S
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# Background: rounded square, vertical gradient indigo -> violet
bg = Image.new("RGBA", (N, N), (0, 0, 0, 0))
top, bot = (63, 61, 191), (118, 64, 214)
for y in range(N):
    t = y / N
    c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,)
    ImageDraw.Draw(bg).line([(0, y), (N, y)], fill=c)
mask = Image.new("L", (N, N), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, N - 1, N - 1], radius=int(N * 0.22), fill=255)
img.paste(bg, (0, 0), mask)

# Clipboard body
cx, cy = N / 2, N / 2
bw, bh = N * 0.50, N * 0.62
x0, y0 = cx - bw / 2, cy - bh / 2 + N * 0.03
x1, y1 = x0 + bw, y0 + bh
d.rounded_rectangle([x0, y0, x1, y1], radius=int(N * 0.05), fill=(245, 245, 250, 255))
# Clip at top
cw, ch = bw * 0.42, N * 0.09
d.rounded_rectangle([cx - cw / 2, y0 - ch * 0.45, cx + cw / 2, y0 + ch * 0.55],
                    radius=int(N * 0.025), fill=(60, 60, 75, 255))
d.rounded_rectangle([cx - cw * 0.32, y0 - ch * 0.20, cx + cw * 0.32, y0 + ch * 0.20],
                    radius=int(N * 0.015), fill=(245, 245, 250, 255))

# Big amber slash
slash = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(N * 0.66), index=1)
d.text((cx, cy + N * 0.07), "/", font=slash, fill=(255, 173, 51, 255), anchor="mm")

out = os.path.join(ROOT, "workflow", "icon.png")
img.resize((512, 512), Image.LANCZOS).save(out)
print("→ workflow/icon.png")

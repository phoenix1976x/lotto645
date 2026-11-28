# -*- coding: utf-8 -*-
"""Build the 1200x630 OpenGraph preview card for the integrated
Lotto 6/45 + Pension 720+ + Tojeongbigyeol/Saju page.

Run from /workspace:  python3 work/lotto645/make_og.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = "#12151c"
FG = "#eef0f5"
MUT = "#9aa0b0"
PAPER = "#fffdf6"
INK = "#2a2a2a"
LINE = "#cfcab8"
Y, B, R, G, N = "#f2b705", "#2f6fdb", "#d8453a", "#7a8090", "#2e9e5b"
ACC = "#d8453a"
PJ = "#6b4de0"
PJ2 = "#9a6bff"

FONT = "/usr/share/fonts/pickle-hwp/NotoSansCJKkr-Regular.otf"


def f(size):
    return ImageFont.truetype(FONT, size)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# soft glow behind the cards
glow = Image.new("RGB", (W, H), BG)
gd = ImageDraw.Draw(glow)
for i in range(70, 0, -1):
    a = i / 70
    gd.ellipse([860 - 330 * a, 300 - 300 * a, 860 + 350 * a, 300 + 330 * a],
               fill=(int(18 + 24 * (1 - a)), int(21 + 26 * (1 - a)), int(28 + 34 * (1 - a))))
img = Image.blend(img, glow, 0.5)
d = ImageDraw.Draw(img)


def text(xy, s, size, fill, bold=0, anchor="la"):
    d.text(xy, s, font=f(size), fill=fill, anchor=anchor,
           stroke_width=bold, stroke_fill=fill)


# ---------- left column ----------
LX = 66
text((LX, 74), "무료 웹 도구 · Phoenix Academy", 22, MUT)
d.rectangle([LX, 112, LX + 54, 117], fill=ACC)

text((LX, 142), "로또 6/45 · 연금복권", 50, FG, bold=2)
text((LX, 204), "토정비결 · 사주", 50, FG, bold=2)
text((LX, 282), "세 가지를 한 페이지에서, 전부 무료", 24, MUT)

feats = [
    ("로또 6/45", "반자동 · 당첨금 나눠먹기 줄이기", Y),
    ("연금복권 720+", "세트 · 낱장 · 조·자리 반자동", ACC),
    ("토정비결 144괘 · 사주", "총운·12달 + 사주 오행", PJ2),
]
fy = 350
for name, sub, color in feats:
    d.ellipse([LX + 2, fy + 9, LX + 14, fy + 21], fill=color)
    wname = d.textlength(name, font=f(26))
    text((LX + 26, fy), name, 26, FG, bold=1)
    text((LX + 26 + wname + 10, fy + 3), sub, 21, MUT)
    fy += 58

text((LX, 560), "phoenix1976x.github.io/lotto645", 21, "#6b7080")

# ---------- ticket card (kept: 제 oooo회 가상 용지) ----------
TX0, TY0, TX1, TY1 = 700, 40, 1140, 428
d.rounded_rectangle([TX0, TY0, TX1, TY1], radius=10, fill=PAPER)

PX = TX0 + 28
d.text((PX, TY0 + 18), "Lotto 6/45", font=f(32), fill=INK, stroke_width=1, stroke_fill=INK)
w = d.textlength("제 oooo회", font=f(19))
d.text((TX1 - 26 - w, TY0 + 27), "제 oooo회", font=f(19), fill=INK, stroke_width=1, stroke_fill=INK)

d.rectangle([PX, TY0 + 64, TX1 - 26, TY0 + 68], fill=INK)

rows = [("발행일", "xxxx/xx/xx xx:xx"), ("추첨일", "xxxx/xx/xx"), ("지급기한", "xxxx/xx/xx")]
ry = TY0 + 84
for lab, val in rows:
    d.text((PX, ry), lab, font=f(19), fill="#8a8676")
    d.text((PX + 86, ry), val, font=f(21), fill=INK, stroke_width=1, stroke_fill=INK)
    ry += 34

# dashed divider
dy = ry + 6
x = PX
while x < TX1 - 26:
    d.line([x, dy, min(x + 8, TX1 - 26), dy], fill=LINE, width=2)
    x += 16


def ball(cx, cy, r, label, color, fg="#fff"):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    tw = d.textlength(label, font=f(int(r * 1.0)))
    d.text((cx - tw / 2, cy - r * 0.66), label, font=f(int(r * 1.0)), fill=fg)


sets = [["7", "13", "21", "28", "34", "42"], ["3", "11", "19", "25", "31", "45"]]
colors = [Y, B, R, G, N, B]
by = dy + 40
r = 20
for si, s2 in enumerate(sets):
    d.text((PX, by - 11), "AB"[si], font=f(20), fill=INK, stroke_width=1, stroke_fill=INK)
    for i, num in enumerate(s2):
        cx = PX + 48 + i * (2 * r + 5) + r
        fg = "#2a2200" if colors[i] == Y else "#ffffff"
        ball(cx, by, r, num, colors[i], fg)
    by += 56

d.text((PX, TY1 - 42), "금액", font=f(21), fill=INK, stroke_width=1, stroke_fill=INK)
w = d.textlength("0원", font=f(23))
d.text((TX1 - 26 - w, TY1 - 44), "0원", font=f(23), fill=INK, stroke_width=1, stroke_fill=INK)

# ---------- purple card (tojeong + saju) ----------
QX0, QY0, QX1, QY1 = 700, 444, 1140, 612
grad = Image.new("RGB", (QX1 - QX0, QY1 - QY0))
gd2 = ImageDraw.Draw(grad)
c1 = (107, 77, 224)
c2 = (154, 107, 255)
for yy in range(QY1 - QY0):
    t = yy / (QY1 - QY0)
    gd2.line([(0, yy), (QX1 - QX0, yy)],
             fill=(int(c1[0] + (c2[0] - c1[0]) * t),
                   int(c1[1] + (c2[1] - c1[1]) * t),
                   int(c1[2] + (c2[2] - c1[2]) * t)))
mask = Image.new("L", (QX1 - QX0, QY1 - QY0), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, QX1 - QX0 - 1, QY1 - QY0 - 1], radius=12, fill=255)
img.paste(grad, (QX0, QY0), mask)
d = ImageDraw.Draw(img)

text((QX0 + 28, QY0 + 14), "토정비결 144괘 · 사주", 29, "#ffffff", bold=1)
text((QX0 + 28, QY0 + 56), "양력·음력 생년월일만 넣으면", 19, "#e8e0ff")
text((QX0 + 28, QY0 + 82), "올해 총운 + 12달 흐름 + 사주 오행", 19, "#e8e0ff")
text((QX0 + 28, QY0 + 112), "입력값은 기기 안에서만 계산", 16, "#cfc2ff")

chip = [QX1 - 116, QY0 + 26, QX1 - 26, QY0 + 104]
d.rounded_rectangle(chip, radius=10, fill="#5a3ac9", outline="#c9b8ff", width=2)
text(((chip[0] + chip[2]) / 2, chip[1] + 8), "332", 34, "#ffffff", bold=2, anchor="ma")
text(((chip[0] + chip[2]) / 2, chip[1] + 54), "상·중·하괘", 12, "#d8ccff", anchor="ma")

img.save("work/lotto645/og-preview.png", optimize=True)
print("saved", img.size)

"""Logo Ẩm Thực An Tâm, hướng Bột & Lửa.

Chữ: Gluten (nét tròn như bột nhào, SIL OFL) chuyển thành đường vẽ.
Hình: chiếc bánh tortilla tròn có đốm nướng, ba sợi khói nóng.
Chạy: python3 logo_bot_lua.py  -> in JSON các SVG ra stdout.
"""
import json
import math
import os
import random
import sys

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
DO, DO_DAM, BOT, BANH, VANH, DOM, VANG, MUC, RAU = (
    "#D62718", "#A5170D", "#FFF3DD", "#F4D59B", "#E5B566", "#A7652E", "#FFB400", "#3A1A12", "#3E8E41")

_fonts = {}


def fonts(fam, w):
    key = (fam, w)
    if key not in _fonts:
        _fonts[key] = [TTFont(os.path.join(HERE, f"{fam}/files/{fam}-{s}-{w}-normal.woff2"))
                       for s in ("latin", "vietnamese", "latin-ext")
                       if os.path.exists(os.path.join(HERE, f"{fam}/files/{fam}-{s}-{w}-normal.woff2"))]
    return _fonts[key]


def outline(text, fam="gluten", w=900, size=100.0, track=0.0):
    """Trả về (path, bề ngang) của dòng chữ, chân chữ ở y = 0, cỡ chữ `size` (em)."""
    fs = fonts(fam, w)
    upm = fs[0]["head"].unitsPerEm
    sc = size / upm
    out = pathops.Path(); x = 0.0
    for ch in text:
        for f in fs:
            gname = f.getBestCmap().get(ord(ch))
            if gname:
                break
        gp = pathops.Path()
        gs = f.getGlyphSet()
        rec = DecomposingRecordingPen(gs)
        gs[gname].draw(rec)
        rec.replay(TransformPen(gp.getPen(), (sc, 0, 0, -sc, x, 0)))
        out = pathops.op(out, gp, pathops.PathOp.UNION)
        x += f["hmtx"][gname][0] * sc + track * size
    return out, x - track * size


def d(p):
    pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    p.draw(pen); return pen.getCommands()


def bounds(p):
    return p.bounds


# ---------- chữ ----------
WM, WM_W = outline("An Tâm", "gluten", 800, 100)
WM_B = bounds(WM)
AMT, AMT_W = outline("ẨM THỰC", "gluten", 700, 30, .16)
AMT_B = bounds(AMT)
DESC, DESC_W = outline("BÁNH TORTILLAS · DONER KEBAB", "nunito", 800, 15, .14)
DESC_B = bounds(DESC)
A_HAT, A_HAT_W = outline("Â", "gluten", 800, 100)
A_B = bounds(A_HAT)


# ---------- hình ----------
def tortilla(cx, cy, r, seed=4, wob=.011):
    """Vòng bánh hơi méo tự nhiên."""
    rnd = random.Random(seed)
    ph = [rnd.uniform(0, 6.3) for _ in range(3)]
    pts = []
    for i in range(96):
        a = i / 96 * 2 * math.pi
        k = 1 + wob * (math.sin(3 * a + ph[0]) + .6 * math.sin(5 * a + ph[1]) + .4 * math.sin(8 * a + ph[2]))
        pts.append((cx + r * k * math.cos(a), cy + r * k * math.sin(a)))
    s = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts)):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]
        s += f" Q{p1[0]:.1f},{p1[1]:.1f} {(p1[0] + p2[0]) / 2:.1f},{(p1[1] + p2[1]) / 2:.1f}"
    return s + "Z"


def char_spots(cx, cy, r, n, seed, keep_out=None, scale=1.0, color=DOM):
    """Đốm nướng rải gần mép bánh, tránh vùng chữ (keep_out = (x0, y0, x1, y1))."""
    rnd = random.Random(seed)
    out = []
    tries = 0
    while len(out) < n and tries < 4000:
        tries += 1
        a = rnd.uniform(0, 2 * math.pi)
        dd = r * math.sqrt(rnd.uniform(.08, .86))
        x, y = cx + dd * math.cos(a), cy + dd * math.sin(a)
        if keep_out and keep_out[0] < x < keep_out[2] and keep_out[1] < y < keep_out[3]:
            continue
        L = rnd.uniform(5, 14) * scale; W = L * rnd.uniform(.5, .8)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{L / 2:.1f}" ry="{W / 2:.1f}" '
                   f'transform="rotate({rnd.randint(0, 180)} {x:.1f} {y:.1f})" fill="{color}" opacity="{rnd.choice([.35, .5, .7])}"/>')
    return "".join(out)


def steam(cx, top, h, color, w=6.0, gap=26.0):
    s = ""
    for i, dx in enumerate((-gap, 0, gap)):
        x = cx + dx; y0 = top + h + (6 if i != 1 else 0); hh = h - (6 if i != 1 else 0)
        s += (f'<path d="M{x:.1f},{y0:.1f} c-{hh * .22:.1f},-{hh * .18:.1f} {hh * .22:.1f},-{hh * .32:.1f} 0,-{hh * .5:.1f} '
              f'c-{hh * .22:.1f},-{hh * .18:.1f} {hh * .22:.1f},-{hh * .32:.1f} 0,-{hh * .5:.1f}" fill="none" stroke="{color}" '
              f'stroke-width="{w}" stroke-linecap="round"/>')
    return s


def place(path_d, bx, x, y, fill, s=1.0):
    """Đặt đường chữ có bounds bx sao cho góc trái-chân (x, y) theo tỉ lệ s."""
    return f'<path transform="translate({x:.2f} {y:.2f}) scale({s})" fill="{fill}" d="{path_d}"/>'


def svg(vb, body, label="Ẩm Thực An Tâm"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>'


WMD, AMTD, DESCD, AD = d(WM), d(AMT), d(DESC), d(A_HAT)


def seal(txt=BOT, top=MUC, disc=BANH, rim=VANH, smoke=DO, band=DO, band2=DO_DAM, spots=True):
    """Logo chính: chiếc bánh tròn, dải băng đỏ mang chữ An Tâm."""
    cx, cy, r = 250, 285, 195
    b = f'<path d="{tortilla(cx, cy, r)}" fill="{disc}"/>'
    b += f'<path d="{tortilla(cx, cy, r - 13, seed=7, wob=.018)}" fill="none" stroke="{rim}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
    if spots:
        b += char_spots(cx, cy, r - 16, 30, 9, keep_out=(20, cy - 128, 480, cy + 118))
    y0, y1 = cy - 52, cy + 48
    b += (f'<path d="M6,{y0 + 26} H70 V{y1 + 26} H6 L28,{(y0 + y1) / 2 + 26} Z" fill="{band2}"/>'
          f'<path d="M494,{y0 + 26} H430 V{y1 + 26} H494 L472,{(y0 + y1) / 2 + 26} Z" fill="{band2}"/>'
          f'<path d="M52,{y1} L70,{y1 + 26} V{y1} Z M448,{y1} L430,{y1 + 26} V{y1} Z" fill="#000" opacity=".28"/>'
          f'<path d="M52,{y0} Q250,{y0 - 16} 448,{y0} V{y1} Q250,{y1 - 16} 52,{y1} Z" fill="{band}"/>')
    wm_s = 330 / (WM_B[2] - WM_B[0])
    ww = (WM_B[2] - WM_B[0]) * wm_s
    b += place(WMD, WM_B, cx - ww / 2 - WM_B[0] * wm_s, cy + 22, txt, round(wm_s, 4))
    b += place(AMTD, AMT_B, cx - AMT_W / 2, cy - 80, top)
    b += place(DESCD, DESC_B, cx - DESC_W / 2, cy + 90, top)
    b += steam(cx, 8, 58, smoke, 8, 34)
    return svg("0 0 500 500", b)


def horiz(txt=DO, top=MUC, disc=BANH, smoke=DO, a_fill=DO):
    """Bản ngang: biểu tượng bánh + chữ."""
    b = mark_body(disc, a_fill, smoke, 0, 0, 1.0)
    x = 250
    b += place(AMTD, AMT_B, x + 4, 150, top)
    b += place(WMD, WM_B, x - WM_B[0], 290, txt, 1.35)
    b += place(DESCD, DESC_B, x + 6, 340, top)
    w = x + (WM_B[2] - WM_B[0]) * 1.35 + 10
    return svg(f"0 0 {w:.0f} 440", b)


def mark_body(disc, a_fill, smoke, ox, oy, s):
    cx, cy, r = 110 + ox, 270 + oy, 105
    b = f'<g transform="translate({ox} {oy}) scale({s})">'
    b += f'<path d="{tortilla(110, 270, r, seed=11)}" fill="{disc}"/>'
    b += char_spots(110, 270, r - 10, 16, 21, keep_out=(55, 200, 165, 330), scale=.8)
    aw = (A_B[2] - A_B[0]) * 1.25
    b += place(AD, A_B, 110 - aw / 2 - A_B[0] * 1.25, 314, a_fill, 1.25)
    b += steam(110, 92, 58, smoke, 7, 24)
    return b + "</g>"


def mark(disc=BANH, a_fill=DO, smoke=DO):
    return svg("0 80 220 305", mark_body(disc, a_fill, smoke, 0, 0, 1.0))


def mark_tron(disc=BANH, a_fill=DO):
    """Chỉ chiếc bánh chữ Â, không khói: cho ảnh đại diện tròn."""
    return svg("0 160 220 220", mark_body(disc, a_fill, "none", 0, 0, 1.0))


def wordmark(txt=DO, smoke=DO):
    """Chữ An Tâm với khói nóng bốc trên dấu mũ."""
    s = 1.0
    b = place(WMD, WM_B, -WM_B[0], 0, txt, s)
    # chữ â ở vị trí thứ 5: lấy tâm theo bề ngang ký tự trong font
    fs = fonts("gluten", 800); upm = fs[0]["head"].unitsPerEm; sc = 100 / upm
    x = 0.0; hat_cx = 0
    for ch in "An Tâm":
        f = next(f for f in fs if f.getBestCmap().get(ord(ch)))
        g = f.getBestCmap()[ord(ch)]; adv = f["hmtx"][g][0] * sc
        if ch == "â":
            hat_cx = x + adv / 2
        x += adv
    b += steam(hat_cx - WM_B[0], WM_B[1] - 50, 36, smoke, 4.5, 14)
    return svg(f"-6 {WM_B[1] - 58:.0f} {WM_B[2] - WM_B[0] + 12:.0f} {-WM_B[1] + 58 + WM_B[3] + 8:.0f}", b)


OUT = {
    "seal": seal(), "seal_do": seal(smoke=BOT, band=MUC, band2="#1F0D08"),
    "seal_mot_mau": seal(txt="#FFFFFF", top=MUC, disc="#FFFFFF", rim=MUC, smoke=MUC, band=MUC, band2=MUC, spots=False),
    "horiz": horiz(), "horiz_do": horiz(txt=BOT, top=BOT, disc=BANH, smoke=BOT, a_fill=DO),
    "mark": mark(), "mark_do": mark(disc=BANH, a_fill=DO, smoke=BOT), "mark_tron": mark_tron(),
    "wordmark": wordmark(), "wordmark_bot": wordmark(BOT, VANG),
}

if __name__ == "__main__":
    json.dump(OUT, sys.stdout)

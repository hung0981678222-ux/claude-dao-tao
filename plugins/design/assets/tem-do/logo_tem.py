"""Hướng "Tem Đỏ": tem niêm phong và băng keo đỏ AN TÂM — mỗi thùng bánh rời xưởng đều được dán tem.
Chữ: Big Shoulders Display (SIL OFL) nét đậm, nén, kiểu chữ in trên thùng hàng.
"""
import math
import os
from functools import lru_cache

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
DO, DO2, TRANG, DEN, KRAFT, NGO, XAM = "#E1251B", "#A3150F", "#FFFFFF", "#141414", "#C9A27A", "#FFC531", "#F3EEE7"
F = {"h": os.path.join(HERE, "fonts-tem", "bsd-900.ttf"), "h7": os.path.join(HERE, "fonts-tem", "bsd-700.ttf"),
     "s": os.path.join(HERE, "fonts-bv", "BeVietnamPro-600.ttf"), "s8": os.path.join(HERE, "fonts-bv", "BeVietnamPro-800.ttf")}


@lru_cache(None)
def _f(k):
    f = TTFont(F[k]); return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm


def text(t, size, k="h", x=0, y=0, fill=DO, anchor="start", track=0.0):
    f, gs, cm, upm = _f(k); s = size / upm; cx = 0; parts = []
    for ch in t:
        n = cm.get(ord(ch))
        if not n:
            continue
        pen = SVGPathPen(gs); gs[n].draw(pen); d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        cx += f["hmtx"][n][0] * s + size * track
    w = cx - size * track; ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    return f'<g fill="{fill}" transform="translate({x + ox:.1f} {y:.1f})">{"".join(parts)}</g>', w


def check(x, y, s, fill, sw=None):
    """Dấu tích."""
    sw = sw or s * .22
    return f'<path d="M{x - s * .5:.1f},{y:.1f} L{x - s * .12:.1f},{y + s * .38:.1f} L{x + s * .55:.1f},{y - s * .42:.1f}" fill="none" stroke="{fill}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'


def ring_text(t, size, cx, cy, R, fill, start=-90, k="s8", track=.18, bottom=False):
    f, gs, cm, upm = _f(k); s = size / upm; items = []
    for ch in t:
        n = cm.get(ord(ch)); d = ""
        if n:
            pen = SVGPathPen(gs); gs[n].draw(pen); d = pen.getCommands()
        items.append((d, (f["hmtx"][n][0] if n else 0) * s + size * track))
    total = sum(w for _, w in items); out = []
    if not bottom:
        ang = math.radians(start) - total / R / 2
        for d, w in items:
            a = ang + w / 2 / R; x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            if d:
                out.append(f'<path transform="translate({x:.1f} {y:.1f}) rotate({math.degrees(a) + 90:.2f}) translate({-w / 2 + size * .09:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
            ang += w / R
    else:
        ang = math.radians(90) + total / R / 2
        for d, w in items:
            a = ang - w / 2 / R; x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            if d:
                out.append(f'<path transform="translate({x:.1f} {y:.1f}) rotate({math.degrees(a) - 90:.2f}) translate({-w / 2 + size * .09:.1f} {size * .36:.1f}) scale({s:.4f} {-s:.4f})" d="{d}"/>')
            ang -= w / R
    return f'<g fill="{fill}">{"".join(out)}</g>'


def rang_cua(cx, cy, R, teeth=36, depth=.06):
    pts = []
    for i in range(teeth * 2):
        a = math.pi * i / teeth; r = R if i % 2 == 0 else R * (1 - depth)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"


def svg(vb, body, label, bg=None):
    x, y, w, h = vb
    r = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.0f} {y:.0f} {w:.0f} {h:.0f}" role="img" aria-label="{label}">{r}{body}</svg>'


def tem(fg=DO, ink=TRANG, accent=NGO):
    """Tem tròn răng cưa: chữ AN TÂM giữa, dấu tích trên, chữ chạy vòng."""
    c = 200
    s = f'<path d="{rang_cua(c, c, 196)}" fill="{fg}"/>'
    s += f'<circle cx="{c}" cy="{c}" r="162" fill="none" stroke="{ink}" stroke-width="5"/><circle cx="{c}" cy="{c}" r="116" fill="none" stroke="{ink}" stroke-width="2.5"/>'
    s += ring_text("ẨM THỰC AN TÂM", 26, c, c, 132, ink, -90)
    s += ring_text("SẢN PHẨM TẬN TÂM", 22, c, c, 134, ink, bottom=True)
    for a in (180, 0):
        x = c + 139 * math.cos(math.radians(a)); s += f'<circle cx="{x:.1f}" cy="{c}" r="5" fill="{accent}"/>'
    s += check(c, 140, 46, accent, 14)
    t, w = text("AN TÂM", 78, "h", c, 246, ink, "middle", .02)
    return svg((0, 0, 400, 400), s + t, "Tem Ẩm Thực An Tâm")


def logo_ngang(fg=DO, sub=DEN, bg=None, ink=TRANG):
    """Bản ngang: tem nhỏ + chữ AN TÂM lớn + dòng ẨM THỰC."""
    t = tem(fg, ink); inner = t[t.index(">") + 1:t.rindex("</svg>")]
    s = f'<g transform="scale(.6)">{inner}</g>'
    w1, w = text("AN TÂM", 190, "h", 262, 196, fg, track=.0)
    t2, tw = text("ẨM THỰC · SẢN PHẨM TẬN TÂM", 22, "s8", 268, 236, sub, track=.26)
    return svg((-6, -6, 262 + max(w, tw) + 30, 262), s + w1 + t2, "Logo ngang Ẩm Thực An Tâm", bg)


def logo_dung(fg=DO, sub=DEN, bg=None, ink=TRANG):
    t = tem(fg, ink); inner = t[t.index(">") + 1:t.rindex("</svg>")]
    s = f'<g transform="translate(-130 -320) scale(.65)">{inner}</g>'
    w1, w = text("AN TÂM", 170, "h", 0, 140, fg, "middle")
    t2, tw = text("ẨM THỰC · SẢN PHẨM TẬN TÂM", 22, "s8", 0, 180, sub, "middle", .26)
    W = max(w, tw) + 60
    return svg((-W / 2, -334, W, 540), s + w1 + t2, "Logo đứng Ẩm Thực An Tâm", bg)


def bang_keo_g(w, h=64, fg=DO, ink=TRANG):
    """Nội dung băng keo (không bọc svg), gốc toạ độ ở góc trên trái."""
    s = f'<rect width="{w}" height="{h}" fill="{fg}"/>'
    s += "".join(f'<path d="M{x},0 l6,5 l6,-5 Z M{x},{h} l6,-5 l6,5 Z" fill="{XAM}"/>' for x in range(0, w, 12))
    x = 14
    while x < w:
        t, tw = text("AN TÂM", h * .58, "h", x, h * .74, ink)
        s += t; x += tw + 18
        s += check(x + h * .16, h * .5, h * .34, NGO, h * .09); x += h * .5 + 18
        t2, tw2 = text("SẢN PHẨM TẬN TÂM", h * .24, "s8", x, h * .6, ink, track=.2)
        s += t2; x += tw2 + 30
    return s


def bang_keo(w, h=64, fg=DO, ink=TRANG):
    """Băng keo niêm phong: chữ AN TÂM lặp, dấu tích, mép răng."""
    s = bang_keo_g(w, h, fg, ink)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMinYMid slice" role="img" aria-label="Băng keo niêm phong An Tâm">{s}</svg>'

"""Hướng "Gói Trọn" bản đỏ: bánh tròn buộc lạt, nút buộc là chiếc lá gập (chính là dấu mũ của chữ â).
Màu: xanh lá chuối đậm, lá non, vàng ngô, kem, đỏ cà chua."""
import math
import os
import random
from functools import lru_cache

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

import make_font_la as FL

HERE = os.path.dirname(os.path.abspath(__file__))
XANH, LA, NGO, NGO2, KEM, CA, NAU, DEN = "#C8102E", "#4F8F3A", "#F4B731", "#E39A1C", "#FFF6E6", "#8E0B20", "#B9772F", "#2A1414"
DO, DO2 = XANH, CA  # XANH giữ tên cũ nhưng là màu đỏ chủ đạo
FONT = {"xb": os.path.join(HERE, "fonts-la", "AnTamLa-ExtraBold.ttf"), "sb": os.path.join(HERE, "fonts-la", "AnTamLa-SemiBold.ttf"),
        "bv": os.path.join(HERE, "fonts-bv", "BeVietnamPro-600.ttf")}


@lru_cache(None)
def _f(k):
    f = TTFont(FONT[k]); return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm, (f["OS/2"].sxHeight or 500)


@lru_cache(None)
def _glyph(k, ch):
    """(đường chữ, đường lá, advance) — lá là các đường viền nằm trên chiều cao chữ thường/hoa."""
    f, gs, cm, upm, xh = _f(k); n = cm.get(ord(ch))
    if not n:
        return "", "", 0
    p = pathops.Path(); gs[n].draw(p.getPen(glyphSet=gs))
    top = (xh if ch.islower() else (f["OS/2"].sCapHeight or 700)) * .98
    body, leaf = pathops.Path(), pathops.Path()
    bp, lp = body.getPen(), leaf.getPen()
    for c in p.contours:
        b = c.bounds
        c.draw(lp if (b and b[1] >= top and ch in "âêôÂÊÔ") else bp)
    out = []
    for q in (body, leaf):
        pen = SVGPathPen(None); q.draw(pen); out.append(pen.getCommands())
    return out[0], out[1], f["hmtx"][n][0]


def text(t, size, k="xb", x=0, y=0, fill=XANH, leaf=None, anchor="start", track=0.0):
    f, gs, cm, upm, xh = _f(k); s = size / upm; cx = 0; a, b = [], []
    for ch in t:
        d, dl, adv = _glyph(k, ch)
        tr = f'transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})"'
        if d:
            a.append(f'<path {tr} d="{d}"/>')
        if dl:
            b.append(f'<path {tr} d="{dl}"/>')
        cx += adv * s + size * track
    w = cx - size * track; ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    g = f'<g transform="translate({x + ox:.1f} {y:.1f})"><g fill="{fill}">{"".join(a)}</g><g fill="{leaf or fill}">{"".join(b)}</g></g>'
    return g, w


def _p(path):
    pen = SVGPathPen(None); path.draw(pen); return pen.getCommands()


def nut_la(cx, cy, w, fill):
    """Nút buộc = chiếc lá gập hình mái (giống dấu mũ)."""
    return f'<path fill="{fill}" d="{_p(FL.la(cx - w / 2 / 1.12, cx + w / 2 / 1.12, cy, cy))}" transform="translate(0 {2 * cy}) scale(1 -1)"/>'


def mark(size=200, ngo=NGO, ngo2=NGO2, lat=DO, soc=NGO, leaf=LA, dom=NAU, bg=None):
    """Bánh tròn buộc lạt chữ thập: viền bánh nướng, đốm nướng, sọc vàng trên lạt, nút là chiếc lá gập."""
    S = size; c = S / 2; R = S * .42
    s = f'<rect width="{S}" height="{S}" rx="{S * .2:.0f}" fill="{bg}"/>' if bg else ""
    s += f'<circle cx="{c}" cy="{c}" r="{R:.1f}" fill="{ngo}"/>'
    s += f'<circle cx="{c}" cy="{c}" r="{R * .9:.1f}" fill="none" stroke="{ngo2}" stroke-width="{S * .014:.1f}" opacity=".7"/>'
    rr = random.Random(5)
    for _ in range(26):
        a = rr.uniform(0, 2 * math.pi); d = math.sqrt(rr.uniform(.06, .95)) * R * .92
        x, y = c + d * math.cos(a), c + d * math.sin(a)
        if abs(x - c) < S * .07 or abs(y - c) < S * .07:
            continue
        s += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{S * rr.uniform(.016, .028):.1f}" ry="{S * .011:.1f}" transform="rotate({rr.randint(0, 180)} {x:.1f} {y:.1f})" fill="{dom}" opacity=".8"/>'
    # lạt chữ thập, cắt theo vòng bánh (nhô ra một chút như sợi lạt vòng qua mép)
    bw = S * .1; L = R + S * .02
    s += f'<rect x="{c - bw / 2:.1f}" y="{c - L:.1f}" width="{bw:.1f}" height="{2 * L:.1f}" rx="{bw * .2:.1f}" fill="{lat}"/><rect x="{c - L:.1f}" y="{c - bw / 2:.1f}" width="{2 * L:.1f}" height="{bw:.1f}" rx="{bw * .2:.1f}" fill="{lat}"/>'
    s += f'<rect x="{c - bw * .12:.1f}" y="{c - L:.1f}" width="{bw * .24:.1f}" height="{2 * L:.1f}" fill="{soc}"/><rect x="{c - L:.1f}" y="{c - bw * .12:.1f}" width="{2 * L:.1f}" height="{bw * .24:.1f}" fill="{soc}"/>'
    s += f'<circle cx="{c}" cy="{c}" r="{bw * .95:.1f}" fill="{lat}"/>'
    s += nut_la(c, c - bw * .25, S * .42, leaf)
    return s


def svg(vb, body, label, bg=None):
    x, y, w, h = vb
    r = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.0f} {y:.0f} {w:.0f} {h:.0f}" role="img" aria-label="{label}">{r}{body}</svg>'


def logo_ngang(fg=XANH, leaf=LA, sub=None, bg=None):
    sub = sub or fg
    ring = f'<circle cx="100" cy="100" r="98" fill="{KEM}"/>' if fg == KEM else ""
    m = f'<g transform="translate(0 -150) scale(.95)">{ring}{mark(200)}</g>'
    w1, w = text("an tâm", 150, "xb", 205, 6, fg, leaf, track=-.02)
    t, tw = text("ẨM THỰC · SẢN PHẨM TẬN TÂM", 24, "sb", 211, 50, sub, track=.12)
    return svg((-10, -170, 215 + max(w, tw) + 20, 240), m + w1 + t, "Logo ngang Ẩm Thực An Tâm", bg)


def logo_dung(fg=XANH, leaf=LA, sub=None, bg=None):
    sub = sub or fg
    w1, w = text("an tâm", 150, "xb", 0, 0, fg, leaf, "middle", -.02)
    ring = f'<circle cx="100" cy="100" r="98" fill="{KEM}"/>' if fg == KEM else ""
    m = f'<g transform="translate(-95 -345) scale(.95)">{ring}{mark(200)}</g>'
    t, tw = text("ẨM THỰC · SẢN PHẨM TẬN TÂM", 24, "sb", 0, 56, sub, anchor="middle", track=.12)
    W = max(w, tw) + 80
    return svg((-W / 2, -365, W, 455), m + w1 + t, "Logo đứng Ẩm Thực An Tâm", bg)


def bieu_tuong(bg=KEM):
    return svg((0, 0, 200, 200), mark(200, bg=bg), "Biểu tượng bánh gói An Tâm")


def tem(fg=XANH, ring=KEM):
    """Tem tròn: biểu tượng giữa, chữ chạy vòng."""
    import logo_vom as L
    L.SERIF = FONT["xb"]; L._fonts.cache_clear()
    s = f'<circle cx="200" cy="200" r="196" fill="{fg}"/><circle cx="200" cy="200" r="182" fill="none" stroke="{ring}" stroke-width="2" stroke-dasharray="1 7" stroke-linecap="round"/>'
    s += L._ring_text("GÓI TRỌN TẬN TÂM", 30, 200, 200, 150, ring, -90, key="serif", track=.12)
    s += L._ring_bottom("ẨM THỰC AN TÂM", 26, 200, 200, 152, ring, key="serif", track=.14)
    s += f'<g transform="translate(110 110) scale(.9)">{mark(200)}</g>'
    return svg((0, 0, 400, 400), s, "Tem Ẩm Thực An Tâm")

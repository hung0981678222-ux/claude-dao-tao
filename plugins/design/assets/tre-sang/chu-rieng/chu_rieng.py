"""Chữ "an tâm" cá nhân hoá trên khung Lexend 800: 4 kiểu.
- tron:  chữ a vẽ lại thành đĩa bánh tròn hoàn hảo + thân đứng, chữ t có đỉnh cắt chéo.
- dao:   mọi đầu nét cắt chéo 30 độ như nhát dao thái thịt doner.
- sot:   giọt sốt chảy từ chân chữ.
- khuon: khe hở kiểu chữ in khuôn (stencil) như in trên thùng hàng.
"""
import math

import pathops
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen

import logo_bot_lua as LB
import logo_tre as T

U, D, I = pathops.PathOp.UNION, pathops.PathOp.DIFFERENCE, pathops.PathOp.INTERSECTION
SIZE, TRACK = 100.0, -0.05


def op(a, b, k):
    return pathops.op(a, b, k)


def poly(pts):
    p = pathops.Path(); pen = p.getPen(); pen.moveTo(pts[0])
    for q in pts[1:]:
        pen.lineTo(q)
    pen.closePath(); return p


def rect(x0, y0, x1, y1):
    return poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def circle(cx, cy, r):
    k = .5523 * r
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((cx + r, cy))
    pen.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    pen.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    pen.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    pen.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    pen.closePath(); return p


def glyphs(text="an tam"):
    fs = LB.fonts("lexend", 800)
    upm = fs[0]["head"].unitsPerEm; sc = SIZE / upm
    out, x = [], 0.0
    for ch in text:
        f = next(f for f in fs if f.getBestCmap().get(ord(ch)))
        g = f.getBestCmap()[ord(ch)]; adv = f["hmtx"][g][0] * sc
        p = pathops.Path()
        if ch != " ":
            gs = f.getGlyphSet(); rec = DecomposingRecordingPen(gs); gs[g].draw(rec)
            rec.replay(TransformPen(p.getPen(), (sc, 0, 0, -sc, x, 0)))
        out.append([ch, p, x, adv])
        x += adv + TRACK * SIZE
    return out, x - TRACK * SIZE


def merge(gl):
    p = pathops.Path()
    for _, g, _, _ in gl:
        p = op(p, g, U)
    return p


XH = -T.A_TOP  # chiều cao chữ thường (dương)


def a_tron(x, adv):
    """Chữ a: đĩa tròn + thân đứng phải, lòng tròn."""
    b = T.AB
    w = b[2] - b[0]; stem = w * .27
    r = (XH + 1) / 2
    cx = x + b[0] + r + 1; cy = -r + .5
    ring = op(circle(cx, cy, r), circle(cx, cy, r - stem * .92), D)
    st = rect(x + b[2] - stem, -XH - .5, x + b[2], 0)
    # đốm nướng nhỏ trong lòng chữ
    dots = op(op(circle(cx - r * .18, cy - r * .12, r * .1), circle(cx + r * .14, cy + r * .2, r * .08), U), circle(cx + r * .2, cy - r * .22, r * .06), U)
    return op(op(ring, st, U), dots, U)


def cut_tops(p, x0, x1, ytop, depth=12, ang=30):
    """Cắt chéo phần đỉnh trong khoảng x0..x1."""
    t = math.tan(math.radians(ang))
    w = x1 - x0
    tri = poly([(x0 - 1, ytop - 2), (x1 + 1, ytop - 2), (x1 + 1, ytop - 2 + .1), (x0 - 1, ytop - 2 + (w + 2) * t)])
    return op(p, tri, D)


DRIPS = []


def kieu(name):
    DRIPS.clear()
    gl, W = glyphs()
    hat_fill_cut = True
    if name == "tron":
        for g in gl:
            if g[0] == "a":
                g[1] = a_tron(g[2], g[3])
            if g[0] == "t":
                b = g[1].bounds
                g[1] = op(g[1], poly([(b[0] - 1, b[1] - 1), (b[0] + 16, b[1] - 1), (b[0] - 1, b[1] + 16)]), D)
    elif name == "dao":
        for g in gl:
            if g[0] == " ":
                continue
            b = g[1].bounds
            c = 11
            if g[0] in "nmt":
                g[1] = op(g[1], poly([(b[0] - 1, b[1] - 1), (b[0] + c, b[1] - 1), (b[0] - 1, b[1] + c * .8)]), D)
            g[1] = op(g[1], poly([(b[2] + 1, -c * .9), (b[2] + 1, 1), (b[2] - c, 1)]), D)
    elif name == "sot":
        drips = {"a": [(.8, 20, 6.5)], "n": [], "t": [(.5, 28, 7.5)], "m": [(.86, 15, 6)]}
        seen = {}
        for g in gl:
            if g[0] not in drips:
                continue
            seen[g[0]] = seen.get(g[0], 0) + 1
            if g[0] == "a" and seen["a"] == 2:
                continue
            b = g[1].bounds
            for fx, ln, r in drips[g[0]]:
                cx = b[0] + (b[2] - b[0]) * fx
                pp = pathops.Path(); pen = pp.getPen()
                pen.moveTo((cx - r * 2.4, -6)); pen.lineTo((cx + r * 2.4, -6)); pen.lineTo((cx + r * 2.4, -.5))
                pen.curveTo((cx + r * 1.1, -.5), (cx + r * .8, 3), (cx + r * .8, 9))
                pen.lineTo((cx + r * .8, ln - r * 1.1))
                pen.curveTo((cx + r * 1.35, ln - r * .2), (cx + r * .7, ln + r * .55), (cx, ln + r * .55))
                pen.curveTo((cx - r * .7, ln + r * .55), (cx - r * 1.35, ln - r * .2), (cx - r * .8, ln - r * 1.1))
                pen.lineTo((cx - r * .8, 9))
                pen.curveTo((cx - r * .8, 3), (cx - r * 1.1, -.5), (cx - r * 2.4, -.5))
                pen.closePath()
                DRIPS.append(pp)
    elif name == "khuon":
        for g in gl:
            if g[0] == " ":
                continue
            b = g[1].bounds
            gaps = {"a": [b[0] + (b[2] - b[0]) * .42], "n": [b[0] + (b[2] - b[0]) * .3], "t": [], "m": [b[0] + (b[2] - b[0]) * .33, b[0] + (b[2] - b[0]) * .66]}[g[0]]
            for gx in gaps:
                g[1] = op(g[1], rect(gx - 2.6, b[1] - 2, gx + 2.6, b[1] + (b[3] - b[1]) * .42), D)
            if g[0] == "t":
                g[1] = op(g[1], rect(b[0] - 1, -XH + 9.6, b[2] + 1, -XH + 14.6), D)
    p = merge(gl)
    a2 = [g for g in gl if g[0] == "a"][1]
    ab = a2[1].bounds
    return LB.d(p), (ab[0] + ab[2]) / 2, ab[1], p.bounds


def svg(name, fg, hatc, cut, label="an tâm", extra=""):
    d, hx, htop, b = kieu(name)
    dp = pathops.Path()
    for x in DRIPS:
        dp = op(dp, x, U)
    drip = f'<path fill="{hatc}" d="{LB.d(dp)}"/>' if DRIPS else ""
    if DRIPS:
        b = (b[0], b[1], b[2], dp.bounds[3])
    hat = T.hat(hx - (3 if name != "tron" else 0), htop - 6, 44, hatc, cut)
    y1 = b[3] + 4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{b[0] - 6:.0f} {htop - 46:.0f} {b[2] - b[0] + 12:.0f} {y1 - htop + 46:.0f}" '
            f'role="img" aria-label="{label}">{drip}<path fill="{fg}" d="{d}"/>{hat}{extra}</svg>')

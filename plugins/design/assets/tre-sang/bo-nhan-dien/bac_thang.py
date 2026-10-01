"""Chữ bậc thang dựng bằng font An Tâm Sans (ExtraBold hoặc Nét Đứt), góc 30 độ.
stairs(lines, fg, side, hi, hi_idx, font="ExtraBold") -> chuỗi SVG.
"""
import math
import os
from functools import lru_cache

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
C, S = math.cos(math.pi / 6), math.sin(math.pi / 6)


@lru_cache(None)
def _font(style):
    f = TTFont(style if style.endswith(".ttf") else os.path.join(HERE, f"AnTamSans-{style}.ttf"))
    gs = f.getGlyphSet(); cmap = f.getBestCmap()
    return f, gs, cmap, f["OS/2"].sCapHeight or 700


@lru_cache(None)
def _glyph(style, ch):
    f, gs, cmap, cap = _font(style)
    n = cmap.get(ord(ch))
    if not n:
        return None
    pen = SVGPathPen(gs)
    gs[n].draw(pen)
    return f["hmtx"][n][0], pen.getCommands()


def word(t, cap, style="ExtraBold", track=-.02):
    f, gs, cmap, capu = _font(style)
    s = cap / capu; x = 0; out = ""
    for ch in t:
        g = _glyph(style, ch)
        if not g:
            continue
        adv, d = g
        if d:
            out += f'<path transform="translate({x:.1f} 0) scale({s:.5f} {-s:.5f})" d="{d}"/>'
        x += adv * s + cap * track
    return out, max(0, x - cap * track)


def shade(h, k=.82):
    n = int(h[1:], 16); r, g, b = n >> 16, n >> 8 & 255, n & 255
    return f"rgb({round(r * k)},{round(g * k)},{round(b * k)})"


def stairs(lines, fg, side=None, hi=None, hi_idx=(), D=120, H=150, F=.66, style="ExtraBold", pad=30, bg=None, label=None):
    side = side or shade(fg); hi = hi or fg
    fx = fy = 0; xs, ys = [], []; body = ""; B = .12
    for i, t in enumerate(lines):
        t = t.upper()
        flat = i % 2 == 0
        col = hi if i in hi_idx else (fg if flat else side)
        if flat:
            p, ln = word(t, D * F, style); o = D * B
            body += f'<g fill="{col}" transform="matrix({C:.4f} {S} {-C:.4f} {S} {fx + C * o:.1f} {fy - S * o:.1f})">{p}</g>'
            xs += [fx, fx + C * ln, fx + C * D, fx + C * (ln + D)]; ys += [fy, fy + S * ln, fy - S * D, fy + S * (ln - D)]
        else:
            p, ln = word(t, H * F, style); bx, by, o = fx, fy + H, H * B
            body += f'<g fill="{col}" transform="matrix({C:.4f} {S} 0 1 {bx:.1f} {by - o:.1f})">{p}</g>'
            xs += [fx, bx + C * ln, fx + C * ln, bx]; ys += [fy, by + S * ln, fy + S * ln, by]
            fx, fy = bx - C * D, by + S * D
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad - 30, max(ys) + pad
    rect = f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="{bg}"/>' if bg else ""
    lab = label or " ".join(lines)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}" role="img" aria-label="{lab}">{rect}{body}</svg>'

"""Tạo font thương hiệu "An Tâm Sans" từ Lexend 800 (SIL OFL 1.1, đổi tên theo điều khoản Reserved Font Name).

Dấu hiệu riêng, áp cho mọi chữ:
1. Nhát dao: góc trên bên trái mỗi chữ cắt chéo, góc dưới bên phải khía một vết nhỏ.
2. Mũ bánh: mọi dấu mũ (â ê ô, có cả dấu thanh đi kèm) là chiếc bánh gập đôi có đốm nướng.

Chạy: python3 make_font.py  -> AnTamSans-latin.woff2, AnTamSans-vietnamese.woff2, AnTamSans.ttf
"""
import os

import pathops
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
K = .5523
CHAMFER = 120       # đơn vị font (upm 1000), bản đậm
NOTCH = 92


def path_of(font, name):
    p = pathops.Path()
    font.getGlyphSet()[name].draw(p.getPen(glyphSet=font.getGlyphSet()))
    return p


def poly(pts):
    p = pathops.Path(); pen = p.getPen(); pen.moveTo(pts[0])
    for q in pts[1:]:
        pen.lineTo(q)
    pen.closePath(); return p


def ellipse(cx, cy, rx, ry):
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((cx + rx, cy))
    pen.curveTo((cx + rx, cy + K * ry), (cx + K * rx, cy + ry), (cx, cy + ry))
    pen.curveTo((cx - K * rx, cy + ry), (cx - rx, cy + K * ry), (cx - rx, cy))
    pen.curveTo((cx - rx, cy - K * ry), (cx - K * rx, cy - ry), (cx, cy - ry))
    pen.curveTo((cx + K * rx, cy - ry), (cx + rx, cy - K * ry), (cx + rx, cy))
    pen.closePath(); return p


def dome(x0, x1, y0, y1):
    """Bánh gập đôi trong khung (y hướng lên): cạnh phẳng dưới, vòm trên, 3 đốm khoét."""
    w = x1 - x0; cx = (x0 + x1) / 2; h = y1 - y0
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, y0))
    pen.curveTo((x0, y0 + h * 1.32), (x1, y0 + h * 1.32), (x1, y0))
    pen.closePath()
    for dx, dy, r in [(-.24, .36, .075), (.02, .62, .06), (.22, .34, .085)]:
        p = pathops.op(p, ellipse(cx + dx * w, y0 + dy * h, r * w * 1.25, r * w * .85), pathops.PathOp.DIFFERENCE)
    return p


def contours(p):
    out = []
    for c in p.contours:
        out.append(c)
    return out


def set_glyph(font, name, p):
    pen = TTGlyphPen(font.getGlyphSet())
    p.draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
    font["glyf"][name] = pen.glyph()


def knife(p):
    b = p.bounds
    if b is None or (b[3] - b[1]) < 400:
        return p
    x0, y0, x1, y1 = b
    tri = poly([(x0 - 2, y1 + 2), (x0 + CHAMFER, y1 + 2), (x0 - 2, y1 - CHAMFER * .85)])
    p = pathops.op(p, tri, pathops.PathOp.DIFFERENCE)
    notch = poly([(x1 + 2, y0 - 2), (x1 + 2, y0 + NOTCH), (x1 - NOTCH, y0 - 2)])
    return pathops.op(p, notch, pathops.PathOp.DIFFERENCE)


def tortilla_cap(p):
    """Thay hình dấu mũ (đường viền rộng nhất) bằng chiếc bánh, giữ dấu thanh đi kèm."""
    cs = contours(p)
    if not cs:
        return p
    widest = max(cs, key=lambda c: (c.bounds[2] - c.bounds[0]))
    out = pathops.Path()
    for c in cs:
        if c is widest:
            x0, y0, x1, y1 = c.bounds
            pad = (x1 - x0) * .06
            out = pathops.op(out, dome(x0 - pad, x1 + pad, y0 - 6, y1 + 4), pathops.PathOp.UNION)
        else:
            q = pathops.Path(); c.draw(q.getPen())
            out = pathops.op(out, q, pathops.PathOp.UNION)
    return out


def build(sub, w=800, style="ExtraBold"):
    global CHAMFER, NOTCH
    CHAMFER, NOTCH = (120, 92) if w >= 700 else (70, 54)
    f = TTFont(os.path.join(HERE, f"lexend/files/lexend-{sub}-{w}-normal.woff2"))
    glyf = f["glyf"]
    caps = [n for n in f.getGlyphOrder() if n.startswith("uni0302") or n == "circumflex"]
    for n in f.getGlyphOrder():
        g = glyf[n]
        if g.isComposite() or g.numberOfContours == 0:
            continue
        p = path_of(f, n)
        if n in caps:
            p = tortilla_cap(p)
        elif "comb" not in n and not n.startswith("uni03"):
            p = knife(p)
        else:
            continue
        set_glyph(f, n, p)
    # tên font mới theo điều khoản OFL (không dùng tên "Lexend")
    for rec in f["name"].names:
        if rec.nameID in (1, 16):
            rec.string = "An Tam Sans"
        elif rec.nameID in (2, 17):
            rec.string = style
        elif rec.nameID == 4:
            rec.string = f"An Tam Sans {style}"
        elif rec.nameID == 6:
            rec.string = f"AnTamSans-{style}"
        elif rec.nameID == 3:
            rec.string = f"AnTamSans-{style};1.0"
    for t in ("hdmx", "LTSH", "VDMX", "fpgm", "prep", "cvt "):
        if t in f:
            del f[t]
    f["maxp"].maxComponentDepth = max(1, f["maxp"].maxComponentDepth)
    f.flavor = "woff2"
    f.save(os.path.join(HERE, f"AnTamSans-{style}-{sub}.woff2"))
    f.flavor = None
    return f


if __name__ == "__main__":
    from fontTools.merge import Merger
    for w, style in ((800, "ExtraBold"), (400, "Regular")):
        parts = []
        for sub in ("latin", "vietnamese"):
            ft = build(sub, w, style)
            fn = os.path.join(HERE, f"_tmp-{style}-{sub}.ttf"); ft.save(fn); parts.append(fn)
        try:
            m = Merger().merge(parts)
            m.save(os.path.join(HERE, f"AnTamSans-{style}.ttf"))
            print("ttf ok", style)
        except Exception as e:  # gộp không được thì vẫn còn 2 file woff2
            print("merge failed", style, e)
        for fn in parts:
            os.remove(fn)

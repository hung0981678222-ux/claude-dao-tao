"""Chữ AN TÂM hệ Vòm: mọi nét cùng độ dày, chữ A là mái vòm, dấu mũ là nửa chiếc bánh."""
import pathops
from fontTools.pens.svgPathPen import SVGPathPen

K = 0.5523
H = 100.0     # chiều cao chữ hoa
S = 23.0      # độ dày nét


def P():
    return pathops.Path()


def rect(x0, y0, x1, y1):
    p = P(); pen = p.getPen()
    pen.moveTo((x0, y0)); pen.lineTo((x1, y0)); pen.lineTo((x1, y1)); pen.lineTo((x0, y1)); pen.closePath()
    return p


def poly(pts):
    p = P(); pen = p.getPen()
    pen.moveTo(pts[0])
    for q in pts[1:]:
        pen.lineTo(q)
    pen.closePath()
    return p


def arch(x0, x1, ytop, ybot):
    """Mái vòm: nửa tròn trên, thân chữ nhật xuống ybot (trục y hướng xuống)."""
    r = (x1 - x0) / 2; cx = x0 + r; cy = ytop + r
    p = P(); pen = p.getPen()
    pen.moveTo((x0, ybot)); pen.lineTo((x0, cy))
    pen.curveTo((x0, cy - K * r), (cx - K * r, ytop), (cx, ytop))
    pen.curveTo((cx + K * r, ytop), (x1, cy - K * r), (x1, cy))
    pen.lineTo((x1, ybot)); pen.closePath()
    return p


def half_moon(x0, x1, ybase):
    """Nửa chiếc bánh gập đôi: nửa tròn, cạnh phẳng nằm dưới."""
    r = (x1 - x0) / 2; cx = x0 + r
    p = P(); pen = p.getPen()
    pen.moveTo((x0, ybase))
    pen.curveTo((x0, ybase - K * r), (cx - K * r, ybase - r), (cx, ybase - r))
    pen.curveTo((cx + K * r, ybase - r), (x1, ybase - K * r), (x1, ybase))
    pen.closePath()
    return p


def op(a, b, kind):
    return pathops.op(a, b, kind)


U, D = pathops.PathOp.UNION, pathops.PathOp.DIFFERENCE


def union(*ps):
    out = ps[0]
    for q in ps[1:]:
        out = op(out, q, U)
    return out


def glyph_A(x, w=84):
    outer = arch(x, x + w, 0, H)
    inner_top = arch(x + S, x + w - S, S, 60)
    inner_bot = rect(x + S, 60 + S * .82, x + w - S, H + 1)
    return op(op(outer, inner_top, D), inner_bot, D), w


def glyph_N(x, w=80):
    d = S * 1.08
    diag = poly([(x, 0), (x + d, 0), (x + w, H), (x + w - d, H)])
    return union(rect(x, 0, x + S, H), rect(x + w - S, 0, x + w, H), diag), w


def glyph_T(x, w=76):
    return union(rect(x, 0, x + w, S), rect(x + (w - S) / 2, 0, x + (w + S) / 2, H)), w


def glyph_M_vom(x, w=112):
    """M hai mái vòm liền nhau."""
    a = (w + S) / 2
    left = op(arch(x, x + a, 0, H), arch(x + S, x + a - S, S, H + 1), D)
    right = op(arch(x + w - a, x + w, 0, H), arch(x + w - a + S, x + w - S, S, H + 1), D)
    return union(left, right), w


def glyph_M(x, w=104):
    d = S * 1.1; m = x + w / 2
    v = poly([(x, 0), (x + d, 0), (m + d / 2, H * .72), (m - d / 2, H * .72)])
    v2 = poly([(x + w, 0), (x + w - d, 0), (m - d / 2, H * .72), (m + d / 2, H * .72)])
    return union(rect(x, 0, x + S, H), rect(x + w - S, 0, x + w, H), v, v2), w


def hat(x, w):
    """Dấu mũ nửa chiếc bánh đặt trên chữ rộng w."""
    hw = 44
    x0 = x + (w - hw) / 2
    return half_moon(x0, x0 + hw, -12)


def to_d(path):
    pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    path.draw(pen)
    return pen.getCommands()


GAP, SPACE = 11, 30


def wordmark(m_style="vom"):
    parts = []; x = 0
    for ch in ["A", "N", " ", "T", "Â", "M"]:
        if ch == " ":
            x += SPACE; continue
        if ch in "AÂ":
            g, w = glyph_A(x)
            if ch == "Â":
                g = union(g, hat(x, w))
        elif ch == "N":
            g, w = glyph_N(x)
        elif ch == "T":
            g, w = glyph_T(x)
        else:
            g, w = (glyph_M_vom if m_style == "vom" else glyph_M)(x)
        parts.append(g); x += w + GAP
    return union(*parts), x - GAP


def mark():
    """Biểu tượng rút gọn: chữ Â vòm + dấu mũ nửa bánh, đặt trong ô vuông 160."""
    g, w = glyph_A(0)
    return union(g, hat(0, w)), w


if __name__ == "__main__":
    import json, sys
    out = {}
    for st in ["vom", "goc"]:
        p, w = wordmark(st)
        out["wm_" + st] = {"d": to_d(p), "w": w}
    p, w = mark()
    out["mark"] = {"d": to_d(p), "w": w}
    a, w = glyph_A(0); out["A"] = {"d": to_d(a), "w": w}
    json.dump(out, sys.stdout)

"""Hướng "Gói Trọn": font Montserrat Alternates (SIL OFL), dấu mũ (â ê ô) là chiếc lá chuối nghiêng có gân giữa.
Chạy: python3 make_font_la.py -> fonts-la/AnTamLa-{ExtraBold,SemiBold}.ttf/.woff2
"""
import math
import os

import pathops

import make_fonts_multi as M

HERE = os.path.dirname(os.path.abspath(__file__))


def _lens(p0, p1, t):
    """Lá thon hai đầu dọc đoạn p0 -> p1, bề rộng lớn nhất t."""
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]; L = math.hypot(dx, dy); nx, ny = -dy / L * t, dx / L * t
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo(p0)
    pen.curveTo((p0[0] + dx * .2 + nx, p0[1] + dy * .2 + ny), (p1[0] - dx * .25 + nx * .9, p1[1] - dy * .25 + ny * .9), p1)
    pen.curveTo((p1[0] - dx * .25 - nx * .9, p1[1] - dy * .25 - ny * .9), (p0[0] + dx * .2 - nx, p0[1] + dy * .2 - ny), p0)
    pen.closePath(); return p


def la(x0, x1, y0, y1):
    """Lá chuối gập đôi thành hình mái (^): hai cánh lá thon, chung đỉnh, gân giữa mảnh."""
    cx = (x0 + x1) / 2; w = (x1 - x0) * 1.12; h = w * .5
    apex = (cx, y0 + h); lt = (cx - w / 2, y0); rt = (cx + w / 2, y0)
    t = w * .16
    p = pathops.op(_lens(apex, lt, t), _lens(apex, rt, t), pathops.PathOp.UNION)
    # đỉnh bo cho liền khối
    p = pathops.op(p, M.ellipse(cx, apex[1] - t * .55, t * .62, t * .62), pathops.PathOp.UNION)
    for tip in (lt, rt):
        v = pathops.Path(); vp = v.getPen(); k = t * .16
        a0 = (apex[0] + (tip[0] - apex[0]) * .12, apex[1] + (tip[1] - apex[1]) * .12 - t * .1)
        a1 = (apex[0] + (tip[0] - apex[0]) * .8, apex[1] + (tip[1] - apex[1]) * .8)
        vp.moveTo((a0[0], a0[1] - k)); vp.lineTo((a1[0], a1[1] - k * .3)); vp.lineTo((a1[0], a1[1] + k * .3)); vp.lineTo((a0[0], a0[1] + k)); vp.closePath()
        p = pathops.op(p, v, pathops.PathOp.DIFFERENCE)
    return p


M.dome = la
M.OUT = os.path.join(HERE, "fonts-la")

if __name__ == "__main__":
    root = os.path.join(HERE, "montserrat-alternates", "files")
    for style, w in (("ExtraBold", 800), ("SemiBold", 600)):
        files = [p for p in (os.path.join(root, f"montserrat-alternates-{s}-{w}-normal.woff2") for s in ("latin", "vietnamese", "latin-ext")) if os.path.exists(p)]
        M.FONTS = {f"La {style}": (files, f"AnTamLa-{style}", "")}
        M.build(f"La {style}")

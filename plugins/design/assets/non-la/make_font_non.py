"""Hướng "Nón Lá": chữ nét đậm, dấu mũ (â ê ô) là chiếc nón lá có vành.
Dựng từ các font SIL OFL nét đậm. Chạy: python3 make_font_non.py [Tên...] -> fonts-non/AnTam<Tên>-Non.ttf/.woff2
"""
import os
import sys

import pathops

import make_fonts_multi as M

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)


def non(x0, x1, y0, y1):
    """Nón lá: hình chóp, hai sườn hơi lõm, đáy cong nhẹ; một vành sáng cắt ngang thân nón."""
    cx = (x0 + x1) / 2; w = (x1 - x0) * 1.12; x0, x1 = cx - w / 2, cx + w / 2
    h = w * .56; top = y0 + h; sag = h * .07
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, y0))
    pen.curveTo((x0 + w * .2, y0 + h * .2), (cx - w * .1, y0 + h * .72), (cx, top))
    pen.curveTo((cx + w * .1, y0 + h * .72), (x1 - w * .2, y0 + h * .2), (x1, y0))
    pen.curveTo((x1 - w * .2, y0 - sag), (x0 + w * .2, y0 - sag), (x0, y0))
    pen.closePath()
    # vành nón: dải mảnh song song đáy, cắt rỗng
    band = pathops.Path(); bp = band.getPen()
    by = y0 + h * .32; bt = h * .07
    bp.moveTo((x0 - 10, by)); bp.lineTo((x1 + 10, by)); bp.lineTo((x1 + 10, by + bt)); bp.lineTo((x0 - 10, by + bt)); bp.closePath()
    return pathops.op(p, band, pathops.PathOp.DIFFERENCE)


M.dome = non
M.OUT = os.path.join(HERE, "fonts-non")


def fs(fam, w, root=None):
    root = root or os.path.join(HERE, fam, "files")
    return [p for p in (os.path.join(root, f"{fam}-{s}-{w}-normal.woff2") for s in ("latin", "vietnamese", "latin-ext")) if os.path.exists(p)]


BASES = {
    # tên: (file, mô tả)
    "BeVietnam": (fs("be-vietnam-pro", 900), "Be Vietnam Pro Black – khung chữ do nhóm tác giả Việt thiết kế, rất đậm, rõ dấu"),
    "Phudu": (fs("phudu", 900), "Phudu Black – hẹp, đậm, kiểu chữ kẻ biển hiệu"),
    "Anton": (fs("anton", 400, os.path.join(SCR, "anton", "package", "files")), "Anton – cao, nén, mạnh như biển hiệu Sài Gòn xưa"),
    "Dela": (fs("dela-gothic-one", 400), "Dela Gothic One – siêu đậm, rộng, nhìn rõ từ xa"),
}

if __name__ == "__main__":
    for name in (sys.argv[1:] or BASES):
        M.FONTS = {name: (BASES[name][0], f"AnTam{name}-Non", "")}
        M.build(name)

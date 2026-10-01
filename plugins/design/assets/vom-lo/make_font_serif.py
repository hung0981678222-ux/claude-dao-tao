"""An Tâm Serif (hướng Tin cậy · Tinh tế · Ấm áp): dựng từ Fraunces (SIL OFL).
Dấu mũ (â ê ô) thành vòm bếp mảnh: nửa vòng cung đều nét, hai chân cắt bằng.
Chạy: python3 make_font_serif.py -> fonts-serif/AnTamSerif-{SemiBold,Regular}.ttf/.woff2
"""
import os

import pathops

import make_fonts_multi as M

HERE = os.path.dirname(os.path.abspath(__file__))
K = M.K


def half(x0, x1, y0, h):
    """Nửa elip đặc, đáy phẳng tại y0."""
    cx = (x0 + x1) / 2; rx = (x1 - x0) / 2
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, y0))
    pen.curveTo((x0, y0 + K * h), (cx - K * rx, y0 + h), (cx, y0 + h))
    pen.curveTo((cx + K * rx, y0 + h), (x1, y0 + K * h), (x1, y0))
    pen.closePath(); return p


def arch(x0, x1, y0, y1):
    """Vòm lò nướng: nửa vòng cung đều nét, đáy phẳng, có một hạt than hồng ở giữa lòng vòm."""
    cx = (x0 + x1) / 2; w = (x1 - x0) * 1.12; x0, x1 = cx - w / 2, cx + w / 2
    h = w * .5; t = w * .13
    outer = half(x0, x1, y0, h)
    inner = half(x0 + t, x1 - t, y0 - 1, h - t)
    p = pathops.op(outer, inner, pathops.PathOp.DIFFERENCE)
    r = t * .62
    return pathops.op(p, M.ellipse(cx, y0 + r * 1.1, r, r), pathops.PathOp.UNION)


M.dome = arch
WEIGHTS = {"SemiBold": 600, "Regular": 400}
M.OUT = os.path.join(HERE, "fonts-serif")

BASES = {
    # tên: (thư mục fontsource, độ đậm, mô tả)
    "Serif": ("fraunces", 600, "Fraunces – có chân mềm, ấm"),
    "Playfair": ("playfair-display", 700, "Playfair Display – tương phản cao, sang kiểu tạp chí"),
    "Cormorant": ("cormorant-garamond", 700, "Cormorant Garamond – thanh mảnh, cổ điển, rất tinh tế"),
    "Prata": ("prata", 400, "Prata – nét đậm nhạt mạnh, sang kiểu biển hiệu châu Âu"),
    "NotoDisplay": ("noto-serif-display", 600, "Noto Serif Display – gọn, sắc, hiện đại sang"),
}

if __name__ == "__main__":
    import sys
    for name in (sys.argv[1:] or BASES):
        fam, w, _ = BASES[name]
        root = os.path.join(HERE, fam, "files")
        M.FONTS = {name: ([p for p in (os.path.join(root, f"{fam}-{s}-{w}-normal.woff2") for s in ("latin", "vietnamese", "latin-ext")) if os.path.exists(p)], f"AnTam{name}-Vom", "")}
        M.build(name)

"""Tạo nhiều font thương hiệu từ các khung chữ khác nhau (đều SIL OFL), cùng nét riêng: dấu mũ là chiếc bánh.
Chạy: python3 make_fonts_multi.py -> fonts-moi/<Ten>.ttf và .woff2
"""
import os

import pathops
from fontTools.merge import Merger
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
OUT = os.path.join(HERE, "fonts-moi")
K = .5523
CIRC = "âêôÂÊÔấầẩẫậếềểễệốồổỗộẤẦẨẪẬẾỀỂỄỆỐỒỔỖỘ"
BASES = set("aeoAEO")


def fs_files(fam, w, root=None, subs=("latin", "vietnamese", "latin-ext")):
    root = root or os.path.join(HERE, fam, "files")
    return [p for p in (os.path.join(root, f"{fam}-{s}-{w}-normal.woff2") for s in subs) if os.path.exists(p)]


FONTS = {
    # tên hiển thị: (danh sách file, tên PostScript, mô tả)
    "Bricolage": (fs_files("bricolage-grotesque", 800), "AnTamBricolage", "Hiện đại, có khía mực, cá tính trẻ"),
    "Fraunces": ([os.path.join(SCR, "nl", f"fr50-{s}-900.woff2") for s in ("latin", "vietnamese")], "AnTamFraunces", "Có chân mềm, ấm, sang"),
    "Anton": (fs_files("anton", 400, os.path.join(SCR, "anton", "package", "files")), "AnTamAnton", "Cao hẹp, mạnh, hợp biển hiệu và bậc thang"),
    "Baloo": (fs_files("baloo-2", 800), "AnTamBaloo", "Tròn mập, thân thiện, đồ ăn vặt"),
    "Grandstander": (fs_files("grandstander", 900), "AnTamGrandstander", "Vui, nghịch, như vẽ tay"),
    "Dela": (fs_files("dela-gothic-one", 400), "AnTamDela", "Rất đậm, rộng, nổi bật từ xa"),
}


def ellipse(cx, cy, rx, ry):
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((cx + rx, cy))
    pen.curveTo((cx + rx, cy + K * ry), (cx + K * rx, cy + ry), (cx, cy + ry))
    pen.curveTo((cx - K * rx, cy + ry), (cx - rx, cy + K * ry), (cx - rx, cy))
    pen.curveTo((cx - rx, cy - K * ry), (cx - K * rx, cy - ry), (cx, cy - ry))
    pen.curveTo((cx + K * rx, cy - ry), (cx + rx, cy - K * ry), (cx + rx, cy))
    pen.closePath(); return p


def dome(x0, x1, y0, y1):
    w = x1 - x0; cx = (x0 + x1) / 2; h = y1 - y0
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, y0)); pen.curveTo((x0, y0 + h * 1.32), (x1, y0 + h * 1.32), (x1, y0)); pen.closePath()
    for dx, dy, r in [(-.24, .36, .075), (.02, .62, .06), (.22, .34, .085)]:
        u = min(w * .5, h * 1.1)
        p = pathops.op(p, ellipse(cx + dx * w, y0 + dy * h, r * u * 2.1, r * u * 1.45), pathops.PathOp.DIFFERENCE)
    return p


def gpath(f, n):
    p = pathops.Path(); gs = f.getGlyphSet()
    gs[n].draw(p.getPen(glyphSet=gs)); return p


def set_glyph(f, n, p):
    pen = TTGlyphPen(f.getGlyphSet()); p.draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
    f["glyf"][n] = pen.glyph()


def replace_cap(p, min_y):
    """Trong đường p, đường viền rộng nhất nằm trên min_y là dấu mũ -> thay bằng chiếc bánh.
    Các đường viền còn lại vẽ chung một lần để giữ nguyên lỗ trong (counter)."""
    cs = list(p.contours)
    upper = [c for c in cs if c.bounds and c.bounds[1] >= min_y]
    if not upper:
        return p
    widest = max(upper, key=lambda c: c.bounds[2] - c.bounds[0])
    rest = pathops.Path(); pen = rest.getPen()
    for c in cs:
        if c is not widest:
            c.draw(pen)
    x0, y0, x1, y1 = widest.bounds; pad = (x1 - x0) * .06
    lower = [c.bounds[3] for c in cs if c is not widest and c.bounds and c.bounds[1] < min_y]
    gap = min_y * .05
    b = max(y0, (max(lower) + gap) if lower else y0)
    h = min((x1 - x0 + 2 * pad) * .46, max(y1 - b, (x1 - x0) * .25))
    q = dome(x0 - pad, x1 + pad, b, b + h)
    return pathops.op(rest, q, pathops.PathOp.UNION, fix_winding=True)


def process(f):
    """Tách rời từng chữ có dấu mũ (không đụng glyph dấu dùng chung) rồi thay dấu mũ bằng bánh."""
    cmap = f.getBestCmap(); gs = f.getGlyphSet()
    xh = getattr(f["OS/2"], "sxHeight", 0) or 500
    cap = getattr(f["OS/2"], "sCapHeight", 0) or 700
    paths = {}
    for ch in CIRC:
        n = cmap.get(ord(ch))
        if n and n not in paths:
            paths[n] = (gpath(f, n), (xh if ch.islower() else cap) * .98)
    for n, (p, top) in paths.items():
        set_glyph(f, n, replace_cap(p, top))
    return len(paths)


def rename(f, fam, ps):
    for rec in f["name"].names:
        if rec.nameID in (1, 16):
            rec.string = fam
        elif rec.nameID in (2, 17):
            rec.string = "Regular"
        elif rec.nameID == 4:
            rec.string = fam
        elif rec.nameID == 6:
            rec.string = ps
        elif rec.nameID == 3:
            rec.string = ps + ";1.0"
    for t in ("hdmx", "LTSH", "VDMX", "fpgm", "prep", "cvt ", "gasp"):
        if t in f:
            del f[t]


def build(name):
    files, ps, _ = FONTS[name]
    os.makedirs(OUT, exist_ok=True)
    tmp = []
    for i, fp in enumerate(files):
        f = TTFont(fp); f.flavor = None
        t = os.path.join(OUT, f"_{ps}-{i}.ttf"); f.save(t); tmp.append(t)
    m = Merger().merge(tmp) if len(tmp) > 1 else TTFont(tmp[0])
    t = os.path.join(OUT, f"_{ps}.ttf"); m.save(t); m = TTFont(t)
    total = process(m)
    rename(m, f"An Tam {name}", ps)
    m.save(os.path.join(OUT, f"{ps}.ttf"))
    m.flavor = "woff2"; m.save(os.path.join(OUT, f"{ps}.woff2"))
    for x in tmp + [t]:
        os.remove(x)
    c = TTFont(os.path.join(OUT, f"{ps}.ttf")).getBestCmap()
    ok = all(ord(x) in c for x in "ẨẤỐỰđươâêôĂ")
    print(f"{name}: sửa {total} glyph, đủ tiếng Việt={ok}")


if __name__ == "__main__":
    for n in FONTS:
        build(n)

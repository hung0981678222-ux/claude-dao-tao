"""Font "An Tâm Vân" (hướng Điểm Chỉ): dựng từ Be Vietnam Pro (SIL OFL), dấu mũ â ê ô là ba đường vân tay lồng nhau hình mái vòm.
Chạy: python3 make_font_van.py -> fonts-van/AnTamVan-{ExtraBold,Medium}.ttf/.woff2
"""
import os

import pathops

import make_fonts_multi as M

HERE = os.path.dirname(os.path.abspath(__file__))


def van(x0, x1, y0, y1):
    """Ba đường vân cong lồng nhau đồng tâm (như đỉnh vân tay), dáng mái nhọn mềm – đọc được như dấu mũ."""
    cx = (x0 + x1) / 2; w = (x1 - x0) * 1.2; h = w * .5
    t = w * .072
    out = pathops.Path()
    peak0 = y0 + t / 2 + h; g = t * 1.85
    for i in range(3):
        peak = peak0 - i * g; ww = w - i * g * 2.4
        base = y0 + t / 2; hh = peak - base
        a = (cx - ww / 2, base); b = (cx + ww / 2, base)
        p = pathops.Path(); pen = p.getPen()
        pen.moveTo(a)
        pen.curveTo((a[0] + ww * .16, base + hh * .66), (cx - ww * .16, peak), (cx, peak))
        pen.curveTo((cx + ww * .16, peak), (b[0] - ww * .16, base + hh * .66), b)
        pen.endPath()
        p.stroke(t, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
        p.convertConicsToQuads()
        out = pathops.op(out, p, pathops.PathOp.UNION)
    return out


M.dome = van
M.OUT = os.path.join(HERE, "fonts-van")
_process = M.process
INK = {"ExtraBold": 16, "Medium": 12}  # độ loang mực (đơn vị font)
_cur = {"r": 14}


def mem_muc(f, r):
    """Bo tròn mọi góc chữ như mực son loang nhẹ khi in: hợp nhất đường viền với nét viền tròn mảnh."""
    gs = f.getGlyphSet(); n = 0
    for g in f.getGlyphOrder():
        gl = f["glyf"][g]
        if gl.numberOfContours == 0:
            continue
        p = pathops.Path(); gs[g].draw(p.getPen(glyphSet=gs))
        if not list(p.contours):
            continue
        p.simplify(fix_winding=True)
        st = pathops.Path(); p.draw(st.getPen())
        st.stroke(r, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4); st.convertConicsToQuads()
        q = pathops.op(p, st, pathops.PathOp.UNION, fix_winding=True)
        M.set_glyph(f, g, q); n += 1
    return n


def process(f):
    k = _process(f)
    mem_muc(f, _cur["r"])
    return k


M.process = process

if __name__ == "__main__":
    root = os.path.join(HERE, "be-vietnam-pro", "files")
    for style, w in (("ExtraBold", 800), ("Medium", 500)):
        files = [p for p in (os.path.join(root, f"be-vietnam-pro-{s}-{w}-normal.woff2") for s in ("latin", "vietnamese", "latin-ext")) if os.path.exists(p)]
        _cur["r"] = INK[style]
        M.FONTS = {f"Van {style}": (files, f"AnTamVan-{style}", "")}
        M.build(f"Van {style}")

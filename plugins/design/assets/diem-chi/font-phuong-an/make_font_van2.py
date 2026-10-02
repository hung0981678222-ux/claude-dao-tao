"""Các phương án font cho hướng Điểm Chỉ: cùng dấu mũ vân tay, khung chữ khác nhau (SIL OFL).
Chạy: python3 make_font_van2.py [Tên...] -> fonts-van2/AnTam<Tên>.ttf/.woff2
"""
import math
import os
import sys

import pathops

import make_fonts_multi as M
import make_font_van as V

HERE = os.path.dirname(os.path.abspath(__file__))
M.dome = V.van
M.OUT = os.path.join(HERE, "fonts-van2")
_base_process = V._process   # bản gốc (thay dấu mũ), chưa bo mực


def fs(fam, w):
    root = os.path.join(HERE, fam, "files")
    return [p for p in (os.path.join(root, f"{fam}-{s}-{w}-normal.woff2") for s in ("latin", "vietnamese", "latin-ext")) if os.path.exists(p)]


def ke_van(f, period=78, band=40, amp=14, wave=420, ring=20):
    """Chữ kẻ vân: lòng chữ là các đường vân lượn sóng, quanh chữ giữ một đường viền liền."""
    gs = f.getGlyphSet(); n = 0
    for g in f.getGlyphOrder():
        if f["glyf"][g].numberOfContours == 0:
            continue
        p = pathops.Path(); gs[g].draw(p.getPen(glyphSet=gs))
        if not list(p.contours):
            continue
        p.simplify(fix_winding=True)
        x0, y0, x1, y1 = p.bounds
        stripes = pathops.Path(); sp = stripes.getPen()
        y = y0 - period
        while y < y1 + period:
            xs = list(range(int(x0) - 60, int(x1) + 80, 30))
            top = [(x, y + band / 2 + amp * math.sin(x / wave * 2 * math.pi)) for x in xs]
            bot = [(x, y - band / 2 + amp * math.sin(x / wave * 2 * math.pi)) for x in xs]
            sp.moveTo(bot[0]); [sp.lineTo(q) for q in bot[1:]]; [sp.lineTo(q) for q in reversed(top)]; sp.closePath()
            y += period
        inner = pathops.op(p, stripes, pathops.PathOp.INTERSECTION)
        st = pathops.Path(); p.draw(st.getPen())
        st.stroke(ring * 2, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4); st.convertConicsToQuads()
        edge = pathops.op(p, st, pathops.PathOp.INTERSECTION)
        q = pathops.op(inner, edge, pathops.PathOp.UNION, fix_winding=True)
        M.set_glyph(f, g, q); n += 1
    return n


BASES = {
    # tên: (file, độ loang mực, chữ kẻ vân?, mô tả)
    "Moc": (fs("bitter", 900), 10, False, "Bitter Black – chân vuông như chữ khắc con dấu, máy đánh chữ trên phiếu giao hàng"),
    "Am": (fs("fraunces", 900), 8, False, "Fraunces Black – có chân mềm, ấm, có hồn như chữ viết tay của người làm bánh"),
    "Bien": (fs("oswald", 700), 8, False, "Oswald Bold – cao, nén, mạnh như chữ biển hiệu, nhìn rõ từ xa"),
    "Tron": (fs("baloo-2", 800), 10, False, "Baloo 2 ExtraBold – tròn, đầy đặn, thân thiện như chiếc bánh"),
    "Ke": (fs("be-vietnam-pro", 900), 0, True, "Be Vietnam Pro Black kẻ vân – mỗi nét chữ là những đường vân tay, chỉ dùng cho chữ lớn"),
}

if __name__ == "__main__":
    for name in (sys.argv[1:] or BASES):
        files, ink, ke, _ = BASES[name]
        def proc(f, ink=ink, ke=ke):
            k = _base_process(f)
            if ink:
                V.mem_muc(f, ink)
            if ke:
                ke_van(f)
            return k
        M.process = proc
        M.FONTS = {name: (files, f"AnTam{name}", "")}
        M.build(name)

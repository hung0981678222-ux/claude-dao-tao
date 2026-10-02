"""Phương án 04 "Tròn Bánh" thêm nét: dựng từ Baloo 2 ExtraBold (SIL OFL).
Nét chung: dấu mũ vân tay + góc mực loang. Thêm:
  van   – một đường vân lõm chạy liền bên trong nét chữ
  dut   – đường vân lõm đứt quãng như vân tay thật
  cham  – dấu chấm (i, j, dấu nặng, dấu chấm câu) thành vòng xoáy nhỏ
Chạy: python3 make_font_tron.py -> fonts-tron/AnTamTron<Biến thể>.ttf/.woff2
"""
import math
import os
import sys

import pathops
from fontTools.pens.basePen import BasePen

import make_fonts_multi as M
import make_font_van as V
import make_font_van2 as F2

HERE = os.path.dirname(os.path.abspath(__file__))
def van_ngan(x0, x1, y0, y1):
    """Dấu mũ vân tay bản thấp: ba đường vân lồng nhau, chiều cao còn khoảng 2/3 bản cũ."""
    cx = (x0 + x1) / 2; w = (x1 - x0) * 1.12; h = w * .33
    t = w * .066; g = t * 1.7
    out = pathops.Path(); peak0 = y0 + t / 2 + h
    for i in range(3):
        peak = peak0 - i * g; ww = w - i * g * 2.5
        base = y0 + t / 2; hh = peak - base
        a = (cx - ww / 2, base); b = (cx + ww / 2, base)
        p = pathops.Path(); pen = p.getPen()
        pen.moveTo(a)
        pen.curveTo((a[0] + ww * .16, base + hh * .7), (cx - ww * .18, peak), (cx, peak))
        pen.curveTo((cx + ww * .18, peak), (b[0] - ww * .16, base + hh * .7), b)
        pen.endPath()
        out = pathops.op(out, _stroke(p, t), pathops.PathOp.UNION)
    return out


M.dome = V.van
M.OUT = os.path.join(HERE, "fonts-tron")
FILES = F2.fs("baloo-2", 800)
INSET, GROOVE = 34, 11       # độ lùi vào trong và bề rộng đường vân (đơn vị font, upm 1000)


class _Flat(BasePen):
    """Làm phẳng đường cong thành các điểm để cắt nét đứt."""
    def __init__(self):
        super().__init__(None); self.contours = []; self.cur = None
    def _moveTo(self, p):
        self.cur = [p]; self.contours.append(self.cur)
    def _lineTo(self, p):
        self.cur.append(p)
    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for k in range(1, 9):
            t = k / 8; a = (1 - t) ** 3; b = 3 * (1 - t) ** 2 * t; c = 3 * (1 - t) * t * t; d = t ** 3
            self.cur.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for k in range(1, 7):
            t = k / 6; a = (1 - t) ** 2; b = 2 * (1 - t) * t; c = t * t
            self.cur.append((a * p0[0] + b * p1[0] + c * p2[0], a * p0[1] + b * p1[1] + c * p2[1]))
    def _closePath(self):
        if self.cur:
            self.cur.append(self.cur[0])


def _stroke(path, w):
    s = pathops.Path(); path.draw(s.getPen())
    s.stroke(w, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4); s.convertConicsToQuads(); return s


def _eroded(p, d):
    return pathops.op(p, _stroke(p, 2 * d), pathops.PathOp.DIFFERENCE)


def _dashes(path, dash=70, gap=34, w=GROOVE):
    """Nét đứt dọc theo đường viền: cắt polyline thành đoạn rồi tô nét."""
    fp = _Flat(); path.draw(fp); out = pathops.Path()
    for pts in fp.contours:
        acc = 0; on = True; seg = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            L = math.dist(a, b); pos = 0
            while L - pos > 1e-6:
                lim = (dash if on else gap) - acc; step = min(lim, L - pos)
                t = (pos + step) / L; q = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
                if on:
                    seg.append(q)
                acc += step; pos += step
                if acc >= (dash if on else gap) - 1e-6:
                    if on and len(seg) > 1:
                        sp = pathops.Path(); pen = sp.getPen(); pen.moveTo(seg[0]); [pen.lineTo(x) for x in seg[1:]]; pen.endPath()
                        out = pathops.op(out, _stroke(sp, w), pathops.PathOp.UNION)
                    on = not on; acc = 0; seg = [q]
        if on and len(seg) > 1:
            sp = pathops.Path(); pen = sp.getPen(); pen.moveTo(seg[0]); [pen.lineTo(x) for x in seg[1:]]; pen.endPath()
            out = pathops.op(out, _stroke(sp, w), pathops.PathOp.UNION)
    return out


def _is_dot(c):
    """Chấm tròn: kích thước vừa, gần vuông, và diện tích gần bằng hình tròn nội tiếp (loại dấu phẩy)."""
    b = c.bounds
    if not b:
        return False
    w, h = b[2] - b[0], b[3] - b[1]
    if not (40 < w < 240 and abs(w - h) < .22 * max(w, h)):
        return False
    fp = _Flat(); c.draw(fp); pts = fp.contours[0] if fp.contours else []
    area = abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:]))) / 2
    return area > .7 * w * h


def them_net(f, groove=None, cham=False):
    gs = f.getGlyphSet()
    for g in f.getGlyphOrder():
        if f["glyf"][g].numberOfContours == 0:
            continue
        p = pathops.Path(); gs[g].draw(p.getPen(glyphSet=gs))
        if not list(p.contours):
            continue
        p.simplify(fix_winding=True)
        cs = list(p.contours)
        def inside(c):
            b = c.bounds
            return any(o is not c and o.bounds and o.bounds[0] <= b[0] and o.bounds[1] <= b[1] and o.bounds[2] >= b[2] and o.bounds[3] >= b[3] for o in cs)
        dots = [c for c in cs if _is_dot(c) and not inside(c)] if cham else []
        body = pathops.Path(); bp = body.getPen()
        for c in p.contours:
            if c not in dots:
                c.draw(bp)
        if groove:
            e = _eroded(body, INSET)
            if list(e.contours):
                cut = _stroke(e, GROOVE) if groove == "van" else _dashes(e)
                cut = pathops.op(cut, _eroded(body, INSET * .45), pathops.PathOp.INTERSECTION)
                body = pathops.op(body, cut, pathops.PathOp.DIFFERENCE)
        for c in dots:
            x0, y0, x1, y1 = c.bounds; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2; r = max(x1 - x0, y1 - y0) / 2 * 1.08
            ring = pathops.op(M.ellipse(cx, cy, r, r), M.ellipse(cx, cy, r * .62, r * .62), pathops.PathOp.DIFFERENCE)
            ring = pathops.op(ring, M.ellipse(cx, cy, r * .28, r * .28), pathops.PathOp.UNION)
            body = pathops.op(body, ring, pathops.PathOp.UNION)
        M.set_glyph(f, g, body)


VARIANTS = {
    "Goc": (None, False, "Bản gốc phương án 04: dấu mũ vân tay, góc mực loang"),
    "Van": ("van", False, "Thêm một đường vân lõm chạy liền bên trong mọi nét chữ"),
    "Dut": ("dut", False, "Đường vân lõm đứt quãng như vân tay thật"),
    "Cham": (None, True, "Dấu chấm (i, j, dấu nặng, dấu câu) thành vòng xoáy vân tay nhỏ"),
    "Du": ("dut", True, "Đủ cả: vân đứt trong nét chữ + chấm vân xoáy"),
    # bản đã chọn: Chấm Vân, dấu mũ thấp; hai độ đậm
    "ChamNgan": (None, True, "Chấm Vân, dấu mũ vân tay thấp – ExtraBold (tiêu đề, logo)"),
    "ChamNganVua": (None, True, "Chấm Vân, dấu mũ vân tay thấp – SemiBold (nội dung)"),
    "ChamNganThuong": (None, True, "Chấm Vân, dấu mũ vân tay thấp – Regular (văn bản dài)"),
}
WEIGHT = {"ChamNganVua": 600, "ChamNganThuong": 400}

if __name__ == "__main__":
    for name in (sys.argv[1:] or VARIANTS):
        groove, cham, _ = VARIANTS[name]
        M.dome = van_ngan if name.startswith("ChamNgan") else V.van
        files = F2.fs("baloo-2", WEIGHT.get(name, 800))
        def proc(f, groove=groove, cham=cham, name=name):
            k = V._process(f); V.mem_muc(f, 8 if WEIGHT.get(name, 800) < 600 else 10)
            if groove or cham:
                them_net(f, groove, cham)
            return k
        M.process = proc
        M.FONTS = {name: (files, f"AnTamTron{name}", "")}
        M.build(name)

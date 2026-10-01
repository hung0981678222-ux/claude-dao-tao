"""Thêm 2 kiểu hoạ tiết cho họ font An Tâm Sans (dựng từ AnTamSans-ExtraBold.ttf):
- Nét Đứt (Stitch): đường chỉ đứt quãng khoét trong lòng nét, cách mép một khoảng đều.
- Đốm Nướng (Toast): đốm cháy khoét trong lòng chữ như mặt bánh nướng.
Chạy: python3 make_font_ht.py
"""
import math
import os
import random

import pathops
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
U, D, I = pathops.PathOp.UNION, pathops.PathOp.DIFFERENCE, pathops.PathOp.INTERSECTION


def glyph_path(font, name):
    p = pathops.Path()
    font.getGlyphSet()[name].draw(p.getPen())
    return p


def erode(p, d):
    q = pathops.Path(p)
    q.stroke(2 * d, pathops.LineCap.BUTT_CAP, pathops.LineJoin.ROUND_JOIN, 4)
    q.convertConicsToQuads()
    return pathops.op(p, q, D)


def _bez(pts, t):
    while len(pts) > 1:
        pts = [((1 - t) * a[0] + t * b[0], (1 - t) * a[1] + t * b[1]) for a, b in zip(pts, pts[1:])]
    return pts[0]


def polylines(p, step=6):
    """Làm phẳng đường cong thành các đường gấp khúc khép kín."""
    rec = RecordingPen(); p.draw(rec)
    out, cur, start = [], [], None
    for op_, args in rec.value:
        if op_ == "moveTo":
            cur = [args[0]]; start = args[0]
        elif op_ == "lineTo":
            cur.append(args[0])
        elif op_ in ("qCurveTo", "curveTo"):
            p0 = cur[-1]
            if op_ == "qCurveTo" and len(args) > 2:   # nhiều điểm điều khiển: tách thành các đoạn bậc 2
                ctrl = list(args[:-1]); end = args[-1]
                segs = []
                for i in range(len(ctrl) - 1):
                    mid = ((ctrl[i][0] + ctrl[i + 1][0]) / 2, (ctrl[i][1] + ctrl[i + 1][1]) / 2)
                    segs.append((ctrl[i], mid))
                segs.append((ctrl[-1], end))
                for c, e in segs:
                    for k in range(1, step + 1):
                        cur.append(_bez([p0, c, e], k / step))
                    p0 = e
            else:
                pts = [p0] + list(args)
                for k in range(1, step + 1):
                    cur.append(_bez(pts, k / step))
        elif op_ in ("closePath", "endPath"):
            if cur and start:
                cur.append(start)
            if len(cur) > 2:
                out.append(cur)
            cur = []
    return out


def dashes(lines, dash=64, gap=40, width=20):
    res = pathops.Path()
    for pl in lines:
        segs, acc, on, cur = [], 0.0, True, [pl[0]]
        for a, b in zip(pl, pl[1:]):
            seg = math.dist(a, b)
            pos = 0.0
            while seg - pos > 1e-6:
                need = (dash if on else gap) - acc
                take = min(need, seg - pos)
                pos += take; acc += take
                t = pos / seg
                pt = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
                if on:
                    cur.append(pt)
                if acc >= (dash if on else gap) - 1e-6:
                    if on and len(cur) > 1:
                        segs.append(cur)
                    on = not on; acc = 0.0; cur = [pt]
        for s in segs:
            q = pathops.Path(); pen = q.getPen(); pen.moveTo(s[0])
            for pt in s[1:]:
                pen.lineTo(pt)
            pen.endPath()
            q.stroke(width, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
            q.convertConicsToQuads()
            res = pathops.op(res, q, U)
    return res


def ellipse(cx, cy, rx, ry, ang=0):
    k = .5523; ca, sa = math.cos(ang), math.sin(ang)
    T = lambda x, y: (cx + x * ca - y * sa, cy + x * sa + y * ca)  # noqa: E731
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo(T(rx, 0))
    pen.curveTo(T(rx, k * ry), T(k * rx, ry), T(0, ry))
    pen.curveTo(T(-k * rx, ry), T(-rx, k * ry), T(-rx, 0))
    pen.curveTo(T(-rx, -k * ry), T(-k * rx, -ry), T(0, -ry))
    pen.curveTo(T(k * rx, -ry), T(rx, -k * ry), T(rx, 0))
    pen.closePath(); return p


def stitch(p):
    inner = erode(p, 34)
    if inner.bounds is None:
        return p
    return pathops.op(p, dashes(polylines(inner)), D)


def toast(p, seed):
    area = erode(p, 30)
    if area.bounds is None:
        return p
    b = area.bounds; rnd = random.Random(seed)
    sp = pathops.Path(); y = b[1]
    row = 0
    while y < b[3]:
        x = b[0] + (52 if row % 2 else 0)
        while x < b[2]:
            if rnd.random() < .62:
                rx = rnd.uniform(16, 30)
                sp = pathops.op(sp, ellipse(x + rnd.uniform(-20, 20), y + rnd.uniform(-16, 16), rx, rx * rnd.uniform(.55, .75), rnd.uniform(0, 3.14)), U)
            x += 104
        y += 92; row += 1
    return pathops.op(p, pathops.op(sp, area, I), D)


def set_glyph(font, name, p):
    pen = TTGlyphPen(font.getGlyphSet())
    p.draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
    font["glyf"][name] = pen.glyph()


def make(kind, label, ps):
    f = TTFont(os.path.join(HERE, "AnTamSans-ExtraBold.ttf"))
    glyf = f["glyf"]
    for i, n in enumerate(f.getGlyphOrder()):
        g = glyf[n]
        if g.isComposite() or g.numberOfContours == 0:
            continue
        p = glyph_path(f, n)
        b = p.bounds
        if b is None or (b[3] - b[1]) < 400 or "comb" in n or n.startswith("uni03") or n == "circumflex":
            continue
        p = stitch(p) if kind == "stitch" else toast(p, i)
        set_glyph(f, n, p)
    for rec in f["name"].names:
        if rec.nameID in (1, 16):
            rec.string = f"An Tam Sans {label}"
        elif rec.nameID in (2, 17):
            rec.string = "Regular"
        elif rec.nameID == 4:
            rec.string = f"An Tam Sans {label}"
        elif rec.nameID == 6:
            rec.string = f"AnTamSans-{ps}"
        elif rec.nameID == 3:
            rec.string = f"AnTamSans-{ps};1.0"
    f.save(os.path.join(HERE, f"AnTamSans-{ps}.ttf"))
    f.flavor = "woff2"
    f.save(os.path.join(HERE, f"AnTamSans-{ps}.woff2"))
    print("ok", ps)


if __name__ == "__main__":
    make("stitch", "Net Dut", "NetDut")
    make("toast", "Dom Nuong", "DomNuong")

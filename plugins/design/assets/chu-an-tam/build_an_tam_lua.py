"""Chữ "AN TÂM" dải lụa và bông lúa, lấy từ logo Ẩm Thực An Tâm.

- A, N, Â, M: một dải lụa đỏ liền mạch gấp khúc, mặt trước sáng, mặt sau sẫm,
  hai đầu cắt đuôi nơ (như chữ A ruy băng của logo).
- T: bông lúa vàng trĩu hạt, cong ra hai bên (như chữ T bông lúa của logo),
  vắt qua dải lụa của chữ Â.
- Dấu mũ của Â: hai hạt lúa.

Chạy:  python3 build_an_tam_lua.py
Xuất cạnh file này: an-tam-lua.svg (nền trắng), an-tam-lua-nen-do.svg.
"""
import math
import os

import pathops
from fontTools.pens.svgPathPen import SVGPathPen

HERE = os.path.dirname(os.path.abspath(__file__))
W = 132          # bề rộng dải lụa
CAP = 700


def poly(pts):
    p = pathops.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    return p


def op(a, b, o):
    return pathops.op(a, b, o)


def clip(p, y0=0, y1=CAP):
    return op(p, poly([(-500, y0), (5000, y0), (5000, y1), (-500, y1)]), pathops.PathOp.INTERSECTION)


def _off(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    return (-dy / L * d, dx / L * d)


def _isect(p1, d1, p2, d2):
    """Giao của đường p1+t*d1 và p2+s*d2."""
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-9:
        return p2
    t = ((p2[0] - p1[0]) * d2[1] - (p2[1] - p1[1]) * d2[0]) / den
    return (p1[0] + t * d1[0], p1[1] + t * d1[1])


def ribbon(pts, w=W):
    """Tách dải lụa thành từng mặt (tứ giác) nối vát theo đường gấp."""
    h = w / 2
    n = len(pts)
    left, right = [], []
    for i in range(n):
        if i == 0 or i == n - 1:
            a, b = (pts[0], pts[1]) if i == 0 else (pts[-2], pts[-1])
            o = _off(a, b, h)
            left.append((pts[i][0] + o[0], pts[i][1] + o[1]))
            right.append((pts[i][0] - o[0], pts[i][1] - o[1]))
        else:
            a, b, c = pts[i - 1], pts[i], pts[i + 1]
            o1, o2 = _off(a, b, h), _off(b, c, h)
            d1 = (b[0] - a[0], b[1] - a[1])
            d2 = (c[0] - b[0], c[1] - b[1])
            left.append(_isect((a[0] + o1[0], a[1] + o1[1]), d1, (b[0] + o2[0], b[1] + o2[1]), d2))
            right.append(_isect((a[0] - o1[0], a[1] - o1[1]), d1, (b[0] - o2[0], b[1] - o2[1]), d2))
    faces = []
    for i in range(n - 1):
        faces.append(clip(poly([left[i], left[i + 1], right[i + 1], right[i]])))
    return faces


def notch(x, y, down=True, half=70, depth=62):
    """Đuôi nơ: khoét hình chữ V ở đầu dải."""
    if down:
        return poly([(x - half, y - 1), (x + half, y - 1), (x, y + depth)])
    return poly([(x - half, y + 1), (x + half, y + 1), (x, y - depth)])


def grain(cx, cy, length, width, angle):
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    def t(x, y):
        return (cx + x * ca - y * sa, cy + x * sa + y * ca)
    h, w = length / 2, width * 0.72
    p = pathops.Path()
    p.moveTo(*t(-h, 0))
    p.cubicTo(*t(-h * 0.4, w), *t(h * 0.5, w * 0.9), *t(h, 0))
    p.cubicTo(*t(h * 0.5, -w * 0.9), *t(-h * 0.4, -w), *t(-h, 0))
    p.close()
    return p


def band(pts, r0, r1):
    """Thân lúa: nét cong thon dần (hợp các hình tròn dọc đường)."""
    out = None
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        r = r0 + (r1 - r0) * i / (n - 1)
        k = 0.5523 * r
        c = pathops.Path()
        c.moveTo(x + r, y); c.cubicTo(x + r, y + k, x + k, y + r, x, y + r)
        c.cubicTo(x - k, y + r, x - r, y + k, x - r, y); c.cubicTo(x - r, y - k, x - k, y - r, x, y - r)
        c.cubicTo(x + k, y - r, x + r, y - k, x + r, y); c.close()
        out = c if out is None else op(out, c, pathops.PathOp.UNION)
    return out


def bez(p0, p1, p2, p3, n=30):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


def panicle(stem_top, side):
    """Nhánh bông lúa cong ra một bên, hạt mọc so le hai phía."""
    sx, sy = stem_top
    curve = bez((sx, sy), (sx + 110 * side, sy + 95), (sx + 270 * side, sy + 70), (sx + 330 * side, sy - 90), 48)
    stalk = band(curve, 16, 6)
    grains = []
    for k, i in enumerate(range(7, 49, 5)):
        x, y = curve[i]
        x0, y0 = curve[i - 2]
        ang = math.degrees(math.atan2(y - y0, x - x0))
        off = 38 if k % 2 == 0 else -38
        a = math.radians(ang + 90)
        gx, gy = x + math.cos(a) * off * 0.9, y + math.sin(a) * off * 0.9
        tilt = ang + (35 if off > 0 else -35) * side
        grains.append(grain(gx, gy, 92 - k * 3.5, 44 - k * 1.8, tilt))
    out = stalk
    for g in grains:
        out = op(out, g, pathops.PathOp.UNION)
    return out


def crossbar(pts_left, pts_right, y0, y1):
    """Thanh ngang của A: dải lụa nằm giữa hai chân, ở mặt sau."""
    def xat(a, b, y):
        return a[0] + (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1])
    l0, l1 = xat(*pts_left, y0), xat(*pts_left, y1)
    r0, r1 = xat(*pts_right, y0), xat(*pts_right, y1)
    return poly([(l0, y0), (r0, y0), (r1, y1), (l1, y1)])


def design():
    # ---- AN: một dải lụa, thân N đứng thẳng ----
    an_pts = [(70, 0), (310, CAP), (560, 0), (560, CAP), (960, 0), (960, CAP)]
    an = ribbon(an_pts)
    an[0] = op(an[0], notch(70, 0), pathops.PathOp.DIFFERENCE)
    an[-1] = op(an[-1], notch(960, CAP, down=False), pathops.PathOp.DIFFERENCE)
    bars = [crossbar(((70, 0), (310, CAP)), ((560, 0), (310, CAP)), 190, 280)]
    # ---- T: bông lúa ----
    tx = 1450
    stem = band(bez((tx, 0), (tx + 6, 220), (tx - 4, 450), (tx, 610), 30), 36, 24)
    t_parts = [stem, panicle((tx, 610), -1), panicle((tx, 610), 1)]
    # ---- ÂM: một dải lụa; chân trái Â vắt qua thân lúa ----
    x0 = tx + 30
    ax = x0 + 250
    am_pts = [(x0, 0), (ax, CAP), (x0 + 500, 0), (x0 + 500, CAP), (x0 + 700, 230), (x0 + 900, CAP), (x0 + 900, 0)]
    am = ribbon(am_pts)
    am[0] = op(am[0], notch(x0, 0), pathops.PathOp.DIFFERENCE)
    am[-1] = op(am[-1], notch(x0 + 900, 0), pathops.PathOp.DIFFERENCE)
    bars.append(crossbar(((x0, 0), (ax, CAP)), ((x0 + 500, 0), (ax, CAP)), 190, 280))
    # ---- dấu mũ: hai hạt lúa ----
    hat = [grain(ax - 46, 830, 140, 50, 52), grain(ax + 46, 830, 140, 50, 128)]
    return an, am, t_parts, hat, bars


def d(p):
    pen = SVGPathPen(None)
    p.draw(pen)
    return pen.getCommands()


def render(bg=None, front=("#F2382C", "#C8120C"), back=("#A80E0B", "#7E0C10"), gold=("#F6C24C", "#B87018")):
    an, am, t_parts, hat, bars = design()
    bs = [p.bounds for p in an + am + t_parts + hat if p.bounds]
    x0 = min(b[0] for b in bs) - 70; x1 = max(b[2] for b in bs) + 70
    y0 = min(b[1] for b in bs) - 70; y1 = max(b[3] for b in bs) + 70
    defs = [
        f'<linearGradient id="f" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{front[1]}"/><stop offset=".55" stop-color="{front[0]}"/><stop offset="1" stop-color="{front[1]}"/></linearGradient>',
        f'<linearGradient id="b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{back[0]}"/><stop offset="1" stop-color="{back[1]}"/></linearGradient>',
        f'<linearGradient id="g" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{gold[1]}"/><stop offset=".5" stop-color="{gold[0]}"/><stop offset="1" stop-color="{gold[1]}"/></linearGradient>',
    ]
    body = []
    # thứ tự vẽ: mặt sau trước, mặt trước sau; bông lúa vắt qua chữ Â
    for faces in (an, am):
        for i, f in enumerate(faces):
            if i % 2 == 1:
                body.append(f'<path d="{d(f)}" fill="url(#b)"/>')
    for bar in bars:
        body.append(f'<path d="{d(bar)}" fill="url(#b)"/>')
    for faces in (an,):
        for i, f in enumerate(faces):
            if i % 2 == 0:
                body.append(f'<path d="{d(f)}" fill="url(#f)"/>')
    # T: thân lúa sau chân trái Â, nhánh lúa trước
    body.append(f'<path d="{d(t_parts[0])}" fill="url(#g)"/>')
    for i, f in enumerate(am):
        if i % 2 == 0:
            body.append(f'<path d="{d(f)}" fill="url(#f)"/>')
    for p in t_parts[1:] + hat:
        body.append(f'<path d="{d(p)}" fill="url(#g)"/>')
    rect = f'<rect x="{x0:.0f}" y="{-y1:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {-y1:.0f} {x1 - x0:.0f} {y1 - y0:.0f}">'
            f'<defs>{"".join(defs)}</defs>{rect}<g transform="scale(1,-1)">{"".join(body)}</g></svg>\n')


if __name__ == "__main__":
    open(os.path.join(HERE, "an-tam-lua.svg"), "w").write(render())
    open(os.path.join(HERE, "an-tam-lua-nen-do.svg"), "w").write(
        render(bg="#D7150E", front=("#FFFFFF", "#F4E6DC"), back=("#E7CFC4", "#C9A89A")))
    print("ok")

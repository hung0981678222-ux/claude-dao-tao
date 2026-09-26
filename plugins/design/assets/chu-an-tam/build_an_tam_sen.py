"""Chữ "An Tâm" hướng Hoa Sen: chữ A cánh sen, nụ sen trên chữ â, đường bát/lá sen nâng đỡ.

Chạy:  python3 build_an_tam_sen.py
Xuất cạnh file này: an-tam-sen.svg (nền trắng), an-tam-sen-nen-do.svg, an-tam-sen-bieu-tuong.svg.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "fonts"))
import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from build_antam_display import poly, disc, union, diff, move, bez, ell, path, stroke

R = 46                       # nửa bề dày nét
XH, CAP = 470, 720           # chiều cao chữ thường, chữ hoa
RED, RED_TXT, GOLD, CREAM = "#D7150E", "#BE0A0E", "#E9A62E", "#FFFFFF"


def taper(pts, r0, r1, mid=None):
    """Nét thon hai đầu: r0 ở đầu, r1 ở cuối, mid ở giữa (nếu có)."""
    dense = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        for k in range(5):
            t = k / 5
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    n = len(dense) - 1
    out = []
    for i, (x, y) in enumerate(dense):
        t = i / n
        if mid is None:
            r = r0 + (r1 - r0) * t
        else:
            r = (r0 + (mid - r0) * math.sin(t * math.pi / 2) ** 0.8) if t < .5 else (r1 + (mid - r1) * math.sin((1 - t) * math.pi / 2) ** 0.8)
        out.append(disc(x, y, r))
    return union(*out)


def petal(cx, cy, length, width, angle):
    """Cánh sen: thuôn nhọn ở chóp, tròn ở gốc."""
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    def t(x, y):
        return (cx + x * ca - y * sa, cy + x * sa + y * ca)
    L, W = length, width / 2
    p = pathops.Path()
    p.moveTo(*t(0, 0))
    p.cubicTo(*t(L * 0.15, W * 1.3), *t(L * 0.65, W * 1.0), *t(L, 0))
    p.cubicTo(*t(L * 0.65, -W * 1.0), *t(L * 0.15, -W * 1.3), *t(0, 0))
    p.close()
    return p


# ---------- chữ ----------
def A_sen():
    """Chữ A cánh sen: hai nét cong kiểu vòm nhọn gặp nhau ở chóp, thanh ngang là nụ cười."""
    w = 470
    left = bez((20, R), (15, 300), (170, 560), (w / 2, CAP - 30), 24)
    right = [(w - x, y) for x, y in left]
    bar = bez((58, 262), (170, 200), (300, 200), (412, 262), 16)
    tip = petal(w / 2, CAP - 60, 120, 60, 90)
    return union(taper(left, R, R - 10), taper(right, R, R - 10), stroke(bar, R - 6), tip), w


def n_():
    arch = path([(0, R), (0, XH - 60)], bez((0, XH - 60), (30, XH + 20), (300, XH + 30), (300, 300)), [(300, 300), (300, R)])
    return stroke(arch), 300


def T_():
    bar = bez((0, CAP - 90), (140, CAP - 40), (340, CAP - 40), (480, CAP - 90), 20)
    return union(taper(bar, R - 18, R - 18, R), stroke([(240, CAP - 60), (240, R)])), 480


def a_():
    bowl = stroke(ell(165, 225, 165, 190, 0, 360, 56))
    return union(bowl, stroke([(330, XH - 30), (330, R)])), 330


def m_():
    arch1 = bez((0, XH - 60), (20, XH + 20), (260, XH + 30), (260, 300))
    arch2 = bez((260, 300), (260, XH + 30), (520, XH + 20), (520, 300))
    return union(stroke([(0, R), (0, XH - 60)]), stroke(path(arch1, [(260, 300), (260, R)])),
                 stroke(path(arch2, [(520, 300), (520, R)]))), 520


def lotus_bud(cx, y):
    """Nụ sen ba cánh: cánh giữa đứng, hai cánh bên nghiêng ra."""
    return union(petal(cx, y, 190, 92, 90), petal(cx - 10, y + 10, 150, 70, 132), petal(cx + 10, y + 10, 150, 70, 48))


def word():
    x = 0
    parts = []
    A, w = A_sen(); parts.append(move(A, x, 0)); x += w + 115
    n, w = n_(); parts.append(move(n, x, 0)); x += w + 250
    T, w = T_(); parts.append(move(T, x, 0)); tx = x; x += w + 55
    a, w = a_(); parts.append(move(a, x, 0)); ax = x; x += w + 105
    m, w = m_(); parts.append(move(m, x, 0)); x += w
    letters = union(*parts)
    bud = lotus_bud(ax + 195, XH + 95)
    width = x
    cradle = taper(bez((-120, -20), (width * 0.2, -270), (width * 0.8, -270), (width + 120, -20), 60), 6, 6, 34)
    return letters, union(bud, cradle), width


def emblem():
    """Biểu tượng nhỏ: chữ A cánh sen trong đoá sen, dùng làm tem, ảnh đại diện."""
    A, w = A_sen()
    A = move(A, -w / 2, 0)
    bud = lotus_bud(0, CAP + 20)
    cradle = taper(bez((-400, 90), (-240, -170), (240, -170), (400, 90), 40), 6, 6, 32)
    side = union(petal(-20, 30, 380, 190, 128), petal(20, 30, 380, 190, 52), petal(-40, 20, 330, 150, 160), petal(40, 20, 330, 150, 20))
    return A, union(bud, cradle), side


def d(p):
    pen = SVGPathPen(None)
    p.draw(pen)
    return pen.getCommands()


def svg(parts, pad=60, bg=None, size=None):
    bs = [p.bounds for p, _ in parts if p.bounds]
    x0 = min(b[0] for b in bs) - pad; y0 = min(b[1] for b in bs) - pad
    x1 = max(b[2] for b in bs) + pad; y1 = max(b[3] for b in bs) + pad
    if size:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        x0, x1, y0, y1 = cx - size / 2, cx + size / 2, cy - size / 2, cy + size / 2
    rect = f'<rect x="{x0:.0f}" y="{-y1:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" rx="{(x1 - x0) * .12 if size else 0:.0f}" fill="{bg}"/>' if bg else ""
    body = "".join(f'<path d="{d(p)}" fill="{c}"/>' for p, c in parts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {-y1:.0f} {x1 - x0:.0f} {y1 - y0:.0f}">'
            f'{rect}<g transform="scale(1,-1)">{body}</g></svg>\n')


if __name__ == "__main__":
    letters, gold, _ = word()
    open(os.path.join(HERE, "an-tam-sen.svg"), "w").write(svg([(gold, GOLD), (letters, RED_TXT)]))
    open(os.path.join(HERE, "an-tam-sen-nen-do.svg"), "w").write(svg([(gold, GOLD), (letters, CREAM)], bg=RED))
    A, g2, side = emblem()
    open(os.path.join(HERE, "an-tam-sen-bieu-tuong.svg"), "w").write(
        svg([(side, "#FBE3B4"), (g2, GOLD), (A, RED_TXT)], size=1200, bg="#FFFFFF"))
    print("ok")

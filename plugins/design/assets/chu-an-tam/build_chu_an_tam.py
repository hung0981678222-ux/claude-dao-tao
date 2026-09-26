"""Chữ lồng AN TÂM: bản ngang và bản con triện.

Chạy:  python3 build_chu_an_tam.py duong-ra.json
Ghi ra JSON chứa đường nét SVG (word, hat, seal); các file .svg cạnh file này
được xuất từ JSON đó.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts"))
import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from build_antam_display import poly, disc, union, diff, move, bez, path, stroke, xform

R = 62
YB, YT = R, 700 - R


def rrect(x0, y0, x1, y1, r):
    K = .5523; p = pathops.Path()
    p.moveTo(x0 + r, y0); p.lineTo(x1 - r, y0); p.cubicTo(x1 - r + r * K, y0, x1, y0 + r - r * K, x1, y0 + r)
    p.lineTo(x1, y1 - r); p.cubicTo(x1, y1 - r + r * K, x1 - r + r * K, y1, x1 - r, y1)
    p.lineTo(x0 + r, y1); p.cubicTo(x0 + r - r * K, y1, x0, y1 - r + r * K, x0, y1 - r)
    p.lineTo(x0, y0 + r); p.cubicTo(x0, y0 + r - r * K, x0 + r - r * K, y0, x0 + r, y0)
    p.close(); return p


def non_la(cx, y, s=1.0):
    """Nón lá: chóp nhọn, sườn hơi võng, vành cong."""
    p = pathops.Path()
    p.moveTo(cx - 190 * s, y + 34 * s)
    p.cubicTo(cx - 100 * s, y + 70 * s, cx - 38 * s, y + 135 * s, cx, y + 210 * s)
    p.cubicTo(cx + 38 * s, y + 135 * s, cx + 100 * s, y + 70 * s, cx + 190 * s, y + 34 * s)
    p.cubicTo(cx + 100 * s, y, cx - 100 * s, y, cx - 190 * s, y + 34 * s)
    p.close()
    return p


def taper(pts, r0, r1):
    """Nét thon dần từ r0 tới r1 (đầu đao nhọn dần)."""
    n = len(pts)
    dense = []
    for i in range(n - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        for k in range(6):
            t = k / 6
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    m = len(dense)
    return union(*[disc(x, y, r0 + (r1 - r0) * (i / (m - 1)) ** 1.4) for i, (x, y) in enumerate(dense)])


def dao_curl(p0, p1, side):
    """Đầu đao: đoạn cong vểnh lên ở cuối nét ngang, side=-1 bên trái."""
    x, y = p0
    return bez((x, y), (x + 45 * side, y), (x + 70 * side, y + 8), (x + 88 * side, y + 58), 10)


def lettering():
    # AN: A có cạnh phải đứng, dùng chung làm thân đầu của N
    ax = 380                                   # cạnh phải A = thân trái N
    a_left = [(110, 190), (ax, YT)]
    a_eave = bez((110, 190), (88, 120), (40, 62), (-40, 104), 16)
    t = (270 - 190) / (YT - 190)
    a_bar = [(110 + (ax - 110) * t, 270), (ax, 270)]
    an = union(stroke(a_left, R), taper(a_eave, R, 16), stroke([(ax, YT), (ax, YB)], R), stroke(a_bar, R),
               stroke([(ax, YT), (720, YB), (720, YT)], R))
    # TÂM: thanh T kéo dài thành mái che chữ Â; cạnh phải Â là thân trái M
    x0 = 1010
    tx = x0 + 150                               # thân T
    mx = tx + 400                               # cạnh phải Â = thân trái M
    bar = [(x0 + 60, YT), (mx, YT)]
    t_eave = bez((x0 + 60, YT), (x0 + 10, YT), (x0 - 30, YT + 10), (x0 - 60, YT + 70), 16)
    t_stem = [(tx, YT), (tx, YB)]
    a2_left = [(tx + 90, YB), (mx, YT)]
    tt = (270 - YB) / (YT - YB)
    a2_bar = [(tx + 90 + (mx - tx - 90) * tt, 270), (mx, 270)]
    m = [(mx, YT), (mx, YB)]
    m2 = [(mx, YT), (mx + 200, 250), (mx + 400, YT), (mx + 400, YB)]
    tam = union(stroke(bar, R), taper(t_eave, R, 16), stroke(t_stem, R), stroke(a2_left, R), stroke(a2_bar, R), stroke(m, R), stroke(m2, R))
    hat_cx = (tx + 90 + mx) / 2 + 40
    hat = non_la(hat_cx, 770)
    return an, tam, hat


def svg_d(p):
    pen = SVGPathPen(None); p.draw(pen); return pen.getCommands()


def seal(an, tam, hat):
    """Con triện: khung vuông đỏ, chữ khoét trắng, AN trên TÂM dưới."""
    S = 1000
    frame = rrect(0, 0, S, S, 90)
    b1 = an.bounds; b2 = union(tam, hat).bounds
    sc1 = min(700 / (b1[2] - b1[0]), 360 / (b1[3] - b1[1]))
    sc2 = min(800 / (b2[2] - b2[0]), 470 / (b2[3] - b2[1]))
    def place(p, b, sc, cx, y0):
        return xform(p, lambda q: (cx + (q[0] - (b[0] + b[2]) / 2) * sc, y0 + (q[1] - b[1]) * sc))
    top = place(an, b1, sc1, S / 2 - 15, 575)
    bot = place(union(tam, hat), b2, sc2, S / 2 + 10, 95)
    inner = diff(rrect(40, 40, S - 40, S - 40, 60), rrect(62, 62, S - 62, S - 62, 44))
    return diff(frame, top, bot, inner)


if __name__ == "__main__":
    an, tam, hat = lettering()
    word = union(an, tam)
    b = union(word, hat).bounds
    out = {"word": svg_d(word), "hat": svg_d(hat), "bounds": b, "seal": svg_d(seal(an, tam, hat))}
    json.dump(out, open(sys.argv[1], "w"))
    print(b)

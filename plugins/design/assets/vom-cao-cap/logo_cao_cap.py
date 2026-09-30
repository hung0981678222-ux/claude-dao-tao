"""Logo Ẩm Thực An Tâm, hướng Vòm cao cấp.

Chữ AN TÂM dựng hình học trên lưới cao 100 đơn vị, nét mảnh đều, khoảng chữ rộng.
Hai chữ A là mái vòm, dấu mũ của Â là nửa chiếc bánh gập đôi (tách riêng để in màu vàng).
Dòng ẨM THỰC lấy nét thật từ Be Vietnam Pro 500 (SIL OFL), chuyển thành đường vẽ.
Chạy: python3 logo_cao_cap.py  -> in JSON các đường vẽ ra stdout.
"""
import json
import os
import sys

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
K = 0.5523
H = 100.0
S = 11.0            # nét đứng
SB = S * 0.86       # nét ngang (thanh A, thanh T) mảnh hơn một chút cho cân mắt
OV = 1.6            # vòm vượt đỉnh 1,6 đơn vị (bù thị giác cho nét tròn)
TRACK = 24.0        # khoảng giữa hai chữ
SPACE = 54.0        # khoảng giữa AN và TÂM
U, D = pathops.PathOp.UNION, pathops.PathOp.DIFFERENCE


def P():
    return pathops.Path()


def poly(pts):
    p = P(); pen = p.getPen(); pen.moveTo(pts[0])
    for q in pts[1:]:
        pen.lineTo(q)
    pen.closePath(); return p


def rect(x0, y0, x1, y1):
    return poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def arch(x0, x1, ytop, ybot):
    r = (x1 - x0) / 2; cx = x0 + r; cy = ytop + r
    p = P(); pen = p.getPen()
    pen.moveTo((x0, ybot)); pen.lineTo((x0, cy))
    pen.curveTo((x0, cy - K * r), (cx - K * r, ytop), (cx, ytop))
    pen.curveTo((cx + K * r, ytop), (x1, cy - K * r), (x1, cy))
    pen.lineTo((x1, ybot)); pen.closePath(); return p


def half_moon(cx, r, ybase):
    p = P(); pen = p.getPen()
    pen.moveTo((cx - r, ybase))
    pen.curveTo((cx - r, ybase - K * r), (cx - K * r, ybase - r), (cx, ybase - r))
    pen.curveTo((cx + K * r, ybase - r), (cx + r, ybase - K * r), (cx + r, ybase))
    pen.closePath(); return p


def U_(*ps):
    out = ps[0]
    for q in ps[1:]:
        out = pathops.op(out, q, U)
    return out


def D_(a, b):
    return pathops.op(a, b, D)


# ---------- chữ ----------
def A(x, w=72):
    outer = arch(x, x + w, -OV, H)
    inner = arch(x + S, x + w - S, -OV + S * 1.04, H + 1)
    bar_y = 64
    return U_(D_(outer, inner), rect(x + S - .5, bar_y, x + w - S + .5, bar_y + SB)), w


def N(x, w=70):
    d = S * 1.22   # bề ngang đường chéo, để độ dày vuông góc ~ bằng nét đứng
    diag = poly([(x, 0), (x + d, 0), (x + w, H), (x + w - d, H)])
    return U_(rect(x, 0, x + S * .96, H), rect(x + w - S * .96, 0, x + w, H), diag), w


def T(x, w=66):
    return U_(rect(x, 0, x + w, SB), rect(x + (w - S) / 2, 0, x + (w + S) / 2, H)), w


def M(x, w=88):
    d = S * 1.18; m = x + w / 2
    l = poly([(x, 0), (x + d, 0), (m + d / 2, H * .80), (m - d / 2, H * .80)])
    r = poly([(x + w, 0), (x + w - d, 0), (m - d / 2, H * .80), (m + d / 2, H * .80)])
    return U_(rect(x, 0, x + S, H), rect(x + w - S, 0, x + w, H), l, r), w


HAT_R, HAT_GAP = 15.0, 9.0


def hat(x, w):
    return half_moon(x + w / 2, HAT_R, -OV - HAT_GAP)


def wordmark():
    letters, hats, x = [], [], 0.0
    for ch in "AN TÂM":
        if ch == " ":
            x += SPACE - TRACK; continue
        g, w = {"A": A, "Â": A, "N": N, "T": T, "M": M}[ch](x)
        if ch == "Â":
            hats.append(hat(x, w))
        letters.append(g); x += w + TRACK
    return U_(*letters), U_(*hats), x - TRACK


def mark():
    """Biểu tượng: chữ Â vòm đặt trong khung vòm nét mảnh."""
    a, w = A(0)
    return a, hat(0, w), w


# ---------- ẨM THỰC từ font thật ----------
def font_line(text, weight=500, track_em=0.42, cap_target=24.0):
    fonts = [TTFont(os.path.join(HERE, f"be-vietnam-pro/files/be-vietnam-pro-{s}-{weight}-normal.woff2"))
             for s in ("latin", "vietnamese", "latin-ext")]
    upm = fonts[0]["head"].unitsPerEm
    cap = fonts[0]["OS/2"].sCapHeight or 0.7 * upm
    sc = cap_target / cap
    out = P(); x = 0.0
    for ch in text:
        if ch == " ":
            x += upm * .28 * sc + track_em * upm * sc; continue
        for f in fonts:
            gname = f.getBestCmap().get(ord(ch))
            if gname:
                break
        gs = f.getGlyphSet()
        gp = P()
        gs[gname].draw(TransformPen(gp.getPen(), (sc, 0, 0, -sc, x, 0)))
        out = U_(out, gp) if len(list(out)) else gp
        x += f["hmtx"][gname][0] * sc + track_em * upm * sc
    x -= track_em * upm * sc
    return out, x, cap_target


def d(path):
    pen = SVGPathPen(None, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    path.draw(pen); return pen.getCommands()


def bounds(path):
    return path.bounds


if __name__ == "__main__":
    wl, wh, ww = wordmark()
    ml, mh, mw = mark()
    at, atw, atc = font_line("ẨM THỰC")
    out = {"wm": d(wl), "wm_hat": d(wh), "wm_w": ww, "wm_bounds": bounds(U_(wl, wh)),
           "mk": d(ml), "mk_hat": d(mh), "mk_w": mw,
           "amt": d(at), "amt_w": atw, "amt_bounds": bounds(at),
           "S": S, "H": H, "TRACK": TRACK, "HAT_R": HAT_R}
    json.dump(out, sys.stdout)

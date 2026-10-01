"""Chữ AN TÂM vẽ riêng, kiểu tương phản cao (dày mảnh như chữ thời trang), có chân mảnh.
- Hai chữ A là mái vòm, nét đậm dồn về bên phải như nét bút.
- Thanh ngang chữ A là đường gợn như mép bánh cuộn.
- Dấu mũ chữ Â là chiếc bánh gập đôi có đốm nướng.
Tạo lại 3 phương án bố cục (canh giữa, nhãn trên AN T, biểu tượng) với chữ mới.
"""
import json
import math
import sys

import pathops
import logo_cao_cap as L

RED, IVORY, INK, GOLD = "#A8160F", "#F6F1E8", "#1F1714", "#C39443"
H = 100.0
TK = 17.0      # nét dày
TN = 4.2       # nét mảnh
SF = 3.2       # độ dày chân chữ
OV = 1.8
U, D = pathops.PathOp.UNION, pathops.PathOp.DIFFERENCE
K = L.K


def rect(x0, y0, x1, y1):
    return L.rect(x0, y0, x1, y1)


def poly(pts):
    return L.poly(pts)


def ellipse_arch(x0, x1, ytop, ybot, cx=None):
    """Vòm nửa elip (tâm có thể lệch) + thân thẳng xuống ybot."""
    cx = (x0 + x1) / 2 if cx is None else cx
    rl, rr = cx - x0, x1 - cx
    ry = (x1 - x0) / 2
    cy = ytop + ry
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, ybot)); pen.lineTo((x0, cy))
    pen.curveTo((x0, cy - K * ry), (cx - K * rl, ytop), (cx, ytop))
    pen.curveTo((cx + K * rr, ytop), (x1, cy - K * ry), (x1, cy))
    pen.lineTo((x1, ybot)); pen.closePath()
    return p


def serif(cx, w, y, top=False):
    """Chân mảnh ngang, đầu hơi vát."""
    y0, y1 = (y, y + SF) if top else (y - SF, y)
    return rect(cx - w / 2, y0, cx + w / 2, y1)


def wave(x0, x1, y, amp=2.6, n=2, width=TN):
    p = pathops.Path(); pen = p.getPen()
    steps = 40
    pen.moveTo((x0, y))
    for i in range(1, steps + 1):
        t = i / steps
        pen.lineTo((x0 + (x1 - x0) * t, y + amp * math.sin(t * n * 2 * math.pi)))
    pen.endPath()
    p.stroke(width, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
    p.convertConicsToQuads()
    return p


def Uo(*ps):
    return L.U_(*ps)


def A(x, w=78):
    outer = ellipse_arch(x, x + w, -OV, H)
    # lòng chữ lệch trái: chân trái mảnh, chân phải dày, đỉnh vòm nét dồn sang phải
    inner = ellipse_arch(x + TN + 2.2, x + w - TK, -OV + 8.5, H + 1, cx=x + (w - TK + TN) / 2 - 3)
    a = L.D_(outer, inner)
    bar = wave(x + TN + 1, x + w - TK + 1, 64, 2.4, 1.5, TN + .4)
    a = Uo(a, bar,
           serif(x + (TN + 2.2) / 2, 18, H), serif(x + w - TK / 2, 30, H))
    return a, w


def N(x, w=74):
    l = rect(x + 3, 0, x + 3 + TN, H)
    r = rect(x + w - 3 - TN, 0, x + w - 3, H)
    dg = poly([(x + 3, 0), (x + 3 + TK + 3, 0), (x + w - 3, H), (x + w - 3 - TK - 3, H)])
    return Uo(l, r, dg, serif(x + 3 + TN / 2, 20, 0, True), serif(x + 3 + TN / 2, 20, H),
              serif(x + w - 3 - TN / 2, 20, 0, True)), w


def T(x, w=70):
    bar = rect(x, 0, x + w, TN + 1)
    st = rect(x + (w - TK) / 2, 0, x + (w + TK) / 2, H)
    beak_l = poly([(x, 0), (x + TN, 0), (x + TN + 1.5, 18), (x, 14)])
    beak_r = poly([(x + w, 0), (x + w - TN, 0), (x + w - TN - 1.5, 18), (x + w, 14)])
    return Uo(bar, st, beak_l, beak_r, serif(x + w / 2, 34, H)), w


def M(x, w=98):
    l = rect(x + 3, 0, x + 3 + TN, H)
    r = rect(x + w - 3 - TK, 0, x + w - 3, H)
    m = x + w / 2 + 2
    d1 = poly([(x + 3, 0), (x + 3 + TK + 4, 0), (m + TK / 2, H), (m - TK / 2 + 2, H)])
    d2 = poly([(x + w - 3 - TK, 0), (x + w - 3 - TK + TN + 1, 0), (m + 2, H), (m - 1, H)])
    return Uo(l, r, d1, d2, serif(x + 3 + TN / 2, 20, H), serif(x + w - 3 - TK / 2, 30, H),
              serif(x + 3 + TN / 2, 16, 0, True)), w


TRACK, SPACE = 20.0, 52.0


def tortilla_hat(cx, base, r):
    h = L.half_moon(cx, r, base)
    for dx, dy, rr in [(-.42, -.32, .13), (.18, -.6, .11), (.46, -.25, .1), (-.02, -.22, .07)]:
        h = L.D_(h, _circle(cx + dx * r, base + dy * r, rr * r))
    return h


def _circle(cx, cy, r):
    k = K * r
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((cx + r, cy))
    pen.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    pen.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    pen.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    pen.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    pen.closePath(); return p


def wordmark_paths():
    parts, x, hat_cx, xs = [], 0.0, 0, {}
    for ch in "AN TÂM":
        if ch == " ":
            x += SPACE - TRACK; continue
        g, w = {"A": A, "Â": A, "N": N, "T": T, "M": M}[ch](x)
        xs[ch] = (x, w)
        if ch == "Â":
            hat_cx = x + (w - TK + TN) / 2 + 2
        parts.append(g); x += w + TRACK
    return Uo(*parts), x - TRACK, hat_cx, xs


WL, WW, HAT_CX, XS = wordmark_paths()
HATP = tortilla_hat(HAT_CX, -11, 17)
T_RIGHT = XS["T"][0] + XS["T"][1]
WM, HATD = L.d(WL), L.d(HATP)


def text(t, cap, track, weight=500):
    p, w, _ = L.font_line(t, weight=weight, track_em=track, cap_target=cap)
    return L.d(p), w


AMT_C, AMT_CW = text("ẨM THỰC", 15, .55)
AMT_T, AMT_TW = text("ẨM THỰC", 12.5, .46, 600)
AMT_L, AMT_LW = text("ẨM THỰC", 14, .42)
DESC, DESCW = text("BÁNH TORTILLAS · DONER KEBAB", 10.5, .34)


def wm(fg, hat):
    return f'<path fill="{fg}" d="{WM}"/><path fill="{hat}" d="{HATD}"/>'


def at(dd, x, y, fill):
    return f'<path transform="translate({x:.2f} {y:.2f})" fill="{fill}" d="{dd}"/>'


def svg(vb, body, label="Ẩm Thực An Tâm"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>'


def pa1(fg, hat, rule):
    b = wm(fg, hat) + at(AMT_C, (WW - AMT_CW) / 2, -44, fg)
    y = 134
    b += at(DESC, (WW - DESCW) / 2, y, fg)
    b += f'<path d="M0,{y - 5} H{(WW - DESCW) / 2 - 16} M{(WW + DESCW) / 2 + 16},{y - 5} H{WW}" stroke="{rule}" stroke-width="1.2"/>'
    return svg(f"-6 -74 {WW + 12} 222", b)


def pa2(fg, hat, tag_bg, tag_fg):
    b = wm(fg, hat)
    b += f'<rect x="0" y="-46" width="{T_RIGHT}" height="25" rx="12.5" fill="{tag_bg}"/>'
    b += at(AMT_T, (T_RIGHT - AMT_TW) / 2, -27.5, tag_fg)
    b += at(DESC, 0, 134, fg) + f'<path d="M{DESCW + 16},129 H{WW}" stroke="{hat}" stroke-width="1.2"/>'
    return svg(f"-6 -66 {WW + 12} 214", b)


def taco_badge(bb, shell, fill, spot, line, back):
    """Khung vòm chứa chiếc taco nghiêng (khung 170 × 230)."""
    lettuce = "M38,142 " + " ".join(f"q6,{-12 if i % 2 == 0 else -8} 12,0" for i in range(8)) + " V150 H38 Z"
    s = (f'<path d="M0,230 V85 a85,85 0 0 1 170,0 V230 Z" fill="{bb}"/>'
         f'<path d="M9,221 V85 a76,76 0 0 1 152,0 V221 Z" fill="none" stroke="{line}" stroke-width="1.4"/>')
    g = f'<path d="M24,140 H146 A61,61 0 0 1 24,140 Z" fill="{back}" opacity=".62"/>'
    g += '<path d="M34,146 q51,-26 102,0 V152 H34 Z" fill="#6B3A22"/>'
    g += f'<path d="{lettuce}" fill="{fill}"/>'
    for cx, cy, r in [(54, 139, 6), (79, 135, 6.5), (104, 135, 6), (124, 140, 5)]:
        g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{spot}"/>'
    g += f'<path d="M30,148 H140 A55,55 0 0 1 30,148 Z" fill="{shell}"/>'
    for cx, cy, r in [(55, 166, 4), (80, 184, 3.2), (107, 172, 4.2), (123, 158, 2.8), (90, 160, 2.6)]:
        g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#9A5B2A" opacity=".55"/>'
    return s + f'<g transform="translate(85 138) scale(1.16) rotate(-14) translate(-85 -150)">{g}</g>'


def pa3(fg, hat, *badge):
    top, bot = -66, 138
    sc = (bot - top) / 230
    b = f'<g transform="translate(0 {top}) scale({sc:.4f})">{taco_badge(*badge)}</g>'
    x0 = 170 * sc + 36
    b += f'<g transform="translate({x0:.2f} 0)">{wm(fg, hat)}{at(AMT_L, 0, -42, fg)}{at(DESC, 0, 134, fg)}</g>'
    return svg(f"-4 {top - 6} {x0 + WW + 10:.0f} {bot - top + 12}", b)


def badge_only(*badge):
    return svg("0 0 170 230", taco_badge(*badge), "Biểu tượng Ẩm Thực An Tâm")


def a_mark(fg, hat):
    a, w = A(0)
    h = tortilla_hat((w - TK + TN) / 2 + 2, -11, 18)
    return svg(f"-22 -40 {w + 44:.0f} 152", f'<path fill="{fg}" d="{L.d(a)}"/><path fill="{hat}" d="{L.d(h)}"/>', "Biểu tượng chữ Â")


B_DO = (RED, "#E9B75A", "#7FA33A", "#E8452F", GOLD, "#F3D08A")
B_KEM = (IVORY, "#E2AE4F", "#6E9432", RED, GOLD, "#EBC67C")
OUT = {
    "pa1_kem": pa1(INK, GOLD, GOLD), "pa1_do": pa1(IVORY, GOLD, GOLD),
    "pa2_kem": pa2(INK, GOLD, RED, IVORY), "pa2_do": pa2(IVORY, GOLD, IVORY, RED),
    "pa3_kem": pa3(INK, GOLD, *B_DO), "pa3_do": pa3(IVORY, GOLD, *B_KEM),
    "badge_do": badge_only(*B_DO), "badge_kem": badge_only(*B_KEM),
    "wm_kem": svg(f"-6 -40 {WW + 12} 148", wm(INK, GOLD)), "wm_do": svg(f"-6 -40 {WW + 12} 148", wm(IVORY, GOLD)),
}

if __name__ == "__main__":
    json.dump(OUT, sys.stdout)

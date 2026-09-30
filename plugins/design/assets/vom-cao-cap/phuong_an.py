"""Ba phương án bố cục logo Ẩm Thực An Tâm, nhấn rõ ngành thực phẩm.

- Dấu mũ chữ Â là chiếc bánh tortilla gập đôi, có đốm nướng.
- Dòng mô tả BÁNH TORTILLAS · DONER KEBAB nói thẳng sản phẩm.
- Biểu tượng vòm chứa chiếc taco bốc khói.
Chạy: python3 phuong_an.py  -> in JSON các SVG.
"""
import json
import sys

import pathops
import logo_cao_cap as L

RED, IVORY, INK, GOLD = "#A8160F", "#F6F1E8", "#1F1714", "#C39443"


def circle(cx, cy, r):
    k = L.K * r
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((cx + r, cy))
    pen.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    pen.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    pen.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    pen.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    pen.closePath(); return p


def tortilla_hat(cx=346.0, base=-9.6, r=18.0):
    """Nửa chiếc bánh gập đôi, khoét ba đốm nướng."""
    h = L.half_moon(cx, r, base)
    for dx, dy, rr in [(-7, -6.5, 2.6), (4.5, -10.5, 2.3), (7.5, -4.2, 1.9)]:
        h = L.D_(h, circle(cx + dx, base + dy, rr))
    return h


WL, _, WW = L.wordmark()
HAT = tortilla_hat()
WM = L.d(WL)
HATD = L.d(HAT)


def text(t, cap, track, weight=500):
    p, w, _ = L.font_line(t, weight=weight, track_em=track, cap_target=cap)
    return L.d(p), w


AMT_C, AMT_CW = text("ẨM THỰC", 16, .5)
AMT_T, AMT_TW = text("ẨM THỰC", 13, .42, 600)
AMT_L, AMT_LW = text("ẨM THỰC", 15, .38)
DESC, DESCW = text("BÁNH TORTILLAS · DONER KEBAB", 11.5, .3)


def wm(fg, hat):
    return f'<path fill="{fg}" d="{WM}"/><path fill="{hat}" d="{HATD}"/>'


def at(d, x, y, fill):
    return f'<path transform="translate({x:.2f} {y:.2f})" fill="{fill}" d="{d}"/>'


def svg(vb, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>'


def pa1(fg, hat, rule):
    """Ẩm thực canh giữa trên đầu, mô tả dưới chân."""
    b = wm(fg, hat)
    b += at(AMT_C, (WW - AMT_CW) / 2, -42, fg)
    y = 132
    b += at(DESC, (WW - DESCW) / 2, y, fg)
    gap = 16
    b += (f'<path d="M0,{y - 5} H{(WW - DESCW) / 2 - gap} M{(WW + DESCW) / 2 + gap},{y - 5} H{WW}" '
          f'stroke="{rule}" stroke-width="1.2"/>')
    return svg(f"-4 -72 {WW + 8} 214", b, "Ẩm Thực An Tâm")


def pa2(fg, hat, tag_bg, tag_fg):
    """Nhãn ẨM THỰC đặt trên đầu chữ AN T, ngang dấu mũ."""
    t_right = 286
    b = wm(fg, hat)
    b += f'<rect x="0" y="-45" width="{t_right}" height="27" rx="13.5" fill="{tag_bg}"/>'
    b += at(AMT_T, (t_right - AMT_TW) / 2, -25, tag_fg)
    b += at(DESC, 0, 132, fg)
    b += f'<path d="M{DESCW + 16},127 H{WW}" stroke="{hat}" stroke-width="1.2"/>'
    return svg(f"-4 -64 {WW + 8} 206", b, "Ẩm Thực An Tâm")


def taco_badge(bb, shell, fill, spot, steam, back=None, meat="#6B3A22"):
    """Vòm chứa chiếc taco nghiêng (khung 170 × 230): vỏ sau, nhân thịt, rau, cà chua, vỏ trước có đốm nướng."""
    back = back or shell
    lettuce = "M38,142 " + " ".join(f"q6,{-12 if i % 2 == 0 else -8} 12,0" for i in range(8)) + " V150 H38 Z"
    s = (f'<path d="M0,230 V85 a85,85 0 0 1 170,0 V230 Z" fill="{bb}"/>'
         f'<path d="M9,221 V85 a76,76 0 0 1 152,0 V221 Z" fill="none" stroke="{steam}" stroke-width="1.4"/>')
    g = f'<path d="M24,140 H146 A61,61 0 0 1 24,140 Z" fill="{back}" opacity=".62"/>'
    g += f'<path d="M34,146 q51,-26 102,0 V152 H34 Z" fill="{meat}"/>'
    g += f'<path d="{lettuce}" fill="{fill}"/>'
    for cx, cy, r in [(54, 139, 6), (79, 135, 6.5), (104, 135, 6), (124, 140, 5)]:
        g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{spot}"/>'
    g += f'<path d="M30,148 H140 A55,55 0 0 1 30,148 Z" fill="{shell}"/>'
    for cx, cy, r in [(55, 166, 4), (80, 184, 3.2), (107, 172, 4.2), (123, 158, 2.8), (90, 160, 2.6), (66, 184, 2.2)]:
        g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#9A5B2A" opacity=".55"/>'
    s += f'<g transform="translate(85 138) scale(1.16) rotate(-14) translate(-85 -150)">{g}</g>'
    return s


def pa3(fg, hat, bb, shell, fill, spot, steam, back=None):
    """Biểu tượng taco bên trái, chữ bên phải."""
    top, bot = -64, 136
    sc = (bot - top) / 230
    b = f'<g transform="translate(0 {top}) scale({sc:.4f})">{taco_badge(bb, shell, fill, spot, steam, back)}</g>'
    x0 = 170 * sc + 34
    b += f'<g transform="translate({x0:.2f} 0)">{wm(fg, hat)}{at(AMT_L, 0, -40, fg)}{at(DESC, 0, 132, fg)}</g>'
    return svg(f"-4 {top - 6} {x0 + WW + 8:.0f} {bot - top + 12}", b, "Ẩm Thực An Tâm")


def badge_only(bb, shell, fill, spot, steam, back=None):
    return svg("0 0 170 230", taco_badge(bb, shell, fill, spot, steam, back), "Biểu tượng Ẩm Thực An Tâm")


OUT = {
    "pa1_kem": pa1(INK, GOLD, GOLD), "pa1_do": pa1(IVORY, GOLD, GOLD),
    "pa2_kem": pa2(INK, GOLD, RED, IVORY), "pa2_do": pa2(IVORY, GOLD, IVORY, RED),
    "pa3_kem": pa3(INK, GOLD, RED, "#E9B75A", "#7FA33A", "#E8452F", GOLD, "#F3D08A"),
    "pa3_do": pa3(IVORY, GOLD, IVORY, "#E2AE4F", "#6E9432", RED, GOLD, "#EBC67C"),
    "badge_do": badge_only(RED, "#E9B75A", "#7FA33A", "#E8452F", GOLD, "#F3D08A"),
    "badge_kem": badge_only(IVORY, "#E2AE4F", "#6E9432", RED, GOLD, "#EBC67C"),
}

if __name__ == "__main__":
    json.dump(OUT, sys.stdout)

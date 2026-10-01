"""Logo hướng "Nón Lá": nét đậm, cá tính Việt. Dùng font AnTam<Tên>-Non (dấu mũ là nón lá).
- bien_hieu(): chữ AN TÂM đổ bóng khối kiểu biển hiệu kẻ tay, dải băng ẨM THỰC
- an_trien(): ấn triện vuông đỏ, chữ xếp chồng
- bieu_tuong(): nón lá đội trên chiếc bánh tròn
"""
import os
import random

import logo_vom as L

HERE = os.path.dirname(os.path.abspath(__file__))
CH, CH2, KEM, HONG, BO, DEN = L.CH, L.CH2, L.KEM, L.HONG, L.BO, L.DEN


def use(name):
    L.SERIF = os.path.join(HERE, "fonts-non", f"AnTam{name}-Non.ttf"); L._fonts.cache_clear()


def _shadow(t, size, x, y, fg, sh, depth, track):
    out = ""
    for k in range(int(depth), 0, -1):
        g, w = L.text(t, size, "serif", track, x + k, y + k, sh, "middle"); out += g
    g, w = L.text(t, size, "serif", track, x, y, fg, "middle")
    return out + g, w


def non_path(cx, base, w, fill, band=None):
    """Nón lá rời (vector), đáy tại base."""
    h = w * .56; x0, x1 = cx - w / 2, cx + w / 2; top = base - h; sag = h * .07
    d = (f"M{x0:.1f},{base:.1f} C{x0 + w * .2:.1f},{base - h * .2:.1f} {cx - w * .1:.1f},{base - h * .72:.1f} {cx:.1f},{top:.1f} "
         f"C{cx + w * .1:.1f},{base - h * .72:.1f} {x1 - w * .2:.1f},{base - h * .2:.1f} {x1:.1f},{base:.1f} "
         f"C{x1 - w * .2:.1f},{base + sag:.1f} {x0 + w * .2:.1f},{base + sag:.1f} {x0:.1f},{base:.1f}Z")
    s = f'<path fill="{fill}" d="{d}"/>'
    if band:
        by = base - h * .32
        s += f'<path d="M{x0 + w * .16:.1f},{by:.1f} L{x1 - w * .16:.1f},{by:.1f}" stroke="{band}" stroke-width="{h * .07:.1f}"/>'
    return s


def bien_hieu(fg=CH, sh=CH2, bg=KEM, accent=BO, size=150):
    """Biển hiệu: khung viền kép, chữ đổ bóng khối, dải băng ẨM THỰC phía trên."""
    word, w = _shadow("AN TÂM", size, 0, 0, fg, sh, size * .06, .02)
    W = w + size * .9; H = size * 1.9
    x0, y0 = -W / 2, -size * 1.35
    frame = (f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{W:.0f}" height="{H:.0f}" rx="{size * .14:.0f}" fill="{bg}" stroke="{fg}" stroke-width="{size * .05:.1f}"/>'
             f'<rect x="{x0 + size * .1:.0f}" y="{y0 + size * .1:.0f}" width="{W - size * .2:.0f}" height="{H - size * .2:.0f}" rx="{size * .08:.0f}" fill="none" stroke="{fg}" stroke-width="{size * .015:.1f}"/>')
    rb_w = size * 2.3; rb_y = y0 - size * .2
    ribbon = (f'<path fill="{fg}" d="M{-rb_w / 2:.0f},{rb_y:.0f} h{rb_w:.0f} l{-size * .12:.0f},{size * .19:.0f} l{size * .12:.0f},{size * .19:.0f} h{-rb_w:.0f} l{size * .12:.0f},{-size * .19:.0f}Z"/>')
    tg, _ = L.text("ẨM THỰC", size * .22, "sans", .3, 0, rb_y + size * .28, bg, "middle")
    sub, _ = L.text("SẢN PHẨM TẬN TÂM", size * .15, "sans", .34, 0, y0 + H - size * .28, fg, "middle")
    dots = "".join(f'<circle cx="{sx * (W / 2 - size * .3):.0f}" cy="{y0 + H - size * .33:.0f}" r="{size * .035:.1f}" fill="{accent}"/>' for sx in (-1, 1))
    return L.svg((x0 - 20, rb_y - 20, W + 40, H + (y0 - rb_y) + 40), frame + ribbon + tg + word + sub + dots, "Biển hiệu Ẩm Thực An Tâm")


def an_trien(fg=CH, ink=KEM, size=100):
    """Ấn triện vuông: nền đỏ, mép hơi sần như dấu son, chữ AN / TÂM xếp chồng."""
    r = random.Random(7); S = size * 3
    pts = []
    for i in range(4):
        for k in range(12):
            t = k / 12
            x, y = [(t, 0), (1, t), (1 - t, 1), (0, 1 - t)][i]
            pts.append((x * S + r.uniform(-2, 2), y * S + r.uniform(-2, 2)))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"
    _, wt = L.text("TÂM", 100, "serif", .02)
    fs = min(size * 1.08, S * .74 / wt * 100)
    a, wa = L.text("AN", fs, "serif", .02, S / 2, S * .44, ink, "middle")
    b, wb = L.text("TÂM", fs, "serif", .02, S / 2, S * .86, ink, "middle")
    border = f'<rect x="{S * .06:.0f}" y="{S * .06:.0f}" width="{S * .88:.0f}" height="{S * .88:.0f}" fill="none" stroke="{ink}" stroke-width="{S * .015:.1f}"/>'
    return L.svg((-10, -10, S + 20, S + 20), f'<path fill="{fg}" d="{d}"/>' + border + a + b, "Ấn triện An Tâm")


def bieu_tuong(fg=CH, banh=BO, bg=KEM, dom="#C9832F"):
    """Nón lá trước chiếc bánh tortilla tròn (như mặt trời sau nón); đốm nướng quanh mép bánh."""
    import math
    s = f'<circle cx="100" cy="100" r="100" fill="{bg}"/><circle cx="100" cy="92" r="62" fill="{banh}"/>'
    for k in range(14):
        a = k / 14 * 6.283 + .2; d = 50 + (k % 3) * 3
        s += f'<ellipse cx="{100 + d * math.cos(a):.1f}" cy="{92 + d * math.sin(a):.1f}" rx="4" ry="2.4" transform="rotate({math.degrees(a) + 90:.0f} {100 + d * math.cos(a):.1f} {92 + d * math.sin(a):.1f})" fill="{dom}" opacity=".75"/>'
    s += non_path(100, 150, 168, fg, band=bg)
    return L.svg((0, 0, 200, 200), s, "Biểu tượng nón lá An Tâm")


def ngang(fg=CH, sh=CH2, sub=None, bg=None, size=120):
    """Bản ngang: biểu tượng trái, chữ đổ bóng phải."""
    sub = sub or fg
    ic = bieu_tuong(CH, BO, KEM); inner = ic[ic.index(">") + 1:ic.rindex("</svg>")]
    S = size * 1.75
    icon = f'<g transform="translate(0 {-S * .82:.0f}) scale({S / 200:.3f})">{inner}</g>'
    word, w = _shadow("AN TÂM", size, 0, 0, fg, sh, size * .05, .02)
    gx = S + size * .25
    tg, tw = L.text("ẨM THỰC · SẢN PHẨM TẬN TÂM", size * .15, "sans", .24, gx, size * .36, sub)
    body = icon + f'<g transform="translate({gx + w / 2:.0f} 0)">{word}</g>' + tg
    return L.svg((-10, -S * .86, gx + max(w, tw) + 30, S * 1.12), body, "Logo ngang An Tâm", bg)

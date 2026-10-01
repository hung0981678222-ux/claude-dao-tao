"""Hướng "Tranh Mộc": vẽ tay, ấm, truyền thống Việt, nét đậm.
Cảm hứng: tranh khắc gỗ Đông Hồ (nét viền nâu mực, mảng màu in lệch nhẹ, giấy dó) và mặt trời trống đồng
— chiếc bánh tortilla tròn là mặt trời ở giữa, quanh là tia sáng và vòng hoa văn.
"""
import math
import os
import random

import logo_vom as L

HERE = os.path.dirname(os.path.abspath(__file__))
DO, DO2, KEM, BO, MUC, GIAY, LA = "#B5121B", "#7D0A10", "#FFF4E8", "#FFD37A", "#3B1E10", "#F6EBD5", "#4E7A3A"
VANG = "#F2C46B"
HAND = os.path.join(HERE, "fonts-hand", "shantell-sans-800.ttf")
HAND_M = os.path.join(HERE, "fonts-hand", "shantell-sans-500.ttf")


def use(path=HAND):
    L.SERIF = path; L._fonts.cache_clear()


def defs(uid, scale=3.2):
    """Bộ lọc làm mép rung như nét khắc gỗ."""
    return (f'<defs><filter id="{uid}w" x="-5%" y="-5%" width="110%" height="110%">'
            f'<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4"/>'
            f'<feDisplacementMap in="SourceGraphic" scale="{scale}" xChannelSelector="R" yChannelSelector="G"/></filter></defs>')


from functools import lru_cache

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


@lru_cache(None)
def _font(path):
    f = TTFont(path); return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm


@lru_cache(None)
def _clean(path, ch):
    """Đường viền chữ đã gộp các nét chồng (để vẽ viền mực không bị lộ nét bên trong)."""
    f, gs, cm, upm = _font(path); n = cm.get(ord(ch))
    if not n:
        return "", 0
    p = pathops.Path(); gs[n].draw(p.getPen(glyphSet=gs)); p.simplify(fix_winding=True)
    pen = SVGPathPen(None); p.draw(pen)
    return pen.getCommands(), f["hmtx"][n][0]


def clean_text(t, size, x=0, y=0, anchor="middle", track=0.0, path=HAND):
    f, gs, cm, upm = _font(path); s = size / upm; cx = 0; parts = []
    for ch in t:
        d, adv = _clean(path, ch)
        if d:
            parts.append(f'<path transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        cx += adv * s + size * track
    w = cx - size * track
    ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    return f'transform="translate({x + ox:.1f} {y:.1f})"', "".join(parts), w


def ink_text(t, size, fill, ink, x=0, y=0, anchor="middle", track=0.0, off=(2.2, 2), sw=None, path=HAND):
    """Chữ kiểu in khắc gỗ: viền nâu mực dày + mảng màu in lệch nhẹ."""
    tr, parts, w = clean_text(t, size, x, y, anchor, track, path)
    sw = sw or size * .045
    stroke_parts = parts.replace("<path ", '<path vector-effect="non-scaling-stroke" ')
    return (f'<g {tr} fill="{ink}" stroke="{ink}" stroke-width="{sw:.1f}" stroke-linejoin="round">{stroke_parts}</g>'
            f'<g transform="translate({off[0] - sw * .25:.1f} {off[1] - sw * .25:.1f})"><g {tr} fill="{fill}">{parts}</g></g>'), w


def sun(cx, cy, R, uid, banh=VANG, ray=DO, ink=MUC, rays=14, spots=True):
    """Mặt trời trống đồng: đĩa bánh ở giữa, tia nhọn, vòng chấm, vòng viền."""
    r0 = R * .42
    s = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{GIAY}" stroke="{ink}" stroke-width="{R * .035:.1f}"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{R * .86:.1f}" fill="none" stroke="{ink}" stroke-width="{R * .018:.1f}"/>'
    # vòng chấm
    n = 28
    for k in range(n):
        a = k / n * 2 * math.pi
        s += f'<circle cx="{cx + R * .93 * math.cos(a):.1f}" cy="{cy + R * .93 * math.sin(a):.1f}" r="{R * .026:.1f}" fill="{ink}"/>'
    # tia
    for k in range(rays):
        a = k / rays * 2 * math.pi - math.pi / 2; da = math.pi / rays * .78
        p1 = (cx + r0 * .96 * math.cos(a - da), cy + r0 * .96 * math.sin(a - da))
        p2 = (cx + R * .8 * math.cos(a), cy + R * .8 * math.sin(a))
        p3 = (cx + r0 * .96 * math.cos(a + da), cy + r0 * .96 * math.sin(a + da))
        s += f'<path d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} L{p3[0]:.1f},{p3[1]:.1f} Z" fill="{ray}" stroke="{ink}" stroke-width="{R * .016:.1f}" stroke-linejoin="round"/>'
        # vạch lông chim giữa hai tia
        b = a + math.pi / rays
        for j in (0.6, 0.7):
            q1 = (cx + R * j * math.cos(b - .05), cy + R * j * math.sin(b - .05)); q2 = (cx + R * (j + .07) * math.cos(b), cy + R * (j + .07) * math.sin(b)); q3 = (cx + R * j * math.cos(b + .05), cy + R * j * math.sin(b + .05))
            s += f'<path d="M{q1[0]:.1f},{q1[1]:.1f} L{q2[0]:.1f},{q2[1]:.1f} L{q3[0]:.1f},{q3[1]:.1f}" fill="none" stroke="{ink}" stroke-width="{R * .012:.1f}" stroke-linecap="round"/>'
    # đĩa bánh
    s += f'<circle cx="{cx}" cy="{cy}" r="{r0:.1f}" fill="{banh}" stroke="{ink}" stroke-width="{R * .03:.1f}"/>'
    if spots:
        rr = random.Random(11)
        for _ in range(16):
            a = rr.uniform(0, 2 * math.pi); d = math.sqrt(rr.uniform(.04, 1)) * r0 * .78
            x, y = cx + d * math.cos(a), cy + d * math.sin(a)
            s += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r0 * rr.uniform(.05, .09):.1f}" ry="{r0 * rr.uniform(.03, .05):.1f}" transform="rotate({rr.randint(0, 180)} {x:.1f} {y:.1f})" fill="#B5652A" opacity=".85"/>'
    return f'<g filter="url(#{uid}w)">{s}</g>'


def emblem(uid="e", ring=DO, ink=MUC, txt=KEM):
    """Huy hiệu tròn: vòng chữ ẨM THỰC AN TÂM · SẢN PHẨM TẬN TÂM bao quanh mặt trời bánh."""
    use(HAND)
    cx = cy = 250
    s = defs(uid)
    s += f'<g filter="url(#{uid}w)"><circle cx="{cx}" cy="{cy}" r="240" fill="{ring}" stroke="{ink}" stroke-width="9"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="226" fill="none" stroke="{txt}" stroke-width="2.5" stroke-dasharray="2 9" stroke-linecap="round"/></g>'
    s += L._ring_text("ẨM THỰC AN TÂM", 38, cx, cy, 186, txt, -90, key="serif", track=.12)
    s += L._ring_bottom("SẢN PHẨM TẬN TÂM", 30, cx, cy, 188, txt, key="serif", track=.12)
    for a in (180, 0):
        x = cx + 192 * math.cos(math.radians(a))
        s += f'<path d="M{x:.0f},{cy - 13} L{x + 9:.0f},{cy} L{x:.0f},{cy + 13} L{x - 9:.0f},{cy} Z" fill="{BO}" stroke="{ink}" stroke-width="2"/>'
    s += sun(cx, cy, 150, uid)
    return L.svg((0, 0, 500, 500), s, "Huy hiệu Ẩm Thực An Tâm")


def may(x, y, w, ink=MUC, fill=None):
    """Cụm mây cuộn (hoạ tiết dân gian)."""
    k = w / 100
    d = (f"M{x},{y} c{8 * k:.1f},{-18 * k:.1f} {30 * k:.1f},{-18 * k:.1f} {34 * k:.1f},{-2 * k:.1f} "
         f"c{6 * k:.1f},{-16 * k:.1f} {30 * k:.1f},{-16 * k:.1f} {32 * k:.1f},{2 * k:.1f} "
         f"c{14 * k:.1f},{-8 * k:.1f} {30 * k:.1f},{4 * k:.1f} {24 * k:.1f},{16 * k:.1f} "
         f"c{-4 * k:.1f},{7 * k:.1f} {-14 * k:.1f},{8 * k:.1f} {-20 * k:.1f},{2 * k:.1f}")
    spiral = f'<path d="M{x + 40 * k:.1f},{y - 4 * k:.1f} a{6 * k:.1f},{6 * k:.1f} 0 1 1 {8 * k:.1f},{4 * k:.1f}" fill="none" stroke="{ink}" stroke-width="{3 * k:.1f}" stroke-linecap="round"/>'
    return f'<path d="{d}" fill="{fill or "none"}" stroke="{ink}" stroke-width="{3.4 * k:.1f}" stroke-linecap="round" stroke-linejoin="round"/>' + spiral


def logo_chinh(uid="c", bg=None, fg=DO, ink=MUC, sub=MUC):
    """Logo chính bản đứng: mặt trời bánh phía trên, chữ An Tâm khắc gỗ, dòng ẨM THỰC · TẬN TÂM."""
    s = defs(uid, 2.4)
    s += f'<g transform="translate(310 -250) scale(.36)">{sun(250, 250, 240, uid)}</g>'
    w1, w = ink_text("An Tâm", 150, fg, ink, 400, 60, "middle")
    use(HAND_M)
    tg, tw = L.text("ẨM THỰC  ·  TẬN TÂM", 30, "serif", .22, 400, 122, sub, "middle")
    lines = f'<g filter="url(#{uid}w)"><path d="M{400 - tw / 2 - 70:.0f},112 h52 M{400 + tw / 2 + 18:.0f},112 h52" stroke="{ink}" stroke-width="4" stroke-linecap="round"/></g>'
    return L.svg((400 - max(w, tw) / 2 - 60, -260, max(w, tw) + 120, 410), s + w1 + tg + lines, "Logo Ẩm Thực An Tâm", bg)


def logo_ngang(uid="h", bg=None, fg=DO, ink=MUC, sub=MUC):
    """Bản ngang: huy hiệu mặt trời bánh trái, chữ phải."""
    s = defs(uid, 2.4)
    s += f'<g transform="translate(0 -20) scale(.5)">{sun(250, 250, 240, uid)}</g>'
    w1, w = ink_text("An Tâm", 150, fg, ink, 280, 170, "start")
    use(HAND_M)
    tg, tw = L.text("ẨM THỰC · SẢN PHẨM TẬN TÂM", 26, "serif", .16, 284, 222, sub)
    return L.svg((-10, -30, 300 + max(w, tw) + 20, 280), s + w1 + tg, "Logo ngang Ẩm Thực An Tâm", bg)

"""Hướng "Nét Tâm": thư pháp chữ Việt, màu đỏ son chủ đạo.
- Vòng tròn nét bút (chiếc bánh tròn, sự trọn vẹn) viết một nét, đầu đậm đuôi khô.
- Chữ "An Tâm" bút lông (dựng từ Charm, SIL OFL) có mép xơ như mực trên giấy dó.
- Con dấu son vuông, như triện ký tên dưới bức thư pháp.
"""
import math
import os
import random
from functools import lru_cache

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
DO, DO2, MUC, GIAY, VANG, KEM = "#C8102E", "#8E0B20", "#1E1412", "#FBF4EA", "#D4A04C", "#FFF8EE"
F = {"brush": os.path.join(HERE, "fonts-thu", "charm-700.ttf"), "brush-r": os.path.join(HERE, "fonts-thu", "charm-400.ttf"),
     "sans": os.path.join(HERE, "fonts-bv", "BeVietnamPro-600.ttf"), "sans-b": os.path.join(HERE, "fonts-bv", "BeVietnamPro-800.ttf")}


@lru_cache(None)
def _f(k):
    f = TTFont(F[k]); return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm


def text(t, size, k="brush", x=0, y=0, fill=DO, anchor="start", track=0.0):
    f, gs, cm, upm = _f(k); s = size / upm; cx = 0; parts = []
    for ch in t:
        n = cm.get(ord(ch))
        if not n:
            continue
        pen = SVGPathPen(gs); gs[n].draw(pen); d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        cx += f["hmtx"][n][0] * s + size * track
    w = cx - size * track; ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    return f'<g fill="{fill}" transform="translate({x + ox:.1f} {y:.1f})">{"".join(parts)}</g>', w


def defs(uid, rough=2.2, dry=True):
    """Bộ lọc mực: mép xơ (rung nhẹ) + lốm đốm khô như bút lông trên giấy."""
    holes = (f'<feTurbulence type="fractalNoise" baseFrequency="0.35 0.12" numOctaves="2" seed="3" result="n"/>'
             f'<feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -9 7.3" result="m"/>'
             f'<feComposite in="d" in2="m" operator="in"/>') if dry else ""
    return (f'<defs><filter id="{uid}" x="-10%" y="-10%" width="120%" height="120%">'
            f'<feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="3" seed="8" result="t"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="t" scale="{rough}" xChannelSelector="R" yChannelSelector="G" result="d"/>{holes}</filter></defs>')


def enso(cx, cy, R, w, fill, seed=2, start=-60, sweep=318):
    """Vòng tròn một nét bút: nhiều sợi lông chồng lên nhau, đầu đậm, đuôi mảnh và khô."""
    r = random.Random(seed); out = []
    n = 26
    for i in range(n):
        off = (i / (n - 1) - .5) * w
        a0 = start + r.uniform(-3, 5); sw = sweep * r.uniform(.84, 1.0) * (1 - abs(off) / w * .35)
        pts = []
        steps = 90
        for k in range(steps + 1):
            t = k / steps; a = math.radians(a0 + sw * t)
            rr = R + off * (1 - t * .55) + math.sin(t * 9 + i) * w * .015
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        sw_px = w / n * r.uniform(2.2, 3.2)
        out.append(f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{sw_px:.2f}" stroke-linecap="round" opacity="{r.uniform(.9, 1):.2f}"/>')
    # đầu nét đậm (chỗ đặt bút)
    a = math.radians(start); out.append(f'<ellipse cx="{cx + R * math.cos(a):.1f}" cy="{cy + R * math.sin(a):.1f}" rx="{w * .62:.1f}" ry="{w * .48:.1f}" transform="rotate({start + 90} {cx + R * math.cos(a):.1f} {cy + R * math.sin(a):.1f})" fill="{fill}"/>')
    return "".join(out)


def seal(x, y, s, fill=DO, ink=KEM, lines=("AN", "TÂM"), uid="sl"):
    """Con dấu son vuông, mép sần, chữ xếp hai dòng."""
    r = random.Random(4); pts = []
    for i in range(4):
        for k in range(10):
            t = k / 10; px, py = [(t, 0), (1, t), (1 - t, 1), (0, 1 - t)][i]
            pts.append((x + px * s + r.uniform(-s * .012, s * .012), y + py * s + r.uniform(-s * .012, s * .012)))
    d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts) + "Z"
    g = f'<path d="{d}" fill="{fill}"/><rect x="{x + s * .08:.1f}" y="{y + s * .08:.1f}" width="{s * .84:.1f}" height="{s * .84:.1f}" fill="none" stroke="{ink}" stroke-width="{s * .03:.1f}"/>'
    fs = s * .3
    for j, t in enumerate(lines):
        tg, w = text(t, fs, "sans-b", x + s / 2, y + s * (.47 + j * .33), ink, "middle", .02)
        g += tg
    return f'<g filter="url(#{uid})">{g}</g>'


def svg(vb, body, label, bg=None):
    x, y, w, h = vb
    r = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.0f} {y:.0f} {w:.0f} {h:.0f}" role="img" aria-label="{label}">{r}{body}</svg>'


def logo(uid="lg", circle=DO, word=DO, sub=MUC, seal_fill=DO, seal_ink=KEM, bg=None):
    """Logo chính: vòng tròn nét bút, giữa là chữ Tâm lớn, trên nhỏ 'An', góc con dấu, dưới ẨM THỰC."""
    s = defs(uid) + defs(uid + "s", 1.4, False)
    s += f'<g filter="url(#{uid})">{enso(300, 300, 225, 46, circle)}</g>'
    an, wa = text("An", 92, "brush", 300, 228, word, "middle")
    tam, wt = text("Tâm", 210, "brush", 300, 400, word, "middle")
    s += f'<g filter="url(#{uid})">{an}{tam}</g>'
    s += seal(438, 418, 74, seal_fill, seal_ink, uid=uid + "s")
    tg, tw = text("ẨM THỰC AN TÂM", 26, "sans-b", 300, 600, sub, "middle", .34)
    sl, _ = text("Sản Phẩm Tận Tâm · Phát Triển Xứng Tầm", 19, "sans", 300, 636, sub, "middle", .04)
    return svg((40, 40, 520, 620), s + tg + sl, "Logo Ẩm Thực An Tâm", bg)


def logo_ngang(uid="ln", fg=DO, sub=MUC, bg=None, seal_ink=KEM):
    """Bản ngang: vòng nét bút ôm con dấu son, bên phải chữ Ẩm Thực / An Tâm."""
    s = defs(uid) + defs(uid + "s", 1.4, False)
    s += f'<g filter="url(#{uid})">{enso(120, 130, 92, 22, fg)}</g>'
    s += seal(80, 90, 80, fg, seal_ink, uid=uid + "s")
    t1, w1 = text("Ẩm Thực", 54, "brush", 250, 88, fg)
    t2, w2 = text("An Tâm", 120, "brush", 244, 196, fg)
    s += f'<g filter="url(#{uid})">{t1}{t2}</g>'
    tg, tw = text("SẢN PHẨM TẬN TÂM · PHÁT TRIỂN XỨNG TẦM", 15, "sans-b", 250, 236, sub, track=.18)
    W = 250 + max(w1, w2, tw) + 30
    return svg((10, 10, W, 250), s + tg, "Logo ngang Ẩm Thực An Tâm", bg)


def bieu_tuong(uid="bt", fg=DO, bg=GIAY, inner=None):
    s = defs(uid) + f'<rect width="400" height="400" rx="80" fill="{bg}"/>'
    s += f'<g filter="url(#{uid})">{enso(200, 200, 140, 32, fg)}</g>'
    t, _ = text("Tâm", 150, "brush", 200, 250, inner or fg, "middle")
    return svg((0, 0, 400, 400), s + f'<g filter="url(#{uid})">{t}</g>', "Biểu tượng chữ Tâm")

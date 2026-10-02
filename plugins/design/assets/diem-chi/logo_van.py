"""Hướng "Điểm Chỉ": dấu vân tay son đỏ – lời cam kết của người làm bánh.
Font thương hiệu An Tâm Vân (dựng từ Be Vietnam Pro, SIL OFL): dấu mũ là ba đường vân, góc chữ bo như mực son loang.
"""
import math
import os
import random
from functools import lru_cache

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
DO, DO2, SON, KEM, GIAY, MUC, NGO = "#D2141E", "#8F0D14", "#E2332B", "#FFF6EA", "#F6EEE2", "#231716", "#F5B82E"
F = {"xb": os.path.join(HERE, "fonts-van", "AnTamVan-ExtraBold.ttf"), "md": os.path.join(HERE, "fonts-van", "AnTamVan-Medium.ttf")}


@lru_cache(None)
def _f(k):
    f = TTFont(F[k]); return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm


def text(t, size, k="xb", x=0, y=0, fill=DO, anchor="start", track=0.0):
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


def van_tay(cx, cy, r, fill=DO, seed=5, rings=11, sw=None, aspect=1.22):
    """Dấu vân tay dạng xoáy: các vòng vân lượn sóng đồng pha, vài chỗ đứt, lõi vòng nhỏ, đuôi vân phía dưới."""
    rr = random.Random(seed); sw = sw or r * .052; out = []
    ph = [rr.uniform(0, 6.28) for _ in range(3)]
    for i in range(1, rings + 1):
        rad = r * (i + .2) / (rings + .2)
        pts = []
        N = 120
        for k in range(N + 1):
            a = k / N * 2 * math.pi
            wob = 1 + .045 * math.sin(3 * a + ph[0]) + .03 * math.sin(5 * a + ph[1] + i * .25) + .02 * math.sin(2 * a + ph[2])
            x = cx + rad * wob * math.cos(a)
            y = cy + rad * wob * math.sin(a) * aspect - r * .08 * (1 - i / rings)
            pts.append((x, y))
        # một chỗ đứt cho mỗi vòng (vân thật không khép kín)
        g0 = rr.randint(0, N - 1); gl = rr.randint(4, 12) if i > 1 else 0
        seg = [pts[(g0 + gl + j) % (N + 1)] for j in range(N - gl)]
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in seg)
        out.append(f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')
    clip = f'<ellipse cx="{cx}" cy="{cy}" rx="{r * 1.02:.1f}" ry="{r * aspect * 1.02:.1f}"/>'
    cid = f"vt{abs(hash((cx, cy, r, seed))) % 99999}"
    return f'<clipPath id="{cid}">{clip}</clipPath><g clip-path="url(#{cid})">{"".join(out)}</g>'


def svg(vb, body, label, bg=None):
    x, y, w, h = vb
    r = f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.0f} {y:.0f} {w:.0f} {h:.0f}" role="img" aria-label="{label}">{r}{body}</svg>'


def logo_ngang(fg=DO, sub=MUC, bg=None, mark=None):
    m = van_tay(110, 128, 88, mark or fg)
    t0, _ = text("ẨM THỰC", 24, "xb", 232, 70, sub, track=.32)
    t1, w1 = text("An Tâm", 118, "xb", 226, 176, fg, track=-.02)
    t2, w2 = text("Sản Phẩm Tận Tâm · Phát Triển Xứng Tầm", 17, "md", 232, 214, sub, track=.02)
    return svg((10, 10, 232 + max(w1, w2) + 30, 230), m + t0 + t1 + t2, "Logo ngang Ẩm Thực An Tâm", bg)


def logo_dung(fg=DO, sub=MUC, bg=None, mark=None):
    m = van_tay(0, -215, 86, mark or fg)
    t0, _ = text("ẨM THỰC", 22, "xb", 0, -66, sub, "middle", .34)
    t1, w1 = text("An Tâm", 124, "xb", 0, 72, fg, "middle", -.02)
    t2, w2 = text("Sản Phẩm Tận Tâm · Phát Triển Xứng Tầm", 17, "md", 0, 112, sub, "middle", .02)
    W = max(w1, w2) + 60
    return svg((-W / 2, -335, W, 465), m + t0 + t1 + t2, "Logo đứng Ẩm Thực An Tâm", bg)


def con_dau(fg=DO, ink=KEM):
    """Dấu tròn: vân tay giữa, chữ chạy vòng."""
    import logo_vom as L
    L.SERIF = F["xb"]; L._fonts.cache_clear()
    s = f'<circle cx="200" cy="200" r="196" fill="{fg}"/><circle cx="200" cy="200" r="182" fill="none" stroke="{ink}" stroke-width="3"/>'
    s += L._ring_text("ẨM THỰC AN TÂM", 30, 200, 200, 154, ink, -90, key="serif", track=.14)
    s += L._ring_bottom("CAM KẾT TỪ TÂM", 26, 200, 200, 156, ink, key="serif", track=.16)
    s += f'<circle cx="200" cy="200" r="116" fill="{ink}"/>' + van_tay(200, 200, 84, fg, aspect=1.12)
    return svg((0, 0, 400, 400), s, "Dấu An Tâm")


def bieu_tuong(fg=DO, bg=KEM):
    return svg((0, 0, 300, 300), f'<rect width="300" height="300" rx="60" fill="{bg}"/>' + van_tay(150, 150, 96, fg, aspect=1.15), "Biểu tượng vân tay An Tâm")

"""Logo hướng "Vòm Lò" (Tin cậy · Tinh tế · Ấm áp), giữ bảng màu cũ.
Biểu tượng: vòm lò nướng mảnh + hạt than hồng — chính là dấu mũ của font An Tâm Serif.
Mọi chữ được dựng thành nét (outline) để in ấn không cần cài font.
"""
import math
import os
from functools import lru_cache

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
CH, CH2, KEM, HONG, BO, DEN = "#B5121B", "#7D0A10", "#FFF4E8", "#F7CFC6", "#FFD37A", "#1B1B1B"
SERIF = os.path.join(HERE, "fonts-serif", "AnTamSerif-SemiBold.ttf")
SERIF_R = os.path.join(HERE, "fonts-serif", "AnTamSerif-Regular.ttf")
BV = [os.path.join(HERE, "be-vietnam-pro", "files", f"be-vietnam-pro-{s}-600-normal.woff2") for s in ("latin", "vietnamese")]


@lru_cache(None)
def _fonts(key):
    paths = {"serif": [SERIF], "serif-r": [SERIF_R], "sans": BV}[key]
    return [TTFont(p) for p in paths]


def _glyph(key, ch):
    for f in _fonts(key):
        n = f.getBestCmap().get(ord(ch))
        if n:
            gs = f.getGlyphSet(); pen = SVGPathPen(gs); gs[n].draw(pen)
            return pen.getCommands(), f["hmtx"][n][0], f["head"].unitsPerEm, f
    return "", 0, 1000, None


def text(t, size, key="serif", track=0.0, x=0, y=0, fill=DEN, anchor="start"):
    """Chữ dựng nét. size = cỡ chữ (em) tính bằng px; y = đường chân chữ."""
    parts = []; cx = 0
    for ch in t:
        d, adv, upm, _ = _glyph(key, ch); s = size / upm
        if d:
            parts.append(f'<path transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        cx += adv * s + size * track
    w = cx - size * track
    ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    return f'<g fill="{fill}" transform="translate({x + ox:.1f} {y:.1f})">{"".join(parts)}</g>', w


def ember_pos(t, size, key="serif", track=0.0):
    """Vị trí (x, y, r) các hạt than trong chữ có dấu mũ, so với gốc chữ (0, chân chữ)."""
    out = []; cx = 0
    for ch in t:
        d, adv, upm, f = _glyph(key, ch); s = size / upm
        if f is not None and ch in "âêôÂÊÔấầẩẫậếềểễệốồổỗộẤẦẨẪẬẾỀỂỄỆỐỒỔỖỘ":
            gs = f.getGlyphSet(); p = pathops.Path(); gs[f.getBestCmap()[ord(ch)]].draw(p.getPen(glyphSet=gs))
            dots = [c.bounds for c in p.contours if c.bounds and abs((c.bounds[2] - c.bounds[0]) - (c.bounds[3] - c.bounds[1])) < 3 and c.bounds[1] > upm * .3]
            if dots:
                b = min(dots, key=lambda b: b[2] - b[0])
                out.append((cx + (b[0] + b[2]) / 2 * s, -(b[1] + b[3]) / 2 * s, (b[2] - b[0]) / 2 * s))
        cx += adv * s + size * track
    return out


def wordmark_text(t, size, fill, ember, x=0, y=0, key="serif", track=0.0, anchor="start"):
    """Chữ dựng nét + tô màu hạt than."""
    g, w = text(t, size, key, track, x, y, fill, anchor)
    ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    dots = "".join(f'<circle cx="{x + ox + ex:.1f}" cy="{y + ey:.1f}" r="{r * 1.08:.1f}" fill="{ember}"/>' for ex, ey, r in ember_pos(t, size, key, track)) if ember else ""
    return g + dots, w


def arch(cx, base, w, fill, ember, t=None):
    """Biểu tượng vòm lò: nửa vòng cung đáy phẳng + hạt than."""
    t = t or w * .13; h = w * .5; r = t * .62; k = .5523
    def half(x0, x1, hh):
        c = (x0 + x1) / 2; rx = (x1 - x0) / 2
        return (f"M{x0:.1f},{base:.1f} C{x0:.1f},{base - k * hh:.1f} {c - k * rx:.1f},{base - hh:.1f} {c:.1f},{base - hh:.1f} "
                f"C{c + k * rx:.1f},{base - hh:.1f} {x1:.1f},{base - k * hh:.1f} {x1:.1f},{base:.1f} Z")
    x0, x1 = cx - w / 2, cx + w / 2
    d = half(x0, x1, h) + " " + half(x0 + t, x1 - t, h - t)
    return (f'<path fill="{fill}" fill-rule="evenodd" d="{d}"/>'
            f'<circle cx="{cx:.1f}" cy="{base - r * 1.1:.1f}" r="{r:.1f}" fill="{ember}"/>')


def svg(vb, body, label, bg=None):
    x, y, w, h = vb
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" role="img" aria-label="{label}">{rect}{body}</svg>'


# ---------- các bản logo ----------
def logo_dung(fg=CH, ember=BO, sub=None, bg=None):
    """Bản đứng (chính): vòm + An Tâm + ẨM THỰC · TẬN TÂM."""
    sub = sub or fg
    wm, w = wordmark_text("An Tâm", 120, fg, ember, 0, 250, anchor="middle")
    b = arch(0, 128, 128, fg, ember)
    tg, tw = text("ẨM THỰC  ·  TẬN TÂM", 22, "sans", .32, 0, 312, sub, "middle")
    line = f'<rect x="{-w * .32:.0f}" y="276" width="{w * .64:.0f}" height="2" fill="{sub}" opacity=".5"/>'
    W = max(w, tw) + 80
    return svg((-W / 2, 30, W, 310), b + wm + line + tg, "Logo Ẩm Thực An Tâm bản đứng", bg)


def logo_ngang(fg=CH, ember=BO, sub=None, bg=None):
    """Bản ngang: vòm trái + chữ phải. Dùng cho biển hiệu, đầu thư, website."""
    sub = sub or fg
    b = arch(80, 118, 120, fg, ember)
    wm, w = wordmark_text("An Tâm", 104, fg, ember, 165, 118)
    tg, _ = text("ẨM THỰC · SẢN PHẨM TẬN TÂM", 17.5, "sans", .26, 168, 158, sub)
    return svg((10, 10, 175 + w + 20, 170), b + wm + tg, "Logo Ẩm Thực An Tâm bản ngang", bg)


def _ring_text(t, size, cx, cy, R, fill, start=-90, key="sans", track=.2):
    """Chữ chạy quanh vòng tròn (theo chiều kim đồng hồ, đọc từ ngoài)."""
    out = []; ang = math.radians(start)
    widths = []
    for ch in t:
        d, adv, upm, _ = _glyph(key, ch); s = size / upm
        widths.append((d, adv * s + size * track, s))
    total = sum(w for _, w, _ in widths)
    ang -= total / R / 2
    for d, w, s in widths:
        a = ang + w / 2 / R
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        rot = math.degrees(a) + 90
        if d:
            out.append(f'<path transform="translate({x:.1f} {y:.1f}) rotate({rot:.2f}) translate({-w / 2 + size * .1:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        ang += w / R
    return f'<g fill="{fill}">{"".join(out)}</g>'


def logo_dau(fg=CH, ember=BO, ring=KEM, bg=None):
    """Con dấu tròn: viền kép, chữ chạy vòng, giữa là vòm + An Tâm."""
    cx = cy = 200
    b = (f'<circle cx="{cx}" cy="{cy}" r="190" fill="{fg}"/>'
         f'<circle cx="{cx}" cy="{cy}" r="178" fill="none" stroke="{ring}" stroke-width="2"/>'
         f'<circle cx="{cx}" cy="{cy}" r="128" fill="none" stroke="{ring}" stroke-width="2"/>')
    b += _ring_text("ẨM THỰC AN TÂM", 25, cx, cy, 143, ring, -90, track=.22)
    b += _ring_bottom("SẢN PHẨM TẬN TÂM", 21, cx, cy, 151, ring)
    for a in (180, 0):
        x = cx + 151 * math.cos(math.radians(a)); b += f'<circle cx="{x:.1f}" cy="{cy}" r="5" fill="{ember}"/>'
    b += arch(cx, 190, 120, ring, ember)
    wm, _ = wordmark_text("An Tâm", 72, ring, ember, cx, 262, anchor="middle")
    return svg((0, 0, 400, 400), b + wm, "Con dấu Ẩm Thực An Tâm", bg)


def _ring_bottom(t, size, cx, cy, R, fill, key="sans", track=.2):
    """Chữ trên cung dưới, đọc xuôi từ trái sang phải."""
    out = []; ws = []
    for ch in t:
        d, adv, upm, _ = _glyph(key, ch); s = size / upm
        ws.append((d, adv * s + size * track, s))
    total = sum(w for _, w, _ in ws)
    ang = math.radians(90) + total / R / 2
    for d, w, s in ws:
        a = ang - w / 2 / R
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        rot = math.degrees(a) - 90
        if d:
            out.append(f'<path transform="translate({x:.1f} {y:.1f}) rotate({rot:.2f}) translate({-w / 2 + size * .1:.1f} {size * .35:.1f}) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        ang -= w / R
    return f'<g fill="{fill}">{"".join(out)}</g>'


def bieu_tuong(fg=CH, ember=BO, bg=KEM, shape="circle"):
    """Biểu tượng rời (ảnh đại diện, favicon)."""
    sh = f'<circle cx="100" cy="100" r="100" fill="{bg}"/>' if shape == "circle" else f'<rect width="200" height="200" rx="44" fill="{bg}"/>'
    return svg((0, 0, 200, 200), sh + arch(100, 128, 120, fg, ember), "Biểu tượng vòm lò An Tâm")


def hoa_van(w, h, fg=CH, ember=BO, bg=KEM, step=110):
    """Hoa văn vòm lặp, hàng so le."""
    b = [f'<rect width="{w}" height="{h}" fill="{bg}"/>']
    for j, y in enumerate(range(60, h + step, int(step * .62))):
        off = step / 2 if j % 2 else 0
        for x in range(-step, w + step, step):
            b.append(arch(x + off, y, 84, fg, ember if (x // step + j) % 3 == 0 else fg))
    return svg((0, 0, w, h), "".join(b), "Hoa văn vòm lò An Tâm")


if __name__ == "__main__":
    out = os.path.join(HERE, "vom")
    os.makedirs(out, exist_ok=True)
    files = {
        "logo-dung-cherry.svg": logo_dung(),
        "logo-dung-kem-tren-cherry.svg": logo_dung(KEM, BO, KEM, CH),
        "logo-ngang-cherry.svg": logo_ngang(),
        "logo-ngang-kem-tren-cherry.svg": logo_ngang(KEM, BO, KEM, CH),
        "con-dau-cherry.svg": logo_dau(),
        "con-dau-den.svg": logo_dau(DEN, BO, KEM),
        "bieu-tuong-tron.svg": bieu_tuong(),
        "bieu-tuong-vuong-cherry.svg": bieu_tuong(KEM, BO, CH, "square"),
        "hoa-van-vom.svg": hoa_van(1200, 800),
    }
    for k, v in files.items():
        open(os.path.join(out, k), "w").write(v + "\n")
    print("đã xuất", len(files), "file")


def vault(cx, base, w, h, t, fg):
    """Mái vòm cao (cửa lò): nửa elip rộng w, cao h, nét dày t, đáy phẳng."""
    k = .5523
    def half(x0, x1, hh):
        c = (x0 + x1) / 2; rx = (x1 - x0) / 2
        return (f"M{x0:.1f},{base:.1f} C{x0:.1f},{base - k * hh:.1f} {c - k * rx:.1f},{base - hh:.1f} {c:.1f},{base - hh:.1f} "
                f"C{c + k * rx:.1f},{base - hh:.1f} {x1:.1f},{base - k * hh:.1f} {x1:.1f},{base:.1f} Z")
    return f'<path fill="{fg}" fill-rule="evenodd" d="{half(cx - w / 2, cx + w / 2, h)} {half(cx - w / 2 + t, cx + w / 2 - t, h - t)}"/>'


def wordmark_lo(size, fg, ember, x=0, y=0, anchor="middle"):
    """Chữ "An Tâm": dấu mũ phóng to thành cửa lò cao ngang chữ hoa, chữ a nằm trong lò, hạt than phía trên."""
    f = _fonts("serif")[0]; cm = f.getBestCmap(); upm = f["head"].unitsPerEm; s = size / upm
    aw = f["hmtx"][cm[ord("a")]][0] * s
    xh = (f["OS/2"].sxHeight or upm * .5) * s; cap = (f["OS/2"].sCapHeight or upm * .7) * s
    t = size * .042; W = aw + 2 * t + size * .3; H = cap * 1.04
    p1, w1 = text("An T", size, x=0, y=0, fill=fg)
    vx = w1 + size * .05 + W / 2
    a_g, _ = text("a", size, x=vx - aw / 2, y=0, fill=fg)
    r = t * .85
    em = f'<circle cx="{vx:.1f}" cy="{-(xh + (H - t - xh) * .55):.1f}" r="{r * 1.25:.1f}" fill="{ember}"/>'
    m_g, wm = text("m", size, x=vx + W / 2 + size * .05, y=0, fill=fg)
    total = vx + W / 2 + size * .05 + wm
    ox = {"start": 0, "middle": -total / 2}[anchor]
    return f'<g transform="translate({x + ox:.1f} {y:.1f})">{p1}{vault(vx, 0, W, H, t, fg)}{em}{a_g}{m_g}</g>', total

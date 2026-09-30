"""Logo Ẩm Thực An Tâm theo tinh thần hình mẫu Nonla:
chữ thường đậm có chân (Fraunces 900, SOFT 50, WONK), dấu mũ chữ â là chiếc taco,
dòng chữ cao hẹp (Anton), hai màu tương phản mạnh: đỏ và vàng.
Chạy: python3 logo_nl.py -> in JSON các SVG.
"""
import json
import math
import os
import sys

import pathops
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
DO, DO_DAM, VANG, KEM, MUC, BO, RAU = "#D7150E", "#A90F09", "#FFC53D", "#FFF6E6", "#3A1410", "#FFE3A3", "#5BA94A"

FONTS = {
    "fr": [os.path.join(HERE, f"fr50-{s}-900.woff2") for s in ("latin", "vietnamese")],
    "anton": [os.path.join(SCR, f"anton/package/files/anton-{s}-400-normal.woff2") for s in ("latin", "vietnamese", "latin-ext")],
}
_cache = {}


def fonts(k):
    if k not in _cache:
        _cache[k] = [TTFont(p) for p in FONTS[k] if os.path.exists(p)]
    return _cache[k]


def outline(text, k="fr", size=100.0, track=0.0):
    """(path, advance list, bề ngang). Chân chữ y = 0."""
    fs = fonts(k); upm = fs[0]["head"].unitsPerEm; sc = size / upm
    out = pathops.Path(); x = 0.0; xs = []
    for ch in text:
        f = next((f for f in fs if f.getBestCmap().get(ord(ch))), fs[0])
        gname = f.getBestCmap().get(ord(ch), ".notdef")
        adv = f["hmtx"][gname][0] * sc
        xs.append((x, adv))
        if ch != " ":
            gs = f.getGlyphSet(); rec = DecomposingRecordingPen(gs); gs[gname].draw(rec)
            gp = pathops.Path(); rec.replay(TransformPen(gp.getPen(), (sc, 0, 0, -sc, x, 0)))
            out = pathops.op(out, gp, pathops.PathOp.UNION)
        x += adv + track * size
    return out, xs, x - track * size


def d(p):
    pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    p.draw(pen); return pen.getCommands()


# ---------- chữ "an tâm", chữ â vẽ bằng a + taco ----------
WM, WM_XS, WM_W = outline("an tam", "fr", 100, -0.005)
WM_B = WM.bounds
A_X, A_ADV = WM_XS[4]
X_TOP = WM_B[1]          # đỉnh chữ (chữ t cao nhất)


def taco(cx, bottom, w, fill, cut, tilt=-14):
    """Chiếc taco một màu, khoét chi tiết bằng màu nền: vỏ bán nguyệt, sóng rau, hai quả cà chua."""
    r = w / 2
    yt = bottom - r * .66                      # mép trên vỏ bánh
    s = f'<g transform="rotate({tilt} {cx:.1f} {bottom - r * .4:.1f})">'
    s += (f'<path d="M{cx - r * .96:.1f},{yt - r * .06:.1f} ' +
          " ".join(f"q{r * .12:.2f},{-r * (.46 if i % 2 == 0 else .34):.2f} {r * .24:.2f},0" for i in range(8)) +
          f' V{yt + r * .06:.1f} H{cx - r * .96:.1f} Z" fill="{fill}"/>')
    s += f'<path d="M{cx - r:.1f},{yt + r * .16:.1f} H{cx + r:.1f} A{r:.1f},{r * .66 - r * .16:.1f} 0 0 1 {cx - r:.1f},{yt + r * .16:.1f} Z" fill="{fill}"/>'
    for dx, dy, rr in [(-.5, .22, .075), (-.08, .36, .065), (.38, .24, .08)]:
        s += f'<ellipse cx="{cx + dx * r:.1f}" cy="{yt + r * .16 + dy * r:.1f}" rx="{rr * r * 1.4:.1f}" ry="{rr * r:.1f}" fill="{cut}"/>'
    return s + "</g>"


A_TOP = outline("a", "fr", 100)[0].bounds[1]


def wordmark(fg=VANG, cut=DO, sub=True, sub_fg=None, top=True):
    """Chữ an tâm + (tuỳ chọn) ẨM THỰC phía trên và dòng sản phẩm phía dưới."""
    sub_fg = sub_fg or fg
    b = f'<path fill="{fg}" d="{d(WM)}"/>'
    b += taco(A_X + A_ADV / 2 + 3, A_TOP - 7, 52, fg, cut)
    y0 = X_TOP - 34
    if top:
        p, _, w = outline("ẨM THỰC", "anton", 21, .09)
        b += f'<path transform="translate(2 {X_TOP - 12:.1f})" fill="{fg}" d="{d(p)}"/>'
        y0 = X_TOP - 50
    y1 = 20
    if sub:
        p, _, w = outline("BÁNH TORTILLAS & DONER KEBAB", "anton", 19.5, .035)
        sc = (WM_B[2] - WM_B[0]) / w
        b += f'<path transform="translate({WM_B[0]:.1f} 46) scale({sc:.4f})" fill="{sub_fg}" d="{d(p)}"/>'
        y1 = 58
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{WM_B[0] - 6:.0f} {y0:.0f} {WM_B[2] - WM_B[0] + 12:.0f} {y1 - y0:.0f}" '
            f'role="img" aria-label="Ẩm Thực An Tâm">{b}</svg>')


def mark(fg=VANG, cut=DO, bg=DO, rounded=True):
    """Biểu tượng: chữ â có mũ taco trong ô vuông bo góc."""
    p, xs, w = outline("a", "fr", 100)
    bb = p.bounds
    cx = (bb[0] + bb[2]) / 2
    s = 150 / 1.0
    body = (f'<rect x="-75" y="-75" width="150" height="150" rx="{36 if rounded else 75}" fill="{bg}"/>'
            f'<g transform="translate({-cx * 1.0:.1f} 38) scale(1.0)"><path fill="{fg}" d="{d(p)}"/>'
            f'{taco(cx + 3, bb[1] - 7, 56, fg, cut)}</g>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-75 -75 150 150" role="img" aria-label="Biểu tượng An Tâm">{body}</svg>'


# ---------- linh vật Bé Tâm: chiếc taco biết cười ----------
def mascot(uid="m", pose="chao", scale=1.0):
    """Nhân vật phẳng có đổ bóng mềm để gợi khối, cao 300 x rộng 260."""
    g = (f'<defs><radialGradient id="{uid}s" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#FFE08A"/><stop offset=".6" stop-color="#F7B642"/><stop offset="1" stop-color="#D98A22"/></radialGradient>'
         f'<radialGradient id="{uid}l" cx=".5" cy=".3" r=".7"><stop offset="0" stop-color="#8BD66A"/><stop offset="1" stop-color="#3F8F34"/></radialGradient>'
         f'<radialGradient id="{uid}b" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FF7A6A" stop-opacity=".9"/><stop offset="1" stop-color="#FF7A6A" stop-opacity="0"/></radialGradient></defs>')
    g += '<ellipse cx="130" cy="292" rx="80" ry="10" fill="#000" opacity=".18"/>'
    # chân
    g += '<path d="M100,250 v28 q0,8 -14,8 h-4" stroke="#C2771D" stroke-width="12" stroke-linecap="round" fill="none"/>'
    g += '<path d="M160,250 v28 q0,8 14,8 h4" stroke="#C2771D" stroke-width="12" stroke-linecap="round" fill="none"/>'
    # tay
    if pose == "chao":
        g += '<path d="M42,178 q-30,-20 -26,-62" stroke="#C2771D" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="16" cy="112" r="11" fill="#F7B642"/>'
    else:
        g += '<path d="M40,190 q-22,10 -24,34" stroke="#C2771D" stroke-width="12" stroke-linecap="round" fill="none"/>'
    g += '<path d="M220,190 q22,10 24,34" stroke="#C2771D" stroke-width="12" stroke-linecap="round" fill="none"/>'
    g += '<g transform="rotate(-7 130 170)">'
    # nhân: thịt, rau, cà chua
    g += '<path d="M34,120 q96,-50 192,0 v20 h-192 z" fill="#8A4A26"/>'
    g += ('<path d="M28,126 ' + " ".join(f"q{8.5},{-20 if i % 2 == 0 else -13} 17,0" for i in range(12)) + ' v18 h-204 z" fill="url(#' + uid + 'l)"/>')
    for x, y in [(62, 104), (104, 94), (150, 94), (196, 104)]:
        g += f'<circle cx="{x}" cy="{y}" r="13" fill="#E8352A"/><circle cx="{x - 4}" cy="{y - 4}" r="4" fill="#fff" opacity=".45"/>'
    # vỏ bánh
    g += f'<path d="M22,132 H238 A108,104 0 0 1 22,132 Z" fill="url(#{uid}s)"/>'
    for x, y, r in [(52, 168, 5), (74, 214, 4), (196, 222, 5), (214, 170, 4), (176, 240, 3.5), (92, 244, 3)]:
        g += f'<ellipse cx="{x}" cy="{y}" rx="{r * 1.4}" ry="{r}" fill="#B86A22" opacity=".55"/>'
    g += '<path d="M40,150 q20,-6 44,-4" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".35" fill="none"/></g>'
    # mặt
    if pose == "nhay":
        g += '<path d="M96,176 q10,-10 20,0" stroke="#3A1410" stroke-width="6" stroke-linecap="round" fill="none"/>'
    else:
        g += '<ellipse cx="106" cy="176" rx="7.5" ry="10" fill="#3A1410"/><circle cx="108" cy="172" r="2.6" fill="#fff"/>'
    g += '<ellipse cx="154" cy="176" rx="7.5" ry="10" fill="#3A1410"/><circle cx="156" cy="172" r="2.6" fill="#fff"/>'
    g += '<path d="M116,198 q14,14 28,0" stroke="#3A1410" stroke-width="6" stroke-linecap="round" fill="none"/>'
    g += f'<ellipse cx="84" cy="196" rx="16" ry="10" fill="url(#{uid}b)"/><ellipse cx="176" cy="196" rx="16" ry="10" fill="url(#{uid}b)"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 60 260 245" role="img" aria-label="Linh vật Bé Tâm">{g}</svg>'


# ---------- chữ bậc thang (Anton, góc 30°) ----------
C, S = math.cos(math.pi / 6), math.sin(math.pi / 6)
_G = json.load(open(os.path.join(SCR, "anton-glyphs.json")))


def _word(t, cap):
    s = cap / _G["cap"]; x = 0; out = ""
    for ch in t:
        if ch == " ":
            x += _G["space"] * s; continue
        gl = _G["g"].get(ch)
        if not gl:
            x += _G["space"] * s; continue
        out += f'<path transform="translate({x:.1f} 0) scale({s:.5f} {-s:.5f})" d="{gl[1]}"/>'
        x += gl[0] * s + cap * .03
    return out, max(0, x - cap * .03)


def stairs(lines, fg=VANG, side=None, hi=KEM, hi_idx=(), D=110, H=140, F=.64, bg=None, pad=30):
    def shade(h):
        n = int(h[1:], 16); r, gg, b = n >> 16, n >> 8 & 255, n & 255
        return f"rgb({round(r * .94)},{round(gg * .9)},{round(b * .9)})"
    side = side or shade(fg)
    fx = fy = 0; xs = []; ys = []; body = ""; B = .13
    for i, t in enumerate(lines):
        flat = i % 2 == 0
        col = hi if i in hi_idx else (fg if flat else side)
        if flat:
            p, ln = _word(t, D * F); o = D * B
            body += f'<g fill="{col}" transform="matrix({C:.4f} {S} {-C:.4f} {S} {fx + C * o:.1f} {fy - S * o:.1f})">{p}</g>'
            xs += [fx, fx + C * ln, fx + C * D, fx + C * (ln + D)]; ys += [fy, fy + S * ln, fy - S * D, fy + S * (ln - D)]
        else:
            p, ln = _word(t, H * F); bx, by, o = fx, fy + H, H * B
            body += f'<g fill="{col}" transform="matrix({C:.4f} {S} 0 1 {bx:.1f} {by - o:.1f})">{p}</g>'
            xs += [fx, bx + C * ln, fx + C * ln, bx]; ys += [fy, by + S * ln, fy + S * ln, by]
            fx, fy = bx - C * D, by + S * D
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    rect = f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}" role="img" aria-label="{" ".join(lines)}">{rect}{body}</svg>'


OUT = {
    "wm_do": wordmark(VANG, DO),                         # vàng trên đỏ (bản chính)
    "wm_kem": wordmark(DO, KEM, sub_fg=MUC),             # đỏ trên kem
    "wm_bo": wordmark(DO, BO, sub_fg=MUC),               # đỏ trên vàng bơ (bao bì)
    "wm_muc": wordmark(VANG, MUC),                       # vàng trên nâu mực
    "wm_den": wordmark("#000", "#fff"),                  # một màu
    "wm_gon_do": wordmark(VANG, DO, sub=False, top=False),
    "mark_do": mark(), "mark_vang": mark(DO, VANG, VANG), "mark_kem": mark(DO, KEM, KEM),
    "mascot": mascot("a", "chao"), "mascot2": mascot("b", "nhay"),
}

if __name__ == "__main__":
    json.dump(OUT, sys.stdout)

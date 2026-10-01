"""Biến thể chữ AN TÂM và bố cục mới, dựng từ chu_sang.py."""
import pathops
import chu_sang as C
import logo_cao_cap as L

RED, IVORY, INK, GOLD = C.RED, C.IVORY, C.INK, C.GOLD
_serif = C.serif


def build(tk=17.0, tn=4.2, serif=True, bite=False):
    C.TK, C.TN = tk, tn
    C.serif = _serif if serif else (lambda *a, **k: pathops.Path())
    wl, ww, hat_cx, xs = C.wordmark_paths()
    if bite:
        mx, mw = xs["M"]
        cx, cy = mx + mw + 1, 1
        for dx, dy, r in [(-2, 4, 22), (-22, -4, 13), (2, 30, 14), (-34, 8, 9), (-8, -8, 10)]:
            wl = L.D_(wl, C._circle(cx + dx, cy + dy, r))
    hat = C.tortilla_hat(hat_cx, -11, 17 + (tk - 17) * .3)
    C.TK, C.TN, C.serif = 17.0, 4.2, _serif
    return L.d(wl), L.d(hat), ww, xs


VARS = {
    "thanh_lich": dict(), "dam": dict(tk=24, tn=6.5), "khong_chan": dict(tk=19, tn=4.6, serif=False),
    "khac": dict(tk=25, tn=7), "mieng_can": dict(bite=True), "nghieng": dict(),
}
P = {k: build(**v) for k, v in VARS.items()}


def word_svg(key, fg, hat, bg=None, skew=0, inline=False, uid="x"):
    wd, hd, ww, _ = P[key]
    g = f'<path fill="{fg}" d="{wd}"/>'
    if inline:
        g = (f'<clipPath id="{uid}c"><path d="{wd}"/></clipPath>{g}'
             f'<g clip-path="url(#{uid}c)"><path d="{wd}" fill="none" stroke="{bg}" stroke-width="10"/>'
             f'<path d="{wd}" fill="none" stroke="{fg}" stroke-width="5"/></g>')
    g += f'<path fill="{hat}" d="{hd}"/>'
    if skew:
        g = f'<g transform="skewX({skew})">{g}</g>'
    x0 = -8 - (24 if skew else 0)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0 - 10:.0f} -42 {ww + 28:.0f} 152" role="img" aria-label="AN TÂM">{g}</svg>'


def _txt(t, cap, track, weight=500):
    return C.text(t, cap, track, weight)


AMT_V, AMT_VW = _txt("ẨM THỰC", 13, .55)
DESC_V, DESC_VW = _txt("BÁNH TORTILLAS · DONER KEBAB", 8.2, .26)


def vom_dung(fg, hat, line, bg, uid="v"):
    """Khung vòm đứng: AN trên, TÂM dưới, như nhãn chai nước hoa."""
    wd, hd, ww, xs = P["thanh_lich"]
    an_w = xs["N"][0] + xs["N"][1]
    tam_x = xs["T"][0]; tam_w = ww - tam_x
    W = 360
    s = f'<rect width="{W}" height="520" fill="{bg}"/>' if bg else ""
    s += f'<path d="M30,500 V180 a150,150 0 0 1 300,0 V500 Z" fill="none" stroke="{line}" stroke-width="1.6"/>'
    s += f'<path d="M42,488 V180 a138,138 0 0 1 276,0 V488 Z" fill="none" stroke="{line}" stroke-width=".8"/>'
    s += C.at(AMT_V, (W - AMT_VW) / 2, 120, fg)
    sc = 240 / tam_w
    s += f'<g transform="translate({(W - an_w * sc) / 2:.1f} 170) scale({sc:.3f})"><clipPath id="{uid}an"><rect x="-20" y="-60" width="{an_w + 30:.0f}" height="200"/></clipPath><g clip-path="url(#{uid}an)"><path fill="{fg}" d="{wd}"/></g></g>'
    s += f'<g transform="translate({(W - tam_w * sc) / 2 - tam_x * sc:.1f} 314) scale({sc:.3f})"><clipPath id="{uid}tam"><rect x="{tam_x - 10:.0f}" y="-60" width="{tam_w + 30:.0f}" height="200"/></clipPath><g clip-path="url(#{uid}tam)"><path fill="{fg}" d="{wd}"/></g><path fill="{hat}" d="{hd}"/></g>'
    s += f'<path d="M110,{462} H250" stroke="{hat}" stroke-width="1"/>'
    s += C.at(DESC_V, (W - DESC_VW) / 2, 440, fg)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 520" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'


def tem_tron(fg, hat, ring, bg, uid="t"):
    wd, hd, ww, xs = P["thanh_lich"]
    sc = 230 / ww
    s = f'<circle cx="200" cy="200" r="196" fill="{bg}"/><circle cx="200" cy="200" r="186" fill="none" stroke="{ring}" stroke-width="1.6"/>'
    s += f'<circle cx="200" cy="200" r="138" fill="none" stroke="{ring}" stroke-width=".8"/>'
    s += (f'<defs><path id="{uid}a" d="M48,200 A152,152 0 0 1 352,200"/><path id="{uid}b" d="M40,200 A160,160 0 0 0 360,200"/></defs>'
          f'<text fill="{fg}" style="font:600 19px \'BVP\',sans-serif;letter-spacing:.42em"><textPath href="#{uid}a" startOffset="50%" text-anchor="middle">ẨM THỰC AN TÂM</textPath></text>'
          f'<text fill="{fg}" style="font:500 15px \'BVP\',sans-serif;letter-spacing:.3em"><textPath href="#{uid}b" startOffset="50%" text-anchor="middle">BÁNH TORTILLAS · DONER KEBAB</textPath></text>')
    s += f'<circle cx="54" cy="200" r="3" fill="{hat}"/><circle cx="346" cy="200" r="3" fill="{hat}"/>'
    s += f'<g transform="translate({200 - ww * sc / 2:.1f} 196) scale({sc:.3f})"><path fill="{fg}" d="{wd}"/><path fill="{hat}" d="{hd}"/></g>'
    s += f'<path d="M150,250 H250" stroke="{hat}" stroke-width="1"/>'
    s += f'<text x="200" y="276" text-anchor="middle" fill="{fg}" style="font:500 11px \'BVP\',sans-serif;letter-spacing:.4em">TP. HỒ CHÍ MINH</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img" aria-label="Tem Ẩm Thực An Tâm">{s}</svg>'

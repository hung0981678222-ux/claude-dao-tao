"""Ba logo kết hợp: Cửa vòm, Huy hiệu, Ngang mạnh."""
import bien_the as V
import chu_sang as C

RED, IVORY, INK, GOLD = V.RED, V.IVORY, V.INK, V.GOLD
DEEP = "#7E0F0A"


def inline_group(dd, fg, bg, uid, sw=(9, 4.5)):
    return (f'<clipPath id="{uid}"><path d="{dd}"/></clipPath><path fill="{fg}" d="{dd}"/>'
            f'<g clip-path="url(#{uid})"><path d="{dd}" fill="none" stroke="{bg}" stroke-width="{sw[0]}"/>'
            f'<path d="{dd}" fill="none" stroke="{fg}" stroke-width="{sw[1]}"/></g>')


def part(key, which, uid):
    """Trả về (đường cắt clip cho AN hoặc TÂM, x0, bề ngang)."""
    wd, hd, ww, xs = V.P[key]
    if which == "an":
        x0, w = 0, xs["N"][0] + xs["N"][1]
    else:
        x0, w = xs["T"][0], ww - xs["T"][0]
    return wd, hd, x0, w


def stacked(key, fg, bg, hat, cx, y_an, y_tam, width, uid, inline=True):
    out = ""
    for which, y in (("an", y_an), ("tam", y_tam)):
        wd, hd, x0, w = part(key, which, uid)
        sc = width / w if which == "tam" else width * .78 / w
        body = inline_group(wd, fg, bg, f"{uid}{which}i") if inline else f'<path fill="{fg}" d="{wd}"/>'
        clip = f'<clipPath id="{uid}{which}"><rect x="{x0 - 30}" y="-70" width="{w + 60}" height="200"/></clipPath>'
        hat_s = f'<path fill="{hat}" d="{hd}"/>' if which == "tam" else ""
        out += (f'<g transform="translate({cx - (x0 + w / 2) * sc:.1f} {y}) scale({sc:.4f})">{clip}'
                f'<g clip-path="url(#{uid}{which})">{body}</g>{hat_s}</g>')
    return out


def ribbon(cx, y, w, h, fill, tail, text_d, text_w, text_fill, sc=1.0):
    x0, x1 = cx - w / 2, cx + w / 2
    s = (f'<path d="M{x0 - 34},{y + 10} H{x0 + 8} V{y + h + 10} H{x0 - 34} L{x0 - 20},{y + 10 + h / 2} Z" fill="{tail}"/>'
         f'<path d="M{x1 + 34},{y + 10} H{x1 - 8} V{y + h + 10} H{x1 + 34} L{x1 + 20},{y + 10 + h / 2} Z" fill="{tail}"/>'
         f'<path d="M{x0},{y + h} L{x0 + 8},{y + h + 10} V{y + h} Z M{x1},{y + h} L{x1 - 8},{y + h + 10} V{y + h} Z" fill="#000" opacity=".35"/>'
         f'<rect x="{x0}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>')
    s += f'<path transform="translate({cx - text_w * sc / 2:.1f} {y + h / 2 + 5.5 * sc:.1f}) scale({sc})" fill="{text_fill}" d="{text_d}"/>'
    return s


def cua_vom(bg=None, arch=RED, fg=GOLD, cut=RED, uid="cv"):
    """Khung vòm đỏ đặc, chữ AN/TÂM đậm viền khắc vàng, nhãn ẨM THỰC, dải băng sản phẩm."""
    W, Hh = 420, 560
    s = f'<rect width="{W}" height="{Hh}" fill="{bg}"/>' if bg else ""
    s += f'<path d="M50,520 V210 a160,160 0 0 1 320,0 V520 Z" fill="{arch}"/>'
    s += f'<path d="M64,506 V210 a146,146 0 0 1 292,0 V506 Z" fill="none" stroke="{fg}" stroke-width="1.6"/>'
    s += f'<path d="M72,498 V210 a138,138 0 0 1 276,0 V498 Z" fill="none" stroke="{fg}" stroke-width=".7"/>'
    # nhãn ẨM THỰC
    s += f'<rect x="{W / 2 - C.AMT_TW / 2 - 16:.1f}" y="104" width="{C.AMT_TW + 32:.1f}" height="26" rx="13" fill="{fg}"/>'
    s += C.at(C.AMT_T, W / 2 - C.AMT_TW / 2, 122.5, arch)
    s += stacked("khac", fg, arch, fg, W / 2, 170, 318, 236, uid)
    s += ribbon(W / 2, 410, 330, 34, DEEP, "#5A0A06", C.DESC, C.DESCW, IVORY, .9)
    s += f'<circle cx="{W / 2}" cy="475" r="3" fill="{fg}"/>'
    s += f'<path d="M{W / 2 - 60},475 H{W / 2 - 12} M{W / 2 + 12},475 H{W / 2 + 60}" stroke="{fg}" stroke-width="1"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hh}" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'


def huy_hieu(ring=RED, inner=DEEP, fg=GOLD, txt=IVORY, uid="hh"):
    """Huy hiệu tròn: taco trên đỉnh, chữ AN/TÂM đậm viền khắc, băng sản phẩm vắt ngang."""
    s = f'<circle cx="220" cy="230" r="200" fill="{ring}"/><circle cx="220" cy="230" r="186" fill="none" stroke="{fg}" stroke-width="1.6"/>'
    s += f'<circle cx="220" cy="230" r="150" fill="{inner}"/><circle cx="220" cy="230" r="142" fill="none" stroke="{fg}" stroke-width=".8"/>'
    for a in range(0, 360, 15):
        if 60 < a < 120:
            continue
        import math
        r1, r2 = 160, 176
        x1 = 220 + r1 * math.cos(math.radians(a)); y1 = 230 + r1 * math.sin(math.radians(a))
        x2 = 220 + r2 * math.cos(math.radians(a)); y2 = 230 + r2 * math.sin(math.radians(a))
        s += f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" stroke="{fg}" stroke-width="1.2" opacity=".55"/>'
    badge = V.C.taco_badge(IVORY, "#E9B75A", "#7FA33A", "#E8452F", fg, "#F3D08A") if hasattr(V.C, "taco_badge") else ""
    s += f'<g transform="translate(184 18) scale(.42)">{badge}</g>'
    s += C.at(C.AMT_C, 220 - C.AMT_CW / 2, 150, txt)
    s += stacked("khac", fg, inner, fg, 220, 178, 286, 170, uid)
    s += ribbon(220, 358, 316, 30, ring, "#5A0A06", C.DESC, C.DESCW, txt, .88)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 440" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'


def ngang(fg=INK, tag=RED, tag_fg=IVORY, hat=GOLD, uid="ng", badge_cols=None):
    """Ngang mạnh: biểu tượng taco + chữ đậm có miếng cắn + nhãn ẨM THỰC trên AN T + nét gạch vàng."""
    import pathops  # noqa: F401
    wd, hd, ww, xs = V.build(tk=24, tn=6.5, bite=True)
    t_right = xs["T"][0] + xs["T"][1]
    top, bot = -70, 140
    sc = (bot - top) / 230
    cols = badge_cols or (RED, "#E9B75A", "#7FA33A", "#E8452F", GOLD, "#F3D08A")
    s = f'<g transform="translate(0 {top}) scale({sc:.4f})">{C.taco_badge(*cols)}</g>'
    x0 = 170 * sc + 34
    g = f'<path fill="{fg}" d="{wd}"/><path fill="{hat}" d="{hd}"/>'
    g += f'<rect x="0" y="-48" width="{t_right}" height="26" rx="13" fill="{tag}"/>'
    g += C.at(C.AMT_T, (t_right - C.AMT_TW) / 2, -29.5, tag_fg)
    g += f'<path d="M0,118 C{ww * .3:.0f},110 {ww * .7:.0f},126 {ww},116" fill="none" stroke="{hat}" stroke-width="3" stroke-linecap="round"/>'
    g += C.at(C.DESC, 0, 140, fg)
    s += f'<g transform="translate({x0:.1f} 0)">{g}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 {top - 8} {x0 + ww + 12:.0f} {bot - top + 16}" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'

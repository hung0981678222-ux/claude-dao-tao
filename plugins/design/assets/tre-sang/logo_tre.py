"""Logo "an tâm" hướng Trẻ & Sang: Lexend 800 viết thường, khít chữ; chữ a một tầng tròn như chiếc bánh;
dấu mũ là chiếc bánh gập đôi màu bơ. Cherry, kem, hồng phấn, bơ."""
import logo_bot_lua as LB

CHERRY, KEM, HONG, BO, DEN, CHERRY2 = "#B5121B", "#FFF4E8", "#F7CFC6", "#FFD37A", "#1B1B1B", "#7D0A10"

WMP, WXS, WW = None, None, None
_p, _w = LB.outline("an tam", "lexend", 800, 100, -0.05)
WM = LB.d(_p)
WB = _p.bounds
# vị trí chữ a thứ hai: đo bằng outline từng phần
_pre, _pw = LB.outline("an t", "lexend", 800, 100, -0.05)
_a, _aw = LB.outline("a", "lexend", 800, 100)
AB = _a.bounds
A2_X = _pw + 100 * -0.05
A2_CX = A2_X + (AB[0] + AB[2]) / 2
A_TOP = AB[1]


def hat(cx, bottom, w, fill, cut, tilt=-12):
    r = w / 2; h = r * .7
    s = f'<g transform="rotate({tilt} {cx:.1f} {bottom:.1f})">'
    s += (f'<path d="M{cx - r:.1f},{bottom:.1f} C{cx - r:.1f},{bottom - h * 1.32:.1f} {cx + r:.1f},{bottom - h * 1.32:.1f} {cx + r:.1f},{bottom:.1f} Z" fill="{fill}"/>')
    for dx, dy, rr in [(-.48, -.28, .1), (-.02, -.52, .085), (.42, -.26, .11), (.16, -.14, .06)]:
        s += f'<ellipse cx="{cx + dx * r:.1f}" cy="{bottom + dy * r:.1f}" rx="{rr * r * 1.3:.1f}" ry="{rr * r * .85:.1f}" fill="{cut}"/>'
    return s + "</g>"


AMT, AMT_W = LB.outline("ẨM THỰC", "lexend", 800, 17, .12)
DESC, DESC_W = LB.outline("BÁNH TORTILLAS & DONER KEBAB", "lexend", 800, 11.5, .1)
AMT_D, DESC_D = LB.d(AMT), LB.d(DESC)


def wordmark(fg=CHERRY, hatc=BO, cut=None, top=True, sub=True, label="Ẩm Thực An Tâm"):
    cut = cut or fg
    b = f'<path fill="{fg}" d="{WM}"/>' + hat(A2_CX - 4, A_TOP - 6, 44, hatc, cut)
    y0 = A_TOP - 50
    if top:
        b += f'<path transform="translate({WB[0] + 2:.1f} {A_TOP - 14:.1f})" fill="{fg}" d="{AMT_D}"/>'
        y0 = A_TOP - 46
    y1 = 8
    if sub:
        sc = (WB[2] - WB[0] - 4) / DESC_W
        b += f'<path transform="translate({WB[0] + 2:.1f} 34) scale({sc:.4f})" fill="{fg}" d="{DESC_D}"/>'
        y1 = 42
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{WB[0] - 6:.0f} {y0:.0f} {WB[2] - WB[0] + 12:.0f} {y1 - y0:.0f}" '
            f'role="img" aria-label="{label}">{b}</svg>')


def mark(bg=CHERRY, fg=KEM, hatc=BO, shape="circle"):
    a = LB.d(_a)
    cx = (AB[0] + AB[2]) / 2
    sh = '<circle cx="0" cy="0" r="80"/>' if shape == "circle" else '<rect x="-80" y="-80" width="160" height="160" rx="44"/>'
    sh = sh.replace("/>", f' fill="{bg}"/>')
    body = (f'{sh}<g transform="translate({-cx * 1.15:.1f} 38) scale(1.15)"><path fill="{fg}" d="{a}"/>'
            f'{hat(cx + 1, A_TOP - 6, 48, hatc, bg)}</g>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-80 -80 160 160" role="img" aria-label="Biểu tượng An Tâm">{body}</svg>'

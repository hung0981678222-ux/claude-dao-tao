"""Logo chữ "an tâm" bản tinh chỉnh: Fraunces 900 (SOFT 50), khoảng chữ khít,
dấu mũ chữ â là chiếc bánh gập đôi có đốm nướng và viền rau."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "nl"))
import logo_nl as NL  # noqa: E402

DO, DO2, VANG, KEM, MUC, BO = "#D7150E", "#A90F09", "#FFC53D", "#FFF6E6", "#3A1410", "#FFE3A3"

WM, XS, W = NL.outline("an tam", "fr", 100, -0.03)
B = WM.bounds
A_X, A_ADV = XS[4]
A_TOP = NL.A_TOP


def hat(cx, bottom, w, fill, cut, fringe=None, tilt=-10):
    """Bánh gập đôi: vòm trên, cạnh phẳng dưới, đốm nướng khoét, viền rau thò ra dưới cạnh."""
    r = w / 2; h = r * .66
    fringe = fringe or fill
    s = f'<g transform="rotate({tilt} {cx:.1f} {bottom:.1f})">'
    s += (f'<path d="M{cx - r:.1f},{bottom - r * .1:.1f} C{cx - r:.1f},{bottom - h * 1.3:.1f} {cx + r:.1f},{bottom - h * 1.3:.1f} {cx + r:.1f},{bottom - r * .1:.1f} Z" '
          f'fill="{fill}" stroke="{cut}" stroke-width="{r * .1:.1f}" stroke-linejoin="round" paint-order="stroke"/>')
    for dx, dy, rr in [(-.5, -.3, .08), (-.05, -.5, .07), (.4, -.3, .09), (.14, -.2, .05)]:
        s += f'<ellipse cx="{cx + dx * r:.1f}" cy="{bottom + dy * r:.1f}" rx="{rr * r * 1.3:.1f}" ry="{rr * r * .85:.1f}" fill="{cut}"/>'
    return s + "</g>"


def wordmark(fg=VANG, cut=DO, sub_fg=None, top=True, sub=True, fringe=None):
    sub_fg = sub_fg or fg
    b = f'<path fill="{fg}" d="{NL.d(WM)}"/>'
    b += hat(A_X + A_ADV / 2 + 1, A_TOP - 9, 52, fg, cut, fringe)
    y0 = A_TOP - 50
    if top:
        p, _, w = NL.outline("ẨM THỰC", "anton", 20, .14)
        b += f'<path transform="translate({B[0] + 3:.1f} {B[1] - 12:.1f})" fill="{fg}" d="{NL.d(p)}"/>'
        y0 = min(y0, B[1] - 40)
    y1 = 10
    if sub:
        p, _, w = NL.outline("BÁNH TORTILLAS · DONER KEBAB", "anton", 17, .06)
        sc = (B[2] - B[0] - 6) / w
        b += f'<path transform="translate({B[0] + 3:.1f} 42) scale({sc:.4f})" fill="{sub_fg}" d="{NL.d(p)}"/>'
        y1 = 52
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{B[0] - 8:.0f} {y0:.0f} {B[2] - B[0] + 16:.0f} {y1 - y0:.0f}" '
            f'role="img" aria-label="Ẩm Thực An Tâm">{b}</svg>')


def mark(fg=VANG, cut=DO, bg=DO, fringe=None):
    p, _, _ = NL.outline("a", "fr", 100)
    bb = p.bounds; cx = (bb[0] + bb[2]) / 2
    body = (f'<rect x="-80" y="-80" width="160" height="160" rx="40" fill="{bg}"/>'
            f'<g transform="translate({-cx:.1f} 42)"><path fill="{fg}" d="{NL.d(p)}"/>{hat(cx + 1, bb[1] - 9, 60, fg, cut, fringe)}</g>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-80 -80 160 160" role="img" aria-label="Biểu tượng An Tâm">{body}</svg>'

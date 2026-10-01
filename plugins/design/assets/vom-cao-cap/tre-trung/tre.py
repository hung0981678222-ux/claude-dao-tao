"""Hướng trẻ trung: chữ AN TÂM nét dày đều, không chân, màu tươi, ba bố cục vui."""
import pathops
import chu_sang as C
import logo_cao_cap as L

DO, VANG, RAU, HONG, KEM, MUC = "#E8341C", "#FFC72C", "#22B573", "#FF8FA3", "#FFF8EC", "#1E1A17"
_serif = C.serif


def letters(tk=23.0, tn=13.0):
    """Từng chữ riêng: [(ký tự, path, x, w)], cùng hệ toạ độ chữ cao 100."""
    C.TK, C.TN = tk, tn
    C.serif = lambda *a, **k: pathops.Path()
    out, x = [], 0.0
    for ch in "AN TÂM":
        if ch == " ":
            x += C.SPACE - C.TRACK; continue
        g, w = {"A": C.A, "Â": C.A, "N": C.N, "T": C.T, "M": C.M}[ch](x)
        out.append((ch, g, x, w)); x += w + C.TRACK
    hat_x = [o for o in out if o[0] == "Â"][0]
    hat_cx = hat_x[2] + (hat_x[3] - tk + tn) / 2 + 2
    C.TK, C.TN, C.serif = 17.0, 4.2, _serif
    return out, x - C.TRACK, hat_cx


LT, LW, HCX = letters()
HAT = L.d(C.tortilla_hat(HCX, -10, 19))
WORD = L.d(L.U_(*[g for _, g, _, _ in LT]))


def _at(dd, x, y, fill, s=1.0):
    return f'<path transform="translate({x:.1f} {y:.1f}) scale({s})" fill="{fill}" d="{dd}"/>'


def sticker(fg=KEM, bg=DO, hat=VANG, tag_bg=VANG, tag_fg=MUC, uid="st"):
    """Bố cục 1: chữ trên viên thuốc bo tròn, nghiêng nhẹ, nhãn ẨM THỰC dán chéo."""
    W, Hh = LW + 190, 240
    s = f'<g transform="rotate(-5 {W / 2} {Hh / 2})">'
    s += f'<rect x="10" y="40" width="{W - 20}" height="170" rx="85" fill="#fff"/>'
    s += f'<rect x="20" y="50" width="{W - 40}" height="150" rx="75" fill="{bg}"/>'
    s += f'<g transform="translate(95 82)"><path fill="{fg}" d="{WORD}"/><path fill="{hat}" d="{HAT}"/></g>'
    s += '</g>'
    s += f'<g transform="rotate(-12 110 34)"><rect x="34" y="14" width="{C.AMT_TW * 1.15 + 34:.0f}" height="40" rx="20" fill="#fff"/>'
    s += f'<rect x="40" y="20" width="{C.AMT_TW * 1.15 + 22:.0f}" height="28" rx="14" fill="{tag_bg}"/>'
    s += _at(C.AMT_T, 51, 40, tag_fg, 1.15) + '</g>'
    for x, y, r in [(W - 40, 30, 9), (W - 18, 62, 5), (W - 62, 14, 4)]:
        s += f'<path d="M{x},{y - r} L{x + r * .3},{y - r * .3} L{x + r},{y} L{x + r * .3},{y + r * .3} L{x},{y + r} L{x - r * .3},{y + r * .3} L{x - r},{y} L{x - r * .3},{y - r * .3} Z" fill="{tag_bg}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {Hh}" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'


def o_mau(cols=(DO, VANG, RAU, HONG, DO), fgs=(KEM, MUC, KEM, MUC, KEM), hat=VANG, bg=None):
    """Bố cục 2: mỗi chữ một ô màu bo góc, như bảng màu đồ ăn."""
    pad, gap = 14, 8
    x, s, i = 0, "", 0
    tiles = []
    for ch, g, gx, w in LT:
        tw = w + pad * 2
        tiles.append((ch, g, gx, w, x, tw)); x += tw + gap
        if ch == "N":
            x += 18
    W = x - gap
    hat_done = False
    for (ch, g, gx, w, tx, tw), col, fg in zip(tiles, cols, fgs):
        rot = [-4, 3, -2, 4, -3][i]; i += 1
        s += f'<g transform="rotate({rot} {tx + tw / 2:.1f} 70)"><rect x="{tx:.1f}" y="6" width="{tw:.1f}" height="132" rx="26" fill="{col}"/>'
        s += f'<g transform="translate({tx + pad - gx:.1f} 22)"><path fill="{fg}" d="{L.d(g)}"/>'
        if ch == "Â" and not hat_done:
            s += f'<path fill="{MUC if col == VANG else hat}" d="{HAT}"/>'; hat_done = True
        s += '</g></g>'
    s += _at(C.AMT_C, (W - C.AMT_CW) / 2, -14, MUC)
    s += _at(C.DESC, (W - C.DESCW) / 2, 172, MUC)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -44 {W + 20:.0f} 230" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'


def nhun(fg=DO, hat=MUC, sub=MUC, uid="nh"):
    """Bố cục 3: chữ nhún nhảy lên xuống, ẨM THỰC trong bong bóng nói."""
    s = ""
    offs = [6, -6, 4, -8, 5]
    rots = [-6, 4, -3, 6, -4]
    for (ch, g, gx, w), dy, r in zip(LT, offs, rots):
        s += f'<g transform="rotate({r} {gx + w / 2:.1f} 50) translate(0 {dy})"><path fill="{fg}" d="{L.d(g)}"/>'
        if ch == "Â":
            s += f'<path fill="{hat}" d="{HAT}" transform="translate(0 -4)"/>'
        s += "</g>"
    bw = C.AMT_TW + 34
    s += (f'<g transform="translate(-6 -70) rotate(-6)"><rect width="{bw:.0f}" height="34" rx="17" fill="{MUC}"/>'
          f'<path d="M26,32 l4,14 l12,-14 z" fill="{MUC}"/>{_at(C.AMT_T, 17, 23, KEM)}</g>')
    s += f'<path d="M0,128 q{LW / 8:.0f},-10 {LW / 4:.0f},0 t{LW / 4:.0f},0 t{LW / 4:.0f},0 t{LW / 4:.0f},0" fill="none" stroke="{hat}" stroke-width="5" stroke-linecap="round"/>'
    s += _at(C.DESC, (LW - C.DESCW) / 2, 160, sub)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-24 -104 {LW + 48:.0f} 280" role="img" aria-label="Ẩm Thực An Tâm">{s}</svg>'


def mark(bg=DO, fg=KEM, hat=VANG):
    a = [o for o in LT if o[0] == "Â"][0]
    ch, g, gx, w = a
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" role="img" aria-label="Biểu tượng An Tâm">'
            f'<rect width="160" height="160" rx="48" fill="{bg}"/><g transform="translate({80 - (gx + w / 2) * .84:.1f} 44) scale(.84)">'
            f'<path fill="{fg}" d="{L.d(g)}"/><path fill="{hat}" d="{HAT}"/></g></svg>')

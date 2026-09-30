"""Logo Ẩm Thực An Tâm: biểu tượng vẽ lại bằng vector + chữ riêng của thương hiệu.

- Biểu tượng: chữ A ruy băng đỏ gấp nếp ôm bông lúa vàng hình chữ T (vẽ lại từ logo gốc).
- Chữ "AN TÂM", "ẨM THỰC": không chân, đậm, vững; đỉnh A bằng như logo; dấu mũ và
  dấu nặng là hạt lúa vàng.
- Khẩu hiệu: DejaVu Sans Bold, chuyển thành nét.

Chạy:  python3 build_logo_an_tam.py
Xuất cạnh file này: logo-ngang.svg, logo-doc.svg, logo-con-dau.svg, bieu-tuong.svg
và các bản trên nền đỏ (-nen-do).
"""
import math
import os

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

RED, RED_TXT, DEEP, GOLD, GOLD_D, INK = "#D7150E", "#BE0A0E", "#8C0F14", "#EFAE35", "#B87018", "#2A2A2A"
U, I, D = pathops.PathOp.UNION, pathops.PathOp.INTERSECTION, pathops.PathOp.DIFFERENCE


# ---------- hình cơ bản ----------
def poly(pts):
    p = pathops.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    return p


def rect(x0, y0, x1, y1):
    return poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def rrect(x0, y0, x1, y1, r):
    tl, tr, br, bl = (r,) * 4 if isinstance(r, (int, float)) else r
    k = .5523
    p = pathops.Path()
    p.moveTo(x0 + bl, y0); p.lineTo(x1 - br, y0)
    if br: p.cubicTo(x1 - br + br * k, y0, x1, y0 + br - br * k, x1, y0 + br)
    p.lineTo(x1, y1 - tr)
    if tr: p.cubicTo(x1, y1 - tr + tr * k, x1 - tr + tr * k, y1, x1 - tr, y1)
    p.lineTo(x0 + tl, y1)
    if tl: p.cubicTo(x0 + tl - tl * k, y1, x0, y1 - tl + tl * k, x0, y1 - tl)
    p.lineTo(x0, y0 + bl)
    if bl: p.cubicTo(x0, y0 + bl - bl * k, x0 + bl - bl * k, y0, x0 + bl, y0)
    p.close()
    return p


def circle(cx, cy, r):
    return rrect(cx - r, cy - r, cx + r, cy + r, r)


def union(*ps):
    ps = [p for p in ps if p is not None]
    out = ps[0]
    for p in ps[1:]:
        out = pathops.op(out, p, U)
    return out


def diff(a, *bs):
    for b in bs:
        a = pathops.op(a, b, D)
    return a


class _X:
    def __init__(self, path, fn): self.p, self.fn = path, fn
    def moveTo(self, pt): self.p.moveTo(*self.fn(pt))
    def lineTo(self, pt): self.p.lineTo(*self.fn(pt))
    def curveTo(self, *pts): self.p.cubicTo(*[c for q in pts for c in self.fn(q)])
    def qCurveTo(self, *pts):
        # đổi đường bậc hai (có thể nhiều điểm) sang từng đoạn quadTo
        pts = [self.fn(q) for q in pts]
        for i in range(len(pts) - 1):
            ctrl, end = pts[i], pts[i + 1]
            if i < len(pts) - 2:
                end = ((ctrl[0] + end[0]) / 2, (ctrl[1] + end[1]) / 2)
            self.p.quadTo(*ctrl, *end)
    def closePath(self): self.p.close()
    def endPath(self): self.p.close()


def xform(p, fn):
    out = pathops.Path()
    p.draw(_X(out, fn))
    return out


def move(p, dx, dy, s=1.0):
    return xform(p, lambda q: (q[0] * s + dx, q[1] * s + dy))


def grain(cx, cy, length, width, angle):
    """Hạt lúa: thuôn hai đầu, bụng hơi lệch."""
    a = math.radians(angle); ca, sa = math.cos(a), math.sin(a)
    def t(x, y): return (cx + x * ca - y * sa, cy + x * sa + y * ca)
    h, w = length / 2, width * 0.72
    p = pathops.Path()
    p.moveTo(*t(-h, 0))
    p.cubicTo(*t(-h * 0.35, w), *t(h * 0.5, w * 0.9), *t(h, 0))
    p.cubicTo(*t(h * 0.5, -w * 0.9), *t(-h * 0.35, -w), *t(-h, 0))
    p.close()
    return p


def d(p):
    pen = SVGPathPen(None)
    p.draw(pen)
    return pen.getCommands()


# ---------- biểu tượng: A ruy băng + T bông lúa ----------
def symbol():
    """Hệ toạ độ 0..1000, y hướng lên. Trả về các lớp để tô màu."""
    W = 158
    ax, ay = 500, 930

    def leg(foot, top):
        (fx, fy), (tx, ty) = foot, top
        dx, dy = tx - fx, ty - fy
        L = math.hypot(dx, dy)
        nx, ny = dy / L * W / 2 / (dy / L), 0  # bề rộng theo phương ngang
        h = W / 2 / (dy / L)
        return poly([(fx - h, fy), (fx + h, fy), (tx + h, ty), (tx - h, ty)])

    left = leg((150, 70), (ax, ay))
    right = leg((850, 70), (ax, ay))
    clipbox = rect(0, 70, 1000, ay)
    left = pathops.op(left, clipbox, I)
    right = pathops.op(right, clipbox, I)
    # đỉnh gấp: bo tròn đỉnh A, phần chân phải phía trên nằm sau (mặt trái của lụa)
    cap = circle(ax, ay - 70, 100)
    top = pathops.op(union(left, right), rect(0, ay - 150, 1000, ay + 50), I)
    apex = pathops.op(union(top, cap), rect(0, 0, 1000, ay - 5), I)
    back = diff(poly([(ax - 10, ay - 150), (ax + 110, ay - 150), (ax + 40, ay - 40)]), left)
    front_left = union(left, apex)
    front_right = right
    # nếp gấp ở hai chân (lụa lật ra ngoài)
    fold_l = poly([(150 - 95, 70), (150 - 190, 70), (150 - 95, 190)])
    fold_r = poly([(850 + 95, 70), (850 + 190, 70), (850 + 95, 190)])
    # bông lúa hình chữ T, đứng trong lòng chữ A
    gold = []
    for side in (-1, 1):
        sx = ax + side * 16
        pts = []
        for i in range(91):
            t = i / 90
            if t < 0.62:
                x, y = sx, 70 + t / 0.62 * 330
            else:
                u = (t - 0.62) / 0.38
                x = sx + side * (u ** 1.5) * 170
                y = 400 + math.sin(u * math.pi / 2) * 120
            pts.append((x, y))
        stalk = union(*[circle(x, y, 15 - 7 * (i / 90)) for i, (x, y) in enumerate(pts)])
        gold.append(stalk)
        for k, i in enumerate(range(60, 91, 9)):
            x, y = pts[i]
            gold.append(grain(x + side * 4, y + 34, 74 - k * 6, 30, 90 - side * (25 + k * 12)))
            gold.append(grain(x + side * 26, y - 6, 66 - k * 6, 26, 90 - side * (70 + k * 6)))
    gold = union(*gold)
    return {"front_left": front_left, "front_right": front_right, "back": back,
            "folds": union(fold_l, fold_r), "gold": gold}


# ---------- chữ riêng: A N T Â M Ẩ H Ự C ----------
S, B = 150, 128     # nét đứng, nét ngang
CAP = 700


def A_(w=720):
    ta = 70
    outer = poly([(0, 0), (w / 2 - ta, CAP), (w / 2 + ta, CAP), (w, 0)])
    k = CAP / (w / 2 - ta)                       # độ dốc chân
    h = S / math.sin(math.atan(k))              # bề rộng ngang của chân
    apex_y = CAP - (h - ta) * k if h > ta else CAP - 30
    inner = poly([(h, 0), (w / 2, (w / 2 - h) * k), (w - h, 0)])
    return diff(outer, diff(inner, rect(0, 150, w, 150 + B))), w


def N_(w=640):
    return union(rect(0, 0, S, CAP), rect(w - S, 0, w, CAP), poly([(0, CAP), (S + 30, CAP), (w, 0), (w - S - 30, 0)])), w


def T_(w=620):
    return union(rect(0, CAP - B, w, CAP), rect((w - S) / 2, 0, (w + S) / 2, CAP)), w


def M_(w=820):
    v = poly([(0, CAP), (S + 20, CAP), (w / 2, 250), (w - S - 20, CAP), (w, CAP), (w / 2 + 75, 90), (w / 2 - 75, 90)])
    return union(rect(0, 0, S, CAP), rect(w - S, 0, w, CAP), v), w


def H_(w=640):
    return union(rect(0, 0, S, CAP), rect(w - S, 0, w, CAP), rect(0, 290, w, 290 + B)), w


def U_(w=650):
    return diff(rrect(0, 0, w, CAP, (0, 0, 280, 280)), rrect(S, B, w - S, CAP + 50, (0, 0, 150, 150))), w


def C_(w=660):
    ring = diff(rrect(0, 0, w, CAP, 330), rrect(S, B, w - S, CAP - B, 190))
    return diff(ring, poly([(w * .55, 250), (w + 10, 190), (w + 10, 510), (w * .55, 450)])), w


def hat(cx, y):
    """Dấu mũ: hai hạt lúa chụm đầu."""
    return union(grain(cx - 62, y + 60, 170, 64, 38), grain(cx + 62, y + 60, 170, 64, 142))


def dot_below(cx):
    return grain(cx, -150, 110, 62, 20)


def hook(cx, y):
    ring = diff(circle(cx, y + 110, 62), circle(cx, y + 110, 24), rect(cx - 70, y + 40, cx, y + 118))
    return union(ring, rect(cx - 22, y, cx + 22, y + 60))


def horn(x):
    return grain(x + 10, CAP - 10, 150, 60, 58)


def word(letters, gap=70):
    """Ghép chữ: letters là danh sách (path, width) hoặc ('space', w). Trả (red, gold, width)."""
    x, red, gold = 0, [], []
    for item in letters:
        if item[0] == "space":
            x += item[1]; continue
        p, w, extras = item
        red.append(move(p, x, 0))
        for e in extras:
            gold.append(move(e(w), x, 0))
        x += w + gap
    return union(*red), (union(*gold) if gold else None), x - gap


def an_tam():
    A, wa = A_(); N, wn = N_(); T, wt = T_(); A2, _ = A_(); M, wm = M_()
    return word([(A, wa, []), (N, wn, []), ("space", 230), (T, wt, []),
                 (A2, wa, [lambda w: hat(w / 2, CAP + 60)]), (M, wm, [])], gap=60)


def am_thuc():
    A, wa = A_(); M, wm = M_(); T, wt = T_(); H, wh = H_(); Uu, wu = U_(); Cc, wc = C_()
    return word([(A, wa, [lambda w: hat(w / 2 - 50, CAP + 60), lambda w: hook(w / 2 + 170, CAP + 150)]),
                 (M, wm, []), ("space", 230), (T, wt, []), (H, wh, []),
                 (Uu, wu, [lambda w: horn(w - 60), lambda w: dot_below(w / 2)]), (Cc, wc, [])], gap=60)


# ---------- chữ khẩu hiệu (DejaVu Sans Bold) ----------
_FONT = None


def text_path(s, size, tracking=0):
    global _FONT
    if _FONT is None:
        _FONT = TTFont(DEJAVU)
    gs = _FONT.getGlyphSet(); cmap = _FONT.getBestCmap(); upm = _FONT["head"].unitsPerEm
    sc = size / upm
    x, parts = 0, []
    import unicodedata
    for ch in unicodedata.normalize("NFC", s):
        g = cmap.get(ord(ch))
        if g is None:
            continue
        p = pathops.Path()
        rec = DecomposingRecordingPen(gs)
        gs[g].draw(rec)
        rec.replay(_X(p, lambda q, x=x: (x + q[0] * sc, q[1] * sc)))
        parts.append(p)
        x += gs[g].width * sc + tracking
    return union(*[q for q in parts if list(_segs(q))]), x - tracking


def _segs(p):
    out = []
    class R:
        def moveTo(s, pt): out.append(1)
        def lineTo(s, pt): out.append(1)
        def curveTo(s, *a): out.append(1)
        def qCurveTo(s, *a): out.append(1)
        def closePath(s): pass
        def endPath(s): pass
    p.draw(R())
    return out


# ---------- ghép bố cục ----------
def defs():
    return (f'<defs><linearGradient id="gL" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4493D"/><stop offset="1" stop-color="#C8120C"/></linearGradient>'
            f'<linearGradient id="gR" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C8120C"/><stop offset=".55" stop-color="#D7150E"/><stop offset="1" stop-color="#7E0C10"/></linearGradient>'
            f'<linearGradient id="gG" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{GOLD_D}"/><stop offset=".55" stop-color="#F6C24C"/><stop offset="1" stop-color="{GOLD_D}"/></linearGradient></defs>')


def sym_layers(sym, dx, dy, s, on_red=False):
    def put(p): return d(move(p, dx, dy, s))
    if on_red:
        fills = {"front_left": "#FFFFFF", "front_right": "#F3E3DC", "back": "#D9BFB5", "folds": "#C9A89A"}
    else:
        fills = {"front_left": "url(#gL)", "front_right": "url(#gR)", "back": DEEP, "folds": "#7E0C10"}
    out = "".join(f'<path d="{put(sym[k])}" fill="{fills[k]}"/>' for k in ("back", "folds", "front_right", "front_left"))
    return out + f'<path d="{put(sym["gold"])}" fill="url(#gG)"/>'


def svg(body, box, bg=None, radius=0):
    x0, y0, x1, y1 = box
    r = f'<rect x="{x0}" y="{-y1}" width="{x1 - x0}" height="{y1 - y0}" rx="{radius}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {-y1:.0f} {x1 - x0:.0f} {y1 - y0:.0f}">'
            f'{defs()}{r}<g transform="scale(1,-1)">{body}</g></svg>\n')


def rules(x0, x1, y, color):
    return f'<rect x="{x0:.0f}" y="{y - 5:.0f}" width="{x1 - x0:.0f}" height="10" rx="5" fill="{color}"/>'


def lockup_horizontal(on_red=False):
    sym = symbol()
    red, gold, w1 = an_tam()
    sred, sgold, w2 = am_thuc()
    slogan, ws = text_path("SẢN PHẨM TẬN TÂM - PHÁT TRIỂN XỨNG TẦM", 64, 2)
    txt = "#FFFFFF" if on_red else RED_TXT
    ink = "#FFFFFF" if on_red else INK
    X = 1150
    body = sym_layers(sym, 0, 0, 1.0, on_red)
    body += f'<path d="{d(move(sred, X, 800, 0.24))}" fill="{ink}"/>'
    body += f'<path d="{d(move(sgold, X, 800, 0.24))}" fill="url(#gG)"/>'
    body += f'<path d="{d(move(red, X, 170, 0.62))}" fill="{txt}"/>'
    body += f'<path d="{d(move(gold, X, 170, 0.62))}" fill="url(#gG)"/>'
    wbig = w1 * 0.62
    sx = X + (wbig - ws) / 2
    body += f'<path d="{d(move(slogan, sx, 40))}" fill="{ink}"/>'
    body += rules(X, sx - 40, 62, GOLD) + rules(sx + ws + 40, X + wbig, 62, GOLD)
    return svg(body, (-120, -60, X + wbig + 80, 1110), "#D7150E" if on_red else None)


def lockup_vertical(on_red=False):
    sym = symbol()
    red, gold, w = am_thuc_an_tam()
    slogan, ws = text_path("Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm", 70, 1)
    txt = "#FFFFFF" if on_red else RED_TXT
    ink = "#FFFFFF" if on_red else INK
    s = 0.34
    W = w * s
    body = sym_layers(sym, (W - 1000 * 0.9) / 2, 420, 0.9, on_red)
    body += f'<path d="{d(move(red, 0, 190, s))}" fill="{txt}"/><path d="{d(move(gold, 0, 190, s))}" fill="url(#gG)"/>'
    sx = (W - ws) / 2
    body += f'<path d="{d(move(slogan, sx, 40))}" fill="{ink}"/>'
    body += rules(0, sx - 40, 62, GOLD) + rules(sx + ws + 40, W, 62, GOLD)
    return svg(body, (-100, -60, W + 100, 1330), "#D7150E" if on_red else None)


def am_thuc_an_tam():
    a, ga, wa = am_thuc()
    b, gb, wb = an_tam()
    gap = 260
    return union(a, move(b, wa + gap, 0)), union(ga, move(gb, wa + gap, 0)), wa + gap + wb


def seal():
    """Con dấu tròn như chiếc bánh: vòng đỏ, chữ chạy quanh, biểu tượng ở giữa."""
    sym = symbol()
    R = 1000
    body = f'<circle cx="0" cy="0" r="{R}" fill="{RED}"/><circle cx="0" cy="0" r="{R - 60}" fill="none" stroke="#FFFFFF" stroke-width="14"/>'
    body += f'<circle cx="0" cy="0" r="{R - 300}" fill="#FFFFFF"/>'
    body += sym_layers(sym, -380, -370, 0.76)

    def arc_text(s, radius, center_deg, size, top=True):
        out = []
        glyph, w = text_path(s, size, 6)
        # đặt từng nét theo cung tròn: chia chữ thành các ký tự
        chars, x = [], 0
        for ch in s:
            g, cw = text_path(ch, size, 0) if ch.strip() else (None, size * 0.33)
            chars.append((g, cw)); x += cw + 6
        total = x - 6
        ang_total = total / radius
        a = math.radians(center_deg) + (ang_total / 2 if top else -ang_total / 2)
        for g, cw in chars:
            da = (cw + 6) / radius
            mid = a - da / 2 if top else a + da / 2
            if g is not None:
                rot = mid - math.pi / 2 if top else mid + math.pi / 2
                cx0, cy0 = radius * math.cos(mid), radius * math.sin(mid)
                def f(q, cw=cw, rot=rot, cx0=cx0, cy0=cy0):
                    x, y = q[0] - cw / 2, q[1] - size * 0.36
                    return (cx0 + x * math.cos(rot) - y * math.sin(rot), cy0 + x * math.sin(rot) + y * math.cos(rot))
                out.append(xform(g, f))
            a = a - da if top else a + da
        return union(*out)

    top = arc_text("ẨM THỰC AN TÂM", R - 170, 90, 150, True)
    bot = arc_text("ANTAMFOODS.COM", R - 175, 270, 104, False)
    body += f'<path d="{d(top)}" fill="#FFFFFF"/><path d="{d(bot)}" fill="#FFFFFF"/>'
    for sgn in (-1, 1):
        body += f'<path d="{d(grain(sgn * (R - 170), 0, 120, 56, 90))}" fill="url(#gG)"/>'
    return svg(body, (-R - 20, -R - 20, R + 20, R + 20))


def symbol_only(on_red=False):
    return svg(sym_layers(symbol(), 0, 0, 1.0, on_red), (-80, -20, 1080, 1060), "#D7150E" if on_red else None)


if __name__ == "__main__":
    out = {
        "bieu-tuong.svg": symbol_only(), "bieu-tuong-nen-do.svg": symbol_only(True),
        "logo-ngang.svg": lockup_horizontal(), "logo-ngang-nen-do.svg": lockup_horizontal(True),
        "logo-doc.svg": lockup_vertical(), "logo-doc-nen-do.svg": lockup_vertical(True),
        "logo-con-dau.svg": seal(),
    }
    for k, v in out.items():
        open(os.path.join(HERE, k), "w").write(v)
    print("Đã tạo", len(out), "file")

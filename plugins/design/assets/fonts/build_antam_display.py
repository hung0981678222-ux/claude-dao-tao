"""Dựng font tiêu đề An Tâm Display 3.0 (chữ in hoa, đủ dấu tiếng Việt).

Chạy:  pip install fonttools skia-pathops brotli
       python3 build_antam_display.py
Kết quả: AnTamDisplay-Black.otf và AnTamDisplay-Black.woff2 cạnh file này.

Ý tưởng: "an tâm" là cảm giác được che chở, nên chữ tròn đầu nét, dày, vững,
không góc nhọn. Nét Việt Nam lấy từ hai hình quen thuộc:
- Đầu đao mái đình: đầu các nét ngang tự do (T, E, F, L, Z, số 2, 5, 7) cong vểnh
  lên. Chữ A là mái nhà, hai chân vểnh ra như đầu đao: mái nhà che chở, an cư.
- Nón lá: dấu mũ của Â, Ê, Ô là chiếc nón lá.
- Hạt gạo: dấu nặng, dấu chấm, dấu phẩy là hạt gạo.

Mọi chữ dựng từ "xương" (đường giữa nét) rồi tô dày bằng nét tròn đầu.
"""
import math
import os
import unicodedata

import pathops
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.ttLib import TTFont

UPM, CAP = 1000, 700
R = 74                    # nửa bề dày nét
YB, YT, YM = R, CAP - R, 350
SIDE = 45                 # lề hai bên chữ


# ---------- hình cơ bản ----------
def poly(pts):
    p = pathops.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    return p


def disc(cx, cy, r):
    k = 0.5523 * r
    p = pathops.Path()
    p.moveTo(cx + r, cy)
    p.cubicTo(cx + r, cy + k, cx + k, cy + r, cx, cy + r)
    p.cubicTo(cx - k, cy + r, cx - r, cy + k, cx - r, cy)
    p.cubicTo(cx - r, cy - k, cx - k, cy - r, cx, cy - r)
    p.cubicTo(cx + k, cy - r, cx + r, cy - k, cx + r, cy)
    p.close()
    return p


def union(*ps):
    ps = [p for p in ps if p is not None]
    out = ps[0]
    for p in ps[1:]:
        out = pathops.op(out, p, pathops.PathOp.UNION)
    return out


def diff(a, *bs):
    for b in bs:
        a = pathops.op(a, b, pathops.PathOp.DIFFERENCE)
    return a


class _Xform:
    def __init__(self, path, fn):
        self.p, self.fn = path, fn

    def moveTo(self, pt): self.p.moveTo(*self.fn(pt))
    def lineTo(self, pt): self.p.lineTo(*self.fn(pt))
    def curveTo(self, *pts): self.p.cubicTo(*[c for q in pts for c in self.fn(q)])
    def qCurveTo(self, *pts): self.p.quadTo(*[c for q in pts for c in self.fn(q)])
    def closePath(self): self.p.close()
    def endPath(self): self.p.close()


def xform(p, fn):
    out = pathops.Path()
    p.draw(_Xform(out, fn))
    return out


def move(p, dx, dy):
    return xform(p, lambda q: (q[0] + dx, q[1] + dy))


def mirror_x(p, w):
    return xform(p, lambda q: (w - q[0], q[1]))


def rot180(p, cx, cy):
    return xform(p, lambda q: (2 * cx - q[0], 2 * cy - q[1]))


# ---------- nét tròn đầu ----------
def capsule(a, b, r):
    (x0, y0), (x1, y1) = a, b
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L * r, dx / L * r
    body = poly([(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)])
    return union(body, disc(x0, y0, r), disc(x1, y1, r))


def stroke(pts, r=R):
    parts = [capsule(pts[i], pts[i + 1], r) for i in range(len(pts) - 1)]
    return union(*parts)


def bez(p0, p1, p2, p3, n=18):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


def ell(cx, cy, rx, ry, a0=0, a1=360, n=48):
    """Điểm trên elip (độ, ngược chiều kim đồng hồ từ a0 tới a1)."""
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def ring(cx, cy, rx, ry, r=R):
    """Vòng kín, tô đặc giữa hai elip (mượt hơn nối nhiều nét)."""
    def e(ax, ay):
        pts = ell(cx, cy, ax, ay, 0, 360, 64)[:-1]
        return poly(pts)
    return diff(e(rx + r, ry + r), e(rx - r, ry - r))


def path(*segs):
    """Nối các đoạn điểm thành một đường xương."""
    out = []
    for s in segs:
        out.extend(s if not out else s[1:] if s[0] == out[-1] else s)
    return out


def dao(x0, y, x1, up=1, side=1):
    """Nét ngang có đầu đao: đi thẳng rồi cong vểnh lên ở đầu x1 (side=1 phải, -1 trái)."""
    L = 70 * side
    return path([(x0, y), (x1 - L, y)],
                bez((x1 - L, y), (x1 - L * 0.35, y), (x1, y + 6 * up), (x1 + 16 * side, y + 50 * up), 10))


# ---------- chữ ----------
G = {}


def glyph(name):
    def deco(fn):
        G[name] = fn()
        return fn
    return deco


@glyph("A")
def _A():
    ax, ay = 310, YT
    left = path([(ax, ay), (110, 190)], bez((110, 190), (82, 110), (30, 58), (-45, 118), 14))
    right = [(620 - x, y) for x, y in left]
    t = (ay - 270) / (ay - 170)
    xl = ax + (100 - ax) * t
    return union(stroke(left), stroke(right), stroke([(xl, 270), (620 - xl, 270)]))


@glyph("B")
def _B():
    top = path([(0, YT), (270, YT)], bez((270, YT), (440, YT), (440, 372), (270, 372)), [(270, 372), (0, 372)])
    bot = path([(0, 372), (300, 372)], bez((300, 372), (480, 372), (480, YB), (300, YB)), [(300, YB), (0, YB)])
    return union(stroke([(0, YB), (0, YT)]), stroke(top), stroke(bot))


@glyph("C")
def _C():
    return stroke(ell(320, 350, 300, 284, 42, 318, 40))


@glyph("D")
def _D():
    d = path([(0, YT), (230, YT)], bez((230, YT), (580, YT), (580, YB), (230, YB)), [(230, YB), (0, YB)])
    return union(stroke([(0, YB), (0, YT)]), stroke(d))


@glyph("E")
def _E():
    return union(stroke([(0, YB), (0, YT)]), stroke(dao(0, YT, 430)), stroke(dao(0, YM, 370)),
                 stroke(dao(0, YB, 450)))


@glyph("F")
def _F():
    return union(stroke([(0, YB), (0, YT)]), stroke(dao(0, YT, 430)), stroke(dao(0, YM - 10, 370)))


@glyph("G")
def _G():
    arc = ell(320, 350, 300, 284, 42, 360, 40)
    return union(stroke(arc), stroke([(620, 350), (620, 300)]), stroke([(620, 330), (390, 330)]))


@glyph("H")
def _H():
    return union(stroke([(0, YB), (0, YT)]), stroke([(500, YB), (500, YT)]), stroke([(0, YM), (500, YM)]))


@glyph("I")
def _I():
    return stroke([(0, YB), (0, YT)])


@glyph("J")
def _J():
    return stroke(path([(420, YT), (420, 250)], bez((420, 250), (420, 20), (40, 10), (20, 220))))


@glyph("K")
def _K():
    return union(stroke([(0, YB), (0, YT)]), stroke([(470, YT), (40, 290)]), stroke([(170, 410), (500, YB)]))


@glyph("L")
def _L():
    return union(stroke([(0, YB), (0, YT)]), stroke(dao(0, YB, 440)))


@glyph("M")
def _M():
    return stroke([(0, YB), (0, YT), (320, 250), (640, YT), (640, YB)])


@glyph("N")
def _N():
    return stroke([(0, YB), (0, YT), (520, YB), (520, YT)])


@glyph("O")
def _O():
    return ring(330, 350, 310, 284)


@glyph("P")
def _P():
    top = path([(0, YT), (270, YT)], bez((270, YT), (470, YT), (470, 300), (270, 300)), [(270, 300), (0, 300)])
    return union(stroke([(0, YB), (0, YT)]), stroke(top))


@glyph("Q")
def _Q():
    return union(ring(330, 350, 310, 284), stroke([(420, 190), (660, -40)]))


@glyph("R")
def _R():
    return union(_P(), stroke([(230, 300), (480, YB)]))


@glyph("S")
def _S():
    spine = path(bez((500, 560), (450, 670), (90, 680), (80, 520)),
                 bez((80, 520), (70, 380), (520, 370), (520, 210)),
                 bez((520, 210), (520, 20), (110, 20), (40, 150)))
    return stroke(spine)


@glyph("T")
def _T():
    bar = path(list(reversed(dao(280, YT, 0, 1, -1))), dao(280, YT, 560)[1:])
    return union(stroke(bar), stroke([(280, YT), (280, YB)]))


@glyph("U")
def _U():
    return stroke(path([(0, YT), (0, 260)], bez((0, 260), (0, 10), (520, 10), (520, 260)), [(520, 260), (520, YT)]))


@glyph("V")
def _V():
    return stroke([(0, YT), (300, YB), (600, YT)])


@glyph("W")
def _W():
    return stroke([(0, YT), (210, YB), (420, 560), (630, YB), (840, YT)])


@glyph("X")
def _X():
    return union(stroke([(0, YT), (540, YB)]), stroke([(540, YT), (0, YB)]))


@glyph("Y")
def _Y():
    return union(stroke([(0, YT), (280, 330), (560, YT)]), stroke([(280, 330), (280, YB)]))


@glyph("Z")
def _Z():
    return stroke(path([(0, YT), (500, YT), (0, YB)], dao(0, YB, 520)[1:]))


@glyph("Dcroat")
def _Dcroat():
    return union(move(_D(), 70, 0), stroke([(0, YM), (230, YM)]))


# ---------- số ----------
@glyph("zero")
def _0():
    return ring(260, 350, 240, 284)


@glyph("one")
def _1():
    return stroke([(90, 520), (290, YT), (290, YB)])


@glyph("two")
def _2():
    return stroke(path(bez((40, 500), (40, 690), (470, 690), (470, 470)),
                       bez((470, 470), (470, 330), (60, 250), (40, YB)),
                       dao(40, YB, 500)[1:]))


@glyph("three")
def _3():
    top = path(bez((40, 540), (90, 690), (450, 690), (450, 520)),
               bez((450, 520), (450, 400), (330, 372), (220, 372)))
    bot = path(bez((220, 372), (520, 372), (540, YB), (280, YB)),
               bez((280, YB), (170, YB), (80, 90), (40, 150)))
    return union(stroke(top), stroke(bot))


@glyph("four")
def _4():
    return union(stroke([(390, YB), (390, YT), (20, 210), (530, 210)]))


@glyph("five")
def _5():
    return stroke(path(list(reversed(dao(90, YT, 470))) + [(70, 380)],
                       bez((70, 380), (200, 440), (520, 450), (510, 230)),
                       bez((510, 230), (500, 30), (140, 30), (40, 150))))


@glyph("six")
def _6():
    return union(stroke(bez((440, 610), (370, 690), (50, 660), (50, 320))), ring(270, 230, 220, 164))


@glyph("seven")
def _7():
    return stroke(path(list(reversed(dao(250, YT, 0, 1, -1))), [(250, YT), (500, YT), (170, YB)]))


@glyph("eight")
def _8():
    return union(ring(270, 500, 190, 136), ring(270, 200, 230, 136))


@glyph("nine")
def _9():
    return rot180(_6(), 270, 350)


# ---------- dấu câu ----------
def grain(cx, cy, rx=58, ry=40, ang=30):
    """Hạt gạo: elip hơi thuôn, nghiêng."""
    a = math.radians(ang)
    pts = []
    for i in range(40):
        t = 2 * math.pi * i / 40
        x, y = rx * math.cos(t), ry * math.sin(t) * (1 - 0.18 * math.cos(t))
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    return poly(pts)


@glyph("period")
def _period():
    return disc(0, 72, 72)


@glyph("comma")
def _comma():
    return union(disc(0, 72, 72), stroke([(30, 60), (-30, -120)], 34))


@glyph("colon")
def _colon():
    return union(disc(0, 72, 72), disc(0, 420, 72))


@glyph("semicolon")
def _semicolon():
    return union(_comma(), disc(0, 420, 72))


@glyph("exclam")
def _exclam():
    return union(stroke([(0, YT), (0, 290)]), disc(0, 72, 72))


@glyph("question")
def _question():
    return union(stroke(path(bez((20, 540), (40, 690), (440, 700), (440, 520)),
                             bez((440, 520), (440, 400), (230, 400), (230, 280)))), disc(230, 72, 72))


@glyph("hyphen")
def _hyphen():
    return stroke([(0, 300), (240, 300)])


@glyph("endash")
def _endash():
    return stroke([(0, 300), (440, 300)])


@glyph("quotesingle")
def _quotesingle():
    return stroke([(0, YT), (0, 480)], 50)


@glyph("quotedbl")
def _quotedbl():
    return union(_quotesingle(), move(_quotesingle(), 170, 0))


@glyph("parenleft")
def _parenleft():
    return stroke(ell(330, 350, 270, 470, 118, 242, 24))


@glyph("parenright")
def _parenright():
    return mirror_x(_parenleft(), 220)


@glyph("slash")
def _slash():
    return stroke([(0, -60), (360, 760)])


@glyph("plus")
def _plus():
    return union(stroke([(0, 320), (440, 320)]), stroke([(220, 100), (220, 540)]))


@glyph("percent")
def _percent():
    return union(ring(110, 530, 90, 110, 44), ring(560, 170, 90, 110, 44), stroke([(560, YT), (110, YB)], 44))


G["space"] = pathops.Path()


# ---------- dấu tiếng Việt (vẽ quanh x=0, đáy y=0) ----------
MR = 40   # nửa bề dày nét dấu


def m_acute():
    return stroke([(-45, 22), (55, 128)], MR)


def m_grave():
    return stroke([(45, 22), (-55, 128)], MR)


def m_non_la():
    """Dấu mũ = chiếc nón lá: chóp nhọn, hai sườn hơi võng, vành cong."""
    p = pathops.Path()
    p.moveTo(-175, 34)
    p.cubicTo(-95, 66, -35, 125, 0, 196)
    p.cubicTo(35, 125, 95, 66, 175, 34)
    p.cubicTo(95, 0, -95, 0, -175, 34)
    p.close()
    return p


def m_breve():
    return stroke(ell(0, 120, 105, 95, 200, 340, 16), MR)


def m_tilde():
    pts = [(-120 + 240 * i / 20, 70 + 38 * math.sin(math.pi * 2 * i / 20)) for i in range(21)]
    return stroke(pts, MR - 4)


def m_hook():
    return stroke(path(bez((-55, 120), (-45, 205), (70, 205), (55, 125)),
                       bez((55, 125), (45, 85), (0, 90), (0, 40))), MR - 6)


def m_dot():
    return grain(0, -140, 60, 42, 28)


TONES = {"̀": m_grave, "́": m_acute, "̉": m_hook, "̃": m_tilde, "̣": m_dot}


def bounds(p):
    b = p.bounds
    return b if b else (0, 0, 0, 0)


def horn(base_path):
    """Móc của Ơ, Ư: nét vểnh lên như đầu đao."""
    x0, y0, x1, y1 = bounds(base_path)
    sx = x1 - R - 10
    return stroke(bez((sx, 560), (sx + 60, 600), (sx + 85, 640), (sx + 80, 720), 10), R - 12)


def compose(ch):
    d = unicodedata.normalize("NFD", ch)
    base, marks = d[0], d[1:]
    mod = None
    if "̂" in marks: mod = "circ"
    if "̆" in marks: mod = "breve"
    if "̛" in marks: mod = "horn"
    tone = next((m for m in marks if m in TONES), None)
    bp = G[base]
    x0, _, x1, _ = bounds(bp)
    cx = (x0 + x1) / 2
    if base == "A":
        cx = 310
    parts = [bp]
    if mod == "horn":
        parts.append(horn(bp))
        cx -= 20
    y = 790
    if mod in ("circ", "breve"):
        m = m_non_la() if mod == "circ" else m_breve()
        dx = cx - 50 if (mod == "circ" and tone in ("̀", "́", "̉")) else cx
        parts.append(move(m, dx, y))
    if tone:
        t = TONES[tone]()
        if tone == "̣":
            parts.append(move(t, cx, 0))
        elif mod == "circ" and tone != "̃":
            parts.append(move(t, cx + 175, 890))
        elif mod in ("circ", "breve"):
            parts.append(move(t, cx, 1010))
        else:
            parts.append(move(t, cx, y))
    return union(*parts)


def place(p):
    """Dời nét để mép trái cách gốc SIDE; trả về (nét, bề rộng chữ)."""
    if p.bounds is None or not list(_segs(p)):
        return p, 260
    x0, _, x1, _ = p.bounds
    return move(p, SIDE - x0, 0), round(x1 - x0 + 2 * SIDE)


def _segs(p):
    class Rec:
        def __init__(self): self.n = 0
        def moveTo(self, pt): self.n += 1
        def lineTo(self, pt): self.n += 1
        def curveTo(self, *pts): self.n += 1
        def qCurveTo(self, *pts): self.n += 1
        def closePath(self): pass
        def endPath(self): pass
    r = Rec()
    p.draw(r)
    return range(r.n)


def build(out_dir):
    names, cmap = {}, {}
    for n, p in G.items():
        names[n] = place(p) if n != "space" else (p, 260)
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cmap[ord(ch)] = ch
        cmap[ord(ch.lower())] = ch
    cmap[ord("Đ")] = cmap[ord("đ")] = "Dcroat"
    for ch, n in zip("0123456789", ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        cmap[ord(ch)] = n
    for ch, n in {".": "period", ",": "comma", ":": "colon", ";": "semicolon", "!": "exclam", "?": "question",
                  "-": "hyphen", "–": "endash", "'": "quotesingle", "\"": "quotedbl", "(": "parenleft",
                  ")": "parenright", "/": "slash", "+": "plus", "%": "percent", " ": "space",
                  " ": "space", "’": "quotesingle"}.items():
        cmap[ord(ch)] = n
    viet = set()
    for base in ["A", "Ă", "Â", "E", "Ê", "I", "O", "Ô", "Ơ", "U", "Ư", "Y"]:
        viet.add(base)
        for t in TONES:
            viet.add(unicodedata.normalize("NFC", base + t))
    for ch in sorted(viet):
        if len(ch) != 1 or ch in "AEIOUY":
            continue
        n = "uni%04X" % ord(ch)
        names[n] = place(compose(ch))
        cmap[ord(ch)] = n
        if len(ch.lower()) == 1:
            cmap[ord(ch.lower())] = n

    order = [".notdef"] + sorted(names)
    fb = FontBuilder(UPM, isTTF=False)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    notdef = diff(poly([(50, 0), (450, 0), (450, 700), (50, 700)]), poly([(110, 60), (390, 60), (390, 640), (110, 640)]))
    charstrings, metrics = {}, {}
    for n in order:
        p, adv = (notdef, 500) if n == ".notdef" else names[n]
        pen = T2CharStringPen(adv, None)
        p.draw(pen)
        charstrings[n] = pen.getCharString()
        b = p.bounds if list(_segs(p)) else None
        metrics[n] = (adv, int(b[0]) if b else 0)
    fb.setupCFF("AnTamDisplay-Black", {"FullName": "An Tam Display Black"}, charstrings, {})
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=1150, descent=-300)
    fb.setupNameTable({
        "familyName": "An Tam Display", "styleName": "Regular",
        "uniqueFontIdentifier": "AnTamDisplay-Black-3.0",
        "fullName": "An Tam Display Black", "psName": "AnTamDisplay-Black",
        "version": "Version 3.000",
        "copyright": "© 2026 Công ty TNHH SX-TM Ẩm Thực An Tâm",
        "trademark": "Ẩm Thực An Tâm",
        "description": "Font tiêu đề của Ẩm Thực An Tâm: chữ tròn, vững; đầu đao mái đình, dấu mũ nón lá, dấu nặng hạt gạo.",
    })
    fb.setupOS2(sTypoAscender=900, sTypoDescender=-250, sTypoLineGap=150,
                usWinAscent=1150, usWinDescent=300, sCapHeight=CAP, sxHeight=CAP,
                usWeightClass=900, achVendID="ANTM", fsType=0)
    fb.setupPost()
    otf = os.path.join(out_dir, "AnTamDisplay-Black.otf")
    fb.save(otf)
    f = TTFont(otf)
    f.flavor = "woff2"
    f.save(os.path.join(out_dir, "AnTamDisplay-Black.woff2"))
    return otf, len(order), len(cmap)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    otf, ng, nc = build(here)
    print("Đã tạo", otf, "-", ng, "glyph,", nc, "mã ký tự")

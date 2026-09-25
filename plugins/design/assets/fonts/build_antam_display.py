"""Dựng font tiêu đề An Tâm Display (chữ in hoa, đủ dấu tiếng Việt).

Chạy:  pip install fonttools skia-pathops brotli
       python3 build_antam_display.py
Kết quả: AnTamDisplay-Black.otf và AnTamDisplay-Black.woff2 cạnh file này.

Bản 2.0. Chi tiết riêng lấy từ logo Ẩm Thực An Tâm:
- Nếp gấp ruy băng: ở A, V, W, M, N, X, Q, số 1 một nét đè lên nét kia, cách khe trắng GAP.
- Đường gấp (seam) trên nét tròn O, C, G, số 0.
- Chữ T bông lúa: hai thân song song, đỉnh cong ra hai bên.
- Đỉnh thân cắt xiên (TILT) và đầu nét ngang cắt xiên (C) cùng nhịp ruy băng.
- Dấu sắc, huyền, mũ là hạt lúa; dấu nặng và dấu chấm là hình tròn như chiếc bánh.
"""
import math
import os
import unicodedata

import pathops
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.ttLib import TTFont

UPM, CAP = 1000, 700
S = 130   # nét đứng
B = 118   # nét ngang
C = 42    # độ xiên đầu nét
K = 0.5523


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
    """Chữ nhật bo góc; r là số hoặc (trên-trái, trên-phải, dưới-phải, dưới-trái)."""
    tl, tr, br, bl = (r, r, r, r) if isinstance(r, (int, float)) else r
    p = pathops.Path()
    p.moveTo(x0 + bl, y0)
    p.lineTo(x1 - br, y0)
    if br:
        p.cubicTo(x1 - br + br * K, y0, x1, y0 + br - br * K, x1, y0 + br)
    p.lineTo(x1, y1 - tr)
    if tr:
        p.cubicTo(x1, y1 - tr + tr * K, x1 - tr + tr * K, y1, x1 - tr, y1)
    p.lineTo(x0 + tl, y1)
    if tl:
        p.cubicTo(x0 + tl - tl * K, y1, x0, y1 - tl + tl * K, x0, y1 - tl)
    p.lineTo(x0, y0 + bl)
    if bl:
        p.cubicTo(x0, y0 + bl - bl * K, x0 + bl - bl * K, y0, x0 + bl, y0)
    p.close()
    return p


def disc(cx, cy, r):
    return rrect(cx - r, cy - r, cx + r, cy + r, r)


def leaf(cx, cy, length, width, angle):
    """Hạt lúa: hình thấu kính, xoay theo góc (độ)."""
    h = length / 2
    w = width * 0.75
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)

    def t(x, y):
        return (cx + x * ca - y * sa, cy + x * sa + y * ca)

    p = pathops.Path()
    p.moveTo(*t(-h, 0))
    p.cubicTo(*t(-h / 2, w), *t(h / 2, w), *t(h, 0))
    p.cubicTo(*t(h / 2, -w), *t(-h / 2, -w), *t(-h, 0))
    p.close()
    return p


def union(*ps):
    out = ps[0]
    for p in ps[1:]:
        out = pathops.op(out, p, pathops.PathOp.UNION)
    return out


def diff(a, *bs):
    for b in bs:
        a = pathops.op(a, b, pathops.PathOp.DIFFERENCE)
    return a


def move(p, dx, dy):
    out = pathops.Path()
    p.draw(_Shift(out, dx, dy, 1))
    return out


def rot180(p, w, h):
    out = pathops.Path()
    p.draw(_Shift(out, w, h, -1))
    return out


class _Shift:
    def __init__(self, path, dx, dy, s):
        self.p, self.dx, self.dy, self.s = path, dx, dy, s

    def _t(self, pt):
        return (self.s * pt[0] + self.dx, self.s * pt[1] + self.dy)

    def moveTo(self, pt): self.p.moveTo(*self._t(pt))
    def lineTo(self, pt): self.p.lineTo(*self._t(pt))
    def curveTo(self, *pts): self.p.cubicTo(*[c for q in pts for c in self._t(q)])
    def qCurveTo(self, *pts): self.p.quadTo(*[c for q in pts for c in self._t(q)])
    def closePath(self): self.p.close()
    def endPath(self): self.p.close()


class _Mirror(_Shift):
    """Lật ngang quanh bề rộng w."""
    def __init__(self, path, w):
        super().__init__(path, 0, 0, 1)
        self.w = w

    def _t(self, pt):
        return (self.w - pt[0], pt[1])


def arm_r(x0, y0, x1, y1):
    """Nét ngang, đầu phải cắt xiên (mép trên dài hơn)."""
    return poly([(x0, y0), (x1 - C, y0), (x1, y1), (x0, y1)])


def arm_l(x0, y0, x1, y1):
    """Nét ngang, đầu trái cắt xiên (mép dưới dài hơn)."""
    return poly([(x0, y0), (x1, y0), (x1, y1), (x0 + C, y1)])


def ring(x0, y0, x1, y1, ro, ri):
    return diff(rrect(x0, y0, x1, y1, ro), rrect(x0 + S, y0 + B, x1 - S, y1 - B, ri))


# ---------- chi tiết chữ ký (bản 2) ----------
GAP = 26   # khe trắng giữa hai lớp ruy băng
TILT = 30  # độ xiên đỉnh thân chữ


def grow(p, d=GAP):
    """Nở đường nét ra khoảng d (xấp xỉ bằng cách dời theo 12 hướng)."""
    out = p
    for i in range(12):
        a = math.pi * 2 * i / 12
        out = union(out, move(p, d * math.cos(a), d * math.sin(a)))
    return out


def over(front, back):
    """Nếp gấp ruy băng: nét trước đè lên nét sau, cách một khe trắng."""
    return union(front, diff(back, grow(front)))


def inter(a, b):
    return pathops.op(a, b, pathops.PathOp.INTERSECTION)


def stem(x0, x1, top=700, bottom=0):
    """Thân đứng, đỉnh cắt xiên lên bên phải như mép ruy băng."""
    return poly([(x0, bottom), (x1, bottom), (x1, top), (x0, top - TILT)])


def seam(cx, cy, angle, length=300):
    """Đường gấp: một khe mảnh cắt ngang nét tròn."""
    a = math.radians(angle)
    dx, dy = math.cos(a) * length / 2, math.sin(a) * length / 2
    nx, ny = -math.sin(a) * GAP / 2, math.cos(a) * GAP / 2
    return poly([(cx - dx - nx, cy - dy - ny), (cx + dx - nx, cy + dy - ny),
                 (cx + dx + nx, cy + dy + ny), (cx - dx + nx, cy - dy + ny)])


# ---------- chữ ----------
G = {}  # tên -> (đường nét, bề rộng nét vẽ, lề)


def glyph(name, w, side=50):
    def deco(fn):
        G[name] = (fn(), w, side)
        return fn
    return deco


@glyph("A", 700, 20)
def _A():
    left = poly([(0, 0), (150, 0), (425, 700), (275, 700)])
    right = poly([(550, 0), (700, 0), (425, 700), (275, 700)])
    hull = poly([(0, 0), (275, 700), (425, 700), (700, 0)])
    bar = inter(rect(0, 170, 700, 282), hull)
    return over(right, union(left, bar))

@glyph("B", 600)
def _B():
    top = rrect(0, 300, 560, 700, (0, 170, 170, 0))
    bot = rrect(0, 0, 600, 418, (0, 190, 190, 0))
    return diff(union(top, bot, rect(0, 0, S, 700)),
                rrect(S, 418, 560 - S, 700 - B, (0, 60, 60, 0)),
                rrect(S, B, 600 - S, 300, (0, 70, 70, 0)))


@glyph("C", 620)
def _C():
    body = diff(ring(0, 0, 620, 700, 240, 110),
                poly([(330, 270), (640, 220), (640, 480), (330, 430)]))
    return diff(body, seam(116, 584, 135))

@glyph("D", 640)
def _D():
    return diff(rrect(0, 0, 640, 700, (0, 260, 260, 0)),
                rrect(S, B, 640 - S, 700 - B, (0, 130, 130, 0)))


@glyph("E", 520)
def _E():
    return union(rect(0, 0, S, 700), arm_r(0, 700 - B, 520, 700),
                 arm_r(0, 292, 480, 292 + B), arm_r(0, 0, 540, B))


@glyph("F", 500)
def _F():
    return union(rect(0, 0, S, 700), arm_r(0, 700 - B, 500, 700), arm_r(0, 280, 460, 280 + B))


@glyph("G", 650)
def _G():
    body = diff(ring(0, 0, 650, 700, 240, 110),
                poly([(340, 398), (670, 398), (670, 540), (340, 500)]))
    return diff(union(body, rect(350, 280, 650, 398)), seam(116, 584, 135))

@glyph("H", 620)
def _H():
    return union(stem(0, S), stem(620 - S, 620), rect(0, 292, 620, 292 + B))

@glyph("I", S)
def _I():
    return stem(0, S)

@glyph("J", 520)
def _J():
    hook = diff(rrect(0, 0, 520, 420, (0, 0, 210, 210)),
                rrect(S, B, 520 - S, 520, (0, 0, 90, 90)),
                poly([(-10, 180), (S + 10, 220), (S + 10, 520), (-10, 520)]))
    return union(hook, rect(520 - S, 200, 520, 700))


@glyph("K", 630)
def _K():
    up = poly([(S + GAP, 270), (630, 700), (465, 700), (S + GAP, 450)])
    leg = poly([(290, 360), (465, 0), (640, 0), (410, 450)])
    return union(stem(0, S), up, leg)

@glyph("L", 500)
def _L():
    return union(stem(0, S), arm_r(0, 0, 520, B))

@glyph("M", 790)
def _M():
    dl = poly([(0, 700), (150, 700), (470, 170), (320, 170)])
    dr = poly([(640, 700), (790, 700), (470, 170), (320, 170)])
    v = over(dl, dr)
    return over(v, union(stem(0, S), stem(790 - S, 790)))

@glyph("N", 640)
def _N():
    return over(poly([(0, 700), (160, 700), (640, 0), (480, 0)]),
                union(stem(0, S), stem(640 - S, 640)))

@glyph("O", 690)
def _O():
    return diff(ring(0, 0, 690, 700, 250, 120), seam(119, 581, 135))

@glyph("P", 590)
def _P():
    bowl = diff(rrect(0, 260, 590, 700, (0, 210, 210, 0)),
                rrect(S, 260 + B, 590 - S, 700 - B, (0, 90, 90, 0)))
    return union(rect(0, 0, S, 700), bowl)


@glyph("Q", 690)
def _Q():
    return over(poly([(400, 210), (545, 240), (740, -60), (595, -90)]), G["O"][0])

@glyph("R", 610)
def _R():
    bowl = diff(rrect(0, 260, 590, 700, (0, 210, 210, 0)),
                rrect(S, 260 + B, 590 - S, 700 - B, (0, 90, 90, 0)))
    leg = poly([(250, 330), (410, 330), (620, 0), (455, 0)])
    return union(rect(0, 0, S, 700), bowl, leg)

@glyph("S", 580)
def _S():
    up = diff(rrect(0, 292, 560, 700, (200, 0, 0, 170)),
              rrect(S, 292 + B, 570, 700 - B, (80, 0, 0, 60)),
              poly([(560 - C, 700 - B - 1), (570, 700 - B - 1), (570, 700)]))
    lo = diff(rrect(20, 0, 580, 410, (0, 170, 200, 0)),
              rrect(10, B, 580 - S, 410 - B, (0, 60, 80, 0)),
              poly([(10, B + 1), (20 + C, B + 1), (10, -1)]))
    return union(up, lo)


@glyph("T", 620, 25)
def _T():
    """T bông lúa: hai thân song song tách ra ở đỉnh, như chữ T giữa logo."""
    h = GAP / 2
    def half():
        p = pathops.Path()
        p.moveTo(310 - h, 0)
        p.lineTo(310 - h - 118, 0)
        p.lineTo(310 - h - 118, 440)
        p.cubicTo(310 - h - 118, 590, 150, 612, 0, 628)
        p.lineTo(0, 700)
        p.lineTo(310 - h, 700)
        p.close()
        return p
    left = half()
    right = pathops.Path()
    left.draw(_Mirror(right, 620))
    return union(left, right)

@glyph("U", 630)
def _U():
    return diff(union(rrect(0, 0, 630, 640, (0, 0, 250, 250)), stem(0, S), stem(630 - S, 630)),
                rrect(S, B, 630 - S, 760, (0, 0, 120, 120)))

@glyph("V", 660, 20)
def _V():
    return over(poly([(0, 700), (150, 700), (405, 0), (255, 0)]),
                poly([(510, 700), (660, 700), (405, 0), (255, 0)]))

@glyph("W", 900, 20)
def _W():
    s1 = poly([(0, 700), (140, 700), (320, 0), (180, 0)])
    s2 = poly([(180, 0), (320, 0), (510, 700), (390, 700)])
    s3 = poly([(390, 700), (510, 700), (720, 0), (580, 0)])
    s4 = poly([(580, 0), (720, 0), (900, 700), (760, 700)])
    acc = over(s1, s2)
    acc = over(s3, acc)
    return over(acc, s4)

@glyph("X", 640, 20)
def _X():
    return over(poly([(0, 700), (155, 700), (640, 0), (485, 0)]),
                poly([(485, 700), (640, 700), (155, 0), (0, 0)]))

@glyph("Y", 640, 20)
def _Y():
    return union(poly([(0, 700), (155, 700), (320, 440), (485, 700), (640, 700), (385, 300), (255, 300)]),
                 rect(255, 0, 385, 330))

@glyph("Z", 580, 30)
def _Z():
    return union(arm_l(0, 700 - B, 580, 700), poly([(420, 582), (580, 582), (160, B), (0, B)]),
                 arm_r(0, 0, 580, B))

@glyph("Dcroat", 680)
def _Dcroat():
    d = move(G["D"][0], 40, 0)
    return union(d, rect(0, 292, 300, 292 + B))


# ---------- số ----------
@glyph("zero", 560)
def _0():
    return diff(ring(0, 0, 560, 700, 230, 110), seam(114, 586, 135))

@glyph("one", 560)
def _1():
    return over(poly([(110, 560), (300, 700), (430, 700), (170, 450)]), stem(300, 430))

@glyph("two", 560)
def _2():
    top = diff(rrect(0, 330, 560, 700, (0, 220, 200, 0)),
               rrect(-10, 330 + B, 560 - S, 700 - B, (0, 100, 90, 0)),
               rect(-1, 320, 420, 330 + B + 1),
               poly([(-1, 701), (C, 701), (-1, 700 - B)]))
    diag = poly([(415, 460), (560, 430), (175, B), (0, B)])
    return union(top, diag, arm_r(0, 0, 560, B))


@glyph("three", 560)
def _3():
    top = arm_l(0, 700 - B, 540, 700)
    diag = poly([(390, 700 - B), (540, 700 - B), (350, 460 - B), (200, 460 - B)])
    bowl = diff(rrect(0, 0, 560, 460, (0, 200, 210, 190)),
                rrect(S, B, 560 - S, 460 - B, (0, 80, 90, 70)),
                rect(-1, B, S + 1, 460 - B), rect(-1, 300, 200, 470))
    return union(top, diag, bowl)


@glyph("four", 560)
def _4():
    return union(rect(360, 0, 490, 700), rect(0, 170, 560, 170 + B),
                 poly([(0, 190), (350, 700), (490, 700), (150, 190)]))


@glyph("five", 560)
def _5():
    bowl = diff(rrect(0, 0, 560, 470, (0, 200, 210, 190)),
                rrect(S, B, 560 - S, 470 - B, (0, 80, 90, 70)),
                rect(-1, B, S + 1, 470 - B), rect(-1, 340, 40, 480))
    return union(bowl, rect(40, 380, 170, 700), arm_r(40, 700 - B, 560, 700))


@glyph("six", 560)
def _6():
    lo = ring(0, 0, 560, 470, 200, 90)
    top = diff(rrect(0, 300, 560, 700, (210, 200, 0, 0)),
               rrect(S, 290, 560 - S, 700 - B, (90, 80, 0, 0)),
               rect(560 - S - 1, 290, 561, 560))
    return union(lo, rect(0, 200, S, 560), top)


@glyph("seven", 560)
def _7():
    return union(arm_l(0, 700 - B, 560, 700), poly([(420, 700 - B), (560, 700 - B), (250, 0), (110, 0)]))


@glyph("eight", 560)
def _8():
    return union(ring(25, 330, 535, 700, 180, 70), ring(0, 0, 560, 430, 200, 90))


@glyph("nine", 560)
def _9():
    return rot180(G["six"][0], 560, 700)


# ---------- dấu câu ----------
@glyph("period", 150, 40)
def _period():
    return disc(75, 75, 75)


@glyph("comma", 150, 40)
def _comma():
    return union(disc(75, 75, 75), poly([(60, 20), (150, 60), (60, -150), (0, -150)]))


@glyph("colon", 150, 40)
def _colon():
    return union(disc(75, 75, 75), disc(75, 420, 75))


@glyph("semicolon", 150, 40)
def _semicolon():
    return union(G["comma"][0], disc(75, 420, 75))


@glyph("exclam", 150, 40)
def _exclam():
    return union(poly([(10, 700), (140, 700), (115, 230), (35, 230)]), disc(75, 75, 75))


@glyph("question", 520)
def _question():
    hook = diff(rrect(0, 330, 520, 700, (0, 210, 190, 0)),
                rrect(-10, 330 + B, 520 - S, 700 - B, (0, 90, 80, 0)),
                rect(-1, 320, 200, 330 + B + 1),
                poly([(-1, 701), (C, 701), (-1, 700 - B)]))
    return union(hook, rect(200, 210, 330, 330 + B), disc(265, 75, 75))


@glyph("hyphen", 320, 40)
def _hyphen():
    return poly([(0, 250), (320 - C, 250), (320, 250 + B), (C, 250 + B)])


@glyph("endash", 520, 40)
def _endash():
    return poly([(0, 250), (520 - C, 250), (520, 250 + B), (C, 250 + B)])


@glyph("quotesingle", 130, 50)
def _quotesingle():
    return poly([(0, 700), (130, 700), (100, 450), (30, 450)])


@glyph("quotedbl", 330, 50)
def _quotedbl():
    return union(_quotesingle(), move(_quotesingle(), 200, 0))


@glyph("parenleft", 260, 40)
def _parenleft():
    return diff(rrect(0, -120, 520, 820, (240, 0, 0, 240)), rrect(S, -120 + B, 700, 820 - B, (130, 0, 0, 130)),
                rect(260, -200, 800, 900))


@glyph("parenright", 260, 40)
def _parenright():
    return rot180(G["parenleft"][0], 260, 700)


@glyph("slash", 420, 20)
def _slash():
    return poly([(0, -80), (140, -80), (420, 780), (280, 780)])


@glyph("plus", 500, 40)
def _plus():
    return union(rect(185, 70, 315, 570), rect(0, 262, 500, 262 + B))


@glyph("percent", 760, 30)
def _percent():
    small = lambda x, y: diff(rrect(x, y, x + 260, y + 300, 110), rrect(x + 90, y + 85, x + 170, y + 215, 40))
    return union(small(0, 400), small(500, 0), poly([(520, 700), (660, 700), (240, 0), (100, 0)]))


@glyph("space", 240, 0)
def _space():
    return pathops.Path()


# ---------- dấu tiếng Việt (vẽ quanh x=0, đáy y=0) ----------
def m_acute():
    return leaf(10, 72, 200, 64, 40)


def m_grave():
    return leaf(-10, 72, 200, 64, 140)


def m_circ():
    return union(leaf(-58, 92, 220, 70, 58), leaf(58, 92, 220, 70, 122))


def m_breve():
    return diff(rrect(-130, 0, 130, 140, (0, 0, 110, 110)), rrect(-75, 58, 75, 220, (0, 0, 55, 55)))


def m_tilde():
    pts_top, pts_bot = [], []
    for i in range(21):
        x = -140 + 280 * i / 20
        y = 55 + 42 * math.sin(math.pi * 2 * i / 20)
        pts_top.append((x, y + 34))
        pts_bot.append((x, y - 34))
    return poly(pts_top + pts_bot[::-1])


def m_hook():
    ringp = diff(rrect(-80, 70, 80, 230, 78), rrect(-30, 118, 30, 182, 30), rect(-90, 60, 0, 150))
    return union(ringp, rect(-26, 0, 26, 100))


def m_dot():
    return disc(0, -130, 62)


def m_horn(x):
    """Móc của Ơ, Ư: hạt lúa mọc từ góc trên phải của chữ."""
    a = math.radians(55)
    return leaf(x - 70 + 85 * math.cos(a), 630 + 85 * math.sin(a), 170, 74, 55)


TONES = {"̀": m_grave, "́": m_acute, "̉": m_hook, "̃": m_tilde, "̣": m_dot}
MOD = {"Ă": ("A", "breve"), "Â": ("A", "circ"), "Ê": ("E", "circ"), "Ô": ("O", "circ"),
       "Ơ": ("O", "horn"), "Ư": ("U", "horn")}


def compose(ch):
    """Ghép chữ gốc + dấu mũ/trăng/móc + dấu thanh cho một chữ hoa tiếng Việt."""
    d = unicodedata.normalize("NFD", ch)
    base, marks = d[0], d[1:]
    mod = None
    if "̂" in marks: mod = "circ"
    if "̆" in marks: mod = "breve"
    if "̛" in marks: mod = "horn"
    tone = next((m for m in marks if m in TONES), None)
    path, w, side = G[base]
    cx = w / 2
    if base == "A": cx = 350
    parts = [path]
    extra = 0
    if mod == "horn":
        hx = w - 5
        parts.append(m_horn(hx))
        extra = 70
        cx = w / 2 - 10
    y = 770
    if mod in ("circ", "breve"):
        m = m_circ() if mod == "circ" else m_breve()
        dx = cx
        if mod == "circ" and tone in ("̀", "́", "̉"):
            dx = cx - 45
        parts.append(move(m, dx, y))
    if tone:
        t = TONES[tone]()
        if tone == "̣":
            parts.append(move(t, cx, 0))
        elif mod == "circ" and tone != "̃":
            parts.append(move(t, cx + 150, 860))
        elif mod in ("circ", "breve"):
            parts.append(move(t, cx, 960))
        else:
            parts.append(move(t, cx, y))
    return union(*parts), w + extra, side


def build(out_dir):
    names = {}          # tên glyph -> (path, advance)
    cmap = {}
    for n, (p, w, side) in G.items():
        names[n] = (move(p, side, 0), w + 2 * side)
    for ch, n in [(c, c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"] + [("Đ", "Dcroat")]:
        cmap[ord(ch)] = n
        cmap[ord(ch.lower())] = n
    for ch, n in zip("0123456789", ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        cmap[ord(ch)] = n
    for ch, n in {".": "period", ",": "comma", ":": "colon", ";": "semicolon", "!": "exclam", "?": "question",
                  "-": "hyphen", "–": "endash", "'": "quotesingle", "\"": "quotedbl", "(": "parenleft",
                  ")": "parenright", "/": "slash", "+": "plus", "%": "percent", " ": "space",
                  " ": "space", "’": "quotesingle"}.items():
        cmap[ord(ch)] = n
    # nguyên âm tiếng Việt: gốc + mũ/trăng/móc + 5 thanh
    viet = set()
    for base in ["A", "Ă", "Â", "E", "Ê", "I", "O", "Ô", "Ơ", "U", "Ư", "Y"]:
        viet.add(base)
        for t in TONES:
            viet.add(unicodedata.normalize("NFC", base + t))
    for ch in sorted(viet):
        if len(ch) != 1 or ch in "AEIOUY":
            continue
        n = "uni%04X" % ord(ch)
        p, w, side = compose(ch)
        names[n] = (move(p, side, 0), w + 2 * side)
        cmap[ord(ch)] = n
        lo = ch.lower()
        if len(lo) == 1:
            cmap[ord(lo)] = n

    order = [".notdef"] + sorted(names)
    fb = FontBuilder(UPM, isTTF=False)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    charstrings, metrics = {}, {}
    notdef = diff(rect(50, 0, 450, 700), rect(110, 60, 390, 640))
    for n in order:
        p, adv = (move(notdef, 0, 0), 500) if n == ".notdef" else names[n]
        pen = T2CharStringPen(adv, None)
        p.draw(pen)
        charstrings[n] = pen.getCharString()
        xs = [pt[0] for pt, _ in _points(p)] or [0]
        metrics[n] = (adv, int(min(xs)))
    fam = "An Tam Display"
    fb.setupCFF("AnTamDisplay-Black", {"FullName": "An Tam Display Black"}, charstrings, {})
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=1100, descent=-300)
    fb.setupNameTable({
        "familyName": fam, "styleName": "Regular",
        "uniqueFontIdentifier": "AnTamDisplay-Black-2.0",
        "fullName": "An Tam Display Black", "psName": "AnTamDisplay-Black",
        "version": "Version 2.000",
        "copyright": "© 2026 Công ty TNHH SX-TM Ẩm Thực An Tâm",
        "trademark": "Ẩm Thực An Tâm",
        "description": "Font tiêu đề chữ in hoa của Ẩm Thực An Tâm, đủ dấu tiếng Việt.",
    })
    fb.setupOS2(sTypoAscender=900, sTypoDescender=-250, sTypoLineGap=100,
                usWinAscent=1100, usWinDescent=300, sCapHeight=CAP, sxHeight=CAP,
                usWeightClass=900, achVendID="ANTM", fsType=0)
    fb.setupPost()
    otf = os.path.join(out_dir, "AnTamDisplay-Black.otf")
    fb.save(otf)
    f = TTFont(otf)
    f.flavor = "woff2"
    f.save(os.path.join(out_dir, "AnTamDisplay-Black.woff2"))
    return otf, len(order), len(cmap)


def _points(p):
    return [(pt, on) for pt, on in p.segments_points()] if hasattr(p, "segments_points") else list(_iter_pts(p))


def _iter_pts(p):
    class Rec:
        def __init__(self): self.pts = []
        def moveTo(self, pt): self.pts.append((pt, True))
        def lineTo(self, pt): self.pts.append((pt, True))
        def curveTo(self, *pts): self.pts.extend((q, True) for q in pts)
        def qCurveTo(self, *pts): self.pts.extend((q, True) for q in pts)
        def closePath(self): pass
        def endPath(self): pass
    r = Rec()
    p.draw(r)
    return r.pts


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    otf, ng, nc = build(here)
    print("Đã tạo", otf, "-", ng, "glyph,", nc, "mã ký tự")

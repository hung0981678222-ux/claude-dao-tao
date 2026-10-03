"""Vân tay Điểm Chỉ – lượt ý tưởng B: chữ A/a bằng khoảng trống, khuôn chữ, dấu mũ tách."""
import math, random
import numpy as np
from PIL import Image, ImageDraw
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
import logo_van as V
import van_a as A
DO, KEM = A.DO, A.KEM

def _glyph(ch):
    f, gs, cm, upm = V._f("xb"); n = cm[ord(ch)]
    bp = BoundsPen(gs); gs[n].draw(bp); pen = SVGPathPen(gs); gs[n].draw(pen)
    return pen.getCommands(), bp.bounds, gs, n

def _holes(ch, S=400):
    """Tâm lỗ (counter) của chữ – rasterize rồi tìm vùng nền không chạm biên."""
    from fontTools.pens.basePen import BasePen
    d, (x0, y0, x1, y1), gs, n = _glyph(ch); sc = (S - 40) / max(x1 - x0, y1 - y0)
    class P(BasePen):
        def __init__(s): super().__init__(gs); s.polys = []; s.cur = []
        def _moveTo(s, p): s.cur = [p]
        def _lineTo(s, p): s.cur.append(p)
        def _curveToOne(s, a, b, c):
            p0 = s.cur[-1]
            for t in np.linspace(0, 1, 12)[1:]:
                s.cur.append(tuple((1-t)**3*np.array(p0)+3*(1-t)**2*t*np.array(a)+3*(1-t)*t*t*np.array(b)+t**3*np.array(c)))
        def _qCurveToOne(s, a, b):
            p0 = s.cur[-1]
            for t in np.linspace(0, 1, 10)[1:]:
                s.cur.append(tuple((1-t)**2*np.array(p0)+2*(1-t)*t*np.array(a)+t*t*np.array(b)))
        def _closePath(s): s.polys.append(s.cur); s.cur = []
        _endPath = _closePath
    p = P(); gs[n].draw(p)
    im = Image.new("L", (S, S), 0); dr = ImageDraw.Draw(im)
    tf = lambda q: (20 + (q[0] - x0) * sc, S - 20 - (q[1] - y0) * sc)
    # nonzero xấp xỉ bằng XOR từng contour
    acc = np.zeros((S, S), bool)
    for poly in p.polys:
        m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).polygon([tf(q) for q in poly], fill=1); acc ^= np.array(m, bool)
    from scipy import ndimage
    lab, k = ndimage.label(~acc); out = []
    for i in range(1, k + 1):
        ys, xs = np.nonzero(lab == i)
        if xs.min() == 0 or ys.min() == 0 or xs.max() == S - 1 or ys.max() == S - 1: continue
        dt = ndimage.distance_transform_edt(lab == i); yy, xx = np.unravel_index(dt.argmax(), dt.shape)
        out.append(((xx - 20) / sc + x0, y0 + (S - 20 - yy) / sc, dt.max() / sc))
    return out

def glyph_mark(ch, cx, cy, H, c=DO, seed=5, step=None, idn="g"):
    """Chữ (font An Tâm) lấp đầy bằng đường vân đồng tâm quanh lỗ chữ; chấm tâm nằm trong lỗ."""
    d, (x0, y0, x1, y1), gs, n = _glyph(ch); s = H / (y1 - y0)
    tx, ty = cx - (x0 + x1) / 2 * s, cy + (y0 + y1) / 2 * s
    T = lambda X, Y: (tx + X * s, ty - Y * s)
    hx, hy, hr = max(_holes(ch), key=lambda h: h[2]); px, py = T(hx, hy); hr *= s
    clip = f'<clipPath id="{idn}"><path transform="translate({tx:.1f} {ty:.1f}) scale({s:.4f} {-s:.4f})" d="{d}"/></clipPath>'
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]
    step = step or H * .052; sw = step * .52; o = ""
    R = H * 1.3; i = 0; rad = hr * .95
    while rad < R:
        pts = []
        for k in range(181):
            a = k / 180 * 2 * math.pi
            wob = 1 + .05 * math.sin(3 * a + ph[0] + i * .1) + .03 * math.sin(5 * a + ph[1] + i * .23)
            pts.append((px + rad * wob * math.cos(a), py + rad * wob * math.sin(a) * 1.1))
        if i % 3 == 2:
            g0 = rr.randint(0, 170); gl = rr.randint(5, 10); pts = pts[g0 + gl:] + pts[1:g0]
        o += A._p(pts, c, sw); rad += step; i += 1
    dot = f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{min(hr * .62, H * .09):.1f}" fill="{c}"/>'
    return clip + f'<g clip-path="url(#{idn})">{o}</g>' + dot

def _seg_dist(x, y, a, b):
    ax, ay = a; bx, by = b; dx, dy = bx - ax, by - ay
    t = max(0, min(1, ((x - ax) * dx + (y - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(x - ax - t * dx, y - ay - t * dy)

def khac_A(cx, cy, r, c=DO, seed=5, rings=11):
    """Chữ A khắc âm bản: các đường vân đứt theo nét chữ A, chữ hiện ra bằng khoảng trống."""
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; sw = r * .052; o = ""
    top = (cx, cy - r * 1.35); L = (cx - r * .78, cy + r * 1.35); Rr = (cx + r * .78, cy + r * 1.35)
    by = cy + r * .42; bar = ((cx - r * .34, by), (cx + r * .34, by))
    gap = r * .095
    for i in range(3, rings + 1):
        pts, rad = A._ring(cx, cy, r, i, rings, ph)
        segs, cur = [], []
        for x, y in pts:
            dmin = min(_seg_dist(x, y, top, L), _seg_dist(x, y, top, Rr), _seg_dist(x, y, *bar))
            if dmin < gap: 
                if len(cur) > 1: segs.append(cur)
                cur = []
            else: cur.append((x, y))
        if len(cur) > 1: segs.append(cur)
        for sg in segs: o += A._p(sg, c, sw)
    return o + f'<circle cx="{cx:.1f}" cy="{cy - r * .05:.1f}" r="{r * .13:.1f}" fill="{c}"/>'

def mu_tach(cx, cy, r, c=DO, seed=5, rings=9):
    """Vân tay tròn + dấu mũ vòm vân tách rời phía trên – đọc thành â (như dấu mũ của font)."""
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; sw = r * .06; o = ""
    by = cy + r * .18; rb = r * .80
    for i in range(3, rings + 1):
        rad = rb * (i + .2) / (rings + .2); pts = []
        for k in range(181):
            a = k / 180 * 2 * math.pi
            wob = 1 + .04 * math.sin(3 * a + ph[0]) + .03 * math.sin(5 * a + ph[1] + i * .25)
            pts.append((cx + rad * wob * math.cos(a), by + rad * wob * math.sin(a) * 1.05))
        o += A._p(A._gap(pts, rr, i) if i > 3 else pts, c, sw)
    o += f'<circle cx="{cx:.1f}" cy="{by:.1f}" r="{r * .13:.1f}" fill="{c}"/>'
    ay = by - rb * 1.05 - r * .06                          # chân dấu mũ
    for j in range(3):
        w = r * (.42 + .16 * j); h = r * (.20 + .10 * j); y0 = ay - j * r * .02
        e = .2; f = lambda t: (math.sqrt(1 + e * e) - math.sqrt(t * t + e * e)) / (math.sqrt(1 + e * e) - e)
        pts = [(cx + w * t, y0 - h * f(t)) for t in np.linspace(-1, 1, 60)]
        o += A._p(pts, c, sw)
    return o

KINDS = [("khac-A", "B1 · Chữ A khắc trong vân", lambda cx, cy, r, c, u: khac_A(cx, cy, r, c)),
         ("mu-tach", "B2 · Dấu mũ tách – vân tay đội dấu mũ thành â", lambda cx, cy, r, c, u: mu_tach(cx, cy, r, c)),
         ("khuon-A", "B3 · Vân trong khuôn chữ A", lambda cx, cy, r, c, u: glyph_mark("A", cx, cy, r * 2.2, c, idn="kA" + u)),
         ("khuon-a", "B4 · Vân trong khuôn chữ a", lambda cx, cy, r, c, u: glyph_mark("a", cx, cy, r * 1.9, c, idn="ka" + u))]

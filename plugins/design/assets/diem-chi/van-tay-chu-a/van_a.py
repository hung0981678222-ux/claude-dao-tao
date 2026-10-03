"""Vân tay Điểm Chỉ có hình chữ a / A – các biến thể thương hiệu."""
import math, random
import logo_van as V
DO, KEM, MUC = "#D2141E", "#FFF6EA", "#231716"

def _ring(cx, cy, r, i, rings, ph, aspect=1.22, N=180):
    rad = r * (i + .2) / (rings + .2); pts = []
    for k in range(N + 1):
        a = k / N * 2 * math.pi - math.pi / 2          # bắt đầu từ đỉnh
        wob = 1 + .045 * math.sin(3 * a + ph[0]) + .03 * math.sin(5 * a + ph[1] + i * .25) + .02 * math.sin(2 * a + ph[2])
        pts.append((cx + rad * wob * math.cos(a), cy + rad * wob * math.sin(a) * aspect - r * .08 * (1 - i / rings)))
    return pts, rad

def _p(pts, c, sw):
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{c}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'

def _gap(pts, rr, i, keep_top=False):
    N = len(pts) - 1; gl = rr.randint(5, 14)
    g0 = rr.randint(N // 5, 4 * N // 5) if keep_top else rr.randint(0, N - 1)
    return [pts[(g0 + gl + j) % (N + 1)] for j in range(N - gl)]

def _peak(pts, cx, cy, rad, k, soft=.18):
    """Kéo phần trên thành đỉnh nhọn mềm (hình chữ A / vân lều)."""
    out = []
    for x, y in pts:
        if y < cy:
            dx = x - cx; t = max(0.0, 1 - math.sqrt(dx * dx + (soft * rad) ** 2) / (rad * 1.05))
            h = (cy - y) / (rad * 1.22)
            y -= k * rad * t ** 1.3 * h
            x = cx + dx * (1 - .10 * k * h)            # thu hẹp vai cho ra dáng A
        out.append((x, y))
    return out

def _a_core(cx, cy, r, c, sw, rb=None):
    """Chữ a một tầng quanh chấm tâm: thân tròn + nét đứng bên phải có đuôi."""
    rb = rb or r * .29; ry = rb * 1.08; o = ""
    # thân: cung tròn mở ở phía phải (nối với nét đứng)
    pts = [(cx + rb * math.cos(a), cy + ry * math.sin(a)) for a in [math.radians(d) for d in range(-60, 241, 4)]]
    pts = [(cx + rb * math.cos(math.radians(d)), cy + ry * math.sin(math.radians(d))) for d in range(-25, 286, 3)]
    o += _p(pts, c, sw)
    sx = cx + rb * 1.0
    o += _p([(sx, cy - ry * 1.0), (sx, cy + ry * .70)] + [(sx + rb * .30 * (1 - math.cos(t)), cy + ry * .70 + rb * .30 * math.sin(t)) for t in [j / 8 * math.pi / 2 for j in range(1, 9)]], c, sw)
    o += f'<circle cx="{cx - rb * .05:.1f}" cy="{cy:.1f}" r="{r * .10:.1f}" fill="{c}"/>'
    return o

def mark(kind, cx=0, cy=0, r=100, c=DO, seed=5, rings=11):
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; sw = r * .052; o = ""
    if kind == "goc":                                   # bản chuẩn 1.1 để so
        return V.van_tay(cx, cy, r, c)
    if kind in ("a-loi", "a-mu"):
        # vòng 1–3 nhường chỗ cho chữ a quanh chấm tâm
        for i in range(5, rings + 1):
            pts, rad = _ring(cx, cy, r, i, rings, ph)
            if kind == "a-mu":
                pts = _peak(pts, cx, cy - r * .05, rad, .30 + .045 * i)
            if i == 5:                                   # khe phải cho đuôi chữ a
                N = len(pts) - 1; o += _p(pts[int(N * .40):], c, sw) + _p(pts[:int(N * .22)], c, sw)
            else:
                o += _p(_gap(pts, rr, i, keep_top=kind == "a-mu"), c, sw)
        return o + _a_core(cx, cy - r * .05, r, c, sw * 1.75)
    if kind in ("A-leu", "A-nhe", "A-mo"):
        k0, kk = {"A-leu": (.30, .045), "A-nhe": (.12, .02), "A-mo": (.30, .045)}[kind]
        for i in range(3, rings + 1):
            pts, rad = _ring(cx, cy, r, i, rings, ph)
            pts = _peak(pts, cx, cy - r * .05, rad, k0 + kk * i)
            if kind == "A-mo" and i >= 3:               # mở ở chân giữa → hai chân chữ A
                N = len(pts) - 1; half = N // 2; w = int(N * (.05 + .012 * i))
                o += _p(pts[:half - w], c, sw) + _p(pts[half + w:], c, sw)
            else:
                o += _p(_gap(pts, rr, i, keep_top=True), c, sw)
        if kind == "A-mo":                              # nét ngang chữ A dưới chấm tâm
            y = cy + r * .24; o += _p([(cx - r * .17, y), (cx + r * .17, y)], c, sw)
        return o + f'<circle cx="{cx:.1f}" cy="{cy - r * .07:.1f}" r="{r * .13:.1f}" fill="{c}"/>'
    if kind == "a-long":                               # mọi vòng vân là chữ a lồng nhau
        for i in range(3, rings + 1):
            rad = r * (i + .2) / (rings + .2); ry = rad * 1.18; sx = cx + rad
            arc = [(cx + rad * math.cos(math.radians(d)) * (1 + .03 * math.sin(3 * math.radians(d) + ph[0] + i * .2)),
                    cy + ry * math.sin(math.radians(d))) for d in range(-35, 300, 3)]
            if rr.random() < .6 and i > 3:
                g = rr.randint(10, len(arc) - 25); arc1, arc2 = arc[:g], arc[g + rr.randint(4, 8):]
                o += _p(arc1, c, sw) + _p(arc2, c, sw)
            else:
                o += _p(arc, c, sw)
            o += _p([(sx, cy - ry * .95), (sx, cy + ry * .80), (sx + rad * .08, cy + ry * .98)], c, sw)
        return o + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * .13:.1f}" fill="{c}"/>'
    raise ValueError(kind)

KINDS = [("goc", "Bản chuẩn 1.1 (để so)"),
         ("a-loi", "a1 · Lõi chữ a – vòng quanh chấm tâm thành chữ a"),
         ("a-mu", "a2 · â của Tâm – lõi chữ a, vân vồng nhọn thành dấu mũ"),
         ("A-nhe", "A1 · Vân uốn nhẹ – đỉnh hơi nhọn, gợi chữ A"),
         ("A-leu", "A2 · Vân lều chữ A – đỉnh nhọn rõ (kiểu vân tay có thật)"),
         ("A-mo", "A3 · Chữ A mở chân – vân mở ở đáy thành hai chân, có nét ngang")]

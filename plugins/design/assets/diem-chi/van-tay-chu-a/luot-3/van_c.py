"""Vân tay Điểm Chỉ – lượt ý tưởng C: gắn với sản phẩm và câu chuyện hợp tác."""
import math, random
import van_a as A
DO, KEM = A.DO, A.KEM
P = A._p

def _oval(cx, cy, rx, ry, rot, ph, i, N=160):
    c, s = math.cos(rot), math.sin(rot); pts = []
    for k in range(N + 1):
        a = k / N * 2 * math.pi
        w = 1 + .04 * math.sin(3 * a + ph[0] + i * .1) + .025 * math.sin(5 * a + ph[1] + i * .2)
        x, y = rx * w * math.cos(a), ry * w * math.sin(a)
        pts.append((cx + x * c - y * s, cy + x * s + y * c))
    return pts

def hai_dau(cx, cy, r, c=DO, seed=7):
    """Hai dấu điểm chỉ nghiêng chụm đầu thành chữ A – hai bên cùng cam kết; chấm tâm ở giữa."""
    rr = random.Random(seed); sw = r * .055; o = ""
    for side in (-1, 1):
        ph = [rr.uniform(0, 6.28) for _ in range(3)]
        ox, oy, rot = cx + side * r * .50, cy + r * .10, side * math.radians(-17)
        for i in range(1, 8):
            k = (i + .3) / 7.3; pts = _oval(ox, oy, r * .40 * k, r * .95 * k, rot, ph, i)
            if i > 1:
                g0 = rr.randint(0, 150); gl = rr.randint(5, 12); pts = pts[g0 + gl:] + pts[1:g0]
            o += P(pts, c, sw)
    # nét ngang chữ A + chấm tâm ở lòng chữ
    o += f'<circle cx="{cx:.1f}" cy="{cy + r * .52:.1f}" r="{r * .12:.1f}" fill="{c}"/>'
    return o

def xoay_cuon(cx, cy, r, c=DO, seed=5):
    """Vân xoáy một nét từ chấm tâm – như mặt cắt cuộn bánh kebab/tortilla cuộn."""
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; sw = r * .055
    turns = 8.2; pts = []; r0 = r * .20
    for k in range(int(turns * 120)):
        t = k / 120 * 2 * math.pi; rad = r0 + (r * .98 - r0) * t / (turns * 2 * math.pi)
        w = 1 + .04 * math.sin(3 * t + ph[0]) + .025 * math.sin(5 * t + ph[1])
        pts.append((cx + rad * w * math.cos(t), cy + rad * w * math.sin(t) * 1.16))
    # vài chỗ đứt như vân thật
    o = ""; cuts = sorted(rr.sample(range(200, len(pts) - 60), 5)); last = 0
    for cu in cuts:
        o += P(pts[last:cu], c, sw); last = cu + rr.randint(6, 12)
    o += P(pts[last:], c, sw)
    return o + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * .13:.1f}" fill="{c}"/>'

def vo_taco(cx, cy, r, c=DO, seed=5, n=9):
    """Dấu vân tay gập đôi thành vỏ taco (∪); chấm tâm là nhân bánh ở miệng vỏ."""
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; sw = r * .058; o = ""
    top = cy - r * .30
    for i in range(1, n + 1):
        rad = r * (i + .6) / (n + .6); pts = []
        for k in range(91):
            a = math.pi * k / 90
            w = 1 + .035 * math.sin(3 * a + ph[0] + i * .2) + .02 * math.sin(6 * a + ph[1])
            pts.append((cx + rad * 1.06 * w * math.cos(a), top + rad * 1.05 * w * math.sin(a)))
        if i > 2 and rr.random() < .55:
            g = rr.randint(15, 70); gl = rr.randint(4, 8); o += P(pts[:g], c, sw) + P(pts[g + gl:], c, sw)
        else:
            o += P(pts, c, sw)
    return o + f'<circle cx="{cx:.1f}" cy="{top - r * .02:.1f}" r="{r * .15:.1f}" fill="{c}"/>'

def banh_tron(cx, cy, r, c=DO, seed=5):
    """Vỏ bánh tortilla tròn (vành viền) – trong lòng là vân tay chữ A (vân lều); chấm tâm ở giữa."""
    o = f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{c}" stroke-width="{r * .075:.1f}"/>'
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; sw = r * .05
    clip = f"bt{abs(hash((cx, cy, r))) % 99999}"
    inner = ""
    for i in range(2, 11):
        pts, rad = A._ring(cx, cy + r * .12, r * .70, i, 10, ph, aspect=1.0)
        pts = A._peak(pts, cx, cy, rad, .45 + .07 * i)
        inner += P(A._gap(pts, rr, i, keep_top=True), c, sw)
    o += f'<clipPath id="{clip}"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * .86:.1f}"/></clipPath><g clip-path="url(#{clip})">{inner}</g>'
    return o + f'<circle cx="{cx:.1f}" cy="{cy - r * .02:.1f}" r="{r * .11:.1f}" fill="{c}"/>'

KINDS = [("hai-dau", "C1 · Hai dấu chụm thành chữ A", hai_dau),
         ("xoay-cuon", "C2 · Vân xoáy cuộn bánh", xoay_cuon),
         ("vo-taco", "C3 · Dấu gập vỏ taco", vo_taco),
         ("banh-tron", "C4 · Vân lều trong vỏ bánh tròn", banh_tron)]

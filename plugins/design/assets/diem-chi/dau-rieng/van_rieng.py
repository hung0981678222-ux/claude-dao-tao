"""Giữ nguyên dấu vân tay Điểm Chỉ (cùng thuật toán, cùng seed với logo_van.van_tay) và lồng chi tiết riêng An Tâm.
lõi: None | "A" (lõi vân thành chữ A) | "tam" (chấm tâm) ; mu: nhấc 3 vân trên cùng thành dấu mũ ^ như font ;
duoi: vân ngoài cùng kéo thành nét ký tên.
"""
import math
import random

import build_chuan as C

V = C.V
DO, KEM = V.DO, V.KEM


def _seg(pts, color, sw):
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{color}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'


def van(cx=0, cy=0, r=84, color=DO, seed=5, rings=11, aspect=1.15, loi=None, mu=False, duoi=False):
    rr = random.Random(seed); sw = r * .052; out = []
    ph = [rr.uniform(0, 6.28) for _ in range(3)]
    skip = {"A": 3, "tam": 2}.get(loi, 0)
    lift = r * .2
    for i in range(1, rings + 1):
        rad = r * (i + .2) / (rings + .2)
        N = 120; pts = []
        for k in range(N + 1):
            a = k / N * 2 * math.pi
            wob = 1 + .045 * math.sin(3 * a + ph[0]) + .03 * math.sin(5 * a + ph[1] + i * .25) + .02 * math.sin(2 * a + ph[2])
            pts.append((cx + rad * wob * math.cos(a), cy + rad * wob * math.sin(a) * aspect - r * .08 * (1 - i / rings), a))
        g0 = rr.randint(0, N - 1); gl = rr.randint(4, 12) if i > 1 else 0
        if i <= skip:
            continue
        seg = [pts[(g0 + gl + j) % (N + 1)] for j in range(N - gl)]
        top = mu and i > rings - 3
        if top:
            # tách phần vân phía trên (góc 205°–335°) và nhấc lên thành dấu mũ
            lo, hi = math.radians(222), math.radians(318)
            body = [p for p in pts if not (lo <= p[2] <= hi)]
            # sắp lại để liền mạch từ 328° vòng xuống tới 212°
            body = sorted(body, key=lambda p: (p[2] - hi) % (2 * math.pi))
            body = body[2:-2]
            cap = [(x, y - lift) for x, y, a in pts if lo + .06 <= a <= hi - .06]
            out.append(_seg([(x, y) for x, y, _ in body], color, sw))
            out.append(_seg(cap, color, sw * 1.08))
            continue
        if duoi and i == rings:
            # mở vân ngoài ở góc dưới phải, kéo ra thành nét ký
            seg2 = sorted(pts, key=lambda p: (p[2] - math.radians(70)) % (2 * math.pi))[8:]
            xs, ys, _ = seg2[0]
            tail = [(xs + t * r * 1.15, ys + r * .10 * math.sin(t * 2.2) + t * t * r * .06) for t in [j / 24 for j in range(25)]]
            out.append(_seg([(x, y) for x, y, _ in reversed(seg2)] + tail, color, sw))
            continue
        out.append(_seg([(x, y) for x, y, _ in seg], color, sw))
    if loi == "A":
        rad = r * 3.6 / (rings + .2)
        h = rad * 1.9; b = rad * 1.15
        out.append(_seg([(cx - b, cy + h * .55), (cx, cy - h * .6), (cx + b, cy + h * .55)], color, sw))
        out.append(_seg([(cx - b * .45, cy + h * .12), (cx + b * .45, cy + h * .12)], color, sw))
    if loi == "tam":
        out.append(f'<circle cx="{cx}" cy="{cy - r * .07:.1f}" r="{r * .13:.1f}" fill="{color}"/>')
    return "".join(out)


BIEN_THE = [
    ("goc", "Gốc (đang dùng)", {}),
    ("loi-a", "1 · Lõi chữ A", {"loi": "A"}),
    ("mu-van", "2 · Mũ vân", {"mu": True}),
    ("cham-tam", "3 · Chấm tâm", {"loi": "tam"}),
    ("mu-a", "4 · Mũ vân + lõi A", {"mu": True, "loi": "A"}),
    ("mu-tam", "5 · Mũ vân + chấm tâm", {"mu": True, "loi": "tam"}),
]


def svg(body, size=200, label="Biểu tượng"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-150 -125 300 250" width="{size}" height="{size * 250 / 300:.0f}" role="img" aria-label="{label}">{body}</svg>'

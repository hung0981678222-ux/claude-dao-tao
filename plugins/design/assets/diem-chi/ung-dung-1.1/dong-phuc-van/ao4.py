"""Đồng phục An Tâm – đường vân cách điệu (áo thun nhân viên, áo văn phòng, tạp dề)."""
import math
import random

import ao2 as A
import ao3 as G

V = A.V
DO, DO2, KEM, MUC, NGO, TRANG = A.DO, A.DO2, A.KEM, A.MUC, A.NGO, A.TRANG
SON = V.SON
W, fit, mark, _P = A.W, A.fit, A.mark, A.P if hasattr(A, "P") else A._P


def _pl(pts, c, sw, op=1):
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-opacity="{op}"/>'


def gon(cx, cy, n=8, step=9, c=DO, sw=2.6, op_end=.15, seed=5, gap=True, start=4, aspect=1.15):
    """Vân lan: vòng vân lượn sóng toả ra từ chấm tâm, nhạt dần."""
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; o = f'<circle cx="{cx}" cy="{cy}" r="{step * .55}" fill="{c}"/>'
    for i in range(n):
        rad = start + step * (i + 1)
        pts = []
        for k in range(181):
            a = k / 180 * 2 * math.pi
            wob = 1 + .045 * math.sin(3 * a + ph[0] + i * .12) + .03 * math.sin(5 * a + ph[1] + i * .25)
            pts.append((cx + rad * wob * math.cos(a), cy + rad * wob * math.sin(a) * aspect))
        if gap and i:
            g0 = rr.randint(0, 170); gl = rr.randint(6, 16)
            pts = pts[g0 + gl:] + pts[1:g0]
        op = 1 - (1 - op_end) * i / max(1, n - 1)
        o += _pl(pts, c, sw, op)
    return o


def soc(x0, x1, y0, y1, px, py, R, c, sw=2.4, step=11, core=True):
    """Sọc vân: sọc dọc uốn quanh một lõi (chấm tâm) như dòng vân tay chảy quanh tâm."""
    o = ""
    k = -int((px - x0) / step) - 1
    while px + k * step < x1 + step:
        cval = k * step + step / 2
        pts = []
        for yy in range(int(y0), int(y1) + 4, 4):
            dy = yy - py
            pts.append((px + cval * (1 + R * R / (cval * cval + dy * dy * .7 + 1)), yy))
        o += _pl(pts, c, sw)
        k += 1
    if core:
        for i, r in enumerate((R * .55, R * .85)):
            o += f'<ellipse cx="{px}" cy="{py}" rx="{r}" ry="{r * 1.15}" fill="none" stroke="{c}" stroke-width="{sw}"/>'
        o += f'<circle cx="{px}" cy="{py}" r="{R * .26}" fill="{DO if c != DO else KEM}"/>'
    return o


def dong(x, y, w, h, c, sw=2.4, step=10, amp=26, op_top=0.0):
    """Vân dòng chảy: đường vân nằm ngang lượn sóng, đậm dần xuống dưới."""
    o = ""; n = int(h / step) + 2
    for i in range(n):
        y0 = y + i * step; pts = []
        for xx in range(int(x) - 10, int(x + w) + 14, 8):
            pts.append((xx, y0 + amp * math.sin((xx - x) / 120 + i * .09) + amp * .45 * math.sin((xx - x) / 47 + i * .2)))
        op = op_top + (1 - op_top) * i / max(1, n - 1)
        o += _pl(pts, c, sw, op)
    return o


def vom(cx, cy, n, c, sw=2.6, step=11, w0=20):
    """Vân vòm: các vòm vân (dạng vân cung) lồng nhau."""
    o = ""
    for i in range(n):
        a = w0 + i * step * 1.5; h = 10 + i * step
        pts = [(cx + a * t, cy - h * max(0.0, 1 - t * t) ** .6) for t in [-1 + 2 * j / 80 for j in range(81)]]
        o += _pl(pts, c, sw)
    return o


# ───────── ghép bộ
def _ten(cx, cy, c, size=12):
    return W("An Tâm", size, cx, cy, c, "xb", "middle")


def bo_1():
    u = "v1"; ts = .95
    t = G.garm(190, 290, ts, KEM, u, "t", A.TEE, gon(190 + 52, 290 - 96, 16, 11, DO, 2.6, .08)) + A._co_tron(190, 290, ts, DO)
    t += _ten(190 + 52, 290 - 50, DO, 13)
    p = G.garm(540, 290, ts, TRANG, u, "p", A.POLO, gon(540 + 52, 290 - 90, 9, 8, DO, 1.8, .1)) + G.collar_polo(540, 290, ts, DO, u)
    p += _ten(540 + 52, 290 - 50, DO, 11)
    a = G.tie(890, 300, .9, KEM) + G.garm(890, 300, .9, DO, u, "a", G.APRON, gon(890, 300 - 110, 22, 10, KEM, 2.8, .1), seams=False) + G.stitch(890, 300, .9, KEM)
    a += W("An Tâm", 26, 890, 300 + 20, KEM, "xb", "middle") + W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 + 44, KEM, "md", "middle")
    return G.bang("Vân 1 · Vân lan", "Vòng vân toả ra từ chấm tâm ở ngực, nhạt dần như vết son loang – áo trông như vừa được điểm chỉ.", t + p + a, u)


def bo_2():
    u = "v2"; ts = .95
    t = G.garm(190, 290, ts, DO, u, "t", A.TEE, soc(20, 360, 120, 470, 190 + 52, 290 - 90, 20, DO2, 2.6, 12)) + A._co_tron(190, 290, ts, DO2)
    t += W("An Tâm", 22, 190, 290 + 70, KEM, "xb", "middle") if False else ""
    t += _ten(190 + 52, 290 - 46, KEM, 13)
    p = G.garm(540, 290, ts, TRANG, u, "p", A.POLO, soc(370, 710, 130, 470, 540 + 52, 290 - 88, 14, "#F0B9B4", 1.6, 10, core=False)) + G.collar_polo(540, 290, ts, DO, u)
    p += f'<circle cx="{540 + 52}" cy="{290 - 88}" r="10" fill="{DO}"/>' + _ten(540 + 52, 290 - 60, DO, 11)
    a = G.tie(890, 300, .9, KEM) + G.garm(890, 300, .9, MUC, u, "a", G.APRON, soc(740, 1040, 60, 520, 890, 300 - 100, 24, "#4a3834", 2.6, 12), seams=False) + G.stitch(890, 300, .9, KEM)
    a += W("An Tâm", 26, 890, 300 - 30, KEM, "xb", "middle") + W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 - 6, KEM, "md", "middle")
    return G.bang("Vân 2 · Sọc vân", "Sọc dọc như vải áo sơ mi, nhưng uốn cong quanh chấm tâm ở ngực – đúng cách vân tay chảy quanh lõi. Kín đáo, lịch sự.", t + p + a, u)


def bo_3():
    u = "v3"; ts = .95
    t = G.garm(190, 290, ts, KEM, u, "t", A.TEE, dong(20, 300, 360, 170, DO, 3, 11, 20, .3)) + A._co_tron(190, 290, ts, DO)
    t += mark(190 + 52, 290 - 96, 15, DO) + _ten(190 + 52, 290 - 66, DO, 12)
    p = G.garm(540, 290, ts, MUC, u, "p", A.POLO, dong(370, 330, 340, 140, DO, 2.6, 11, 16, .35)) + G.collar_polo(540, 290, ts, MUC, u)
    p += fit(V.logo_ngang(KEM, KEM), 540 + 54 * ts, 290 - 82 * ts, w=64 * ts)
    a = G.tie(890, 300, .9, DO) + G.garm(890, 300, .9, KEM, u, "a", G.APRON, dong(740, 330, 300, 200, DO, 3, 11, 22, .3), seams=False) + G.stitch(890, 300, .9, DO)
    a += mark(890, 300 - 120, 26, DO) + W("An Tâm", 26, 890, 300 - 52, DO, "xb", "middle") + W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 - 26, MUC, "md", "middle")
    return G.bang("Vân 3 · Dòng chảy", "Đường vân nằm ngang dâng lên từ gấu áo, đậm dưới – nhạt trên, như bột chảy, như sóng – ấm, mềm.", t + p + a, u)


def bo_4():
    u = "v4"; ts = .95
    t = G.garm(190, 290, ts, DO, u, "t", A.TEE, vom(190, 422, 13, DO2, 3, 12)) + A._co_tron(190, 290, ts, DO2)
    t += f'<circle cx="190" cy="{422 - 6}" r="9" fill="{KEM}"/>' + mark(190 + 52, 290 - 96, 15, KEM) + _ten(190 + 52, 290 - 66, KEM, 12)
    p = G.garm(540, 290, ts, KEM, u, "p", A.POLO, vom(540, 422, 9, DO, 2.2, 11)) + G.collar_polo(540, 290, ts, DO, u)
    p += f'<circle cx="540" cy="{422 - 6}" r="7" fill="{DO}"/>' + fit(V.logo_ngang(), 540 + 54 * ts, 290 - 82 * ts, w=64 * ts)
    a = G.tie(890, 300, .9, MUC) + G.garm(890, 300, .9, DO, u, "a", G.APRON, vom(890, 488, 14, DO2, 3, 12), seams=False) + G.stitch(890, 300, .9, KEM)
    a += f'<circle cx="890" cy="{488 - 6}" r="9" fill="{KEM}"/>' + mark(890, 300 - 120, 26, KEM) + W("An Tâm", 26, 890, 300 - 52, KEM, "xb", "middle")
    a += W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 - 26, KEM, "md", "middle")
    return G.bang("Vân 4 · Vân vòm", "Các vòm vân lồng nhau mọc lên từ gấu, đỉnh là một chấm son – như mặt trời mọc, như ổ bánh vừa phồng trong lò.", t + p + a, u)


BO = [("van-1-van-lan", bo_1), ("van-2-soc-van", bo_2), ("van-3-dong-chay", bo_3), ("van-4-van-vom", bo_4)]

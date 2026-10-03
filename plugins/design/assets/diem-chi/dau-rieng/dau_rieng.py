"""Biểu tượng Điểm Chỉ – các hướng làm dấu vân tay mang dấu riêng An Tâm.
Mỗi hàm trả về phần thân SVG trong hộp (-100,-100)–(100,100), tâm (0,0).
"""
import math
import random

import build_chuan as C

V = C.V
DO, DO2, SON, KEM, MUC, NGO = V.DO, V.DO2, V.SON, V.KEM, V.MUC, V.NGO


def _path(pts):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def _cat(pts, rr, n_gap=1, gap=(3, 7)):
    """Cắt một đường vân thành vài đoạn (vân thật có chỗ đứt)."""
    out, i = [], 0
    cuts = sorted(rr.sample(range(8, max(9, len(pts) - 8)), min(n_gap, max(0, len(pts) - 16)))) if len(pts) > 20 else []
    for c in cuts:
        out.append(pts[i:c]); i = c + rr.randint(*gap)
    out.append(pts[i:])
    return [p for p in out if len(p) > 2]


def _stroke(paths, color, w):
    return "".join(f'<path d="{_path(p)}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>' for p in paths)


# 1 ─ Vân mái lều = chữ A (tented arch là một dạng vân tay thật)
def mai_leu(color=DO, w=7.0, seed=3):
    """Các đường vân dạng mái lều lồng nhau, đỉnh nhọn ở giữa – đọc ra chữ A; cắt trong dáng đầu ngón tay."""
    rr = random.Random(seed)
    clip = '<clipPath id="ml"><ellipse cx="0" cy="4" rx="84" ry="100"/></clipPath>'
    s = ""
    sl, gap = 1.35, 12.5
    step = gap * math.sqrt(1 + sl * sl)
    for k in range(7):
        top = -6 - k * step
        rho = 2 + k * 7.5                    # lớp ngoài đỉnh tròn dần như vân thật
        pts = []
        for i in range(161):
            x = -130 + 260 * i / 160
            y = top + sl * (math.sqrt(x * x + rho * rho) - rho) - 0.0009 * k * x * x
            pts.append((x, y))
        pts = [q for q in pts if (q[0] / 80) ** 2 + ((q[1] - 4) / 96) ** 2 <= 1]
        s += _stroke(_cat(pts, rr, 1 if k > 0 else 0, (3, 5)), color, w)
    # chữ A ở lõi: vạch ngang
    s += _stroke([[(-14, 30), (14, 30)]], color, w)
    for j, y in enumerate((80, 95)):
        pts = [(x, y + 3 * math.sin(x / 20 + j)) for x in range(-90, 91, 2)]
        pts = [q for q in pts if (q[0] / 80) ** 2 + ((q[1] - 4) / 96) ** 2 <= 1]
        s += _stroke(_cat(pts, rr, 1, (4, 6)), color, w)
    return s


# 2 ─ Vân cuộn = mặt cắt cuốn bánh (vân xoáy chính là lát cắt của một cuốn tortilla)
def van_cuon(color=DO, w=7.0, seed=8):
    rr = random.Random(seed); pts = []
    turns, r0, r1 = 4.6, 6, 80
    N = 520
    for i in range(N + 1):
        t = i / N
        th = t * turns * 2 * math.pi
        r = r0 + (r1 - r0) * t
        wob = 1 + 0.035 * math.sin(3 * th + 0.6)
        pts.append((r * wob * math.cos(th) * 1.0, r * wob * math.sin(th) * 1.12))
    # mép bánh: đuôi cuốn duỗi ra tiếp tuyến
    x, y = pts[-1]; px, py = pts[-6]
    dx, dy = x - px, y - py; L = math.hypot(dx, dy)
    for k in range(1, 9):
        pts.append((x + dx / L * k * 5, y + dy / L * k * 5 + k * k * 0.25))
    s = _stroke(_cat(pts, rr, 3, (5, 9)), color, w)
    return s


# 3 ─ Dấu mũ vân: chữ "â" của font An Tâm Tròn Bánh – dấu mũ là 3 đường vân tay
def dau_mu(color=DO, bg=KEM):
    s = f'<circle r="96" fill="{color}"/>'
    g, w = V.text("â", 190, "xb", 0, 0, bg, "middle")
    # căn giữa theo chiều cao chữ (x-height + dấu mũ)
    s += g.replace('<g fill', '<g transform="translate(0 58)"><g fill', 1) + "</g>"
    return s


# 4 ─ Bánh điểm chỉ: vân tay son ấn lên mặt bánh tortilla
def banh_diem_chi(color=DO, seed=4):
    rr = random.Random(seed)
    edge = []
    for i in range(121):
        a = i / 120 * 2 * math.pi
        r = 92 * (1 + 0.025 * math.sin(5 * a + 1) + 0.015 * math.sin(11 * a))
        edge.append((r * math.cos(a), r * math.sin(a)))
    s = f'<path d="{_path(edge)}Z" fill="#F3DDB0"/>'
    for _ in range(26):
        a = rr.uniform(0, 6.28); d = rr.uniform(20, 84)
        s += f'<ellipse cx="{d * math.cos(a):.1f}" cy="{d * math.sin(a):.1f}" rx="{rr.uniform(2, 5):.1f}" ry="{rr.uniform(1.5, 3.5):.1f}" fill="#C98F4E" opacity=".55"/>'
    s += V.van_tay(0, 0, 54, color, seed=5, rings=9, sw=4.6, aspect=1.18)
    return s


def hien_tai(color=DO):
    return V.van_tay(0, 0, 84, color, seed=5, rings=11, aspect=1.15)


def svg(body, size=200, bg=None, label="Biểu tượng"):
    r = f'<rect x="-110" y="-110" width="220" height="220" rx="36" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-110 -110 220 220" width="{size}" height="{size}" role="img" aria-label="{label}">{r}{body}</svg>'


def _nested(shape, n, color, w, rr, s0=0.18, gaps=1, inside=None):
    """Vẽ n đường vân lồng nhau theo hàm shape(scale) -> list điểm."""
    out = ""
    for k in range(n):
        sc = s0 + (1 - s0) * k / (n - 1)
        pts = shape(sc)
        if inside:
            pts = [q for q in pts if inside(q)]
        out += _stroke(_cat(pts, rr, gaps if k > 1 else 0, (3, 6)), color, w)
    return out


# 5 ─ Vân hạt lúa mì: đầu ngón tay thành hạt lúa mì – bánh làm từ bột mì
def hat_lua_mi(color=DO, w=6.4, seed=6):
    rr = random.Random(seed)

    def lens(sc):
        pts = []
        for i in range(161):
            t = -1 + 2 * i / 160
            y = 96 * sc * t
            x = 70 * sc * (1 - t * t) ** 0.72 * (1 + 0.04 * math.sin(4 * t))
            pts.append((x, y))
        return pts + [(-x, y) for x, y in reversed(pts)]
    s = _nested(lens, 7, color, w, rr, 0.16)
    s += _stroke([[(0, -78), (0, 78)]], color, w * 0.8).replace('stroke-width', 'stroke-dasharray="1 14" stroke-width') if False else ""
    return s


# 6 ─ Giọt son: dấu vân tay trong dáng giọt mực son, đỉnh nhọn như chữ A
def giot_son(color=DO, w=6.4, seed=9):
    rr = random.Random(seed)

    def drop(sc):
        pts = []
        for i in range(201):
            t = 2 * math.pi * i / 200
            x = 74 * math.sin(t) * math.sin(t / 2) ** 0.9
            y = -96 * math.cos(t)
            pts.append((x * sc, y * sc + 30 * (1 - sc)))
        return pts
    s = _nested(drop, 8, color, w, rr, 0.12)
    return f'<g transform="translate(0 -6)">{s}</g>'


# 7 ─ Vân AT: vân mái lều bên ngoài (A), lõi vân là chữ T (Tâm)
def van_at(color=DO, w=6.6, seed=4):
    rr = random.Random(seed); s = ""
    sl, gap = 1.25, 12.5
    step = gap * math.sqrt(1 + sl * sl)
    for k in range(6):
        top = -20 - k * step; rho = 4 + k * 8
        pts = [(x, top + sl * (math.sqrt(x * x + rho * rho) - rho) - 0.0009 * k * x * x) for x in [-130 + 260 * i / 160 for i in range(161)]]
        pts = [q for q in pts if (q[0] / 80) ** 2 + ((q[1] - 4) / 96) ** 2 <= 1]
        s += _stroke(_cat(pts, rr, 1 if k else 0, (3, 5)), color, w)
    s += _stroke([[(-16, 6), (16, 6)], [(0, 6), (0, 44)]], color, w)          # chữ T ở lõi
    for j, y in enumerate((82, 96)):
        pts = [(x, y + 3 * math.sin(x / 20 + j)) for x in range(-90, 91, 2)]
        pts = [q for q in pts if (q[0] / 80) ** 2 + ((q[1] - 4) / 96) ** 2 <= 1]
        s += _stroke(_cat(pts, rr, 1, (4, 6)), color, w)
    return s


# 8 ─ Mới ra lò: nửa dưới là vân tay, phía trên ba làn hơi nóng (cũng là ba vân của dấu mũ)
def moi_ra_lo(color=DO, w=6.6, seed=2):
    rr = random.Random(seed); s = ""
    for k in range(6):
        r = 22 + k * 13
        pts = [(r * math.cos(a), 30 + r * 0.95 * math.sin(a)) for a in [math.pi * (0.02 + 0.96 * i / 80) for i in range(81)]]
        s += _stroke(_cat(pts, rr, 1 if k > 1 else 0, (3, 5)), color, w)
    s += _stroke([[(-10, 30), (10, 30)]], color, w)
    for j, x0 in enumerate((-30, 0, 30)):
        pts = [(x0 + 7 * math.sin(y / 11 + j), y) for y in range(-92, 6, 2)]
        s += _stroke([pts], color, w)
    return s


# 9 ─ Ấn Â: chữ Â hoa của font riêng trong vòng vân tay
def an_a(color=DO, w=6, seed=7):
    rr = random.Random(seed); s = ""
    for k, r in enumerate((86, 98)):
        pts = [(r * 0.86 * math.cos(a), r * math.sin(a)) for a in [2 * math.pi * i / 160 for i in range(161)]]
        s += _stroke(_cat(pts, rr, 2, (5, 9)), color, w)
    g, _ = V.text("Â", 150, "xb", 0, 0, color, "middle")
    s += g.replace('<g fill', '<g transform="translate(0 48)"><g fill', 1) + "</g>"
    return s

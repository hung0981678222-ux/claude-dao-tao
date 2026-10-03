"""Vân tay Điểm Chỉ – lượt G: thêm ý tưởng công nghiệp, dựng hình học."""
import math
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union
import van_f as F
DO, KEM, MUC, VANG = F.DO, F.KEM, F.MUC, F.VANG
_d, _stroke, _arc = F._d, F._stroke, F._arcpts
def P(g, c): return f'<path fill="{c}" fill-rule="evenodd" d="{_d(g)}"/>'

def chu_A(cx, cy, R, n=5):
    """Vân lều dựng hình: vân ngoài là đường bao đều quanh chữ Λ, vân trong là chữ A thu nhỏ dần;
    chân cắt thẳng ở đáy, lòng chữ A có nét ngang và chấm tâm."""
    g = R / (n + 2.4); w = g * .5; base = cy + R * .80; apy = cy - R * .30
    tri = Polygon([(cx - R * .36, base + g * 3), (cx, apy), (cx + R * .36, base + g * 3)])
    clipb = box(cx - 3 * R, cy - 3 * R, cx + 3 * R, base - g * .25)
    parts = []
    for i in range(n):                                    # vân bao ngoài
        ring = tri.buffer(g * (i + .5), join_style=1, resolution=32).exterior
        sh = _stroke(ring, w, 2).intersection(clipb)
        if i in (1, 3):
            ang = 32 if i == 1 else 148
            cut = LineString([(cx, cy), (cx + 3 * R * math.cos(math.radians(ang)), cy - 3 * R * math.sin(math.radians(ang)))]).buffer(g * .3)
            sh = sh.difference(cut)
        parts.append(sh)
    for j in range(1):                                    # vân trong lòng chữ A
        inner = tri.buffer(-g * (j + .5), join_style=1, resolution=32)
        if inner.is_empty: break
        parts.append(_stroke(inner.exterior, w, 2).intersection(box(cx - 3 * R, cy - 3 * R, cx + 3 * R, base - g * .25)))
    yb = cy + R * .40
    hw = (R * .36) * (yb - apy) / (base + g * 3 - apy) - g * 2.1
    if False: parts.append(_stroke(LineString([(cx - hw, yb), (cx + hw, yb)]), w, 2))
    dot = Point(cx, cy + R * .36).buffer(g * .62, resolution=32)
    return P(unary_union(parts), "{c}") + P(dot, "{c}")

def _squircle(cx, cy, rx, ry, n=4.0, m=120):
    pts = []
    for k in range(m + 1):
        t = 2 * math.pi * k / m; ct, st = math.cos(t), math.sin(t)
        pts.append((cx + rx * math.copysign(abs(ct) ** (2 / n), ct), cy + ry * math.copysign(abs(st) ** (2 / n), st)))
    return pts

def vuong_bo(cx, cy, R, n=7):
    """Vân vuông bo (squircle): vòng vân dạng vuông bo hiện đại, lõi vân móc; như biểu tượng công nghệ."""
    g = R / (n + .3); w = g * .5; parts = []; top = cy - R * .12
    for i in range(n):
        r = g * (i + .85)
        if i < 2:
            leg = g * (2.6 - .3 * i)
            pts = [(cx - r, top + leg)] + _arc(cx, top, r, 180, 0) + [(cx + r, top + leg)]
            parts.append(_stroke(LineString(pts), w, 2))
        else:
            pts = _squircle(cx, cy + R * .05, r * 1.0, r * 1.02, 4.2)
            sh = _stroke(LineString(pts), w, 2)
            ang = [-45, 210, -70, 235, -25][i % 5]
            cut = LineString([(cx, cy), (cx + 3 * R * math.cos(math.radians(ang)), cy - 3 * R * math.sin(math.radians(ang)))]).buffer(g * .3)
            parts.append(sh.difference(cut))
    dot = Point(cx, top).buffer(g * .52, resolution=32)
    return P(unary_union(parts), "{c}") + P(dot, "{c}")

def ma_vach(cx, cy, R, n=7):
    """Vân truy xuất: vòm vân phía trên, chân vân thả xuống thành vạch mã vạch dày mỏng –
    mỗi mẻ bánh truy xuất được nguồn gốc như dấu vân tay."""
    g = R / (n + .2); parts = []; top = cy - R * .25; base = cy + R * .85
    ws = [.50, .32, .62, .40, .55, .30, .58]
    for i in range(n):
        r = g * (i + .8); w = g * ws[i]
        arc = _stroke(LineString(_arc(cx, top, r, 0, 180, 80)), g * .5, 2)
        lw = g * ws[i]; rw = g * ws[(i + 3) % n]
        L = box(cx - r - lw / 2, top, cx - r + lw / 2, base - (g * .9 if i % 3 == 1 else 0))
        Rr = box(cx + r - rw / 2, top, cx + r + rw / 2, base - (g * .9 if i % 3 == 2 else 0))
        parts += [arc, L, Rr]
    dot = Point(cx, top).buffer(g * .5, resolution=32)
    return P(unary_union(parts), "{c}") + P(dot, "{c}")

def kiem_dinh(cx, cy, R, n=6):
    """Dấu kiểm định: vân tay tròn đồng tâm trong vòng thước đo có vạch chia – chính xác, kiểm soát chất lượng."""
    g = R * .78 / (n + .3); w = g * .5; parts = []
    for i in range(1, n + 1):
        r = g * (i + .4)
        sh = _stroke(LineString(_arc(cx, cy, r, 0, 360, 120)), w, 2)
        ang = [30, 200, 75, 250, 140, 320][i % 6]
        cut = LineString([(cx, cy), (cx + 3 * R * math.cos(math.radians(ang)), cy - 3 * R * math.sin(math.radians(ang)))]).buffer(g * .32)
        parts.append(sh.difference(cut))
    outer = Point(cx, cy).buffer(R * 1.0, resolution=64).difference(Point(cx, cy).buffer(R * .93, resolution=64))
    ticks = []
    for k in range(60):
        a = math.radians(k * 6); L = R * (.84 if k % 5 == 0 else .88)
        ticks.append(_stroke(LineString([(cx + L * math.cos(a), cy + L * math.sin(a)), (cx + R * .905 * math.cos(a), cy + R * .905 * math.sin(a))]), R * (.022 if k % 5 == 0 else .012), 2))
    dot = Point(cx, cy).buffer(g * .55, resolution=32)
    return P(unary_union(parts + [outer] + ticks), "{c}") + P(dot, "{c}")

FN = {"G1": chu_A, "G2": vuong_bo, "G3": ma_vach, "G4": kiem_dinh}
def mark(kind, cx=0, cy=0, R=100, c=DO, bg=KEM):
    return FN[kind](cx, cy, R).replace("{c}", c)
KINDS = [("G1", "G1 · Vân chữ A dựng hình"), ("G2", "G2 · Vân vuông bo"), ("G3", "G3 · Vân truy xuất (mã vạch)"), ("G4", "G4 · Dấu kiểm định")]

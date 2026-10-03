"""Vân tay Điểm Chỉ – lượt H: công nghiệp, thêm ý tưởng (ghép A + dây chuyền, lục giác, roundel, lệch tầng)."""
import math
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union
from shapely import affinity
import van_f as F, van_g as Gm
DO, KEM, MUC, VANG = F.DO, F.KEM, F.MUC, F.VANG
_d, _stroke, _arc = F._d, F._stroke, F._arcpts
def P(g, c): return f'<path fill="{c}" fill-rule="evenodd" d="{_d(g)}"/>'

def a_day_chuyen(cx, cy, R, c, bg, n=5):
    """Chữ A vân lều; chân phải mỗi đường vân bẻ góc chạy ngang thành dải dây chuyền."""
    g = R / (n + 2.4); w = g * .5; base = cy + R * .80; apy = cy - R * .30
    W, H = R * .36, base + g * 3 - apy; L = math.hypot(W, H)
    tri = Polygon([(cx - W, base + g * 3), (cx, apy), (cx + W, base + g * 3)])
    clipb = box(cx - 3 * R, cy - 3 * R, cx + 3 * R, base - g * .25)
    parts = []; xend = cx + R * 1.55
    for i in range(n):
        d = g * (i + .5); ring = tri.buffer(d, join_style=1, resolution=32).exterior
        sh = _stroke(ring, w, 2).intersection(clipb)
        yi = base - g * .5 - i * g * 1.0
        xr = cx + W * (yi - apy) / H + d * L / H
        sh = sh.difference(box(cx + 1e-3, yi, cx + 3 * R, cy + 3 * R))
        parts += [sh, _stroke(LineString([(xr, yi - w / 2 + w / 2), (xend, yi)]), w, 2).union(box(xr - w / 2, yi - w / 2, xr + w / 2, yi + w / 2))]
    inner = tri.buffer(-g * .5, join_style=1, resolution=32)
    parts.append(_stroke(inner.exterior, w, 2).intersection(clipb))
    dot = Point(cx, cy + R * .36).buffer(g * .62, resolution=32)
    return P(unary_union(parts), c) + P(dot, c)

def _hex(cx, cy, r, rot=0):
    return Polygon([(cx + r * math.cos(math.radians(60 * k + 30 + rot)), cy + r * math.sin(math.radians(60 * k + 30 + rot))) for k in range(6)])

def luc_giac(cx, cy, R, c, bg, n=6):
    """Vân lục giác: vòng vân lục giác bo góc lồng nhau (tổ ong, bu-lông – cơ khí, chuẩn xác), lõi vân móc."""
    g = R / (n + .6); w = g * .5; parts = []
    for i in range(2, n + 1):
        hx = _hex(cx, cy + g * .2, g * (i + .2)).buffer(-g * .25).buffer(g * .25, resolution=16)
        sh = _stroke(hx.exterior, w, 2)
        ang = [0, 0, -30, 210, -60, 240, 20][i]
        cut = LineString([(cx, cy), (cx + 3 * R * math.cos(math.radians(ang)), cy - 3 * R * math.sin(math.radians(ang)))]).buffer(g * .3)
        parts.append(sh.difference(cut))
    top = cy - g * .4; r = g * .85
    parts.append(_stroke(LineString([(cx - r, top + g * 1.4)] + _arc(cx, top, r, 180, 0) + [(cx + r, top + g * 1.4)]), w, 2))
    dot = Point(cx, top).buffer(g * .45, resolution=32)
    return P(unary_union(parts), c) + P(dot, c)

def roundel(cx, cy, R, c, bg, n=6):
    """Roundel vân tay: vòng vân tròn, một băng ngang đặc xuyên qua mang chữ AN TÂM – như biển hiệu nhà ga, nhà máy."""
    g = R / (n + .4); w = g * .5; parts = []
    for i in range(1, n + 1):
        sh = _stroke(LineString(_arc(cx, cy, g * (i + .3), 0, 360, 120)), w, 2)
        ang = [0, 40, 220, 70, 250, 130, 310][i]
        cut = LineString([(cx, cy), (cx + 3 * R * math.cos(math.radians(ang)), cy - 3 * R * math.sin(math.radians(ang)))]).buffer(g * .3)
        parts.append(sh.difference(cut))
    bh = R * .36; band = box(cx - R * 1.22, cy - bh / 2 + R * .34, cx + R * 1.22, cy + bh / 2 + R * .34)
    ridges = unary_union(parts).difference(band.buffer(g * .45))
    dot = Point(cx, cy - R * .02).buffer(g * .5, resolution=32)
    t, wt = F.text("AN TÂM", R * .30, "xb", cx, cy + R * .34 + R * .105, KEM if c == DO else DO, "middle", .04)
    return P(ridges, c) + P(band, c) + P(dot, c) + t

def lech_tang(cx, cy, R, c, bg, n=7):
    """Vân lệch tầng: dấu vân tay tròn bị cắt ngang, nửa trên trượt lệch đúng một đường vân – chuyển động, dây chuyền đang chạy."""
    g = R / (n + .5); w = g * .5; parts = []
    for i in range(1, n + 1):
        parts.append(_stroke(LineString(_arc(cx, cy, g * (i + .2), 0, 360, 120)), w, 2))
    rings = unary_union(parts)
    top = rings.intersection(box(cx - 3 * R, cy - 3 * R, cx + 3 * R, cy - g * .18))
    bot = rings.intersection(box(cx - 3 * R, cy + g * .18, cx + 3 * R, cy + 3 * R))
    top = affinity.translate(top, g * 1.0, 0)
    dot = Point(cx + g * .5, cy).buffer(g * .5, resolution=32)
    return P(unary_union([top, bot]), c) + P(dot, c)

FN = {"H1": a_day_chuyen, "H2": luc_giac, "H3": roundel, "H4": lech_tang}
def mark(kind, cx=0, cy=0, R=100, c=DO, bg=KEM): return FN[kind](cx, cy, R, c, bg)
KINDS = [("H1", "H1 · Chữ A + dây chuyền"), ("H2", "H2 · Vân lục giác"), ("H3", "H3 · Roundel vân tay"), ("H4", "H4 · Vân lệch tầng")]

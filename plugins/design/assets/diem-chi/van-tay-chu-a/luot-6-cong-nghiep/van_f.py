"""Vân tay Điểm Chỉ – lượt F: dựng hình học, nét đều, khối chắc – cảm giác công nghiệp, chuyên nghiệp."""
import math, os
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union
from shapely import affinity
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
DO, KEM, MUC, VANG = "#D2141E", "#FFF6EA", "#231716", "#F5B82E"
HERE = os.path.dirname(os.path.abspath(__file__))
FB = {"xb": os.path.join(HERE, "fonts-cn", "BeVietnamPro-800.ttf"), "sb": os.path.join(HERE, "fonts-cn", "BeVietnamPro-600.ttf")}
_F = {}
def text(t, size, k="xb", x=0, y=0, fill=MUC, anchor="start", track=0.0):
    if k not in _F: _F[k] = TTFont(FB[k])
    f = _F[k]; gs = f.getGlyphSet(); cm = f.getBestCmap(); upm = f["head"].unitsPerEm; s = size / upm; cx = 0; parts = []
    for ch in t:
        n = cm.get(ord(ch))
        if not n: continue
        pen = SVGPathPen(gs); gs[n].draw(pen); d = pen.getCommands()
        if d: parts.append(f'<path transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        cx += f["hmtx"][n][0] * s + size * track
    w = cx - size * track; ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    return f'<g fill="{fill}" transform="translate({x + ox:.1f} {y:.1f})">{"".join(parts)}</g>', w

def _d(geom):
    """shapely → path d (fill-rule evenodd)."""
    polys = getattr(geom, "geoms", [geom]); out = []
    for p in polys:
        if p.is_empty: continue
        for ring in [p.exterior, *p.interiors]:
            cs = list(ring.coords); out.append("M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in cs) + "Z")
    return " ".join(out)

def _stroke(line, w, cap=2):          # cap 2 = flat, 1 = round
    return line.buffer(w / 2, cap_style=cap, join_style=1, resolution=24)

def _arcpts(cx, cy, r, a0, a1, n=64):
    return [(cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))) for a in [a0 + (a1 - a0) * k / n for k in range(n + 1)]]

def loop_geom(cx, cy, R, n=7, cap=2):
    """Vân móc dựng hình: 3 vòm lõi chữ U ngược quanh chấm tâm, ngoài là các vòng bao kín
    (nửa trên tròn, thân thẳng, đáy bầu); nét đều, khe đều, vài khe cắt có chủ ý."""
    g = R / (n + .3); w = g * .5; parts = []
    top = cy - R * .16; S = R * .34                       # S: chiều dài thân thẳng của vòng bao
    for i in range(n):
        r = g * (i + .85)
        if i < 3:
            r3 = g * 3.85; lim = S + .78 * r3 * math.sqrt(max(0, 1 - (r / r3) ** 2)) - g * 1.05
            pts = [(cx - r, top + lim * (1 if i != 1 else .93))] + _arcpts(cx, top, r, 180, 0) + [(cx + r, top + lim * (.86 if i == 1 else 1))]
            parts.append(_stroke(LineString(pts), w, cap))
        else:
            ry = r * .78
            pts = _arcpts(cx, top, r, 0, 180) + [(cx - r, top + S)] + \
                  [(cx + r * math.cos(math.radians(a)), top + S + ry * math.sin(math.radians(a))) for a in [180 - 180 * k / 64 for k in range(65)]]
            sh = _stroke(LineString(pts + [pts[0]]), w, cap)
            ang = [-40, 215, -62, 232][i % 4]
            cut = LineString([(cx, top + S * .5), (cx + 3 * R * math.cos(math.radians(ang)), top + S * .5 - 3 * R * math.sin(math.radians(ang)))]).buffer(g * .30)
            parts.append(sh.difference(cut))
    dot = Point(cx, top).buffer(g * .52, resolution=32)
    return unary_union(parts), dot

def line_geom(cx, cy, R, n=6, cap=2, run=1.7):
    """Vân dây chuyền: vân ôm chấm tâm 3/4 vòng rồi chạy thẳng ra phải thành các dải song song."""
    g = R / (n + .5); w = g * .52; parts = []
    for i in range(n):
        r = g * (i + 1)
        pts = _arcpts(cx, cy, r, 0, 270, 96) + [(cx + R * run, cy + r)]
        parts.append(_stroke(LineString(pts), w, cap))
    dot = Point(cx, cy).buffer(g * .55, resolution=32)
    return unary_union(parts), dot

def mark(kind, cx=0, cy=0, R=100, c=DO, bg=KEM):
    if kind == "F1":
        g, dot = loop_geom(cx, cy, R); return f'<path fill="{c}" fill-rule="evenodd" d="{_d(g)}"/><path fill="{c}" d="{_d(dot)}"/>'
    if kind == "F2":
        g, dot = line_geom(cx - R * .45, cy, R * .95); return f'<path fill="{c}" fill-rule="evenodd" d="{_d(g)}"/><path fill="{c}" d="{_d(dot)}"/>'
    if kind == "F3":                                      # huy hiệu khối: ô vuông bo đỏ, vân khoét âm bản
        s = R * 1.12; sq = box(cx - s, cy - s, cx + s, cy + s).buffer(-R * .2).buffer(R * .2, resolution=16)
        g, dot = loop_geom(cx, cy + R * .06, R * .86)
        body = sq.difference(g).difference(dot)
        return f'<path fill="{c}" fill-rule="evenodd" d="{_d(body)}"/><path fill="{VANG}" d="{_d(dot)}"/>'
    if kind == "F4":                                      # con dấu tròn: vân dây chuyền trong vòng tròn
        ring = Point(cx, cy).buffer(R * 1.05, resolution=64).difference(Point(cx, cy).buffer(R * .96, resolution=64))
        g, dot = line_geom(cx - R * .16, cy - R * .10, R * .62, n=5, run=3)
        g = g.intersection(Point(cx, cy).buffer(R * .84, resolution=64))
        return f'<path fill="{c}" fill-rule="evenodd" d="{_d(unary_union([ring, g]))}"/><path fill="{c}" d="{_d(dot)}"/>'
    raise ValueError(kind)

KINDS = [("F1", "F1 · Vân móc dựng hình"), ("F2", "F2 · Vân dây chuyền"), ("F3", "F3 · Huy hiệu khối"), ("F4", "F4 · Con dấu dây chuyền")]

"""Vân tay Điểm Chỉ – lượt E: vân tay chi tiết như thật (vân móc, rẽ nhánh, đậm nhạt theo lực ấn),
dựng từ trường hướng vân rồi vector hoá – cho cảm giác dấu son thật, sang."""
import math
import numpy as np
from scipy import ndimage
from scipy.spatial import cKDTree
from skimage import measure
DO, KEM, VANG = "#D2141E", "#FFF6EA", "#F5B82E"
G = 700; U = np.linspace(-1.25, 1.25, G); X, Y = np.meshgrid(U, U)

def _noise(seed, scale, amp):
    rs = np.random.RandomState(seed); n = ndimage.gaussian_filter(rs.randn(G, G), scale); return n / n.std() * amp

def _skel_loop(h=.30, w=.10):
    """Bộ xương vân móc (loop): chữ U ngược hẹp ở lõi."""
    P = [(-w, .12 - t * h) for t in np.linspace(0, 1, 40)]
    P += [(w * math.cos(a), .12 - h - w * math.sin(a) * 1.2 + .0) for a in np.linspace(math.pi, 0, 40)]
    P += [(w, .12 - h + t * h * .7) for t in np.linspace(0, 1, 30)]
    return np.array(P)

def ridge_field(seed=5, lam=.064, kind="loop"):
    if kind == "loop":
        sk = _skel_loop()
        d = cKDTree(sk).query(np.c_[X.ravel(), Y.ravel()])[0].reshape(G, G)
    else:                                                # xoáy tròn
        d = np.sqrt(X ** 2 + (Y / 1.1) ** 2)
    e = np.sqrt((X / .86) ** 2 + ((Y + .02) / 1.06) ** 2)
    w = np.clip(d / .9, 0, 1) ** 1.3 * .75
    F = (1 - w) * d + w * (e - .12)
    F += _noise(seed, 40, .018) + _noise(seed + 1, 14, .006)          # cong vênh tự nhiên
    return F, e

def ridges(seed=5, lam=.064, kind="loop", press=True):
    F, e = ridge_field(seed, lam, kind)
    R = np.cos(2 * np.pi * F / lam)                                     # 1 = giữa vân
    t = -.10 + _noise(seed + 2, 11, .20)                                 # ngưỡng nhiễu → đứt / rẽ nhánh
    if press:
        t += .35 * np.clip(e - .55, 0, 1) ** 1.5 * 3                    # mép dấu: ấn nhẹ, vân mảnh dần
    edge = 1.0 + _noise(seed + 3, 18, .035)                             # mép dấu loang không đều
    M = (R - t) * (e < edge)
    M = ndimage.gaussian_filter(np.where(e < edge, M, -1.0), 1.6)
    return M, F, e

def to_svg_paths(M, cx, cy, r, c, level=0.0, step=1):
    sc = r / 1.0; o = []
    for cont in measure.find_contours(M, level):
        if len(cont) < 6: continue
        pts = measure.approximate_polygon(cont, tolerance=.7)
        if len(pts) < 4: continue
        d = "M" + " L".join(f"{cx + (p[1] / (G - 1) * 2.5 - 1.25) * sc:.1f},{cy + (p[0] / (G - 1) * 2.5 - 1.25) * sc:.1f}" for p in pts) + "Z"
        o.append(d)
    return f'<path fill="{c}" fill-rule="evenodd" d="{" ".join(o)}"/>'

_cache = {}
def mark(kind, cx=0, cy=0, r=100, c=DO, bg=KEM, seed=5):
    key = (kind, seed)
    if key not in _cache:
        if kind == "E5":
            M, F, e = ridges(seed, lam=.042, kind="loop")
        else:
            M, F, e = ridges(seed, kind="whorl" if kind == "E3" else "loop")
        _cache[key] = (M, F, e)
    M, F, e = _cache[key]
    o = to_svg_paths(M, cx, cy, r, c)
    core = (0, -.05)                                                   # lõi vân móc
    if kind == "E3": core = (0, 0)
    px, py = cx + core[0] * r, cy + core[1] * r
    if kind == "E2":                                                   # "sợi chỉ tâm": một đường vân vàng chạy suốt dấu
        lam = .064; lv = 2 * lam
        cs = [cc for cc in measure.find_contours(F, lv) if len(cc) > 30]
        best = min(cs, key=lambda cc: np.hypot(cc[:, 1].mean() / (G - 1) * 2.5 - 1.25, cc[:, 0].mean() / (G - 1) * 2.5 - 1.25))
        d = "M" + " L".join(f"{cx + (p[1] / (G - 1) * 2.5 - 1.25) * r:.1f},{cy + (p[0] / (G - 1) * 2.5 - 1.25) * r:.1f}" for p in best[::2])
        o += f'<path d="{d}" fill="none" stroke="{bg}" stroke-width="{r * .05:.1f}" stroke-linecap="round"/>'
        o += f'<path d="{d}" fill="none" stroke="{VANG}" stroke-width="{r * .028:.1f}" stroke-linecap="round"/>'
    if kind == "E4":                                                   # khoảng sáng tròn quanh tâm – như lỗ khuyên của dấu
        o += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r * .19:.1f}" fill="{bg}"/>'
    o += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r * (.085 if kind != "E4" else .10):.1f}" fill="{c}"/>'
    return o

KINDS = [("E1", "E1 · Dấu son thật"), ("E2", "E2 · Sợi chỉ tâm"), ("E3", "E3 · Vân xoáy thật"),
         ("E4", "E4 · Khoảng lặng quanh tâm"), ("E5", "E5 · Vân khắc mảnh")]

"""Vân tay Điểm Chỉ – lượt D: đường vân là các đường đồng mức toả ra từ một hạt nhân chữ a/A
(như vân tay thật chảy quanh lõi), gần lõi rõ chữ, ra ngoài tròn dần thành dấu vân tay."""
import math, random
import numpy as np
from scipy.spatial import cKDTree
from skimage import measure
DO, KEM = "#D2141E", "#FFF6EA"
G = 520                                   # độ phân giải lưới
U = np.linspace(-1.35, 1.35, G)
X, Y = np.meshgrid(U, U)

def _poly(pts): return np.array(pts)

def skel_a(tail=True, stem_top=-.28):
    """Bộ xương chữ a một tầng (đơn vị chuẩn hoá, tâm thân chữ ở gốc)."""
    rb, ry = .26, .28; P = []
    for d in np.linspace(-30, 290, 120):
        t = math.radians(d); P.append((rb * math.cos(t), ry * math.sin(t)))
    sx = rb
    P += [(sx, y) for y in np.linspace(stem_top, .22, 40)]
    if tail:
        P += [(sx + .09 * (1 - math.cos(t)), .22 + .09 * math.sin(t)) for t in np.linspace(0, math.pi / 2, 14)]
    return _poly(P)

def skel_A():
    P = [(-.34 + .34 * t, .40 - .78 * t) for t in np.linspace(0, 1, 60)]
    P += [(.34 * t, -.38 + .78 * t) for t in np.linspace(0, 1, 60)]
    P += [(-.18 + .36 * t, .10) for t in np.linspace(0, 1, 30)]
    return _poly(P)

def field(sk, morph=.85, aspect=1.2, seed=5, reach=1.0):
    d = cKDTree(sk).query(np.c_[X.ravel(), Y.ravel()])[0].reshape(G, G)
    e = np.sqrt(X ** 2 + (Y / aspect) ** 2)                      # trường tròn của dấu vân tay
    w = np.clip(d / reach, 0, 1) ** 1.2 * morph                  # càng xa lõi càng tròn
    F = (1 - w) * d + w * (e - .15)
    rr = np.random.RandomState(seed); ph = rr.uniform(0, 6.28, 4)
    A = np.arctan2(Y, X)
    F += .012 * np.sin(3 * A + ph[0]) + .008 * np.sin(5 * A + ph[1] + 4 * e)   # rung nhẹ như vân thật
    return F, d

def mark(kind, cx=0, cy=0, r=100, c=DO, seed=5):
    rr = random.Random(seed)
    cfg = {"D1": dict(sk=skel_a(), morph=.80, core=True),
           "D2": dict(sk=skel_a(), morph=.80, core=False),
           "D3": dict(sk=skel_a(), morph=.97, core=False),
           "D4": dict(sk=skel_A(), morph=.80, core=False),
           "D5": dict(sk=skel_a(tail=False, stem_top=-.30), morph=.88, core=False)}[kind]
    F, d = field(cfg["sk"], cfg["morph"], seed=seed)
    step = .098; sw = r * .05; o = ""
    lv0 = .072 if cfg["core"] else .0
    levels = np.arange(step * 1.25, .93, step) if cfg["core"] else np.arange(.035, .93, step)
    sc = r / 1.0
    tf = lambda p: (cx + (p[1] / (G - 1) * 2.7 - 1.35) * sc, cy + (p[0] / (G - 1) * 2.7 - 1.35) * sc)
    for j, lv in enumerate(levels):
        for cont in measure.find_contours(F, lv):
            if len(cont) < 12: continue
            px = cont[:, 1] / (G - 1) * 2.7 - 1.35; py = cont[:, 0] / (G - 1) * 2.7 - 1.35
            if kind != "D4" and np.max(np.hypot(px, py)) < .22: continue      # vụn trong lòng chữ a
            if kind == "D4" and np.max(np.hypot(px, py + .02)) < .2: continue
            pts = [tf(p) for p in cont[::2]]
            # đứt vân ngẫu nhiên ở vòng ngoài
            if j >= 3 and len(pts) > 80 and rr.random() < .8:
                g0 = rr.randint(0, len(pts) - 20); gl = rr.randint(4, 9)
                segs = [pts[:g0], pts[g0 + gl:]]
            else:
                segs = [pts]
            for sg in segs:
                if len(sg) > 3:
                    o += '<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in sg) + f'" fill="none" stroke="{c}" stroke-width="{sw * (1 if j else (1.0)):.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
    if cfg["core"]:
        sk = cfg["sk"]; o += '<path d="M' + " L".join(f"{cx + x * sc:.1f},{cy + y * sc:.1f}" for x, y in sk[:120]) + f'" fill="none" stroke="{c}" stroke-width="{sw * 1.8:.1f}" stroke-linecap="round"/>'
        o += '<path d="M' + " L".join(f"{cx + x * sc:.1f},{cy + y * sc:.1f}" for x, y in sk[120:]) + f'" fill="none" stroke="{c}" stroke-width="{sw * 1.8:.1f}" stroke-linecap="round"/>'
    dx = -.02 if kind != "D4" else 0; dy = 0 if kind != "D4" else -.04
    o += f'<circle cx="{cx + dx * sc:.1f}" cy="{cy + dy * sc:.1f}" r="{r * (.075 if kind == "D4" else .12):.1f}" fill="{c}"/>'
    return o

KINDS = [("D1", "D1 · Lõi chữ a đậm, vân toả theo"),
         ("D2", "D2 · Vòng vân đầu tiên là chữ a"),
         ("D3", "D3 · Vân uốn nhẹ theo chữ a"),
         ("D4", "D4 · Vân toả từ hạt nhân chữ A")]

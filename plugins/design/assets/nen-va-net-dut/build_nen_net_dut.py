"""Ảnh nền và đường nét đứt thương hiệu Ẩm Thực An Tâm.

Chạy:  python3 build_nen_net_dut.py
Xuất cạnh file này:
- nen-<kiểu>-<cỡ>.svg: 5 kiểu nền × 3 cỡ (1920x1080, 1080x1350, 1080x1920)
- net-dut-<kiểu>.svg: 5 đường nét đứt, dải 1200×60, lặp liền được
"""
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
DO, DO2, DO3, VANG, VANG2, BOT, THAN, BANH, NAU = (
    "#E3120B", "#C40E08", "#F0372B", "#FFB627", "#C98A1C", "#FFF6E8", "#1C1412", "#F3DDB3", "#8A5230")
C, S = math.cos(math.radians(30)), math.sin(math.radians(30))
M = 2400  # cạnh bản gốc hình vuông; mỗi cỡ cắt giữa từ bản gốc
SIZES = {"ngang-1920x1080": (1920, 1080), "bai-dang-1080x1350": (1080, 1350), "doc-1080x1920": (1080, 1920)}


def svg(body, vb, w, h, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" '
            f'preserveAspectRatio="xMidYMid slice"><defs>{defs}</defs>{body}</svg>\n')


def crop(w, h):
    """viewBox cắt giữa bản gốc M×M theo tỉ lệ w:h."""
    if w / h >= 1:
        cw, ch = M, M * h / w
    else:
        cw, ch = M * w / h, M
    return f"{(M - cw) / 2:.0f} {(M - ch) / 2:.0f} {cw:.0f} {ch:.0f}"


def poly(pts, fill, extra=""):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" {extra}/>'


def grain(x, y, L, W, ang, fill, op=1):
    return (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{L / 2:.1f}" ry="{W / 2:.1f}" fill="{fill}" opacity="{op}" '
            f'transform="rotate({ang:.0f} {x:.1f} {y:.1f})"/>')


def spots(cx, cy, rx, ry, n, seed, scale=1.0):
    r = random.Random(seed)
    out = []
    for _ in range(n):
        a = r.uniform(0, 2 * math.pi)
        d = math.sqrt(r.uniform(0, 1))
        x, y = cx + math.cos(a) * d * rx, cy + math.sin(a) * d * ry
        s = r.uniform(6, 26) * scale
        out.append(grain(x, y, s * 2, s * 1.3, r.randint(0, 180), r.choice([NAU, "#B07A4A", "#6E3E1E"]), r.choice([.45, .65, .85])))
    return "".join(out)


# ---------- ảnh nền ----------
def nen_cau_thang():
    """Cầu thang nhìn nghiêng: mặt bậc sáng, thành bậc tối, mặt cắt đầu cầu thang màu hồng đỏ."""
    body = [f'<rect width="{M}" height="{M}" fill="{DO}"/>']
    D, H, L = 280, 300, 4000
    fx, fy = 1150, -250
    prof = [(fx + C * D, fy - S * D)]
    for i in range(10):
        a = (fx, fy); b = (fx + C * L, fy + S * L)
        tread = [a, b, (b[0] + C * D, b[1] - S * D), (a[0] + C * D, a[1] - S * D)]
        riser = [a, b, (b[0], b[1] + H), (a[0], a[1] + H)]
        body.append(poly(tread, DO3))
        body.append(poly(riser, DO2))
        body.append(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="{VANG}" stroke-width="8" stroke-dasharray="2 26" stroke-linecap="round" opacity=".8"/>')
        prof += [a, (a[0], a[1] + H)]
        fx, fy = fx - C * D, fy + H + S * D
    # mặt cắt đầu cầu thang (bên trái), khép xuống đáy
    last = prof[-1]
    prof += [(last[0], M + 800), (prof[0][0], M + 800)]
    body.append(poly(prof, "#FF5A4E"))
    body.append(f'<polyline points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in prof[:-2])}" fill="none" stroke="{VANG}" stroke-width="6" stroke-dasharray="20 14" opacity=".9"/>')
    return "".join(body)


def nen_dom_chay():
    return f'<rect width="{M}" height="{M}" fill="{BANH}"/>' + spots(M / 2, M / 2, M * .72, M * .72, 520, 11, 1.1)


def nen_xoan_cuon():
    body = [f'<rect width="{M}" height="{M}" fill="{BOT}"/>']
    step = 300
    for iy in range(-1, M // step + 2):
        for ix in range(-1, M // step + 2):
            cx = ix * step + (step / 2 if iy % 2 else 0); cy = iy * step * .88
            pts = []
            for k in range(140):
                t = k / 139; a = t * 3.1 * 2 * math.pi; r = 118 * t
                pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
            body.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="126" fill="{BANH}" opacity=".55"/>')
            body.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{DO}" stroke-width="7" stroke-linecap="round" opacity=".22"/>')
    return "".join(body)


def nen_hat_lua():
    body = [f'<rect width="{M}" height="{M}" fill="{DO}"/>']
    r = random.Random(5)
    for _ in range(420):
        x, y = r.uniform(0, M), r.uniform(0, M)
        body.append(grain(x, y, r.uniform(34, 60), r.uniform(15, 24), r.randint(0, 180), r.choice([VANG, "#FFC85A", VANG2]), r.choice([.35, .6, .9])))
    return "".join(body)


def nen_than():
    """Nền tối: đường bậc thang vàng nét đứt, một đĩa bánh lớn mờ."""
    body = [f'<rect width="{M}" height="{M}" fill="{THAN}"/>',
            f'<circle cx="{M * .72:.0f}" cy="{M * .38:.0f}" r="620" fill="{NAU}" opacity=".22"/>']
    for j in range(7):
        x, y = -200, 300 + j * 330
        pts = []
        for k in range(10):
            pts += [(x, y), (x + C * 260, y + S * 260)]
            x, y = x + C * 260, y + S * 260 - 190
        d = "M" + " L".join(f"{a:.0f},{b:.0f}" for a, b in pts)
        body.append(f'<path d="{d}" fill="none" stroke="{VANG}" stroke-width="5" stroke-dasharray="26 18" opacity="{.38 + .08 * (j % 3):.2f}"/>')
    return "".join(body)


BACKGROUNDS = {"cau-thang": nen_cau_thang, "dom-chay": nen_dom_chay, "xoan-cuon": nen_xoan_cuon,
               "hat-lua": nen_hat_lua, "than-dem": nen_than}


# ---------- đường nét đứt (dải 1200×60, lặp liền) ----------
W, HH = 1200, 60


def net_hat_lua():
    return "".join(grain(20 + i * 50, 30, 30, 13, 20 if i % 2 else -20, VANG) for i in range(24))


def net_dom_chay():
    r = random.Random(3)
    out = []
    for i in range(30):
        x = 20 + i * 40
        s = r.uniform(6, 11)
        out.append(grain(x + r.uniform(-4, 4), 30 + r.uniform(-4, 4), s * 2, s * 1.4, r.randint(0, 180), r.choice([NAU, "#B07A4A", "#6E3E1E"])))
    return "".join(out)


def net_bac_thang():
    """Chuỗi bậc "/|" rời nhau, cùng góc 30° với chữ cầu thang."""
    out = []
    for i in range(W // 48 + 1):
        x = i * 48 + 6
        out.append(f'<path d="M{x},44 l30,-17 l0,17" fill="none" stroke="{DO}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>')
    return "".join(out)


def net_giay_goi():
    out = []
    for i in range(20):
        x = i * 60
        out.append(f'<rect x="{x + 4}" y="25" width="30" height="10" rx="5" fill="{DO}"/>')
        out.append(f'<rect x="{x + 40}" y="25" width="10" height="10" rx="5" fill="{VANG}"/>')
    return "".join(out)


def net_duong_cat():
    out = [f'<line x1="70" y1="30" x2="{W}" y2="30" stroke="{THAN}" stroke-width="4" stroke-dasharray="16 12" stroke-linecap="round"/>']
    for i in range(1, 6):
        x = i * 220
        out.append(f'<circle cx="{x}" cy="30" r="11" fill="{BANH}" stroke="{NAU}" stroke-width="3"/>')
    # cây kéo
    out.append(f'<g transform="translate(10 12)" fill="none" stroke="{DO}" stroke-width="4" stroke-linecap="round">'
               f'<circle cx="10" cy="8" r="7"/><circle cx="10" cy="28" r="7"/><path d="M16,12 L46,26 M16,24 L46,10"/></g>')
    return "".join(out)


LINES = {"hat-lua": net_hat_lua, "dom-chay": net_dom_chay, "bac-thang": net_bac_thang,
         "giay-goi": net_giay_goi, "duong-cat": net_duong_cat}


if __name__ == "__main__":
    n = 0
    for name, fn in BACKGROUNDS.items():
        body = fn()
        for sz, (w, h) in SIZES.items():
            open(os.path.join(HERE, f"nen-{name}-{sz}.svg"), "w").write(svg(body, crop(w, h), w, h)); n += 1
    for name, fn in LINES.items():
        open(os.path.join(HERE, f"net-dut-{name}.svg"), "w").write(svg(fn(), f"0 0 {W} {HH}", W, HH)); n += 1
    print("Đã tạo", n, "file")

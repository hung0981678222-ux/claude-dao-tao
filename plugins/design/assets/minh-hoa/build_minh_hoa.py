"""Bộ minh hoạ sản phẩm Ẩm Thực An Tâm: bánh tortillas, taco, doner kebab.

Vẽ phẳng (flat vector), cùng một bảng màu: màu thương hiệu (đỏ, vàng kim, trắng bột)
cộng màu thật của món ăn. Mỗi hình là một file SVG 800×800, nền trong suốt.

Chạy:  python3 build_minh_hoa.py
"""
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))

C = {
    "banh": "#F6E3BD", "banh2": "#EBCB91", "banh3": "#D9AE6A", "chay": "#9A5A2E", "chay2": "#C28A55",
    "thit": "#8E4A26", "thit2": "#6B3419", "thit3": "#B8693A",
    "rau": "#7DB34A", "rau2": "#4F8A2E", "ca": "#E0392B", "ca2": "#B32419",
    "hanh": "#9B4F8C", "hanh2": "#F4EDE6", "phomai": "#F2B530", "sot": "#FFF3DC", "sot2": "#E9D4B0",
    "thep": "#AEB6BA", "thep2": "#6E777C", "thep3": "#D9DEE0",
    "do": "#D7150E", "do2": "#8C0F14", "vang": "#EFAE35", "vang2": "#B87018", "kem": "#FBF3E6",
    "muc": "#2A2A2A", "lua": "#FFB347",
}


def svg(body, w=800, h=800):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{body}</svg>\n'


def ell(cx, cy, rx, ry, fill, extra=""):
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" {extra}/>'


def path(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}" {extra}/>'


def blob(cx, cy, r, n=9, jitter=0.28, seed=0, sx=1.0, sy=1.0):
    """Hình tròn méo, nối cong: miếng thịt, cục cà chua..."""
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r * (1 + rnd.uniform(-jitter, jitter))
        pts.append((cx + math.cos(a) * rr * sx, cy + math.sin(a) * rr * sy))
    d = f"M{(pts[0][0] + pts[-1][0]) / 2:.1f},{(pts[0][1] + pts[-1][1]) / 2:.1f} "
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        d += f"Q{p[0]:.1f},{p[1]:.1f} {(p[0] + q[0]) / 2:.1f},{(p[1] + q[1]) / 2:.1f} "
    return d + "Z"


def char_spots(cx, cy, rx, ry, n, seed, clip=None, scale=1.0):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        a = rnd.uniform(0, 2 * math.pi)
        r = math.sqrt(rnd.uniform(0, 1)) * 0.86
        x, y = cx + math.cos(a) * r * rx, cy + math.sin(a) * r * ry
        s = rnd.uniform(5, 15) * scale
        col = C["chay"] if rnd.random() < 0.55 else C["chay2"]
        op = rnd.choice([0.55, 0.75, 0.95])
        out.append(ell(x, y, s, s * ry / rx * 1.4, col, f'opacity="{op}" transform="rotate({rnd.randint(-40, 40)} {x:.1f} {y:.1f})"'))
    g = "".join(out)
    return f'<g clip-path="url(#{clip})">{g}</g>' if clip else g


def lettuce(x0, y0, x1, y1, amp=16, n=9, fill=None, seed=0):
    """Mép lá xà lách gợn sóng từ (x0,y0) tới (x1,y1), dày xuống dưới."""
    rnd = random.Random(seed)
    top = []
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t - (amp * rnd.uniform(0.6, 1.2) if i % 2 else 0)
        top.append((x, y))
    d = f"M{top[0][0]:.1f},{top[0][1]:.1f} "
    for i in range(1, len(top)):
        px, py = top[i - 1]; qx, qy = top[i]
        d += f"Q{(px + qx) / 2:.1f},{min(py, qy) - amp * 0.8:.1f} {qx:.1f},{qy:.1f} "
    d += f"L{x1:.1f},{y1 + 34:.1f} L{x0:.1f},{y0 + 34:.1f} Z"
    return path(d, fill or C["rau"])


def sauce(points, w=9, color=None):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<path d="{d}" fill="none" stroke="{color or C["sot"]}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


# ---------- 1. chồng bánh tortillas ----------
def tortilla_stack():
    b = ['<defs><clipPath id="top"><ellipse cx="370" cy="400" rx="270" ry="92"/></clipPath>'
         '<clipPath id="fold"><path d="M470,640 L470,380 A260,260 0 0 1 700,560 Z"/></clipPath></defs>']
    b.append(ell(400, 660, 330, 58, C["muc"], 'opacity=".10"'))
    for i in range(7, 0, -1):
        y = 400 + i * 24
        b.append(ell(370, y + 6, 272, 94, C["banh3"]))
        b.append(ell(370, y, 272, 94, C["banh2"] if i % 2 else C["banh"]))
    b.append(ell(370, 400, 270, 92, C["banh"]))
    b.append(char_spots(370, 400, 270, 92, 46, 3, "top"))
    # bánh gập tư dựng nghiêng phía trước
    b.append(path("M470,640 L470,380 A260,260 0 0 1 700,560 Z", C["banh"], 'transform="rotate(8 470 640)"'))
    b.append(f'<g transform="rotate(8 470 640)">{char_spots(560, 520, 150, 150, 26, 7, "fold")}'
             f'<path d="M470,640 L470,380" stroke="{C["banh3"]}" stroke-width="6"/>'
             f'<path d="M470,640 L700,560" stroke="{C["banh3"]}" stroke-width="6"/></g>')
    return svg("".join(b))


# ---------- 2. taco ----------
def taco():
    b = [ell(400, 640, 300, 44, C["muc"], 'opacity=".10"')]
    b.append(path("M110,560 A290,290 0 0 1 690,560 Z", C["banh2"]))          # vỏ sau
    # nhân
    b.append(lettuce(150, 400, 650, 400, 20, 12, C["rau2"], 1))
    for k, (x, y) in enumerate([(200, 380), (260, 360), (330, 350), (400, 346), (470, 350), (540, 362), (600, 384)]):
        b.append(path(blob(x, y, 38, seed=k), C["thit"]))
        b.append(path(blob(x - 8, y - 10, 18, seed=k + 20), C["thit3"]))
    b.append(lettuce(140, 430, 660, 430, 18, 12, C["rau"], 2))
    for k, (x, y) in enumerate([(230, 400), (360, 385), (500, 392), (590, 410)]):
        b.append(f'<rect x="{x - 20}" y="{y - 20}" width="40" height="40" rx="9" fill="{C["ca"]}" transform="rotate({k * 17} {x} {y})"/>')
        b.append(f'<rect x="{x - 9}" y="{y - 9}" width="16" height="16" rx="4" fill="{C["ca2"]}" transform="rotate({k * 17} {x} {y})"/>')
    for k, (x, y) in enumerate([(285, 395), (430, 380), (545, 395)]):
        b.append(path(f"M{x - 26},{y} Q{x},{y - 30} {x + 26},{y} Q{x},{y - 14} {x - 26},{y} Z", C["hanh"]))
    rnd = random.Random(5)
    for _ in range(14):
        x, y = rnd.uniform(180, 620), rnd.uniform(360, 410)
        b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="34" height="8" rx="4" fill="{C["phomai"]}" transform="rotate({rnd.randint(-40, 40)} {x:.0f} {y:.0f})"/>')
    b.append(sauce([(180, 380), (240, 350), (300, 385), (360, 345), (420, 382), (480, 348), (540, 384), (600, 360)], 10))
    # vỏ trước
    front = "M100,590 C130,470 270,480 400,486 C530,480 670,470 700,590 C600,650 200,650 100,590 Z"
    b.append(path(front, C["banh"], f'stroke="{C["banh3"]}" stroke-width="8" stroke-linejoin="round"'))
    b.append(f'<clipPath id="shell"><path d="{front}"/></clipPath>')
    b.append(char_spots(400, 560, 290, 80, 34, 9, "shell"))
    return svg("".join(b))


# ---------- 3. doner kebab trên trụ quay ----------
def doner_spit():
    b = [ell(380, 700, 240, 34, C["muc"], 'opacity=".10"')]
    # tấm nhiệt phía sau
    b.append(f'<rect x="530" y="130" width="120" height="480" rx="22" fill="{C["do2"]}"/>')
    for i in range(6):
        y = 170 + i * 72
        b.append(f'<rect x="552" y="{y}" width="76" height="34" rx="12" fill="{C["lua"]}" opacity="{0.55 + 0.07 * i:.2f}"/>')
    # trụ, đĩa trên, đĩa dưới
    b.append(f'<rect x="372" y="70" width="16" height="610" rx="8" fill="{C["thep2"]}"/>')
    b.append(ell(380, 150, 150, 26, C["thep2"]))
    b.append(ell(380, 144, 150, 24, C["thep"]))
    # khối thịt hình nón ngược
    cone = "M232,160 Q380,190 528,160 L470,600 Q380,628 290,600 Z"
    b.append(path(cone, C["thit"]))
    b.append(f'<clipPath id="cone"><path d="{cone}"/></clipPath>')
    layers = []
    for i in range(16):
        y = 180 + i * 27
        col = [C["thit3"], C["thit"], C["thit2"]][i % 3]
        layers.append(path(f"M200,{y} Q380,{y + 34} 560,{y} L560,{y + 14} Q380,{y + 48} 200,{y + 14} Z", col, 'opacity=".75"'))
    b.append(f'<g clip-path="url(#cone)">{"".join(layers)}'
             f'<path d="M232,160 L300,160 L318,610 L290,610 Z" fill="{C["thit2"]}" opacity=".45"/>'
             f'<path d="M470,160 L528,160 L470,610 L430,610 Z" fill="{C["thit3"]}" opacity=".45"/></g>')
    b.append(ell(380, 612, 110, 20, C["thep2"]))
    b.append(ell(380, 606, 110, 18, C["thep"]))
    b.append(f'<rect x="300" y="660" width="160" height="30" rx="10" fill="{C["thep2"]}"/>')
    # dao lạng thịt và lát thịt rơi
    b.append(path("M130,360 L330,300 L338,322 L140,392 Z", C["thep3"]))
    b.append(path("M60,390 L140,366 L150,396 L70,420 Q48,410 60,390 Z", C["muc"]))
    for k, (x, y) in enumerate([(300, 420), (260, 480), (320, 530)]):
        b.append(path(f"M{x - 34},{y} Q{x},{y - 22} {x + 34},{y - 4} Q{x},{y + 10} {x - 34},{y} Z", C["thit3"]))
    return svg("".join(b))


# ---------- 4. doner cuộn cắt chéo ----------
def doner_wrap():
    b = [ell(400, 690, 280, 40, C["muc"], 'opacity=".10"')]

    def half(cx, cy, s, angle):
        g = []
        # thân cuộn
        g.append(f'<rect x="{-110 * s}" y="{-40 * s}" width="{220 * s}" height="{330 * s}" rx="{90 * s}" fill="{C["banh2"]}"/>')
        g.append(f'<rect x="{-110 * s}" y="{-40 * s}" width="{120 * s}" height="{330 * s}" rx="{80 * s}" fill="{C["banh"]}"/>')
        # giấy gói thương hiệu
        g.append(f'<path d="M{-116 * s},{110 * s} L{116 * s},{80 * s} L{116 * s},{300 * s} L{-116 * s},{300 * s} Z" fill="{C["do"]}"/>')
        g.append(f'<path d="M{-116 * s},{150 * s} L{116 * s},{120 * s} L{116 * s},{138 * s} L{-116 * s},{168 * s} Z" fill="{C["vang"]}"/>')
        # mặt cắt
        g.append(ell(0, -40 * s, 112 * s, 70 * s, C["banh3"]))
        g.append(ell(0, -40 * s, 98 * s, 60 * s, C["sot2"]))
        g.append(f'<clipPath id="cut{cx}"><ellipse cx="0" cy="{-40 * s}" rx="{98 * s}" ry="{60 * s}"/></clipPath>')
        inner = [ell(0, -40 * s, 98 * s, 60 * s, C["rau2"])]
        for k, (x, y, r) in enumerate([(-40, -60, 30), (20, -70, 28), (50, -30, 26), (-10, -25, 30), (-60, -20, 22)]):
            inner.append(path(blob(x * s, y * s, r * s, seed=k + cx), C["thit"] if k % 2 == 0 else C["thit3"]))
        for x, y in [(-15, -80), (60, -60), (-70, -45)]:
            inner.append(ell(x * s, y * s, 16 * s, 11 * s, C["ca"]))
        for x, y in [(30, -10), (-45, -5)]:
            inner.append(ell(x * s, y * s, 18 * s, 8 * s, C["hanh2"]))
        inner.append(sauce([(-80 * s, -50 * s), (-30 * s, -30 * s), (20 * s, -55 * s), (70 * s, -35 * s)], 7 * s))
        g.append(f'<g clip-path="url(#cut{cx})">{"".join(inner)}</g>')
        g.append(ell(0, -40 * s, 104 * s, 65 * s, "none", f'stroke="{C["banh"]}" stroke-width="{7 * s}"'))
        return f'<g transform="translate({cx} {cy}) rotate({angle})">{"".join(g)}</g>'

    b.append(half(470, 250, 1.0, 14))
    b.append(half(320, 330, 1.05, -10))
    return svg("".join(b))


# ---------- 5. túi bánh đóng gói ----------
def package():
    b = [ell(400, 720, 250, 36, C["muc"], 'opacity=".10"')]
    b.append(path("M190,120 L610,120 L630,700 L170,700 Z", C["do"]))
    b.append(path("M190,120 L610,120 L612,170 L188,170 Z", C["do2"]))
    for i in range(12):
        x = 200 + i * 35
        b.append(f'<rect x="{x}" y="128" width="14" height="34" rx="3" fill="{C["do"]}" opacity=".6"/>')
    b.append(ell(400, 400, 170, 170, C["kem"]))
    b.append(ell(400, 400, 150, 150, C["banh"]))
    b.append('<clipPath id="win"><circle cx="400" cy="400" r="150"/></clipPath>')
    b.append(char_spots(400, 400, 150, 150, 40, 11, "win"))
    b.append(ell(400, 400, 150, 150, "none", f'stroke="{C["banh2"]}" stroke-width="8"'))
    b.append(f'<rect x="170" y="600" width="460" height="46" fill="{C["vang"]}"/>')
    b.append(f'<text x="400" y="230" text-anchor="middle" font-family="Be Vietnam Pro, Segoe UI, sans-serif" font-weight="800" font-size="44" fill="#fff">BÁNH TORTILLAS</text>')
    b.append(f'<text x="400" y="632" text-anchor="middle" font-family="Be Vietnam Pro, Segoe UI, sans-serif" font-weight="700" font-size="26" fill="{C["muc"]}">ẨM THỰC AN TÂM</text>')
    return svg("".join(b))


# ---------- 6. biểu tượng nguyên liệu ----------
def icons():
    cells = []

    def cell(i, body, label):
        x, y = (i % 3) * 260, (i // 3) * 260
        return (f'<g transform="translate({x} {y})"><circle cx="130" cy="112" r="96" fill="{C["kem"]}"/>{body}'
                f'<text x="130" y="238" text-anchor="middle" font-family="Be Vietnam Pro, Segoe UI, sans-serif" font-weight="700" font-size="22" fill="{C["muc"]}">{label}</text></g>')

    wheat = f'<path d="M130,190 L130,70" stroke="{C["vang2"]}" stroke-width="6"/>' + "".join(
        ell(130 + dx, 80 + k * 22, 12, 22, C["vang"], f'transform="rotate({ang} {130 + dx} {80 + k * 22})"')
        for k in range(4) for dx, ang in [(-14, -30), (14, 30)]) + ell(130, 60, 10, 20, C["vang"])
    cells.append(cell(0, wheat, "Bột mì"))
    bag = path("M85,70 L175,70 L185,180 L75,180 Z", C["kem"], f'stroke="{C["vang2"]}" stroke-width="5"') + \
        f'<rect x="85" y="110" width="90" height="36" fill="{C["do"]}"/>' + path("M85,70 Q130,50 175,70", "none", f'stroke="{C["vang2"]}" stroke-width="5"')
    cells.append(cell(1, bag, "Bao bột"))
    cells.append(cell(2, path(blob(130, 112, 60, seed=4), C["thit"]) + path(blob(118, 98, 26, seed=5), C["thit3"]) +
                      f'<path d="M95,130 Q130,120 165,135" stroke="{C["thit2"]}" stroke-width="6" fill="none"/>', "Thịt"))
    lt = path("M60,150 Q70,60 130,50 Q190,60 200,150 Q130,180 60,150 Z", C["rau"]) + \
        f'<path d="M130,60 L130,165 M130,100 L95,80 M130,120 L165,95 M130,140 L90,125" stroke="{C["rau2"]}" stroke-width="5" fill="none"/>'
    cells.append(cell(3, lt, "Xà lách"))
    cells.append(cell(4, ell(130, 120, 66, 58, C["ca"]) + ell(110, 102, 18, 12, "#F26B5E") +
                      path("M130,64 L110,50 L128,58 L130,40 L134,58 L152,50 Z", C["rau2"]), "Cà chua"))
    cells.append(cell(5, ell(130, 118, 62, 60, C["hanh"]) + ell(130, 118, 44, 42, "#C27BB3") + ell(130, 118, 24, 22, C["hanh2"]), "Hành tây"))
    cells.append(cell(6, path("M160,60 C200,90 190,160 120,180 C80,190 70,170 90,160 C140,140 150,110 145,70 Z", C["ca"]) +
                      path("M145,70 C150,50 165,45 175,50", "none", f'stroke="{C["rau2"]}" stroke-width="8" stroke-linecap="round"'), "Ớt"))
    bottle = f'<rect x="100" y="80" width="60" height="110" rx="18" fill="{C["do"]}"/><rect x="118" y="50" width="24" height="34" rx="6" fill="{C["muc"]}"/>' \
             f'<rect x="100" y="115" width="60" height="30" fill="{C["kem"]}"/>'
    cells.append(cell(7, bottle, "Sốt"))
    pan = ell(115, 120, 72, 30, C["muc"]) + ell(115, 114, 64, 24, "#4A4A4A") + ell(115, 112, 48, 17, C["banh"]) + \
        f'<rect x="182" y="106" width="60" height="14" rx="7" fill="{C["muc"]}"/>' + char_spots(115, 112, 48, 17, 8, 2, scale=0.5)
    cells.append(cell(8, pan, "Chảo nướng"))
    return svg("".join(cells), 780, 780)


FILES = {
    "banh-tortillas.svg": tortilla_stack, "taco.svg": taco, "doner-tru-quay.svg": doner_spit,
    "doner-cuon.svg": doner_wrap, "tui-banh.svg": package, "nguyen-lieu.svg": icons,
}

if __name__ == "__main__":
    for name, fn in FILES.items():
        open(os.path.join(HERE, name), "w").write(fn())
    print("Đã tạo", len(FILES), "hình")

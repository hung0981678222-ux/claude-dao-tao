"""Bao bì túi bánh tortilla An Tâm – khổ thành phẩm 300 × 330 mm (rộng × cao), tràn lề 3 mm.
Đơn vị trong SVG = mm. Chữ đã chuyển thành nét (outline) nên nhà in không cần cài font.
Giả định khuôn (đối chiếu lại với nhà in): túi 3 biên hàn + miệng zip; biên hàn hông và đáy 10 mm,
zip cách mép trên 35 mm, vết xé cách mép trên 25 mm; cửa sổ trong suốt tròn Ø108 mm ở mặt trước.
Chạy: python3 tui_tortilla.py OUTDIR
"""
import math
import os
import random
import sys

import build_chuan as C
import build_van as B

V = C.V
V.F["rg"] = os.path.join(C.DIST, "AnTamTronBanh-Regular.ttf")
DO, DO2, SON, KEM, MUC, NGO = V.DO, V.DO2, V.SON, V.KEM, V.MUC, V.NGO
TW, TH, BL = 300, 330, 3            # thành phẩm, tràn lề
SEAL, ZIP, TEAR, SAFE = 10, 35, 25, 15
WIN = (150, 184, 54)                # cửa sổ: tâm x, tâm y, bán kính
RING = 84                           # bán kính ngoài vòng vân quanh cửa sổ


def W(t, size, x, y, fill=DO, k="xb", anchor="start", track=0.0):
    return V.text(t, size, k, x, y, fill, anchor, track)[0]


def place(svg, x, y, w, h):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


def doc(body, label, mm=True):
    size = f'width="{TW + 2 * BL}mm" height="{TH + 2 * BL}mm" ' if mm else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" {size}viewBox="{-BL} {-BL} {TW + 2 * BL} {TH + 2 * BL}" '
            f'role="img" aria-label="{label}">{body}</svg>')


def vong_van(cx, cy, r0, r1, color, n=13, seed=11, sw=1.7):
    """Các vòng vân tay đồng tâm (lượn sóng, có chỗ đứt) giữa bán kính r0 và r1 – cửa sổ là lõi vân."""
    rr = random.Random(seed); ph = [rr.uniform(0, 6.28) for _ in range(3)]; out = []
    for i in range(n):
        rad = r0 + (r1 - r0) * (i + .5) / n; N = 180; pts = []
        for k in range(N + 1):
            a = k / N * 2 * math.pi
            wob = 1 + .018 * math.sin(3 * a + ph[0] + i * .2) + .012 * math.sin(5 * a + ph[1] + i * .35) + .008 * math.sin(2 * a + ph[2])
            pts.append((cx + rad * wob * math.cos(a), cy + rad * wob * math.sin(a)))
        g0 = rr.randint(0, N - 1); gl = rr.randint(5, 14)
        seg = [pts[(g0 + gl + j) % (N + 1)] for j in range(N - gl)]
        out.append(f'<path d="M{" L".join(f"{x:.2f},{y:.2f}" for x, y in seg)}" fill="none" stroke="{color}" '
                   f'stroke-width="{sw}" stroke-linecap="round"/>')
    return "".join(out)


def dau_tron(cx, cy, r, rot=-12):
    s = V.con_dau()
    return f'<g transform="rotate({rot} {cx} {cy})">{place(s, cx - r, cy - r, 2 * r, 2 * r)}</g>'


def nen(x, y, w, h):
    """Nền đỏ có đường vân chảy (tỷ lệ theo mm)."""
    k = 4.0
    return place(B.nen_van(int(w * k), int(h * k)), x, y, w, h)


# ------------------------------------------------------------------ mặt trước
def mat_truoc(window=None):
    """window=None: để trống (không in mực) tại cửa sổ. window='banh': vẽ bánh nhìn qua cửa sổ (dùng cho mockup)."""
    cx, cy, rw = WIN
    s = f'<rect x="{-BL}" y="{-BL}" width="{TW + 2 * BL}" height="{TH + 2 * BL}" fill="{KEM}"/>'
    s += f'<mask id="cs"><rect x="-10" y="-10" width="320" height="350" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="{rw}" fill="#000"/></mask>'
    s += f'<g mask="url(#cs)">'
    s += nen(-BL, -BL, TW + 2 * BL, 100 + BL)
    s += f'<rect x="{-BL}" y="97" width="{TW + 2 * BL}" height="3" fill="{DO2}"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{RING + 3}" fill="{KEM}"/>'
    s += vong_van(cx, cy, rw + 4, RING, DO)
    s += f'<circle cx="{cx}" cy="{cy}" r="{rw + 1.2}" fill="none" stroke="{DO}" stroke-width="2.4"/>'
    s += "</g>"
    if window == "banh":
        s += banh_qua_cua_so(cx, cy, rw)
    s += place(V.logo_ngang(KEM, KEM), 71, 38, 158, 56.3)
    s += dau_tron(244, 252, 25)
    s += W("Bánh Tortilla", 27, 150, 293, DO, "xb", "middle")
    s += W("Bánh bột mì mềm  ·  Cỡ [ ] inch  ·  [ ] chiếc / túi", 4.6, 150, 303.5, MUC, "md", "middle", .02)
    s += W("Khối lượng tịnh: [      ] g", 4.6, 150, 312.5, DO, "xb", "middle", .02)
    return s


def banh_qua_cua_so(cx, cy, r):
    rr = random.Random(4); dots = []
    for _ in range(70):
        a = rr.uniform(0, 6.28); d = r * math.sqrt(rr.uniform(0, 1))
        dots.append(f'<ellipse cx="{cx + d * math.cos(a):.1f}" cy="{cy + d * math.sin(a):.1f}" rx="{rr.uniform(1.2, 3.4):.1f}" '
                    f'ry="{rr.uniform(.8, 2.2):.1f}" transform="rotate({rr.randint(0, 180)} {cx + d * math.cos(a):.1f} {cy + d * math.sin(a):.1f})" '
                    f'fill="{rr.choice(["#C98F4E", "#B07038", "#D9A866"])}" opacity="{rr.uniform(.45, .85):.2f}"/>')
    return (f'<defs><radialGradient id="bg1" cx=".45" cy=".4" r=".7"><stop offset="0" stop-color="#F6E2B3"/><stop offset="1" stop-color="#E8C88C"/></radialGradient>'
            f'<linearGradient id="kinh" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".35" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#bg1)"/>{"".join(dots)}'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#kinh)"/>')


# ------------------------------------------------------------------ mặt sau
ROWS = [
    ("Tên sản phẩm", "Bánh tortilla bột mì – [Cần điền: loại, cỡ]"),
    ("Thành phần", "[Cần điền theo công thức thực tế]"),
    ("Khối lượng tịnh", "[ ] g  ·  [ ] chiếc / túi"),
    ("NSX · HSD · Số lô", "In tại ô bên dưới"),
    ("Bảo quản", "[Cần điền: nhiệt độ, điều kiện]"),
    ("Sau khi mở", "Kéo kín miệng zip, dùng trong [Cần điền]"),
    ("Thông tin dị ứng", "[Cần điền]"),
    ("Xuất xứ", "[Cần điền]"),
    ("Chịu trách nhiệm", "Công ty TNHH SX-TM Ẩm Thực An Tâm"),
    ("Địa chỉ", "[Cần điền]"),
]

GOI_Y = [("doner-cuon", "Cuộn doner kebab"), ("taco", "Gấp vỏ taco"), ("nguyen-lieu", "Cuộn rau, thịt tuỳ thích")]


def mat_sau():
    s = f'<rect x="{-BL}" y="{-BL}" width="{TW + 2 * BL}" height="{TH + 2 * BL}" fill="{KEM}"/>'
    s += nen(-BL, -BL, TW + 2 * BL, 70 + BL) + f'<rect x="{-BL}" y="67" width="{TW + 2 * BL}" height="3" fill="{DO2}"/>'
    s += place(V.logo_ngang(KEM, KEM), 105, 39, 90, 32)
    # bảng thông tin
    s += W("Thông tin sản phẩm", 6.2, SAFE, 86, DO, "xb")
    y = 95
    for i, (k, v) in enumerate(ROWS):
        if i % 2 == 0:
            s += f'<rect x="{SAFE}" y="{y}" width="160" height="10.4" fill="#F7E6D3"/>'
        s += W(k, 3.3, SAFE + 3, y + 6.6, MUC, "xb") + W(v, 3.3, SAFE + 43, y + 6.6, MUC, "md")
        y += 10.4
    s += f'<rect x="{SAFE}" y="95" width="160" height="{y - 95:.1f}" fill="none" stroke="{DO}" stroke-width=".5"/>'
    # gợi ý dùng
    gx = 188
    s += W("Gợi ý dùng", 6.2, gx, 86, DO, "xb")
    for i, (n, cap) in enumerate(GOI_Y):
        yy = 95 + i * 35
        s += f'<rect x="{gx}" y="{yy}" width="97" height="31" rx="4" fill="#fff"/>' + B.img(n, gx + 3, yy + 3, 32, 25)
        s += W(cap, 3.6, gx + 39, yy + 17.5, MUC, "xb")
    s += W("Làm nóng: áp chảo khô hoặc lò vi sóng – [Cần điền: thời gian]", 3.3, gx, 205, MUC, "md")
    # ô in phun, mã vạch, QR, liên hệ
    by = 222
    s += f'<rect x="{SAFE}" y="{by}" width="74" height="30" rx="2" fill="#fff" stroke="{MUC}" stroke-width=".4" stroke-dasharray="1.6 1.2"/>'
    s += W("Ô IN PHUN – không in mực nền", 2.6, SAFE + 37, by + 6, "#8a7a74", "xb", "middle", .08)
    s += W("NSX:", 3.3, SAFE + 5, by + 14, MUC, "xb") + W("HSD:", 3.3, SAFE + 5, by + 20.5, MUC, "xb") + W("Số lô:", 3.3, SAFE + 5, by + 27, MUC, "xb")
    s += f'<rect x="101" y="{by}" width="37.29" height="25.93" fill="#fff"/>' + barcode_gia(101, by, 37.29, 25.93)
    s += W("[Mã vạch EAN-13 – thay bằng mã thật]", 2.4, 119.6, by + 30, "#8a7a74", "md", "middle")
    s += f'<rect x="150" y="{by}" width="26" height="26" fill="#fff" stroke="{MUC}" stroke-width=".4"/>' + W("[QR]", 3.4, 163, by + 14.6, "#8a7a74", "xb", "middle")
    s += W("antamfoods.com", 2.6, 163, by + 30, MUC, "md", "middle")
    s += W("Đặt hàng & hỗ trợ đại lý", 3.6, gx, by + 6, DO, "xb")
    s += W("0348.635.222", 9, gx, by + 17.5, DO, "xb")
    s += W("antamfoods.com · Zalo 0348.635.222", 3.3, gx, by + 25, MUC, "md")
    # dải chân
    s += nen(-BL, 268, TW + 2 * BL, TH - 268 + BL) + f'<rect x="{-BL}" y="268" width="{TW + 2 * BL}" height="3" fill="{DO2}"/>'
    s += V.van_tay(150, 287, 9, KEM, seed=31, rings=8)
    s += W("Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm", 6, 150, 307, KEM, "xb", "middle")
    return s


def barcode_gia(x, y, w, h):
    """Vạch minh hoạ vị trí – KHÔNG phải mã vạch thật."""
    rr = random.Random(13); out = []; cx = x + 3.6
    while cx < x + w - 3.6:
        bw = rr.choice([.33, .33, .66, .99]); out.append(f'<rect x="{cx:.2f}" y="{y + 2}" width="{bw}" height="{h - 6}" fill="{MUC}"/>'); cx += bw + rr.choice([.33, .66, .99])
    return "".join(out)


# ------------------------------------------------------------------ bản kỹ thuật
def ky_thuat(face):
    """Một mặt kèm đường chỉ dẫn: tràn lề, đường cắt, biên hàn, zip, vết xé, vùng an toàn, cửa sổ."""
    g = f'<rect x="{-BL}" y="{-BL}" width="{TW + 2 * BL}" height="{TH + 2 * BL}" fill="none" stroke="#00A0E3" stroke-width=".5"/>'
    g += f'<rect x="0" y="0" width="{TW}" height="{TH}" fill="none" stroke="{MUC}" stroke-width=".7"/>'
    hatch = '<pattern id="ht" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="1.4" height="4" fill="#7B61FF" opacity=".5"/></pattern>'
    g += f'<defs>{hatch}</defs><rect x="0" y="0" width="{SEAL}" height="{TH}" fill="url(#ht)"/><rect x="{TW - SEAL}" y="0" width="{SEAL}" height="{TH}" fill="url(#ht)"/><rect x="0" y="{TH - SEAL}" width="{TW}" height="{SEAL}" fill="url(#ht)"/><rect x="0" y="0" width="{TW}" height="{SEAL}" fill="url(#ht)"/>'
    g += f'<line x1="0" y1="{ZIP}" x2="{TW}" y2="{ZIP}" stroke="#7B61FF" stroke-width="1.2" stroke-dasharray="4 2"/>'
    g += f'<path d="M0,{TEAR - 3} L5,{TEAR} L0,{TEAR + 3} M{TW},{TEAR - 3} L{TW - 5},{TEAR} L{TW},{TEAR + 3}" fill="none" stroke="#7B61FF" stroke-width="1"/>'
    g += f'<rect x="{SAFE}" y="{ZIP + 3}" width="{TW - 2 * SAFE}" height="{TH - SAFE - ZIP - 3}" fill="none" stroke="#2F9E44" stroke-width=".6" stroke-dasharray="3 2"/>'
    if face == "truoc":
        g += f'<circle cx="{WIN[0]}" cy="{WIN[1]}" r="{WIN[2]}" fill="none" stroke="#00A0E3" stroke-width="1" stroke-dasharray="3 1.5"/>'
    return g


def chu_thich():
    items = [("#00A0E3", "Tràn lề 3 mm / cửa sổ trong (không mực, không lót trắng)"), (MUC, "Đường cắt thành phẩm 300 × 330 mm"),
             ("#7B61FF", "Biên hàn 10 mm · zip cách mép trên 35 mm · vết xé 25 mm"), ("#2F9E44", "Vùng an toàn cho chữ (cách mép 15 mm, dưới zip)")]
    return items


def tui_3d(face, uid):
    """Một túi đứng: thân in, biên hàn có vân dập, zip, bóng phim."""
    body = f'<clipPath id="k{uid}"><rect width="{TW}" height="{TH}" rx="3"/></clipPath><g clip-path="url(#k{uid})">{face}'
    crimp = "".join(f'<line x1="{x}" y1="{TH - SEAL + 1}" x2="{x}" y2="{TH - 1}" stroke="#000" stroke-opacity=".10" stroke-width=".5"/>' for x in range(2, TW, 2))
    crimp += "".join(f'<line x1="1" y1="{y}" x2="{SEAL - 1}" y2="{y}" stroke="#000" stroke-opacity=".08" stroke-width=".5"/><line x1="{TW - SEAL + 1}" y1="{y}" x2="{TW - 1}" y2="{y}" stroke="#000" stroke-opacity=".08" stroke-width=".5"/>' for y in range(2, TH, 2))
    crimp += "".join(f'<line x1="{x}" y1="1" x2="{x}" y2="{SEAL - 1}" stroke="#000" stroke-opacity=".10" stroke-width=".5"/>' for x in range(2, TW, 2))
    zip_ = f'<rect x="0" y="{ZIP - 1.6}" width="{TW}" height="3.2" fill="#000" opacity=".12"/><rect x="0" y="{ZIP - 1.6}" width="{TW}" height=".8" fill="#fff" opacity=".5"/>'
    gloss = (f'<defs><linearGradient id="gl{uid}" x1="0" y1="0" x2="1" y2=".3"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             f'<stop offset=".18" stop-color="#fff" stop-opacity=".22"/><stop offset=".26" stop-color="#fff" stop-opacity="0"/>'
             f'<stop offset=".7" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".10"/></linearGradient></defs>'
             f'<rect width="{TW}" height="{TH}" fill="url(#gl{uid})"/>')
    notch = f'<path d="M0,{TEAR - 2} L3,{TEAR} L0,{TEAR + 2} Z M{TW},{TEAR - 2} L{TW - 3},{TEAR} L{TW},{TEAR + 2} Z" fill="#EFE7DC"/>'
    return body + crimp + zip_ + gloss + notch + "</g>"


def mockup():
    sh = ('<defs><filter id="bo" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="9" '
          'flood-color="#231716" flood-opacity=".28"/></filter></defs>')
    s = f'<rect width="760" height="480" fill="#EFE7DC"/><rect y="420" width="760" height="60" fill="#E2D6C4"/>' + sh
    s += f'<g filter="url(#bo)" transform="translate(410 70) rotate(4) scale(1.08)">{tui_3d(mat_sau(), "s")}</g>'
    s += f'<g filter="url(#bo)" transform="translate(60 52) rotate(-3) scale(1.12)">{tui_3d(mat_truoc("banh"), "t")}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480" role="img" aria-label="Mô phỏng túi bánh tortilla An Tâm">{s}</svg>'


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    files = {
        "tui-tortilla-mat-truoc.svg": doc(mat_truoc(), "Túi bánh tortilla – mặt trước (file in)"),
        "tui-tortilla-mat-sau.svg": doc(mat_sau(), "Túi bánh tortilla – mặt sau (file in)"),
        "ky-thuat-mat-truoc.svg": doc(mat_truoc() + ky_thuat("truoc"), "Bản kỹ thuật mặt trước", mm=False),
        "ky-thuat-mat-sau.svg": doc(mat_sau() + ky_thuat("sau"), "Bản kỹ thuật mặt sau", mm=False),
        "mockup-mat-truoc.svg": doc(mat_truoc("banh"), "Mặt trước nhìn bánh qua cửa sổ", mm=False),
        "mockup-tui.svg": mockup(),
    }
    for n, s in files.items():
        open(os.path.join(out, n), "w").write(s)
    print("ok", list(files))

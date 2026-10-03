"""Bộ hình ảnh website antamfoods.com – Điểm Chỉ 1.1. Chạy: python3 web_kit.py OUTDIR"""
import os
import sys

import ud2 as U2

V, B = U2.V, U2.B
DO, DO2, SON, KEM, MUC, NGO = U2.DO, U2.DO2, U2.SON, U2.KEM, U2.MUC, U2.NGO
W, fit, mark, anh, S = U2.W, U2.fit, U2.mark, U2.anh, U2.S
HOT = "0398 431 300"


def T(t, size, x, y, fill=MUC, k="xb", anchor="start", track=0.0, maxw=None):
    if maxw:
        w = V.text(t, size, k, 0, 0, fill, anchor, track)[1]
        if w > maxw:
            size *= maxw / w
    return V.text(t, size, k, x, y, fill, anchor, track)[0]


def van_bg(x, y, w, h):
    inner = B.nen_van(int(w), int(h)).split(">", 1)[1].rsplit("</svg>", 1)[0]
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {int(w)} {int(h)}" preserveAspectRatio="none">{inner}</svg>'


def photo(n, x, y, w, h, r=0, al="xMidYMid", nhan=True, size=1400):
    cid = f"ph{abs(hash((n, x, y, w))) % 99999}"
    o = (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'
         f'<image href="{anh(n, size)}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="{al} slice" clip-path="url(#{cid})"/>')
    if nhan:
        o += f'<rect x="{x + 16}" y="{y + h - 50}" width="214" height="34" rx="17" fill="{KEM}" opacity=".94"/>' + mark(x + 36, y + h - 33, 9, DO, rings=6)
        o += T("Ảnh thật tại xưởng An Tâm", 15, x + 52, y + h - 27, MUC, "xb")
    return o


def nut(x, y, t, fill=NGO, ink=MUC, h=60, size=22):
    w = V.text(t, size, "xb")[1] + 64
    return f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="{h / 2}" fill="{fill}"/>' + T(t, size, x + 32, y + h / 2 + size * .36, ink, "xb")


# ── 1. Favicon / icon
def favicon():
    return S(512, 512, f'<rect width="512" height="512" rx="112" fill="{DO}"/>' + V.van_tay_nho(256, 256, 170, KEM), "Favicon")


def app_icon():
    return S(512, 512, f'<rect width="512" height="512" fill="{KEM}"/>' + mark(256, 256, 150, DO), "App icon")


# ── 2. Ảnh chia sẻ (OG) 1200×630
def og():
    s = f'<rect width="1200" height="630" fill="{DO}"/>' + van_bg(0, 0, 1200, 630)
    s += f'<rect x="60" y="60" width="640" height="510" rx="24" fill="{KEM}"/>'
    s += fit(V.logo_ngang(), 380, 170, w=480)
    s += T("Vỏ bánh Tortilla · Taco · Kebab", 34, 100, 330, DO, "xb", maxw=560)
    s += T("Nhà sản xuất cho quán ăn, đại lý, nhượng quyền", 22, 100, 372, MUC, "md", maxw=560)
    s += T(f"Hotline/Zalo {HOT}", 28, 100, 470, MUC, "xb") + T("antamfoods.com", 22, 100, 510, DO, "md")
    s += photo("xuong-gia-banh-1", 730, 60, 410, 510, 24, nhan=False)
    return S(1200, 630, s, "Ảnh chia sẻ antamfoods.com")


# ── 3. Banner trang chủ 1920×720 (3 slide) + bản điện thoại 750×1000
SLIDES = [
    ("Mỗi mẻ bánh,", "một lời cam kết", "Vỏ tortilla, taco, kebab giao tận bếp quán ăn, nhà hàng tại TP.HCM.", "Xem sản phẩm", "xuong-gia-banh-1"),
    ("Dây chuyền tự động,", "đều tay mọi mẻ", "Sản xuất khép kín, kiểm tra từng mẻ trước khi đóng gói.", "Tìm hiểu nhà xưởng", "kiem-tra-banh"),
    ("Giá xưởng,", "nói thẳng, rõ ràng", "Báo giá đại lý, quán ăn và đối tác nhượng quyền – liên hệ để nhận bảng giá.", "Nhận báo giá", "khay-banh-chong"),
]


def hero(i):
    a, b, c, btn, ph = SLIDES[i]
    s = f'<rect width="1920" height="720" fill="{DO}"/>' + van_bg(0, 0, 1920, 720)
    s += photo(ph, 1000, 0, 920, 720, 0)
    s += f'<path d="M940,0 L1060,0 C1000,240 1000,480 1060,720 L940,720 Z" fill="{DO}"/>'
    s += f'<rect x="120" y="120" width="860" height="480" rx="28" fill="{KEM}"/>'
    s += fit(V.logo_ngang(), 330, 200, w=300)
    s += T(a, 66, 170, 340, MUC, "xb") + T(b, 66, 170, 418, DO, "xb")
    s += T(c, 22, 170, 470, MUC, "md", maxw=760)
    s += nut(170, 506, btn, DO, KEM) + T(f"Hotline/Zalo {HOT}", 22, 520, 545, MUC, "xb")
    for k in range(3):
        s += f'<circle cx="{510 + k * 30}" cy="660" r="7" fill="{KEM if k == i else "#E8838A"}"/>'
    return S(1920, 720, s, f"Banner {i + 1}")


def hero_mobile(i):
    a, b, c, btn, ph = SLIDES[i]
    s = f'<rect width="750" height="1000" fill="{DO}"/>' + photo(ph, 0, 0, 750, 560, 0)
    s += f'<rect x="0" y="520" width="750" height="480" fill="{DO}"/>' + van_bg(0, 520, 750, 480)
    s += f'<rect x="40" y="480" width="670" height="470" rx="26" fill="{KEM}"/>'
    s += fit(V.logo_ngang(), 230, 550, w=230)
    s += T(a, 50, 80, 660, MUC, "xb", maxw=590) + T(b, 50, 80, 722, DO, "xb", maxw=590)
    s += T(c, 21, 80, 772, MUC, "md", maxw=590) + nut(80, 820, btn, DO, KEM, 64, 24)
    return S(750, 1000, s, f"Banner điện thoại {i + 1}")


# ── 4. Danh mục 1200×400
CATS = [("Bánh Tortilla", "22 · 25 · 28 · 31 cm · 15 chiếc/túi", "Tươi · Nướng · Nguyên cám", "banh-tortillas"),
        ("Vỏ bánh Kebab", "Vàng · Mè đen · Mè trắng · Than tre", "Dùng cho doner kebab, bánh mì kebab", "doner-cuon"),
        ("Vỏ Taco", "[Cần điền: quy cách]", "Cho quán taco, đồ ăn Mexico", "taco")]


def danh_muc(i):
    n, q, d, ill = CATS[i]
    s = f'<rect width="1200" height="400" fill="{KEM}"/><rect x="760" width="440" height="400" fill="{DO}"/>' + van_bg(760, 0, 440, 400)
    s += f'<circle cx="980" cy="200" r="150" fill="{KEM}"/>' + U2.U.img(ill, 860, 100, 240, 200)
    s += T("DANH MỤC", 16, 80, 110, DO, "xb", track=.3) + T(n, 64, 76, 190, DO, "xb")
    s += T(q, 24, 80, 240, MUC, "xb", maxw=640) + T(d, 20, 80, 278, "#6b5a55", "md", maxw=640)
    s += nut(80, 306, "Xem sản phẩm  →", DO, KEM, 52, 18) + mark(700, 70, 22, DO)
    return S(1200, 400, s, n)


# ── 5. Thẻ sản phẩm 800×800
PRODS = [("Tortilla tươi", "22 / 25 / 28 / 31 cm", "banh-tortillas", DO),
         ("Tortilla nướng", "22 / 25 / 28 / 31 cm", "banh-tortillas", DO2),
         ("Tortilla nguyên cám", "22 / 25 / 28 / 31 cm", "banh-tortillas", "#7A4A2E"),
         ("Vỏ kebab bánh vàng", "[Cần điền: quy cách]", "doner-cuon", NGO),
         ("Vỏ kebab mè đen", "[Cần điền: quy cách]", "doner-cuon", MUC),
         ("Vỏ kebab mè trắng", "[Cần điền: quy cách]", "doner-cuon", "#C9B79A"),
         ("Vỏ kebab than tre", "[Cần điền: quy cách]", "doner-cuon", "#2B2B2B")]


def the_sp(i):
    n, q, ill, acc = PRODS[i]
    s = f'<rect width="800" height="800" fill="#fff"/><rect x="30" y="30" width="740" height="560" rx="24" fill="{KEM}"/>'
    s += f'<circle cx="400" cy="300" r="210" fill="#F6E7D4"/><circle cx="400" cy="300" r="210" fill="none" stroke="{acc}" stroke-width="10" stroke-dasharray="2 16" stroke-linecap="round"/>'
    s += U2.U.img(ill, 220, 150, 360, 300)
    s += f'<rect x="60" y="60" width="120" height="40" rx="20" fill="{DO}"/>' + T("15 chiếc/túi" if "Tortilla" in n else "Vỏ kebab", 15, 120, 86, KEM, "xb", "middle")
    s += mark(700, 100, 26, DO, rings=8)
    s += T("Hình minh hoạ – thay bằng ảnh chụp sản phẩm thật", 13, 400, 570, "#9b8a82", "md", "middle")
    s += T(n, 46, 40, 668, DO, "xb", maxw=720) + T(q, 24, 40, 712, MUC, "md")
    s += T("Liên hệ báo giá", 22, 40, 760, DO, "xb") + T(f"Zalo {HOT}", 22, 760, 760, MUC, "xb", "end")
    return S(800, 800, s, n)


# ── 6. Biểu tượng điểm mạnh (icon SVG 160×160)
def _ico(body):
    return S(160, 160, f'<circle cx="80" cy="80" r="76" fill="{KEM}" stroke="{DO}" stroke-width="4"/>' + body, "Biểu tượng")


ICONS = {
    "day-chuyen": _ico(f'<rect x="30" y="92" width="100" height="14" rx="7" fill="{DO}"/><circle cx="46" cy="99" r="4" fill="{KEM}"/><circle cx="114" cy="99" r="4" fill="{KEM}"/>'
                       f'<ellipse cx="62" cy="84" rx="16" ry="5" fill="{NGO}"/><ellipse cx="98" cy="84" rx="16" ry="5" fill="{NGO}"/><path d="M70,40 L90,40 L90,62 L80,72 L70,62 Z" fill="{DO}"/>'),
    "chat-luong": _ico(mark(80, 80, 40, DO, rings=8) + f'<circle cx="112" cy="112" r="20" fill="{DO}"/><path d="M102,112 l7,7 l13,-14" stroke="{KEM}" stroke-width="5" fill="none" stroke-linecap="round"/>'),
    "giao-hang": _ico(f'<rect x="28" y="58" width="66" height="44" rx="6" fill="{DO}"/><path d="M94,70 L118,70 L132,86 L132,102 L94,102 Z" fill="{DO2}"/>'
                      f'<circle cx="50" cy="108" r="10" fill="{MUC}"/><circle cx="114" cy="108" r="10" fill="{MUC}"/>' + mark(60, 80, 12, KEM, rings=5)),
    "gia-xuong": _ico(f'<path d="M40,50 L92,50 L124,82 L84,122 L40,78 Z" fill="{DO}"/><circle cx="58" cy="66" r="7" fill="{KEM}"/>' + T("₫", 34, 88, 98, KEM, "xb", "middle")),
}


# ── 7. Banner trang con 1920×480
PAGES = [("ve-chung-toi", "Về An Tâm", "Nhà sản xuất vỏ bánh tortilla, taco & kebab tại TP.HCM", "xuong-nguoi-lam"),
         ("san-pham", "Sản phẩm", "Tortilla · Vỏ kebab · Vỏ taco", "khay-banh-chong"),
         ("nha-xuong", "Nhà xưởng", "Dây chuyền tự động khép kín – kiểm tra từng mẻ", "xuong-gia-banh-2"),
         ("doi-tac", "Đại lý & nhượng quyền", "Cùng An Tâm phát triển xứng tầm", "banh-tren-khay"),
         ("lien-he", "Liên hệ", f"Hotline/Zalo {HOT} · antamfoods.com", "xuong-gia-banh-3")]


def trang_con(i):
    k, t, sub, ph = PAGES[i]
    s = photo(ph, 0, 0, 1920, 480, 0, nhan=False) + f'<rect width="1920" height="480" fill="{MUC}" opacity=".45"/>'
    s += f'<rect x="0" y="0" width="900" height="480" fill="{DO}" opacity=".92"/>' + f'<g opacity=".35">{van_bg(0, 0, 900, 480)}</g>'
    s += T("ẨM THỰC AN TÂM", 18, 120, 170, NGO, "xb", track=.3) + T(t, 76, 116, 270, KEM, "xb", maxw=720)
    s += T(sub, 24, 120, 324, KEM, "md", maxw=720) + mark(820, 400, 46, KEM)
    s += T("Ảnh thật tại xưởng An Tâm", 15, 1890, 456, KEM, "md", "end")
    return S(1920, 480, s, t)


# ── 8. Băng kêu gọi 1920×360
def cta():
    s = f'<rect width="1920" height="360" fill="{DO}"/>' + van_bg(0, 0, 1920, 360)
    s += f'<rect x="120" y="60" width="1680" height="240" rx="28" fill="{KEM}"/>' + mark(260, 180, 70, DO)
    s += T("Quán bạn cần vỏ bánh ổn định mỗi ngày?", 46, 380, 170, MUC, "xb") + T("Gửi Zalo để nhận báo giá xưởng và mẫu quy cách phù hợp.", 24, 380, 216, MUC, "md")
    s += nut(1380, 150, f"Zalo {HOT}", DO, KEM, 64, 26)
    return S(1920, 360, s, "Kêu gọi liên hệ")


# ── 9. Nút nổi Zalo / gọi 120×120
def nut_noi(kind):
    s = f'<circle cx="60" cy="60" r="56" fill="{DO}"/><circle cx="60" cy="60" r="56" fill="none" stroke="{KEM}" stroke-width="4"/>'
    if kind == "zalo":
        s += T("Zalo", 26, 60, 70, KEM, "xb", "middle")
    else:
        s += f'<path d="M42,36 l12,-4 l8,18 l-8,6 c4,10 10,16 20,20 l6,-8 l18,8 l-4,12 c-30,4 -56,-22 -52,-52 z" fill="{KEM}"/>'
    return S(120, 120, s, kind)


def all_files():
    f = {"favicon.svg": favicon(), "app-icon.svg": app_icon(), "og-chia-se-1200x630.svg": og(), "bang-keu-goi-1920x360.svg": cta(),
         "nut-zalo.svg": nut_noi("zalo"), "nut-goi.svg": nut_noi("goi")}
    for i in range(3):
        f[f"banner-{i + 1}-1920x720.svg"] = hero(i); f[f"banner-{i + 1}-dien-thoai-750x1000.svg"] = hero_mobile(i)
        f[f"danh-muc-{i + 1}-1200x400.svg"] = danh_muc(i)
    for i in range(len(PRODS)):
        f[f"san-pham-{i + 1}-800x800.svg"] = the_sp(i)
    for k, v in ICONS.items():
        f[f"icon-{k}.svg"] = v
    for i, p in enumerate(PAGES):
        f[f"trang-{p[0]}-1920x480.svg"] = trang_con(i)
    return f


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for n, s in all_files().items():
        open(os.path.join(out, n), "w").write(s)
    print(len(os.listdir(out)))

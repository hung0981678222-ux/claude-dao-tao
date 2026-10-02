"""Bài đăng Facebook 05/10–18/10/2026 – trang "Ẩm Thực An Tâm", khung mẫu Điểm Chỉ ("Ứng dụng An Tâm").
Chưa có ảnh/video thật trong phiên → mọi chỗ ảnh là "KHUNG ẢNH THẬT" (không dùng ảnh mạng/AI thay ảnh thật).
Reels: ảnh bìa + bộ lớp chữ PNG nền trong suốt để đặt lên video thật khi dựng + thẻ kết.
Chạy: python3 fanpage_1018.py OUTDIR
"""
import os
import sys

import build_van as B
import fanpage_t10 as P

V, T, place, doc, khung_anh, cham = P.V, P.T, P.place, P.doc, P.khung_anh, P.cham
DO, DO2, KEM, MUC, NGO = P.DO, P.DO2, P.KEM, P.MUC, P.NGO
HOTLINE = "0398 431 300"
SLOGAN = "Mỗi mẻ bánh, một lời cam kết"
SIZES = [("22", "Taco, quesadilla"), ("25", "Wrap gà, cuốn salad"), ("28", "Burrito, wrap thịt"), ("31", "Doner kebab cuốn, burrito lớn")]
LOAI = "Tươi · Nướng · Nguyên cám"


# ---------------------------------------------------------------- khung bài ảnh 1080×1350
def khung(kicker, body, label, w=1080, h=1350):
    s = f'<rect width="{w}" height="{h}" fill="{KEM}"/>'
    s += f'<rect width="{w}" height="150" fill="{DO}"/>' + T(kicker, 26, 56, 88, NGO, "xb", track=.2, maxw=560)
    s += place(V.logo_ngang(KEM, KEM), w - 44 - 290, 26, 290, 103)
    s += body
    s += f'<rect y="{h - 96}" width="{w}" height="96" fill="{DO}"/>' + V.van_tay(78, h - 48, 26, KEM, seed=31, rings=7)
    s += T(SLOGAN, 27, 122, h - 38, KEM, "xb", maxw=420)
    s += T(f"Hotline/Zalo {HOTLINE}  ·  antamfoods.com", 25, w - 50, h - 38, KEM, "md", "end", maxw=470)
    return doc(w, h, s, label)


def chip3(items, y, h=118, w=1080):
    cw = (w - 112 - 2 * 16) / 3; s = ""
    for i, t in enumerate(items):
        x = 56 + i * (cw + 16); a, b = t.split("|")
        s += f'<rect x="{x}" y="{y}" width="{cw}" height="{h}" rx="16" fill="{DO}"/>' + cham(x + 38, y + h / 2, 17, KEM)
        s += T(a, 26, x + 68, y + h / 2 - 5, KEM, "xb", maxw=cw - 82) + T(b, 26, x + 68, y + h / 2 + 28, NGO, "xb", maxw=cw - 82)
    return s


def bai_0510():
    b = T("Chào bạn, đây là", 54, 56, 250, MUC, "xb") + T("Ẩm Thực An Tâm", 104, 52, 362, DO, "xb", maxw=970)
    b += khung_anh(56, 400, 968, 690, "Chồng bánh tortilla tại xưởng An Tâm")
    b += chip3(["Dây chuyền tự động|khép kín", "Chất lượng đều tay|mọi mẻ", "Giá xưởng,|nói thẳng, rõ ràng"], 1116)
    return khung("TRANG CHÍNH THỨC", b, "Chào bạn, đây là Ẩm Thực An Tâm")


def size_bia():
    b = T("Chọn size vỏ bánh", 62, 56, 250, MUC, "xb") + T("cho món của quán", 62, 56, 326, DO, "xb")
    y = 370
    for i, (cm, mon) in enumerate(SIZES):
        yy = y + i * 128; r = 22 + i * 8
        b += f'<rect x="56" y="{yy}" width="590" height="112" rx="16" fill="#fff"/><circle cx="118" cy="{yy + 56}" r="{r}" fill="{DO}"/>'
        b += T(f"{cm} cm", 44, 178, yy + 54, DO, "xb") + T(mon, 24, 178, yy + 90, MUC, "md", maxw=450)
    b += khung_anh(668, y, 356, 496, "4 size vỏ bánh thật xếp cạnh nhau")
    b += f'<rect x="56" y="{y + 520}" width="968" height="96" rx="48" fill="{DO}"/>'
    b += T(f"15 chiếc / túi  ·  {LOAI}", 32, 540, y + 580, KEM, "xb", "middle", maxw=900)
    b += T("Vuốt để xem từng size  →", 28, 540, y + 690, MUC, "md", "middle")
    return khung("BẢNG SIZE TORTILLA · 1/5", b, "Album bảng size – bìa")


def size_tam(i):
    cm, mon = SIZES[i]
    b = ""
    for j, (c, _) in enumerate(SIZES):
        on = j == i; x = 56 + j * 150
        b += f'<rect x="{x}" y="186" width="136" height="54" rx="27" fill="{DO if on else "none"}" stroke="{DO}" stroke-width="3"/>' + T(f"{c} cm", 26, x + 68, 222, KEM if on else DO, "xb", "middle")
    b += T(cm, 230, 56, 470, DO, "xb") + T("cm", 80, 56 + V.text(cm, 230, "xb")[1] + 20, 470, MUC, "xb")
    b += T("Hợp món:", 30, 1024, 380, MUC, "md", "end") + T(mon, 40, 1024, 432, DO, "xb", "end", maxw=520)
    b += khung_anh(56, 512, 968, 600, f"Vỏ bánh {cm} cm thật cạnh thước đo + món phù hợp")
    b += f'<rect x="56" y="1136" width="968" height="86" rx="43" fill="#fff"/>' + T(f"15 chiếc / túi  ·  {LOAI}", 30, 540, 1190, MUC, "xb", "middle", maxw=900)
    return khung(f"BẢNG SIZE TORTILLA · {i + 2}/5", b, f"Album bảng size – {cm} cm")


def nang_luc():
    b = T("Năng lực sản xuất", 70, 56, 262, DO, "xb") + T("Số liệu thật của xưởng An Tâm", 30, 56, 312, MUC, "md")
    tiles = [("4 size", "22 · 25 · 28 · 31 cm", False), ("15 chiếc", "mỗi túi tortilla", False),
             ("3 loại tortilla", LOAI, False), ("4 loại vỏ kebab", "Bánh vàng · Mè đen · Mè trắng · Than tre", False),
             ("[cần bổ sung]", "chiếc / ngày – công suất", True), ("[cần bổ sung]", "dây chuyền tự động khép kín", True)]
    tw, th = 476, 176
    for i, (big, small, todo) in enumerate(tiles):
        x = 56 + (i % 2) * (tw + 16); y = 350 + (i // 2) * (th + 16)
        st = 'stroke-dasharray="10 8" stroke="#8A6F63" stroke-width="3"' if todo else ""
        b += f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="18" fill="{"#fff" if todo else DO}" {st}/>'
        b += T(big, 50, x + 30, y + 82, DO if todo else KEM, "xb", maxw=tw - 60) + T(small, 25, x + 30, y + 130, MUC if todo else "#FFE1DE", "md", maxw=tw - 60)
    b += khung_anh(56, 950, 968, 290, "Dây chuyền tự động tại xưởng")
    return khung("NĂNG LỰC · XƯỞNG AN TÂM", b, "Infographic năng lực sản xuất")


def khach_noi():
    b = T("Khách nói gì", 70, 56, 262, MUC, "xb") + T("về An Tâm", 70, 56, 346, DO, "xb")
    for i in range(3):
        y = 392 + i * 280
        b += f'<rect x="56" y="{y}" width="968" height="260" rx="20" fill="#fff"/>'
        b += khung_anh(80, y + 24, 212, 212, "Ảnh quán / chủ quán", r=106, k=.55)
        b += T("“", 120, 320, y + 110, DO, "xb") + T("[Trích nguyên văn đánh giá thật]", 34, 380, y + 100, MUC, "xb", maxw=610)
        b += T("[Đánh giá thật – dòng 2 nếu cần]", 28, 380, y + 146, MUC, "md", maxw=610)
        b += T("— [Tên quán · khu vực]  ·  đã đồng ý đăng", 24, 380, y + 206, DO, "xb", maxw=610)
    return khung("ĐỐI TÁC CỦA AN TÂM", b, "Khách nói gì về An Tâm")


# ---------------------------------------------------------------- Reels 1080×1920
SAFE_T, SAFE_B = 250, 340


def nen_reel():
    return place(B.nen_van(1080, 1920), 0, 0, 1080, 1920)


def bia_reel(so, ngay, lines, mo_ta):
    s = nen_reel()
    cy0, cy1 = SAFE_T + 40, 1920 - SAFE_B - 40
    s += f'<rect x="72" y="{cy0}" width="936" height="{cy1 - cy0}" rx="32" fill="{KEM}"/>'
    s += place(V.logo_ngang(), 540 - 150, cy0 + 34, 300, 107)
    s += T(f"REEL {so}  ·  {ngay}", 26, 540, cy0 + 196, DO, "xb", "middle", .2)
    for j, t in enumerate(lines):
        s += T(t, 74, 540, cy0 + 290 + j * 86, MUC if j < len(lines) - 1 or len(lines) == 1 else DO, "xb", "middle", maxw=840)
    fy = cy0 + 290 + len(lines) * 86 - 40
    s += khung_anh(120, fy, 840, cy1 - 110 - fy, mo_ta, r=20)
    s += T(f"Hotline/Zalo {HOTLINE}  ·  antamfoods.com", 26, 540, cy1 - 44, MUC, "md", "middle")
    return doc(1080, 1920, s, f"Bìa Reel {so}")


def the_ket():
    s = nen_reel()
    s += f'<rect x="72" y="560" width="936" height="800" rx="32" fill="{KEM}"/>' + place(V.logo_dung(), 540 - 230, 610, 460, 400)
    s += T(SLOGAN, 46, 540, 1110, DO, "xb", "middle", maxw=840)
    s += T(f"Hotline/Zalo {HOTLINE}", 40, 540, 1200, MUC, "xb", "middle") + T("antamfoods.com", 34, 540, 1258, MUC, "md", "middle")
    return doc(1080, 1920, s, "Thẻ kết Reels")


def lop_buoc(n, tong, text):
    """Lớp chữ trong suốt: nhãn bước ở vùng dưới an toàn (y ≈ 1400–1520)."""
    y = 1920 - SAFE_B - 170
    w = min(900, 200 + V.text(text, 46, "xb")[1])
    x = 540 - w / 2
    s = f'<rect x="{x}" y="{y}" width="{w}" height="116" rx="58" fill="{KEM}"/>'
    s += f'<circle cx="{x + 58}" cy="{y + 58}" r="42" fill="{DO}"/>' + T(str(n), 44, x + 58, y + 74, KEM, "xb", "middle")
    s += T(text, 46, x + 118, y + 74, MUC, "xb", maxw=w - 150)
    s += T(f"{n}/{tong}", 22, x + w - 30, y + 106, DO, "xb", "end") if tong > 1 else ""
    return doc(1080, 1920, s, f"Lớp chữ bước {n}")


def lop_dem(n):
    """Lớp đếm cho R2: số lớn góc phải trên vùng an toàn."""
    s = f'<rect x="760" y="{SAFE_T + 20}" width="250" height="170" rx="28" fill="{KEM}"/>'
    s += T(f"{n}", 110, 870, SAFE_T + 150, DO, "xb", "middle") + T("/10", 40, 960, SAFE_T + 150, MUC, "xb", "middle")
    return doc(1080, 1920, s, f"Đếm {n}/10")


def lop_ten(ten, vai):
    y = 1920 - SAFE_B - 210
    s = f'<rect x="72" y="{y}" width="760" height="156" rx="24" fill="{KEM}"/><rect x="72" y="{y}" width="16" height="156" rx="8" fill="{DO}"/>'
    s += T(ten, 46, 118, y + 70, MUC, "xb", maxw=680) + T(vai, 30, 118, y + 120, DO, "md", maxw=680)
    return doc(1080, 1920, s, "Lớp tên khách")


REELS = [
    ("R1", "06/10", "r1-vo-banh-lam-the-nay", ["Vỏ bánh quán bạn", "được làm thế này"], "Dây chuyền: bột vào máy → ép → nướng",
     ["Bột vào máy", "Ép bánh", "Nướng", "Làm nguội", "Xếp chồng", "Đóng gói"]),
    ("R2", "08/10", "r2-cuon-10-kebab", ["Cuốn 10 cái kebab", "không rách cái nào"], "Góc máy cố định: tay cuốn kebab", None),
    ("R3", "10/10", "r3-mo-tiem-doner", ["Mở tiệm Doner Kebab", "cần những gì?"], "Một ngày ở cửa hàng đối tác",
     ["Chuẩn bị quầy & nguyên liệu", "Lò quay thịt doner", "Vỏ bánh An Tâm", "Giờ cao điểm", "[Điều chủ quán muốn nói]"]),
    ("R4", "13/10", "r4-kiem-tra-tung-me", ["Kiểm tra chất lượng", "từng mẻ"], "Đo đường kính · cân · gập thử",
     ["Đo đường kính", "Cân từng chiếc", "Gập thử – không nứt"]),
    ("R5", "15/10", "r5-3-mon-1-tortilla", ["3 món", "từ 1 chiếc tortilla"], "Wrap gà · taco · quesadilla",
     ["Wrap gà", "Taco", "Quesadilla"]),
    ("R6", "17/10", "r6-chu-xe-banh-mi", ["Chủ xe bánh mì", "kể chuyện"], "Khách thật kể chuyện (đã đồng ý)", None),
]


def all_items():
    """(bài, ngày, slug, svg, ghi chú ảnh thật cần có)"""
    out = [("1. Ảnh – Chào bạn", "T2 05/10", "b01-0510-chao-ban", bai_0510(), "Chồng bánh tortilla tại xưởng")]
    r = {x[0]: x for x in REELS}

    def reel(idx, title, so):
        _, ngay, slug, lines, mo, steps = r[so]
        items = [(title, ngay, f"{idx}-{slug}-bia", bia_reel(so, ngay, lines, mo), mo)]
        if steps:
            for k, t in enumerate(steps, 1):
                items.append((title, ngay, f"{idx}-{slug}-lop-{k}", lop_buoc(k, len(steps), t), "lớp chữ đặt lên video"))
        if so == "R2":
            for k in range(1, 11):
                items.append((title, ngay, f"{idx}-{slug}-dem-{k:02d}", lop_dem(k), "lớp đếm đặt lên video"))
        if so == "R6":
            items.append((title, ngay, f"{idx}-{slug}-lop-ten", lop_ten("[Tên anh/chị]", "Chủ xe bánh mì [tên xe] · [khu vực]"), "lớp tên khách"))
        return items

    out += reel("b02", "2. Reel R1 – Vỏ bánh làm thế này", "R1")
    out += reel("b03", "3. Reel R2 – Cuốn 10 kebab", "R2")
    out.append(("4. Album bảng size", "T6 09/10", "b04-0910-size-1-bia", size_bia(), "4 size vỏ bánh thật xếp cạnh nhau"))
    for i, (cm, _) in enumerate(SIZES):
        out.append(("4. Album bảng size", "T6 09/10", f"b04-0910-size-{i + 2}-{cm}cm", size_tam(i), f"Vỏ {cm} cm cạnh thước + món"))
    out += reel("b05", "5. Reel R3 – Mở tiệm Doner", "R3")
    out.append(("6. Ảnh – Năng lực sản xuất", "T2 12/10", "b06-1210-nang-luc", nang_luc(), "Dây chuyền tự động"))
    out += reel("b07", "7. Reel R4 – Kiểm tra từng mẻ", "R4")
    out += reel("b08", "8. Reel R5 – 3 món từ 1 tortilla", "R5")
    out.append(("9. Ảnh – Khách nói gì", "T6 16/10", "b09-1610-khach-noi", khach_noi(), "Ảnh 3 quán đối tác + đánh giá thật"))
    out += reel("b10", "10. Reel R6 – Chủ xe bánh mì", "R6")
    out.append(("Chung cho mọi Reels", "—", "the-ket-reels", the_ket(), "thẻ kết 2–3 giây cuối video"))
    return out


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for _, _, slug, s, _ in all_items():
        open(os.path.join(out, slug + ".svg"), "w").write(s)
    print(len(all_items()))

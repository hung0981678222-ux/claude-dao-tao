"""Ảnh fanpage tuần 05–11/10/2026 – Ẩm Thực An Tâm, nhận diện Điểm Chỉ (logo vân tay + font An Tam Tron Banh).
Mọi khung "KHUNG ẢNH THẬT" là chỗ chèn ảnh chụp thật – không dùng hình minh hoạ thay ảnh thật.
Chạy: python3 fanpage_t10.py OUTDIR  → OUTDIR/<slug>.svg
"""
import os
import sys

import build_chuan as C

V = C.V
DO, DO2, KEM, MUC, NGO, GIAY = V.DO, V.DO2, V.KEM, V.MUC, V.NGO, V.GIAY
HOTLINE = "0398 431 300"   # hotline duy nhất – đã chốt 03/10/2026
CHAN = f"Ẩm Thực An Tâm  |  Hotline/Zalo: {HOTLINE}  |  antamfoods.com"


def T(t, size, x, y, fill=MUC, k="xb", anchor="start", track=0.0, maxw=None):
    if maxw:
        w = V.text(t, size, k, 0, 0, fill, anchor, track)[1]
        if w > maxw:
            size *= maxw / w
    return V.text(t, size, k, x, y, fill, anchor, track)[0]


def place(svg, x, y, w, h):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


def doc(w, h, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">{body}</svg>'


def logo(w, light=False):
    """Logo ngang góc phải trên, rộng 300 px."""
    lw = 300; lh = lw * 230 / 646
    svg = V.logo_ngang(KEM, KEM) if light else V.logo_ngang()
    return place(svg, w - 44 - lw, 40, lw, lh)


def chan(w, h, bg=DO):
    return f'<rect y="{h - 78}" width="{w}" height="78" fill="{bg}"/>' + T(CHAN, 25, w / 2, h - 30, KEM, "md", "middle", maxw=w - 80)


def khung_anh(x, y, w, h, mo_ta, dark=False, r=18, cy=None, k=None):
    """Khung chèn ảnh thật: nền kẻ chéo nhạt, viền đứt, biểu tượng máy ảnh, nhãn."""
    pid = f"kh{x}{y}{w}"
    c1, c2, ink = ("#3A2A27", "#4A3733", "#F3D9C9") if dark else ("#EFE3D3", "#E6D6C2", "#8A6F63")
    cx = x + w / 2; cy = cy or y + h / 2
    s = (f'<defs><pattern id="{pid}" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<rect width="22" height="22" fill="{c1}"/><rect width="11" height="22" fill="{c2}"/></pattern></defs>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="url(#{pid})"/>'
         f'<rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{h - 12}" rx="{r - 4}" fill="none" stroke="{ink}" stroke-width="3" stroke-dasharray="14 10"/>')
    k = k or min(1, h / 330)
    s += (f'<g transform="translate({cx} {cy - 34 * k}) scale({k})"><rect x="-46" y="-30" width="92" height="64" rx="12" fill="none" stroke="{ink}" stroke-width="6"/>'
          f'<rect x="-18" y="-42" width="36" height="14" rx="4" fill="{ink}"/><circle r="17" fill="none" stroke="{ink}" stroke-width="6"/></g>')
    s += T("KHUNG ẢNH THẬT", 30 * max(k, .7), cx, cy + 40 * k + 8, ink, "xb", "middle", .12)
    s += T(mo_ta, 22 * max(k, .75), cx, cy + 76 * k + 10, ink, "md", "middle", maxw=w - 60)
    return s


def cham(x, y, r=13, fill=DO):
    return V.van_tay(x, y, r, fill, seed=31, rings=6)


# =========================== 1) BÀI 05/10 – RA MẮT NHẬN DIỆN ===========================
Y_RA_MAT = ["Dây chuyền tự động|khép kín", "Chất lượng ổn định|mọi lô", "Giá xưởng|tối ưu"]


def ra_mat(w, h):
    s = f'<rect width="{w}" height="{h}" fill="{KEM}"/>' + logo(w)
    tall = h > 1100
    y0 = 236 if tall else 222
    s += T("NHÀ BÁNH MÌ GIỜ LÀ", 52, 60, y0, MUC, "xb", track=.02, maxw=w - 120)
    s += T("ẨM THỰC AN TÂM", 104 if tall else 96, 56, y0 + (112 if tall else 100), DO, "xb", maxw=w - 112)
    s += T("Nhà sản xuất vỏ bánh Tortillas, Taco & Kebab", 36 if tall else 33, 60, y0 + (172 if tall else 152), MUC, "md", maxw=w - 120)
    fy = y0 + (215 if tall else 190); fh = (h - 78 - 170) - fy if tall else (h - 78 - 140) - fy
    s += khung_anh(60, fy, w - 120, fh, "Chồng bánh tortilla tại xưởng An Tâm")
    cy = fy + fh + 26; cw = (w - 120 - 2 * 18) / 3; ch = (h - 78 - 30) - cy
    for i, t in enumerate(Y_RA_MAT):
        x = 60 + i * (cw + 18); a, b = t.split("|")
        s += f'<rect x="{x}" y="{cy}" width="{cw}" height="{ch}" rx="16" fill="{DO}"/>' + cham(x + 36, cy + ch / 2, 16, KEM)
        s += T(a, 26, x + 64, cy + ch / 2 - 4, KEM, "xb", maxw=cw - 80) + T(b, 26, x + 64, cy + ch / 2 + 28, NGO, "xb", maxw=cw - 80)
    return doc(w, h, s + chan(w, h), "Ra mắt nhận diện Ẩm Thực An Tâm")


# =========================== 2) BÀI 09/10 – ALBUM SIZE ===========================
SIZES = [("Mini", "taco, khai vị"), ("Nhỏ", "taco, quesadilla"), ("Vừa", "burrito, wrap gà, cuốn salad"), ("Lớn", "Doner kebab cuốn, burrito lớn")]


def thang_size(x, y, active=None, scale=1.0):
    """Bốn vòng tròn tăng dần (sơ đồ so sánh size, không phải ảnh). active = chỉ số đang nói."""
    s = ""; cx = x
    for i, (n, _) in enumerate(SIZES):
        r = (16 + i * 7) * scale
        on = active is None or i == active
        s += f'<circle cx="{cx + r}" cy="{y}" r="{r}" fill="{DO if on else "none"}" stroke="{DO}" stroke-width="{3 * scale}"/>'
        s += T(n.upper(), 15 * scale, cx + r, y + r + 24 * scale, DO if on else "#B9A79C", "xb", "middle", .08)
        cx += 2 * r + 22 * scale
    return s


def size_bia():
    w = h = 1080
    s = f'<rect width="{w}" height="{h}" fill="{KEM}"/>' + logo(w)
    s += T("CHỌN SIZE VỎ BÁNH NÀO", 60, 60, 238, DO, "xb", maxw=960) + T("CHO MÓN CỦA QUÁN BẠN?", 60, 60, 310, MUC, "xb", maxw=960)
    ty = 352; rh = 112
    for i, (n, mon) in enumerate(SIZES):
        y = ty + i * (rh + 12); r = 18 + i * 7
        s += f'<rect x="60" y="{y}" width="600" height="{rh}" rx="16" fill="#fff"/>'
        s += f'<circle cx="{116}" cy="{y + rh / 2}" r="{r}" fill="{DO}"/>'
        s += T(f"Size {n}", 34, 170, y + 48, DO, "xb") + T("[__] cm", 34, 640, y + 48, MUC, "xb", "end")
        s += T(mon[0].upper() + mon[1:], 23, 170, y + 86, MUC, "md", maxw=470)
    s += khung_anh(684, ty, 336, 4 * rh + 36, "4 size vỏ bánh xếp cạnh nhau")
    return doc(w, h, s + chan(w, h), "Album size vỏ bánh – bìa")


def size_tam(i):
    w = h = 1080; n, mon = SIZES[i]
    s = f'<rect width="{w}" height="{h}" fill="{KEM}"/>' + logo(w)
    s += thang_size(60, 98, i, 1.0)
    s += T(f"SIZE {n.upper()}", 92, 60, 290, DO, "xb")
    s += T("[__] cm", 92, 1020, 290, MUC, "xb", "end")
    s += T("Món: " + mon, 38, 60, 352, MUC, "md", maxw=960)
    last = i == len(SIZES) - 1
    fy = 392; fh = (h - 78 - 32) - fy - (96 if last else 0)
    s += khung_anh(60, fy, 960, fh, "Vỏ bánh cạnh thước đo + món tương ứng")
    if last:
        s += f'<rect x="60" y="{fy + fh + 22}" width="960" height="76" rx="38" fill="{DO}"/>' + cham(112, fy + fh + 60, 18, KEM)
        s += T("Inbox An Tâm để được tư vấn size", 36, 560, fy + fh + 73, KEM, "xb", "middle")
    return doc(w, h, s + chan(w, h), f"Album size vỏ bánh – size {n}")


# =========================== 3) ẢNH BÌA REELS ===========================
REELS = [
    ("r1-06-10", ["Vỏ bánh quán bạn", "được làm thế này?"], "Dây chuyền sản xuất vỏ bánh tại xưởng"),
    ("r2-08-10", ["Thử thách:", "cuốn 10 cái kebab", "không rách"], "Tay cuốn kebab – cảnh quay thử thách"),
    ("r3-10-10", ["Mở tiệm Doner Kebab", "cần những gì?"], "Quầy doner kebab / nguyên liệu bày sẵn"),
]


def reel(lines, mo_ta):
    w, h = 1080, 1920
    s = khung_anh(0, 0, w, h, mo_ta, dark=True, r=0, cy=420, k=1.6)
    s += f'<rect width="{w}" height="{h}" fill="#231716" opacity=".18"/>' + logo(w, light=True)
    # khối chữ trong vùng an toàn giữa khung (y 640–1280 – vẫn đọc được khi lưới trang cắt 1:1 hoặc 4:5)
    n = len(lines); lh = 104; bh = n * lh + 92; by = 960 - bh / 2
    s += f'<rect x="90" y="{by}" width="900" height="{bh}" rx="28" fill="{DO}"/>'
    s += f'<circle cx="540" cy="{by}" r="44" fill="{KEM}"/>' + cham(540, by, 32, DO)
    for j, t in enumerate(lines):
        s += T(t, 86, 540, by + 60 + (j + 1) * lh - 22, KEM if j or n == 2 else NGO, "xb", "middle", maxw=820)
    return doc(w, h, s + chan(w, h, DO2), "Ảnh bìa Reels")


def all_items():
    items = [("bai-05-10", "Ra mắt nhận diện", "1080x1350", "ra-mat-1080x1350", ra_mat(1080, 1350)),
             ("bai-05-10", "Ra mắt nhận diện", "1080x1080", "ra-mat-1080x1080", ra_mat(1080, 1080)),
             ("bai-09-10", "Album size – Tấm 1 (bìa)", "1080x1080", "size-1-bia", size_bia())]
    for i, (n, _) in enumerate(SIZES):
        items.append(("bai-09-10", f"Album size – Tấm {i + 2} (Size {n})", "1080x1080", f"size-{i + 2}-{n.lower().replace('ỏ', 'o').replace('ừ', 'u').replace('ớ', 'o')}", size_tam(i)))
    for slug, lines, mo in REELS:
        items.append(("reels", f"Bìa Reels {slug[1]} ({slug[3:5]}/10)", "1080x1920", f"reels-{slug}", reel(lines, mo)))
    return items


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for _, cap, size, slug, s in all_items():
        open(os.path.join(out, slug + ".svg"), "w").write(s); print(slug, size)

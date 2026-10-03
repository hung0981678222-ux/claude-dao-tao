"""Đồng phục Vân lan (chốt 03/10/2026) – bản chi tiết gửi nhà may: mặt trước, mặt sau, thông số."""
import ao2 as A
import ao3 as G
import ao4 as F

V = A.V
DO, DO2, KEM, MUC, NGO, TRANG = A.DO, A.DO2, A.KEM, A.MUC, A.NGO, A.TRANG
W, fit, mark, nen, bong, S, _P = A.W, A.fit, A.mark, A.nen, A.bong, A.S, A._P
HOTLINE = "0398 431 300"


def chu_thich(x0, y0, x1, y1, txt, anchor="start"):
    o = f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{MUC}" stroke-width="1.2"/><circle cx="{x0}" cy="{y0}" r="3.5" fill="{MUC}"/>'
    o += W(txt, 13, x1 + (6 if anchor == "start" else -6), y1 + 4, MUC, "md", anchor)
    return o


def mau(x, y):
    o = W("MÀU", 12, x, y, DO, "xb", track=.2)
    for i, (n, c, ma) in enumerate((("Đỏ An Tâm", DO, "#D2141E"), ("Kem giấy", KEM, "#FFF6EA"), ("Đỏ đậm", DO2, "#8F0D14"), ("Mực", MUC, "#231716"))):
        yy = y + 14 + i * 30
        o += f'<rect x="{x}" y="{yy}" width="22" height="22" rx="4" fill="{c}" stroke="#ccc"/>' + W(f"{n}  {ma}", 12, x + 30, yy + 16, MUC, "md")
    return o + W("Pantone: [chốt khi in thử]", 11, x, y + 140, "#8a7a74", "md")


def sheet(title, sub, body, notes, u, w=1400, h=860):
    s = nen(w, h, u) + A._defs(u)
    s += f'<rect x="1000" y="0" width="400" height="{h}" fill="#fff"/>'
    s += W(title, 30, 40, 56, DO, "xb") + W(sub, 15, 40, 84, "#6b5a55", "md") + body
    s += W("THÔNG SỐ", 12, 1030, 56, DO, "xb", track=.2)
    for i, (k, v) in enumerate(notes):
        yy = 86 + i * 46
        s += W(k, 13, 1030, yy, MUC, "xb") + W(v, 12.5, 1030, yy + 19, "#4a3a36", "md")
    s += mau(1030, h - 190)
    s += fit(V.logo_ngang(), 1300, h - 40, w=140)
    return S(w, h, s, title)


def ao_thun():
    u = "f1"; ts = 1.45
    cx1, cx2, cy = 260, 740, 430
    b = bong(cx1, cy + 238, 190, 16, u) + bong(cx2, cy + 238, 190, 16, u)
    b += G.garm(cx1, cy, ts, KEM, u, "t", A.TEE, F.gon(cx1 + 52 * ts, cy - 96 * ts, 12, 12, DO, 3.2, .06)) + A._co_tron(cx1, cy, ts, DO)
    b += W("An Tâm", 19, cx1 + 52 * ts, cy - 96 * ts + 48, DO, "xb", "middle")
    b += G.garm(cx2, cy, ts, KEM, u, "b", A.TEE_BACK, F.gon(cx2, cy - 20, 15, 14, DO, 3.4, .06, seed=8)) + A._co_tron(cx2, cy, ts, DO, back=True)
    b += f'<rect x="{cx2 - 110}" y="{cy - 92}" width="220" height="150" rx="12" fill="{KEM}"/>'
    b += fit(V.logo_dung(), cx2, cy - 18, w=150)
    b += f'<rect x="{cx2 - 86}" y="{cy + 92}" width="172" height="34" rx="17" fill="{DO}"/>' + W("NHÂN VIÊN", 14, cx2, cy + 115, KEM, "xb", "middle", .25)
    b += W("Mỗi mẻ bánh, một lời cam kết", 15, cx2, cy + 160, DO, "xb", "middle")
    b += chu_thich(cx1 + 52 * ts, cy - 96 * ts, cx1 + 210, cy - 250, "Chấm tâm Ø 2 cm")
    b += chu_thich(cx1 + 100, cy - 60, cx1 + 210, cy - 222, "Vân lan Ø ~24 cm, nhạt dần")
    b += chu_thich(cx2 + 86, cy + 109, cx2 + 150, cy + 60, "Nhãn bộ phận")
    b += W("MẶT TRƯỚC", 13, cx1, cy + 280, "#8A6F63", "xb", "middle", .22) + W("MẶT SAU", 13, cx2, cy + 280, "#8A6F63", "xb", "middle", .22)
    notes = [("Vải", "Cotton 65/35 hoặc CVC, 180–200 gsm, màu Kem"),
             ("Cổ & bo", "Bo gân Đỏ An Tâm, rộng 2 cm"),
             ("Ngực trái", "Chấm tâm Ø 2 cm + vân lan Ø 24 cm + chữ An Tâm"),
             ("Kỹ thuật in", "In chuyển nhiệt DTF (giữ độ nhạt dần) – không in lụa"),
             ("Lưng", "Vân lan Ø 30 cm, khung kem, logo đứng rộng 18 cm"),
             ("Nhãn bộ phận", "NHÂN VIÊN / GIAO HÀNG / BẾP / XƯỞNG"),
             ("Câu thương hiệu", "Mỗi mẻ bánh, một lời cam kết – cao chữ 2,5 cm"),
             ("Size", "S–XXL; bảng size: [Cần điền theo nhà may]")]
    return sheet("Áo thun nhân viên · Vân lan", "Nền kem, vòng vân son toả ra từ chấm tâm ở ngực – áo như vừa được điểm chỉ.", b, notes, u)


def ao_polo():
    u = "f2"; ts = 1.45
    cx1, cx2, cy = 260, 740, 430
    b = bong(cx1, cy + 232, 180, 16, u) + bong(cx2, cy + 232, 180, 16, u)
    b += G.garm(cx1, cy, ts, TRANG, u, "p", A.POLO, F.gon(cx1 + 52 * ts, cy - 88 * ts, 8, 10, DO, 2.2, .1)) + G.collar_polo(cx1, cy, ts, DO, u)
    b += W("An Tâm", 15, cx1 + 52 * ts, cy - 88 * ts + 36, DO, "xb", "middle")
    b += G.garm(cx2, cy, ts, TRANG, u, "q", A.POLO, "")
    b += f'<path d="{_P(cx2, cy, ts, "M -40,-150 C -20,-160 20,-160 40,-150")}" fill="none" stroke="{DO}" stroke-width="{9 * ts}" stroke-linecap="round"/>'
    b += f'<path d="{_P(cx2, cy, ts, "M -44,-150 C -20,-138 20,-138 44,-150 L 40,-128 C 18,-118 -18,-118 -40,-128 Z")}" fill="{DO}"/>'
    b += f'<rect x="{cx2 - 92}" y="{cy - 140}" width="184" height="30" rx="6" fill="{TRANG}"/>' + W("ẨM THỰC AN TÂM", 14, cx2, cy - 119, DO, "xb", "middle", .3)
    for sg in (-1, 1):
        b += f'<path d="{_P(cx1, cy, ts, f"M {sg * 146},-100 L {sg * 124},-50")}" stroke="{DO}" stroke-width="{8 * ts}"/>'
        b += f'<path d="{_P(cx2, cy, ts, f"M {sg * 146},-100 L {sg * 124},-50")}" stroke="{DO}" stroke-width="{8 * ts}"/>'
    b += chu_thich(cx1 + 52 * ts, cy - 88 * ts, cx1 + 200, cy - 250, "Chấm tâm thêu Ø 1,5 cm")
    b += chu_thich(cx1 + 110, cy - 90, cx1 + 200, cy - 222, "Vân lan in Ø 14 cm, nét mảnh")
    b += chu_thich(cx2 + 70, cy - 124, cx2 + 150, cy - 40, "Thêu sau cổ")
    b += W("MẶT TRƯỚC", 13, cx1, cy + 280, "#8A6F63", "xb", "middle", .22) + W("MẶT SAU", 13, cx2, cy + 280, "#8A6F63", "xb", "middle", .22)
    notes = [("Vải", "Cá sấu cotton 4 chiều, 220 gsm, màu trắng kem"),
             ("Cổ, chân cổ, viền tay", "Bo dệt Đỏ An Tâm"),
             ("Nẹp", "3 cúc đỏ, nẹp dài 12 cm"),
             ("Ngực trái", "Chấm tâm thêu Ø 1,5 cm + vân lan in Ø 14 cm"),
             ("Kỹ thuật", "Vân lan: in DTF mỏng; chấm tâm + chữ: thêu chỉ đỏ"),
             ("Sau cổ", "Thêu ẨM THỰC AN TÂM, cao chữ 1,2 cm"),
             ("Dùng cho", "Văn phòng, bán hàng, gặp đối tác"),
             ("Size", "Nam/nữ S–XXL; bảng size: [Cần điền]")]
    return sheet("Áo văn phòng (polo) · Vân lan", "Polo trắng kem, cổ và viền tay đỏ; vân lan nhỏ, nét mảnh ở ngực – lịch sự, vẫn đúng chất điểm chỉ.", b, notes, u)


def tap_de():
    u = "f3"
    cx1, cy1, s1 = 300, 440, 1.25
    cx2, cy2, s2 = 760, 470, 1.15
    b = bong(cx1, cy1 + 300, 170, 16, u) + bong(cx2, cy2 + 160, 180, 14, u)
    b += G.tie(cx1, cy1, s1, KEM) + G.garm(cx1, cy1, s1, DO, u, "a", G.APRON, F.gon(cx1, cy1 - 110 * s1, 22, 13, KEM, 3.4, .1), seams=False) + G.stitch(cx1, cy1, s1, KEM)
    b += W("An Tâm", 34, cx1, cy1 + 26 * s1, KEM, "xb", "middle") + W("Mỗi mẻ bánh, một lời cam kết", 14, cx1, cy1 + 56 * s1, KEM, "md", "middle")
    po = "M -92,92 L 92,92 L 92,170 C 92,178 86,182 80,182 L -80,182 C -86,182 -92,178 -92,170 Z"
    b += f'<path d="{_P(cx1, cy1, s1, po)}" fill="#000" opacity=".1"/><path d="{_P(cx1, cy1, s1, po + " M 0,92 L 0,182 M -30,92 L -30,182")}" fill="none" stroke="{KEM}" stroke-opacity=".7" stroke-width="2" stroke-dasharray="6 5"/>'
    # tạp dề ngang eo
    eo = "M -130,-40 L 130,-40 L 136,110 C 136,120 128,124 120,124 L -120,124 C -128,124 -136,120 -136,110 Z"
    b += f'<path d="{_P(cx2, cy2, s2, "M -130,-36 C -152,-34 -160,-16 -156,20 C -152,52 -162,74 -158,96 M 130,-36 C 152,-34 160,-16 156,20 C 152,52 162,74 158,96")}" fill="none" stroke="{KEM}" stroke-width="9" stroke-linecap="round"/>'
    b += G.garm(cx2, cy2, s2, DO, u, "e", eo, F.gon(cx2 - 70 * s2, cy2 + 30 * s2, 14, 12, KEM, 3, .1, seed=3), seams=False)
    b += f'<path d="{_P(cx2, cy2, s2, "M -130,-40 L 130,-40 L 130,-24 L -130,-24 Z")}" fill="{KEM}"/>'
    b += W("An Tâm", 26, cx2 + 50 * s2, cy2 + 40 * s2, KEM, "xb", "middle") + W(HOTLINE, 13, cx2 + 50 * s2, cy2 + 64 * s2, KEM, "md", "middle")
    b += chu_thich(cx1, cy1 - 110 * s1, cx1 + 190, cy1 - 300, "Chấm tâm Ø 3 cm – tâm vân lan")
    b += chu_thich(cx1 + 60, cy1 + 160, cx1 + 190, cy1 + 120, "Túi 3 ngăn, may lộ chỉ kem")
    b += W("TẠP DỀ YẾM – BẾP / QUẦY / XƯỞNG", 13, cx1, cy1 + 340, "#8A6F63", "xb", "middle", .18)
    b += W("TẠP DỀ NGANG EO – BÁN HÀNG", 13, cx2, cy2 + 200, "#8A6F63", "xb", "middle", .18)
    notes = [("Vải", "Kaki 65/35 chống thấm, màu Đỏ An Tâm"),
             ("Kích thước yếm", "70 × 85 cm; ngang eo 60 × 35 cm"),
             ("Dây", "Dây cổ chỉnh được, dây eo 90 cm, màu Kem"),
             ("Ngực", "Vân lan Kem Ø 30 cm, chấm tâm Ø 3 cm"),
             ("Kỹ thuật in", "In lụa Kem dạng tram nhạt dần, hoặc DTF"),
             ("Chữ", "An Tâm cao 5 cm + câu thương hiệu"),
             ("Túi", "Túi trước 3 ngăn (bút, sổ, điện thoại)"),
             ("Đường may", "Lộ chỉ Kem quanh viền")]
    return sheet("Tạp dề · Vân lan", "Nền Đỏ An Tâm, vòng vân kem lan ra từ chấm tâm ở ngực; thêm bản ngang eo cho nhân viên bán hàng.", b, notes, u)


ALL = [("ao-thun-van-lan", ao_thun), ("ao-van-phong-van-lan", ao_polo), ("tap-de-van-lan", tap_de)]

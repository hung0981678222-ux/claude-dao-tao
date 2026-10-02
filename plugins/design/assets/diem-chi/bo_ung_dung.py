"""Bộ ứng dụng nhận diện Ẩm Thực An Tâm (Điểm Chỉ): mạng xã hội, ấn phẩm văn phòng, bao bì, đồng phục, điểm bán.
Mỗi hàm trả về một SVG hoàn chỉnh. Chỗ trong [ ] là thông tin cần công ty điền thật.
"""
import math
import random

import build_chuan as C

V, B = C.V, C.B
DO, DO2, SON, KEM, GIAY, MUC, NGO = V.DO, V.DO2, V.SON, V.KEM, V.GIAY, V.MUC, V.NGO
KRAFT, KRAFT2 = "#CDA87C", "#B48C5E"


def W(t, size, x, y, fill=DO, k="xb", anchor="start", track=0.0):
    return V.text(t, size, k, x, y, fill, anchor, track)[0]


def place(svg, x, y, w, h, extra=""):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" {extra}', 1)


def S(w, h, body, label, bg=None):
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{r}{body}</svg>'


def shadow(i):
    return f'<defs><filter id="{i}" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#231716" flood-opacity=".22"/></filter></defs>'


def vt(cx, cy, r, fill=SON, seed=5, rings=11):
    return V.van_tay(cx, cy, r, fill, seed=seed, rings=rings)


LOGO_N = lambda: V.logo_ngang()
LOGO_NK = lambda: V.logo_ngang(KEM, KEM)
LOGO_D = lambda: V.logo_dung()
LOGO_DK = lambda: V.logo_dung(KEM, KEM)


def banh(x, y, w, h):
    return B.img("banh-tortillas", x, y, w, h)


def img(n, x, y, w, h):
    return B.img(n, x, y, w, h)


# ======================= MẠNG XÃ HỘI =======================
def avatar():
    s = f'<rect width="400" height="400" fill="{GIAY}"/><circle cx="200" cy="200" r="190" fill="{DO}"/>' + vt(200, 200, 118, KEM, seed=7)
    s += f'<circle cx="200" cy="200" r="190" fill="none" stroke="{DO2}" stroke-width="2" stroke-dasharray="4 6"/>'
    return S(400, 400, s, "Ảnh đại diện")


def bia_facebook():
    s = place(B.nen_van(1640, 624), 0, 0, 1640, 624)
    s += f'<rect x="0" y="0" width="900" height="624" fill="{KEM}"/>'
    s += place(LOGO_N(), 120, 120, 640, 230)
    s += W("Mỗi mẻ bánh, một lời cam kết", 46, 126, 440, MUC, "xb")
    s += W("Tortilla · Taco · Doner kebab giao tận bếp tại TP.HCM · 0348.635.222", 24, 126, 490, MUC, "md")
    s += vt(1260, 312, 210, KEM, seed=9)
    s += f'<rect x="0" y="0" width="1640" height="624" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="14 10" opacity=".0"/>'
    return S(1640, 624, s, "Ảnh bìa Facebook 1640×624")


def post_san_pham():
    s = f'<rect width="540" height="675" fill="{KEM}"/><rect width="540" height="150" fill="{DO}"/>'
    s += W("BÁNH TORTILLA", 18, 40, 58, NGO, "xb", track=.24) + W("Mềm dẻo, cuộn gì cũng vừa", 34, 40, 108, KEM, "xb")
    s += f'<circle cx="270" cy="350" r="150" fill="#fff"/>' + banh(140, 250, 260, 200)
    s += W("Gói [số] chiếc · cỡ [inch]", 22, 270, 560, MUC, "xb", "middle") + W("Làm mới mỗi ngày tại xưởng TP.HCM", 16, 270, 590, MUC, "md", "middle")
    s += f'<rect x="0" y="625" width="540" height="50" fill="{DO}"/>' + W("0348.635.222 · antamfoods.com", 17, 270, 657, KEM, "xb", "middle", .04)
    s += place(V.bieu_tuong(DO, "#fff"), 452, 172, 64, 64)
    return S(540, 675, s, "Bài đăng giới thiệu sản phẩm")


def post_uu_dai():
    s = place(B.nen_van(540, 675), 0, 0, 540, 675)
    s += f'<rect x="40" y="40" width="460" height="595" fill="{KEM}"/>'
    s += W("ƯU ĐÃI ĐẠI LÝ", 18, 270, 100, DO, "xb", "middle", .24) + W("Đặt từ [số lượng]", 44, 270, 160, MUC, "xb", "middle") + W("giảm [số]%", 72, 270, 240, DO, "xb", "middle")
    s += img("taco", 150, 270, 240, 180)
    s += f'<circle cx="408" cy="300" r="62" fill="{NGO}"/>' + W("[giá]", 30, 408, 300, DO2, "xb", "middle") + W("/gói", 14, 408, 322, DO2, "md", "middle")
    s += W("Áp dụng [ngày] – [ngày]. Chưa gồm VAT.", 15, 270, 500, MUC, "md", "middle")
    s += f'<rect x="150" y="530" width="240" height="56" rx="28" fill="{DO}"/>' + W("Gọi 0348.635.222", 22, 270, 566, KEM, "xb", "middle")
    return S(540, 675, s, "Bài đăng ưu đãi")


def post_nguoi_lam_banh():
    s = f'<rect width="540" height="675" fill="{DO}"/>'
    s += vt(270, 230, 130, "#E84A42", seed=13)
    s += f'<circle cx="270" cy="230" r="86" fill="{KEM}"/>' + W("[Ảnh người", 18, 270, 226, MUC, "md", "middle") + W("làm bánh]", 18, 270, 250, MUC, "md", "middle")
    s += W("“Mẻ nào ra lò cũng", 36, 270, 440, KEM, "xb", "middle") + W("phải ngon như mẻ đầu.”", 36, 270, 486, KEM, "xb", "middle")
    s += W("— [Tên], người làm bánh tại xưởng An Tâm", 17, 270, 540, "#FFD6D3", "md", "middle")
    s += place(LOGO_NK(), 150, 584, 240, 70)
    return S(540, 675, s, "Bài đăng câu chuyện người làm bánh")


def post_dai_ly():
    s = f'<rect width="540" height="675" fill="{KEM}"/>' + f'<rect x="0" y="0" width="540" height="270" fill="{DO}"/>'
    s += W("TÌM ĐỐI TÁC", 20, 40, 70, NGO, "xb", track=.24) + W("Mở điểm bán", 52, 40, 140, KEM, "xb") + W("tortilla – kebab", 52, 40, 204, KEM, "xb")
    items = ["Bảng giá đại lý rõ ràng", "Giao bánh tận nơi tại TP.HCM", "Hỗ trợ: [Cần điền]", "Chính sách: [Cần điền]"]
    for i, t in enumerate(items):
        y = 330 + i * 62
        s += vt(66, y - 8, 16, DO, seed=20 + i, rings=6) + W(t, 22, 100, y, MUC, "xb")
    s += f'<rect x="40" y="590" width="460" height="56" rx="28" fill="{DO}"/>' + W("Nhắn Zalo: 0348.635.222", 22, 270, 626, KEM, "xb", "middle")
    return S(540, 675, s, "Bài đăng tìm đối tác")


def post_thong_bao():
    s = f'<rect width="540" height="675" fill="{KEM}"/><rect x="24" y="24" width="492" height="627" fill="none" stroke="{DO}" stroke-width="4"/>'
    s += place(V.con_dau(), 210, 60, 120, 120)
    s += W("THÔNG BÁO", 22, 270, 236, DO, "xb", "middle", .3) + W("Lịch giao hàng", 46, 270, 300, MUC, "xb", "middle") + W("dịp [Lễ / Tết]", 46, 270, 356, MUC, "xb", "middle")
    for i, (a, b) in enumerate([("Nhận đơn cuối", "[ngày]"), ("Nghỉ giao", "[ngày] – [ngày]"), ("Giao lại", "[ngày]")]):
        y = 430 + i * 52
        s += f'<path d="M80,{y + 14} H460" stroke="#EADFCD"/>' + W(a, 20, 80, y, MUC, "md") + W(b, 20, 460, y, DO, "xb", "end")
    s += W("Cảm ơn anh chị đã đồng hành cùng An Tâm!", 17, 270, 610, MUC, "md", "middle")
    return S(540, 675, s, "Bài đăng thông báo")


def story():
    s = place(B.nen_van(360, 640), 0, 0, 360, 640)
    s += f'<rect x="24" y="110" width="312" height="420" rx="18" fill="{KEM}"/>'
    s += place(LOGO_NK(), 60, 30, 240, 70)
    s += img("doner-cuon", 90, 130, 180, 170) + W("Doner cuộn", 36, 180, 340, DO, "xb", "middle") + W("nóng hổi giao tận bếp", 20, 180, 372, MUC, "md", "middle")
    s += W("[giá] / phần", 30, 180, 426, DO2, "xb", "middle")
    s += f'<rect x="80" y="456" width="200" height="46" rx="23" fill="{DO}"/>' + W("Đặt ngay", 20, 180, 486, KEM, "xb", "middle")
    s += W("Vuốt lên để xem bảng giá", 14, 180, 600, KEM, "md", "middle")
    return S(360, 640, s, "Story 1080×1920")


def _icon(kind, cx, cy, r):
    k = KEM
    if kind == "banh":
        return f'<circle cx="{cx}" cy="{cy}" r="{r * .55}" fill="{k}"/>' + "".join(f'<circle cx="{cx + dx * r}" cy="{cy + dy * r}" r="{r * .06}" fill="{DO}"/>' for dx, dy in ((-.2, -.15), (.18, -.05), (-.05, .22), (.25, .25)))
    if kind == "gia":
        return f'<path d="M{cx - r * .5},{cy - r * .2} L{cx - r * .1},{cy - r * .55} H{cx + r * .5} V{cy + r * .05} L{cx + r * .1},{cy + r * .45} Z" fill="{k}"/><circle cx="{cx + r * .28}" cy="{cy - r * .32}" r="{r * .08}" fill="{DO}"/>'
    if kind == "cuahang":
        return f'<path d="M{cx - r * .55},{cy - r * .1} L{cx - r * .45},{cy - r * .45} H{cx + r * .45} L{cx + r * .55},{cy - r * .1} Z" fill="{k}"/><rect x="{cx - r * .45}" y="{cy - r * .05}" width="{r * .9}" height="{r * .55}" fill="{k}"/><rect x="{cx - r * .12}" y="{cy + r * .15}" width="{r * .24}" height="{r * .35}" fill="{DO}"/>'
    if kind == "chat":
        return f'<path d="M{cx - r * .5},{cy - r * .4} H{cx + r * .5} V{cy + r * .25} H{cx - r * .1} L{cx - r * .35},{cy + r * .5} V{cy + r * .25} H{cx - r * .5} Z" fill="{k}"/>' + "".join(f'<circle cx="{cx + d * r * .25}" cy="{cy - r * .08}" r="{r * .06}" fill="{DO}"/>' for d in (-1, 0, 1))
    if kind == "phone":
        return f'<rect x="{cx - r * .28}" y="{cy - r * .5}" width="{r * .56}" height="{r}" rx="{r * .1}" fill="{k}"/><rect x="{cx - r * .2}" y="{cy - r * .38}" width="{r * .4}" height="{r * .66}" fill="{DO}"/>'
    return ""


def highlight():
    items = [("banh", "Sản phẩm"), ("gia", "Bảng giá"), ("cuahang", "Đại lý"), ("chat", "Phản hồi"), ("phone", "Liên hệ")]
    s = f'<rect width="700" height="190" fill="#fff"/>'
    for i, (k, t) in enumerate(items):
        cx = 70 + i * 140
        s += f'<circle cx="{cx}" cy="80" r="58" fill="none" stroke="{SON}" stroke-width="3"/><circle cx="{cx}" cy="80" r="50" fill="{DO}"/>' + _icon(k, cx, 80, 50)
        s += W(t, 16, cx, 168, MUC, "md", "middle")
    return S(700, 190, s, "Ảnh tin nổi bật")


def dien_thoai():
    """Trang Facebook trên điện thoại."""
    s = f'<rect width="380" height="700" rx="46" fill="{MUC}"/><rect x="14" y="14" width="352" height="672" rx="34" fill="#fff"/>'
    s += f'<clipPath id="ph"><rect x="14" y="14" width="352" height="672" rx="34"/></clipPath><g clip-path="url(#ph)">'
    s += place(bia_facebook(), 14, 40, 352, 134)
    s += f'<circle cx="80" cy="190" r="48" fill="#fff"/>' + place(avatar(), 36, 146, 88, 88)
    s += W("Ẩm Thực An Tâm", 22, 30, 268, MUC, "xb") + W("Bánh tortilla · Taco · Doner kebab – TP.HCM", 13, 30, 290, "#6b5a55", "md")
    s += f'<rect x="30" y="306" width="150" height="36" rx="8" fill="{DO}"/>' + W("Nhắn tin", 15, 105, 330, "#fff", "xb", "middle")
    s += f'<rect x="190" y="306" width="150" height="36" rx="8" fill="#EEE"/>' + W("Gọi điện", 15, 265, 330, MUC, "xb", "middle")
    s += place(highlight(), 14, 356, 352, 96)
    s += place(post_san_pham(), 40, 462, 300, 375)
    s += "</g>"
    return S(380, 700, s, "Trang Facebook trên điện thoại")


# ======================= ẤN PHẨM VĂN PHÒNG =======================
def tieu_de_thu():
    s = f'<rect width="595" height="842" fill="#fff"/>' + place(LOGO_N(), 40, 36, 200, 64)
    s += W("Công ty TNHH SX-TM Ẩm Thực An Tâm", 10, 555, 56, MUC, "xb", "end") + W("[Cần điền: địa chỉ]", 9, 555, 72, MUC, "md", "end") + W("0348.635.222 · antamfoods.com", 9, 555, 88, MUC, "md", "end")
    s += f'<rect x="40" y="116" width="515" height="3" fill="{DO}"/>'
    for i in range(14):
        s += f'<rect x="40" y="{170 + i * 26}" width="{515 if i % 4 != 3 else 300}" height="6" rx="3" fill="#EFE7DC"/>'
    s += f'<g opacity=".08">{vt(500, 720, 120, DO, seed=33)}</g>'
    s += f'<rect x="0" y="812" width="595" height="30" fill="{DO}"/>' + W("Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm", 10, 297, 831, KEM, "xb", "middle", .1)
    return S(595, 842, s, "Tiêu đề thư A4")


def phong_bi():
    s = f'<rect width="660" height="330" fill="#fff"/>' + place(LOGO_N(), 30, 26, 220, 70)
    s += W("Kính gửi: [Cần điền]", 18, 330, 190, MUC, "md") + f'<path d="M330,210 H610 M330,240 H610" stroke="#E5DBCB"/>'
    s += f'<rect x="0" y="300" width="660" height="30" fill="{DO}"/>' + W("[địa chỉ] · 0348.635.222 · antamfoods.com", 12, 30, 320, KEM, "md")
    s += f'<g opacity=".9">{vt(600, 300, 34, SON, seed=40, rings=8)}</g>'
    return S(660, 330, s, "Phong bì DL")


def bao_gia():
    s = f'<rect width="595" height="842" fill="#fff"/>' + place(LOGO_N(), 40, 36, 200, 64)
    s += W("BÁO GIÁ", 34, 555, 72, DO, "xb", "end", .06) + W("Số [ ] · Ngày [dd/mm/yyyy]", 10, 555, 92, MUC, "md", "end")
    s += f'<rect x="40" y="116" width="515" height="3" fill="{DO}"/>'
    s += W("Kính gửi: [Tên khách hàng]", 12, 40, 150, MUC, "xb") + W("Ẩm Thực An Tâm xin gửi bảng giá sản phẩm như sau:", 11, 40, 172, MUC, "md")
    s += f'<rect x="40" y="190" width="515" height="30" fill="{MUC}"/>'
    for x, t in ((50, "Sản phẩm"), (300, "Quy cách"), (420, "SL tối thiểu"), (545, "Đơn giá")):
        s += W(t, 11, x, 210, KEM, "xb", "end" if x == 545 else "start")
    rows = [("Bánh tortilla 8 inch", "Gói [số] chiếc"), ("Bánh tortilla 10 inch", "Gói [số] chiếc"), ("Vỏ taco", "Gói [số] chiếc"), ("Thịt doner", "Kg"), ("Sốt doner", "Chai [ml]")]
    for i, (a, b) in enumerate(rows):
        y = 246 + i * 32
        s += f'<rect x="40" y="{y - 20}" width="515" height="32" fill="{"#FBF5EC" if i % 2 else "#fff"}"/>' + W(a, 11, 50, y, MUC, "md") + W(b, 11, 300, y, MUC, "md") + W("[ ]", 11, 420, y, MUC, "md") + W("[giá]", 11, 545, y, DO, "xb", "end")
    s += W("Giá chưa gồm VAT. Báo giá có hiệu lực đến [ngày].", 10, 40, 430, MUC, "md")
    s += W("Người lập báo giá", 10, 420, 500, MUC, "md", "middle") + vt(420, 560, 32, SON, seed=41, rings=9) + W("[Tên]", 11, 420, 620, MUC, "xb", "middle")
    s += f'<rect x="0" y="812" width="595" height="30" fill="{DO}"/>' + W("0348.635.222 · antamfoods.com · [địa chỉ]", 10, 297, 831, KEM, "md", "middle")
    return S(595, 842, s, "Báo giá A4")


def the_nhan_vien():
    s = f'<rect width="420" height="560" fill="{GIAY}"/><path d="M210,0 V80" stroke="{DO}" stroke-width="16"/>'
    s += f'<g filter="url(#tn)"><rect x="110" y="70" width="200" height="320" rx="16" fill="#fff"/></g>' + shadow("tn")
    s += f'<path d="M110,86 a16,16 0 0 1 16,-16 h168 a16,16 0 0 1 16,16 V170 H110 Z" fill="{DO}"/><rect x="184" y="80" width="52" height="8" rx="4" fill="{GIAY}"/>'
    s += place(LOGO_NK(), 128, 100, 164, 52)
    s += f'<circle cx="210" cy="230" r="46" fill="#EFE7DC"/>' + W("[Ảnh]", 14, 210, 235, "#8a7a72", "md", "middle")
    s += W("[Họ tên]", 20, 210, 310, MUC, "xb", "middle") + W("[Bộ phận]", 13, 210, 332, DO, "md", "middle") + W("Mã NV: [ ]", 11, 210, 360, MUC, "md", "middle")
    s += f'<g opacity=".9">{vt(282, 366, 16, SON, seed=44, rings=6)}</g>'
    return S(420, 560, s, "Thẻ nhân viên")


def ho_so_nang_luc():
    s = place(B.nen_van(420, 594), 0, 0, 420, 594)
    s += f'<rect x="36" y="300" width="348" height="250" fill="{KEM}"/>'
    s += W("HỒ SƠ", 18, 60, 350, DO, "xb", track=.3) + W("Năng lực", 50, 60, 410, MUC, "xb") + W("doanh nghiệp", 34, 60, 452, MUC, "xb") + W("[Năm]", 16, 60, 520, DO, "md")
    s += place(LOGO_NK(), 40, 40, 230, 72)
    return S(420, 594, s, "Bìa hồ sơ năng lực")


def to_roi():
    s = f'<rect width="420" height="594" fill="{KEM}"/><rect width="420" height="230" fill="{DO}"/>'
    s += place(LOGO_NK(), 28, 22, 200, 60) + W("Bánh tươi cho", 40, 28, 140, KEM, "xb") + W("quán của bạn", 40, 28, 190, NGO, "xb")
    for i, (n, t) in enumerate([("banh-tortillas", "Tortilla"), ("taco", "Vỏ taco"), ("doner-cuon", "Doner")]):
        x = 20 + i * 132
        s += f'<rect x="{x}" y="250" width="120" height="150" rx="12" fill="#fff"/>' + img(n, x + 10, 258, 100, 92) + W(t, 16, x + 60, 376, MUC, "xb", "middle")
    s += W("Vì sao chọn An Tâm?", 22, 28, 450, DO, "xb")
    for i, t in enumerate(["Bánh làm mới mỗi ngày", "Giao tận nơi tại TP.HCM", "Báo giá đại lý rõ ràng"]):
        s += vt(40, 478 + i * 30, 9, DO, seed=50 + i, rings=5) + W(t, 15, 58, 484 + i * 30, MUC, "md")
    s += f'<rect x="0" y="564" width="420" height="30" fill="{DO}"/>' + W("0348.635.222 · antamfoods.com", 13, 210, 584, KEM, "xb", "middle")
    return S(420, 594, s, "Tờ rơi A5")


def standee():
    s = f'<rect width="300" height="760" fill="{GIAY}"/><rect x="40" y="20" width="220" height="690" fill="{DO}"/>'
    s += place(B.nen_van(220, 300), 40, 20, 220, 300)
    s += place(LOGO_NK(), 56, 40, 188, 60)
    s += f'<rect x="58" y="320" width="184" height="360" fill="{KEM}"/>' + img("doner-cuon", 85, 330, 130, 120)
    s += W("Doner kebab", 24, 150, 488, DO, "xb", "middle") + W("& Taco", 24, 150, 518, DO, "xb", "middle") + W("[giá] / phần", 20, 150, 560, MUC, "xb", "middle")
    s += W("Gọi món tại quầy", 13, 150, 600, MUC, "md", "middle") + vt(150, 640, 22, SON, seed=55, rings=7)
    s += f'<path d="M80,710 L60,750 M220,710 L240,750" stroke="#777" stroke-width="6"/>'
    return S(300, 760, s, "Standee 60×160 cm")


def menu_treo():
    s = f'<rect width="720" height="420" fill="{MUC}"/><rect x="20" y="20" width="680" height="380" fill="{KEM}"/>'
    s += f'<rect x="20" y="20" width="680" height="80" fill="{DO}"/>' + place(LOGO_NK(), 40, 30, 200, 60) + W("THỰC ĐƠN", 30, 680, 72, NGO, "xb", "end", .2)
    items = [("Doner cuộn", "doner-cuon"), ("Taco", "taco"), ("Bánh tortilla gói", "banh-tortillas")]
    for i, (t, n) in enumerate(items):
        x = 50 + i * 215
        s += f'<rect x="{x}" y="120" width="190" height="250" rx="14" fill="#fff"/>' + img(n, x + 30, 130, 130, 120) + W(t, 22, x + 95, 290, MUC, "xb", "middle") + W("[giá]", 30, x + 95, 340, DO, "xb", "middle")
    return S(720, 420, s, "Bảng thực đơn treo")


# ======================= BAO BÌ =======================
def nhan_san_pham():
    s = f'<rect width="520" height="320" fill="#fff" stroke="#E5DBCB"/>' + f'<rect width="180" height="320" fill="{DO}"/>'
    s += place(LOGO_DK(), 14, 40, 152, 170) + W("BÁNH TORTILLA", 16, 90, 260, NGO, "xb", "middle", .1) + W("[inch] · [số] chiếc", 13, 90, 284, KEM, "md", "middle")
    rows = ["Thành phần: [Cần điền]", "Khối lượng tịnh: [ ] g", "NSX: [dd/mm/yyyy]   HSD: [dd/mm/yyyy]", "Bảo quản: [Cần điền]", "Hướng dẫn dùng: [Cần điền]", "Sản xuất bởi: Công ty TNHH SX-TM Ẩm Thực An Tâm", "Địa chỉ: [Cần điền]", "Hotline: 0348.635.222"]
    for i, t in enumerate(rows):
        s += W(t, 12, 200, 40 + i * 30, MUC, "xb" if i in (0, 2) else "md")
    s += vt(470, 270, 26, SON, seed=60, rings=8)
    return S(520, 320, s, "Nhãn sản phẩm (nội dung bắt buộc)")


def hop_taco():
    s = shadow("ht") + f'<rect width="560" height="420" fill="{GIAY}"/>'
    s += f'<g filter="url(#ht)"><path d="M100,170 L280,90 L460,170 L280,250 Z" fill="{DO}"/><path d="M100,170 L280,250 L280,370 L100,290 Z" fill="{KEM}"/><path d="M280,250 L460,170 L460,290 L280,370 Z" fill="#EADFCD"/></g>'
    s += f'<path d="M190,150 L280,110 L370,150 L280,190 Z" fill="#FDE9D0" opacity=".9"/>'
    s += f'<g transform="matrix(1 .44 0 1 100 170)">{W("Taco", 40, 30, 70, DO, "xb")}{W("ẨM THỰC AN TÂM", 11, 32, 92, MUC, "xb", track=.2)}</g>'
    s += f'<g transform="matrix(1 -.44 0 1 280 250)"><g transform="translate(110 60)">{vt(0, 0, 34, SON, seed=61, rings=9)}</g></g>'
    s += f'<g transform="matrix(.9 .4 -.9 .4 280 95)">{W("an tâm", 1, 0, 0, KEM)}</g>'
    return S(560, 420, s, "Hộp taco")


def giay_goi():
    pat = "".join(vt(40 + (i % 6) * 90 + (45 if (i // 6) % 2 else 0), 40 + (i // 6) * 90, 26, SON, seed=70 + i, rings=7) for i in range(30))
    s = f'<rect width="560" height="420" fill="{GIAY}"/><g transform="rotate(-6 220 220)"><rect x="40" y="40" width="360" height="330" fill="{KEM}"/><clipPath id="gg"><rect x="40" y="40" width="360" height="330"/></clipPath><g clip-path="url(#gg)" opacity=".85">{pat}</g></g>'
    s += f'<path d="M400,130 L520,150 L470,390 L380,380 Z" fill="{KEM}"/><clipPath id="gc"><path d="M400,130 L520,150 L470,390 L380,380 Z"/></clipPath><g clip-path="url(#gc)" opacity=".85">{pat}</g>'
    s += f'<ellipse cx="460" cy="140" rx="62" ry="22" fill="#E7C08A"/>' + f'<circle cx="440" cy="132" r="9" fill="{LA if False else "#4E8A3A"}"/><circle cx="470" cy="128" r="9" fill="{DO}"/>'
    s += f'<rect x="398" y="250" width="100" height="40" fill="{DO}" transform="rotate(8 448 270)"/>' + f'<g transform="rotate(8 448 270)">{W("AN TÂM", 18, 448, 277, KEM, "xb", "middle", .1)}</g>'
    return S(560, 420, s, "Giấy gói doner")


LA = "#4E8A3A"


def thung_carton():
    s = shadow("tc") + f'<rect width="560" height="440" fill="{GIAY}"/>'
    s += f'<g filter="url(#tc)"><path d="M70,160 L280,70 L490,160 L280,250 Z" fill="#D6B38A"/><path d="M70,160 L280,250 L280,400 L70,310 Z" fill="{KRAFT}"/><path d="M280,250 L490,160 L490,310 L280,400 Z" fill="{KRAFT2}"/></g>'
    tape = "".join(f'<g transform="translate({20 + i * 56} 22)">{vt(0, 0, 14, KEM, seed=80 + i, rings=6)}</g>' for i in range(5))
    s += f'<g transform="matrix(.913 .43 -.913 .43 175 115) translate(0 -22)"><rect width="230" height="44" fill="{DO}"/>{tape}</g>'
    s += f'<g transform="matrix(1 .43 0 1 70 160) translate(83 0)"><rect width="44" height="74" fill="{DO}"/></g>'
    s += f'<g transform="matrix(1 -.43 0 1 280 250)"><g transform="translate(18 18)">{place(LOGO_N(), 0, 0, 170, 54)}</g>{W("BÁNH TORTILLA · [số] gói", 12, 22, 104, MUC, "xb")}{W("NSX: [ ] · HSD: [ ]", 10, 22, 122, MUC, "md")}</g>'
    return S(560, 440, s, "Thùng carton dán băng keo vân tay")


def tui_quai():
    s = shadow("tq") + f'<rect width="420" height="520" fill="{GIAY}"/><path d="M150,140 C150,60 270,60 270,140" fill="none" stroke="{DO2}" stroke-width="10"/>'
    s += f'<g filter="url(#tq)"><path d="M80,130 H340 L356,490 H64 Z" fill="{KRAFT}"/></g><path d="M80,130 H340 L338,160 H82 Z" fill="{KRAFT2}"/>'
    s += vt(210, 300, 92, DO, seed=90) + place(LOGO_N(), 110, 410, 200, 64)
    return S(420, 520, s, "Túi giấy kraft có quai")


def ly_giay():
    s = shadow("lg") + f'<rect width="420" height="520" fill="{GIAY}"/>'
    s += f'<g filter="url(#lg)"><path d="M110,110 H310 L290,470 H130 Z" fill="#fff"/></g><rect x="100" y="94" width="220" height="22" rx="8" fill="{DO2}"/>'
    s += f'<clipPath id="lc"><path d="M110,116 H310 L290,470 H130 Z"/></clipPath><g clip-path="url(#lc)"><rect x="100" y="300" width="220" height="180" fill="{DO}"/>{vt(210, 230, 70, SON, seed=91)}</g>'
    s += W("an tâm", 34, 210, 380, KEM, "xb", "middle")
    return S(420, 520, s, "Ly giấy")


def tem_niem_phong():
    s = f'<rect width="420" height="260" fill="{GIAY}"/>' + place(V.con_dau(), 20, 20, 220, 220)
    s += f'<rect x="260" y="40" width="140" height="180" rx="12" fill="{DO}"/>' + vt(330, 110, 40, KEM, seed=92, rings=9) + W("ĐÃ NIÊM PHONG", 12, 330, 186, KEM, "xb", "middle", .1) + W("Mẻ [ ]", 12, 330, 204, "#FFD6D3", "md", "middle")
    return S(420, 260, s, "Tem niêm phong")


# ======================= ĐỒNG PHỤC =======================
def _ao(fill, s_extra):
    return (f'<path d="M150,60 L200,40 Q240,70 280,40 L330,60 L420,120 L380,190 L340,170 L340,410 L140,410 L140,170 L100,190 L60,120 Z" fill="{fill}"/>'
            f'<path d="M200,40 Q240,70 280,40" fill="none" stroke="{DO2 if fill != DO2 else MUC}" stroke-width="10"/>{s_extra}')


def ao_thun():
    t = _ao(DO, place(V.bieu_tuong(KEM, DO), 278, 104, 54, 54))
    b = _ao(DO, vt(240, 210, 64, KEM, seed=93) + W("ẨM THỰC", 14, 240, 316, KEM, "xb", "middle", .3) + W("AN TÂM", 34, 240, 352, KEM, "xb", "middle"))
    return S(960, 440, f'<rect width="960" height="440" fill="{GIAY}"/>' + t + f'<g transform="translate(480 0)">{b}</g>', "Áo thun nhân viên trước và sau")


def ao_polo():
    s = (f'<path d="M150,60 L205,40 L240,90 L275,40 L330,60 L420,120 L380,190 L340,170 L340,410 L140,410 L140,170 L100,190 L60,120 Z" fill="{KEM}"/>'
         f'<path d="M205,40 L240,90 L275,40" fill="none" stroke="{DO}" stroke-width="8"/><path d="M240,90 V150" stroke="{DO}" stroke-width="4"/>'
         f'<circle cx="240" cy="110" r="4" fill="{DO}"/><circle cx="240" cy="132" r="4" fill="{DO}"/>{place(LOGO_N(), 270, 112, 70, 24)}'
         f'<path d="M100,190 L60,120" stroke="{DO}" stroke-width="10"/><path d="M380,190 L420,120" stroke="{DO}" stroke-width="10"/>')
    return S(480, 440, f'<rect width="480" height="440" fill="{GIAY}"/>' + s, "Áo polo văn phòng")


def tap_de():
    s = f'<rect width="420" height="520" fill="{GIAY}"/><path d="M150,40 C150,0 270,0 270,40" fill="none" stroke="{MUC}" stroke-width="10"/>'
    s += f'<path d="M140,40 H280 L290,150 L360,170 L350,480 H70 L60,170 L130,150 Z" fill="{DO}"/><path d="M60,170 L20,200 M360,170 L400,200" stroke="{MUC}" stroke-width="8"/>'
    s += vt(210, 250, 60, KEM, seed=94) + W("AN TÂM", 30, 210, 360, KEM, "xb", "middle") + W("Mỗi mẻ bánh, một lời cam kết", 12, 210, 384, "#FFD6D3", "md", "middle")
    s += f'<rect x="120" y="410" width="180" height="60" rx="6" fill="{DO2}"/>'
    return S(420, 520, s, "Tạp dề")


def mu_luoi_trai():
    s = f'<rect width="420" height="300" fill="{GIAY}"/><path d="M90,200 C90,80 330,80 330,200 Z" fill="{DO}"/><path d="M90,200 C150,230 300,250 400,210 C380,250 200,260 90,200 Z" fill="{DO2}"/>'
    s += f'<circle cx="210" cy="96" r="8" fill="{DO2}"/>' + vt(210, 160, 30, KEM, seed=95, rings=8)
    return S(420, 300, s, "Mũ lưỡi trai")


def mu_bep():
    s = f'<rect width="420" height="300" fill="{GIAY}"/><path d="M100,220 C70,140 120,80 170,100 C190,50 240,50 260,100 C310,80 350,140 320,220 Z" fill="#fff" stroke="#E5DBCB" stroke-width="3"/>'
    s += f'<rect x="110" y="200" width="200" height="60" rx="6" fill="#fff" stroke="#E5DBCB" stroke-width="3"/><rect x="110" y="222" width="200" height="16" fill="{DO}"/>' + W("AN TÂM", 12, 210, 234, KEM, "xb", "middle", .3)
    return S(420, 300, s, "Mũ bếp")


# ======================= ĐIỂM BÁN, PHƯƠNG TIỆN =======================
def bien_hieu():
    s = f'<rect width="760" height="440" fill="#E8DFD2"/><rect y="390" width="760" height="50" fill="#CFC3B1"/>'
    s += f'<rect x="60" y="40" width="640" height="120" fill="{DO}"/>' + place(LOGO_NK(), 215, 52, 330, 100)
    s += f'<rect x="60" y="160" width="640" height="230" fill="#F7EEE2"/><rect x="60" y="160" width="640" height="30" fill="{MUC}"/>' + W("TORTILLA · TACO · DONER · 0348.635.222", 15, 380, 181, NGO, "xb", "middle", .14)
    s += f'<rect x="100" y="200" width="250" height="190" fill="#BFD8E4"/><rect x="390" y="200" width="270" height="190" fill="#5A3B2A"/>'
    s += img("doner-tru-quay", 160, 210, 140, 170) + vt(525, 280, 50, KEM, seed=96)
    return S(760, 440, s, "Biển hiệu cửa hàng")


def xe_tai():
    return B.xe().replace(f'<g opacity=".35">{V.van_tay(420, 150, 90, KEM, seed=61)}</g>', "")


def kiosk():
    s = f'<rect width="560" height="440" fill="#EFE7DC"/><rect y="390" width="560" height="50" fill="#D6CAB8"/>'
    s += f'<rect x="80" y="40" width="400" height="70" fill="{DO}"/>' + place(LOGO_NK(), 100, 46, 200, 60)
    s += f'<rect x="96" y="110" width="8" height="140" fill="{MUC}"/><rect x="456" y="110" width="8" height="140" fill="{MUC}"/>'
    s += f'<rect x="80" y="250" width="400" height="140" fill="{DO}"/>' + place(B.nen_van(400, 140), 80, 250, 400, 140) + f'<rect x="150" y="280" width="260" height="80" fill="{KEM}"/>' + W("Doner · Taco", 30, 280, 330, DO, "xb", "middle")
    return S(560, 440, s, "Quầy kiosk")


def xe_may():
    s = f'<rect width="560" height="420" fill="#ECE5DA"/><rect y="360" width="560" height="60" fill="#D5CAB8"/>'
    s += f'<rect x="230" y="70" width="220" height="190" rx="16" fill="{DO}"/>' + vt(340, 150, 54, KEM, seed=97) + W("AN TÂM", 28, 340, 238, KEM, "xb", "middle", .06)
    s += f'<path d="M120,290 Q160,240 240,262 L460,262 Q500,264 510,300 L516,320 L130,320 Z" fill="{MUC}"/><circle cx="160" cy="330" r="38" fill="{MUC}"/><circle cx="160" cy="330" r="14" fill="#888"/><circle cx="470" cy="330" r="38" fill="{MUC}"/><circle cx="470" cy="330" r="14" fill="#888"/>'
    s += f'<path d="M110,240 L150,230 L170,290" stroke="{MUC}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    return S(560, 420, s, "Thùng giao hàng xe máy")


def sticker():
    s = f'<rect width="560" height="300" fill="#fff"/>'
    s += f'<circle cx="90" cy="100" r="64" fill="{DO}"/>' + vt(90, 100, 40, KEM, seed=98, rings=9)
    s += f'<rect x="180" y="40" width="170" height="120" rx="60" fill="{KEM}" stroke="{DO}" stroke-width="5"/>' + W("Ngon", 30, 265, 96, DO, "xb", "middle") + W("an tâm!", 30, 265, 132, DO, "xb", "middle")
    s += f'<rect x="380" y="40" width="150" height="120" rx="14" fill="{NGO}"/>' + W("Bánh", 26, 455, 92, DO2, "xb", "middle") + W("mới ra lò", 22, 455, 124, DO2, "xb", "middle")
    s += place(V.con_dau(), 40, 180, 110, 110) + f'<rect x="180" y="200" width="350" height="70" rx="35" fill="{DO}"/>' + W("Mỗi mẻ bánh, một lời cam kết", 18, 355, 242, KEM, "xb", "middle")
    return S(560, 300, s, "Bộ sticker")


def chu_ky_email():
    s = f'<rect width="640" height="180" fill="#fff"/><rect x="20" y="20" width="4" height="140" fill="{DO}"/>'
    s += W("[Họ tên]", 22, 44, 52, MUC, "xb") + W("[Chức danh] · Ẩm Thực An Tâm", 14, 44, 76, DO, "md")
    s += W("0348.635.222 · antamfoods.com", 13, 44, 110, MUC, "md") + W("[địa chỉ], TP.HCM", 13, 44, 132, MUC, "md")
    s += place(LOGO_N(), 420, 50, 200, 64)
    return S(640, 180, s, "Chữ ký email")


GROUPS = [
    ("mxh", "Mạng xã hội", [
        ("anh-dai-dien", "Ảnh đại diện (1080×1080, cắt tròn)", avatar), ("bia-facebook", "Ảnh bìa Facebook 1640×624 – chữ nằm trong nửa trái để không bị che trên điện thoại", bia_facebook),
        ("trang-dien-thoai", "Trang Facebook trên điện thoại", dien_thoai), ("tin-noi-bat", "Ảnh tin nổi bật (highlight)", highlight),
        ("bai-san-pham", "Mẫu bài: giới thiệu sản phẩm", post_san_pham), ("bai-uu-dai", "Mẫu bài: ưu đãi đại lý", post_uu_dai),
        ("bai-nguoi-lam-banh", "Mẫu bài: câu chuyện người làm bánh", post_nguoi_lam_banh), ("bai-doi-tac", "Mẫu bài: tìm đối tác", post_dai_ly),
        ("bai-thong-bao", "Mẫu bài: thông báo lịch giao hàng", post_thong_bao), ("story", "Story / Reels 1080×1920", story)]),
    ("an-pham", "Ấn phẩm văn phòng & bán hàng", [
        ("tieu-de-thu", "Tiêu đề thư A4", tieu_de_thu), ("bao-gia", "Báo giá A4", bao_gia), ("phong-bi", "Phong bì DL 220×110 mm", phong_bi),
        ("the-nhan-vien", "Thẻ nhân viên 54×86 mm", the_nhan_vien), ("ho-so-nang-luc", "Bìa hồ sơ năng lực A4", ho_so_nang_luc), ("to-roi", "Tờ rơi A5", to_roi),
        ("standee", "Standee 60×160 cm", standee), ("thuc-don", "Bảng thực đơn treo", menu_treo), ("phieu-giao-hang", "Phiếu giao hàng A5", B.phieu), ("chu-ky-email", "Chữ ký email", chu_ky_email)]),
    ("bao-bi", "Bao bì", [
        ("tui-tortilla", "Túi bánh tortilla", B.tui), ("nhan-san-pham", "Nhãn sản phẩm – đủ mục bắt buộc", nhan_san_pham), ("hop-taco", "Hộp taco", hop_taco),
        ("giay-goi-doner", "Giấy gói doner", giay_goi), ("thung-carton", "Thùng carton + băng keo vân tay", thung_carton), ("tui-quai", "Túi giấy kraft có quai", tui_quai),
        ("ly-giay", "Ly giấy", ly_giay), ("tem-niem-phong", "Tem niêm phong", tem_niem_phong), ("the-me-banh", "Thẻ treo \"Mẻ bánh hôm nay\"", B.the_tho)]),
    ("dong-phuc", "Đồng phục", [
        ("ao-thun", "Áo thun nhân viên – trước & sau", ao_thun), ("ao-polo", "Áo polo văn phòng", ao_polo), ("tap-de", "Tạp dề", tap_de),
        ("mu-luoi-trai", "Mũ lưỡi trai", mu_luoi_trai), ("mu-bep", "Mũ bếp", mu_bep)]),
    ("diem-ban", "Điểm bán & phương tiện", [
        ("bien-hieu", "Biển hiệu cửa hàng", bien_hieu), ("quay-kiosk", "Quầy kiosk", kiosk), ("xe-may", "Thùng giao hàng xe máy", xe_may),
        ("xe-tai", "Xe giao hàng", xe_tai), ("sticker", "Bộ sticker", sticker)]),
]

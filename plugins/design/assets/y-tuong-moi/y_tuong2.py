"""Đợt 2: 5 ý tưởng mới khác cho Ẩm Thực An Tâm (đỏ làm nền tảng). Chạy: python3 y_tuong2.py OUT.html"""
import math
import random
import sys

import y_tuong as Y
from y_tuong import T, Tw, svg, img, DO, DO2, KEM, NGO, DEN, LA

XANH_GACH = "#2F6F73"


# ===== 06. Taco Cười =====
def taco_cuoi(cx, cy, w, fill=NGO, ink=DO, nhan=True):
    """Vỏ taco gập nhìn nghiêng = một nụ cười; nhân đỏ – xanh lấp ló ở miệng."""
    h = w * .42; o = ""
    if nhan:
        rr = random.Random(3)
        for i in range(9):
            x = cx - w * .38 + i * w * .095
            o += f'<circle cx="{x:.1f}" cy="{cy - h * .02 + rr.uniform(-4, 4):.1f}" r="{w * rr.uniform(.045, .06):.1f}" fill="{[LA, ink, LA, "#F06A3A"][i % 4]}"/>'
    o += (f'<path fill="{fill}" d="M{cx - w / 2:.1f},{cy:.1f} C{cx - w / 2:.1f},{cy + h * 1.25:.1f} {cx + w / 2:.1f},{cy + h * 1.25:.1f} {cx + w / 2:.1f},{cy:.1f} '
          f'C{cx + w * .32:.1f},{cy + h * .6:.1f} {cx - w * .32:.1f},{cy + h * .6:.1f} {cx - w / 2:.1f},{cy:.1f} Z"/>')
    for k in range(6):
        x = cx - w * .3 + k * w * .12
        o += f'<ellipse cx="{x:.1f}" cy="{cy + h * .66 + abs(k - 2.5) * -h * .06:.1f}" rx="{w * .016:.1f}" ry="{w * .01:.1f}" fill="#B9772F"/>'
    return o


def y6_logo():
    s = T("an tâm", 112, 40, 150, DO, "b9", track=-.03)
    w = Tw("an tâm", 112, "b9", -.03)
    s += taco_cuoi(40 + w / 2, 176, w * .84, nhan=False)
    s += T("TACO · TORTILLA · DONER", 15, 40 + w / 2, 312, DEN, "b8", "middle", .26)
    return svg(int(w + 80), 330, s, "Logo Taco Cười")


def y6_ung_dung():
    s = f'<rect width="520" height="360" fill="{DO}"/>' + taco_cuoi(260, 150, 300, NGO, DO2)
    s += T("Chủ quán cười tươi", 30, 260, 300, KEM, "b9", "middle") + T("khi bánh luôn sẵn sàng", 18, 260, 330, "#FFD6D6", "b6", "middle")
    return svg(520, 360, s, "Bài đăng Taco Cười")


# ===== 07. Gạch Bông =====
def gach(x, y, s, a=DO, b=KEM, c=NGO, d=XANH_GACH):
    """Viên gạch bông vuông: bốn góc cung tròn, giữa là chiếc bánh tròn với bốn lá – ghép nhiều viên thành hoa văn."""
    o = f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{b}"/>'
    for (px, py) in ((x, y), (x + s, y), (x, y + s), (x + s, y + s)):
        o += f'<circle cx="{px}" cy="{py}" r="{s * .26:.1f}" fill="{a}"/><circle cx="{px}" cy="{py}" r="{s * .17:.1f}" fill="{b}"/><circle cx="{px}" cy="{py}" r="{s * .1:.1f}" fill="{c}"/>'
    cx, cy = x + s / 2, y + s / 2
    for ang in (0, 90, 180, 270):
        o += f'<path d="M{cx},{cy} q{s * .12:.1f},{-s * .12:.1f} 0,{-s * .34:.1f} q{-s * .12:.1f},{s * .12:.1f} 0,{s * .34:.1f}" fill="{d}" transform="rotate({ang + 45} {cx} {cy})"/>'
    o += f'<circle cx="{cx}" cy="{cy}" r="{s * .16:.1f}" fill="{c}" stroke="{a}" stroke-width="{s * .03:.1f}"/>'
    o += f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="none" stroke="{a}" stroke-width="{s * .02:.1f}"/>'
    return f'<clipPath id="g{int(x)}{int(y)}{int(s)}"><rect x="{x}" y="{y}" width="{s}" height="{s}"/></clipPath><g clip-path="url(#g{int(x)}{int(y)}{int(s)})">{o}</g>'


def y7_logo():
    s = gach(30, 50, 200) + T("ẨM THỰC", 24, 260, 110, DEN, "b8", track=.3) + T("an tâm", 100, 254, 196, DO, "b9", track=-.03) + T("BẾP NHÀ SÀI GÒN", 14, 262, 232, DEN, "b8", track=.3)
    return svg(int(254 + Tw("an tâm", 100, "b9", -.03) + 30), 300, s, "Logo Gạch Bông")


def y7_ung_dung():
    s = "".join(gach(x, y, 90) for x in range(0, 540, 90) for y in range(0, 360, 90))
    s += f'<rect x="110" y="110" width="300" height="140" fill="{KEM}" stroke="{DO}" stroke-width="6"/>' + T("an tâm", 70, 260, 196, DO, "b9", "middle", -.03) + T("GIẤY GÓI BÁNH", 13, 260, 228, DEN, "b8", "middle", .3)
    return svg(520, 360, s, "Giấy gói hoa văn gạch bông")


# ===== 08. Điểm Chỉ =====
def van_tay(cx, cy, r, fill=DO, banh=None, seed=4):
    """Dấu vân tay son đỏ: các đường vân đồng tâm hơi lệch, đứt quãng – như lăn tay cam kết."""
    rr = random.Random(seed); o = ""
    if banh:
        o += f'<ellipse cx="{cx}" cy="{cy}" rx="{r:.1f}" ry="{r * 1.2:.1f}" fill="{banh}"/>'
    for i in range(1, 12):
        rx = r * i / 11; ry = rx * 1.2
        gap0 = rr.uniform(0, 300); glen = rr.uniform(20, 55)
        circ = math.pi * (rx + ry)
        o += (f'<ellipse cx="{cx + rr.uniform(-1.5, 1.5):.1f}" cy="{cy + (11 - i) * r * .012:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="{fill}" '
              f'stroke-width="{r * .045:.1f}" stroke-linecap="round" stroke-dasharray="{circ * (1 - glen / 360):.1f} {circ * glen / 360:.1f}" stroke-dashoffset="{circ * gap0 / 360:.1f}"/>')
    return o


def y8_logo():
    s = van_tay(120, 150, 92) + T("An Tâm", 96, 250, 168, DO, "b9", track=-.02) + T("ĐIỂM CHỈ CHO TỪNG MẺ BÁNH", 14, 254, 204, DEN, "b8", track=.22)
    return svg(int(250 + Tw("An Tâm", 96, "b9", -.02) + 30), 300, s, "Logo Điểm Chỉ")


def y8_ung_dung():
    s = f'<rect width="520" height="360" fill="{KEM}"/><rect x="40" y="30" width="440" height="300" fill="#fff" stroke="#E7D8C2"/>'
    s += T("PHIẾU GIAO HÀNG", 22, 70, 76, DEN, "b9", track=.06) + T("Số: [Cần điền] · Ngày: [Cần điền]", 12, 70, 98, DEN, "b4")
    rows = [("Bánh tortilla 10 inch", "[sl]"), ("Vỏ taco", "[sl]"), ("Thịt doner (kg)", "[sl]")]
    for i, (a, b) in enumerate(rows):
        y = 140 + i * 34
        s += f'<path d="M70,{y + 10} H450" stroke="#EDE2D2"/>' + T(a, 15, 70, y, DEN, "b6") + T(b, 15, 450, y, DO, "b8", "end")
    s += van_tay(380, 250, 30, DO) + T("Người làm bánh xác nhận", 12, 380, 312, DEN, "b6", "middle")
    return svg(520, 360, s, "Phiếu giao hàng có dấu điểm chỉ")


# ===== 09. Xe Bánh =====
def xe_banh(cx, base, w, body=DO, glass=KEM, ink=DO2, banh=NGO):
    """Xe đẩy bánh mì Sài Gòn: tủ kính, mái che, hai bánh xe – xe của chính khách hàng An Tâm."""
    h = w * .62; x0 = cx - w / 2
    o = f'<path d="M{x0 - w * .04:.1f},{base - h:.1f} h{w * 1.08:.1f} l{-w * .06:.1f},{h * .14:.1f} h{-w * .96:.1f} Z" fill="{body}"/>'
    for k in range(6):
        o += f'<path d="M{x0 + k * w / 6:.1f},{base - h * .86:.1f} q{w / 12:.1f},{h * .1:.1f} {w / 6:.1f},0" fill="{body if k % 2 else ink}"/>'
    o += f'<rect x="{x0:.1f}" y="{base - h * .74:.1f}" width="{w:.1f}" height="{h * .36:.1f}" rx="{w * .02:.1f}" fill="{glass}" stroke="{body}" stroke-width="{w * .025:.1f}"/>'
    for i in range(3):
        o += f'<ellipse cx="{x0 + w * (.22 + i * .28):.1f}" cy="{base - h * .46:.1f}" rx="{w * .1:.1f}" ry="{h * .045:.1f}" fill="{banh}" stroke="#E39A1C" stroke-width="2"/>'
    o += f'<rect x="{x0:.1f}" y="{base - h * .36:.1f}" width="{w:.1f}" height="{h * .26:.1f}" fill="{body}"/>'
    o += f'<path d="M{x0 + w:.1f},{base - h * .3:.1f} h{w * .12:.1f}" stroke="{ink}" stroke-width="{w * .025:.1f}" stroke-linecap="round"/>'
    for wx in (x0 + w * .2, x0 + w * .8):
        o += f'<circle cx="{wx:.1f}" cy="{base - h * .06:.1f}" r="{h * .1:.1f}" fill="{DEN}"/><circle cx="{wx:.1f}" cy="{base - h * .06:.1f}" r="{h * .04:.1f}" fill="{glass}"/>'
    return o


def y9_logo():
    s = xe_banh(120, 230, 180) + T("An Tâm", 96, 240, 164, DO, "b9", track=-.02) + T("ĐỒNG HÀNH CÙNG XE BÁNH CỦA BẠN", 13, 244, 198, DEN, "b8", track=.2)
    return svg(int(240 + max(Tw("An Tâm", 96, "b9", -.02), Tw("ĐỒNG HÀNH CÙNG XE BÁNH CỦA BẠN", 13, "b8", .2)) + 30), 300, s, "Logo Xe Bánh")


def y9_ung_dung():
    s = f'<rect width="520" height="360" fill="#F1E6D6"/><rect y="300" width="520" height="60" fill="#D8C8B2"/>' + xe_banh(260, 320, 300)
    s += T("AN TÂM · KEBAB · TACO", 26, 260, 287, KEM, "nen", "middle", .06)
    return svg(520, 360, s, "Xe đẩy đối tác mang thương hiệu An Tâm")


# ===== 10. Bản Đồ Bếp =====
def ban_do(cx, cy, R, fill=DO, dot=NGO, n=10, seed=7, nha=KEM):
    """Xưởng An Tâm ở giữa, các đường giao toả tới những căn bếp đối tác xếp thành vòng tròn chiếc bánh."""
    rr = random.Random(seed); o = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{fill}" stroke-width="{R * .03:.1f}" stroke-dasharray="{R * .05:.1f} {R * .05:.1f}"/>'
    pts = []
    for k in range(n):
        a = k / n * 2 * math.pi + rr.uniform(-.12, .12); r = R * rr.uniform(.72, .98)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for x, y in pts:
        mx, my = (cx + x) / 2 + rr.uniform(-R * .12, R * .12), (cy + y) / 2 + rr.uniform(-R * .12, R * .12)
        o += f'<path d="M{cx},{cy} Q{mx:.1f},{my:.1f} {x:.1f},{y:.1f}" fill="none" stroke="{fill}" stroke-width="{R * .03:.1f}"/>'
    for x, y in pts:
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R * .08:.1f}" fill="{dot}" stroke="{fill}" stroke-width="{R * .03:.1f}"/>'
    o += f'<circle cx="{cx}" cy="{cy}" r="{R * .22:.1f}" fill="{fill}"/><path d="M{cx - R * .1:.1f},{cy + R * .06:.1f} V{cy - R * .04:.1f} L{cx:.1f},{cy - R * .12:.1f} L{cx + R * .1:.1f},{cy - R * .04:.1f} V{cy + R * .06:.1f} Z" fill="{nha}"/>'
    return o


def y10_logo():
    s = ban_do(125, 150, 100) + T("An Tâm", 96, 250, 164, DO, "b9", track=-.02) + T("XƯỞNG CHUNG CỦA NHỮNG CĂN BẾP", 13, 254, 198, DEN, "b8", track=.2)
    return svg(int(250 + max(Tw("An Tâm", 96, "b9", -.02), Tw("XƯỞNG CHUNG CỦA NHỮNG CĂN BẾP", 13, "b8", .2)) + 30), 300, s, "Logo Bản Đồ Bếp")


def y10_ung_dung():
    s = f'<rect width="520" height="360" fill="{DO}"/>' + ban_do(150, 180, 120, KEM, NGO, 12, nha=DO)
    s += T("[số]+", 64, 300, 160, NGO, "nen") + T("căn bếp đối tác", 22, 300, 192, KEM, "b8") + T("dùng bánh An Tâm mỗi ngày", 15, 300, 218, "#FFD6D6", "b6")
    s += T("(Số liệu cần công ty xác nhận)", 11, 300, 250, "#FFD6D6", "b4")
    return svg(520, 360, s, "Bài đăng Bản Đồ Bếp")


IDEAS = [
    dict(num="06", name="Taco Cười", logo=y6_logo, app=y6_ung_dung, pal=[DO, NGO, LA, KEM],
         insight="Thương hiệu thực phẩm được nhớ lâu khi có một chi tiết cảm xúc đơn giản; khách B2B cũng là người – họ muốn nhà cung cấp dễ chịu, dễ làm việc.",
         idea="Nét cong của vỏ taco gập đặt dưới chữ \"an tâm\" thành một nụ cười. Sản phẩm và cảm xúc trong một nét: ăn ngon, bán chạy, chủ quán an tâm mà cười.",
         hop="Cực đơn giản, thân thiện, dễ nhớ; dùng tốt trên bao bì, ảnh đại diện, sticker.", luu="Ý tưởng nụ cười dưới chữ đã có thương hiệu lớn dùng – cần vẽ đúng dáng vỏ taco để khác biệt rõ."),
    dict(num="07", name="Gạch Bông", logo=y7_logo, app=y7_ung_dung, pal=[DO, KEM, NGO, XANH_GACH],
         insight="Gạch bông là ký ức chung của nhà Sài Gòn, Hội An; xu hướng 2026 chuộng hoa văn văn hoá bản địa.",
         idea="Logo là một viên gạch bông: giữa là chiếc bánh tròn, bốn chiếc lá, bốn góc cung tròn. Ghép nhiều viên lại thành hoa văn cho giấy gói, hộp, tường quầy – mỗi viên là một căn bếp.",
         hop="Rất Việt, đẹp khi lặp lại, cho bộ hoa văn bao bì phong phú.", luu="Logo dạng hoa văn khó đọc ở cỡ rất nhỏ – cần bản rút gọn chỉ còn chiếc bánh và lá."),
    dict(num="08", name="Điểm Chỉ", logo=y8_logo, app=y8_ung_dung, pal=[DO, KEM, DEN, NGO],
         insight="Người Việt lăn tay điểm chỉ bằng son đỏ để cam kết; khách B2B cần sự cam kết rõ ràng về chất lượng.",
         idea="Biểu tượng là dấu vân tay son đỏ – các đường vân tròn như chiếc bánh. Mỗi mẻ bánh đều có \"dấu tay\" người làm: làm thật, chịu trách nhiệm thật.",
         hop="Rất riêng, có chiều sâu văn hoá, nói đúng chữ \"tâm\" và \"cam kết\".", luu="Hình vân tay có thể gợi cảm giác giấy tờ – cần cách dùng ấm áp, gắn với người làm bánh."),
    dict(num="09", name="Xe Bánh", logo=y9_logo, app=y9_ung_dung, pal=[DO, KEM, NGO, DEN],
         insight="Rất nhiều khách hàng của An Tâm bán kebab bằng xe đẩy; nhà cung cấp lo cả bánh lẫn hình ảnh xe sẽ được chọn.",
         idea="Biểu tượng là chiếc xe đẩy bánh mì Sài Gòn: tủ kính, mái che, bánh xếp bên trong. An Tâm là người đồng hành cùng chiếc xe của từng đối tác – có thể trao kèm bộ dán xe mang thương hiệu.",
         hop="Nói đúng khách hàng mục tiêu, gợi chương trình hỗ trợ đại lý, rất gần gũi.", luu="Hình xe gắn với bán lẻ đường phố – hồ sơ cho nhà hàng lớn nên dùng bản chữ."),
    dict(num="10", name="Bản Đồ Bếp", logo=y10_logo, app=y10_ung_dung, pal=[DO, NGO, KEM, DEN],
         insight="\"Phát triển xứng tầm\" là lời hứa lớn cùng đối tác; doanh nghiệp B2B mạnh khi cho thấy mạng lưới khách hàng tin dùng.",
         idea="Xưởng An Tâm ở giữa, các tuyến giao toả ra những căn bếp đối tác, cùng nhau tạo thành vòng tròn chiếc bánh. Thương hiệu của một cộng đồng bếp cùng lớn lên.",
         hop="Hiện đại, hợp hồ sơ năng lực, website, gọi vốn hay mở rộng đại lý.", luu="Phải có số liệu thật (số đối tác, khu vực giao) – để [số] cho đến khi công ty xác nhận."),
]


def page():
    html = Y.page()
    Y.IDEAS[:] = IDEAS
    html = Y.page()
    html = html.replace("<title>Ý Tưởng Mới An Tâm</title>", "<title>Ý Tưởng Mới An Tâm – Đợt 2</title>")
    html = html.replace("5 ý tưởng mới cho Ẩm Thực An Tâm", "Thêm 5 ý tưởng khác cho An Tâm")
    html = html.replace("Bạn chọn ý tưởng số mấy?", "Bạn chọn ý tưởng số mấy (01–10)?")
    html = html.replace("Có thể ghép: ví dụ biểu tượng của 03 với cách kể chuyện của 05.", "Có thể chọn từ cả hai đợt (01–05 và 06–10), hoặc ghép hai ý tưởng với nhau.")
    return html


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

"""Cẩm nang tiêu chuẩn nhận diện thương hiệu Ẩm Thực An Tâm (hướng Điểm Chỉ). Chạy: python3 build_chuan.py OUT.html"""
import base64
import os
import sys

import build_van as B

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist", "AnTamTronBanh")
V = B.V
V.F["xb"] = os.path.join(DIST, "AnTamTronBanh-ExtraBold.ttf")
V.F["md"] = os.path.join(DIST, "AnTamTronBanh-SemiBold.ttf")
V._f.cache_clear()
DO, DO2, SON, KEM, GIAY, MUC, NGO = V.DO, V.DO2, V.SON, V.KEM, V.GIAY, V.MUC, V.NGO


def b64(p, mime="font/woff2"):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    return "\n".join(f"@font-face{{font-family:'An Tam Tron Banh';font-weight:{w};font-display:swap;src:url({b64(os.path.join(DIST, f'AnTamTronBanh-{n}.woff2'))}) format('woff2')}}"
                     for n, w in (("Regular", 400), ("SemiBold", 600), ("ExtraBold", 800)))


def lum(h):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    return .2126 * ch(r) + .7152 * ch(g) + .0722 * ch(b)


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + .05) / (lb + .05)


def cmyk(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    return tuple(round(x * 100) for x in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def vung_an_toan():
    """Sơ đồ khoảng trống an toàn quanh logo ngang: x = chiều cao vân tay / 2."""
    lg = V.logo_ngang()
    vb = [float(v) for v in lg.split('viewBox="')[1].split('"')[0].split()]
    w, h = vb[2], vb[3]; x = 60
    W, H = w + 2 * x, h + 2 * x
    s = f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" fill="#FBE7E4"/><rect x="{x}" y="{x}" width="{w:.0f}" height="{h:.0f}" fill="#fff"/>'
    s += lg.replace("<svg ", f'<svg x="{x}" y="{x}" width="{w:.0f}" height="{h:.0f}" ', 1)
    s += f'<rect x="{x}" y="{x}" width="{w:.0f}" height="{h:.0f}" fill="none" stroke="{DO}" stroke-width="2" stroke-dasharray="8 6"/>'
    for (ax, ay, bx, by, lx, ly) in ((0, H / 2, x, H / 2, x / 2, H / 2 - 10), (W - x, H / 2, W, H / 2, W - x / 2, H / 2 - 10), (W / 2, 0, W / 2, x, W / 2 + 22, x / 2 + 8), (W / 2, H - x, W / 2, H, W / 2 + 22, H - x / 2 + 8)):
        s += f'<path d="M{ax:.0f},{ay:.0f} L{bx:.0f},{by:.0f}" stroke="{MUC}" stroke-width="2"/><text x="{lx:.0f}" y="{ly:.0f}" font-family="An Tam Tron Banh" font-weight="800" font-size="22" fill="{MUC}" text-anchor="middle">x</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-label="Khoảng trống an toàn quanh logo">{s}</svg>'


def sai(kind):
    """Các cách dùng logo bị cấm, mỗi ô kèm dấu X đỏ."""
    lg = V.logo_ngang()
    vb = lg.split('viewBox="')[1].split('"')[0]
    inner = lg[lg.index(">") + 1:lg.rindex("</svg>")]
    t = {"gian": f'<g transform="translate(20 40) scale(1.25 .55)">{inner}</g>',
         "mau": f'<g transform="translate(30 20) scale(.6)" style="filter:hue-rotate(160deg)">{inner}</g>',
         "xoay": f'<g transform="translate(70 0) rotate(14) scale(.55)">{inner}</g>',
         "bong": f'<defs><filter id="sb"><feDropShadow dx="6" dy="8" stdDeviation="3" flood-color="#000" flood-opacity=".6"/></filter></defs><g filter="url(#sb)" transform="translate(30 20) scale(.6)">{inner}</g>',
         "nen": "".join(f'<rect x="{i * 40}" y="0" width="20" height="260" fill="#F5B82E"/>' for i in range(12)) + f'<g transform="translate(30 20) scale(.6)">{inner}</g>',
         "tach": f'<g transform="translate(30 20) scale(.6)">{inner.split("</g>", 1)[1] if "</g>" in inner else inner}</g>'}[kind]
    x = '<path d="M400,20 L440,60 M440,20 L400,60" stroke="#D2141E" stroke-width="8" stroke-linecap="round"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" role="img" aria-label="Cách dùng sai: {kind}"><rect width="460" height="200" fill="#fff"/><svg x="0" y="0" width="460" height="200" viewBox="0 0 460 200">{t}</svg>{x}</svg>'


CSS = """
:root{--do:#D2141E;--do2:#8F0D14;--son:#E2332B;--kem:#FFF6EA;--giay:#F6EEE2;--muc:#231716;--ngo:#F5B82E}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--giay);color:var(--muc);font:400 16px/1.65 'An Tam Tron Banh',system-ui,sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
b,strong{font-weight:800}
.hero{background:var(--do);color:var(--kem);position:relative;overflow:hidden}
.hero .bg{position:absolute;inset:0;opacity:.45}.hero .bg svg{width:100%;height:100%}
.hero .in{position:relative;max-width:1200px;margin:0 auto;padding:64px 20px 56px;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:40px;align-items:center}
.k{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--ngo)}
.hero h1{font-weight:800;font-size:clamp(44px,6.4vw,92px);line-height:1.05;letter-spacing:-.01em;margin:12px 0 16px}
.hero p{max-width:560px;font-size:17px;color:#FFE1DE}
.hero .card{background:var(--kem);padding:26px;border-radius:6px}
nav.toc{position:sticky;top:0;z-index:5;background:var(--muc);padding:10px 20px;display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
nav.toc a{color:var(--kem);font-weight:600;font-size:13px;text-decoration:none;border:1px solid #ffffff3a;border-radius:999px;padding:4px 12px}
section.s{max-width:1200px;margin:0 auto;padding:76px 20px 8px;scroll-margin-top:60px}
.num{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--do)}
.s h2{font-weight:800;font-size:clamp(34px,4.6vw,58px);line-height:1.06;color:var(--do);margin:8px 0 12px}
.s h3{font-weight:800;font-size:22px;color:var(--do2);margin:28px 0 10px}
.s .lead{max-width:760px;margin:0 0 24px;font-size:17px}
.g{display:grid;gap:18px;align-items:start}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.card{background:#fff;padding:22px;border-radius:6px}.card.d{background:var(--do);color:var(--kem)}.card.k2{background:var(--muc);color:var(--kem)}
.card h4{font-weight:800;font-size:19px;color:var(--do);margin-bottom:4px}.card.d h4,.card.k2 h4{color:var(--ngo)}
.cap{font-size:13px;margin-top:10px;color:#6b5a55}.card.d .cap,.card.k2 .cap{color:#FFD6D3}
.rule{display:grid;grid-template-columns:28px minmax(0,1fr);gap:10px;margin:8px 0}.rule i{font-style:normal;font-weight:800;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;color:#fff}
.ok i{background:#2F7D45}.no i{background:var(--do)}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:6px;overflow:hidden;font-size:15px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid #EFE4D3;vertical-align:top}th{background:var(--muc);color:var(--kem);font-weight:800;font-size:13px;letter-spacing:.06em}
.sw{background:#fff;border-radius:6px;overflow:hidden}.sw .c{height:120px;display:flex;align-items:flex-end;padding:10px;font-weight:800;font-size:13px}
.sw p{padding:12px 14px;font-size:13px;line-height:1.55}.sw b{display:block;font-size:18px;color:var(--do)}
.bar{display:flex;height:46px;border-radius:6px;overflow:hidden;margin-top:14px}
.ty div{border-bottom:1px solid #EFE4D3;padding:14px 0;display:grid;grid-template-columns:200px minmax(0,1fr);gap:16px;align-items:baseline}
.ty span{font-size:13px;color:#6b5a55}
.voice td:first-child{font-weight:800;color:var(--do);width:22%}
.end{text-align:center;padding:72px 20px 90px}
code{background:#fff;border:1px solid #EADFCD;border-radius:4px;padding:1px 6px;font-size:13px}
@media (max-width:860px){.hero .in,.g2,.g3,.g4{grid-template-columns:minmax(0,1fr)}.ty div{grid-template-columns:minmax(0,1fr)}.s{padding-top:56px}table{font-size:13px}th,td{padding:9px}}
"""

COLORS = [("Đỏ An Tâm", "#D2141E", "Màu chính – logo, nền lớn, tiêu đề", "60%"), ("Kem giấy", "#FFF6EA", "Nền giấy, chữ trên nền đỏ", "25%"),
          ("Mực", "#231716", "Chữ thân, đường kẻ", "10%"), ("Đỏ son", "#E2332B", "Chỉ cho dấu vân tay, con dấu", "–"),
          ("Đỏ đậm", "#8F0D14", "Nền sâu, chữ phụ trên nền sáng", "–"), ("Vàng bánh", "#F5B82E", "Điểm nhấn: giá, nhãn mới", "≤5%")]


def page():
    sw = ""
    for n, h, u, ratio in COLORS:
        c, m, y, k = cmyk(h); r, g, b = rgb(h)
        txt = KEM if lum(h) < .3 else MUC
        sw += f'<div class="sw"><div class="c" style="background:{h};color:{txt};{"border-bottom:1px solid #eee" if h == "#FFF6EA" else ""}">{ratio}</div><p><b>{n}</b>HEX {h}<br>RGB {r} {g} {b}<br>CMYK {c} {m} {y} {k} <span style="color:#6b5a55">(tham khảo)</span><br>{u}</p></div>'
    pairs = [("Kem trên Đỏ", KEM, DO), ("Đỏ trên Kem", DO, KEM), ("Mực trên Kem", MUC, KEM), ("Trắng trên Đỏ", "#FFFFFF", DO), ("Vàng trên Đỏ", NGO, DO), ("Đỏ trên Vàng", DO, NGO)]
    ct = "".join(f'<tr><td><span style="display:inline-block;background:{bg};color:{fg};font-weight:800;padding:4px 10px;border-radius:4px">Aa Âm</span> {n}</td><td>{contrast(fg, bg):.1f} : 1</td><td>{"Chữ mọi cỡ" if contrast(fg, bg) >= 4.5 else ("Chỉ chữ lớn ≥ 24px / tiêu đề" if contrast(fg, bg) >= 3 else "Không dùng cho chữ")}</td></tr>' for n, fg, bg in pairs)
    dt_a, dt_b = B.danh_thiep()
    nav = "".join(f'<a href="#c{i}">{t}</a>' for i, t in enumerate(["Nền tảng", "Logo", "Quy tắc logo", "Màu", "Chữ", "Hoạ tiết", "Hình ảnh", "Bố cục", "Ứng dụng", "Giọng nói", "Tệp"], 1))
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cẩm Nang An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="hero"><div class="bg">{B.nen_van(1400, 760)}</div><div class="in"><div><div class="k">Cẩm nang tiêu chuẩn nhận diện · Phiên bản 1.0</div>
<h1>Ẩm Thực An Tâm</h1><p>Tài liệu này quy định cách dùng logo, màu, chữ, hoạ tiết và giọng nói của thương hiệu. Mọi ấn phẩm – từ phiếu giao hàng tới biển hiệu – làm theo cùng một chuẩn để khách hàng nhìn là nhận ra An Tâm.</p></div>
<div class="card">{V.logo_dung()}</div></div></header>
<nav class="toc">{nav}</nav>

<section class="s" id="c1"><div class="num">01 · Nền tảng thương hiệu</div><h2>Mỗi mẻ bánh, một lời cam kết</h2>
<p class="lead">Ẩm Thực An Tâm cung cấp bánh tortilla, vỏ taco và doner kebab cho quán ăn, nhà hàng, cửa hàng và đối tác nhượng quyền tại TP.HCM. Biểu tượng dấu vân tay son đỏ lấy từ tục điểm chỉ của người Việt: lăn tay để cam kết điều quan trọng.</p>
<div class="g g4"><div class="card d"><h4>Tận tâm</h4><p>Làm từng mẻ bánh như làm cho nhà mình.</p></div><div class="card"><h4>Đáng tin</h4><p>Nói được làm được: đúng chất lượng, đúng hẹn.</p></div><div class="card"><h4>Gần gũi</h4><p>Ấm áp, dễ nói chuyện, đồng hành cùng chủ quán.</p></div><div class="card k2"><h4>Rõ ràng</h4><p>Thông tin minh bạch, giá và cam kết nói thẳng.</p></div></div>
<h3>Thông tin cố định</h3><table><tr><th>Mục</th><th>Nội dung</th></tr>
<tr><td>Tên trên ấn phẩm quảng bá</td><td>ẨM THỰC AN TÂM</td></tr><tr><td>Tên pháp lý (nhãn, hoá đơn, hợp đồng)</td><td>Công ty TNHH SX-TM Ẩm Thực An Tâm</td></tr>
<tr><td>Khẩu hiệu</td><td>Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm</td></tr><tr><td>Câu thương hiệu</td><td>Mỗi mẻ bánh, một lời cam kết</td></tr>
<tr><td>Liên hệ</td><td>antamfoods.com · 0348.635.222</td></tr></table></section>

<section class="s" id="c2"><div class="num">02 · Logo</div><h2>Các phiên bản logo</h2>
<p class="lead">Logo gồm biểu tượng dấu vân tay và chữ "An Tâm" viết bằng font thương hiệu. Ưu tiên bản ngang; dùng bản đứng khi khung hẹp; biểu tượng riêng chỉ dùng khi tên thương hiệu đã xuất hiện ở chỗ khác hoặc ở cỡ rất nhỏ.</p>
<div class="g g2"><div class="card">{V.logo_ngang()}<p class="cap">Bản ngang – bản chính</p></div><div class="card d">{V.logo_ngang(KEM, KEM)}<p class="cap">Bản ngang trên nền đỏ</p></div>
<div class="card">{V.logo_dung()}<p class="cap">Bản đứng</p></div><div class="g g2"><div class="card">{V.bieu_tuong()}<p class="cap">Biểu tượng</p></div><div class="card">{V.con_dau()}<p class="cap">Dấu tròn "Cam kết từ tâm" – dùng như con dấu, không thay logo</p></div></div></div>
<h3>Màu logo theo nền</h3><table><tr><th>Nền</th><th>Logo</th></tr><tr><td>Kem, trắng, ảnh sáng</td><td>Đỏ An Tâm (chữ phụ màu Mực)</td></tr><tr><td>Đỏ An Tâm, đỏ đậm</td><td>Kem toàn bộ</td></tr><tr><td>Đen, ảnh tối</td><td>Kem toàn bộ</td></tr><tr><td>In một màu (dập nổi, khắc, fax)</td><td>Một màu đặc – đen hoặc đỏ</td></tr></table></section>

<section class="s" id="c3"><div class="num">03 · Quy tắc dùng logo</div><h2>Khoảng trống, kích thước, điều cấm</h2>
<div class="g g2" style="align-items:center"><div class="card">{vung_an_toan()}</div><div><h3 style="margin-top:0">Khoảng trống an toàn</h3><p>Quanh logo luôn chừa khoảng trống ít nhất bằng <b>x = một nửa chiều cao dấu vân tay</b>. Không đặt chữ, hình hay mép giấy vào vùng này.</p>
<h3>Kích thước tối thiểu</h3><table><tr><th>Phiên bản</th><th>In ấn</th><th>Màn hình</th></tr><tr><td>Bản ngang</td><td>30 mm rộng</td><td>140 px</td></tr><tr><td>Bản đứng</td><td>20 mm rộng</td><td>96 px</td></tr><tr><td>Biểu tượng</td><td>8 mm</td><td>24 px</td></tr></table></div></div>
<h3>Không được</h3><div class="g g3">
<div class="card">{sai("gian")}<p class="cap">Kéo giãn, bóp méo</p></div><div class="card">{sai("mau")}<p class="cap">Đổi màu ngoài bảng màu</p></div><div class="card">{sai("xoay")}<p class="cap">Xoay nghiêng</p></div>
<div class="card">{sai("bong")}<p class="cap">Thêm đổ bóng, hiệu ứng</p></div><div class="card">{sai("nen")}<p class="cap">Đặt trên nền rối, thiếu tương phản</p></div><div class="card">{sai("tach")}<p class="cap">Tự ý tách, sắp xếp lại các phần</p></div></div>
<p style="margin-top:12px">Ngoài ra: không đổi font chữ trong logo, không vẽ lại dấu vân tay, không thêm chữ khác sát logo.</p></section>

<section class="s" id="c4"><div class="num">04 · Màu</div><h2>Bảng màu</h2>
<p class="lead">Đỏ An Tâm là màu nhận diện. Kem giấy làm nền nghỉ mắt. Đỏ son dành riêng cho dấu vân tay. Vàng bánh chỉ điểm xuyết. Giá trị CMYK là quy đổi tham khảo – cần in thử và chốt với nhà in; mã Pantone: [Cần điền sau khi in thử].</p>
<div class="g g3">{sw}</div>
<div class="bar"><div style="flex:60;background:{DO}"></div><div style="flex:25;background:{KEM}"></div><div style="flex:10;background:{MUC}"></div><div style="flex:5;background:{NGO}"></div></div><p class="cap">Tỉ lệ diện tích gợi ý trên một ấn phẩm: 60 đỏ – 25 kem – 10 mực – 5 vàng</p>
<h3>Cặp màu chữ và độ tương phản</h3><table><tr><th>Cặp màu</th><th>Tương phản</th><th>Dùng cho</th></tr>{ct}</table></section>

<section class="s" id="c5"><div class="num">05 · Chữ</div><h2>Font An Tâm Tròn Bánh</h2>
<p class="lead">Font thương hiệu riêng (tên cài đặt <b>"An Tam Tron Banh"</b>), dựng từ Baloo 2 – giấy phép SIL OFL, dùng miễn phí cho in ấn và website. Ba nét riêng: dấu mũ â ê ô là ba đường vân tay; dấu chấm là vòng xoáy vân tay; góc chữ bo như mực son loang. Font thay thế khi không cài được: <b>Baloo 2</b>.</p>
<div class="g g3"><div class="card"><div style="font-weight:800;font-size:64px;line-height:1.15;color:{DO}">Âm 800</div><p class="cap">ExtraBold – logo, tiêu đề, chữ lớn</p></div><div class="card"><div style="font-weight:600;font-size:64px;line-height:1.15;color:{DO}">Âm 600</div><p class="cap">SemiBold – tiêu đề phụ, nhãn, bảng giá</p></div><div class="card"><div style="font-weight:400;font-size:64px;line-height:1.15;color:{DO}">Âm 400</div><p class="cap">Regular – đoạn văn, báo giá, hợp đồng</p></div></div>
<h3>Thang cỡ chữ</h3><div class="card ty">
<div><span>Tiêu đề lớn · ExtraBold<br>In 48–72 pt · Số 48–64 px</span><p style="font-weight:800;font-size:52px;line-height:1.1;color:{DO}">Bánh nóng, giao tận bếp</p></div>
<div><span>Tiêu đề · ExtraBold<br>In 24–36 pt · Số 28–36 px</span><p style="font-weight:800;font-size:32px;line-height:1.2">Bảng giá đại lý tháng này</p></div>
<div><span>Tiêu đề phụ · SemiBold<br>In 14–18 pt · Số 20–22 px</span><p style="font-weight:600;font-size:21px">Bánh tortilla 10 inch – gói 10 chiếc</p></div>
<div><span>Nội dung · Regular<br>In 9–11 pt · Số 16 px</span><p style="font-size:16px">Bánh được làm mới mỗi ngày tại xưởng và giao tận bếp quán ăn, nhà hàng tại TP.HCM. Đặt hàng trước [giờ] để nhận trong ngày.</p></div>
<div><span>Nhãn chữ hoa · ExtraBold<br>Giãn chữ +20%</span><p style="font-weight:800;font-size:13px;letter-spacing:.22em;color:{DO}">ẨM THỰC · SẢN PHẨM TẬN TÂM</p></div>
<div><span>Chú thích · Regular<br>In 7–8 pt · Số 13 px</span><p style="font-size:13px;color:#6b5a55">Giá chưa gồm VAT. Hình ảnh mang tính minh hoạ.</p></div></div>
<h3>Quy tắc</h3><div class="g g2"><div><div class="rule ok"><i>✓</i><p>Căn trái cho đoạn văn; căn giữa chỉ cho tiêu đề ngắn.</p></div><div class="rule ok"><i>✓</i><p>Chữ hoa nhỏ luôn giãn chữ +20%, dùng ExtraBold.</p></div><div class="rule ok"><i>✓</i><p>Khoảng cách dòng: tiêu đề 1.05–1.2, nội dung 1.5–1.65.</p></div></div>
<div><div class="rule no"><i>✕</i><p>Không làm nghiêng giả, không kéo dãn chữ.</p></div><div class="rule no"><i>✕</i><p>Không viết hoa cả đoạn văn dài.</p></div><div class="rule no"><i>✕</i><p>Không dùng quá 2 độ đậm trên một ấn phẩm nhỏ.</p></div></div></div></section>

<section class="s" id="c6"><div class="num">06 · Hoạ tiết</div><h2>Đường vân và dấu tay</h2>
<p class="lead">Ba yếu tố đồ hoạ: nền đường vân (phóng to một góc vân tay), dấu vân tay rời, và dấu tròn "Cam kết từ tâm".</p>
<div class="card" style="padding:0;overflow:hidden">{B.nen_van(1200, 300)}</div>
<div class="g g2" style="margin-top:18px"><div><div class="rule ok"><i>✓</i><p>Nền đường vân dùng 2 màu đỏ gần nhau (Đỏ An Tâm + Đỏ son), để chữ đặt trên khung kem.</p></div><div class="rule ok"><i>✓</i><p>Mỗi ấn phẩm tối đa một dấu vân tay lớn.</p></div><div class="rule ok"><i>✓</i><p>Dấu tròn dùng như con dấu: trên phiếu, tem niêm phong, góc hộp.</p></div></div>
<div><div class="rule no"><i>✕</i><p>Không đổi dấu vân tay sang màu khác Đỏ son, Đỏ An Tâm, Kem.</p></div><div class="rule no"><i>✕</i><p>Không cắt mất lõi xoáy của vân tay.</p></div><div class="rule no"><i>✕</i><p>Không đặt chữ nhỏ trực tiếp trên nền đường vân.</p></div></div></div></section>

<section class="s" id="c7"><div class="num">07 · Hình ảnh</div><h2>Hướng chụp ảnh</h2>
<p class="lead">Ảnh thật của xưởng, của người làm bánh và của món ăn ở quán khách hàng. Không dùng ảnh mẫu nước ngoài cho sản phẩm.</p>
<div class="g g3"><div class="card"><h4>Đôi tay & mẻ bánh</h4><p>Cận cảnh tay nhào, cán, xếp bánh; bánh vừa ra lò còn hơi nóng.</p></div><div class="card"><h4>Ánh sáng ấm</h4><p>Ánh sáng tự nhiên, tông ấm; nền gỗ, giấy kraft hoặc kem. Màu đỏ thương hiệu xuất hiện qua hộp, tạp dề, tem.</p></div><div class="card"><h4>Món ăn ở quán</h4><p>Taco, doner cuộn tại quán đối tác – có khách thật, có chủ quán thật (khi được đồng ý).</p></div></div>
<div class="g g2" style="margin-top:14px"><div><div class="rule no"><i>✕</i><p>Lọc màu lạnh, xanh, quá bão hoà.</p></div></div><div><div class="rule no"><i>✕</i><p>Ảnh có nhãn hiệu khác, ảnh mạng không rõ quyền dùng.</p></div></div></div></section>

<section class="s" id="c8"><div class="num">08 · Bố cục</div><h2>Khổ và lề chuẩn</h2>
<table><tr><th>Ấn phẩm</th><th>Khổ</th><th>Lề an toàn</th><th>Logo</th></tr>
<tr><td>Bài đăng mạng xã hội</td><td>1080 × 1350 px</td><td>72 px</td><td>Biểu tượng hoặc bản ngang, góc trên trái / dưới</td></tr>
<tr><td>Story, Reels</td><td>1080 × 1920 px</td><td>Trên 250 px · dưới 340 px</td><td>Bản ngang, phía trên</td></tr>
<tr><td>Báo giá, thư</td><td>A4 (210 × 297 mm)</td><td>15 mm</td><td>Bản ngang, góc trên trái, rộng 45 mm</td></tr>
<tr><td>Danh thiếp</td><td>90 × 54 mm, chừa xén 2 mm</td><td>4 mm</td><td>Bản ngang mặt trước</td></tr>
<tr><td>Phiếu giao hàng</td><td>A5 (148 × 210 mm)</td><td>10 mm</td><td>Bản ngang, rộng 40 mm</td></tr>
<tr><td>Tem niêm phong</td><td>Tròn Ø 40 mm</td><td>3 mm</td><td>Dấu tròn</td></tr></table></section>

<section class="s" id="c9"><div class="num">09 · Ứng dụng</div><h2>Ấn phẩm mẫu</h2><p class="lead">Chỗ trong ngoặc vuông là thông tin cần điền thật trước khi in.</p>
<div class="g g2"><div class="card">{B.phieu()}<p class="cap">Phiếu giao hàng</p></div><div class="card">{B.the_tho()}<p class="cap">Thẻ "Mẻ bánh hôm nay"</p></div>
<div class="card">{B.tui()}<p class="cap">Túi bánh tortilla</p></div><div class="card">{B.bai_dang()}<p class="cap">Bài đăng mạng xã hội</p></div>
<div class="card">{B.xe()}<p class="cap">Xe giao hàng</p></div><div class="g"><div class="card">{dt_a}<p class="cap">Danh thiếp – mặt trước</p></div><div class="card">{dt_b}<p class="cap">Danh thiếp – mặt sau</p></div></div></div></section>

<section class="s" id="c10"><div class="num">10 · Giọng nói</div><h2>Cách An Tâm nói chuyện</h2>
<p class="lead">Như một người làm bánh có tâm nói với chủ quán: ngắn, thật, ấm. Không nói quá, không so sánh hạ thấp ai.</p>
<table class="voice"><tr><th>Nguyên tắc</th><th>Nên viết</th><th>Tránh viết</th></tr>
<tr><td>Thật</td><td>Bánh làm mới mỗi ngày, giao trước [giờ].</td><td>Bánh ngon nhất Việt Nam, số 1 thị trường.</td></tr>
<tr><td>Ấm</td><td>Cần thêm bánh gấp? Gọi An Tâm, tụi mình lo.</td><td>Quý khách vui lòng liên hệ bộ phận chăm sóc khách hàng.</td></tr>
<tr><td>Rõ</td><td>Giá gói 10 chiếc: [giá]. Chưa gồm VAT.</td><td>Giá cực sốc, liên hệ để biết!!!</td></tr>
<tr><td>Tôn trọng</td><td>Chúng tôi tập trung vào chất lượng mỗi mẻ bánh.</td><td>Không như bên khác, hàng chúng tôi...</td></tr></table></section>

<section class="s" id="c11"><div class="num">11 · Tệp</div><h2>Tệp gốc</h2>
<table><tr><th>Nội dung</th><th>Vị trí trong kho thiết kế</th></tr>
<tr><td>Font (TTF, WOFF2, hướng dẫn cài, giấy phép)</td><td><code>plugins/design/assets/diem-chi/font-an-tam-tron-banh/</code> và file nén <code>AnTamTronBanh.zip</code></td></tr>
<tr><td>Logo SVG (vector, in sắc nét)</td><td><code>plugins/design/assets/diem-chi/logo/</code></td></tr>
<tr><td>Logo PNG nền trong suốt</td><td><code>plugins/design/assets/diem-chi/logo-png/</code></td></tr>
<tr><td>Hoạ tiết, ấn phẩm mẫu SVG</td><td><code>plugins/design/assets/diem-chi/hoa-tiet/</code>, <code>ung-dung/</code></td></tr></table></section>

<div class="end"><div style="max-width:560px;margin:0 auto">{V.logo_ngang()}</div><p class="cap" style="margin-top:12px">Cẩm nang nhận diện Ẩm Thực An Tâm · Phiên bản 1.0</p></div>
</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

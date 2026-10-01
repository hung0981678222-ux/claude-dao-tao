"""Trang trình bày bộ nhận diện "Gói Trọn" cho Ẩm Thực An Tâm. Chạy: python3 build_goi.py OUT.html"""
import base64
import os
import random
import sys

import logo_goi as G

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
XANH, LA, NGO, NGO2, KEM, CA, NAU, DEN = G.XANH, G.LA, G.NGO, G.NGO2, G.KEM, G.CA, G.NAU, G.DEN
KRAFT, KRAFT2 = "#CDA676", "#B98F5D"


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = [f"@font-face{{font-family:'An Tam La';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'fonts-la', f'AnTamLa-{n}.woff2'), 'font/woff2')}) format('woff2')}}" for n, w in (("ExtraBold", 800), ("SemiBold", 600))]
    for w in (400, 600):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'be-vietnam-pro', 'files', f'be-vietnam-pro-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    return "\n".join(out)


def place(svg, x, y, w, h):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


def img(n, x, y, w, h):
    return f'<image href="{b64(f"{MH}/{n}.svg", "image/svg+xml")}" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def T(t, size, x, y, fill=XANH, k="xb", anchor="start", track=0.0, leaf=None):
    return G.text(t, size, k, x, y, fill, leaf, anchor, track)[0]


# ---------- hoạ tiết ----------
def nen_goi(w, h, bg=XANH, uid="ng"):
    """Nền lặp: bánh gói nhỏ xen lá gập, hàng so le."""
    s = f'<rect width="{w}" height="{h}" fill="{bg}"/>'
    for j, y in enumerate(range(20, h + 120, 120)):
        for i, x in enumerate(range(-60 + (60 if j % 2 else 0), w + 120, 120)):
            if (i + j) % 2 == 0:
                s += f'<g transform="translate({x} {y}) scale(.42)" opacity=".95">{G.mark(200)}</g>'
            else:
                s += f'<g opacity=".55">{G.nut_la(x + 42, y + 30, 60, LA)}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Nền bánh gói">{s}</svg>'


def lat(w, h=24, c=XANH, c2=LA):
    """Dải lạt: dùng làm đường phân cách."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="none" role="img" aria-label="Dải lạt">'
            f'<rect width="{w}" height="{h}" fill="{c}"/><rect y="{h * .38:.1f}" width="{w}" height="{h * .24:.1f}" fill="{c2}"/></svg>')


# ---------- ứng dụng ----------
def hop():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 420" role="img" aria-label="Hộp giao hàng buộc lạt">
<defs><filter id="hs"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#14231C" flood-opacity=".25"/></filter></defs>
<g filter="url(#hs)"><path d="M60,150 L260,62 L460,150 L260,238 Z" fill="{KEM}"/>
<path d="M60,150 L260,238 L260,378 L60,290 Z" fill="{KRAFT}"/><path d="M260,238 L460,150 L460,290 L260,378 Z" fill="{KRAFT2}"/></g>
<path d="M160,106 L360,194 M360,106 L160,194" stroke="{XANH}" stroke-width="18"/><path d="M160,106 L360,194 M360,106 L160,194" stroke="{LA}" stroke-width="5"/>
<path d="M160,194 L160,334 M360,194 L360,334" stroke="{XANH}" stroke-width="18"/><path d="M160,194 L160,334 M360,194 L360,334" stroke="{LA}" stroke-width="5"/>
<circle cx="260" cy="150" r="20" fill="{XANH}"/>{G.nut_la(260, 140, 92, LA)}
<g transform="matrix(.82 .36 0 .9 74 214)">{T("an tâm", 46, 0, 0, XANH, leaf=LA)}</g>
</svg>'''


def tui():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" role="img" aria-label="Túi bánh tortilla">
<defs><linearGradient id="tk" x1="0" x2="1"><stop offset="0" stop-color="#DDE9D2"/><stop offset=".4" stop-color="#F3F7EE"/><stop offset="1" stop-color="#D3E2C6"/></linearGradient>
<filter id="ts"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#14231C" flood-opacity=".25"/></filter></defs>
<g filter="url(#ts)"><path d="M72,64 L348,64 L368,492 L52,492 Z" fill="{XANH}"/><path d="M72,64 L348,64 L345,96 L75,96 Z" fill="#0B3A2C"/></g>
<rect x="72" y="104" width="276" height="16" fill="{LA}"/>
{place(G.logo_dung(KEM, "#9FD27A", KEM), 92, 128, 236, 160)}
<rect x="96" y="300" width="228" height="140" rx="24" fill="{NGO}"/>
{img("banh-tortillas", 120, 296, 180, 136)}
<g>{T("BÁNH TORTILLA", 22, 210, 470, KEM, "xb", "middle", .04)}</g>
<g>{T("[Cần điền: số chiếc · khối lượng]", 12, 210, 486, "#CFE3C2", "sb", "middle")}</g>
</svg>'''


def xe():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 380" role="img" aria-label="Xe giao hàng">
<rect width="720" height="380" fill="#E9F0E2"/><rect y="318" width="720" height="62" fill="#C9D6BD"/>
<path d="M60,90 H470 V300 H60 Z" fill="{KEM}"/><path d="M470,150 H580 L650,210 V300 H470 Z" fill="{XANH}"/>
<path d="M490,165 H572 L622,212 H490 Z" fill="#BFD8E4"/>
<rect x="60" y="270" width="590" height="30" fill="{XANH}"/><rect x="60" y="281" width="590" height="8" fill="{LA}"/>
{place(G.logo_ngang(), 80, 120, 370, 110)}
{T("Giao bánh tận bếp mỗi sáng · 0348.635.222", 17, 84, 254, XANH, "sb")}
<circle cx="160" cy="310" r="36" fill="{DEN}"/><circle cx="160" cy="310" r="14" fill="#888"/><circle cx="560" cy="310" r="36" fill="{DEN}"/><circle cx="560" cy="310" r="14" fill="#888"/>
<g transform="translate(486 214) scale(.36)">{G.mark(200)}</g>
</svg>'''


def danh_thiep():
    a = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt trước">
<clipPath id="dtc"><rect width="520" height="300" rx="16"/></clipPath><g clip-path="url(#dtc)">{place(nen_goi(520, 300, XANH, "dt"), 0, 0, 520, 300)}</g>
<rect x="110" y="70" width="300" height="160" rx="22" fill="{KEM}"/>{place(G.logo_dung(), 130, 80, 260, 140)}</svg>'''
    b = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt sau">
<rect width="520" height="300" rx="16" fill="{KEM}"/><rect x="0" y="0" width="22" height="300" fill="{XANH}"/><rect x="8" y="0" width="6" height="300" fill="{LA}"/>
{T("[Cần điền: Họ tên]", 30, 56, 86, XANH)}{T("[Cần điền: Chức danh]", 16, 56, 116, CA, "sb")}
{T("0348.635.222", 17, 56, 182, DEN, "sb")}{T("antamfoods.com", 17, 56, 210, DEN, "sb")}{T("[Cần điền: địa chỉ xưởng, TP.HCM]", 15, 56, 238, DEN, "sb")}
<g transform="translate(386 76) scale(.56)">{G.mark(200)}</g></svg>'''
    return a, b


def bai_dang():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 675" role="img" aria-label="Bài đăng mạng xã hội">
<rect width="540" height="675" fill="{NGO}"/>
<rect x="0" y="300" width="540" height="40" fill="{XANH}"/><rect x="0" y="315" width="540" height="10" fill="{LA}"/>
<rect x="250" y="0" width="40" height="675" fill="{XANH}"/><rect x="265" y="0" width="10" height="675" fill="{LA}"/>
<rect x="60" y="60" width="420" height="555" rx="30" fill="{KEM}"/>
{T("Gói trọn", 64, 270, 150, XANH, "xb", "middle")}{T("sự an tâm", 64, 270, 222, XANH, "xb", "middle", leaf=LA)}
{img("taco", 130, 236, 280, 210)}
{T("Tortilla · Taco · Doner kebab", 21, 270, 482, CA, "sb", "middle")}
{T("Giao tận bếp quán, nhà hàng, đại lý", 18, 270, 512, DEN, "sb", "middle")}
<rect x="150" y="540" width="240" height="50" rx="25" fill="{XANH}"/>{T("0348.635.222", 24, 270, 574, KEM, "xb", "middle")}
</svg>'''


def bang_gia():
    """Bảng giá đại lý (khổ A5 dọc) – giá để trống."""
    rows = [("Bánh tortilla 8 inch", "[giá]"), ("Bánh tortilla 10 inch", "[giá]"), ("Vỏ taco", "[giá]"), ("Thịt doner (kg)", "[giá]"), ("Sốt doner", "[giá]")]
    r = ""
    for i, (n, p) in enumerate(rows):
        y = 238 + i * 52
        r += f'<rect x="40" y="{y - 32}" width="340" height="44" rx="10" fill="{"#fff" if i % 2 == 0 else KEM}"/>' + T(n, 16, 58, y - 4, DEN, "sb") + T(p, 16, 362, y - 4, CA, "xb", "end")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 560" role="img" aria-label="Bảng giá đại lý">
<rect width="420" height="560" rx="18" fill="#F3EFE3"/><rect width="420" height="150" rx="18" fill="{XANH}"/><rect y="132" width="420" height="18" fill="{XANH}"/><rect y="150" width="420" height="10" fill="{LA}"/>
{place(G.logo_ngang(KEM, "#9FD27A", KEM), 40, 26, 250, 76)}
{T("BẢNG GIÁ ĐẠI LÝ", 20, 40, 120, NGO, "xb", track=.06)}
{T("Áp dụng từ [Cần điền: ngày]", 12, 40, 140, "#CFE3C2", "sb")}
{r}
{T("Giá chưa gồm VAT · Đặt hàng: 0348.635.222", 13, 210, 520, XANH, "sb", "middle")}
</svg>'''


CSS = """
:root{--xanh:#0F4D3A;--la:#5E9E3C;--ngo:#F4B731;--kem:#FFF6E6;--ca:#E2412B;--den:#14231C}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--kem);color:var(--den);font:16px/1.6 'Be Vietnam Pro',system-ui,sans-serif}
h1,h2,h3,.k,.num{font-family:'An Tam La','Be Vietnam Pro',sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
.hero{background:var(--xanh);color:var(--kem);position:relative;overflow:hidden}
.hero .bg{position:absolute;inset:0;opacity:.18}.hero .bg svg{width:100%;height:100%}
.hero .in{position:relative;max-width:1200px;margin:0 auto;padding:72px 20px 64px;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:40px;align-items:center}
.k{font-weight:600;font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--ngo)}
.hero h1{font-weight:800;font-size:clamp(46px,6.4vw,92px);line-height:1;letter-spacing:-.02em;margin:14px 0 18px}
.hero p{max-width:560px;font-size:17px;color:#E4EEDF}
.hero .card{background:var(--kem);border-radius:32px;padding:30px}
.lat{height:22px}.lat svg{height:22px}
section.s{max-width:1200px;margin:0 auto;padding:72px 20px 8px}
.num{font-weight:600;font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--la)}
.s h2{font-weight:800;font-size:clamp(32px,4.2vw,52px);line-height:1.08;color:var(--xanh);letter-spacing:-.01em;margin:6px 0 10px}
.s .lead{max-width:720px;margin:0 0 28px;font-size:17px}
.g{display:grid;gap:18px;align-items:start}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:#fff;border-radius:26px;padding:24px;box-shadow:0 1px 0 #14231C14,0 10px 30px -18px #14231C55}
.card.x{background:var(--xanh);color:var(--kem)}.card.n{background:var(--ngo)}
.card h3{font-weight:800;font-size:22px;color:var(--xanh);margin-bottom:6px}.card.x h3{color:var(--ngo)}
.cap{font-size:14px;margin-top:10px;color:#4A5A52}.card.x .cap{color:#CFE3C2}
.chip{display:inline-block;font-size:13px;font-weight:600;border-radius:999px;padding:4px 12px;margin:4px 6px 0 0;background:#E7F0E0;color:var(--xanh)}
.sw{border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 10px 30px -20px #14231C66}
.sw div{height:120px}.sw p{padding:12px 14px;font-size:13px;line-height:1.45}.sw b{font-family:'An Tam La';font-weight:800;font-size:18px;display:block;color:var(--xanh)}
.big{font-family:'An Tam La';font-weight:800;font-size:clamp(46px,6.4vw,88px);line-height:1;color:var(--xanh);letter-spacing:-.02em}
.idea{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-items:stretch}
.idea .card{display:flex;flex-direction:column;gap:8px}
.eq{font-family:'An Tam La';font-weight:800;font-size:40px;color:var(--la);text-align:center;align-self:center}
.src{font-size:13px;color:#4A5A52}.src a{color:var(--xanh)}
.end{text-align:center;padding:80px 20px 96px}
@media (max-width:860px){.hero .in,.g2,.g3,.idea{grid-template-columns:minmax(0,1fr)}.s{padding-top:52px}}
"""


def page():
    dt_a, dt_b = danh_thiep()
    sw = [("Xanh lá chuối", "#0F4D3A", "Màu chính – nền, chữ, lạt buộc"), ("Lá non", "#5E9E3C", "Lá gập, sọc lạt, điểm tươi"), ("Vàng ngô", "#F4B731", "Chiếc bánh, mảng màu lớn"),
          ("Kem", "#FFF6E6", "Nền giấy, khoảng thở"), ("Đỏ cà chua", "#E2412B", "Giá, khuyến mãi – dùng ít"), ("Than", "#14231C", "Chữ thân")]
    sws = "".join(f'<div class="sw"><div style="background:{h}"></div><p><b>{n}</b>{h} · {u}</p></div>' for n, h, u in sw)
    mark_big = G.svg((0, 0, 200, 200), G.mark(200), "Biểu tượng bánh gói")
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gói Trọn An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="hero"><div class="bg">{nen_goi(1400, 760, XANH, "hb")}</div><div class="in">
<div><div class="k">Bộ nhận diện mới · Ẩm Thực An Tâm</div><h1>Gói trọn<br>sự an tâm</h1>
<p>Người Việt gói bánh trong lá và buộc lạt để giữ trọn vị ngon. Tortilla, taco, doner cũng là món cuộn, món gói. Bộ nhận diện mới lấy hình chiếc bánh gói buộc lạt làm biểu tượng — lời hứa rằng mỗi mẻ bánh giao đến bếp của bạn đều được gói ghém tận tâm.</p></div>
<div class="card">{G.logo_dung()}</div></div></header>
<div class="lat">{lat(1600)}</div>

<section class="s"><div class="num">01 · Tìm hiểu</div><h2>Thị trường đang nói gì</h2><p class="lead">Ẩm Thực An Tâm bán cho chủ quán, nhà hàng, cửa hàng và người mở điểm bán kebab – taco tại TP.HCM. Họ không mua một chiếc bánh, họ mua sự yên tâm cho cả ca bán hàng.</p>
<div class="g g3">
<div class="card"><h3>Đối thủ toàn đỏ, cam</h3><p>Các chuỗi bánh mì kebab và nhượng quyền phổ biến dùng cam, đỏ, xanh dương cùng hình que thịt quay. Ví dụ Kebab Torki dùng chữ trắng nền cam, Torki Food chuyển sang xanh chủ đạo với điểm cam. Đi tiếp màu đỏ sẽ bị lẫn.</p><span class="chip">Cần khác biệt màu</span></div>
<div class="card"><h3>Khách B2B cần yên tâm</h3><p>Điều chủ quán lo nhất: bánh đều cỡ, đều chất lượng, giao đúng giờ, an toàn thực phẩm, được hỗ trợ khi mới mở. Thương hiệu phải trông đáng tin, gọn gàng, nói rõ ràng – không cần ồn ào.</p><span class="chip">Tin cậy · rõ ràng</span></div>
<div class="card"><h3>Xu hướng 2026</h3><p>Bao bì thực phẩm năm 2026 nghiêng về chất "dân gian mộc mạc" (gần gũi, có gốc văn hoá), mảng màu mạnh, chữ có cá tính, thông tin minh bạch và vật liệu giấy, kraft thân thiện.</p><span class="chip">Gốc Việt · mảng màu</span></div></div>
<div class="card x" style="margin-top:18px"><h3>Định vị đề xuất</h3><p style="font-size:19px">Ẩm Thực An Tâm là <b>người gói trọn sự an tâm cho bếp của bạn</b>: bánh làm mỗi ngày, đều tay, giao tận nơi, đồng hành cùng quán phát triển. <span style="opacity:.8">(Các cam kết cụ thể như chứng nhận, giờ giao cần công ty xác nhận trước khi đưa lên ấn phẩm.)</span></p></div></section>

<section class="s"><div class="num">02 · Ý tưởng</div><h2>Bánh gói buộc lạt</h2><p class="lead">Ba thứ ghép lại thành một biểu tượng duy nhất.</p>
<div class="idea"><div class="card"><h3>Chiếc bánh cuộn</h3><p>Tortilla gấp bốn vạt vào giữa – đúng cách gói burrito, cũng là cách gói bánh của người Việt.</p></div>
<div class="card"><h3>Sợi lạt chữ thập</h3><p>Như lạt buộc bánh chưng: chắc chắn, chỉn chu, đủ đầy. Trên ấn phẩm, sợi lạt trở thành dải phân cách và khung.</p></div>
<div class="card"><h3>Chiếc lá gập</h3><p>Nút buộc là chiếc lá gập hình mái – và cũng chính là <b>dấu mũ của chữ â</b> trong "an tâm". Nét Việt nằm ngay trong chữ.</p></div></div>
<div class="g g2" style="margin-top:18px;align-items:center"><div class="card n" style="max-width:320px;justify-self:center;width:100%">{mark_big}</div>
<div><div class="big">an tâm</div><p style="margin-top:12px">Chữ dựng riêng từ Montserrat Alternates đậm, chữ a một tầng tròn trịa, thân thiện. Mọi dấu mũ â ê ô được thay bằng chiếc lá gập, nên dòng chữ nào có "â" cũng mang dấu ấn An Tâm.</p></div></div></section>

<section class="s"><div class="num">03 · Logo</div><h2>Logo và các phiên bản</h2><p class="lead">Bản ngang cho biển hiệu, xe, website; bản đứng cho bao bì, bìa hồ sơ; biểu tượng và tem tròn cho ảnh đại diện, tem niêm phong, dập nổi.</p>
<div class="g g2"><div class="card">{G.logo_ngang()}<p class="cap">Bản ngang – nền kem</p></div><div class="card x">{G.logo_ngang(KEM, "#9FD27A", KEM)}<p class="cap">Bản ngang – nền xanh</p></div>
<div class="card">{G.logo_dung()}<p class="cap">Bản đứng</p></div>
<div class="g g2"><div class="card">{G.bieu_tuong()}<p class="cap">Biểu tượng</p></div><div class="card">{G.tem()}<p class="cap">Tem tròn "Gói trọn tận tâm"</p></div></div></div></section>

<section class="s"><div class="num">04 · Màu</div><h2>Màu lá, màu bánh</h2><p class="lead">Xanh lá chuối làm chủ đạo để tách hẳn khỏi rừng đỏ – cam của ngành kebab, đồng thời gợi tươi, sạch, an toàn. Vàng ngô là màu chiếc bánh. Đỏ cà chua chỉ dùng cho giá và khuyến mãi.</p>
<div class="g g3">{sws}</div></section>

<section class="s"><div class="num">05 · Chữ</div><h2>Hai kiểu chữ</h2><p class="lead">An Tâm Lá (dựng từ Montserrat Alternates, có dấu mũ hình lá) cho tiêu đề và logo. Be Vietnam Pro – khung chữ do nhóm tác giả Việt thiết kế – cho nội dung. Cả hai là font mã nguồn mở SIL OFL, đủ dấu tiếng Việt.</p>
<div class="card"><div class="big">Bánh mới mỗi sáng, giao tận bếp</div><p style="margin-top:14px;font-size:18px">Be Vietnam Pro: Bánh tortilla mềm dẻo, vỏ taco giòn và thịt doner tẩm ướp sẵn cho quán ăn, nhà hàng và chuỗi cửa hàng tại TP.HCM. Báo giá đại lý: [giá].</p></div></section>

<section class="s"><div class="num">06 · Hoạ tiết</div><h2>Sợi lạt và bánh gói</h2><p class="lead">Sợi lạt xanh dùng làm đường phân cách và khung buộc nội dung; nền bánh gói lặp dùng cho bao bì, hộp, nền mạng xã hội.</p>
<div class="card" style="padding:0;overflow:hidden">{nen_goi(1200, 360, XANH, "pt")}</div></section>

<section class="s"><div class="num">07 · Ứng dụng</div><h2>Từ xưởng tới bếp khách</h2><p class="lead">Chỗ trong ngoặc vuông là thông tin cần điền thật trước khi in.</p>
<div class="g g2"><div class="card">{hop()}<p class="cap">Hộp giao hàng buộc lạt xanh – mở hộp như mở một chiếc bánh gói</p></div>
<div class="card">{tui()}<p class="cap">Túi bánh tortilla</p></div>
<div class="card">{xe()}<p class="cap">Xe giao hàng</p></div>
<div class="card">{bai_dang()}<p class="cap">Bài đăng mạng xã hội 4:5</p></div>
<div class="card">{bang_gia()}<p class="cap">Bảng giá đại lý – giá để trống</p></div>
<div class="g"><div class="card">{dt_a}<p class="cap">Danh thiếp – mặt trước</p></div><div class="card">{dt_b}<p class="cap">Danh thiếp – mặt sau</p></div></div></div></section>

<section class="s"><div class="num">Nguồn tham khảo</div><p class="src">Thông tin thị trường: <a href="https://torkifood.vn/cau-chuyen-thuong-hieu/">Torki Food – Câu chuyện thương hiệu</a> · <a href="https://bepos.io/blogs/nhuong-quyen-banh-mi/">18 thương hiệu nhượng quyền bánh mì 2024</a> · <a href="https://genk.vn/doner-kebab-va-banh-mi-viet-nam-cuoc-thu-hung-50-nam-tren-moi-via-he-2024110611490368.chn">Doner kebab và bánh mì Việt Nam</a> · Xu hướng bao bì 2026: <a href="https://www.liendesign.com/blog/packaging-design-trends-2026-fb-brands">Lien Design</a>, <a href="https://www.greatergood-brands.com/insights/packaging-design-trends-2026/">Greater Good</a>, <a href="https://www.vistaprint.com/hub/packaging-design-trends">Vistaprint</a>.</p></section>

<div class="end"><div style="max-width:520px;margin:0 auto">{G.logo_dung()}</div><p style="margin-top:12px">Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm · antamfoods.com · 0348.635.222</p></div>
<div class="lat">{lat(1600)}</div>
</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

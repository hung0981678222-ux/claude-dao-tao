"""Trang trình bày bộ nhận diện "Tem Đỏ". Chạy: python3 build_tem.py OUT.html"""
import base64
import os
import sys

import logo_tem as T

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
DO, DO2, TRANG, DEN, KRAFT, NGO, XAM = T.DO, T.DO2, T.TRANG, T.DEN, T.KRAFT, T.NGO, T.XAM


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = []
    for w in (700, 900):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Big Shoulders Display';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'big-shoulders-display', 'files', f'big-shoulders-display-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    for w in (400, 600, 800):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'be-vietnam-pro', 'files', f'be-vietnam-pro-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    return "\n".join(out)


def place(svg, x, y, w, h, extra=""):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" {extra}', 1)


def img(n, x, y, w, h):
    return f'<image href="{b64(f"{MH}/{n}.svg", "image/svg+xml")}" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def W(t, size, x, y, fill=DO, k="h", anchor="start", track=0.0):
    return T.text(t, size, k, x, y, fill, anchor, track)[0]


SH = '<defs><filter id="{i}"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#141414" flood-opacity=".25"/></filter></defs>'


def thung():
    """Thùng carton dán băng keo đỏ qua nắp, nhãn trên mặt bên."""
    tem = T.tem(); tin = tem[tem.index(">") + 1:tem.rindex("</svg>")]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 440" role="img" aria-label="Thùng carton dán băng keo An Tâm">{SH.format(i="ts")}
<g filter="url(#ts)"><path d="M70,160 L280,70 L490,160 L280,250 Z" fill="#D6B38A"/><path d="M70,160 L280,250 L280,400 L70,310 Z" fill="{KRAFT}"/><path d="M280,250 L490,160 L490,310 L280,400 Z" fill="#B88E63"/></g>
<path d="M175,115 L280,160 L385,205" stroke="#B88E63" stroke-width="2"/>
<g transform="matrix(.913 .43 -.913 .43 175 115) translate(0 -22)">{T.bang_keo_g(230, 44)}</g>
<g transform="matrix(1 .43 0 1 70 160) translate(105 0)"><rect x="-22" y="0" width="44" height="74" fill="{DO}"/><path d="M-22,74 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4 l4,-4 l4,4" fill="{DO}"/></g>
<g transform="matrix(1 -.43 0 1 280 250)"><g transform="translate(26 22) scale(.26)">{tin}</g>{W("BÁNH TORTILLA", 19, 122, 60, DEN)}{W("[Cần điền: số lượng]", 10, 122, 78, DEN, "s")}</g>
</svg>'''


def xe_may():
    """Thùng giao hàng trên xe máy."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 440" role="img" aria-label="Thùng giao hàng xe máy">
<rect width="640" height="440" fill="#E9E4DC"/><rect y="380" width="640" height="60" fill="#CFC8BD"/>
<rect x="250" y="70" width="260" height="210" rx="18" fill="{DO}"/><rect x="250" y="70" width="260" height="34" rx="18" fill="{DO2}"/><rect x="250" y="90" width="260" height="14" fill="{DO2}"/>
{place(T.tem(TRANG, DO, NGO), 286, 118, 104, 104)}{W("AN TÂM", 64, 398, 186, TRANG)}{W("GIAO TẬN BẾP", 15, 400, 210, TRANG, "s8", track=.18)}
{W("0348.635.222", 26, 380, 262, NGO, "h", "middle", .04)}
<path d="M120,300 Q160,250 250,280 L520,280 Q560,282 570,320 L580,340 L130,340 Z" fill="{DEN}"/>
<circle cx="170" cy="350" r="40" fill="{DEN}"/><circle cx="170" cy="350" r="16" fill="#888"/><circle cx="530" cy="350" r="40" fill="{DEN}"/><circle cx="530" cy="350" r="16" fill="#888"/>
<path d="M110,250 L150,240 L170,300" stroke="{DEN}" stroke-width="10" fill="none" stroke-linecap="round"/>
</svg>'''


def tui():
    tape = T.bang_keo(560, 40)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" role="img" aria-label="Túi bánh tortilla">{SH.format(i="us")}
<g filter="url(#us)"><path d="M70,70 L350,70 L368,492 L52,492 Z" fill="{TRANG}"/></g>
<path d="M70,70 L350,70 L349,86 L71,86 Z" fill="#E6E0D8"/>
<g transform="translate(58 60)">{T.bang_keo_g(304, 40)}</g>
{W("AN TÂM", 96, 210, 210, DO, "h", "middle")}{W("ẨM THỰC · SẢN PHẨM TẬN TÂM", 12, 210, 234, DEN, "s8", "middle", .24)}
{img("banh-tortillas", 110, 250, 200, 150)}
<rect x="52" y="410" width="316" height="82" fill="{DO}"/>{W("BÁNH TORTILLA", 40, 210, 456, TRANG, "h", "middle", .02)}{W("[Cần điền: số chiếc · khối lượng · HSD]", 11, 210, 478, "#FFD9D6", "s", "middle")}
{place(T.tem(), 290, 330, 96, 96, 'transform="rotate(10 338 378)" ')}
</svg>'''


def ao():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 440" role="img" aria-label="Áo đồng phục">
<rect width="480" height="440" fill="#EFEAE3"/>
<path d="M150,60 L200,40 Q240,70 280,40 L330,60 L420,120 L380,190 L340,170 L340,410 L140,410 L140,170 L100,190 L60,120 Z" fill="{DO}"/>
<path d="M200,40 Q240,70 280,40" fill="none" stroke="{DO2}" stroke-width="10"/>
{place(T.tem(TRANG, DO, NGO), 270, 110, 60, 60)}
{W("AN TÂM", 70, 240, 290, TRANG, "h", "middle")}{W("SẢN PHẨM TẬN TÂM", 14, 240, 316, TRANG, "s8", "middle", .24)}
</svg>'''


def bai_dang():
    tape = T.bang_keo(1100, 70)
    inner = tape[tape.index(">") + 1:tape.rindex("</svg>")]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 675" role="img" aria-label="Bài đăng mạng xã hội">
<rect width="540" height="675" fill="{DO}"/>
{W("DÁN TEM", 120, 40, 150, TRANG)}{W("LÀ AN TÂM", 120, 40, 262, NGO)}
<g transform="rotate(-8 270 320) translate(-200 292)">{T.bang_keo_g(1100, 64)}</g>
{img("doner-cuon", 250, 360, 250, 200)}
{place(T.tem(TRANG, DO, NGO), 50, 400, 170, 170)}
{W("Tortilla · Taco · Doner kebab giao tận bếp mỗi sáng", 17, 40, 616, TRANG, "s")}{W("0348.635.222", 30, 40, 652, NGO, "h", track=.04)}
</svg>'''


def danh_thiep():
    a = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt trước"><rect width="520" height="300" fill="{DO}"/>
{place(T.logo_ngang(TRANG, TRANG, None, DO), 40, 80, 440, 140)}</svg>'''
    tape = T.bang_keo(600, 30)
    b = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt sau"><rect width="520" height="300" fill="{TRANG}"/>
{W("[CẦN ĐIỀN: HỌ TÊN]", 40, 40, 86, DO)}{W("[Cần điền: Chức danh]", 15, 42, 114, DEN, "s")}
{W("0348.635.222", 16, 42, 176, DEN, "s8")}{W("antamfoods.com", 16, 42, 204, DEN, "s")}{W("[Cần điền: địa chỉ xưởng, TP.HCM]", 14, 42, 232, DEN, "s")}
{place(T.tem(), 380, 50, 110, 110)}<g transform="translate(0 270)">{T.bang_keo_g(520, 30)}</g></svg>'''
    return a, b


def bang_gia():
    rows = [("Bánh tortilla 8 inch", "[giá]"), ("Bánh tortilla 10 inch", "[giá]"), ("Vỏ taco", "[giá]"), ("Thịt doner (kg)", "[giá]"), ("Sốt doner", "[giá]")]
    r = ""
    for i, (n, p) in enumerate(rows):
        y = 238 + i * 54
        r += f'<rect x="36" y="{y - 32}" width="348" height="44" fill="{XAM if i % 2 == 0 else TRANG}"/>' + W(n, 16, 50, y - 4, DEN, "s") + W(p, 24, 370, y - 2, DO, "h", "end")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 560" role="img" aria-label="Bảng giá đại lý"><rect width="420" height="560" fill="{TRANG}"/>
<rect width="420" height="160" fill="{DO}"/>{W("BẢNG GIÁ", 78, 36, 96, TRANG)}{W("ĐẠI LÝ", 40, 38, 138, NGO)}{place(T.tem(TRANG, DO, NGO), 290, 30, 100, 100)}
{W("Áp dụng từ [Cần điền: ngày] · Giá chưa gồm VAT", 12, 36, 190, DEN, "s")}{r}
{W("ĐẶT HÀNG: 0348.635.222", 26, 210, 528, DO, "h", "middle", .04)}</svg>'''


CSS = """
:root{--do:#E1251B;--do2:#A3150F;--den:#141414;--xam:#F3EEE7;--ngo:#FFC531}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--xam);color:var(--den);font:16px/1.6 'Be Vietnam Pro',system-ui,sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
.h{font-family:'Big Shoulders Display',sans-serif;font-weight:900;text-transform:uppercase;letter-spacing:.005em}
.hero{background:var(--do);color:#fff;overflow:hidden}
.hero .in{max-width:1200px;margin:0 auto;padding:64px 20px 40px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:36px;align-items:center}
.k{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--ngo)}
.hero h1{font-size:clamp(72px,11vw,170px);line-height:.95;margin:12px 0 18px}
.hero p{max-width:560px;font-size:17px;color:#FFE1DE}
.tape{transform:rotate(-2deg);margin:-14px -20px 0}
section.s{max-width:1200px;margin:0 auto;padding:72px 20px 8px}
.num{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--do)}
.s h2{font-size:clamp(48px,6vw,84px);line-height:1;color:var(--do);margin:8px 0 12px}
.s .lead{max-width:720px;margin:0 0 28px;font-size:17px}
.g{display:grid;gap:18px;align-items:start}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:#fff;padding:24px;border-radius:6px}
.card.d{background:var(--do);color:#fff}.card.k2{background:var(--den);color:#fff}
.card h3{font-family:'Big Shoulders Display';font-weight:900;font-size:34px;line-height:1;text-transform:uppercase;color:var(--do);margin-bottom:8px}
.card.d h3,.card.k2 h3{color:var(--ngo)}
.cap{font-size:14px;margin-top:10px;color:#6A625A}.card.d .cap,.card.k2 .cap{color:#FFD9D6}
.sw{background:#fff;border-radius:6px;overflow:hidden}.sw div{height:120px}.sw p{padding:12px 14px;font-size:13px;line-height:1.45}
.sw b{font-family:'Big Shoulders Display';font-weight:900;font-size:24px;display:block;text-transform:uppercase;color:var(--do)}
.big{font-family:'Big Shoulders Display';font-weight:900;font-size:clamp(64px,9vw,128px);line-height:.9;color:var(--do);text-transform:uppercase}
.src{font-size:13px;color:#6A625A}.src a{color:var(--do)}
.end{text-align:center;padding:72px 20px 90px}
@media (max-width:860px){.hero .in,.g2,.g3{grid-template-columns:minmax(0,1fr)}.s{padding-top:52px}}
"""


def page():
    dt_a, dt_b = danh_thiep()
    sw = [("Đỏ tem", "#E1251B", "Màu chủ đạo – tem, băng keo, chữ"), ("Đỏ đậm", "#A3150F", "Bóng, nền sâu"), ("Đen", "#141414", "Chữ thân, chi tiết"),
          ("Trắng", "#FFFFFF", "Chữ trên nền đỏ, bao bì"), ("Kraft", "#C9A27A", "Thùng carton, túi giấy"), ("Vàng tích", "#FFC531", "Dấu tích – chỉ một điểm")]
    sws = "".join(f'<div class="sw"><div style="background:{h};{"border-bottom:1px solid #eee" if h == "#FFFFFF" else ""}"></div><p><b>{n}</b>{h} · {u}</p></div>' for n, h, u in sw)
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tem Đỏ An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Bộ nhận diện mới · Đỏ chủ đạo</div><h1 class="h">Dán tem<br>là an tâm</h1>
<p>Với khách doanh nghiệp, an tâm là khi thùng bánh đến đúng giờ, còn nguyên niêm phong. Bộ nhận diện mới biến điều đó thành hình ảnh: tem tròn răng cưa đỏ có dấu tích, và cuộn băng keo đỏ in chữ AN TÂM dán trên mọi thùng hàng rời xưởng. Nhìn thấy băng đỏ là biết hàng An Tâm.</p></div>
<div>{T.tem(TRANG, DO, NGO)}</div></div><div class="tape">{T.bang_keo(1700, 60)}</div></header>

<section class="s"><div class="num">01 · Ý tưởng</div><h2 class="h">Một con tem, một cuộn băng</h2><p class="lead">Không cần hình que thịt quay hay chiếc bánh như mọi thương hiệu khác. An Tâm sở hữu một vật rất đời thường mà ai trong ngành cũng gặp mỗi ngày: <b>băng keo niêm phong</b>.</p>
<div class="g g3"><div class="card d"><h3>Tem tròn răng cưa</h3><p>Hình con tem chất lượng, giữa là chữ AN TÂM và dấu tích vàng – "đã sẵn sàng, cứ yên tâm".</p></div>
<div class="card k2"><h3>Băng keo đỏ</h3><p>Chữ AN TÂM lặp lại trên cuộn băng: dán thùng, làm viền ấn phẩm, chạy chéo trên bài đăng. Nhìn từ xa đã nhận ra.</p></div>
<div class="card"><h3>Chữ thùng hàng</h3><p>Big Shoulders Display: chữ nén, đậm, kiểu chữ in trên thùng hàng và kho xưởng – mạnh, thẳng thắn, đáng tin.</p></div></div></section>

<section class="s"><div class="num">02 · Logo</div><h2 class="h">Logo và phiên bản</h2><p class="lead">Bản ngang cho biển hiệu, xe, website; bản đứng cho bao bì; tem dùng riêng làm nhãn niêm phong, ảnh đại diện, dập nổi.</p>
<div class="g g2"><div class="card">{T.logo_ngang()}<p class="cap">Bản ngang</p></div><div class="card d">{T.logo_ngang(TRANG, TRANG, None, DO)}<p class="cap">Bản ngang – nền đỏ</p></div>
<div class="card">{T.logo_dung()}<p class="cap">Bản đứng</p></div>
<div class="g g2"><div class="card">{T.tem()}<p class="cap">Tem đỏ</p></div><div class="card">{T.tem(DEN)}<p class="cap">Tem đen – in một màu</p></div></div></div></section>

<section class="s"><div class="num">03 · Màu</div><h2 class="h">Đỏ tem, trắng, đen</h2><p class="lead">Đỏ tem tươi, rực để nổi bật trên kệ và trên đường. Kraft là màu của thùng hàng. Vàng chỉ dùng cho dấu tích.</p><div class="g g3">{sws}</div></section>

<section class="s"><div class="num">04 · Chữ</div><h2 class="h">Chữ thùng hàng</h2><p class="lead">Tiêu đề: Big Shoulders Display Black, in hoa. Nội dung: Be Vietnam Pro. Cả hai là font mã nguồn mở SIL OFL, đủ dấu tiếng Việt.</p>
<div class="card"><div class="big">Bánh mới mỗi sáng, giao tận bếp</div><p style="margin-top:14px;font-size:18px">Be Vietnam Pro: Bánh tortilla mềm dẻo, vỏ taco giòn và thịt doner tẩm ướp sẵn cho quán ăn, nhà hàng và chuỗi cửa hàng tại TP.HCM. Báo giá đại lý: [giá].</p></div></section>

<section class="s"><div class="num">05 · Ứng dụng</div><h2 class="h">Băng đỏ đi khắp nơi</h2><p class="lead">Chỗ trong ngoặc vuông là thông tin cần điền thật trước khi in.</p>
<div class="g g2"><div class="card">{thung()}<p class="cap">Thùng carton dán băng keo An Tâm</p></div>
<div class="card">{xe_may()}<p class="cap">Thùng giao hàng xe máy</p></div>
<div class="card">{tui()}<p class="cap">Túi bánh tortilla – miệng túi dán băng niêm phong</p></div>
<div class="card">{bai_dang()}<p class="cap">Bài đăng mạng xã hội 4:5</p></div>
<div class="card">{ao()}<p class="cap">Áo đồng phục giao hàng</p></div>
<div class="card">{bang_gia()}<p class="cap">Bảng giá đại lý – giá để trống</p></div>
<div class="card">{dt_a}<p class="cap">Danh thiếp – mặt trước</p></div><div class="card">{dt_b}<p class="cap">Danh thiếp – mặt sau</p></div></div></section>

<div class="end"><div style="max-width:620px;margin:0 auto">{T.logo_ngang()}</div></div>
<div class="tape" style="margin-bottom:-6px">{T.bang_keo(1700, 60)}</div>
</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

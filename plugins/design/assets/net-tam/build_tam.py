"""Trang trình bày bộ nhận diện "Nét Tâm" (thư pháp chữ Việt, đỏ son chủ đạo). Chạy: python3 build_tam.py OUT.html"""
import base64
import os
import sys

import logo_tam as T

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
DO, DO2, MUC, GIAY, VANG, KEM = T.DO, T.DO2, T.MUC, T.GIAY, T.VANG, T.KEM


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = []
    for w in (400, 700):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Charm';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'charm', 'files', f'charm-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    for w in (400, 600, 800):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'be-vietnam-pro', 'files', f'be-vietnam-pro-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    return "\n".join(out)


def place(svg, x, y, w, h):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


def img(n, x, y, w, h):
    return f'<image href="{b64(f"{MH}/{n}.svg", "image/svg+xml")}" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def W(t, size, x, y, fill=DO, k="brush", anchor="start", track=0.0):
    return T.text(t, size, k, x, y, fill, anchor, track)[0]


def ink(uid, body, rough=2.2, dry=True):
    return T.defs(uid, rough, dry) + f'<g filter="url(#{uid})">{body}</g>'


# ---------- hoạ tiết ----------
def nen_giay(w, h, bg=GIAY, fg=DO, uid="ng"):
    """Nền giấy dó rải vòng nét bút nhỏ và con dấu."""
    import random
    r = random.Random(6); b = ""
    for j, y in enumerate(range(60, h + 120, 130)):
        for x in range(-40 + (70 if j % 2 else 0), w + 140, 140):
            if r.random() < .7:
                b += T.enso(x, y, r.choice([34, 46, 58]), 10, fg, seed=r.randint(0, 99), start=r.randint(-180, 180))
                if r.random() < .4:
                    b += f'<rect x="{x - 9}" y="{y - 9}" width="18" height="18" fill="{fg}" transform="rotate({r.randint(-12, 12)} {x} {y})"/>'
            else:
                b += f'<rect x="{x - 12}" y="{y - 12}" width="24" height="24" fill="{fg}" transform="rotate({r.randint(-12, 12)} {x} {y})"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Nền giấy dó"><rect width="{w}" height="{h}" fill="{bg}"/>{ink(uid, b, 1.8)}</svg>'


# ---------- ứng dụng ----------
def cau_doi():
    """Mặt tiền: đôi câu đối là khẩu hiệu, giữa là biển hiệu."""
    def doc(words, x):
        s = f'<rect x="{x}" y="70" width="110" height="440" fill="{DO}"/><rect x="{x + 8}" y="78" width="94" height="424" fill="none" stroke="{VANG}" stroke-width="2"/>'
        for i, wd in enumerate(words):
            s += W(wd, 46, x + 55, 150 + i * 100, KEM, anchor="middle")
        return s
    left = doc(["Sản", "Phẩm", "Tận", "Tâm"], 70); right = doc(["Phát", "Triển", "Xứng", "Tầm"], 540)
    sign = f'<rect x="210" y="70" width="300" height="130" fill="{DO2}"/>' + place(T.logo_ngang("cdn", KEM, KEM, None, DO2), 222, 82, 276, 106)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 560" role="img" aria-label="Mặt tiền với câu đối">
<rect width="720" height="560" fill="#EFE3CF"/><rect y="510" width="720" height="50" fill="#D8C7AA"/>
<rect x="200" y="220" width="320" height="290" fill="#5A3B2A"/><rect x="214" y="234" width="292" height="276" fill="#F7EAD3"/>
{img("doner-cuon", 250, 300, 110, 110)}{img("taco", 360, 330, 130, 100)}
<rect x="214" y="430" width="292" height="80" fill="#E7D3B4"/>
{T.defs("cdi")}<g filter="url(#cdi)">{left}{right}</g>{sign}
</svg>'''


def tui():
    e = ink("tue", T.enso(210, 250, 120, 28, KEM) + W("Tâm", 120, 210, 290, KEM, anchor="middle"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" role="img" aria-label="Túi giấy đỏ">
<defs><filter id="tsh"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#1E1412" flood-opacity=".28"/></filter></defs>
<path d="M150,90 C150,30 270,30 270,90" fill="none" stroke="{DO2}" stroke-width="10"/>
<g filter="url(#tsh)"><path d="M60,90 L360,90 L376,490 L44,490 Z" fill="{DO}"/></g>
{e}{T.defs("tus", 1.4, False)}{T.seal(286, 330, 50, KEM, DO, uid="tus")}
{W("ẨM THỰC AN TÂM", 16, 210, 432, KEM, "sans-b", "middle", .3)}
{W("antamfoods.com · 0348.635.222", 13, 210, 458, "#F6C9CF", "sans", "middle", .04)}
</svg>'''


def hop():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 400" role="img" aria-label="Hộp bánh có đai giấy">
<defs><filter id="hsh"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#1E1412" flood-opacity=".25"/></filter></defs>
<g filter="url(#hsh)"><path d="M60,150 L260,62 L460,150 L260,238 Z" fill="{KEM}"/><path d="M60,150 L260,238 L260,368 L60,280 Z" fill="#EADBC3"/><path d="M260,238 L460,150 L460,280 L260,368 Z" fill="#DCC9AC"/></g>
<path d="M150,110 L350,198 L350,328 L150,240 Z" fill="{DO}"/><path d="M150,110 L230,75 L430,163 L350,198 Z" fill="{DO2}"/>
<g transform="matrix(.88 .39 0 1 160 150)">{ink("hpi", W("An Tâm", 46, 10, 50, KEM))}{W("BÁNH TORTILLA", 11, 14, 74, KEM, "sans-b", track=.3)}</g>
<g transform="translate(300 98) rotate(-8)">{T.defs("hps", 1.4, False)}{T.seal(0, 0, 54, DO, KEM, uid="hps")}</g>
</svg>'''


def bai_dang():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 675" role="img" aria-label="Bài đăng mạng xã hội">
<rect width="540" height="675" fill="{DO}"/>
{ink("bde", T.enso(270, 330, 190, 34, "#E23B4E", seed=9))}
{ink("bdt", W("Bánh nóng", 78, 270, 150, KEM, anchor="middle") + W("làm từ tâm", 78, 270, 236, KEM, anchor="middle"))}
{img("banh-tortillas", 140, 270, 260, 200)}
{W("Tortilla · Taco · Doner kebab giao tận bếp", 19, 270, 540, KEM, "sans", "middle", .02)}
<rect x="160" y="566" width="220" height="48" fill="{KEM}"/>{W("0348.635.222", 24, 270, 599, DO, "sans-b", "middle", .04)}
{T.defs("bds", 1.4, False)}{T.seal(452, 600, 54, KEM, DO, uid="bds")}
</svg>'''


def danh_thiep():
    a = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt trước"><rect width="520" height="300" fill="{DO}"/>
{place(T.logo_ngang("dta", KEM, KEM, None, DO), 40, 70, 440, 160)}</svg>'''
    b = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt sau"><rect width="520" height="300" fill="{GIAY}"/>
{ink("dtb", W("[Cần điền: Họ tên]", 38, 44, 92, DO))}{W("[Cần điền: Chức danh]", 15, 46, 122, MUC, "sans")}
{W("0348.635.222", 16, 46, 190, MUC, "sans-b")}{W("antamfoods.com", 16, 46, 218, MUC, "sans")}{W("[Cần điền: địa chỉ xưởng, TP.HCM]", 14, 46, 246, MUC, "sans")}
{T.defs("dts", 1.4, False)}{T.seal(392, 60, 84, DO, KEM, uid="dts")}<rect x="0" y="288" width="520" height="12" fill="{DO}"/></svg>'''
    return a, b


def bang_gia():
    rows = [("Bánh tortilla 8 inch", "[giá]"), ("Bánh tortilla 10 inch", "[giá]"), ("Vỏ taco", "[giá]"), ("Thịt doner (kg)", "[giá]"), ("Sốt doner", "[giá]")]
    r = ""
    for i, (n, p) in enumerate(rows):
        y = 236 + i * 54
        r += f'<path d="M40,{y + 14} H380" stroke="#E6D6BE" stroke-width="1.5"/>' + W(n, 17, 42, y, MUC, "sans") + W(p, 17, 378, y, DO, "sans-b", "end")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 560" role="img" aria-label="Bảng giá đại lý"><rect width="420" height="560" fill="{GIAY}"/>
<rect width="420" height="160" fill="{DO}"/>{ink("bgt", W("Bảng giá", 58, 40, 92, KEM) + W("đại lý", 40, 44, 136, "#F6C9CF"))}
{T.defs("bgs", 1.4, False)}{T.seal(306, 40, 76, KEM, DO, uid="bgs")}
{W("Áp dụng từ [Cần điền: ngày] · Giá chưa gồm VAT", 12, 40, 192, MUC, "sans")}{r}
{W("Đặt hàng: 0348.635.222 · antamfoods.com", 13, 210, 524, DO, "sans-b", "middle")}</svg>'''


CSS = """
:root{--do:#C8102E;--do2:#8E0B20;--muc:#1E1412;--giay:#FBF4EA;--vang:#D4A04C;--kem:#FFF8EE}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--giay);color:var(--muc);font:16px/1.65 'Be Vietnam Pro',system-ui,sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
.br{font-family:'Charm',serif;font-weight:700}
.hero{background:var(--do);color:var(--kem);position:relative;overflow:hidden}
.hero .in{max-width:1200px;margin:0 auto;padding:64px 20px 60px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px;align-items:center}
.k{font-weight:800;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--vang)}
.hero h1{font-family:'Charm';font-weight:700;font-size:clamp(56px,8vw,118px);line-height:1.02;margin:10px 0 18px}
.hero p{max-width:560px;font-size:17px;color:#FCE3E6}
.rule{height:10px;background:var(--do2);border-bottom:3px solid var(--vang)}
section.s{max-width:1200px;margin:0 auto;padding:72px 20px 8px}
.num{font-weight:800;font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--do)}
.s h2{font-family:'Charm';font-weight:700;font-size:clamp(40px,5vw,64px);line-height:1.05;color:var(--do);margin:4px 0 10px}
.s .lead{max-width:720px;margin:0 0 28px;font-size:17px}
.g{display:grid;gap:18px;align-items:start}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:#fff;padding:24px;border:1px solid #EADCC6}
.card.d{background:var(--do);color:var(--kem);border-color:var(--do)}
.card h3{font-family:'Charm';font-weight:700;font-size:30px;line-height:1.1;color:var(--do);margin-bottom:6px}.card.d h3{color:var(--kem)}
.cap{font-size:14px;margin-top:10px;color:#6B5A50}.card.d .cap{color:#F6C9CF}
.sw{background:#fff;border:1px solid #EADCC6}.sw div{height:120px}.sw p{padding:12px 14px;font-size:13px;line-height:1.45}.sw b{font-family:'Charm';font-size:24px;display:block;color:var(--do);line-height:1.1}
.big{font-family:'Charm';font-weight:700;font-size:clamp(52px,7vw,96px);line-height:1.05;color:var(--do)}
.src{font-size:13px;color:#6B5A50}.src a{color:var(--do)}
.end{text-align:center;padding:72px 20px 90px}
@media (max-width:860px){.hero .in,.g2,.g3{grid-template-columns:minmax(0,1fr)}.s{padding-top:52px}}
"""


def page():
    dt_a, dt_b = danh_thiep()
    sw = [("Đỏ son", "#C8102E", "Màu chủ đạo – nền, chữ, con dấu"), ("Đỏ thẫm", "#8E0B20", "Nền sâu, biển hiệu"), ("Mực", "#1E1412", "Chữ thân, nét phụ"),
          ("Giấy dó", "#FBF4EA", "Nền giấy, bao bì"), ("Vàng kim", "#D4A04C", "Viền câu đối, chi tiết nhỏ"), ("Kem", "#FFF8EE", "Chữ trên nền đỏ")]
    sws = "".join(f'<div class="sw"><div style="background:{h}"></div><p><b>{n}</b>{h} · {u}</p></div>' for n, h, u in sw)
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nét Tâm An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Bộ nhận diện mới · Đỏ son chủ đạo</div><h1>Nét Tâm</h1>
<p>Chữ "Tâm" là chữ được viết thư pháp nhiều nhất trong nhà người Việt. Bộ nhận diện mới lấy chính tinh thần ấy: chữ An Tâm viết bút lông, một vòng tròn một nét như chiếc bánh tròn trọn vẹn, và con dấu son đóng như lời cam kết. Câu "Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm" trở thành đôi câu đối của thương hiệu.</p></div>
<div style="background:var(--kem);padding:28px">{T.logo("hl")}</div></div></header><div class="rule"></div>

<section class="s"><div class="num">01 · Ý tưởng</div><h2>Ba nét làm nên thương hiệu</h2><p class="lead">Màu đỏ son giữ đúng mong muốn và quen mắt với khách Việt. Để không lẫn với các thương hiệu đỏ – cam trong ngành kebab, An Tâm khác biệt bằng <b>nét chữ</b> chứ không bằng màu: thư pháp chữ Việt, thứ không đối thủ nào dùng.</p>
<div class="g g3"><div class="card"><h3>Chữ bút lông</h3><p>"An Tâm" viết bằng nét bút lông có mép xơ như mực thấm giấy dó – ấm, thủ công, có người làm thật phía sau.</p></div>
<div class="card"><h3>Vòng tròn một nét</h3><p>Một nét bút khép gần trọn vòng: chiếc bánh tròn, sự trọn vẹn, và chừa một khe nhỏ cho sự "phát triển".</p></div>
<div class="card"><h3>Con dấu son</h3><p>Như triện đóng dưới bức thư pháp, như con dấu đỏ trên giấy tờ – lời cam kết chất lượng gửi tới khách hàng doanh nghiệp.</p></div></div></section>

<section class="s"><div class="num">02 · Logo</div><h2>Logo và phiên bản</h2><p class="lead">Bản chính vuông cho bao bì, ảnh đại diện; bản ngang cho biển hiệu, xe, website; biểu tượng chữ Tâm trong vòng tròn cho tem, dập nổi, biểu tượng ứng dụng.</p>
<div class="g g3"><div class="card">{T.logo("l1")}<p class="cap">Bản chính – nền giấy</p></div><div class="card d">{T.logo("l2", KEM, KEM, KEM, KEM, DO)}<p class="cap">Bản chính – nền đỏ son</p></div>
<div class="g"><div class="card">{T.bieu_tuong("l3")}<p class="cap">Biểu tượng</p></div><div class="card d">{T.bieu_tuong("l4", KEM, DO)}<p class="cap">Biểu tượng nền đỏ</p></div></div></div>
<div class="g g2" style="margin-top:18px"><div class="card">{T.logo_ngang("l5")}<p class="cap">Bản ngang</p></div><div class="card d">{T.logo_ngang("l6", KEM, KEM, None, DO)}<p class="cap">Bản ngang – nền đỏ</p></div></div></section>

<section class="s"><div class="num">03 · Màu</div><h2>Đỏ son và giấy dó</h2><p class="lead">Đỏ son chiếm phần lớn diện tích; giấy dó làm nền nghỉ mắt; vàng kim chỉ dùng cho viền mảnh và chi tiết nhỏ.</p><div class="g g3">{sws}</div></section>

<section class="s"><div class="num">04 · Chữ</div><h2>Bút lông và chữ in</h2><p class="lead">Tiêu đề, khẩu hiệu dùng Charm – nét bút lông có thanh đậm thanh mảnh, đủ dấu tiếng Việt. Nội dung, bảng giá dùng Be Vietnam Pro cho rõ ràng. Cả hai là font mã nguồn mở SIL OFL.</p>
<div class="card"><div class="big">Bánh ngon làm từ tâm</div><p style="margin-top:12px;font-size:18px">Be Vietnam Pro: Bánh tortilla mềm dẻo, vỏ taco giòn và thịt doner tẩm ướp sẵn cho quán ăn, nhà hàng và chuỗi cửa hàng tại TP.HCM. Báo giá đại lý: [giá].</p></div></section>

<section class="s"><div class="num">05 · Hoạ tiết</div><h2>Giấy dó, nét bút, con dấu</h2><p class="lead">Nền giấy dó rải vòng nét bút và dấu son dùng cho giấy gói, nền mạng xã hội, lót khay.</p>
<div class="card" style="padding:0">{nen_giay(1200, 360)}</div></section>

<section class="s"><div class="num">06 · Ứng dụng</div><h2>Từ xưởng tới quầy</h2><p class="lead">Chỗ trong ngoặc vuông là thông tin cần điền thật trước khi in.</p>
<div class="g g2"><div class="card">{cau_doi()}<p class="cap">Mặt tiền: đôi câu đối chính là khẩu hiệu "Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm"</p></div>
<div class="card">{tui()}<p class="cap">Túi giấy đỏ</p></div>
<div class="card">{hop()}<p class="cap">Hộp bánh có đai giấy đỏ và con dấu niêm phong</p></div>
<div class="card">{bai_dang()}<p class="cap">Bài đăng mạng xã hội 4:5</p></div>
<div class="card">{bang_gia()}<p class="cap">Bảng giá đại lý – giá để trống</p></div>
<div class="g"><div class="card">{dt_a}<p class="cap">Danh thiếp – mặt trước</p></div><div class="card">{dt_b}<p class="cap">Danh thiếp – mặt sau</p></div></div></div></section>

<section class="s"><div class="num">Nguồn tham khảo</div><p class="src">Thị trường: <a href="https://torkifood.vn/cau-chuyen-thuong-hieu/">Torki Food – Câu chuyện thương hiệu</a> · <a href="https://bepos.io/blogs/nhuong-quyen-banh-mi/">18 thương hiệu nhượng quyền bánh mì 2024</a> · Xu hướng bao bì 2026: <a href="https://www.liendesign.com/blog/packaging-design-trends-2026-fb-brands">Lien Design</a>, <a href="https://www.greatergood-brands.com/insights/packaging-design-trends-2026/">Greater Good</a>.</p></section>
<div class="end"><div style="max-width:360px;margin:0 auto">{T.logo("le")}</div></div><div class="rule"></div>
</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

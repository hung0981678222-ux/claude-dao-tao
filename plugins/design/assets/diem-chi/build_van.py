"""Trang bộ nhận diện "Điểm Chỉ" mở rộng, có font thương hiệu An Tâm Vân. Chạy: python3 build_van.py OUT.html"""
import base64
import math
import os
import sys

import logo_van as V

# Font đã chọn: phương án 04 Tròn Bánh – Chấm Vân, dấu mũ vân tay thấp
V.F["xb"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts-tron", "AnTamTronChamNgan.ttf")
V.F["md"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts-tron", "AnTamTronChamNganVua.ttf")
V._f.cache_clear()

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
DO, DO2, SON, KEM, GIAY, MUC, NGO = V.DO, V.DO2, V.SON, V.KEM, V.GIAY, V.MUC, V.NGO


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    return "\n".join(f"@font-face{{font-family:'An Tam Van';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'fonts-tron', f'AnTamTron{n}.woff2'), 'font/woff2')}) format('woff2')}}" for n, w in (("ChamNgan", 800), ("ChamNganVua", 500)))


def place(svg, x, y, w, h):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


def img(n, x, y, w, h):
    return f'<image href="{b64(f"{MH}/{n}.svg", "image/svg+xml")}" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def W(t, size, x, y, fill=DO, k="xb", anchor="start", track=0.0):
    return V.text(t, size, k, x, y, fill, anchor, track)[0]


def nen_van(w, h, bg=DO, fg="#E84A42", uid=0):
    """Nền đường vân chảy: các đường cong song song lượn sóng, như phóng to một góc vân tay."""
    s = f'<rect width="{w}" height="{h}" fill="{bg}"/>'
    for i in range(-6, int(h / 14) + 10):
        y0 = i * 14
        pts = []
        for x in range(-20, w + 30, 20):
            y = y0 + 60 * math.sin(x / 260 + i * .05) + 30 * math.sin(x / 90 + i * .12)
            pts.append((x, y))
        s += f'<path d="M' + " L".join(f"{x},{y:.1f}" for x, y in pts) + f'" fill="none" stroke="{fg}" stroke-width="4.5" stroke-linecap="round"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Nền đường vân">{s}</svg>'


SH = '<defs><filter id="{i}"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#231716" flood-opacity=".22"/></filter></defs>'


def phieu():
    rows = [("Bánh tortilla 10 inch", "[sl]"), ("Vỏ taco", "[sl]"), ("Thịt doner (kg)", "[sl]"), ("Sốt doner", "[sl]")]
    r = ""
    for i, (a, b) in enumerate(rows):
        y = 188 + i * 36
        r += f'<path d="M50,{y + 12} H470" stroke="#EADFCD"/>' + W(a, 15, 50, y, MUC, "md") + W(b, 15, 470, y, DO, "xb", "end")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 440" role="img" aria-label="Phiếu giao hàng có điểm chỉ">{SH.format(i="ps")}
<rect width="520" height="440" fill="#EFE5D6"/><g filter="url(#ps)"><rect x="24" y="24" width="472" height="392" fill="#fff"/></g>
{place(V.logo_ngang(), 46, 40, 220, 70)}{W("PHIẾU GIAO HÀNG", 18, 470, 74, MUC, "xb", "end", .08)}{W("Số [Cần điền] · [Ngày]", 12, 470, 94, MUC, "md", "end")}
<rect x="24" y="122" width="472" height="4" fill="{DO}"/>{W("Khách: [Cần điền: tên quán]", 13, 50, 152, MUC, "md")}{r}
{W("Người làm bánh", 12, 120, 392, MUC, "md", "middle")}<g opacity=".92">{V.van_tay(120, 346, 26, SON, seed=11, rings=9)}</g>
{W("Người nhận", 12, 400, 392, MUC, "md", "middle")}<path d="M340,370 H460" stroke="#cbbba5" stroke-dasharray="4 4"/>
</svg>'''


def the_tho():
    """Thẻ treo trên túi: người làm mẻ bánh hôm nay."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 440" role="img" aria-label="Thẻ người làm bánh">{SH.format(i="ts")}
<rect width="520" height="440" fill="{GIAY}"/><path d="M260,20 V70" stroke="{MUC}" stroke-width="2"/>
<g filter="url(#ts)"><path d="M140,70 H380 V400 H140 Z" fill="{DO}"/></g><circle cx="260" cy="96" r="10" fill="{GIAY}"/>
{W("MẺ BÁNH HÔM NAY", 14, 260, 140, KEM, "xb", "middle", .24)}
<circle cx="260" cy="226" r="70" fill="{KEM}"/>{V.van_tay(260, 226, 52, DO, seed=21, rings=10)}
{W("Người làm:", 13, 260, 330, "#FFD6D3", "md", "middle")}{W("[Cần điền: tên]", 22, 260, 358, KEM, "xb", "middle")}
{W("Mẻ số [ ] · [ngày]", 12, 260, 384, "#FFD6D3", "md", "middle")}
</svg>'''


def tui():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" role="img" aria-label="Túi bánh tortilla">{SH.format(i="us")}
<g filter="url(#us)"><path d="M70,70 L350,70 L368,492 L52,492 Z" fill="{KEM}"/></g><path d="M70,70 L350,70 L349,92 L71,92 Z" fill="{DO}"/>
{place(V.logo_dung(), 120, 104, 180, 150)}{img("banh-tortillas", 120, 262, 180, 136)}
<rect x="52" y="410" width="316" height="82" fill="{DO}"/>{W("Bánh Tortilla", 34, 210, 452, KEM, "xb", "middle")}{W("[Cần điền: số chiếc · khối lượng · HSD]", 11, 210, 476, "#FFD6D3", "md", "middle")}
<g transform="rotate(-14 330 380)"><circle cx="330" cy="380" r="40" fill="{KEM}" stroke="{DO}" stroke-width="3"/>{V.van_tay(330, 380, 26, SON, seed=31, rings=8)}</g>
</svg>'''


def bai_dang():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 675" role="img" aria-label="Bài đăng mạng xã hội">
{place(nen_van(540, 675), 0, 0, 540, 675)}
<rect x="40" y="40" width="460" height="595" fill="{KEM}"/>
{W("Mỗi mẻ bánh", 56, 270, 130, DO, "xb", "middle", -.02)}{W("một lời cam kết", 56, 270, 196, DO, "xb", "middle", -.02)}
{V.van_tay(270, 360, 110, SON, seed=41)}
{W("Tortilla · Taco · Doner kebab giao tận bếp", 18, 270, 548, MUC, "md", "middle")}{W("0348.635.222", 30, 270, 594, DO, "xb", "middle", .02)}
</svg>'''


def danh_thiep():
    a = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt trước">{place(nen_van(520, 300), 0, 0, 520, 300)}
<rect x="40" y="40" width="440" height="220" fill="{DO}"/>{place(V.logo_ngang(KEM, KEM), 56, 70, 408, 160)}</svg>'''
    b = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt sau"><rect width="520" height="300" fill="{KEM}"/>
{W("[Cần điền: Họ tên]", 30, 44, 88, DO)}{W("[Cần điền: Chức danh]", 15, 44, 116, MUC, "md")}
{W("0348.635.222", 16, 44, 182, MUC, "xb")}{W("antamfoods.com", 16, 44, 210, MUC, "md")}{W("[Cần điền: địa chỉ xưởng, TP.HCM]", 14, 44, 238, MUC, "md")}
{V.van_tay(420, 150, 62, SON, seed=51)}</svg>'''
    return a, b


def xe():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 380" role="img" aria-label="Xe giao hàng">
<rect width="720" height="380" fill="#EFE7DB"/><rect y="318" width="720" height="62" fill="#D7CBB8"/>
<path d="M60,90 H470 V300 H60 Z" fill="{DO}"/><path d="M470,150 H580 L650,210 V300 H470 Z" fill="{KEM}"/><path d="M490,165 H572 L622,212 H490 Z" fill="#BFD8E4"/>
{place(V.logo_ngang(KEM, KEM), 80, 110, 330, 110)}{W("Giao bánh tận bếp · 0348.635.222", 17, 84, 262, KEM, "md")}
<g opacity=".35">{V.van_tay(420, 150, 90, KEM, seed=61)}</g>
<circle cx="160" cy="310" r="36" fill="{MUC}"/><circle cx="160" cy="310" r="14" fill="#888"/><circle cx="560" cy="310" r="36" fill="{MUC}"/><circle cx="560" cy="310" r="14" fill="#888"/>
</svg>'''


CSS = """
:root{--do:#D2141E;--do2:#8F0D14;--son:#E2332B;--kem:#FFF6EA;--giay:#F6EEE2;--muc:#231716;--ngo:#F5B82E}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--giay);color:var(--muc);font:500 16px/1.6 'An Tam Van',system-ui,sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
.hero{background:var(--do);color:var(--kem);position:relative;overflow:hidden}
.hero .bg{position:absolute;inset:0;opacity:.5}.hero .bg svg{width:100%;height:100%}
.hero .in{position:relative;max-width:1200px;margin:0 auto;padding:68px 20px 60px;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:40px;align-items:center}
.k{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--ngo)}
.hero h1{font-weight:800;font-size:clamp(48px,7vw,104px);line-height:1.04;letter-spacing:-.02em;margin:12px 0 18px}
.hero p{max-width:560px;font-size:17px;color:#FFE1DE}
.hero .card{background:var(--kem);padding:28px;border-radius:6px}
section.s{max-width:1200px;margin:0 auto;padding:72px 20px 8px}
.num{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--do)}
.s h2{font-weight:800;font-size:clamp(34px,4.6vw,60px);line-height:1.06;letter-spacing:-.02em;color:var(--do);margin:8px 0 12px}
.s .lead{max-width:720px;margin:0 0 28px;font-size:17px}
.g{display:grid;gap:18px;align-items:start}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:#fff;padding:24px;border-radius:6px}.card.d{background:var(--do);color:var(--kem)}
.card h3{font-weight:800;font-size:24px;color:var(--do);margin-bottom:6px}.card.d h3{color:var(--ngo)}
.cap{font-size:14px;margin-top:10px;color:#6b5a55}.card.d .cap{color:#FFD6D3}
.big{font-weight:800;font-size:clamp(60px,9vw,128px);line-height:1.1;letter-spacing:-.03em;color:var(--do);overflow-wrap:anywhere}
.mid{font-weight:500;font-size:clamp(22px,2.6vw,30px);line-height:1.4}
.tester{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0 6px}
.tester input{flex:1;min-width:0;font:500 18px 'An Tam Van';padding:10px 14px;border:2px solid var(--do);border-radius:999px;background:#fff;color:var(--muc)}
.tester button{font:800 14px 'An Tam Van';border:0;border-radius:999px;padding:11px 16px;background:var(--do);color:#fff;cursor:pointer}
.tester button[aria-pressed=true]{background:var(--muc)}
.zoom{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:18px}
.zoom .card{text-align:center}.zoom .gl{font-weight:800;font-size:120px;line-height:1.2;color:var(--do)}
.sw{background:#fff;border-radius:6px;overflow:hidden}.sw div{height:120px}.sw p{padding:12px 14px;font-size:13px;line-height:1.45}.sw b{display:block;font-weight:800;font-size:18px;color:var(--do)}
.end{text-align:center;padding:72px 20px 90px}
@media (max-width:860px){.hero .in,.g2,.g3,.zoom{grid-template-columns:minmax(0,1fr)}.s{padding-top:52px}}
"""


def page():
    dt_a, dt_b = danh_thiep()
    sw = [("Đỏ An Tâm", "#D2141E", "Màu chính – logo, nền, chữ lớn"), ("Đỏ son", "#E2332B", "Dấu vân tay, con dấu"), ("Đỏ đậm", "#8F0D14", "Nền sâu, chữ phụ trên nền sáng"),
          ("Kem", "#FFF6EA", "Nền giấy, chữ trên nền đỏ"), ("Mực", "#231716", "Chữ thân"), ("Vàng bánh", "#F5B82E", "Điểm nhấn nhỏ – giá, nhãn mới")]
    sws = "".join(f'<div class="sw"><div style="background:{h}"></div><p><b>{n}</b>{h} · {u}</p></div>' for n, h, u in sw)
    js = """<script>
const inp=document.getElementById('t'),out=document.getElementById('o'),bs=[...document.querySelectorAll('.tester button')];
function r(){out.textContent=inp.value.trim()||'Bánh nóng, giao tận bếp';try{localStorage.setItem('van-t',inp.value)}catch(e){}}
try{inp.value=localStorage.getItem('van-t')||''}catch(e){}inp.addEventListener('input',r);r();
bs.forEach(b=>b.addEventListener('click',()=>{bs.forEach(x=>x.setAttribute('aria-pressed','false'));b.setAttribute('aria-pressed','true');out.style.fontWeight=b.dataset.w}));
</script>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Điểm Chỉ An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="hero"><div class="bg">{nen_van(1400, 760)}</div><div class="in">
<div><div class="k">Ý tưởng 08 mở rộng · Đỏ chủ đạo</div><h1>Mỗi mẻ bánh, một lời cam kết</h1>
<p>Người Việt lăn tay điểm chỉ bằng son đỏ khi cam kết điều quan trọng. Ẩm Thực An Tâm lấy dấu vân tay son làm biểu tượng: mỗi mẻ bánh có người làm thật, chịu trách nhiệm thật. Các đường vân tròn cũng gợi chiếc bánh tortilla – và chính chúng trở thành dấu mũ trong font chữ riêng của thương hiệu.</p></div>
<div class="card">{V.logo_dung()}</div></div></header>

<section class="s"><div class="num">01 · Font thương hiệu</div><h2>An Tâm Tròn Bánh</h2><p class="lead">Font riêng dựng từ Baloo 2 (SIL OFL) – chữ tròn đầy như chiếc bánh, thêm ba nét chỉ An Tâm có: <b>dấu mũ â ê ô là ba đường vân tay lồng nhau, dáng thấp gọn</b>; <b>mọi dấu chấm (i, j, dấu nặng, dấu câu) là vòng xoáy vân tay nhỏ</b>; và <b>góc chữ bo như mực son loang</b>. Hai độ đậm: ExtraBold cho tiêu đề, SemiBold cho nội dung. Đủ dấu tiếng Việt.</p>
<div class="card"><div class="tester"><input id="t" placeholder="Gõ thử chữ của bạn…" maxlength="60" aria-label="Gõ thử font An Tâm Vân"><button type="button" data-w="800" aria-pressed="true">ExtraBold</button><button type="button" data-w="500" aria-pressed="false">SemiBold</button></div>
<div class="big" id="o">Bánh nóng, giao tận bếp</div>
<div class="mid" style="margin-top:10px">ẨM THỰC AN TÂM · Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm · ấầẩẫậ ếềểễệ ốồổỗộ</div></div>
<div class="zoom"><div class="card"><div class="gl">â</div><p class="cap">Dấu mũ: ba đường vân tay, dáng thấp</p></div><div class="card"><div class="gl">ị</div><p class="cap">Dấu chấm: vòng xoáy vân tay</p></div><div class="card"><div class="gl">ộ</div><p class="cap">Đi cùng dấu thanh tiếng Việt</p></div></div></section>

<section class="s"><div class="num">02 · Logo</div><h2>Logo và phiên bản</h2><p class="lead">Bản ngang cho biển hiệu, xe, website; bản đứng cho bao bì; biểu tượng vân tay cho ảnh đại diện; dấu tròn "Cam kết từ tâm" để đóng lên phiếu, tem, hộp.</p>
<div class="g g2"><div class="card">{V.logo_ngang()}<p class="cap">Bản ngang</p></div><div class="card d">{V.logo_ngang(KEM, KEM)}<p class="cap">Bản ngang – nền đỏ</p></div>
<div class="card">{V.logo_dung()}<p class="cap">Bản đứng</p></div>
<div class="g g2"><div class="card">{V.bieu_tuong()}<p class="cap">Biểu tượng</p></div><div class="card">{V.con_dau()}<p class="cap">Dấu tròn</p></div></div></div></section>

<section class="s"><div class="num">03 · Màu</div><h2>Đỏ son của lời cam kết</h2><p class="lead">Đỏ chủ đạo, đỏ son riêng cho dấu vân tay, kem làm nền giấy. Vàng bánh chỉ là điểm nhấn nhỏ.</p><div class="g g3">{sws}</div></section>

<section class="s"><div class="num">04 · Hoạ tiết</div><h2>Đường vân chảy</h2><p class="lead">Phóng to một góc vân tay thành nền đường cong song song – dùng cho bao bì, nền mạng xã hội, xe giao hàng, giấy gói.</p>
<div class="card" style="padding:0;overflow:hidden">{nen_van(1200, 360)}</div></section>

<section class="s"><div class="num">05 · Ứng dụng</div><h2>Dấu tay trên mọi điểm chạm</h2><p class="lead">Chỗ trong ngoặc vuông là thông tin cần điền thật. Thẻ "người làm bánh" chỉ nên dùng khi xưởng thật sự ghi lại người làm từng mẻ.</p>
<div class="g g2"><div class="card">{phieu()}<p class="cap">Phiếu giao hàng – người làm bánh điểm chỉ xác nhận</p></div>
<div class="card">{the_tho()}<p class="cap">Thẻ treo "Mẻ bánh hôm nay"</p></div>
<div class="card">{tui()}<p class="cap">Túi bánh tortilla có tem vân tay</p></div>
<div class="card">{bai_dang()}<p class="cap">Bài đăng mạng xã hội 4:5</p></div>
<div class="card">{xe()}<p class="cap">Xe giao hàng</p></div>
<div class="g"><div class="card">{dt_a}<p class="cap">Danh thiếp – mặt trước</p></div><div class="card">{dt_b}<p class="cap">Danh thiếp – mặt sau</p></div></div></div></section>

<div class="end"><div style="max-width:620px;margin:0 auto">{V.logo_ngang()}</div></div>
{js}</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

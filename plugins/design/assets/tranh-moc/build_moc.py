"""Trang trình bày hướng "Tranh Mộc" (vẽ tay · ấm · truyền thống Việt). Chạy: python3 build_moc.py OUT.html"""
import base64
import math
import os
import sys

import logo_moc as M

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
DO, DO2, KEM, BO, MUC, GIAY, LA, VANG = M.DO, M.DO2, M.KEM, M.BO, M.MUC, M.GIAY, M.LA, M.VANG
KRAFT, KRAFT2 = "#C9A273", "#B48A5C"


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = []
    for fam, w in (("shantell-sans", 800), ("shantell-sans", 500)):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Shantell Sans';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, fam, 'files', f'{fam}-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    for w in (400, 600):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'be-vietnam-pro', 'files', f'be-vietnam-pro-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    return "\n".join(out)


def inner(svg):
    return svg[svg.index(">") + 1:svg.rindex("</svg>")]


def place(svg, x, y, w, h):
    """Đặt một SVG hoàn chỉnh vào khung (x, y, w, h), giữ tỉ lệ."""
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


def ill(n):
    return f'<image href="{b64(f"{MH}/{n}.svg", "image/svg+xml")}"'


# ---------- hoạ tiết ----------
def bang_tia(w, h=60, fg=DO, bg=GIAY, ink=MUC, uid="bt"):
    """Dải hoa văn trống đồng: hàng tam giác răng cưa + chấm."""
    s = M.defs(uid, 1.8) + f'<rect width="{w}" height="{h}" fill="{bg}"/><g filter="url(#{uid}w)">'
    step = 34
    for x in range(0, w + step, step):
        s += f'<path d="M{x},{h * .72:.0f} L{x + step / 2:.0f},{h * .22:.0f} L{x + step},{h * .72:.0f}Z" fill="{fg}" stroke="{ink}" stroke-width="2" stroke-linejoin="round"/>'
        s += f'<circle cx="{x + step / 2:.0f}" cy="{h * .88:.0f}" r="2.6" fill="{ink}"/>'
    s += f'<path d="M0,{h * .08:.0f} H{w}" stroke="{ink}" stroke-width="3"/><path d="M0,{h * .76:.0f} H{w}" stroke="{ink}" stroke-width="2"/></g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Dải hoa văn trống đồng">{s}</svg>'


def nen_may(w, h, bg=DO, ink=DO2, uid="nm"):
    """Nền mây cuộn lặp, so le."""
    s = M.defs(uid, 2) + f'<rect width="{w}" height="{h}" fill="{bg}"/><g filter="url(#{uid}w)">'
    for j, y in enumerate(range(60, h + 80, 90)):
        for x in range(-60 + (60 if j % 2 else 0), w + 120, 150):
            s += M.may(x, y, 90, ink)
    s += "</g>"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Nền mây cuộn">{s}</svg>'


# ---------- ứng dụng ----------
def tui_banh():
    """Túi giấy kraft đựng bánh tortilla, nhãn tròn huy hiệu, dải trống đồng."""
    e = inner(M.emblem("tb"))
    band = inner(bang_tia(300, 46, uid="tbb"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" role="img" aria-label="Túi bánh tortilla">
<defs><linearGradient id="kr" x1="0" x2="1"><stop offset="0" stop-color="{KRAFT2}"/><stop offset=".35" stop-color="{KRAFT}"/><stop offset=".8" stop-color="#D4AF82"/><stop offset="1" stop-color="{KRAFT2}"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#3B1E10" flood-opacity=".28"/></filter></defs>
<g filter="url(#sh)"><path d="M70,70 L350,70 L372,490 L48,490 Z" fill="url(#kr)"/>
<path d="M70,70 L350,70 L346,104 L74,104 Z" fill="{KRAFT2}"/>
<path d="M70,70 L80,58 L340,58 L350,70Z" fill="#A87F52"/></g>
{place(bang_tia(280, 40, uid="tbb"), 70, 118, 280, 40)}
{place(M.emblem("tb"), 110, 175, 200, 200)}
<g transform="translate(210 430)">{M.ink_text("Bánh Tortilla", 40, DO, MUC, 0, 0)[0]}</g>
<g transform="translate(210 466)">{M.L.text("10 chiếc · [Cần điền: khối lượng]", 15, "sans", .04, 0, 0, MUC, "middle")[0]}</g>
</svg>'''


def hop_giao():
    """Hộp giấy giao hàng nhìn xiên: mặt trên đỏ có huy hiệu, mặt bên kraft có mây."""
    e = inner(M.emblem("hg", MUC, MUC, BO))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 420" role="img" aria-label="Hộp giao hàng">
<defs><filter id="hs"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#3B1E10" flood-opacity=".25"/></filter></defs>
<g filter="url(#hs)">
<path d="M60,150 L260,60 L460,150 L260,240 Z" fill="{DO}"/>
<path d="M60,150 L260,240 L260,380 L60,290 Z" fill="{KRAFT}"/>
<path d="M260,240 L460,150 L460,290 L260,380 Z" fill="{KRAFT2}"/></g>
<g transform="matrix(.42 .19 -.42 .19 260 70)"><g transform="translate(0 0) scale(.9)">{e}</g></g>
<g transform="matrix(1 .45 0 1 80 190)" opacity=".9">{M.may(10, 40, 70, MUC)}{M.may(100, 80, 60, MUC)}</g>
<g transform="matrix(1 -.45 0 1 290 330)">{M.ink_text("An Tâm", 40, DO, MUC, 70, -18)[0]}</g>
</svg>'''


def danh_thiep():
    a = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt trước">
<rect width="520" height="300" rx="14" fill="{DO}"/>{inner(nen_may(520, 300, DO, "#A20F18", "dt"))}
{place(M.logo_chinh("dtl", None, KEM, MUC, KEM), 60, 30, 400, 240)}</svg>'''
    w, _ = M.ink_text("[Cần điền: Họ tên]", 30, DO, MUC, 40, 90, "start")
    use = M.use(M.HAND_M)
    lines = "".join(M.L.text(t, 17, "sans", .02, 40, y, MUC)[0] for t, y in (("[Cần điền: Chức danh]", 124), ("0348.635.222", 186), ("antamfoods.com", 214), ("[Cần điền: địa chỉ xưởng, TP.HCM]", 242)))
    b = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Danh thiếp mặt sau">
<rect width="520" height="300" rx="14" fill="{GIAY}"/>{w}{lines}
{place(M.emblem("dtb"), 360, 60, 140, 140)}
<g transform="translate(0 266)">{inner(bang_tia(520, 34, uid="dtt"))}</g></svg>'''
    return a, b


def bien_hieu():
    """Biển hiệu quầy: mái hiên sọc + biển gỗ chữ An Tâm."""
    stripes = "".join(f'<path d="M{x},40 h40 v60 q-20,22 -40,0 Z" fill="{DO if (x // 40) % 2 == 0 else GIAY}" stroke="{MUC}" stroke-width="2.5"/>' for x in range(40, 680, 40))
    lg = inner(M.logo_ngang("bh", None, DO, MUC, MUC))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 420" role="img" aria-label="Biển hiệu quầy">
<rect width="720" height="420" fill="#EADBC0"/>
<rect x="30" y="30" width="660" height="16" fill="{MUC}"/>{stripes}
<rect x="90" y="150" width="540" height="190" rx="14" fill="{GIAY}" stroke="{MUC}" stroke-width="6"/>
<rect x="104" y="164" width="512" height="162" rx="8" fill="none" stroke="{MUC}" stroke-width="2" stroke-dasharray="3 7"/>
{place(M.logo_ngang("bh", None, DO, MUC, MUC), 120, 170, 480, 150)}
<rect x="60" y="340" width="600" height="60" fill="{DO2}"/>
<g transform="translate(360 380)">{M.L.text("TORTILLAS · TACO · DONER KEBAB", 22, "sans", .2, 0, 0, KEM, "middle")[0]}</g>
</svg>'''


def bai_dang():
    m = inner(nen_may(540, 675, DO, "#A20F18", "bd"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 675" role="img" aria-label="Bài đăng mạng xã hội">
{m}<rect x="36" y="36" width="468" height="603" rx="22" fill="{GIAY}" stroke="{MUC}" stroke-width="6"/>
<g transform="translate(270 132)">{M.ink_text("Bánh nóng", 66, DO, MUC, 0, 0)[0]}</g>
<g transform="translate(270 204)">{M.ink_text("mỗi sáng", 66, DO, MUC, 0, 0)[0]}</g>
{ill("banh-tortillas")} x="110" y="226" width="320" height="250"/>
<g transform="translate(270 528)">{M.L.text("Giao tận bếp nhà hàng, quán, đại lý", 20, "sans", .02, 0, 0, MUC, "middle")[0]}</g>
<g transform="translate(270 590)">{M.ink_text("0348.635.222", 34, BO, MUC, 0, 0)[0]}</g>
</svg>'''


def hoa_tiet():
    t = inner(bang_tia(520, 60, uid="ht1"))
    m = inner(nen_may(520, 220, GIAY, MUC, "ht2"))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 300" role="img" aria-label="Hoạ tiết">{m}<g transform="translate(0 230)">{t}</g></svg>'


CSS = """
:root{--do:#B5121B;--do2:#7D0A10;--kem:#FFF4E8;--bo:#FFD37A;--muc:#3B1E10;--giay:#F6EBD5;--vang:#F2C46B}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--giay);color:var(--muc);font:16px/1.6 'Be Vietnam Pro',system-ui,sans-serif;
background-image:radial-gradient(#3B1E1010 1px,transparent 1.2px);background-size:7px 7px}
h1,h2,h3,.hand{font-family:'Shantell Sans','Be Vietnam Pro',sans-serif;font-weight:800}
:not(svg)>svg{display:block;width:100%;height:auto}
.hero{background:var(--do);color:var(--kem);position:relative;overflow:hidden}
.hero .bg{position:absolute;inset:0;opacity:1}.hero .bg svg{width:100%;height:100%}
.hero .in{position:relative;max-width:1200px;margin:0 auto;padding:64px 20px 56px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:40px;align-items:center}
.hero .k{font-weight:600;font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:var(--bo)}
.hero h1{font-size:clamp(40px,5.4vw,78px);line-height:1.02;margin:12px 0 18px;text-shadow:3px 3px 0 var(--muc)}
.hero p{max-width:560px;font-size:17px}
.band{height:46px}.band svg{height:46px}
section.s{max-width:1200px;margin:0 auto;padding:64px 20px 8px}
.s h2{font-size:clamp(32px,4vw,48px);color:var(--do);line-height:1.1}
.s .lead{max-width:680px;margin:10px 0 26px}
.num{font-weight:600;font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--do2)}
.g{display:grid;gap:18px;align-items:start}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:#FFFDF8;border:3px solid var(--muc);border-radius:22px;padding:22px;box-shadow:5px 5px 0 var(--muc)}
.card.do{background:var(--do)}.card.muc{background:var(--muc)}
.cap{font-size:14px;margin-top:10px}
.sw{border:3px solid var(--muc);border-radius:18px;overflow:hidden;box-shadow:4px 4px 0 var(--muc);background:#fff}
.sw div{height:110px}.sw p{padding:10px 12px;font-size:13px;line-height:1.4}.sw b{font-family:'Shantell Sans';font-size:17px;display:block}
.ty .big{font-family:'Shantell Sans';font-weight:800;font-size:clamp(44px,6vw,80px);line-height:1.05;color:var(--do)}
.ty .mid{font-family:'Shantell Sans';font-weight:500;font-size:26px}
.end{text-align:center;padding:72px 20px 90px}
.end h2{font-size:clamp(34px,5vw,60px);color:var(--do)}
@media (max-width:820px){.hero .in,.g2,.g3{grid-template-columns:minmax(0,1fr)}.s{padding-top:48px}}
"""


def page():
    e = M.emblem("he", DO2, MUC, KEM)
    dt_a, dt_b = danh_thiep()
    sw = [("Đỏ son", "#B5121B", "Màu chính – chữ, huy hiệu"), ("Vàng bánh", "#F2C46B", "Chiếc bánh, điểm nhấn"), ("Nâu mực", "#3B1E10", "Nét viền, chữ thân"),
          ("Giấy dó", "#F6EBD5", "Nền giấy, bao bì"), ("Đỏ đậm", "#7D0A10", "Nền tối, mây"), ("Xanh lá", "#4E7A3A", "Rau tươi – dùng ít")]
    sws = "".join(f'<div class="sw"><div style="background:{h}"></div><p><b>{n}</b>{h} · {u}</p></div>' for n, h, u in sw)
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tranh Mộc An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="hero"><div class="bg">{nen_may(1400, 700, DO, "#A20F18", "hero")}</div><div class="in">
<div><div class="k">Bộ nhận diện mới · Vẽ tay · Ấm · Truyền thống Việt</div><h1>Chiếc bánh là mặt trời trống đồng</h1>
<p>Logo mới vẽ theo lối tranh khắc gỗ Đông Hồ: nét viền nâu mực dày, mảng đỏ son in lệch nhẹ như bản in tay trên giấy dó. Ở giữa là chiếc bánh tortilla vàng, toả tia như mặt trời trên mặt trống đồng — món ăn hằng ngày, nét Việt nghìn năm, làm bằng cả tấm lòng.</p></div>
<div>{e}</div></div></header>
<div class="band">{bang_tia(1600, 46, uid="b1")}</div>

<section class="s"><div class="num">01 · Logo</div><h2>Ba cách đặt logo</h2><p class="lead">Bản đứng dùng cho bao bì và bìa hồ sơ; bản ngang cho biển hiệu, đầu thư, website; huy hiệu tròn cho tem dán, con dấu, ảnh đại diện.</p>
<div class="g g2"><div class="card">{M.logo_chinh("l1")}<p class="cap">Bản đứng – trên nền giấy dó</p></div>
<div class="card do">{M.logo_chinh("l2", None, KEM, MUC, KEM)}<p class="cap" style="color:var(--kem)">Bản đứng – trên nền đỏ son</p></div>
<div class="card">{M.logo_ngang("l3")}<p class="cap">Bản ngang</p></div>
<div class="g g2"><div class="card">{M.emblem("l4")}<p class="cap">Huy hiệu</p></div><div class="card muc">{M.emblem("l5", DO2, MUC, BO)}<p class="cap" style="color:var(--kem)">Huy hiệu nền tối</p></div></div></div></section>

<section class="s"><div class="num">02 · Màu</div><h2>Màu của bếp lửa và giấy dó</h2><p class="lead">Giữ đỏ – kem – vàng quen thuộc, thêm nâu mực cho nét vẽ tay. Đỏ son chiếm phần lớn, vàng bánh chỉ làm điểm nhấn.</p>
<div class="g g3">{sws}</div></section>

<section class="s ty"><div class="num">03 · Chữ</div><h2>Chữ vẽ tay, nét đậm</h2><p class="lead">Tiêu đề dùng Shantell Sans đậm – nét như viết bằng bút lông, đủ dấu tiếng Việt. Nội dung dùng Be Vietnam Pro cho rõ ràng. Cả hai là font mã nguồn mở SIL OFL.</p>
<div class="card"><div class="big">Bánh nóng, giao tận bếp</div><div class="mid">Ẩm Thực An Tâm – Sản Phẩm Tận Tâm, Phát Triển Xứng Tầm</div>
<p style="margin-top:12px">Be Vietnam Pro: Bánh tortilla mềm dẻo, taco giòn và doner kebab đậm vị cho nhà hàng, quán ăn và chuỗi cửa hàng tại TP.HCM. Báo giá: [giá].</p></div></section>

<section class="s"><div class="num">04 · Hoạ tiết</div><h2>Mây cuộn và răng cưa trống đồng</h2><p class="lead">Hai hoạ tiết vẽ tay dùng làm nền, viền, dải trang trí. Mép nét hơi rung như bản khắc gỗ.</p>
<div class="card" style="padding:0;overflow:hidden">{hoa_tiet()}</div></section>

<section class="s"><div class="num">05 · Ứng dụng</div><h2>Lên bao bì, biển hiệu, mạng xã hội</h2><p class="lead">Thông tin trong ngoặc vuông là chỗ cần điền thật trước khi in.</p>
<div class="g g2"><div class="card">{tui_banh()}<p class="cap">Túi giấy kraft đựng bánh tortilla</p></div>
<div class="card">{hop_giao()}<p class="cap">Hộp giao hàng</p></div>
<div class="card">{bien_hieu()}<p class="cap">Biển hiệu quầy</p></div>
<div class="card">{bai_dang()}<p class="cap">Bài đăng mạng xã hội 4:5</p></div>
<div class="card">{dt_a}<p class="cap">Danh thiếp – mặt trước</p></div>
<div class="card">{dt_b}<p class="cap">Danh thiếp – mặt sau</p></div></div></section>

<div class="end"><h2>Ẩm Thực An Tâm</h2><p>Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm · antamfoods.com · 0348.635.222</p></div>
<div class="band">{bang_tia(1600, 46, uid="b2")}</div>
</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

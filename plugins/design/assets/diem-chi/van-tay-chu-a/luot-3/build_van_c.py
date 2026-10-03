import os, itertools, van_c as B, van_a as A, logo_van as V, build_chuan as C
DO, KEM, MUC = A.DO, A.KEM, A.MUC
OUT = "van-c-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "hai-dau": "Hai dấu điểm chỉ nghiêng vào nhau, chụm đầu thành dáng <b>chữ A</b>; chấm tâm nằm ở lòng chữ. Câu chuyện B2B: <b>hai bên cùng điểm chỉ một lời cam kết</b> – xưởng An Tâm và quán/đại lý đối tác. Lưu ý: nhìn nhanh có thể gợi hình hai lá phổi/cánh bướm.",
 "xoay-cuon": "Vân xoáy là một <b>nét liền duy nhất</b> cuộn ra từ chấm tâm – vân tay kiểu xoáy có thật, đồng thời là <b>mặt cắt cuộn bánh</b> kebab, tortilla cuộn. Gắn thẳng với sản phẩm, rất gọn, rõ ở cỡ nhỏ.",
 "vo-taco": "Dấu vân tay <b>gập đôi thành vỏ taco</b>, chấm tâm là nhân bánh nằm ở miệng vỏ. Vui, gắn với sản phẩm taco; nhưng ít gợi chữ A và có thể bị đọc là cái bát / mặt trời mọc.",
 "banh-tron": "Một <b>vỏ bánh tròn</b> (vành viền) ôm dấu <b>vân lều chữ A</b> và chấm tâm. Đọc được ba lớp: bánh tortilla – vân tay – chữ A. Dạng tròn rất hợp làm tem, con dấu, ảnh đại diện.",
}
SC = {"hai-dau": .92, "xoay-cuon": 1.0, "vo-taco": 1.05, "banh-tron": .95}
uid = itertools.count()
def m(k, cx, cy, r, c=DO):
    f = dict((a, fn) for a, _, fn in B.KINDS)[k]; return f(cx, cy, r * SC[k], c)
def sv(vb, body, bg=None):
    x, y, w, h = vb; r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}">{r}{body}</svg>'
def ngang(k, fg=DO, sub=MUC):
    t0, _ = V.text("ẨM THỰC", 24, "xb", 232, 70, sub, track=.32); t1, w1 = V.text("An Tâm", 118, "xb", 226, 176, fg, track=-.02)
    t2, w2 = V.text("Sản Phẩm Tận Tâm · Phát Triển Xứng Tầm", 17, "md", 232, 214, sub, track=.02)
    return sv((0, 0, 232 + max(w1, w2) + 30, 250), m(k, 110, 128, 88, fg) + t0 + t1 + t2)
def lon(k, c=DO, bg=KEM): return sv((0, 0, 300, 300), m(k, 150, 155, 105, c), bg)
def avatar(k): return sv((0, 0, 200, 200), f'<circle cx="100" cy="100" r="100" fill="{DO}"/>' + m(k, 100, 102, 62, KEM))
def nho(k): return sv((0, 0, 150, 50), m(k, 25, 26, 16) + m(k, 70, 26, 11) + m(k, 110, 26, 7))
secs = toc = ""
for k, t, _ in B.KINDS:
    for f, s in (("lon", lon(k)), ("nen-do", lon(k, KEM, DO)), ("ngang", ngang(k))):
        open(f"{OUT}/{k}-{f}.svg", "w").write(s)
    secs += f'''<section class="s" id="{k}"><div class="num">Phương án</div><h2>{t}</h2><p class="lead">{NOTE[k]}</p>
<div class="g g4"><div class="card">{lon(k)}</div><div class="card d">{lon(k, KEM, DO)}</div><div class="card">{avatar(k)}<p class="cap">Ảnh đại diện Facebook/Zalo</p></div>
<div class="card">{nho(k)}<p class="cap">Cỡ nhỏ 32 · 22 · 14 px</p></div></div>
<div class="card" style="margin-top:18px">{ngang(k)}</div></section>'''
    toc += f'<a href="#{k}">{t.split(" · ")[0]}</a>'
ref = sv((0, 0, 300, 300), V.van_tay(150, 155, 105), KEM)
css = C.CSS + ".card svg{display:block;width:100%;height:auto}.d{background:var(--do)!important}.verdict{max-width:1200px;margin:56px auto 0;padding:0 20px}"
html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vân tay – lượt 3</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Lượt 3 – vân tay kể chuyện sản phẩm</div><h1>Dấu son, cuộn bánh, cam kết</h1>
<p>Bốn hướng mới: vân tay gắn với sản phẩm (cuộn bánh, vỏ taco, bánh tròn) và với câu chuyện hai bên cùng điểm chỉ cam kết.</p></div>
<div class="card">{sv((0,0,900,300), m("hai-dau",150,150,100)+m("xoay-cuon",450,150,100)+m("banh-tron",750,150,100))}</div></div></header>
<nav class="toc">{toc}<a href="https://claude.ai/artifact/Edv3fcPpxmsjuu2aatpnx1">Lượt 1</a><a href="https://claude.ai/artifact/TRH7GiDRma2BnUAXVANppd">Lượt 2</a></nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>C2 · Vân xoáy cuộn bánh</b> là phương án sạch và bền nhất: một nét liền, rõ ở mọi cỡ, gắn thẳng với sản phẩm cuộn – và vẫn là vân tay thật. Nếu muốn giữ chữ A: <b>C4 · Vân lều trong vỏ bánh tròn</b> (hợp tem, dấu, ảnh đại diện) hoặc <b>C1 · Hai dấu chụm</b> (câu chuyện hợp tác mạnh nhất).</p><p class="cap">Bản chuẩn 1.1 hiện tại để so: </p><div style="max-width:160px">{ref}</div>
<p class="cap">Có thể kết hợp với lượt 1 (ví dụ: khuôn chữ A + đỉnh vân lều). Ở cỡ ≤ 24 px vẫn dùng biểu tượng bản nhỏ.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án nào (C1–C4, B1–B4, a1–A3)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-chu-a-luot-2.html", "w").write(html); print("ok")

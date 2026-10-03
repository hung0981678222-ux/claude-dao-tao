import os, itertools, van_b as B, van_a as A, logo_van as V, build_chuan as C
DO, KEM, MUC = A.DO, A.KEM, A.MUC
OUT = "van-b-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "khac-A": "Giữ nguyên dấu vân tay tròn và chấm tâm, nhưng các đường vân <b>đứt theo nét chữ A</b> – chữ A hiện ra bằng khoảng trống, như được khắc vào dấu son. Nhìn lướt là vân tay, nhìn kỹ thấy chữ A. Tinh tế, khó sao chép.",
 "mu-tach": "Dấu vân tay tròn đội một <b>dấu mũ ba nét vân</b> tách rời – cả dấu đọc thành <b>ô / â</b>, gợi chữ T<b>â</b>m; cũng gợi hình <b>mái nhà</b> (an tâm như ở nhà). Gọn, dễ nhớ, rõ ở cỡ nhỏ hơn các phương án khác.",
 "khuon-A": "Lấy đúng <b>chữ A của font An Tâm Tròn Bánh</b> làm khuôn, lấp đầy bằng đường vân đồng tâm toả ra từ chấm tâm nằm trong lòng chữ A. Đọc ra chữ A ngay lập tức, vân tay là chất liệu – mạnh nhất về nhận diện chữ.",
 "khuon-a": "Như B3 nhưng dùng <b>chữ a</b> thường của font: chấm tâm nằm đúng lòng chữ a, vân toả ra lấp kín thân chữ. Mềm, tròn, hợp tên “Tròn Bánh”; cần chú ý không bị đọc thành ký hiệu @.",
}
SC = {"khac-A": .92, "mu-tach": 1.0, "khuon-A": .86, "khuon-a": .95}
uid = itertools.count()
def m(k, cx, cy, r, c=DO):
    f = dict((a, fn) for a, _, fn in B.KINDS)[k]; return f(cx, cy, r * SC[k], c, str(next(uid)))
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
<title>Vân tay chữ A – lượt 2</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Ý tưởng khác cho vân tay</div><h1>Chữ A trong dấu son</h1>
<p>Bốn hướng mới, khác lượt trước (uốn vân): chữ A hiện ra bằng khoảng trống, dấu mũ tách rời, và vân tay lấp đầy khuôn chữ A / a của font An Tâm.</p></div>
<div class="card">{sv((0,0,900,300), m("khac-A",150,150,100)+m("mu-tach",450,150,100)+m("khuon-A",750,150,100))}</div></div></header>
<nav class="toc">{toc}<a href="https://claude.ai/artifact/Edv3fcPpxmsjuu2aatpnx1">Lượt 1 (a1–A3)</a></nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p>Nếu ưu tiên <b>vẫn là dấu vân tay</b>: chọn <b>B1 · Chữ A khắc</b> – giữ nguyên dáng dấu son, chữ A ẩn trong khoảng trống. Nếu ưu tiên <b>đọc ra chữ ngay</b>: chọn <b>B3 · Vân trong khuôn chữ A</b> – rõ nhất và đúng chữ của font An Tâm. B2 gọn, dễ dùng ở cỡ nhỏ nhưng dễ bị đọc là “mái nhà”.</p>
<p class="cap">Bản chuẩn 1.1 hiện tại để so: </p><div style="max-width:160px">{ref}</div>
<p class="cap">Có thể kết hợp với lượt 1 (ví dụ: khuôn chữ A + đỉnh vân lều). Ở cỡ ≤ 24 px vẫn dùng biểu tượng bản nhỏ.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án nào (B1–B4, hoặc a1–A3 ở lượt 1)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-chu-a-luot-2.html", "w").write(html); print("ok")

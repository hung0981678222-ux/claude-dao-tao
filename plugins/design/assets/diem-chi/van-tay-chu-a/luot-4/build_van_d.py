import os, itertools, van_d as B, van_a as A, logo_van as V, build_chuan as C
DO, KEM, MUC = A.DO, A.KEM, A.MUC
OUT = "van-d-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "D1": "Hạt nhân là <b>chữ a</b> nét đậm (đúng kiểu chữ a tròn của font An Tâm Tròn Bánh), chấm tâm son nằm trong lòng chữ. Các đường vân <b>chảy theo hình chữ a</b> rồi tròn dần ra ngoài – đúng cách vân tay thật uốn quanh lõi. Nhìn gần rõ chữ a, nhìn xa là dấu điểm chỉ.",
 "D2": "Không có nét chữ riêng: <b>vòng vân đầu tiên quanh chấm tâm chính là chữ a</b> (cùng độ dày với vân). Các vòng sau ôm theo chữ a và mềm dần. Tinh tế hơn D1 – chữ a là một phần của vân tay chứ không đặt lên trên.",
 "D3": "<b>Toàn bộ nét vân chỉ uốn nhẹ</b> theo chữ a: vòng trong còn dáng a, ra ngoài gần như tròn hẳn. Kín đáo nhất – người xem cảm thấy 'có gì đó' rồi mới nhận ra chữ a.",
 "D4": "Cùng cách làm nhưng hạt nhân là <b>chữ A hoa</b>: vân dựng thành mái nhọn chữ A ở giữa rồi tròn dần ra ngoài; chấm tâm nằm trong lòng chữ A. Không bị nhầm với ký hiệu @.",
}
SC = {"D1": .88, "D2": .88, "D3": .88, "D4": .88}
uid = itertools.count()
def m(k, cx, cy, r, c=DO):
    return B.mark(k, cx, cy, r * SC[k], c)
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
for k, t in B.KINDS:
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
<title>Vân tay chữ a – lượt 4</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Lượt 4 – vân chảy quanh chữ a</div><h1>Vân tay mọc ra từ chữ a</h1>
<p>Quay lại đúng ý ban đầu: vòng vân quanh chấm tâm là chữ a, các nét vân còn lại uốn theo chữ a rồi tròn dần – như vân tay thật chảy quanh lõi.</p></div>
<div class="card">{sv((0,0,900,300), m("D1",150,150,110)+m("D2",450,150,110)+m("D4",750,150,110))}</div></div></header>
<nav class="toc">{toc}<a href="https://claude.ai/artifact/Edv3fcPpxmsjuu2aatpnx1">Lượt 1</a><a href="https://claude.ai/artifact/TRH7GiDRma2BnUAXVANppd">Lượt 2</a><a href="https://claude.ai/artifact/7YziFTQz16NdVUY9UB37aN">Lượt 3</a></nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p>Đúng ý “vòng ngoài chấm tâm giống chữ a”: <b>D2</b> – chữ a là chính đường vân, tinh tế và vẫn thuần vân tay. Muốn chữ a rõ, dễ nhận ra trên bảng hiệu/bao bì: <b>D1</b>. Muốn kín đáo nhất: <b>D3</b>. Muốn tránh hẳn nguy cơ bị đọc thành @: <b>D4</b> (chữ A hoa).</p><p class="cap">Bản chuẩn 1.1 hiện tại để so: </p><div style="max-width:160px">{ref}</div>
<p class="cap">Có thể kết hợp với lượt 1 (ví dụ: khuôn chữ A + đỉnh vân lều). Ở cỡ ≤ 24 px vẫn dùng biểu tượng bản nhỏ.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án nào (D1–D4)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-chu-a-luot-2.html", "w").write(html); print("ok")

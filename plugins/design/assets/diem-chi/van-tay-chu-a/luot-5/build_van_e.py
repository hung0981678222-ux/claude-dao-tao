import os, itertools, van_e as B, van_a as A, logo_van as V, build_chuan as C
DO, KEM, MUC = A.DO, A.KEM, A.MUC
OUT = "van-e-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "E1": "Một dấu vân tay <b>thật</b>: kiểu vân móc (loop) – loại phổ biến nhất trên ngón cái người Việt, có chỗ rẽ nhánh, chỗ đứt, nét đậm ở giữa và mảnh dần ra mép như lực ấn ngón tay, mép dấu loang nhẹ như mực son. <b>Chấm tâm</b> nằm đúng điểm lõi của vân móc – nơi các đường vân quay đầu. Không cần chữ: nét riêng là dấu tay thật có tâm son.",
 "E2": "Như E1, thêm <b>một sợi chỉ vàng</b> chạy theo đường vân móc ôm sát chấm tâm – như sợi chỉ đỏ-vàng buộc lời hứa. Một điểm nhấn duy nhất, nhỏ (đúng quy tắc vàng ≤ 5%), làm dấu sang và khó nhầm với bất kỳ dấu vân tay nào khác.",
 "E3": "Vân <b>xoáy</b> (whorl) thật: các vòng vân cuộn quanh chấm tâm. Cân đối, tròn trịa – gần với bản 1.1 nhất nhưng chi tiết và có hồn hơn hẳn.",
 "E4": "Vân móc thật với một <b>khoảng lặng</b> nhỏ quanh chấm tâm – vân dừng lại trước tâm, như mọi thứ quy về một chữ Tâm. Chấm tâm nổi bật hơn, dễ nhận ra ở cỡ vừa.",
 "E5": "Vân móc với <b>nét mảnh và dày đặc</b> như bản khắc trên tiền giấy, tem quý. Sang và tinh tế khi in lớn (bảng hiệu, hộp quà, ép kim) – nhưng cần bản đơn giản hơn cho cỡ nhỏ.",
}
SC = {k: .92 for k in ("E1", "E2", "E3", "E4", "E5")}
uid = itertools.count()
def m(k, cx, cy, r, c=DO):
    return B.mark(k, cx, cy, r * SC[k], c, KEM if c == DO else DO)
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
<title>Vân tay thật – lượt 5</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Lượt 5 – vân tay thật, sang</div><h1>Một dấu tay thật, một chấm tâm</h1>
<p>Không cần chữ. Vân tay chi tiết như dấu ngón cái thật – rẽ nhánh, đậm nhạt theo lực ấn, mép loang như mực son – với chấm tâm đặt đúng điểm lõi của vân.</p></div>
<div class="card">{sv((0,0,900,300), m("E1",150,150,120)+m("E2",450,150,120)+m("E3",750,150,120))}</div></div></header>
<nav class="toc">{toc}<a href="https://claude.ai/artifact/Edv3fcPpxmsjuu2aatpnx1">Lượt 1</a><a href="https://claude.ai/artifact/TRH7GiDRma2BnUAXVANppd">Lượt 2</a><a href="https://claude.ai/artifact/7YziFTQz16NdVUY9UB37aN">Lượt 3</a><a href="https://claude.ai/artifact/RY6djHrZ8rfPVeL8r2ryJv">Lượt 4</a></nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>E2 · Sợi chỉ tâm</b>: dấu tay thật + một sợi chỉ vàng ôm chấm tâm – sang, có một chi tiết riêng không ai trùng. Muốn thuần đỏ, mộc mạc mà vẫn thật: <b>E1</b>. In lớn cao cấp (ép kim, hộp quà): <b>E5</b>.</p><p class='cap'>Vân tay thật có nhiều chi tiết – ở cỡ ≤ 32 px dùng biểu tượng bản nhỏ đơn giản hoá đi kèm.</p><p class="cap">Bản chuẩn 1.1 hiện tại để so: </p><div style="max-width:160px">{ref}</div>
<p class="cap">Có thể kết hợp với lượt 1 (ví dụ: khuôn chữ A + đỉnh vân lều). Ở cỡ ≤ 24 px vẫn dùng biểu tượng bản nhỏ.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án nào (E1–E5)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-chu-a-luot-2.html", "w").write(html); print("ok")

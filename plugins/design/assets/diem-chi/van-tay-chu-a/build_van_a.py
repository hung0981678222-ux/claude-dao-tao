import os, van_a as A, logo_van as V, build_chuan as C
DO, KEM, MUC = A.DO, A.KEM, A.MUC
OUT = "van-a-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "goc": "Bản đang dùng: vòng vân tròn, lõi chấm tâm. Đẹp, sạch nhưng là hình vân tay chung – ai cũng có thể vẽ giống.",
 "a-loi": "Vòng vân sát chấm tâm uốn thành chữ <b>a</b> (đúng kiểu chữ a một tầng của font An Tâm Tròn Bánh): chấm tâm nằm trong lòng chữ a, nét đứng bên phải có đuôi. Nhìn xa vẫn là vân tay, nhìn gần thấy chữ a của An Tâm.",
 "a-mu": "Lõi chữ <b>a</b> như a1, các vòng vân phía trên vồng nhọn lên như dấu mũ – cả dấu đọc thành <b>â</b> của chữ T<b>â</b>m. Dấu mũ của font cũng là vòm vân lồng nhau, nên logo và chữ nói cùng một ngôn ngữ.",
 "A-nhe": "Toàn bộ đường vân chỉ uốn nhẹ: đỉnh hơi nhọn, vai hơi thu – gợi bóng chữ <b>A</b> mà không lộ. Thay đổi ít nhất so với bản đang dùng, chuyển đổi dễ.",
 "A-leu": "Đường vân vồng nhọn rõ thành dáng chữ <b>A</b>. Đây là kiểu vân 'lều' (tented arch) có thật trên đầu ngón tay – nên vẫn là dấu điểm chỉ thật, không phải vẽ chữ giả vân.",
 "A-mo": "Vân mở ở chân giữa thành hai chân chữ <b>A</b>, vòng trong khép đáy làm nét ngang, chấm tâm nằm trong lòng A. Đọc ra chữ A rõ nhất, nhưng bớt giống vân tay nhất.",
}
S = {"goc": 1, "a-loi": 1, "a-mu": .84, "A-nhe": .95, "A-leu": .84, "A-mo": .9}
def m(k, cx, cy, r, c=DO): return A.mark(k, cx, cy, r * S[k], c)
def sv(vb, body, bg=None, w=None):
    x, y, ww, h = vb; r = f'<rect x="{x}" y="{y}" width="{ww}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {ww} {h}">{r}{body}</svg>'
def ngang(k, fg=DO, sub=MUC, bg=None):
    t0, _ = V.text("ẨM THỰC", 24, "xb", 232, 70, sub, track=.32); t1, w1 = V.text("An Tâm", 118, "xb", 226, 176, fg, track=-.02)
    t2, w2 = V.text("Sản Phẩm Tận Tâm · Phát Triển Xứng Tầm", 17, "md", 232, 214, sub, track=.02)
    return sv((0, 0, 232 + max(w1, w2) + 30, 250), m(k, 110, 128, 88, fg) + t0 + t1 + t2, bg)
def lon(k, c=DO, bg=KEM): return sv((0, 0, 300, 300), m(k, 150, 158, 105, c), bg)
def avatar(k): return sv((0, 0, 200, 200), f'<circle cx="100" cy="100" r="100" fill="{DO}"/>' + m(k, 100, 104, 62, KEM))
def nho(k): return sv((0, 0, 150, 50), m(k, 25, 26, 16) + m(k, 70, 26, 11) + m(k, 110, 26, 7))
secs = ""; toc = ""
for k, t in A.KINDS:
    key = k; name = t
    for f, s in (("lon", lon(k)), ("nen-do", lon(k, KEM, DO)), ("ngang", ngang(k))):
        open(f"{OUT}/{k}-{f}.svg", "w").write(s)
    secs += f'''<section class="s" id="{key}"><div class="num">{'Tham chiếu' if k == 'goc' else 'Phương án'}</div><h2>{name}</h2><p class="lead">{NOTE[k]}</p>
<div class="g g4"><div class="card">{lon(k)}</div><div class="card d">{lon(k, KEM, DO)}</div><div class="card">{avatar(k)}<p class="cap">Ảnh đại diện Facebook/Zalo</p></div>
<div class="card">{nho(k)}<p class="cap">Cỡ nhỏ 32 · 22 · 14 px</p></div></div>
<div class="card" style="margin-top:18px">{ngang(k)}</div></section>'''
    toc += f'<a href="#{key}">{name.split(" · ")[0] if " · " in name else "Bản chuẩn"}</a>'
css = C.CSS + ".card svg{display:block;width:100%;height:auto}.d{background:var(--do)!important}.verdict{max-width:1200px;margin:56px auto 0;padding:0 20px}"
html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vân tay chữ A</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Thêm tính thương hiệu cho vân tay</div><h1>Vân tay mang chữ a</h1>
<p>Giữ dấu vân tay son và chấm tâm, nhưng cho đường vân nói ra chữ của An Tâm – chữ <b>a</b> quanh chấm tâm, hoặc cả dấu uốn thành dáng chữ <b>A</b>.</p></div>
<div class="card">{sv((0,0,600,300), m("a-mu",150,160,110)+m("A-leu",450,160,110))}</div></div></header>
<nav class="toc">{toc}</nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>a2 · â của Tâm</b> có câu chuyện mạnh nhất: lõi chữ a + vân vồng thành dấu mũ = chữ “â” trong “Tâm”, khớp luôn với dấu mũ vòm vân của font. Nếu muốn thay đổi kín đáo, chọn <b>A1 · Vân uốn nhẹ</b>; muốn rõ chữ A mà vẫn là vân tay thật, chọn <b>A2 · Vân lều</b>.</p>
<p class="cap">Ở cỡ rất nhỏ (≤ 24 px) chữ a/A không còn đọc được – vẫn dùng biểu tượng bản nhỏ như hiện tại.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án nào (a1, a2, A1, A2, A3)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-chu-a.html", "w").write(html)
print("ok")

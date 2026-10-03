import os, van_f as F, van_g as Gm, build_chuan as C
DO, KEM, MUC, VANG = F.DO, F.KEM, F.MUC, F.VANG
OUT = "van-g-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "G1": "Vân tay kiểu <b>lều</b> (tented arch – có thật trên đầu ngón tay) dựng hình học thành <b>chữ A</b> của An Tâm: các đường vân bao đều quanh chữ A, chân cắt thẳng như nền móng, chấm tâm nằm trong lòng chữ. Vững, nhọn, hướng lên – tinh thần 'phát triển xứng tầm'.",
 "G2": "Vòng vân dạng <b>vuông bo</b> (squircle) với lõi vân móc – ngôn ngữ của biểu tượng công nghệ, ứng dụng, thiết bị. Hiện đại, gọn, đặt vừa khít mọi khung vuông (ảnh đại diện, nhãn, icon app).",
 "G3": "Vòm vân phía trên, chân vân thả xuống thành <b>vạch mã vạch</b> dày mỏng. Câu chuyện: <b>mỗi mẻ bánh truy xuất được nguồn gốc</b> – như dấu vân tay của người làm ra nó. Rất hợp B2B thực phẩm (an toàn, minh bạch).",
 "G4": "Vân tay tròn đặt trong <b>vòng thước đo có vạch chia</b> như mặt đồng hồ đo – <b>kiểm soát chất lượng</b>, chính xác từng mẻ. Hợp tem kiểm định, nhãn QC, con dấu hồ sơ.",
}
def sv(vb, body, bg=None):
    x, y, w, h = vb; r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}">{r}{body}</svg>'
def wm(x, y, fg=DO, sub=MUC, size=112):
    a, _ = F.text("ẨM THỰC", size * .2, "sb", x + 4, y - size * .92, sub, track=.42)
    b, w1 = F.text("AN TÂM", size, "xb", x, y, fg, track=-.01)
    c, w2 = F.text("TORTILLA · TACO · DONER KEBAB", size * .155, "sb", x + 4, y + size * .36, sub, track=.22)
    return a + b + c, max(w1, w2)
def ngang(k, fg=DO, sub=MUC, bg=None):
    R = 92; m = Gm.mark(k, 120 + 0, 130, R, fg, bg or KEM)
    x0 = 270
    t, w = wm(x0, 168, fg, sub)
    return sv((0, 0, x0 + w + 40, 260), m + t, bg)
def lon(k, c=DO, bg=KEM): return sv((0, 0, 300, 300), Gm.mark(k, 150 + 0, 150, 100, c, bg), bg)
def avatar(k): return sv((0, 0, 200, 200), f'<circle cx="100" cy="100" r="100" fill="{DO}"/>' + Gm.mark(k, 100 + 0, 100, 54, KEM, DO))
def nho(k): return sv((0, 0, 160, 54), Gm.mark(k, 27, 27, 22) + Gm.mark(k, 80, 27, 14) + Gm.mark(k, 128, 27, 9))
def xe(k):
    body = f'<rect x="0" y="0" width="900" height="300" rx="16" fill="#FFFFFF"/><rect x="0" y="220" width="900" height="80" fill="{DO}"/>'
    m = Gm.mark(k, 120 + 0, 110, 72, DO, "#FFFFFF")
    t, w = wm(240, 140, DO, MUC, 86)
    hl, _ = F.text("HOTLINE / ZALO  0398 431 300  ·  antamfoods.com", 22, "sb", 40, 268, KEM, track=.06)
    return sv((0, 0, 900, 300), body + m + t + hl)
secs = toc = ""
for k, t in Gm.KINDS:
    for f, s in (("lon", lon(k)), ("nen-do", lon(k, KEM, DO)), ("ngang", ngang(k)), ("xe", xe(k))):
        open(f"{OUT}/{k}-{f}.svg", "w").write(s)
    secs += f'''<section class="s" id="{k}"><div class="num">Phương án</div><h2>{t}</h2><p class="lead">{NOTE[k]}</p>
<div class="g g4"><div class="card">{lon(k)}</div><div class="card d">{lon(k, KEM, DO)}</div><div class="card">{avatar(k)}<p class="cap">Ảnh đại diện</p></div>
<div class="card">{nho(k)}<p class="cap">Cỡ nhỏ 44 · 28 · 18 px</p></div></div>
<div class="g g2" style="margin-top:18px"><div class="card">{ngang(k)}</div><div class="card d">{ngang(k, KEM, "#FFD9D5", None)}</div></div>
<div class="card" style="margin-top:18px">{xe(k)}<p class="cap">Thân xe giao hàng / biển xưởng</p></div></section>'''
    toc += f'<a href="#{k}">{t.split(" · ")[0]}</a>'
css = C.CSS + ".card svg{display:block;width:100%;height:auto}.d{background:var(--do)!important}.verdict{max-width:1200px;margin:56px auto 0;padding:0 20px}"
html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vân tay công nghiệp 2</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Lượt 7 – công nghiệp, thêm ý tưởng</div><h1>Chính xác như dây chuyền</h1>
<p>Tiếp tục hướng công nghiệp với bốn câu chuyện mới: chữ A vững chãi, biểu tượng công nghệ, truy xuất nguồn gốc, kiểm soát chất lượng.</p></div>
<div class="card">{sv((0,0,900,300), Gm.mark("G1",150,150,105)+Gm.mark("G3",450,150,105)+Gm.mark("G4",750,150,100))}</div></div></header>
<nav class="toc">{toc}<a href="https://claude.ai/artifact/HRufL65eammY8kz9UrujNE">Lượt 6 (F1–F4)</a></nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p>Mạnh nhất về câu chuyện B2B thực phẩm: <b>G3 · Vân truy xuất</b> (an toàn, minh bạch). Mạnh nhất về hình và gắn tên An Tâm: <b>G1 · Vân chữ A</b>. Có thể ghép với lượt 6 – ví dụ dải dây chuyền F2 làm hệ đồ hoạ cho G1.</p><p class="cap">Font chữ đề xuất: Be Vietnam Pro (font Việt, giấy phép mở SIL OFL, có đủ dấu tiếng Việt).</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án (G1–G4, hoặc F1–F4 ở lượt 6)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-cong-nghiep.html", "w").write(html); print("ok")

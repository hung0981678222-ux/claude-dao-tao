import os, van_f as F, build_chuan as C
DO, KEM, MUC, VANG = F.DO, F.KEM, F.MUC, F.VANG
OUT = "van-f-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "F1": "Vân tay kiểu móc (loại phổ biến nhất) được <b>dựng lại bằng hình học</b>: nét dày đều, khe đều, góc cắt có chủ ý. Ba vòm lõi ôm chấm tâm, các vòng bao chắc chắn bên ngoài. Gọn, chính xác như ký hiệu kỹ thuật – vẫn đọc ngay là vân tay.",
 "F2": "Đường vân <b>ôm chấm tâm rồi chạy thẳng ra thành các dải song song</b> – từ dấu tay người làm bánh thành <b>dây chuyền sản xuất</b>. Đồng thời gợi hình cuộn bánh. Các dải có thể kéo dài làm đường gạch chân cho chữ, viền xe, viền bao bì – rất 'công nghiệp'.",
 "F3": "F1 đặt trong <b>khối vuông bo đỏ đặc</b>, vân khoét âm bản, chấm tâm vàng. Như nhãn chứng nhận / tem chất lượng – rất mạnh trên thùng carton, xe tải, biển xưởng, ảnh đại diện.",
 "F4": "Vân dây chuyền đặt trong <b>con dấu tròn</b>. Gọn, đối xứng, dùng như tem 'đã kiểm tra', con dấu trên hồ sơ, dập nổi bao bì.",
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
    R = 92; m = F.mark(k, 120 + (40 if k == "F2" else 0), 130, R, fg, bg or KEM)
    x0 = 270 if k != "F2" else 330
    t, w = wm(x0, 168, fg, sub)
    return sv((0, 0, x0 + w + 40, 260), m + t, bg)
def lon(k, c=DO, bg=KEM): return sv((0, 0, 300, 300), F.mark(k, 150 + (28 if k == "F2" else 0), 150, 100, c, bg), bg)
def avatar(k): return sv((0, 0, 200, 200), f'<circle cx="100" cy="100" r="100" fill="{DO}"/>' + F.mark(k, 100 + (14 if k == "F2" else 0), 100, 54, KEM, DO))
def nho(k): return sv((0, 0, 160, 54), F.mark(k, 27, 27, 22) + F.mark(k, 80, 27, 14) + F.mark(k, 128, 27, 9))
def xe(k):
    body = f'<rect x="0" y="0" width="900" height="300" rx="16" fill="#FFFFFF"/><rect x="0" y="220" width="900" height="80" fill="{DO}"/>'
    m = F.mark(k, 120 + (30 if k == "F2" else 0), 110, 72, DO, "#FFFFFF")
    t, w = wm(240 if k != "F2" else 290, 140, DO, MUC, 86)
    hl, _ = F.text("HOTLINE / ZALO  0398 431 300  ·  antamfoods.com", 22, "sb", 40, 268, KEM, track=.06)
    return sv((0, 0, 900, 300), body + m + t + hl)
secs = toc = ""
for k, t in F.KINDS:
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
<title>Vân tay công nghiệp</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Lượt 6 – công nghiệp, chuyên nghiệp</div><h1>Vân tay dựng hình học</h1>
<p>Giữ ý điểm chỉ, nhưng đổi hẳn tinh thần: nét đều, khe đều, khối chắc, chữ không chân cứng cáp (Be Vietnam Pro) – cảm giác một xưởng thực phẩm lớn, sạch, chuẩn mực.</p></div>
<div class="card">{sv((0,0,900,300), F.mark("F1",150,150,105)+F.mark("F2",470,150,105)+F.mark("F3",770,150,100))}</div></div></header>
<nav class="toc">{toc}</nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>F2 · Vân dây chuyền</b> có câu chuyện công nghiệp rõ nhất (dấu tay → dây chuyền) và dải song song là một hệ thống đồ hoạ dùng được khắp nơi: viền xe, viền thùng, đường kẻ trên web. Muốn một biểu tượng khối, đứng một mình thật mạnh: <b>F3 · Huy hiệu khối</b>.</p>
<p class="cap">Font chữ đề xuất: Be Vietnam Pro (font Việt, giấy phép mở SIL OFL, có đủ dấu tiếng Việt).</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Hướng này đã đúng gu chưa? Chọn F1–F4.</h2></div></body></html>"""
open(f"{OUT}/van-tay-cong-nghiep.html", "w").write(html); print("ok")

import os, van_f as F, van_h as Gm, build_chuan as C
DO, KEM, MUC, VANG = F.DO, F.KEM, F.MUC, F.VANG
OUT = "van-h-out"; os.makedirs(OUT, exist_ok=True)
NOTE = {
 "H1": "Ghép hai ý mạnh nhất: <b>chữ A vân lều</b> (G1) và <b>dải dây chuyền</b> (F2). Chân phải mỗi đường vân bẻ góc chạy ngang thành dải song song – từ dấu tay người làm bánh thành dây chuyền. Các dải kéo dài được làm gạch chân chữ, viền xe, viền thùng.",
 "H2": "Vòng vân <b>lục giác</b> lồng nhau – hình của tổ ong, đai ốc, kết cấu kỹ thuật: chắc, chuẩn, cơ khí. Lõi vân móc với chấm tâm. Đứng vững trên mọi nền, rất hợp tem nhãn kỹ thuật.",
 "H3": "<b>Roundel</b> – kiểu biểu tượng của nhà ga, nhà máy, thương hiệu công nghiệp lâu đời: vòng vân tay tròn, một <b>băng đỏ ngang mang chữ AN TÂM</b> xuyên qua, chấm tâm ở giữa. Đọc được tên ngay trong biểu tượng – rất mạnh trên biển xưởng, xe, thùng hàng.",
 "H4": "Dấu vân tay tròn bị cắt ngang, <b>nửa trên trượt lệch đúng một đường vân</b> – như băng chuyền đang chạy. Tĩnh mà động, hiện đại, khó quên. Hợp với thương hiệu muốn thể hiện năng lực sản xuất.",
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
    R = 92; m = Gm.mark(k, 110 if k == 'H1' else 120, 130, R, fg, bg or KEM)
    x0 = 300 if k == 'H1' else 270
    t, w = wm(x0, 168, fg, sub)
    return sv((0, 0, x0 + w + 40, 260), m + t, bg)
def lon(k, c=DO, bg=KEM): return sv((0, 0, 300, 300), Gm.mark(k, 150 + 0, 150, 100, c, bg), bg)
def avatar(k): return sv((0, 0, 200, 200), f'<circle cx="100" cy="100" r="100" fill="{DO}"/>' + Gm.mark(k, 100 + 0, 100, 54, KEM, DO))
def nho(k): return sv((0, 0, 160, 54), Gm.mark(k, 27, 27, 22) + Gm.mark(k, 80, 27, 14) + Gm.mark(k, 128, 27, 9))
def xe(k):
    body = f'<rect x="0" y="0" width="900" height="300" rx="16" fill="#FFFFFF"/><rect x="0" y="220" width="900" height="80" fill="{DO}"/>'
    m = Gm.mark(k, 110 if k == 'H1' else 120, 110, 72, DO, "#FFFFFF")
    t, w = wm(270 if k == 'H1' else 240, 140, DO, MUC, 86)
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
<title>Vân tay công nghiệp 3</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Lượt 8 – công nghiệp, tiếp tục</div><h1>Vững như nhà máy</h1>
<p>Bốn ý mới theo hướng công nghiệp: chữ A chảy thành dây chuyền, lục giác kỹ thuật, roundel mang tên An Tâm, và vân lệch tầng như băng chuyền.</p></div>
<div class="card">{sv((0,0,900,300), Gm.mark("H1",130,150,95)+Gm.mark("H3",470,150,100)+Gm.mark("H4",770,150,100))}</div></div></header>
<nav class="toc">{toc}<a href="https://claude.ai/artifact/HRufL65eammY8kz9UrujNE">Lượt 6</a><a href="https://claude.ai/artifact/SWoFWVfhHQG5LVVMo7YArc">Lượt 7</a></nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>H3 · Roundel vân tay</b> là biểu tượng 'nhà máy' nhất – tên An Tâm nằm ngay trong dấu, rõ trên biển xưởng và xe. <b>H1</b> nếu muốn chữ A cùng hệ dải dây chuyền; <b>H4</b> nếu muốn hiện đại, khác biệt.</p><p class="cap">Font chữ đề xuất: Be Vietnam Pro (font Việt, giấy phép mở SIL OFL, có đủ dấu tiếng Việt).</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn phương án (H1–H4, G1–G4, F1–F4)?</h2></div></body></html>"""
open(f"{OUT}/van-tay-cong-nghiep.html", "w").write(html); print("ok")

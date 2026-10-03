import sys, build_chuan as C, ud2
css = C.CSS + ".it{background:#fff;border-radius:6px;padding:12px;margin:0 0 22px}.it img{display:block;width:100%;height:auto}.it h3{margin:4px 0 10px}"
cards = "".join(f'<figure class="it" id="{s}"><h3>{n}</h3><img src="{s}.png" alt="{n}" loading="lazy"></figure>' for s, n, _ in ud2.MOI)
toc = "".join(f'<a href="#{s}">{n}</a>' for s, n, _ in ud2.MOI)
open(sys.argv[1], "w").write(f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ứng dụng An Tâm 1.1</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ 1.1 · Thiết kế lại</div><h1>11 ứng dụng nhận diện</h1>
<p>Ly giấy, đồng phục, quầy, xe, bao bì, standee, hồ sơ năng lực – vân tay chấm tâm, hotline {ud2.HOTLINE}. Dòng chữ nhỏ dưới mỗi hình là thông số gợi ý cho nhà in/nhà may.</p></div>
<div class="card">{ud2.V.logo_ngang()}</div></div></header><nav class="toc">{toc}</nav><section class="s">{cards}</section>
<div class="end"><p>Chỗ [ ] (giá, số liệu năng lực, địa chỉ, QR) cần điền thông tin thật trước khi sản xuất.</p></div></body></html>""")

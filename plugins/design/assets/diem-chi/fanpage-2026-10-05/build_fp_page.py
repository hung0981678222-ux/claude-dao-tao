"""Trang xem bộ ảnh fanpage tuần 05–11/10/2026. Chạy sau fanpage_t10.py: python3 build_fp_page.py OUTDIR"""
import os
import sys

import build_chuan as C
import fanpage_t10 as F

GROUP = {"bai-05-10": "Bài 05/10 · Ra mắt nhận diện", "bai-09-10": "Bài 09/10 · Album bảng size vỏ bánh", "reels": "Ảnh bìa 3 Reels (06, 08, 10/10)"}


def run(out):
    items = F.all_items(); secs = []
    for g, title in GROUP.items():
        cards = "".join(f'<figure class="it" id="{slug}"><img src="{slug}.png" alt="{cap}" loading="lazy"><figcaption><b>{cap}</b> · {size}<br><code>#{slug}</code></figcaption></figure>'
                        for gg, cap, size, slug, _ in items if gg == g)
        secs.append(f'<section class="s" id="{g}"><h2>{title}</h2><div class="grid">{cards}</div></section>')
    css = C.CSS + """.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-items:start}
.it{background:#fff;border-radius:6px;padding:12px;margin:0;scroll-margin-top:70px}.it img{display:block;width:100%;height:auto}.it figcaption{font-size:14px;margin-top:8px}
.it:target{outline:4px solid var(--ngo)}@media (max-width:860px){.grid{grid-template-columns:minmax(0,1fr)}}"""
    toc = "".join(f'<a href="#{g}">{t.split(" · ")[0]}</a>' for g, t in GROUP.items())
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fanpage tuần 05–11/10</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Bản nháp · không đăng công khai</div><h1>Ảnh fanpage tuần 05–11/10/2026</h1>
<p>Nhận diện Điểm Chỉ (logo vân tay, font An Tam Tron Banh, đỏ #D2141E / kem #FFF6EA). Ô có viền đứt "KHUNG ẢNH THẬT" là chỗ chèn ảnh chụp thật; ô [__] là số đo chờ điền.</p></div>
<div class="card">{F.V.logo_ngang()}</div></div></header><nav class="toc">{toc}</nav>{"".join(secs)}
<div class="end"><p>Hotline trên ảnh: {F.HOTLINE} – chờ xác nhận.</p></div></body></html>"""
    open(os.path.join(out, "fanpage-t10.html"), "w").write(html)


if __name__ == "__main__":
    run(sys.argv[1])

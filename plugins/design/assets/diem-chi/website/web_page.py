import os
from PIL import Image
import build_chuan as C
O="web-out"; X=O+"/xem"; os.makedirs(X,exist_ok=True)
NHOM=[("banner","Banner trang chủ (1920×720) & điện thoại (750×1000)",["banner-1-1920x720","banner-2-1920x720","banner-3-1920x720","banner-1-dien-thoai-750x1000","banner-2-dien-thoai-750x1000","banner-3-dien-thoai-750x1000"],"g3"),
("danh-muc","Danh mục sản phẩm (1200×400)",["danh-muc-1-1200x400","danh-muc-2-1200x400","danh-muc-3-1200x400"],"g3"),
("san-pham","Thẻ sản phẩm (800×800) – hình minh hoạ, cần thay ảnh chụp sản phẩm thật",[f"san-pham-{i}-800x800" for i in range(1,8)],"g4"),
("trang-con","Banner trang con (1920×480)",["trang-ve-chung-toi-1920x480","trang-san-pham-1920x480","trang-nha-xuong-1920x480","trang-doi-tac-1920x480","trang-lien-he-1920x480"],"g1"),
("keu-goi","Dải kêu gọi (1920×360) & ảnh chia sẻ (1200×630)",["bang-keu-goi-1920x360","og-chia-se-1200x630"],"g1"),
("icon","Icon lợi thế, nút nổi, favicon, app icon",["icon-day-chuyen","icon-chat-luong","icon-giao-hang","icon-gia-xuong","nut-zalo","nut-goi","favicon","app-icon"],"g8")]
files={}
def prev(n):
    im=Image.open(f"{O}/{n}.png"); fn=f"xem/{n}."+("png" if im.width<=512 else "jpg")
    if im.width>512:
        im.thumbnail((1400,1400)); bg=Image.new("RGB",im.size,(255,246,234)); bg.paste(im,mask=im.split()[-1] if im.mode=="RGBA" else None); bg.save(f"{O}/{fn}",quality=84)
    else: im.save(f"{O}/{fn}")
    files[fn]=f"{O}/{fn}"; return fn
secs=""
for k,t,ns,g in NHOM:
    cards="".join(f'<figure class="card"><img src="{prev(n)}" alt="{n}" loading="lazy"><figcaption class="cap">{n}.png</figcaption></figure>' for n in ns)
    secs+=f'<section class="s" id="{k}"><h2>{t}</h2><div class="g {g}">{cards}</div></section>'
toc="".join(f'<a href="#{k}">{t.split(" (")[0].split(" –")[0]}</a>' for k,t,*_ in NHOM)
css=C.CSS+""".card img{display:block;width:100%;height:auto;border-radius:8px}figure{margin:0}.g1{grid-template-columns:1fr}.g8{grid-template-columns:repeat(8,1fr)}
@media(max-width:800px){.g8{grid-template-columns:repeat(4,1fr)}}.note{max-width:1200px;margin:24px auto;padding:0 20px}"""
html=f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ảnh website An Tâm</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ 1.1 · antamfoods.com</div><h1>Bộ ảnh cho website</h1>
<p class="lead">31 ảnh: banner trang chủ, bản điện thoại, danh mục, thẻ sản phẩm, banner trang con, dải kêu gọi, ảnh chia sẻ, icon và nút nổi. Ảnh nền là ảnh thật tại xưởng; hotline 0398 431 300.</p></div></div></header>
<nav class="toc">{toc}</nav>{secs}
<div class="note card"><h4>Cần bổ sung trước khi đưa lên web</h4><p class="cap">Thẻ sản phẩm đang dùng hình minh hoạ – thay bằng ảnh chụp sản phẩm thật. Quy cách vỏ taco còn để [Cần điền]. File gốc SVG + PNG nằm ở plugins/design/assets/diem-chi/website/.</p></div></body></html>"""
open(f"{O}/website-anh.html","w").write(html)
import json; json.dump(files,open(f"{O}/files.json","w"))
print(len(files))

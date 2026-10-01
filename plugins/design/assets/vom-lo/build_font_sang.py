"""Trang so sánh 5 font có chân sang cho hướng "Vòm Lò". Chạy: python3 build_font_sang.py OUT.html"""
import base64
import os
import sys

import logo_vom as L
import make_font_serif as S

HERE = os.path.dirname(os.path.abspath(__file__))
FS = os.path.join(HERE, "fonts-serif")
BV = os.path.join(HERE, "be-vietnam-pro", "files")
ORDER = ["Playfair", "Cormorant", "Prata", "NotoDisplay", "Serif"]
TEN = {"Playfair": "Sang tạp chí", "Cormorant": "Thanh mảnh cổ điển", "Prata": "Biển hiệu châu Âu", "NotoDisplay": "Sắc gọn hiện đại", "Serif": "Mềm ấm thủ công"}


def b64(p, mime="font/woff2"):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = [f"@font-face{{font-family:'AT {n}';font-display:swap;src:url({b64(os.path.join(FS, f'AnTam{n}-Vom.woff2'))}) format('woff2')}}" for n in ORDER]
    for w in (400, 600):
        for sub in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(BV, f'be-vietnam-pro-{sub}-{w}-normal.woff2'))}) format('woff2')}}")
    return "\n".join(out)


def art(n):
    L.SERIF = os.path.join(FS, f"AnTam{n}-Vom.ttf"); L._fonts.cache_clear()
    res = []
    for fg, bg in ((L.CH, None), (L.KEM, None)):
        g, w = L.wordmark_lo(150, fg, L.BO)
        tg, _ = L.text("ẨM THỰC  ·  TẬN TÂM", 22, "sans", .32, 0, 62, fg, "middle")
        res.append(L.svg((-w / 2 - 30, -175, w + 60, 260), g + tg, f"Logo An Tâm font {n}"))
    up, w = L.wordmark_text("ẨM THỰC AN TÂM", 56, L.CH2, L.BO, 0, 70, track=.12)
    res.append(L.svg((-10, 0, w + 20, 96), up, "Ẩm Thực An Tâm chữ hoa"))
    return res


CSS = """
:root{--ch:#B5121B;--ch2:#7D0A10;--kem:#FFF4E8;--bo:#FFD37A;--den:#1B1B1B}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--kem);color:var(--den);font:16px/1.55 'Be Vietnam Pro',system-ui,sans-serif}
header{max-width:1180px;margin:0 auto;padding:64px 20px 24px}
header .k{font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--ch)}
header h1{font:400 clamp(44px,7vw,92px)/1 'AT Playfair';color:var(--ch2);margin:14px 0 18px}
header p{max-width:680px}
.bar{position:sticky;top:0;z-index:4;background:var(--ch2);color:var(--kem);padding:10px 20px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.bar label{font-size:12px;letter-spacing:.2em;text-transform:uppercase}
.bar input{flex:1;min-width:0;font:500 17px 'Be Vietnam Pro';border:0;border-radius:999px;padding:9px 14px}
.o{max-width:1180px;margin:28px auto;padding:0 20px}
.c{background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 1px 0 #0000000d}
.top{display:grid;grid-template-columns:1fr 1fr}
.top>div{padding:28px}.top>div:nth-child(2){background:var(--ch2)}
.top svg,.up svg{display:block;width:100%;height:auto}
.body{padding:26px 28px 30px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:28px;align-items:start}
.n{font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--ch)}
.n b{font-weight:600}
h2{font-size:30px;line-height:1.15;margin:6px 0 8px;font-weight:400;color:var(--ch2)}
.up{margin-top:14px;max-width:520px}
.para{font-size:22px;line-height:1.45;color:var(--den)}
.para .live{font-size:44px;line-height:1.15;color:var(--ch);display:block;margin-bottom:10px;overflow-wrap:anywhere}
.end{max-width:1180px;margin:40px auto 72px;padding:0 20px;text-align:center}
.end h3{font:400 clamp(30px,4vw,48px)/1.1 'AT Playfair';color:var(--ch2)}
@media (max-width:760px){.top,.body{grid-template-columns:minmax(0,1fr)}.top>div,.body{padding:20px}}
"""


def page():
    cards = []
    for i, n in enumerate(ORDER, 1):
        a, b, up = art(n)
        fam = f"'AT {n}'"
        cards.append(f"""<section class="o" id="f{i}"><div class="c">
<div class="top"><div>{a}</div><div>{b}</div></div>
<div class="body"><div><div class="n"><b>Phương án {i:02d}</b> · {TEN[n]}</div><h2 style="font-family:{fam}">An Tâm {n}</h2>
<p>{S.BASES[n][2]}. Dấu mũ â ê ô là vòm lò mảnh có hạt than; trong logo, vòm phóng to thành cửa lò ôm lấy chữ a.</p>
<div class="up">{up}</div></div>
<div class="para" style="font-family:{fam}"><span class="live">Ẩm Thực An Tâm</span>Bánh tortilla mềm, taco giòn và doner kebab — nướng mỗi sáng tại xưởng, giao tận bếp nhà hàng và cửa hàng. Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm.</div></div>
</div></section>""")
    js = """<script>
const i=document.getElementById('t'),L=[...document.querySelectorAll('.live')];
function r(){const v=i.value.trim()||'Ẩm Thực An Tâm';L.forEach(e=>e.textContent=v);try{localStorage.setItem('fs-t',i.value)}catch(e){}}
try{i.value=localStorage.getItem('fs-t')||''}catch(e){}i.addEventListener('input',r);r();
</script>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vòm Lò An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header><div class="k">Hướng Vòm Lò · Tin cậy · Tinh tế · Ấm áp</div><h1>Năm kiểu chữ sang<br>cho An Tâm</h1>
<p>Giữ bảng màu cherry, kem, vàng bơ. Chữ có chân để toát lên sự tin cậy và cao cấp; nét riêng là vòm lò nướng có hạt than hồng thay cho dấu mũ. Trong logo, vòm lớn thành cửa lò ôm lấy chữ a — chiếc bánh đang nướng.</p></header>
<div class="bar"><label for="t">Gõ thử</label><input id="t" placeholder="Ẩm Thực An Tâm" maxlength="40"></div>
{''.join(cards)}
<div class="end"><h3>Chọn một số từ 01 đến 05</h3><p>Sau khi chọn, mình hoàn thiện logo, con dấu, bao bì, danh thiếp, biển hiệu và đưa vào Figma.</p></div>
{js}</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

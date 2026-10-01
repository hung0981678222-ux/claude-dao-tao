"""Trang so sánh 6 font mới của An Tâm (dấu mũ là chiếc bánh). Chạy: python3 build_font_moi.py OUT.html"""
import base64
import os
import sys

import bac_thang as BT
import make_fonts_multi as M

HERE = os.path.dirname(os.path.abspath(__file__))
FM = os.path.join(HERE, "fonts-moi")
CH, CH2, KEM, HONG, BO, DEN = "#B5121B", "#7D0A10", "#FFF4E8", "#F7CFC6", "#FFD37A", "#1B1B1B"

# tên: (nền, chữ, điểm nhấn, gợi ý dùng)
MOOD = {
    "Bricolage": (CH, KEM, BO, "Logo, bao bì, mạng xã hội"),
    "Fraunces": (KEM, CH, CH2, "Thực đơn, catalogue, hồ sơ năng lực"),
    "Anton": (BO, DEN, CH, "Biển hiệu, poster, chữ bậc thang"),
    "Baloo": (HONG, CH, CH2, "Ăn vặt, combo, khuyến mãi"),
    "Grandstander": (DEN, BO, HONG, "Story, sticker, ly và túi"),
    "Dela": (CH2, HONG, BO, "Tiêu đề lớn, băng rôn, xe giao hàng"),
}


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    return "\n".join(f"@font-face{{font-family:'An Tam {n}';font-display:swap;src:url({b64(os.path.join(FM, f'{ps}.woff2'), 'font/woff2')}) format('woff2')}}"
                     for n, (_, ps, _) in M.FONTS.items())


def stair(n, fg, side, hi):
    s = BT.stairs(["ẩm thực", "an tâm", "tận tâm"], fg, side=side, hi=hi, hi_idx=(1,), style=os.path.join(FM, f"{M.FONTS[n][1]}.ttf"), label=f"Chữ bậc thang font An Tam {n}")
    return s


CSS = """
:root{--ch:#B5121B;--kem:#FFF4E8;--den:#1B1B1B}
*{box-sizing:border-box;margin:0}
html{overflow-x:clip}
body{background:var(--kem);color:var(--den);font:16px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;overflow-x:clip}
.top{padding:56px 24px 28px;max-width:1240px;margin:0 auto}
.top h1{font:400 clamp(56px,10vw,140px)/.9 'An Tam Bricolage';color:var(--ch);letter-spacing:-.03em}
.top p{max-width:640px;margin-top:18px;font-size:18px}
.bar{position:sticky;top:0;z-index:5;background:var(--den);color:var(--kem);padding:12px 24px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.bar label{font-weight:700;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
.bar input[type=text]{flex:1;min-width:0;font:600 18px system-ui;padding:10px 14px;border-radius:999px;border:0;background:#fff;color:var(--den)}
.bar button{font:700 14px system-ui;border:0;border-radius:999px;padding:10px 16px;background:var(--ch);color:#fff;cursor:pointer}
.jump{display:flex;gap:8px;flex-wrap:wrap;width:100%}
.jump a{color:var(--kem);font-size:13px;text-decoration:none;border:1px solid #ffffff44;border-radius:999px;padding:4px 12px}
.jump a:hover{background:#ffffff22}
.f{padding:64px 24px;color:var(--fg);background:var(--bg)}
.in{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:40px;align-items:center}
.num{font:700 13px/1 system-ui;letter-spacing:.16em;text-transform:uppercase;opacity:.8}
.big{font-size:calc(var(--k,1)*clamp(80px,15vw,220px));white-space:nowrap;line-height:.9;letter-spacing:-.02em;margin:14px 0 10px;}
.big span{color:var(--ac)}
.cap{font-size:clamp(30px,4.4vw,58px);line-height:1;color:var(--ac)}
.sen{font-size:clamp(20px,2.4vw,28px);line-height:1.3;margin-top:22px}
.abc{font-size:22px;line-height:1.35;margin-top:18px;opacity:.85;overflow-wrap:anywhere}
.meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}
.meta b{font:600 13px system-ui;border:1.5px solid currentColor;border-radius:999px;padding:6px 12px}
.st{border-radius:28px;background:#ffffff14;padding:18px}
.st>svg{display:block;width:100%;height:auto}
.end{padding:56px 24px 72px;text-align:center}
.end h2{font:400 clamp(34px,5vw,60px)/1 'An Tam Bricolage';color:var(--ch)}
.end p{max-width:620px;margin:14px auto 0}
@media (max-width:820px){.in{grid-template-columns:minmax(0,1fr)}.f{padding:48px 16px}.top{padding:40px 16px 20px}.bar{padding:10px 16px}}
"""


def card(i, n):
    bg, fg, ac, use = MOOD[n]
    fam = f"'An Tam {n}'"
    side = BT.shade(fg if fg != KEM else "#E8D9C6", .8)
    return f"""<section class="f" id="f-{n.lower()}" style="--bg:{bg};--fg:{fg};--ac:{ac};--k:{ {"Dela": .62, "Grandstander": .85, "Baloo": .95}.get(n, 1)}">
<div class="in"><div style="font-family:{fam}">
<div class="num" style="font-family:system-ui">Phương án {i:02d} · An Tâm {n}</div>
<div class="big t-live">an t<span>â</span>m</div>
<div class="cap">ĂN LÀ AN TÂM</div>
<div class="sen">Bánh tortilla mềm, taco giòn, doner kebab đậm vị — giao tận bếp mỗi sáng.</div>
<div class="abc">ÂÊÔ âêô ấầẩẫậ ếềểễệ ốồổỗộ · Ư Ơ Đ · 0348.635.222</div>
<div class="meta" style="font-family:system-ui"><b>{M.FONTS[n][2]}</b><b>Hợp: {use}</b></div>
</div><div class="st">{stair(n, fg, side, ac)}</div></div></section>"""


def page():
    names = list(M.FONTS)
    jump = "".join(f'<a href="#f-{n.lower()}">{i + 1:02d} {n}</a>' for i, n in enumerate(names))
    cards = "\n".join(card(i + 1, n) for i, n in enumerate(names))
    js = """<script>
const inp=document.getElementById('t'),bigs=[...document.querySelectorAll('.t-live')],orig=bigs.map(b=>b.innerHTML);
function esc(s){return s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function run(){const v=inp.value.trim();bigs.forEach((b,i)=>b.innerHTML=v?esc(v):orig[i]);try{localStorage.setItem('fm-t',inp.value)}catch(e){}}
try{inp.value=localStorage.getItem('fm-t')||''}catch(e){}
inp.addEventListener('input',run);document.getElementById('r').onclick=()=>{inp.value='';run()};run();
</script>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Font Mới An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header class="top"><h1>6 font mới<br>cho an tâm</h1>
<p>Sáu khung chữ khác hẳn nhau, cùng một nét riêng: mọi dấu mũ (â ê ô) là chiếc bánh vòm có đốm nướng. Đủ tiếng Việt, dùng được cho logo, bao bì, biển hiệu và chữ bậc thang. Gõ thử chữ của bạn ở thanh bên dưới.</p></header>
<div class="bar"><label for="t">Gõ thử</label><input id="t" type="text" placeholder="an tâm" maxlength="40"><button id="r" type="button">Về mặc định</button><nav class="jump">{jump}</nav></div>
{cards}
<footer class="end"><h2>Chọn một số từ 01 đến 06</h2><p>Sau khi chọn, toàn bộ logo, chữ bậc thang, bộ nhận diện và trang trình chiếu sẽ dựng lại bằng font đó. Các font dựng từ khung chữ mã nguồn mở SIL OFL, đã đổi tên riêng cho An Tâm.</p></footer>
{js}</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

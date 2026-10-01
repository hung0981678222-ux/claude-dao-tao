"""Trang hướng "Nón Lá": 4 phương án chữ nét đậm, dấu mũ là nón lá. Chạy: python3 build_non.py OUT.html"""
import base64
import os
import sys

import logo_non as N
import make_font_non as F

HERE = os.path.dirname(os.path.abspath(__file__))
FN = os.path.join(HERE, "fonts-non")
BV = os.path.join(HERE, "be-vietnam-pro", "files")
ORDER = ["BeVietnam", "Phudu", "Anton", "Dela"]
TEN = {"BeVietnam": "Chữ Việt hiện đại", "Phudu": "Chữ kẻ biển hiệu", "Anton": "Biển hiệu Sài Gòn xưa", "Dela": "Siêu đậm, nổi từ xa"}


def b64(p, mime="font/woff2"):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = [f"@font-face{{font-family:'ATN {n}';font-display:swap;src:url({b64(os.path.join(FN, f'AnTam{n}-Non.woff2'))}) format('woff2')}}" for n in ORDER]
    for w in (400, 700):
        for sub in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(BV, f'be-vietnam-pro-{sub}-{w}-normal.woff2'))}) format('woff2')}}")
    return "\n".join(out)


CSS = """
:root{--ch:#B5121B;--ch2:#7D0A10;--kem:#FFF4E8;--bo:#FFD37A;--den:#1B1B1B}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--kem);color:var(--den);font:16px/1.55 'Be Vietnam Pro',system-ui,sans-serif}
header{background:var(--ch);color:var(--kem);padding:56px 20px 40px}
header>div{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:32px;align-items:center}
header .k{font-weight:700;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--bo)}
header h1{font:400 clamp(48px,8vw,108px)/.95 'ATN BeVietnam';margin:14px 0 16px;letter-spacing:-.01em}
header p{max-width:620px}
header svg{width:100%;height:auto;display:block}
.bar{position:sticky;top:0;z-index:4;background:var(--den);color:var(--kem);padding:10px 20px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.bar label{font-weight:700;font-size:12px;letter-spacing:.2em;text-transform:uppercase}
.bar input{flex:1;min-width:0;font:500 17px 'Be Vietnam Pro';border:0;border-radius:999px;padding:9px 14px}
.o{max-width:1180px;margin:28px auto;padding:0 20px}
.c{background:#fff;border-radius:28px;overflow:hidden}
.hd{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:baseline;padding:24px 28px 0}
.n{font-weight:700;font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--ch)}
.hd p{font-size:14px;color:#555}
.logos{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,.8fr) minmax(0,.7fr);gap:18px;padding:22px 28px;align-items:center}
.logos svg,.wide svg{display:block;width:100%;height:auto}
.wide{padding:0 28px 22px;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:18px;align-items:center}
.dark{background:var(--ch2);border-radius:18px;padding:18px}
.sp{padding:22px 28px 28px;border-top:1px solid #eee}
.sp .live{font-size:clamp(48px,7vw,88px);line-height:1.15;color:var(--ch);display:block;overflow-wrap:anywhere}
.sp .t{font-size:24px;line-height:1.45;margin-top:10px}
.end{max-width:1180px;margin:40px auto 72px;padding:0 20px;text-align:center}
.end h3{font:400 clamp(30px,4vw,52px)/1.1 'ATN BeVietnam';color:var(--ch)}
@media (max-width:760px){header>div,.wide{grid-template-columns:minmax(0,1fr)}.logos{grid-template-columns:1fr 1fr}.logos>div:first-child{grid-column:1/-1}.logos,.wide,.sp{padding-left:18px;padding-right:18px}.hd{padding:20px 18px 0}}
"""


def card(i, n):
    N.use(n); fam = f"'ATN {n}'"
    return f"""<section class="o" id="p{i}"><div class="c">
<div class="hd"><div class="n">Phương án {i:02d} · {TEN[n]}</div><p>{F.BASES[n][1]}</p></div>
<div class="logos"><div>{N.bien_hieu()}</div><div>{N.an_trien()}</div><div>{N.bieu_tuong()}</div></div>
<div class="wide"><div>{N.ngang()}</div><div class="dark">{N.ngang(N.KEM, '#4A0508', N.KEM)}</div></div>
<div class="sp" style="font-family:{fam}"><span class="live">ẨM THỰC AN TÂM</span>
<div class="t">Bánh tortilla mềm, taco giòn, doner kebab đậm vị — nướng mỗi sáng, giao tận bếp. Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm.</div></div>
</div></section>"""


def page():
    N.use("BeVietnam")
    hero = N.bien_hieu(N.KEM, '#4A0508', N.CH, N.BO)
    cards = "".join(card(i, n) for i, n in enumerate(ORDER, 1))
    js = """<script>
const i=document.getElementById('t'),L=[...document.querySelectorAll('.live')];
function r(){const v=i.value.trim()||'ẨM THỰC AN TÂM';L.forEach(e=>e.textContent=v);try{localStorage.setItem('non-t',i.value)}catch(e){}}
try{i.value=localStorage.getItem('non-t')||''}catch(e){}i.addEventListener('input',r);r();
</script>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nón Lá An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header><div><div><div class="k">Hướng Nón Lá · Nét đậm · Cá tính Việt</div><h1>DẤU MŨ<br>LÀ NÓN LÁ</h1>
<p>Chữ nét đậm như biển hiệu kẻ tay, đổ bóng khối. Mọi dấu mũ â ê ô là chiếc nón lá có vành — nét Việt nằm ngay trong con chữ tiếng Việt. Đi kèm ấn triện son đỏ và biểu tượng nón lá trước chiếc bánh tròn. Giữ bảng màu cherry, kem, vàng bơ.</p></div>
<div>{hero}</div></div></header>
<div class="bar"><label for="t">Gõ thử</label><input id="t" placeholder="ẨM THỰC AN TÂM" maxlength="40"></div>
{cards}
<div class="end"><h3>CHỌN 01 – 04</h3><p>Chọn xong, mình hoàn thiện bao bì, túi giao hàng, danh thiếp, biển hiệu và đưa vào Figma.</p></div>
{js}</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

"""Phương án 04 Tròn Bánh thêm nét – trang so sánh biến thể. Chạy: python3 build_tron.py OUT.html"""
import base64
import os
import sys

import logo_van as V
import make_font_tron as FT

HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["Goc", "Van", "Dut", "Cham", "Du"]
TEN = {"Goc": "Bản gốc 04", "Van": "Vân Lõm", "Dut": "Vân Đứt", "Cham": "Chấm Vân", "Du": "Đủ Nét"}
MD = os.path.join(HERE, "fonts-van", "AnTamVan-Medium.ttf")


def b64(p, mime="font/woff2"):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def faces():
    out = [f"@font-face{{font-family:'AT {n}';font-display:swap;src:url({b64(os.path.join(HERE, 'fonts-tron', f'AnTamTron{n}.woff2'))}) format('woff2')}}" for n in ORDER]
    out.append(f"@font-face{{font-family:'An Tam Van';font-weight:500;font-display:swap;src:url({b64(os.path.join(HERE, 'fonts-van', 'AnTamVan-Medium.woff2'))}) format('woff2')}}")
    out.append(f"@font-face{{font-family:'An Tam Van';font-weight:800;font-display:swap;src:url({b64(os.path.join(HERE, 'fonts-van', 'AnTamVan-ExtraBold.woff2'))}) format('woff2')}}")
    return "\n".join(out)


def use(n):
    V.F["xb"] = os.path.join(HERE, "fonts-tron", f"AnTamTron{n}.ttf")
    V.F["md"] = os.path.join(HERE, "fonts-tron", "AnTamTronCham.ttf")
    V._f.cache_clear()


CSS = """
:root{--do:#D2141E;--do2:#8F0D14;--kem:#FFF6EA;--giay:#F6EEE2;--muc:#231716;--ngo:#F5B82E}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--giay);color:var(--muc);font:500 16px/1.6 'An Tam Van',system-ui,sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
header{background:var(--do);color:var(--kem)}
header .in{max-width:1200px;margin:0 auto;padding:56px 20px 44px;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:32px;align-items:center}
.k{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--ngo)}
h1{font-weight:800;font-size:clamp(40px,6vw,80px);line-height:1.05;letter-spacing:-.02em;margin:12px 0 14px}
header p{max-width:620px;color:#FFE1DE}
.bar{position:sticky;top:0;z-index:4;background:var(--muc);color:var(--kem);padding:10px 20px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.bar label{font-weight:800;font-size:12px;letter-spacing:.2em;text-transform:uppercase}
.bar input{flex:1;min-width:0;font:500 17px 'An Tam Van';border:0;border-radius:999px;padding:9px 14px}
.bar a{color:var(--kem);font-size:13px;text-decoration:none;border:1px solid #ffffff44;border-radius:999px;padding:4px 12px}
.o{max-width:1200px;margin:28px auto;padding:0 20px}
.c{background:#fff;border-radius:6px;overflow:hidden}
.hd{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;align-items:baseline;padding:24px 28px 0}
.n{font-weight:800;font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--do)}
.hd p{font-size:14px;color:#6b5a55;max-width:640px}
.logos{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;padding:20px 28px}
.logos .dk{background:var(--do);padding:14px;border-radius:4px}
.sp{padding:6px 28px 28px;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,.5fr);gap:20px;align-items:center}
.sp .live{font-size:clamp(46px,7vw,92px);line-height:1.12;color:var(--do);overflow-wrap:anywhere}
.sp .t{font-size:22px;line-height:1.45;margin-top:8px}
.sp .gl{font-size:150px;line-height:1.15;color:var(--do);text-align:center}
.end{max-width:1200px;margin:40px auto 72px;padding:0 20px;text-align:center}
.end h2{font-weight:800;font-size:clamp(30px,4vw,48px);color:var(--do)}
@media (max-width:820px){header .in,.logos,.sp{grid-template-columns:minmax(0,1fr)}.hd,.logos,.sp{padding-left:18px;padding-right:18px}.sp .gl{font-size:110px}}
"""


def card(i, n):
    use(n); fam = f"'AT {n}'"
    body_fam = "'AT Cham'"
    return f"""<section class="o" id="f{i}"><div class="c">
<div class="hd"><div class="n">Phương án {i:02d} · {TEN[n]}</div><p>{FT.VARIANTS[n][2]}.</p></div>
<div class="logos"><div>{V.logo_ngang()}</div><div class="dk">{V.logo_ngang(V.KEM, V.KEM)}</div></div>
<div class="sp"><div><div class="live" style="font-family:{fam}">Mỗi mẻ bánh, một lời cam kết</div>
<div class="t" style="font-family:{body_fam}">Bánh tortilla, vỏ taco và thịt doner giao tận bếp quán ăn, nhà hàng tại TP.HCM. Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm. ấầẩẫậ ốồổỗộ</div></div>
<div class="gl" style="font-family:{fam}">â</div></div></div></section>"""


def page():
    use("Dut"); hero = V.logo_dung()
    cards = "".join(card(i, n) for i, n in enumerate(ORDER, 1))
    jump = "".join(f'<a href="#f{i}">{i:02d} {TEN[n]}</a>' for i, n in enumerate(ORDER, 1))
    js = """<script>
const i=document.getElementById('t'),L=[...document.querySelectorAll('.live')];
function r(){const v=i.value.trim()||'Mỗi mẻ bánh, một lời cam kết';L.forEach(e=>e.textContent=v);try{localStorage.setItem('tron-t',i.value)}catch(e){}}
try{i.value=localStorage.getItem('tron-t')||''}catch(e){}i.addEventListener('input',r);r();
</script>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tròn Bánh Thêm Nét</title><style>{faces()}\n{CSS}</style></head><body>
<header><div class="in"><div><div class="k">Điểm Chỉ · Phương án 04 Tròn Bánh</div><h1>Thêm nét riêng cho chữ</h1>
<p>Giữ khung chữ tròn đầy của phương án 04 và dấu mũ vân tay, thêm các nét lấy từ vân tay: một đường vân lõm chạy trong nét chữ (liền hoặc đứt quãng), và dấu chấm thành vòng xoáy nhỏ. Đoạn văn mẫu dùng bản Chấm Vân – bản hợp nhất cho chữ nhỏ.</p></div>
<div style="background:var(--kem);padding:20px;border-radius:6px">{hero}</div></div></header>
<div class="bar"><label for="t">Gõ thử</label><input id="t" placeholder="Mỗi mẻ bánh, một lời cam kết" maxlength="50">{jump}</div>
{cards}
<div class="end"><h2>Bạn chọn biến thể nào?</h2><p>Gợi ý ghép: Vân Đứt hoặc Vân Lõm cho logo và tiêu đề lớn, Chấm Vân cho nội dung, bao bì, bảng giá.</p></div>
{js}</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

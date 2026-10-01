"""An Tâm bản cao cấp: đỏ rượu, kem ngà, vàng đồng ép kim; chữ Fraunces mảnh, nhiều khoảng trắng.
Giữ logo "an tâm" có bánh gập đôi và linh vật Bé Cuộn. Chạy: python3 sang.py OUT.html"""
import base64
import os
import sys

import build_nl2  # noqa: F401
import logo2 as L2
from mascot4 import be_cuon

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
RUOU, RUOU2, DO, NGA, NGA2, DONG, MUC = "#6B0D12", "#3D0609", "#C8161D", "#F5EEE3", "#EAE0D0", "#C9A26A", "#1A1210"
FOIL = "url(#foil)"
RG = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
}


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def ill(n):
    return b64(f"{MH}/{n}.svg", "image/svg+xml")


def fontfaces():
    out = []
    for sub, rg in RG.items():
        for w in (300, 500, 900):
            out.append(("Fraunces AT", w, os.path.join(SCR, f"nl/fr50-{sub}-{w}.woff2"), rg))
        for w in (300, 400, 600):
            out.append(("Be Vietnam Pro", w, os.path.join(SCR, f"cc/be-vietnam-pro/files/be-vietnam-pro-{sub}-{w}-normal.woff2"), rg))
    return "\n".join(f"@font-face{{font-family:'{n}';font-weight:{w};font-display:swap;src:url({b64(p, 'font/woff2')}) format('woff2');unicode-range:{rg}}}" for n, w, p, rg in out)


def wm(fg, cut, sub_fg=None, top=True, sub=True, cls="lg", w=None, h=None, x=None, y=None):
    s = L2.wordmark(fg, cut, sub_fg, top=top, sub=sub)
    if w is not None and cls == "lg":
        cls = "x"
    attrs = f'class="{cls}"' + "".join(f' {k}="{v}"' for k, v in (("x", x), ("y", y), ("width", w), ("height", h)) if v is not None)
    return s.replace("<svg ", f"<svg {attrs} ", 1)


def mk(fg, cut, bg, cls="lg", **kw):
    s = L2.mark(fg, cut, bg)
    if kw and cls == "lg":
        cls = "x"
    attrs = f'class="{cls}"' + "".join(f' {k}="{v}"' for k, v in kw.items())
    return s.replace("<svg ", f"<svg {attrs} ", 1)


def be_line(color=DONG, sw=4, cls="lg"):
    """Bé Cuộn vẽ nét mảnh một màu, để ép kim lên bao bì."""
    let = "M74,112 " + " ".join(f"Q{80 + i * 13},{88 - (i % 2) * 10} {87 + i * 13},{104 - (i % 3) * 4}" for i in range(11))
    return (f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="40 50 220 310" role="img" aria-label="Bé Cuộn nét mảnh">'
            f'<g fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M72,112 V300 A78,26 0 0 0 228,300 V112"/><ellipse cx="150" cy="112" rx="78" ry="24"/>'
            f'<path d="{let}"/><circle cx="112" cy="92" r="9"/><circle cx="150" cy="80" r="10"/><circle cx="188" cy="90" r="9"/>'
            f'<path d="M72,236 Q150,262 228,236"/><path d="M134,200 Q150,214 166,200"/>'
            f'<path d="M150,262 v20 M138,272 h24" opacity=".0"/></g>'
            f'<circle cx="124" cy="176" r="7" fill="{color}"/><circle cx="176" cy="176" r="7" fill="{color}"/>'
            f'<path d="M100,340 h30 M170,340 h30" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/></svg>')


CSS = """
/* Bố cục: biên tập kiểu tạp chí, nền kem ngà và đỏ rượu, ép kim vàng đồng; chữ có chân mảnh, nhiều khoảng trắng. */
:root{--ruou:#6B0D12;--ruou2:#3D0609;--do:#C8161D;--nga:#F5EEE3;--nga2:#EAE0D0;--dong:#C9A26A;--muc:#1A1210;--xam:#6E625B;--line:#DCCFBC;
--ten:'Fraunces AT',Georgia,serif;--noi:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--nga);color:var(--muc);font:300 17px/1.7 var(--noi);-webkit-font-smoothing:antialiased}
svg{max-width:100%}svg.lg{display:block;width:100%;height:auto}
.w{max-width:1240px;margin:0 auto;padding-inline:48px}
section{padding-block:128px}
.lab{font:600 11px/1 var(--noi);letter-spacing:.32em;text-transform:uppercase;color:var(--ruou)}
.dark .lab{color:var(--dong)}
.row{display:grid;grid-template-columns:4fr 8fr;gap:48px;align-items:start}
h2{font:300 clamp(40px,5vw,72px)/1.04 var(--ten);letter-spacing:-.02em;text-wrap:balance}
h2 em{font-style:normal;font-weight:500;color:var(--ruou)}
.dark h2 em{color:var(--dong)}
.lead{font-size:18px;max-width:52ch;margin-top:20px;color:var(--xam)}
.dark{background:var(--ruou2);color:var(--nga)}.dark .lead{color:rgba(245,238,227,.7)}
.rule{height:1px;background:var(--line);margin-block:28px}

/* đầu trang */
.hero{background:radial-gradient(120% 90% at 50% 0%,#8A1218 0%,#5A0A0E 45%,#2A0507 100%);color:var(--nga);text-align:center;overflow:hidden;position:relative}
.hero .top{display:flex;justify-content:space-between;padding:28px 48px;font:600 11px/1 var(--noi);letter-spacing:.32em;color:rgba(245,238,227,.7)}
.hero .lgw{width:min(78vw,620px);margin:72px auto 0}
.hero h1{font:300 clamp(30px,3.6vw,48px)/1.2 var(--ten);margin-top:36px;letter-spacing:-.01em}
.hero h1 em{font-style:normal;font-weight:500;color:var(--dong)}
.stage{position:relative;width:min(70vw,420px);margin:40px auto 0;padding-bottom:40px}
.stage::before{content:"";position:absolute;left:50%;top:-30%;width:160%;height:140%;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(255,214,150,.28),transparent);pointer-events:none}
.stage .bc{position:relative;width:62%;margin:0 auto;display:block;height:auto}
.stage .ped{position:relative;margin:-18px auto 0;width:86%;height:44px;border-radius:50%;background:radial-gradient(closest-side,#C9A26A,#7A5A2E 70%,transparent 72%);opacity:.55}

/* tinh thần */
.mani{font:300 clamp(28px,3.4vw,46px)/1.32 var(--ten);letter-spacing:-.01em;max-width:24ch}
.mani em{font-style:normal;font-weight:500;color:var(--ruou)}
.pill{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:64px;border-top:1px solid var(--line)}
.pill div{padding:22px 24px 0 0}
.pill b{display:block;font:500 22px/1.2 var(--ten)}
.pill p{font-size:15px;color:var(--xam);margin-top:6px}

/* logo */
.logos{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:64px}
.lt{aspect-ratio:3/2;display:grid;place-items:center;padding:12%;position:relative}
.lt .cap{position:absolute;left:22px;bottom:18px;font:600 10px/1 var(--noi);letter-spacing:.28em;text-transform:uppercase;opacity:.6}
.emboss svg path{filter:drop-shadow(1px 1px 0 rgba(255,255,255,.9)) drop-shadow(-1px -1px 0 rgba(120,90,60,.25))}

/* màu */
.sw{display:grid;grid-template-columns:3fr 2fr 1.2fr 1fr 1fr;height:340px;margin-top:64px}
.sw div{padding:22px;display:flex;flex-direction:column;justify-content:flex-end;font:400 12px/1.6 var(--noi);letter-spacing:.06em}
.sw b{font:500 20px/1.2 var(--ten);letter-spacing:0;display:block;margin-bottom:4px}

/* chữ */
.ty{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:64px;align-items:end}
.ty .g{font:300 200px/.9 var(--ten);letter-spacing:-.04em;color:var(--ruou)}
.ty .g span{font-weight:900}
.ty dl{display:grid;grid-template-columns:auto 1fr;gap:14px 28px;border-top:1px solid var(--line);padding-top:22px}
.ty dt{font:600 11px/1.8 var(--noi);letter-spacing:.28em;text-transform:uppercase;color:var(--ruou)}
.ty dd{font-size:15px;color:var(--xam)}

/* linh vật */
.mas{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-top:64px}
.mas > div{aspect-ratio:3/4;display:grid;place-items:center;padding:14%;position:relative}
.mas .cap{position:absolute;left:20px;bottom:16px;font:600 10px/1 var(--noi);letter-spacing:.28em;text-transform:uppercase;opacity:.65}

/* bao bì */
.pk{display:grid;grid-template-columns:repeat(12,1fr);gap:20px;margin-top:64px}
.pk > div{position:relative;overflow:hidden}
.pk .cap{position:absolute;left:20px;top:18px;font:600 10px/1 var(--noi);letter-spacing:.28em;text-transform:uppercase;opacity:.7;z-index:2}
.c7{grid-column:span 7}.c5{grid-column:span 5}.c4{grid-column:span 4}.c8{grid-column:span 8}.c6{grid-column:span 6}.c12{grid-column:span 12}
svg.mkp{display:block;width:100%;height:auto}

footer{background:var(--muc);color:var(--nga);padding-block:72px 48px}
footer .w{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end}
footer .lg{width:240px}
footer p{font-size:13px;opacity:.6;max-width:60ch;margin-top:24px}
footer .ct{font:300 20px/1.6 var(--ten);text-align:right}
@media (prefers-reduced-motion:no-preference){.stage .nhun{animation:nh 3.2s ease-in-out infinite}@keyframes nh{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
 .stage .vay{animation:vy 1.8s ease-in-out infinite}@keyframes vy{0%,100%{transform:rotate(0)}50%{transform:rotate(-14deg)}}}
@media (max-width:900px){.w{padding-inline:20px}section{padding-block:80px}.hero .top{padding:20px}
 .row,.ty{grid-template-columns:1fr;gap:20px}.pill,.logos,.mas{grid-template-columns:1fr}
 .sw{grid-template-columns:1fr 1fr;height:auto}.sw div{min-height:140px}.sw div:first-child{grid-column:1/-1}
 .ty .g{font-size:120px}.c7,.c5,.c4,.c8,.c6,.c12{grid-column:1/-1}
 footer .w{grid-template-columns:1fr}footer .ct{text-align:left}}
"""


def gift_box():
    return f"""<svg class="mkp" viewBox="0 0 700 520" role="img" aria-label="Hộp quà doanh nghiệp">
<rect width="700" height="520" fill="#E7DCCB"/>
<ellipse cx="350" cy="452" rx="260" ry="22" fill="#000" opacity=".22" filter="url(#mo)"/>
<path d="M130,220 L350,160 L570,220 L570,430 L350,490 L130,430 Z" fill="{RUOU}"/>
<path d="M130,220 L350,280 L570,220 L350,160 Z" fill="#7E1117"/>
<path d="M350,280 V490 L570,430 V220 Z" fill="#4E080C"/>
<path d="M240,190 L460,250 V280 L240,220 Z M460,190 L240,250 V280 L460,220 Z" fill="{FOIL}" opacity=".95"/>
<path d="M300,175 L410,205" stroke="{FOIL}" stroke-width="14"/>
<path d="M350,280 V490" stroke="#2B0406" stroke-width="2" opacity=".5"/>
<g transform="translate(170 300) skewY(15.3)">{wm(FOIL, RUOU, cls="x", w=150, h=62)}</g>
<g transform="translate(400 330) skewY(-15.3)">{be_line(DONG, 4).replace('class="lg"', 'width="80" height="110"', 1)}</g>
</svg>"""


def bag():
    return f"""<svg class="mkp" viewBox="0 0 520 620" role="img" aria-label="Túi giấy cao cấp">
<rect width="520" height="620" fill="{RUOU2}"/>
<ellipse cx="260" cy="560" rx="170" ry="16" fill="#000" opacity=".5" filter="url(#mo)"/>
<path d="M200,170 C200,90 300,90 300,170" fill="none" stroke="{DONG}" stroke-width="5"/>
<path d="M120,160 H380 V560 H120 Z" fill="{NGA}"/>
<path d="M380,160 L420,148 V548 L380,560 Z" fill="{NGA2}"/>
<rect x="120" y="470" width="260" height="90" fill="{RUOU}"/>
<g transform="translate(160 260)">{wm(RUOU, NGA, MUC, w=180, h=74)}</g>
<text x="250" y="520" text-anchor="middle" fill="{DONG}" style="font:600 10px 'Be Vietnam Pro';letter-spacing:.32em">ANTAMFOODS.COM</text>
</svg>"""


def pack():
    return f"""<svg class="mkp" viewBox="0 0 520 620" role="img" aria-label="Gói bánh tortillas">
<rect width="520" height="620" fill="{NGA2}"/>
<ellipse cx="260" cy="568" rx="150" ry="14" fill="#000" opacity=".25" filter="url(#mo)"/>
<path d="M130,80 Q260,66 390,80 L398,560 Q260,574 122,560 Z" fill="{MUC}"/>
<path d="M150,80 L156,560" stroke="#fff" stroke-width="40" opacity=".05"/>
<rect x="170" y="150" width="180" height="250" rx="90" fill="{NGA}"/>
<image href="{ill('banh-tortillas')}" x="175" y="230" width="170" height="170"/>
<g transform="translate(180 168)">{wm(RUOU, NGA, MUC, sub=False, w=160, h=56)}</g>
<text x="260" y="460" text-anchor="middle" fill="{DONG}" style="font:300 30px 'Fraunces AT'">Bánh Tortillas</text>
<text x="260" y="490" text-anchor="middle" fill="rgba(245,238,227,.6)" style="font:600 9px 'Be Vietnam Pro';letter-spacing:.3em">[CẦN ĐIỀN: KHỐI LƯỢNG · HẠN DÙNG]</text>
</svg>"""


def store():
    return f"""<svg class="mkp" viewBox="0 0 1240 560" role="img" aria-label="Mặt tiền cửa hàng">
<defs><linearGradient id="am" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD9A0"/><stop offset="1" stop-color="#C77A32"/></linearGradient></defs>
<rect width="1240" height="560" fill="#140C0A"/>
<rect x="120" y="40" width="1000" height="520" fill="{MUC}"/>
<rect x="120" y="40" width="1000" height="150" fill="#100907"/>
<g transform="translate(470 62)">{wm(FOIL, "#100907", w=300, h=124)}</g>
<path d="M120,190 H1120" stroke="{DONG}" stroke-width="2" opacity=".6"/>
<rect x="170" y="240" width="380" height="320" fill="url(#am)" opacity=".92"/>
<image href="{ill('doner-tru-quay')}" x="250" y="300" width="230" height="230"/>
<rect x="590" y="240" width="140" height="320" fill="#2A1A14"/><path d="M660,240 V560" stroke="{DONG}" stroke-width="1.5"/>
<rect x="770" y="240" width="300" height="320" fill="url(#am)" opacity=".92"/>
<g transform="translate(860 300)">{be_cuon('st', 'cuoi', 'chao').replace('<svg ', '<svg width="130" height="148" ', 1)}</g>
<ellipse cx="620" cy="560" rx="520" ry="26" fill="#FFCF8A" opacity=".12" filter="url(#mo)"/>
</svg>"""


def post():
    return f"""<svg class="mkp" viewBox="0 0 1080 1350" role="img" aria-label="Bài đăng mạng xã hội">
<rect width="1080" height="1350" fill="{NGA}"/>
<g transform="translate(80 90)">{wm(RUOU, NGA, MUC, sub=False, w=260, h=96)}</g>
<text x="80" y="330" fill="{MUC}" style="font:300 92px 'Fraunces AT';letter-spacing:-2px">Bữa nhẹ tử tế</text>
<text x="80" y="430" fill="{RUOU}" style="font:500 92px 'Fraunces AT';letter-spacing:-2px">cho văn phòng.</text>
<circle cx="560" cy="900" r="320" fill="{NGA2}"/>
<ellipse cx="560" cy="1150" rx="260" ry="26" fill="#000" opacity=".12" filter="url(#mo)"/>
<image href="{ill('doner-cuon')}" x="300" y="620" width="520" height="520"/>
<text x="80" y="1290" fill="{MUC}" style="font:600 22px 'Be Vietnam Pro';letter-spacing:6px">ĐẶT QUA 0348.635.222</text>
</svg>"""


def card():
    return f"""<svg class="mkp" viewBox="0 0 700 520" role="img" aria-label="Danh thiếp">
<rect width="700" height="520" fill="#D8CBB6"/>
<g transform="rotate(-6 250 230)"><rect x="70" y="120" width="360" height="216" rx="6" fill="{RUOU}" filter="url(#bong)"/>
<g transform="translate(130 178)">{wm(FOIL, RUOU, w=240, h=100)}</g></g>
<g transform="rotate(4 470 330)"><rect x="300" y="230" width="360" height="216" rx="6" fill="{NGA}" filter="url(#bong)"/>
<g transform="translate(326 254)">{mk(RUOU, NGA, NGA, width=46, height=46)}</g>
<text x="326" y="350" fill="{MUC}" style="font:500 24px 'Fraunces AT'">[Cần điền: Họ tên]</text>
<text x="326" y="374" fill="#6E625B" style="font:300 13px 'Be Vietnam Pro'">[Cần điền: Chức danh]</text>
<path d="M326,394 H634" stroke="{DONG}" stroke-width="1"/>
<text x="326" y="420" fill="{MUC}" style="font:400 12px 'Be Vietnam Pro';letter-spacing:1px">0348.635.222 · antamfoods.com · TP. Hồ Chí Minh</text></g>
</svg>"""


def page():
    defs = (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
            f'<linearGradient id="foil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8C6A3A"/><stop offset=".3" stop-color="#E8CF9A"/>'
            f'<stop offset=".5" stop-color="#A67C45"/><stop offset=".72" stop-color="#F3DDB0"/><stop offset="1" stop-color="#8C6A3A"/></linearGradient>'
            f'<filter id="mo" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>'
            f'<filter id="bong" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="18" stdDeviation="16" flood-opacity=".3"/></filter></defs></svg>')
    return f"""<title>An Tâm Signature</title>
<style>{fontfaces()}
{CSS}</style>
{defs}
<header class="hero">
 <div class="top"><span>ẨM THỰC AN TÂM</span><span>BỘ NHẬN DIỆN · BẢN CAO CẤP</span></div>
 <div class="lgw">{wm(FOIL, "#5A0A0E")}</div>
 <h1>Ăn là <em>an tâm.</em></h1>
 <div class="stage">{be_cuon('hero', 'cuoi', 'chao').replace('<svg ', '<svg class="bc" ', 1)}<div class="ped"></div></div>
</header>

<section><div class="w row">
 <p class="lab">Tinh thần</p>
 <div><p class="mani">Một chiếc bánh cuộn đơn giản, <em>làm cho thật tử tế.</em> Đó là cách An Tâm giữ lời với từng khách hàng.</p>
  <div class="pill"><div><b>Tận tâm</b><p>Chăm từng chiếc bánh như làm cho người nhà.</p></div><div><b>Đúng hẹn</b><p>Giao đúng giờ, đúng số lượng đã hứa.</p></div><div><b>Rõ ràng</b><p>Giá minh bạch, báo giá bằng văn bản.</p></div></div></div>
</div></section>

<section style="background:#fff"><div class="w">
 <div class="row"><p class="lab">Logo</p><div><h2>Một chữ ký, <em>bốn chất liệu</em></h2><p class="lead">Logo giữ nguyên hình: chữ "an tâm" có chiếc bánh gập đôi làm dấu mũ. Bản cao cấp đổi chất liệu: ép kim vàng đồng, in nổi không màu, đỏ rượu trên giấy ngà.</p></div></div>
 <div class="logos">
  <div class="lt" style="background:{RUOU}">{wm(FOIL, RUOU)}<span class="cap" style="color:var(--nga)">Ép kim vàng đồng trên đỏ rượu</span></div>
  <div class="lt" style="background:{NGA}">{wm(RUOU, NGA, MUC)}<span class="cap">Đỏ rượu trên giấy ngà</span></div>
  <div class="lt emboss" style="background:{NGA2}">{wm(NGA2, NGA2)}<span class="cap">In nổi không màu</span></div>
  <div class="lt" style="background:{MUC}">{wm(NGA, MUC, sub_fg=DONG)}<span class="cap" style="color:var(--nga)">Ngà trên đen mực</span></div>
 </div>
</div></section>

<section><div class="w">
 <div class="row"><p class="lab">Màu</p><div><h2>Ấm, sâu, <em>tiết chế</em></h2><p class="lead">Đỏ rượu thay cho đỏ tươi ở mảng lớn. Đỏ An Tâm chỉ còn là điểm nhấn nhỏ. Vàng đồng dùng như kim loại: ép kim, đường chỉ, không tô mảng.</p></div></div>
 <div class="sw">
  <div style="background:{RUOU};color:var(--nga)"><b>Đỏ rượu</b>#6B0D12 · nền chính</div>
  <div style="background:{NGA};border:1px solid var(--line)"><b>Kem ngà</b>#F5EEE3 · giấy, nền</div>
  <div style="background:{DONG}"><b>Vàng đồng</b>#C9A26A · ép kim</div>
  <div style="background:{MUC};color:var(--nga)"><b>Đen mực</b>#1A1210</div>
  <div style="background:{DO};color:var(--nga)"><b>Đỏ An Tâm</b>#C8161D · nhấn</div>
 </div>
</div></section>

<section style="background:#fff"><div class="w">
 <div class="row"><p class="lab">Chữ</p><div><h2>Chữ có chân, <em>nét mảnh</em></h2></div></div>
 <div class="ty"><div class="g">Ẩm <span>ă</span></div>
  <dl><dt>Tiêu đề</dt><dd>Fraunces nét mảnh 300, nhấn bằng nét vừa 500. Cỡ lớn, khoảng dòng chặt.</dd>
   <dt>Tên thương hiệu</dt><dd>Fraunces đậm 900, chỉ trong logo.</dd>
   <dt>Nội dung</dt><dd>Be Vietnam Pro nét mảnh 300 và thường 400.</dd>
   <dt>Nhãn</dt><dd>Be Vietnam Pro 600, chữ in hoa nhỏ, giãn rộng 30%.</dd></dl></div>
</div></section>

<section class="dark"><div class="w">
 <div class="row"><p class="lab">Linh vật</p><div><h2>Bé Cuộn, <em>đại sứ lịch thiệp</em></h2><p class="lead">Ở bản cao cấp, Bé Cuộn xuất hiện tiết chế: bản 3D cho mạng xã hội và cửa hàng, bản nét mảnh ép kim cho hộp quà, tem, thiệp. Mỗi ấn phẩm tối đa một linh vật.</p></div></div>
 <div class="mas">
  <div style="background:radial-gradient(circle at 50% 40%,#7E1117,#3D0609)">{be_cuon('d1', 'cuoi', 'chao').replace('<svg ', '<svg class="lg" ', 1)}<span class="cap">Bản 3D</span></div>
  <div style="background:{RUOU}">{be_line(DONG)}<span class="cap">Nét mảnh ép kim</span></div>
  <div style="background:{NGA};color:var(--muc)">{be_line(RUOU, 3.5)}<span class="cap">Nét mảnh trên giấy ngà</span></div>
 </div>
</div></section>

<section><div class="w">
 <div class="row"><p class="lab">Ứng dụng</p><div><h2>Bao bì, cửa hàng, <em>giấy tờ</em></h2><p class="lead">Chỗ ghi [Cần điền] chờ thông tin thật từ công ty.</p></div></div>
 <div class="pk">
  <div class="c7"><span class="cap">Hộp quà doanh nghiệp</span>{gift_box()}</div>
  <div class="c5"><span class="cap" style="color:var(--nga)">Túi giấy</span>{bag()}</div>
  <div class="c12"><span class="cap" style="color:var(--nga)">Mặt tiền cửa hàng</span>{store()}</div>
  <div class="c4"><span class="cap">Gói bánh tortillas</span>{pack()}</div>
  <div class="c4"><span class="cap">Bài đăng 1080 × 1350</span>{post()}</div>
  <div class="c4" style="background:#D8CBB6;display:grid;align-items:center"><span class="cap">Danh thiếp</span>{card()}</div>
 </div>
</div></section>

<footer><div class="w"><div>{wm(FOIL, MUC)}<p>Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm. Bản đề xuất cao cấp, chờ công ty duyệt. Chữ Fraunces và Be Vietnam Pro dùng theo giấy phép SIL Open Font License.</p></div>
<div class="ct">0348.635.222<br>antamfoods.com</div></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

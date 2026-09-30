"""Cẩm nang nhận diện Ẩm Thực An Tâm, hướng Bột & Lửa.
Chạy: python3 build_bot_lua.py OUT.html
Cần: logo_bot_lua.py, thư mục gluten/ và nunito/ (npm @fontsource), minh hoạ trong plugins/design/assets/minh-hoa.
"""
import base64
import os
import sys

import logo_bot_lua as LG
from logo_bot_lua import OUT, DO, DO_DAM, BOT, BANH, VANH, DOM, VANG, MUC, RAU

HERE = os.path.dirname(os.path.abspath(__file__))
MH = os.environ.get("MINH_HOA", "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa")
RANGES = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
}


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def ill(name):
    return b64(f"{MH}/{name}.svg", "image/svg+xml")


def fontfaces():
    out = []
    for fam, name, ws in (("gluten", "Gluten", (600, 800)), ("nunito", "Nunito", (400, 700, 800))):
        for w in ws:
            for sub, rg in RANGES.items():
                uri = b64(os.path.join(HERE, f"{fam}/files/{fam}-{sub}-{w}-normal.woff2"), "font/woff2")
                out.append(f"@font-face{{font-family:'{name}';font-weight:{w};font-display:swap;src:url({uri}) format('woff2');unicode-range:{rg}}}")
    return "\n".join(out)


def logo(key, cls="", label="Ẩm Thực An Tâm"):
    return OUT[key].replace("<svg ", f'<svg class="lg {cls}" ', 1).replace('aria-label="Ẩm Thực An Tâm"', f'aria-label="{label}"')


# ---------- hoạ tiết ----------
def pat_spots():
    return (f'<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="400" fill="{BANH}"/>'
            + LG.char_spots(200, 200, 290, 170, 3, scale=1.3) + "</svg>")


def pat_lettuce():
    rows = ""
    for r in range(9):
        y = r * 46 + 20
        col = [RAU, DO, VANG][r % 3]
        rows += f'<path d="M-20,{y} ' + " ".join(f"q12,-14 24,0 q12,14 24,0" for _ in range(10)) + f'" fill="none" stroke="{col}" stroke-width="7" stroke-linecap="round"/>'
    return f'<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="400" fill="{BOT}"/>{rows}</svg>'


def pat_awning():
    s = "".join(f'<rect x="{i * 50}" y="0" width="25" height="400" fill="{DO}"/>' for i in range(9))
    s += "".join(f'<path d="M{i * 50},330 a25,25 0 0 0 50,0" fill="{DO if i % 2 == 0 else BOT}"/>' for i in range(8))
    return f'<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="400" fill="{BOT}"/>{s}<rect y="355" width="400" height="45" fill="{MUC}"/></svg>'


def pat_icons():
    items = []
    icons = [
        lambda x, y: f'<circle cx="{x}" cy="{y}" r="18" fill="{BANH}"/><circle cx="{x - 6}" cy="{y - 4}" r="2.5" fill="{DOM}"/><circle cx="{x + 7}" cy="{y + 5}" r="2" fill="{DOM}"/>',
        lambda x, y: f'<path d="M{x - 20},{y} H{x + 20} A20,20 0 0 1 {x - 20},{y} Z" fill="{VANG}"/><path d="M{x - 18},{y} q6,-9 12,0 q6,-9 12,0 q6,-9 12,0" fill="{RAU}"/>',
        lambda x, y: f'<path d="M{x - 4},{y - 18} q14,6 10,34 q-2,6 -6,0 q-8,-18 -4,-34 z" fill="{DO}"/><path d="M{x - 4},{y - 18} l-3,-6" stroke="{RAU}" stroke-width="4" stroke-linecap="round"/>',
        lambda x, y: LG.steam(x, y - 22, 40, DO, 4, 12),
    ]
    k = 0
    for r in range(5):
        for c in range(5):
            x, y = c * 84 + (42 if r % 2 else 0) + 10, r * 84 + 40
            items.append(icons[k % 4](x, y)); k += 1
    return f'<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="400" fill="{MUC}"/>{"".join(items)}</svg>'


# ---------- ứng dụng ----------
def store():
    stripes = "".join(f'<rect x="{150 + i * 56.25}" y="150" width="28.1" height="100" fill="{DO}"/>' for i in range(16))
    scallop = "".join(f'<path d="M{150 + i * 56.25},250 a28.1,28.1 0 0 0 56.25,0" fill="{DO if i % 2 == 0 else BOT}"/>' for i in range(16))
    return f"""<svg class="mock" viewBox="0 0 1200 720" role="img" aria-label="Mặt tiền cửa hàng">
<defs><linearGradient id="gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE7B8"/><stop offset="1" stop-color="#F2B35F"/></linearGradient>
<filter id="sf" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="12"/></filter></defs>
<rect width="1200" height="720" fill="#F6E2C2"/>
<rect x="150" y="40" width="900" height="560" fill="{BOT}"/>
<rect x="150" y="40" width="900" height="110" fill="{MUC}"/>
<g transform="translate(600 95)">{OUT['horiz_do'].replace('<svg ', '<svg x="-230" y="-48" width="460" height="96" ', 1)}</g>
<rect x="150" y="150" width="900" height="100" fill="{BOT}"/>{stripes}{scallop}
<ellipse cx="600" cy="300" rx="440" ry="18" fill="#000" opacity=".12" filter="url(#sf)"/>
<rect x="200" y="320" width="330" height="240" rx="8" fill="url(#gl)" stroke="{MUC}" stroke-width="10"/>
<image href="{ill('doner-tru-quay')}" x="240" y="340" width="220" height="220"/>
<rect x="580" y="320" width="170" height="280" fill="{MUC}"/>
<rect x="596" y="336" width="138" height="264" fill="url(#gl)" opacity=".85"/>
<g transform="translate(620 390)">{OUT['mark_tron'].replace('<svg ', '<svg width="90" height="90" ', 1)}</g>
<rect x="800" y="320" width="200" height="240" rx="8" fill="url(#gl)" stroke="{MUC}" stroke-width="10"/>
<image href="{ill('doner-cuon')}" x="820" y="350" width="170" height="190"/>
<rect x="120" y="600" width="960" height="20" fill="{MUC}"/>
<rect y="620" width="1200" height="100" fill="#E7CFA8"/>
<g transform="translate(1040 470)"><rect x="0" y="0" width="120" height="160" rx="8" fill="{MUC}"/>
<text x="60" y="36" text-anchor="middle" fill="{VANG}" style="font:800 18px 'Gluten',sans-serif">Thực đơn</text>
<path d="M18,60 H102 M18,84 H90 M18,108 H100 M18,132 H80" stroke="{BOT}" stroke-width="5" stroke-linecap="round" opacity=".5"/>
<path d="M20,160 L10,220 M100,160 L110,220" stroke="{MUC}" stroke-width="6"/></g>
</svg>"""


def bag():
    return f"""<svg class="mock" viewBox="0 0 600 640" role="img" aria-label="Túi giấy">
<defs><filter id="sf2" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="12"/></filter></defs>
<ellipse cx="300" cy="605" rx="210" ry="18" fill="#000" opacity=".22" filter="url(#sf2)"/>
<path d="M215,175 C215,80 325,80 325,175" fill="none" stroke="{DO_DAM}" stroke-width="8" stroke-linecap="round"/>
<path d="M150,600 L150,170 L400,170 L400,600 Z" fill="{BOT}"/>
<path d="M400,170 L465,150 L465,590 L400,600 Z" fill="#EAD9BC"/>
<path d="M150,170 H400 V230 H150 Z" fill="{DO}"/>
<path d="M150,230 " fill="none"/>
{"".join(f'<path d="M{150 + i * 25},230 a12.5,12.5 0 0 0 25,0" fill="{DO}"/>' for i in range(10))}
<g transform="translate(180 262)">{OUT['seal'].replace('<svg ', '<svg width="190" height="190" ', 1)}</g>
<text x="275" y="500" text-anchor="middle" fill="{MUC}" style="font:800 20px 'Gluten',sans-serif">Nóng giòn mỗi ngày</text>
<text x="275" y="540" text-anchor="middle" fill="{MUC}" style="font:700 12px 'Nunito',sans-serif;letter-spacing:.2em" opacity=".75">ANTAMFOODS.COM · 0348.635.222</text>
</svg>"""


def pack():
    return f"""<svg class="mock" viewBox="0 0 600 640" role="img" aria-label="Gói bánh tortillas">
<defs><clipPath id="pw"><circle cx="300" cy="430" r="110"/></clipPath><filter id="sf3" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="12"/></filter>
<linearGradient id="gloss" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<ellipse cx="300" cy="612" rx="200" ry="16" fill="#000" opacity=".25" filter="url(#sf3)"/>
<path d="M130,70 Q300,55 470,70 L480,600 Q300,616 120,600 Z" fill="{DO}"/>
<path d="M130,70 Q300,55 470,70 L472,108 Q300,94 128,108 Z" fill="{DO_DAM}"/>
<g transform="translate(200 115)">{OUT['seal_do'].replace('<svg ', '<svg width="200" height="200" ', 1)}</g>
<circle cx="300" cy="430" r="118" fill="{BOT}"/>
<image href="{ill('banh-tortillas')}" x="180" y="310" width="240" height="240" clip-path="url(#pw)"/>
<circle cx="300" cy="430" r="110" fill="none" stroke="{VANG}" stroke-width="3" stroke-dasharray="3 8" stroke-linecap="round"/>
<text x="300" y="582" text-anchor="middle" fill="{BOT}" style="font:800 26px 'Gluten',sans-serif">Bánh Tortillas</text>
<text x="420" y="330" fill="{MUC}" style="font:700 11px 'Nunito',sans-serif">[Cần điền: khối lượng]</text>
<path d="M150,70 L160,600" stroke="url(#gloss)" stroke-width="60"/>
</svg>"""


def box():
    return f"""<svg class="mock" viewBox="0 0 600 480" role="img" aria-label="Hộp giấy đựng món">
<defs><filter id="sf4" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="10"/></filter></defs>
<ellipse cx="300" cy="420" rx="230" ry="20" fill="#000" opacity=".22" filter="url(#sf4)"/>
<path d="M90,200 L300,120 L510,200 L300,280 Z" fill="{DO_DAM}"/>
<path d="M90,200 L300,280 L300,420 L90,340 Z" fill="{BOT}"/>
<path d="M510,200 L300,280 L300,420 L510,340 Z" fill="#EAD9BC"/>
<path d="M90,200 L300,280 L300,300 L90,220 Z" fill="{DO}"/>
<path d="M300,280 L510,200 L510,220 L300,300 Z" fill="{DO_DAM}"/>
<g transform="translate(118 238) skewY(20.8)">{OUT['horiz'].replace('<svg ', '<svg width="160" height="80" ', 1)}</g>
<g transform="translate(330 300) skewY(-20.8)">{LG.char_spots(80, 30, 70, 14, 5, scale=.8)}</g>
<path d="M90,200 L300,120 L510,200" fill="none" stroke="{MUC}" stroke-width="2" opacity=".25"/>
</svg>"""


def wrap_paper():
    return f"""<svg class="mock" viewBox="0 0 600 480" role="img" aria-label="Giấy gói bánh cuộn">
<defs><pattern id="wp" width="120" height="120" patternUnits="userSpaceOnUse">
<rect width="120" height="120" fill="{BOT}"/>{LG.steam(30, 12, 26, DO, 3, 9)}
<g transform="translate(62 62)">{OUT['mark_tron'].replace('<svg ', '<svg width="44" height="44" ', 1)}</g></pattern>
<filter id="sf5" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="10"/></filter></defs>
<ellipse cx="300" cy="420" rx="170" ry="18" fill="#000" opacity=".22" filter="url(#sf5)"/>
<g transform="rotate(-10 300 250)">
<path d="M220,90 Q300,60 380,90 L370,410 Q300,430 230,410 Z" fill="{BANH}"/>
<path d="M226,112 q18,-20 36,0 q18,-20 36,0 q18,-20 36,0 q18,-20 36,0" fill="{RAU}"/>
<circle cx="258" cy="102" r="10" fill="{DO}"/><circle cx="330" cy="100" r="9" fill="{DO}"/>
<path d="M222,170 Q300,150 378,170 L370,410 Q300,430 230,410 Z" fill="url(#wp)"/>
<path d="M222,170 Q300,150 378,170" fill="none" stroke="{DO}" stroke-width="5"/>
</g></svg>"""


def post():
    return f"""<div class="phone"><div class="ph-scr">
 <div class="ph-bar"><span class="ph-av">{logo('mark_tron', 'av')}</span><span><b>Ẩm Thực An Tâm</b><small>Được tài trợ</small></span></div>
 <svg class="ph-post" viewBox="0 0 1080 1350" aria-hidden="true"><rect width="1080" height="1350" fill="{DO}"/>
  {LG.char_spots(540, 675, 900, 60, 12, scale=2.2, color=DO_DAM)}
  <circle cx="540" cy="880" r="330" fill="{BANH}"/>
  <image href="{ill('taco')}" x="250" y="590" width="580" height="580"/>
  <text x="540" y="250" text-anchor="middle" fill="{BOT}" style="font:800 120px 'Gluten',sans-serif">Gập đôi,</text>
  <text x="540" y="380" text-anchor="middle" fill="{VANG}" style="font:800 120px 'Gluten',sans-serif">ngon gấp đôi</text>
  <text x="540" y="460" text-anchor="middle" fill="{BOT}" style="font:700 38px 'Nunito',sans-serif">Taco giao tận văn phòng</text>
  <g transform="translate(820 1180)">{OUT['horiz_do'].replace('<svg ', '<svg x="-200" y="-10" width="400" height="120" ', 1)}</g>
 </svg>
 <div class="ph-cap">Taco, doner kebab cho bữa nhẹ văn phòng. Gọi 0348.635.222.</div>
</div></div>"""


def menu():
    rows = [("Bánh tortillas", "[Giá]"), ("Taco", "[Giá]"), ("Doner kebab", "[Giá]"), ("Doner cuộn", "[Giá]")]
    items = "".join(f'<li><span>{n}</span><i></i><b>{p}</b></li>' for n, p in rows)
    return f"""<div class="menu"><div class="m-top">{logo('horiz_do', 'm-logo')}</div>
<h4>Thực đơn</h4><ul>{items}</ul>
<div class="m-ill"><img src="{ill('taco')}" alt=""><img src="{ill('doner-cuon')}" alt=""></div>
<p>Giá ghi [Giá]: chờ phòng tài chính xác nhận.</p></div>"""


def card():
    return f"""<div class="scene sc-card">
 <div class="nc front">{logo('seal_do', 'nc-seal')}</div>
 <div class="nc back"><div class="nc-top">{logo('horiz', 'nc-h')}</div>
  <div class="nc-name"><b>[Cần điền: Họ tên]</b><span>[Cần điền: Chức danh]</span></div>
  <div class="nc-ct"><span>0348.635.222</span><span>antamfoods.com</span><span>TP. Hồ Chí Minh</span></div></div>
</div>"""


def apron():
    return f"""<svg class="mock" viewBox="0 0 400 480" role="img" aria-label="Tạp dề nhân viên">
<defs><filter id="sf6" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="8"/></filter></defs>
<path d="M150,40 C150,0 250,0 250,40" fill="none" stroke="{MUC}" stroke-width="8"/>
<path d="M140,40 H260 L270,150 Q340,150 350,170 L330,450 Q200,470 70,450 L50,170 Q60,150 130,150 Z" fill="{DO}"/>
<path d="M50,170 Q20,175 10,200 M350,170 Q380,175 390,200" stroke="{MUC}" stroke-width="7" fill="none"/>
<rect x="120" y="330" width="160" height="80" rx="10" fill="{DO_DAM}"/>
<g transform="translate(130 150)">{OUT['seal_do'].replace('<svg ', '<svg width="140" height="140" ', 1)}</g>
<path d="M70,450 Q200,470 330,450" stroke="{DO_DAM}" stroke-width="3" fill="none" stroke-dasharray="6 6"/>
</svg>"""


CSS = """
/* Bố cục: cẩm nang nhiều trang; nền kem bột, mảng đỏ cà chua, chữ Gluten mềm như bột nhào. */
:root{--do:#D62718;--do2:#A5170D;--bot:#FFF3DD;--banh:#F4D59B;--vanh:#E5B566;--dom:#A7652E;--vang:#FFB400;--muc:#3A1A12;--rau:#3E8E41;--xam:#7A5A4C;--line:#EBD6B3;
--hien:'Gluten','Nunito',system-ui,sans-serif;--noi:'Nunito',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--bot);color:var(--muc);font:400 17px/1.6 var(--noi);-webkit-font-smoothing:antialiased}
img,svg{max-width:100%}
svg.lg{display:block;height:auto;width:100%}
.w{max-width:1200px;margin:0 auto;padding-inline:40px}
.page{padding-block:104px}
.page.red{background:var(--do);color:var(--bot)}
.page.dark{background:var(--muc);color:var(--bot)}
.page.banh{background:#FBE6BD}
.ph{display:flex;justify-content:space-between;align-items:center;font:800 12px/1 var(--noi);letter-spacing:.2em;text-transform:uppercase;margin-bottom:56px;opacity:.75}
.ph b{display:inline-grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--do);color:var(--bot);letter-spacing:0;font:800 16px/1 var(--noi)}
.red .ph b{background:var(--bot);color:var(--do)}
.head{display:grid;grid-template-columns:6fr 5fr;gap:48px;align-items:end;margin-bottom:56px}
h2{font:800 clamp(40px,6vw,76px)/1 var(--hien);letter-spacing:-.01em;text-wrap:balance}
h2 em{font-style:normal;color:var(--do)}
.red h2 em,.dark h2 em{color:var(--vang)}
.head p{font-size:17px;max-width:54ch;opacity:.85}
h3{font:800 22px/1.2 var(--hien)}

/* bìa */
.cover{background:var(--do);color:var(--bot);position:relative;overflow:hidden;padding-block:36px 0}
.cover .w{position:relative;z-index:1}
.cv-top{display:flex;justify-content:space-between;font:800 12px/1 var(--noi);letter-spacing:.22em;text-transform:uppercase;opacity:.85}
.cv-mid{display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;padding-block:48px 72px}
.cv-mid h1{font:800 clamp(44px,6.4vw,88px)/.98 var(--hien);letter-spacing:-.01em}
.cv-mid h1 span{color:var(--vang)}
.cv-mid p{margin-top:22px;font-size:18px;max-width:40ch;opacity:.92}
.cv-seal{max-width:480px;justify-self:center;width:100%}
.cv-spots{position:absolute;inset:0;opacity:.5}
.awning{display:flex;height:56px}
.awning i{flex:1;background:var(--bot);border-radius:0 0 999px 999px}
.awning i:nth-child(2n){background:var(--vang)}

/* ý tưởng */
.idea{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.idea > div{background:#fff;border-radius:28px;padding:28px;display:flex;flex-direction:column;gap:12px;border:2px solid var(--line)}
.idea svg{height:120px;width:100%}
.idea p{font-size:15px;color:var(--xam)}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:40px}
.chips span{font:800 14px/1 var(--noi);padding:12px 18px;border-radius:999px;background:var(--muc);color:var(--bot)}
.chips span:nth-child(2n){background:var(--do)}
.chips span:nth-child(3n){background:var(--vang);color:var(--muc)}

/* logo */
.hero-logo{background:#fff;border-radius:36px;display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:40px;padding:56px;border:2px solid var(--line)}
.hero-logo .lg{max-width:440px;justify-self:center}
.anat{display:grid;gap:14px}
.anat div{display:grid;grid-template-columns:40px 1fr;gap:14px;align-items:start;font-size:15px}
.anat b{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--do);color:var(--bot);font:800 15px/1 var(--hien)}
.anat strong{display:block;font:800 18px/1.3 var(--hien)}
.vars{display:grid;grid-template-columns:repeat(6,1fr);gap:18px;margin-top:18px}
.v{border-radius:28px;display:grid;place-items:center;padding:40px 28px;min-height:280px;position:relative}
.v .cap{position:absolute;left:20px;bottom:16px;font:800 11px/1 var(--noi);letter-spacing:.16em;text-transform:uppercase;opacity:.7}
.v .lg{max-width:300px}
.v.wide .lg{max-width:460px}
.s2{grid-column:span 2}.s3{grid-column:span 3}.s4{grid-column:span 4}
.bg-bot{background:#fff;border:2px solid var(--line)}.bg-do{background:var(--do);color:var(--bot)}.bg-muc{background:var(--muc);color:var(--bot)}.bg-vang{background:var(--vang)}.bg-banh{background:var(--banh)}

/* quy tắc */
.rules{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.rbox{background:#fff;border-radius:28px;padding:40px;border:2px solid var(--line);display:grid;place-items:center;gap:24px}
.cz{position:relative;padding:44px;background:repeating-linear-gradient(45deg,rgba(214,39,24,.1) 0 7px,transparent 7px 14px);border-radius:24px}
.cz::before{content:"";position:absolute;inset:44px;background:#fff}
.cz .lg{position:relative;width:260px}
.cz i{position:absolute;font:800 13px/1 var(--hien);color:var(--do);font-style:normal}
.cz i.t{top:14px;left:50%}.cz i.l{left:16px;top:50%}
.mins{display:flex;gap:36px;align-items:end;justify-content:center;flex-wrap:wrap}
.mins div{display:flex;flex-direction:column;align-items:center;gap:12px;font:700 12px/1.4 var(--noi);color:var(--xam);text-align:center}
.dont{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:18px}
.dont figure{background:#fff;border-radius:24px;border:2px solid var(--line);aspect-ratio:1;display:grid;place-items:center;position:relative;overflow:hidden;padding:30px 30px 50px}
.dont figure .lg{width:78%}
.dont figcaption{position:absolute;left:16px;right:16px;bottom:14px;font:800 13px/1.2 var(--noi);display:flex;gap:8px;align-items:center}
.dont figcaption::before{content:"✕";display:grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--do);color:#fff;font-size:11px;flex:none}

/* màu */
.pal{display:grid;grid-template-columns:6fr 3fr 1.6fr 1.6fr 1.2fr;gap:14px;height:400px}
.sw{border-radius:28px;padding:24px 20px;display:flex;flex-direction:column;justify-content:flex-end;font:700 13px/1.55 var(--noi);font-variant-numeric:tabular-nums}
.sw b{font:800 22px/1.1 var(--hien);display:block;margin-bottom:6px}
.sw .n{font:800 48px/1 var(--hien);margin-bottom:auto;padding-top:52px}
.sw.small .n{font-size:28px}
.pair{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:14px}
.pair div{border-radius:20px;padding:18px 20px;font:800 28px/1 var(--hien);display:flex;justify-content:space-between;align-items:end}
.pair small{font:700 12px/1.2 var(--noi);opacity:.85}
.note{font-size:14px;color:var(--xam);margin-top:18px;max-width:80ch}

/* chữ */
.type{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.tcard{background:#fff;border-radius:28px;padding:40px;border:2px solid var(--line)}
.tcard .big{font:800 150px/.95 var(--hien);color:var(--do)}
.tcard .big.n{font:800 150px/.95 var(--noi);color:var(--muc)}
.tcard h3{margin-top:18px}
.tcard p{color:var(--xam);font-size:15px;margin-top:8px}
.tcard .chars{letter-spacing:.04em;margin-top:16px;font-size:15px;word-break:break-all}
.scale{grid-column:1/-1}
.scale div{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:baseline;padding:20px 0;border-bottom:2px dashed var(--line)}
.scale small{font:700 12px/1.4 var(--noi);color:var(--xam);text-align:right;white-space:nowrap}
.k1{font:800 64px/1 var(--hien);color:var(--do)}
.k2{font:800 34px/1.1 var(--hien)}
.k3{font:800 14px/1 var(--noi);letter-spacing:.2em;text-transform:uppercase;color:var(--do)}
.k4{font:400 17px/1.6 var(--noi);max-width:52ch}

/* hoạ tiết */
.pats{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.pat svg{display:block;width:100%;aspect-ratio:1;border-radius:28px}
.pat figcaption{margin-top:12px;font-size:14px;opacity:.85}
.pat b{display:block;font:800 18px/1.3 var(--hien)}

/* sản phẩm */
.prod{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.prod .disc{aspect-ratio:1;border-radius:50%;background:var(--banh);display:grid;place-items:center;padding:14%;position:relative;box-shadow:inset 0 0 0 10px #F9E3B8}
.prod .disc::after{content:"";position:absolute;inset:18px;border-radius:50%;border:3px dashed var(--vanh)}
.prod img{position:relative;z-index:1}
.prod h3{margin-top:18px;text-align:center}
.prod p{text-align:center;font-size:15px;color:var(--xam)}
.photo{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:40px}
.photo div{background:#fff;border-radius:24px;padding:28px;border:2px solid var(--line)}
.photo ul{margin-top:10px;padding-left:20px;display:grid;gap:6px;font-size:15px}

/* ứng dụng */
.apps{display:grid;grid-template-columns:repeat(12,1fr);gap:18px}
.app{border-radius:28px;overflow:hidden;position:relative}
.app .cap{position:absolute;left:18px;top:16px;font:800 11px/1 var(--noi);letter-spacing:.16em;text-transform:uppercase;background:var(--bot);color:var(--muc);padding:8px 12px;border-radius:999px;z-index:2}
.a12{grid-column:span 12}.a6{grid-column:span 6}.a4{grid-column:span 4}.a8{grid-column:span 8}.a5{grid-column:span 5}.a7{grid-column:span 7}
.mock{display:block;width:100%;height:auto}
.bgA{background:linear-gradient(160deg,#F7E4C4,#EBCB98);padding:40px 20px 10px}
.bgB{background:linear-gradient(160deg,#4A2419,#2A120C);padding:40px 20px 10px}
.bgC{background:linear-gradient(160deg,#FFD66B,#FFB400);padding:40px 20px 10px}
.bgD{background:linear-gradient(160deg,#FCEBD0,#F2D3A3);padding:40px 20px 10px}
.phone-wrap{background:linear-gradient(160deg,var(--rau),#2C6A2F);display:grid;place-items:center;padding:56px 20px 40px}
.phone{width:min(100%,300px);background:#111;border-radius:40px;padding:12px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)}
.ph-scr{background:#fff;border-radius:30px;overflow:hidden;color:#1c1e21}
.ph-bar{display:flex;gap:10px;align-items:center;padding:16px 14px 10px;font:400 12px/1.3 var(--noi)}
.ph-bar b{display:block;font-weight:800;font-size:13px}.ph-bar small{color:#65676b}
.ph-av{width:36px;height:36px;border-radius:50%;background:var(--bot);display:grid;place-items:center;overflow:hidden;flex:none;padding:3px}
.ph-post{display:block;width:100%;height:auto}
.ph-cap{padding:12px 14px 18px;font:400 12px/1.5 var(--noi)}
.menu-wrap{background:#6B4A33;display:grid;place-items:center;padding:56px 24px 32px}
.menu{background:var(--muc);color:var(--bot);width:min(100%,420px);border-radius:16px;padding:28px;border:10px solid #2A120C;box-shadow:0 30px 50px -20px rgba(0,0,0,.6)}
.m-top{display:flex;justify-content:center}.m-logo{max-width:230px}
.menu h4{font:800 36px/1 var(--hien);color:var(--vang);text-align:center;margin-top:18px}
.menu ul{list-style:none;padding:0;margin-top:14px;display:grid;gap:10px}
.menu li{display:flex;gap:10px;align-items:baseline;font:800 19px/1.2 var(--hien)}
.menu li i{flex:1;border-bottom:2px dotted rgba(255,243,221,.4)}
.menu li b{font:800 15px/1 var(--noi);color:var(--vang)}
.m-ill{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.menu p{font-size:11px;opacity:.6;margin-top:6px;text-align:center}
.sc-card{background:linear-gradient(160deg,#EBD9BC,#D8BF96);aspect-ratio:4/3;position:relative}
.nc{position:absolute;width:52%;aspect-ratio:90/54;border-radius:10px;box-shadow:0 18px 30px -12px rgba(60,25,10,.45)}
.nc.front{background:var(--do);left:8%;top:20%;transform:rotate(-8deg);display:grid;place-items:center;padding:3%}
.nc-seal{width:auto !important;height:100% !important}
.nc.back{background:var(--bot);right:7%;bottom:14%;transform:rotate(5deg);padding:6% 7%;display:grid;grid-template-rows:auto 1fr auto;font:400 clamp(8px,1vw,12px)/1.4 var(--noi)}
.nc-h{width:46% !important}
.nc-name{align-self:center}.nc-name b{display:block;font:800 1.5em/1.3 var(--hien)}.nc-name span{color:var(--xam)}
.nc-ct{display:flex;gap:1.4em;flex-wrap:wrap;border-top:2px dashed var(--line);padding-top:.7em;font-weight:700}
.avs{background:var(--bot);display:flex;gap:28px;justify-content:center;align-items:center;flex-wrap:wrap;padding:56px 20px 40px;border:2px solid var(--line);border-radius:28px}
.avs div{width:130px;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;overflow:hidden;box-shadow:0 10px 20px -12px rgba(0,0,0,.4)}
.avs .sq{border-radius:30px}
.avs .lg{width:80%}

.back{background:var(--muc);color:var(--bot);padding-block:80px 48px}
.back .w{display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center}
.back .lg{width:200px}
.back p{font-size:14px;opacity:.72;max-width:56ch}
.back .ct{font:800 16px/1.9 var(--noi);text-align:right}
.back .ct small{display:block;font:800 11px/1.4 var(--noi);letter-spacing:.2em;text-transform:uppercase;color:var(--vang)}
@media (prefers-reduced-motion:no-preference){.cv-seal{animation:rise .9s ease-out both}@keyframes rise{from{transform:translateY(14px)}to{transform:none}}}
@media (max-width:900px){
 .w{padding-inline:20px}.page{padding-block:72px}.head{grid-template-columns:1fr;gap:18px;margin-bottom:40px}
 .cv-mid{grid-template-columns:1fr}.cv-seal{max-width:340px}
 .idea{grid-template-columns:1fr 1fr}.hero-logo{grid-template-columns:1fr;padding:32px 22px}
 .vars{grid-template-columns:1fr 1fr}.s2,.s3,.s4{grid-column:1/-1}.v{min-height:220px}
 .rules{grid-template-columns:1fr}.dont{grid-template-columns:1fr 1fr}
 .pal{grid-template-columns:1fr 1fr;height:auto}.sw{min-height:220px}.sw:first-child{grid-column:1/-1}.pair{grid-template-columns:1fr 1fr}
 .type{grid-template-columns:1fr}.tcard .big,.tcard .big.n{font-size:100px}.k1{font-size:44px}
 .pats,.prod{grid-template-columns:1fr 1fr}.photo{grid-template-columns:1fr}
 .a12,.a6,.a4,.a8,.a5,.a7{grid-column:1/-1}
 .back .w{grid-template-columns:1fr}.back .ct{text-align:left}}
@media (max-width:480px){.idea,.dont{grid-template-columns:1fr}.scale div{grid-template-columns:1fr;gap:6px}.scale small{text-align:left}}
"""


def ph(n, t):
    return f'<div class="ph"><span>Ẩm Thực An Tâm · {t}</span><b>{n}</b></div>'


def page():
    idea_svgs = [
        (f'<svg viewBox="0 0 200 120" aria-hidden="true"><text x="100" y="92" text-anchor="middle" fill="{DO}" style="font:800 96px \'Gluten\',sans-serif">Aa</text></svg>',
         "Chữ như bột nhào", "Gluten: nét tròn, căng, mềm như bột vừa nhào. Nhìn là thấy đồ ăn, thấy gần gũi."),
        (f'<svg viewBox="0 0 200 120" aria-hidden="true"><path d="{LG.tortilla(100, 62, 52)}" fill="{BANH}"/>{LG.char_spots(100, 62, 44, 12, 2, scale=.7)}</svg>',
         "Chiếc bánh tròn", "Bánh tortilla có đốm nướng là nền của logo, tem, bao bì."),
        (f'<svg viewBox="0 0 200 120" aria-hidden="true">{LG.steam(100, 12, 90, DO, 7, 30)}</svg>',
         "Khói nóng", "Ba sợi khói: bánh mới nướng, giao còn nóng."),
        (f'<svg viewBox="0 0 200 120" aria-hidden="true"><path d="M20,40 Q100,30 180,40 V92 Q100,82 20,92 Z" fill="{DO}"/><text x="100" y="78" text-anchor="middle" fill="{BOT}" style="font:800 34px \'Gluten\',sans-serif">An Tâm</text></svg>',
         "Dải băng đỏ", "Như băng tem trên bánh lò nướng: nơi đặt tên thương hiệu."),
    ]
    ideas = "".join(f"<div>{s}<h3>{t}</h3><p>{p}</p></div>" for s, t, p in idea_svgs)
    prods = "".join(f'<div><div class="disc"><img src="{ill(n)}" alt="{t}"></div><h3>{t}</h3><p>{d}</p></div>' for n, t, d in [
        ("banh-tortillas", "Bánh tortillas", "Bánh nền, bán sỉ cho doanh nghiệp"), ("taco", "Taco", "Gập đôi, nhân đầy"),
        ("doner-tru-quay", "Doner kebab", "Thịt nướng trụ quay"), ("doner-cuon", "Doner cuộn", "Cuộn chặt, ăn gọn")])
    donts = "".join(f'<figure>{logo("seal", "", "")[:-6].replace("<svg ", f"<svg style={chr(34)}{st}{chr(34)} ", 1)}</svg><figcaption>{t}</figcaption></figure>' for t, st in [
        ("Kéo méo", "transform:scaleX(1.4)"), ("Xoay nghiêng", "transform:rotate(-18deg)"),
        ("Đổi màu lạ", "filter:hue-rotate(160deg)"), ("Thêm hiệu ứng", "filter:drop-shadow(8px 8px 0 #3E8E41) blur(.6px)")])
    return f"""<title>An Tâm Bột và Lửa</title>
<style>{fontfaces()}
{CSS}</style>

<header class="cover"><svg class="cv-spots" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{LG.char_spots(600, 400, 900, 90, 31, scale=2.4, color=DO_DAM)}</svg><div class="w">
 <div class="cv-top"><span>Cẩm nang nhận diện</span><span>Bản đề xuất · 09/2026</span></div>
 <div class="cv-mid">
  <div><h1>Bánh nóng,<br><span>ăn an tâm.</span></h1><p>Bộ nhận diện mới cho Ẩm Thực An Tâm: chữ mềm như bột, chiếc bánh có đốm nướng, khói nóng và dải băng đỏ.</p></div>
  {logo('seal_do', 'cv-seal')}
 </div>
</div><div class="awning">{'<i></i>' * 16}</div></header>

<section class="page"><div class="w">
 {ph(1, 'Ý tưởng')}
 <div class="head"><h2>Bột &amp; <em>Lửa</em></h2><p>Bánh tortilla ra đời từ bột và lửa. Bộ nhận diện lấy đúng hai thứ đó: chữ mềm như bột nhào, đốm nướng và khói nóng của lửa. Ai nhìn cũng biết đây là đồ ăn, và là đồ ăn mới làm.</p></div>
 <div class="idea">{ideas}</div>
 <div class="chips"><span>Ấm áp</span><span>Ngon mắt</span><span>Gần gũi</span><span>Sạch sẽ</span><span>Nóng giòn</span><span>Đáng tin</span></div>
</div></section>

<section class="page banh"><div class="w">
 {ph(2, 'Logo chính')}
 <div class="head"><h2>Tem bánh <em>An Tâm</em></h2><p>Logo chính là một chiếc tem tròn: chiếc bánh làm nền, dải băng đỏ mang chữ An Tâm, trên đầu là ẨM THỰC, dưới chân là sản phẩm, trên cùng là khói nóng.</p></div>
 <div class="hero-logo">{logo('seal')}
  <div class="anat">
   <div><b>1</b><span><strong>Khói nóng</strong>Ba sợi khói đỏ: bánh vừa ra lò.</span></div>
   <div><b>2</b><span><strong>ẨM THỰC</strong>Chữ Gluten đậm, màu nâu mực, nằm trên đầu dải băng.</span></div>
   <div><b>3</b><span><strong>Dải băng An Tâm</strong>Tên thương hiệu chữ kem trên nền đỏ, hai đuôi gấp.</span></div>
   <div><b>4</b><span><strong>Dòng sản phẩm</strong>BÁNH TORTILLAS · DONER KEBAB, chữ Nunito đậm.</span></div>
   <div><b>5</b><span><strong>Chiếc bánh</strong>Tortilla có đốm nướng, viền nét đứt như mép bánh.</span></div>
  </div></div>
</div></section>

<section class="page"><div class="w">
 {ph(3, 'Các bản logo')}
 <div class="head"><h2>Một nhà, <em>nhiều cỡ</em></h2><p>Tem tròn dùng chính. Bản ngang cho biển hiệu, đầu thư, hộp dài. Biểu tượng chiếc bánh chữ Â cho ảnh đại diện, tem nhỏ. Chữ An Tâm có khói dùng khi cần gọn.</p></div>
 <div class="vars">
  <div class="v s2 bg-bot">{logo('seal')}<span class="cap">Tem tròn</span></div>
  <div class="v s2 bg-do">{logo('seal_do')}<span class="cap">Tem trên nền đỏ</span></div>
  <div class="v s2 bg-bot">{logo('seal_mot_mau')}<span class="cap">Một màu, con dấu</span></div>
  <div class="v s4 wide bg-bot">{logo('horiz')}<span class="cap">Bản ngang</span></div>
  <div class="v s2 bg-vang">{logo('mark')}<span class="cap">Biểu tượng</span></div>
  <div class="v s3 wide bg-do">{logo('horiz_do')}<span class="cap">Bản ngang trên đỏ</span></div>
  <div class="v s3 wide bg-muc">{logo('wordmark_bot')}<span class="cap">Chữ An Tâm có khói</span></div>
 </div>
</div></section>

<section class="page banh"><div class="w">
 {ph(4, 'Quy tắc dùng')}
 <div class="head"><h2>Chừa chỗ <em>cho bánh thở</em></h2><p>Quanh logo luôn chừa khoảng trống bằng chiều cao chữ Â của biểu tượng (ký hiệu A). Không kéo méo, không xoay, không đổi màu, không thêm hiệu ứng.</p></div>
 <div class="rules">
  <div class="rbox"><div class="cz"><i class="t">A</i><i class="l">A</i>{logo('seal')}</div></div>
  <div class="rbox"><div class="mins">
   <div><span style="width:120px">{logo('seal')}</span>Tem tròn<br>nhỏ nhất 25 mm, 120 px</div>
   <div><span style="width:150px">{logo('horiz')}</span>Bản ngang<br>nhỏ nhất 35 mm, 150 px</div>
   <div><span style="width:34px">{logo('mark')}</span>Biểu tượng<br>nhỏ nhất 32 px</div></div></div>
 </div>
 <div class="dont">{donts}</div>
</div></section>

<section class="page"><div class="w">
 {ph(5, 'Màu')}
 <div class="head"><h2>Màu của <em>bếp nướng</em></h2><p>Đỏ cà chua dẫn đầu, kem bột làm nền, vàng ngô để nhấn. Nâu mực cho chữ. Xanh rau chỉ điểm xuyết cho cảm giác tươi.</p></div>
 <div class="pal">
  <div class="sw" style="background:var(--do);color:var(--bot)"><span class="n">55%</span><b>Đỏ cà chua</b>#D62718<br>Đỏ đậm #A5170D</div>
  <div class="sw" style="background:#fff;border:2px solid var(--line)"><span class="n">25%</span><b>Kem bột</b>#FFF3DD<br>Bánh #F4D59B</div>
  <div class="sw small" style="background:var(--vang)"><span class="n">10%</span><b>Vàng ngô</b>#FFB400</div>
  <div class="sw small" style="background:var(--muc);color:var(--bot)"><span class="n">8%</span><b>Nâu mực</b>#3A1A12</div>
  <div class="sw small" style="background:var(--rau);color:var(--bot)"><span class="n">2%</span><b>Xanh rau</b>#3E8E41</div>
 </div>
 <div class="pair">
  <div style="background:var(--do);color:var(--bot)">Aa<small>Kem trên đỏ · 4,6:1</small></div>
  <div style="background:var(--bot);color:var(--muc);border:2px solid var(--line)">Aa<small>Mực trên kem · 14:1</small></div>
  <div style="background:var(--vang);color:var(--muc)">Aa<small>Mực trên vàng · 8,8:1</small></div>
  <div style="background:var(--banh);color:var(--muc)">Aa<small>Mực trên bánh · 11:1</small></div>
 </div>
 <p class="note">Không đặt chữ vàng hay chữ xanh trên nền đỏ. Chữ kem trên đỏ dùng cho chữ từ 18 px đậm trở lên. Tỉ lệ đỏ dẫn đầu giữ theo yêu cầu ban đầu của công ty (đỏ nhiều nhất, trắng kem thứ hai, vàng để nhấn).</p>
</div></section>

<section class="page banh"><div class="w">
 {ph(6, 'Chữ')}
 <div class="head"><h2>Chữ tròn, <em>đọc dễ</em></h2><p>Hai họ chữ miễn phí trên Google Fonts, đủ dấu tiếng Việt. Gluten cho tiêu đề, tên món, câu khẩu hiệu. Nunito cho nội dung, giá, thông tin liên hệ.</p></div>
 <div class="type">
  <div class="tcard"><div class="big">Ẩm</div><h3>Gluten · tiêu đề</h3><p>Đậm 600 và 800. Nét tròn như bột. Chỉ dùng cho chữ lớn, không dùng cho đoạn văn.</p><p class="chars" style="font-family:var(--hien);font-weight:600">ĂÂĐÊÔƠƯ ắằẳẵặ ấầẩẫậ ếềểễệ ốồổỗộ ớờởỡợ ứừửữự</p></div>
  <div class="tcard"><div class="big n">Ẩm</div><h3>Nunito · nội dung</h3><p>Thường 400, đậm 700 và 800. Đầu nét tròn, hợp với Gluten, dễ đọc ở cỡ nhỏ.</p><p class="chars">ĂÂĐÊÔƠƯ ắằẳẵặ ấầẩẫậ ếềểễệ ốồổỗộ ớờởỡợ ứừửữự 0123456789</p></div>
  <div class="tcard scale">
   <div><span class="k1">Nóng giòn mỗi ngày</span><small>Tiêu đề lớn<br>Gluten 800</small></div>
   <div><span class="k2">Taco giao tận văn phòng</span><small>Tiêu đề phụ<br>Gluten 800</small></div>
   <div><span class="k3">Nhượng quyền cửa hàng</span><small>Nhãn<br>Nunito 800, giãn 20%</small></div>
   <div><span class="k4">Bữa nhẹ tiện lợi cho nhân viên văn phòng. Đặt qua hotline 0348.635.222 hoặc antamfoods.com.</span><small>Nội dung<br>Nunito 400</small></div>
  </div>
 </div>
</div></section>

<section class="page dark"><div class="w">
 {ph(7, 'Hoạ tiết')}
 <div class="head"><h2>Hoạ tiết <em>ngon mắt</em></h2><p>Bốn hoạ tiết lấy từ bếp: đốm nướng trên bánh, sóng rau, mái hiên sọc đỏ của quán, và các biểu tượng nguyên liệu. Mỗi ấn phẩm chọn một.</p></div>
 <div class="pats">
  <figure class="pat">{pat_spots()}<figcaption><b>Đốm nướng</b>Nền bao bì bánh tortillas.</figcaption></figure>
  <figure class="pat">{pat_lettuce()}<figcaption><b>Sóng rau</b>Giấy lót khay, túi.</figcaption></figure>
  <figure class="pat">{pat_awning()}<figcaption><b>Mái hiên</b>Biển hiệu, quầy, đầu thực đơn.</figcaption></figure>
  <figure class="pat">{pat_icons()}<figcaption><b>Nguyên liệu</b>Bánh, taco, ớt, khói. Nền mạng xã hội.</figcaption></figure>
 </div>
</div></section>

<section class="page"><div class="w">
 {ph(8, 'Hình ảnh')}
 <div class="head"><h2>Món nào cũng <em>trên đĩa bánh</em></h2><p>Minh hoạ sản phẩm đặt trên chiếc đĩa tròn màu bánh, viền nét đứt. Ảnh chụp thật theo cùng tinh thần: món ăn nóng, gần, rõ nhân.</p></div>
 <div class="prod">{prods}</div>
 <div class="photo">
  <div><h3>Ảnh chụp nên</h3><ul><li>Bánh thật, thấy đốm nướng, có hơi nóng.</li><li>Chụp gần, thấy rõ nhân thịt, rau.</li><li>Ánh sáng ấm, nền gỗ hoặc giấy kem.</li><li>Có tay người cầm, cắn dở: cảm giác ăn ngay.</li></ul></div>
  <div><h3>Ảnh chụp tránh</h3><ul><li>Ảnh mạng, ảnh kho có sẵn.</li><li>Đèn trắng lạnh, món ăn nguội, khô.</li><li>Nền rối, nhiều đạo cụ không liên quan.</li><li>Mũ rộng vành, xương rồng, ria mép.</li></ul></div>
 </div>
</div></section>

<section class="page banh"><div class="w">
 {ph(9, 'Ứng dụng')}
 <div class="head"><h2>Từ quầy bánh <em>tới tay khách</em></h2><p>Mô phỏng dùng đúng logo, màu, chữ của cẩm nang. Chỗ ghi [Cần điền] và [Giá] chờ thông tin thật từ công ty.</p></div>
 <div class="apps">
  <div class="app a12"><span class="cap">Mặt tiền cửa hàng nhượng quyền</span>{store()}</div>
  <div class="app a4 bgA"><span class="cap">Túi giấy</span>{bag()}</div>
  <div class="app a4 bgB"><span class="cap">Gói bánh tortillas</span>{pack()}</div>
  <div class="app a4 phone-wrap"><span class="cap">Bài đăng Facebook</span>{post()}</div>
  <div class="app a7 bgC"><span class="cap">Hộp đựng món</span>{box()}</div>
  <div class="app a5 bgD"><span class="cap">Giấy gói doner cuộn</span>{wrap_paper()}</div>
  <div class="app a5 menu-wrap"><span class="cap">Bảng thực đơn</span>{menu()}</div>
  <div class="app a7">{card()}<span class="cap">Danh thiếp</span></div>
  <div class="app a4 bgA"><span class="cap">Tạp dề nhân viên</span>{apron()}</div>
  <div class="app a8"><span class="cap">Ảnh đại diện, Zalo OA</span><div class="avs">
   <div style="background:var(--do)">{logo('mark_tron')}</div><div class="sq" style="background:var(--bot)">{logo('mark_tron')}</div><div style="background:var(--vang)">{logo('mark_tron')}</div></div></div>
 </div>
</div></section>

<footer class="back"><div class="w">
 {logo('seal_do')}
 <p>Bản đề xuất hướng Bột &amp; Lửa, chờ công ty duyệt. Logo gốc vẫn là logo chính thức cho tới khi duyệt. Chữ Gluten và Nunito dùng theo giấy phép SIL Open Font License.</p>
 <div class="ct"><small>Liên hệ</small>0348.635.222<br>antamfoods.com</div>
</div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

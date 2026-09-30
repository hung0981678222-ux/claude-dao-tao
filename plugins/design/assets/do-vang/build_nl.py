"""Bộ nhận diện Ẩm Thực An Tâm theo tinh thần hình mẫu Nonla. Chạy: python3 build_nl.py OUT.html"""
import base64
import os
import sys

import logo_nl as L
from logo_nl import OUT, DO, DO_DAM, VANG, KEM, MUC, BO, RAU

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
MH = os.environ.get("MINH_HOA", "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa")
RG = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
}


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def ill(n):
    return b64(f"{MH}/{n}.svg", "image/svg+xml")


def fontfaces():
    faces = []
    for sub, rg in RG.items():
        faces.append(("Fraunces AT", 900, os.path.join(HERE, f"fr50-{sub}-900.woff2"), rg))
        faces.append(("Anton", 400, os.path.join(SCR, f"anton/package/files/anton-{sub}-400-normal.woff2"), rg))
        for w in (400, 600):
            faces.append(("Be Vietnam Pro", w, os.path.join(SCR, f"cc/be-vietnam-pro/files/be-vietnam-pro-{sub}-{w}-normal.woff2"), rg))
    return "\n".join(f"@font-face{{font-family:'{n}';font-weight:{w};font-display:swap;src:url({b64(p, 'font/woff2')}) format('woff2');unicode-range:{rg}}}" for n, w, p, rg in faces)


def lg(key, cls=""):
    return OUT[key].replace("<svg ", f'<svg class="lg {cls}" ', 1)


def taco_row_pattern(bg, fg, fg2, uid):
    """Hàng taco nhỏ nghiêng lặp lại, như hoạ tiết hàng nón của hình mẫu."""
    items = ""
    for r in range(6):
        for c in range(9):
            x, y = c * 70 + (35 if r % 2 else 0) - 20, r * 46 + 30
            items += L.taco(x, y, 30, fg if (r + c) % 4 else fg2, bg, tilt=-18)
    return f'<svg viewBox="0 0 560 290" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="560" height="290" fill="{bg}"/>{items}</svg>'


def step_pattern(bg, fg):
    s = ""
    for r in range(8):
        for c in range(10):
            x, y = c * 60 + (30 if r % 2 else 0), r * 40 + 26
            s += f'<path d="M{x},{y} l24,-14 l0,14" fill="none" stroke="{fg}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>'
    return f'<svg viewBox="0 0 560 320" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="560" height="320" fill="{bg}"/>{s}</svg>'


def dash_line(color):
    return (f'<svg viewBox="0 0 560 20" preserveAspectRatio="none" aria-hidden="true" class="dash">'
            + "".join(f'<path d="M{x},14 l10,-8 l0,8" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>' for x in range(4, 560, 22)) + "</svg>")


CSS = """
/* Bố cục: hai màu tương phản mạnh như hình mẫu (đỏ + vàng), chữ thường đậm có chân cho tên, chữ cao hẹp cho tiêu đề. */
:root{--do:#D7150E;--do2:#A90F09;--vang:#FFC53D;--kem:#FFF6E6;--muc:#3A1410;--bo:#FFE3A3;--rau:#5BA94A;--xam:#6D5049;
--ten:'Fraunces AT',Georgia,serif;--hep:'Anton','Arial Narrow',sans-serif;--noi:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--muc);font:400 17px/1.6 var(--noi);-webkit-font-smoothing:antialiased}
img,svg{max-width:100%}
svg.lg{display:block;width:100%;height:auto}
.w{max-width:1200px;margin:0 auto;padding-inline:40px}
section{padding-block:96px}
.red{background:var(--do);color:var(--kem)}
.bo{background:var(--bo)}
.dark{background:var(--muc);color:var(--kem)}
.kick{font:400 18px/1 var(--hep);letter-spacing:.06em;color:var(--do);display:flex;gap:12px;align-items:center}
.red .kick,.dark .kick{color:var(--vang)}
.kick::before{content:"";width:34px;height:3px;background:currentColor}
h2{font:900 clamp(42px,6vw,80px)/.98 var(--ten);letter-spacing:-.02em;margin-top:14px;text-wrap:balance}
h2 span{color:var(--do)}.red h2 span,.dark h2 span{color:var(--vang)}
.lead{max-width:60ch;margin-top:18px;font-size:18px;opacity:.9}
.hl{font:400 clamp(26px,3vw,40px)/1.05 var(--hep);letter-spacing:.01em;text-transform:uppercase}

/* băng rôn đầu trang */
.hero{background:var(--do);color:var(--kem);overflow:hidden}
.hero .w{display:grid;grid-template-columns:.9fr 1.3fr;gap:32px;align-items:center;padding-block:56px 40px}
.hero .masc{max-width:360px;justify-self:center;filter:drop-shadow(0 20px 24px rgba(80,0,0,.35))}
.hero .lg{max-width:620px}
.hero .tag{font:400 clamp(20px,2.6vw,32px)/1.1 var(--hep);margin-top:26px;color:var(--kem)}
.hero-pat{height:120px;overflow:hidden}
.hero-pat svg{width:100%;height:120px;display:block}

/* học từ hình mẫu */
.learn{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}
.learn div{background:#fff;border-radius:24px;padding:26px;border:2px solid #F0DCC0}
.learn b{display:block;font:400 24px/1.05 var(--hep);color:var(--do);margin-bottom:10px;text-transform:uppercase}
.learn p{font-size:15px;color:var(--xam)}

/* logo */
.lgrid{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:48px}
.cell{border-radius:28px;display:grid;place-items:center;padding:52px 40px;min-height:300px;position:relative}
.cell .cap{position:absolute;left:22px;bottom:16px;font:400 14px/1 var(--hep);letter-spacing:.06em;opacity:.8}
.c4{grid-column:span 4}.c2{grid-column:span 2}.c3{grid-column:span 3}
.cell .lg{max-width:520px}
.cell.c2 .lg{max-width:170px}
.bg-do{background:var(--do);color:var(--kem)}.bg-kem{background:#fff;border:2px solid #F0DCC0}.bg-bo{background:var(--bo)}.bg-muc{background:var(--muc);color:var(--kem)}.bg-trang{background:#fff;border:2px solid #F0DCC0}
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:16px}
.why div{border-top:3px solid var(--do);padding-top:14px;font-size:15px}
.why b{display:block;font:400 22px/1.1 var(--hep);text-transform:uppercase;margin-bottom:6px}

/* linh vật */
.masc-row{display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:16px;margin-top:48px;align-items:stretch}
.mcard{border-radius:28px;padding:36px 30px 26px;display:flex;flex-direction:column;align-items:center;gap:14px}
.mcard .lg{max-width:240px}
.mcard b{font:400 26px/1 var(--hep);text-transform:uppercase}
.mnotes{background:#fff;border-radius:28px;padding:32px;display:grid;gap:16px;align-content:start;border:2px solid #F0DCC0;color:var(--muc)}
.mnotes div{display:grid;grid-template-columns:34px 1fr;gap:12px;font-size:15px}
.mnotes i{font:400 22px/1.2 var(--hep);color:var(--do);font-style:normal}

/* màu */
.pal{display:grid;grid-template-columns:6fr 3fr 1fr;gap:14px;margin-top:48px;height:340px}
.sw{min-width:0;border-radius:28px;padding:26px 22px;display:flex;flex-direction:column;justify-content:space-between;font:600 13px/1.6 var(--noi)}
.sw .n{font:400 72px/1 var(--hep)}
.sw b{font:400 26px/1 var(--hep);display:block;margin-bottom:6px;text-transform:uppercase}
.sub{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:14px}
.sub div{border-radius:20px;padding:18px 20px;font:600 13px/1.5 var(--noi);display:flex;justify-content:space-between;align-items:end;gap:10px}
.sub b{font:400 22px/1 var(--hep);text-transform:uppercase}
.note{font-size:14px;color:var(--xam);margin-top:16px;max-width:80ch}

/* chữ */
.types{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:16px;margin-top:48px}
.tc{background:#fff;border-radius:28px;padding:32px;border:2px solid #F0DCC0}
.tc .big{font-size:120px;line-height:.95;color:var(--do)}
.tc h3{font:400 26px/1 var(--hep);text-transform:uppercase;margin-top:14px}
.tc p{font-size:15px;color:var(--xam);margin-top:8px}
.tc .ch{font-size:15px;margin-top:12px;letter-spacing:.03em;word-break:break-all}
.sample{margin-top:16px;background:var(--do);color:var(--kem);border-radius:28px;padding:40px;display:grid;grid-template-columns:1.2fr 1fr;gap:32px;align-items:center}
.sample h3{font:900 60px/1 var(--ten);letter-spacing:-.02em}
.sample h3 span{color:var(--vang)}
.sample .box{border:3px solid var(--kem);border-radius:22px;padding:22px 26px;font:400 34px/1.12 var(--hep);text-align:center;text-transform:uppercase}
.sample p{margin-top:14px;font-size:16px;opacity:.9}

/* bậc thang */
.stairs{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-top:48px}
.stairs figure{border-radius:28px;display:grid;place-items:center;padding:30px;min-height:420px}
.stairs figcaption{font:400 16px/1 var(--hep);letter-spacing:.05em;margin-top:12px;opacity:.8}
.stairs .lg{max-height:380px;width:auto}

/* hoạ tiết */
.pats{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:48px}
.pats figure svg{width:100%;height:auto;display:block;border-radius:24px;aspect-ratio:560/290}
.pats figcaption{margin-top:10px;font-size:15px}
.pats figcaption b{font:400 22px/1 var(--hep);text-transform:uppercase;display:block;margin-bottom:4px}
.dash{display:block;width:100%;height:20px;margin-top:6px}
.dashes{background:#fff;border-radius:24px;padding:24px 28px;display:grid;gap:16px;border:2px solid #F0DCC0;margin-top:16px}

/* sản phẩm */
.prod{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}
.prod .card{border-radius:28px;aspect-ratio:4/5;display:flex;flex-direction:column;justify-content:space-between;padding:22px;overflow:hidden}
.prod .card b{font:400 28px/1 var(--hep);text-transform:uppercase}
.prod .card small{font:600 13px/1.4 var(--noi);opacity:.85}
.prod img{width:92%;align-self:center}

/* ứng dụng */
.apps{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:48px}
.app{border-radius:28px;overflow:hidden;position:relative}
.app .cap{position:absolute;left:16px;top:14px;z-index:2;font:400 14px/1 var(--hep);letter-spacing:.06em;background:var(--kem);color:var(--muc);padding:8px 12px;border-radius:999px}
.a12{grid-column:span 12}.a7{grid-column:span 7}.a5{grid-column:span 5}.a6{grid-column:span 6}.a4{grid-column:span 4}.a8{grid-column:span 8}
.banner{background:var(--do);color:var(--kem);display:grid;grid-template-columns:.8fr 1.4fr;align-items:center;gap:20px;padding:40px 48px 28px}
.banner .lg.m{max-width:260px;justify-self:center}
.banner .hl{margin-top:14px;color:var(--kem)}
.promo{background:var(--do);color:var(--kem);aspect-ratio:1;display:flex;flex-direction:column;align-items:center;padding:56px 28px 0;gap:18px;position:relative}
.promo .box{border:3px solid var(--kem);border-radius:18px;padding:14px 22px;font:400 clamp(24px,3vw,38px)/1.1 var(--hep);text-align:center;text-transform:uppercase}
.promo .pk{position:relative;z-index:2;width:62%}
.promo .pt{position:absolute;left:0;right:0;bottom:0;height:40%}
.promo .pt svg{width:100%;height:100%}
.bgpk{background:linear-gradient(160deg,#F3E4CC,#E3C9A2);display:grid;place-items:center;padding:56px 24px 28px}
.bgbag{background:linear-gradient(160deg,#FFE9BE,#F8CE79);display:grid;place-items:center;padding:56px 24px 28px}
.store{background:#2A1512;padding:56px 36px 0}
.card-sc{background:linear-gradient(160deg,#EBD6B6,#D6B88C);aspect-ratio:4/3;position:relative}
.nc{position:absolute;width:52%;aspect-ratio:90/54;border-radius:10px;box-shadow:0 18px 30px -12px rgba(60,20,10,.5)}
.nc.f{background:var(--do);left:7%;top:20%;transform:rotate(-8deg);display:grid;place-items:center;padding:6% 10%}
.nc.b{background:var(--kem);right:7%;bottom:13%;transform:rotate(5deg);padding:6% 7%;display:grid;grid-template-rows:auto 1fr auto;font:400 clamp(8px,1vw,12px)/1.4 var(--noi)}
.nc.b .lg{width:3.2em;height:3.2em}
.nc.b .nm{align-self:center}.nc.b .nm b{display:block;font:400 1.8em/1.1 var(--hep);text-transform:uppercase}
.nc.b .ct{display:flex;gap:1.4em;flex-wrap:wrap;font-weight:600;border-top:2px solid var(--do);padding-top:.6em}
.avs{background:var(--bo);display:flex;justify-content:center;align-items:center;gap:26px;flex-wrap:wrap;padding:60px 20px 40px}
.avs .av{width:130px;aspect-ratio:1;border-radius:50%;overflow:hidden;display:grid;place-items:center;box-shadow:0 10px 20px -12px rgba(0,0,0,.4)}
.avs .av .lg{width:100%}
.back{background:var(--muc);color:var(--kem);padding-block:64px 44px}
.back .w{display:grid;grid-template-columns:auto 1fr auto;gap:36px;align-items:center}
.back .lg{width:260px}
.back p{font-size:14px;opacity:.72;max-width:60ch}
.back .ct{font:400 22px/1.4 var(--hep);text-align:right}
@media (max-width:900px){.w{padding-inline:20px}section{padding-block:64px}
 .hero .w{grid-template-columns:1fr}.hero .masc{max-width:220px}
 .learn,.why{grid-template-columns:1fr 1fr}.lgrid{grid-template-columns:1fr 1fr}.c4,.c3{grid-column:1/-1}.c2{grid-column:span 1}.cell{min-height:200px;padding:36px 20px}
 .masc-row{grid-template-columns:1fr 1fr}.mnotes{grid-column:1/-1}
 .pal{grid-template-columns:1fr 1fr;height:auto}.sw .n{font-size:52px}.sw{min-height:180px}.sw:first-child{grid-column:1/-1}.sub{grid-template-columns:1fr}
 .types,.stairs,.pats{grid-template-columns:1fr}.sample{grid-template-columns:1fr;padding:28px}.sample h3{font-size:42px}
 .prod{grid-template-columns:1fr 1fr}
 .a12,.a7,.a5,.a6,.a4,.a8{grid-column:1/-1}.banner{grid-template-columns:1fr;padding:48px 22px 24px}
 .back .w{grid-template-columns:1fr}.back .ct{text-align:left}}
@media (max-width:480px){.learn,.why{grid-template-columns:1fr}}
"""


def pack_svg():
    return f"""<svg viewBox="0 0 420 470" role="img" aria-label="Hộp bánh tortillas" style="display:block;width:100%;height:auto">
<defs><filter id="pks" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="10"/></filter>
<clipPath id="pkw"><rect x="150" y="190" width="190" height="200" rx="16"/></clipPath></defs>
<ellipse cx="210" cy="448" rx="170" ry="14" fill="#000" opacity=".25" filter="url(#pks)"/>
<path d="M330,40 L380,20 L380,420 L330,440 Z" fill="#F1CF7E"/>
<path d="M40,40 L330,40 L330,440 L40,440 Z" fill="{BO}"/>
<path d="M40,40 L90,20 L380,20 L330,40 Z" fill="#FFEEC4"/>
<g transform="translate(70 62)">{OUT['wm_bo'].replace('<svg ', '<svg width="230" height="92" ', 1)}</g>
<rect x="150" y="190" width="190" height="200" rx="16" fill="#FFF8EA"/>
<image href="{ill('banh-tortillas')}" x="140" y="200" width="210" height="210" clip-path="url(#pkw)"/>
<rect x="150" y="190" width="190" height="200" rx="16" fill="none" stroke="{DO}" stroke-width="4"/>
<g transform="translate(34 196)">{OUT['mascot'].replace('<svg ', '<svg width="150" height="141" ', 1)}</g>
<text x="185" y="416" text-anchor="middle" fill="{DO}" style="font:400 26px 'Anton',sans-serif;letter-spacing:.02em">BÁNH TORTILLAS</text>
<text x="185" y="434" text-anchor="middle" fill="{MUC}" style="font:600 11px 'Be Vietnam Pro',sans-serif">[Cần điền: khối lượng, hạn dùng]</text>
</svg>"""


def bag_svg():
    return f"""<svg viewBox="0 0 420 480" role="img" aria-label="Túi giấy" style="display:block;width:100%;height:auto">
<defs><filter id="bgs" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="10"/></filter></defs>
<ellipse cx="200" cy="458" rx="160" ry="14" fill="#000" opacity=".25" filter="url(#bgs)"/>
<path d="M140,110 C140,30 250,30 250,110" fill="none" stroke="{DO_DAM}" stroke-width="9" stroke-linecap="round"/>
<path d="M300,100 L350,85 L350,440 L300,452 Z" fill="{DO_DAM}"/>
<path d="M60,100 H300 V452 H60 Z" fill="{DO}"/>
<g transform="translate(80 150)">{OUT['wm_do'].replace('<svg ', '<svg width="200" height="80" ', 1)}</g>
<g transform="translate(118 272)">{OUT['mascot'].replace('<svg ', '<svg width="124" height="117" ', 1)}</g>
<text x="180" y="425" text-anchor="middle" fill="{VANG}" style="font:400 17px 'Anton',sans-serif;letter-spacing:.06em">ANTAMFOODS.COM · 0348.635.222</text>
</svg>"""


def store_svg():
    return f"""<svg viewBox="0 0 1100 520" role="img" aria-label="Mặt tiền cửa hàng" style="display:block;width:100%;height:auto">
<defs><linearGradient id="stg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE7B8"/><stop offset="1" stop-color="#F2B35F"/></linearGradient></defs>
<rect x="40" y="0" width="1020" height="520" fill="{KEM}"/>
<rect x="40" y="0" width="1020" height="140" fill="{DO}"/>
<g transform="translate(90 18)">{OUT['wm_do'].replace('<svg ', '<svg width="300" height="120" ', 1)}</g>
<text x="1010" y="84" text-anchor="end" fill="{KEM}" style="font:400 34px 'Anton',sans-serif">SẢN PHẨM TẬN TÂM - PHÁT TRIỂN XỨNG TẦM</text>
<g transform="translate(40 140)">{taco_row_pattern(DO_DAM, VANG, KEM, 's').replace('<svg ', '<svg width="1020" height="46" ', 1)}</g>
<rect x="90" y="220" width="380" height="300" rx="10" fill="url(#stg)" stroke="{MUC}" stroke-width="10"/>
<image href="{ill('doner-tru-quay')}" x="140" y="240" width="270" height="270"/>
<rect x="520" y="220" width="170" height="300" fill="{MUC}"/><rect x="534" y="234" width="142" height="286" fill="url(#stg)" opacity=".85"/>
<g transform="translate(555 300)">{OUT['mark_do'].replace('<svg ', '<svg width="100" height="100" ', 1)}</g>
<rect x="740" y="220" width="270" height="300" rx="10" fill="url(#stg)" stroke="{MUC}" stroke-width="10"/>
<g transform="translate(760 300)">{OUT['mascot2'].replace('<svg ', '<svg width="230" height="216" ', 1)}</g>
</svg>"""


def page():
    st1 = L.stairs(["BÁNH", "NÓNG", "CUỘN", "MỀM", "ĂN LÀ", "AN TÂM"], VANG, hi=KEM, hi_idx=(5,))
    st2 = L.stairs(["BỮA", "NHẸ", "VĂN", "PHÒNG"], DO, hi=MUC, hi_idx=(3,))
    st3 = L.stairs(["DONER", "KEBAB", "GIAO", "LIỀN"], KEM, hi=VANG, hi_idx=(3,))
    prods = "".join(f'<div class="card" style="background:{bg};color:{fg}"><b>{t}</b><img src="{ill(n)}" alt="{t}"><small>{d}</small></div>' for n, t, d, bg, fg in [
        ("banh-tortillas", "Bánh tortillas", "Bánh nền, bán sỉ cho doanh nghiệp", VANG, MUC),
        ("taco", "Taco", "Gập đôi, nhân đầy", DO, KEM),
        ("doner-tru-quay", "Doner kebab", "Thịt nướng trụ quay", BO, MUC),
        ("doner-cuon", "Doner cuộn", "Cuộn chặt, ăn gọn", MUC, KEM)])
    return f"""<title>An Tâm Đỏ Vàng</title>
<style>{fontfaces()}
{CSS}</style>

<header class="hero"><div class="w">
 {lg('mascot', 'masc')}
 <div>{lg('wm_do')}<p class="tag">SẢN PHẨM TẬN TÂM - PHÁT TRIỂN XỨNG TẦM</p></div>
</div><div class="hero-pat">{taco_row_pattern(DO, "#E8483F", VANG, 'h')}</div></header>

<section><div class="w">
 <p class="kick">HỌC TỪ HÌNH MẪU ANH CHỊ GỬI</p>
 <h2>Đỏ và vàng, <span>một chiếc taco</span> làm dấu mũ</h2>
 <p class="lead">Hình mẫu Nonla mạnh vì bốn điều. Bộ nhận diện này làm theo đúng bốn điều đó, thay nón lá và hạt cà phê bằng chiếc bánh của An Tâm.</p>
 <div class="learn">
  <div><b>Hai màu đối chọi</b><p>Nonla: xanh dương và vàng. An Tâm: đỏ và vàng, màu của cà chua và vỏ bánh nướng.</p></div>
  <div><b>Tên chữ thường, đậm, có chân</b><p>Chữ "an tâm" viết thường, nét đậm có chân, thân thiện mà vẫn chắc.</p></div>
  <div><b>Sản phẩm nằm trong chữ</b><p>Nonla đặt nón lên chữ n, hạt cà phê thay chữ o. An Tâm đặt chiếc taco làm dấu mũ chữ â.</p></div>
  <div><b>Linh vật dễ thương</b><p>Bé Tâm: chiếc taco biết cười, má hồng, dùng trên bao bì, bài đăng, cửa hàng.</p></div>
 </div>
</div></section>

<section class="bo"><div class="w">
 <p class="kick">LOGO</p>
 <h2>ẨM THỰC <span>an tâm</span></h2>
 <p class="lead">ẨM THỰC chữ cao hẹp nằm trên đầu chữ "an t". Tên "an tâm" chữ thường đậm có chân, dấu mũ là chiếc taco nghiêng. Dưới chân là dòng sản phẩm, dài đúng bằng tên.</p>
 <div class="lgrid">
  <div class="cell c4 bg-do">{lg('wm_do')}<span class="cap">BẢN CHÍNH · VÀNG TRÊN ĐỎ</span></div>
  <div class="cell c2 bg-kem">{lg('mark_do')}<span class="cap">BIỂU TƯỢNG</span></div>
  <div class="cell c3 bg-kem" style="color:var(--muc)">{lg('wm_kem')}<span class="cap">ĐỎ TRÊN KEM</span></div>
  <div class="cell c3 bg-muc">{lg('wm_muc')}<span class="cap">VÀNG TRÊN NÂU</span></div>
  <div class="cell c2 bg-do">{lg('wm_gon_do')}<span class="cap">BẢN GỌN</span></div>
  <div class="cell c2 bg-trang" style="color:var(--muc)">{lg('wm_den')}<span class="cap">MỘT MÀU, CON DẤU</span></div>
  <div class="cell c2 bg-bo" style="color:var(--muc);border:2px solid #F0CF86">{lg('mark_vang')}<span class="cap">BIỂU TƯỢNG TRÊN VÀNG</span></div>
 </div>
 <div class="why">
  <div><b>Đọc là biết đồ ăn</b>Chiếc taco nằm ngay trong tên, dòng sản phẩm ghi rõ bánh tortillas và doner kebab.</div>
  <div><b>Vẫn đọc đúng "tâm"</b>Chiếc taco nằm đúng chỗ dấu mũ, giống cách Nonla đặt nón lên chữ n.</div>
  <div><b>Nhỏ vẫn rõ</b>Bản gọn và biểu tượng chữ â dùng cho ảnh đại diện, tem nhỏ, ly, hộp.</div>
 </div>
</div></section>

<section class="red"><div class="w">
 <p class="kick">LINH VẬT</p>
 <h2>Bé Tâm, <span>chiếc taco biết cười</span></h2>
 <div class="masc-row">
  <div class="mcard" style="background:var(--do2)">{lg('mascot')}<b>Chào khách</b></div>
  <div class="mcard" style="background:var(--bo);color:var(--muc)">{lg('mascot2')}<b>Nháy mắt</b></div>
  <div class="mnotes">
   <div><i>1</i><span>Vỏ bánh vàng có đốm nướng, nhân thịt, rau, cà chua: nhìn là biết taco.</span></div>
   <div><i>2</i><span>Mắt tròn, má hồng, miệng cười nhỏ: cùng kiểu mặt với linh vật của hình mẫu.</span></div>
   <div><i>3</i><span>Dùng trên hộp, túi, bài đăng, biển cửa hàng. Không đặt linh vật đè lên logo.</span></div>
   <div><i>4</i><span>Đây là bản vẽ phẳng. Muốn có bản 3D như Nonla thì cần người dựng hình 3D làm theo bản này.</span></div>
  </div>
 </div>
</div></section>

<section><div class="w">
 <p class="kick">MÀU</p>
 <h2>Đỏ 60, trắng 30, <span>vàng 10</span></h2>
 <p class="lead">Đúng tỉ lệ công ty đặt từ đầu. Đỏ làm nền lớn như màu xanh của hình mẫu, vàng cho tên và điểm nhấn.</p>
 <div class="pal">
  <div class="sw" style="background:var(--do);color:var(--kem)"><span class="n">60%</span><span><b>Đỏ An Tâm</b>#D7150E · đỏ đậm #A90F09</span></div>
  <div class="sw" style="background:#fff;border:2px solid #F0DCC0"><span class="n">30%</span><span><b>Kem trắng</b>#FFF6E6</span></div>
  <div class="sw" style="background:var(--vang)"><span class="n">10%</span><span><b>Vàng</b>#FFC53D</span></div>
 </div>
 <div class="sub">
  <div style="background:var(--muc);color:var(--kem)"><b>Nâu mực</b>#3A1410 · chữ nhỏ</div>
  <div style="background:var(--bo)"><b>Vàng bơ</b>#FFE3A3 · nền bao bì</div>
  <div style="background:var(--rau);color:#fff"><b>Xanh rau</b>#5BA94A · chỉ trong minh hoạ</div>
 </div>
 <p class="note">Chữ vàng trên đỏ chỉ dùng cho chữ lớn (tên, tiêu đề từ 24 px). Chữ nhỏ trên đỏ dùng màu kem. Không dùng xanh rau làm màu chữ.</p>
</div></section>

<section class="bo"><div class="w">
 <p class="kick">CHỮ</p>
 <h2>Ba kiểu chữ, <span>ba việc</span></h2>
 <div class="types">
  <div class="tc"><div class="big" style="font-family:var(--ten);font-weight:900">ăn ngon</div><h3>Fraunces đậm · tên, câu chính</h3><p>Chữ thường, đậm, có chân mềm. Dùng cho tên món, câu khẩu hiệu ngắn.</p><p class="ch" style="font-family:var(--ten);font-weight:900">ă â đ ê ô ơ ư ấ ầ ẩ ẫ ậ ế ề ể ễ ệ</p></div>
  <div class="tc"><div class="big" style="font-family:var(--hep)">TƯƠI</div><h3>Anton · tiêu đề in hoa</h3><p>Chữ cao hẹp, như "HỘP CÀ PHÊ VỊ SỮA DỪA" của hình mẫu. Dùng cho tiêu đề, giá, chữ bậc thang.</p></div>
  <div class="tc"><div class="big" style="font-family:var(--noi);font-weight:600">Aa</div><h3>Be Vietnam Pro · nội dung</h3><p>Chữ đọc, thông tin liên hệ, thành phần, hướng dẫn.</p></div>
 </div>
 <div class="sample"><div><h3>gập đôi là <span>ngon</span></h3><p>Tiêu đề bài đăng dùng Fraunces, khung chữ in hoa dùng Anton trong khung viền bo tròn, giống hình mẫu.</p></div><div class="box">BÁNH TORTILLAS<br>GIAO TẬN VĂN PHÒNG</div></div>
</div></section>

<section class="dark"><div class="w">
 <p class="kick">CHỮ BẬC THANG</p>
 <h2>Giữ lại <span>chữ bậc thang</span></h2>
 <p class="lead">Kiểu chữ cầu thang anh chị chọn giữ lại, dựng bằng Anton trên góc 30 độ. Dùng cho bài đăng chiến dịch, poster, tường cửa hàng. Tạo thêm câu mới bằng trang Máy tạo chữ bậc thang.</p>
 <div class="stairs">
  <figure style="background:var(--do)">{st1.replace('<svg ', '<svg class="lg" ', 1)}</figure>
  <figure style="background:var(--vang)">{st2.replace('<svg ', '<svg class="lg" ', 1)}</figure>
  <figure style="background:var(--do2)">{st3.replace('<svg ', '<svg class="lg" ', 1)}</figure>
 </div>
</div></section>

<section><div class="w">
 <p class="kick">HOẠ TIẾT</p>
 <h2>Hàng taco <span>như hàng nón</span></h2>
 <p class="lead">Hình mẫu lặp hàng nón nhỏ chéo nhau. An Tâm lặp hàng taco nhỏ nghiêng, và hàng bậc thang lấy từ chữ bậc thang.</p>
 <div class="pats">
  <figure>{taco_row_pattern(DO, "#F0574D", VANG, 'p1')}<figcaption><b>Hàng taco</b>Chân bài đăng, băng rôn, thành túi.</figcaption></figure>
  <figure>{step_pattern(VANG, DO)}<figcaption><b>Hàng bậc thang</b>Nền hộp, giấy gói, tường cửa hàng.</figcaption></figure>
 </div>
 <div class="dashes">{dash_line(DO)}{dash_line(VANG)}{dash_line(MUC)}</div>
</div></section>

<section class="bo"><div class="w">
 <p class="kick">MINH HOẠ SẢN PHẨM</p>
 <h2>Giữ lại <span>tranh sản phẩm</span></h2>
 <div class="prod">{prods}</div>
</div></section>

<section><div class="w">
 <p class="kick">ỨNG DỤNG</p>
 <h2>Đặt lên <span>mọi thứ</span></h2>
 <p class="lead">Chỗ ghi [Cần điền] chờ thông tin thật từ công ty.</p>
 <div class="apps">
  <div class="app a12 banner"><span class="cap">BĂNG RÔN FACEBOOK</span>{lg('mascot', 'm')}<div>{lg('wm_do')}<p class="hl">SẢN PHẨM TẬN TÂM - PHÁT TRIỂN XỨNG TẦM</p></div></div>
  <div class="app a6 promo"><span class="cap">BÀI ĐĂNG</span><div class="box">BÁNH TORTILLAS<br>GIAO TẬN VĂN PHÒNG</div><div class="pk">{pack_svg()}</div><div class="pt">{taco_row_pattern(DO, "#EE4A40", KEM, 'p2')}</div></div>
  <div class="app a6 bgpk"><span class="cap">HỘP BÁNH TORTILLAS</span><div style="width:min(100%,420px)">{pack_svg().replace('id="pks"', 'id="pks2"').replace('url(#pks)', 'url(#pks2)').replace('id="pkw"', 'id="pkw2"').replace('url(#pkw)', 'url(#pkw2)')}</div></div>
  <div class="app a4 bgbag"><span class="cap">TÚI GIẤY</span><div style="width:min(100%,340px)">{bag_svg()}</div></div>
  <div class="app a8 store"><span class="cap">MẶT TIỀN CỬA HÀNG</span>{store_svg()}</div>
  <div class="app a7 card-sc"><span class="cap">DANH THIẾP</span>
   <div class="nc f">{lg('wm_do')}</div>
   <div class="nc b">{lg('mark_do')}<div class="nm"><b>[Cần điền: họ tên]</b>[Cần điền: chức danh]</div><div class="ct"><span>0348.635.222</span><span>antamfoods.com</span><span>TP. Hồ Chí Minh</span></div></div></div>
  <div class="app a5 avs"><span class="cap">ẢNH ĐẠI DIỆN</span><div class="av">{lg('mark_do')}</div><div class="av" style="background:var(--do)">{lg('mascot')}</div></div>
 </div>
</div></section>

<footer class="back"><div class="w">
 {lg('wm_muc')}
 <p>Bản đề xuất theo tinh thần hình mẫu Nonla, chờ công ty duyệt. Logo gốc vẫn là logo chính thức cho tới khi duyệt. Chữ Fraunces, Anton, Be Vietnam Pro dùng theo giấy phép SIL Open Font License.</p>
 <div class="ct">0348.635.222<br>ANTAMFOODS.COM</div>
</div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

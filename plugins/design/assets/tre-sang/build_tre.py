"""Bộ nhận diện An Tâm hướng Trẻ & Sang. Chạy: python3 build_tre.py OUT.html"""
import base64
import os
import sys

import logo_tre as T

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
CH, CH2, KEM, HONG, BO, DEN = T.CHERRY, T.CHERRY2, T.KEM, T.HONG, T.BO, T.DEN
RG = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
}


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def ill(n):
    return b64(f"{MH}/{n}.svg", "image/svg+xml")


def fontfaces():
    return "\n".join(
        f"@font-face{{font-family:'Lexend';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, f'lexend/files/lexend-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2');unicode-range:{rg}}}"
        for w in (300, 400, 600, 800) for s, rg in RG.items())


def lg(svg, cls="lg"):
    return svg.replace("<svg ", f'<svg class="{cls}" ', 1)


def at(svg, x, y, w, h):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


WM_CH = T.wordmark()
WM_KEM = T.wordmark(KEM, BO, CH)
WM_DEN = T.wordmark(DEN, CH, KEM)
WM_GON_KEM = T.wordmark(KEM, BO, CH, False, False)
WM_GON_CH = T.wordmark(CH, BO, KEM, False, False)
MARK = T.mark()
MARK_HONG = T.mark(HONG, CH, BO)
MARK_BO = T.mark(BO, CH, CH)
MARK_SQ = T.mark(DEN, KEM, BO, "sq")

CSS = """
/* Bố cục: lưới ô bo tròn kiểu hiện đại; nền kem, mảng cherry đậm, chấm hồng phấn và bơ; chữ Lexend tròn khít. */
:root{--ch:#B5121B;--ch2:#7D0A10;--kem:#FFF4E8;--hong:#F7CFC6;--bo:#FFD37A;--den:#1B1B1B;--xam:#6B5A57;--line:#EED9C8;
--f:'Lexend',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--den);font:300 17px/1.65 var(--f);-webkit-font-smoothing:antialiased;overflow-x:hidden}
svg{max-width:100%}svg.lg{display:block;width:100%;height:auto}
.w{max-width:1240px;margin:0 auto;padding-inline:40px}
section{padding-block:104px}
.chip{display:inline-flex;align-items:center;gap:8px;font:600 12px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;padding:9px 14px;border-radius:999px;background:var(--den);color:var(--kem)}
.chip i{width:8px;height:8px;border-radius:50%;background:var(--bo)}
h2{font:800 clamp(40px,6vw,84px)/.95 var(--f);letter-spacing:-.05em;margin-top:18px;text-wrap:balance}
h2 span{color:var(--ch)}
.lead{max-width:56ch;margin-top:18px;color:var(--xam);font-size:18px}

/* hero */
.hero{position:relative;overflow:hidden;padding-block:28px 0}
.nav{display:flex;justify-content:space-between;align-items:center}
.nav .lg{width:120px}
.nav span{font:600 12px/1 var(--f);letter-spacing:.14em}
.stage{position:relative;display:grid;grid-template-columns:1.25fr .75fr;gap:20px;align-items:center;padding-block:64px 72px}
.stage .lg.big{max-width:720px}
.stage h1{font:300 clamp(28px,3.4vw,46px)/1.15 var(--f);letter-spacing:-.03em;margin-top:30px}
.stage h1 b{font-weight:800;color:var(--ch)}
.orbs{position:relative;aspect-ratio:1}
.orbs .o{position:absolute;border-radius:50%}
.o1{inset:0;background:var(--ch)}
.o2{width:56%;height:56%;right:-12%;top:-8%;background:var(--hong);mix-blend-mode:multiply}
.o3{width:40%;height:40%;left:-6%;bottom:-4%;background:var(--bo)}
.orbs img{position:absolute;inset:14%;width:72%;filter:drop-shadow(0 24px 24px rgba(60,0,0,.35))}
.marq{background:var(--ch);color:var(--kem);white-space:nowrap;overflow:hidden;font:800 34px/1 var(--f);letter-spacing:-.03em;padding-block:20px}
.marq span{padding-inline:28px}.marq i{font-style:normal;color:var(--bo)}
@media (prefers-reduced-motion:no-preference){.marq div{display:inline-block;animation:m 30s linear infinite}@keyframes m{to{transform:translateX(-50%)}}
 .o2{animation:f 6s ease-in-out infinite}.o3{animation:f 7s ease-in-out infinite reverse}@keyframes f{50%{transform:translateY(-10px)}}}

/* bento */
.bento{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:56px}
.b{border-radius:32px;position:relative;overflow:hidden;display:grid;place-items:center;padding:44px 36px;min-height:300px}
.b .cap{position:absolute;left:22px;bottom:18px;font:600 11px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;opacity:.7}
.c8{grid-column:span 8}.c4{grid-column:span 4}.c6{grid-column:span 6}.c3{grid-column:span 3}.c12{grid-column:span 12}.c5{grid-column:span 5}.c7{grid-column:span 7}
.b .lg{max-width:560px}.b .lg.m{max-width:170px}
.bg-kem{background:#fff;border:1px solid var(--line)}.bg-ch{background:var(--ch);color:var(--kem)}.bg-hong{background:var(--hong)}.bg-bo{background:var(--bo)}.bg-den{background:var(--den);color:var(--kem)}

/* màu */
.dots{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:56px}
.dot{display:flex;flex-direction:column;gap:12px}
.dot div{aspect-ratio:1;border-radius:50%}
.dot b{font:800 20px/1.1 var(--f);letter-spacing:-.02em}
.dot span{font:400 13px/1.4 var(--f);color:var(--xam)}

/* chữ */
.type{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:56px}
.type .b{place-items:start;align-content:space-between}
.gl{font:800 180px/.85 var(--f);letter-spacing:-.06em;color:var(--ch)}
.wts{display:flex;gap:18px;flex-wrap:wrap;font-size:22px}
.scale div{padding:16px 0;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:18px;align-items:baseline}
.scale small{font:400 12px/1.3 var(--f);color:var(--xam);white-space:nowrap}

/* đồ hoạ */
.grafx{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:56px}
.grafx > div{border-radius:32px;aspect-ratio:1;overflow:hidden;position:relative}
.grafx svg{width:100%;height:100%;display:block}
.grafx .cap{position:absolute;left:20px;bottom:16px;font:600 11px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;background:var(--kem);color:var(--den);padding:8px 12px;border-radius:999px}

/* ứng dụng */
.apps .b{padding:0;place-items:stretch}
.apps .b svg.mk{width:100%;height:100%;display:block}
.apps .b .cap{bottom:auto;top:18px;background:var(--kem);color:var(--den);padding:8px 12px;border-radius:999px;opacity:1;z-index:2}
footer{background:var(--ch);color:var(--kem);padding-block:72px 48px;overflow:hidden}
footer .w{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end}
footer .lg{max-width:520px}
footer p{font-size:13px;opacity:.75;margin-top:24px;max-width:60ch}
footer .ct{font:800 22px/1.5 var(--f);text-align:right;letter-spacing:-.02em}
@media (max-width:900px){.w{padding-inline:18px}section{padding-block:72px}.stage{grid-template-columns:1fr}.orbs{max-width:320px;justify-self:center;width:100%}
 .c8,.c4,.c6,.c3,.c12,.c5,.c7{grid-column:1/-1}.dots{grid-template-columns:repeat(3,1fr)}.type,.grafx{grid-template-columns:1fr}.gl{font-size:120px}
 footer .w{grid-template-columns:1fr}footer .ct{text-align:left}}
"""


def neon():
    return f"""<svg class="mk" viewBox="0 0 800 520" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Biển đèn neon ban đêm">
<defs><filter id="glow" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A0D10"/><stop offset="1" stop-color="#14070A"/></linearGradient></defs>
<rect width="800" height="520" fill="url(#wall)"/>
{"".join(f'<rect x="{x}" y="0" width="1" height="520" fill="#fff" opacity=".03"/>' for x in range(0, 800, 40))}
<ellipse cx="400" cy="250" rx="320" ry="150" fill="#FF3B4A" opacity=".12" filter="url(#glow)"/>
<g filter="url(#glow)">{at(T.wordmark("none", BO, "none", False, False).replace('fill="none" d', 'fill="none" stroke="#FFB3BA" stroke-width="3.2" d', 1), 150, 150, 500, 210)}</g>
<g filter="url(#glow)"><text x="400" y="400" text-anchor="middle" fill="#FFE7A8" style="font:600 22px Lexend;letter-spacing:.3em">BÁNH TORTILLAS · DONER KEBAB</text></g>
<rect x="0" y="470" width="800" height="50" fill="#0D0406"/>
</svg>"""


def cup():
    return f"""<svg class="mk" preserveAspectRatio="xMidYMid slice" viewBox="0 0 600 600" role="img" aria-label="Ly và hộp">
<rect width="600" height="600" fill="{HONG}"/>
<circle cx="440" cy="150" r="120" fill="{BO}"/>
<ellipse cx="230" cy="530" rx="110" ry="14" fill="#000" opacity=".12"/>
<path d="M140,150 H320 L296,520 H164 Z" fill="{CH}"/><rect x="128" y="126" width="204" height="34" rx="12" fill="{DEN}"/>
{at(WM_GON_KEM, 150, 270, 160, 70)}
<ellipse cx="440" cy="530" rx="110" ry="14" fill="#000" opacity=".12"/>
<rect x="340" y="330" width="200" height="190" rx="18" fill="{KEM}"/>
{at(MARK, 400, 375, 80, 80)}
<text x="440" y="490" text-anchor="middle" fill="{CH}" style="font:800 16px Lexend;letter-spacing:-.02em">ăn là an tâm.</text>
</svg>"""


def tote():
    return f"""<svg class="mk" preserveAspectRatio="xMidYMid slice" viewBox="0 0 600 700" role="img" aria-label="Túi vải">
<rect width="600" height="700" fill="{BO}"/>
<path d="M220,170 C220,60 380,60 380,170" fill="none" stroke="{KEM}" stroke-width="16" stroke-linecap="round"/>
<path d="M140,170 H460 L480,640 H120 Z" fill="{KEM}"/>
{at(MARK, 230, 250, 140, 140)}
{at(WM_GON_CH, 170, 440, 260, 90)}
<text x="300" y="580" text-anchor="middle" fill="{DEN}" style="font:600 13px Lexend;letter-spacing:.3em">ANTAMFOODS.COM</text>
</svg>"""


def phone():
    return f"""<svg class="mk" preserveAspectRatio="xMidYMid slice" viewBox="0 0 600 700" role="img" aria-label="Màn hình đặt món">
<rect width="600" height="700" fill="{DEN}"/>
<rect x="170" y="50" width="260" height="560" rx="40" fill="#0B0B0B"/><rect x="182" y="62" width="236" height="536" rx="30" fill="{KEM}"/>
{at(WM_GON_CH, 200, 92, 120, 44)}
<circle cx="392" cy="112" r="14" fill="{HONG}"/>
<text x="200" y="190" fill="{DEN}" style="font:800 26px Lexend;letter-spacing:-1px">Hôm nay ăn gì?</text>
<rect x="200" y="210" width="200" height="140" rx="22" fill="{CH}"/>
<image href="{ill('doner-cuon')}" x="250" y="216" width="130" height="130"/>
<text x="216" y="338" fill="{KEM}" style="font:800 15px Lexend">Doner cuộn</text>
<rect x="200" y="364" width="96" height="110" rx="20" fill="{BO}"/><image href="{ill('taco')}" x="206" y="366" width="84" height="84"/>
<text x="212" y="464" fill="{DEN}" style="font:800 12px Lexend">Taco</text>
<rect x="304" y="364" width="96" height="110" rx="20" fill="{HONG}"/><image href="{ill('banh-tortillas')}" x="310" y="366" width="84" height="84"/>
<text x="314" y="464" fill="{DEN}" style="font:800 12px Lexend">Tortillas</text>
<rect x="200" y="500" width="200" height="52" rx="26" fill="{DEN}"/>
<text x="300" y="532" text-anchor="middle" fill="{KEM}" style="font:600 14px Lexend">Đặt cho văn phòng</text>
</svg>"""


def box():
    return f"""<svg class="mk" preserveAspectRatio="xMidYMid slice" viewBox="0 0 800 520" role="img" aria-label="Hộp giao hàng">
<rect width="800" height="520" fill="{KEM}"/>
<circle cx="140" cy="110" r="70" fill="{HONG}"/><circle cx="690" cy="420" r="90" fill="{BO}"/>
<ellipse cx="400" cy="460" rx="250" ry="20" fill="#000" opacity=".12"/>
<path d="M180,190 L400,120 L620,190 L620,410 L400,480 L180,410 Z" fill="{CH}"/>
<path d="M180,190 L400,260 L620,190 L400,120 Z" fill="#D2202A"/>
<path d="M400,260 V480 L620,410 V190 Z" fill="{CH2}"/>
<g transform="translate(205 280) skewY(17.6)">{at(WM_GON_KEM, 0, 0, 170, 60)}</g>
<g transform="translate(450 290) skewY(-17.6)">{at(MARK_BO, 0, 0, 90, 90)}</g>
</svg>"""


def post():
    return f"""<svg class="mk" viewBox="0 0 800 520" role="img" aria-label="Bài đăng mạng xã hội">
<rect width="800" height="520" fill="{HONG}"/>
<rect x="40" y="40" width="340" height="440" rx="26" fill="{CH}"/>
<circle cx="210" cy="330" r="130" fill="{BO}"/><image href="{ill('taco')}" x="90" y="210" width="240" height="240"/>
<text x="70" y="110" fill="{KEM}" style="font:800 40px Lexend;letter-spacing:-2px">gập đôi,</text>
<text x="70" y="154" fill="{BO}" style="font:800 40px Lexend;letter-spacing:-2px">ngon gấp đôi.</text>
<rect x="420" y="40" width="340" height="440" rx="26" fill="{KEM}"/>
{at(WM_CH, 450, 90, 280, 120)}
<text x="450" y="290" fill="{DEN}" style="font:800 34px Lexend;letter-spacing:-1.5px">bữa nhẹ</text>
<text x="450" y="330" fill="{DEN}" style="font:800 34px Lexend;letter-spacing:-1.5px">cho văn phòng.</text>
<text x="450" y="440" fill="{CH}" style="font:600 15px Lexend;letter-spacing:2px">0348.635.222</text>
</svg>"""


def page():
    gr1 = f'<svg viewBox="0 0 400 400" aria-hidden="true"><rect width="400" height="400" fill="{CH}"/>' + "".join(
        f'<circle cx="{c * 100 + (50 if r % 2 else 0)}" cy="{r * 90 + 40}" r="38" fill="{[KEM, HONG, BO][(r + c) % 3]}"/>' for r in range(5) for c in range(5)) + "</svg>"
    import re
    gr2 = re.sub(r'viewBox="[^"]*"', 'viewBox="170 -98 115 115" preserveAspectRatio="xMidYMid slice" style="background:#FFF4E8"', WM_GON_CH, count=1)
    gr3 = f'<svg viewBox="0 0 400 400" aria-hidden="true"><rect width="400" height="400" fill="{DEN}"/>' + "".join(
        f'<g transform="translate({c * 100 + 50} {r * 100 + 50}) rotate({(r * 4 + c) * 23})">{T.hat(0, 12, 44, [BO, HONG, CH][(r + c) % 3], DEN, 0)}</g>' for r in range(4) for c in range(4)) + "</svg>"
    strip = "".join(f"<span>{t}</span><i>●</i>" for t in ["ăn là an tâm", "bánh tortillas", "doner kebab", "giao tận văn phòng", "nhượng quyền"] * 2)
    return f"""<title>An Tâm Trẻ và Sang</title>
<style>{fontfaces()}
{CSS}</style>

<header class="hero"><div class="w">
 <div class="nav">{lg(WM_GON_CH)}<span>BỘ NHẬN DIỆN · TRẺ &amp; SANG</span></div>
 <div class="stage"><div>{lg(WM_CH, "lg big")}<h1>Ăn là <b>an tâm.</b> Bánh tortillas và doner kebab cho thế hệ văn phòng mới.</h1></div>
  <div class="orbs"><div class="o o1"></div><div class="o o2"></div><div class="o o3"></div><img src="{ill('doner-cuon')}" alt="Doner cuộn"></div></div>
</div><div class="marq"><div>{strip}</div></div></header>

<section><div class="w">
 <span class="chip"><i></i>Logo</span>
 <h2>Gọn, tròn, <span>có chiếc bánh</span></h2>
 <p class="lead">Chữ "an tâm" viết thường, nét đậm tròn, chữ đứng khít nhau như tên các thương hiệu trẻ. Chữ a một tầng tròn như chiếc bánh. Dấu mũ là chiếc bánh gập đôi màu bơ, điểm vui duy nhất trên nền tiết chế.</p>
 <div class="bento">
  <div class="b c8 bg-kem">{lg(WM_CH)}<span class="cap">Logo chính</span></div>
  <div class="b c4 bg-hong">{lg(MARK, "lg m")}<span class="cap">Biểu tượng</span></div>
  <div class="b c4 bg-den">{lg(MARK_SQ, "lg m")}<span class="cap">Ô ứng dụng</span></div>
  <div class="b c8 bg-ch">{lg(WM_KEM)}<span class="cap">Trên nền cherry</span></div>
  <div class="b c6 bg-bo">{lg(WM_GON_CH)}<span class="cap">Bản gọn</span></div>
  <div class="b c6 bg-kem">{lg(WM_DEN)}<span class="cap">Bản đen, một màu</span></div>
 </div>
</div></section>

<section style="background:#fff"><div class="w">
 <span class="chip"><i></i>Màu</span>
 <h2>Cherry đậm, <span>chấm màu vui</span></h2>
 <p class="lead">Cherry sâu và kem cho cảm giác sang. Hồng phấn và vàng bơ là hai chấm màu trẻ, dùng ít, như topping.</p>
 <div class="dots">
  <div class="dot"><div style="background:{CH}"></div><b>Cherry</b><span>#B5121B · màu chính</span></div>
  <div class="dot"><div style="background:{KEM};border:1px solid var(--line)"></div><b>Kem</b><span>#FFF4E8 · nền</span></div>
  <div class="dot"><div style="background:{DEN}"></div><b>Đen</b><span>#1B1B1B · chữ</span></div>
  <div class="dot"><div style="background:{HONG}"></div><b>Hồng phấn</b><span>#F7CFC6 · điểm nhấn</span></div>
  <div class="dot"><div style="background:{BO}"></div><b>Vàng bơ</b><span>#FFD37A · chiếc bánh</span></div>
 </div>
</div></section>

<section><div class="w">
 <span class="chip"><i></i>Chữ</span>
 <h2>Một họ chữ, <span>Lexend</span></h2>
 <div class="type">
  <div class="b bg-kem"><div class="gl">ẩm</div><div class="wts"><span style="font-weight:300">Mảnh</span><span style="font-weight:400">Thường</span><span style="font-weight:600">Vừa</span><span style="font-weight:800">Đậm</span></div><p style="color:var(--xam);font-size:14px">Lexend: tròn, rộng, dễ đọc, đủ dấu tiếng Việt, miễn phí trên Google Fonts.</p></div>
  <div class="b bg-kem scale" style="display:block">
   <div><span style="font:800 46px/1 Lexend;letter-spacing:-.05em;color:var(--ch)">gập đôi là ngon.</span><small>Tiêu đề · 800 · khít −5%</small></div>
   <div><span style="font:600 24px/1.2 Lexend;letter-spacing:-.02em">Bánh tortillas giao tận nơi</span><small>Tiêu đề phụ · 600</small></div>
   <div><span style="font:600 12px/1 Lexend;letter-spacing:.16em">NHƯỢNG QUYỀN CỬA HÀNG</span><small>Nhãn · 600 · giãn 16%</small></div>
   <div><span style="font:300 16px/1.6 Lexend">Bữa nhẹ cho nhân viên văn phòng, đặt qua 0348.635.222.</span><small>Nội dung · 300</small></div>
  </div>
 </div>
</div></section>

<section style="background:#fff"><div class="w">
 <span class="chip"><i></i>Đồ hoạ</span>
 <h2>Chấm tròn, <span>chữ cắt cúp</span></h2>
 <p class="lead">Ba thủ pháp dùng chung: chấm tròn như những chiếc bánh, chữ "an tâm" phóng to cắt mép, và những chiếc bánh nhỏ rải như sticker.</p>
 <div class="grafx"><div>{gr1}<span class="cap">Chấm tròn</span></div><div>{gr2}<span class="cap">Chữ cắt cúp</span></div><div>{gr3}<span class="cap">Bánh sticker</span></div></div>
</div></section>

<section><div class="w apps">
 <span class="chip"><i></i>Ứng dụng</span>
 <h2>Từ ly nước <span>tới biển neon</span></h2>
 <div class="bento">
  <div class="b c8" style="min-height:0"><span class="cap">Biển neon cửa hàng</span>{neon()}</div>
  <div class="b c4" style="min-height:0"><span class="cap">Ly và hộp</span>{cup()}</div>
  <div class="b c4" style="min-height:0"><span class="cap">Túi vải</span>{tote()}</div>
  <div class="b c4" style="min-height:0"><span class="cap">Ứng dụng đặt món</span>{phone()}</div>
  <div class="b c4" style="min-height:0;background:{KEM}"><span class="cap">Hộp giao hàng</span>{box()}</div>
  <div class="b c12" style="min-height:0"><span class="cap">Bài đăng mạng xã hội</span>{post()}</div>
 </div>
</div></section>

<footer><div class="w"><div>{lg(WM_KEM)}<p>Bản đề xuất hướng Trẻ &amp; Sang, chờ công ty duyệt. Câu "ăn là an tâm" và các câu quảng cáo là đề xuất. Chữ Lexend dùng theo giấy phép SIL Open Font License.</p></div>
<div class="ct">0348.635.222<br>antamfoods.com</div></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

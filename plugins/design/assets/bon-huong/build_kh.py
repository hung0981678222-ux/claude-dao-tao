"""Bốn hướng logo khác nhau cho Ẩm Thực An Tâm, trên một trang để chọn.
Chạy: python3 build_kh.py OUT.html
"""
import base64
import os
import sys

import pathops
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(SCR, "nl"))
import logo_nl as NL  # noqa: E402  (linh vật Bé Tâm, chiếc taco)

DO, DO2, VANG, KEM, MUC, NAU = "#D7150E", "#A90F09", "#FFC53D", "#FFF6E6", "#3A1410", "#8A4A26"
RG = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
}
FILES = {
    "Anton": lambda s: os.path.join(SCR, f"anton/package/files/anton-{s}-400-normal.woff2"),
    "Pacifico": lambda s: os.path.join(HERE, f"pacifico/files/pacifico-{s}-400-normal.woff2"),
    "Baloo": lambda s: os.path.join(SCR, f"moi/baloo-2/files/baloo-2-{s}-800-normal.woff2"),
    "BVP": lambda s: os.path.join(SCR, f"cc/be-vietnam-pro/files/be-vietnam-pro-{s}-400-normal.woff2"),
}


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def fontfaces():
    return "\n".join(f"@font-face{{font-family:'{n}';font-display:swap;src:url({b64(f(s), 'font/woff2')}) format('woff2');unicode-range:{rg}}}"
                     for n, f in FILES.items() for s, rg in RG.items())


def outline(text, fam, size):
    fs = [TTFont(FILES[fam](s)) for s in ("latin", "vietnamese")]
    upm = fs[0]["head"].unitsPerEm; sc = size / upm
    out = pathops.Path(); x = 0.0; xs = []
    for ch in text:
        f = next((f for f in fs if f.getBestCmap().get(ord(ch))), fs[0])
        gname = f.getBestCmap().get(ord(ch), ".notdef"); adv = f["hmtx"][gname][0] * sc
        xs.append((x, adv))
        if ch != " ":
            gs = f.getGlyphSet(); rec = DecomposingRecordingPen(gs); gs[gname].draw(rec)
            gp = pathops.Path(); rec.replay(TransformPen(gp.getPen(), (sc, 0, 0, -sc, x, 0)))
            out = pathops.op(out, gp, pathops.PathOp.UNION)
        x += adv
    return out, xs, x


def d(p):
    pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    p.draw(pen); return pen.getCommands()


def svg(vb, body, label="Ẩm Thực An Tâm", cls="lg"):
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">{body}</svg>'


# ---------- 1. Bảng hiệu Sài Gòn ----------
def sign(bg=VANG, ink=DO, shadow=MUC, band=DO, band_ink=KEM, phone=True):
    b = (f'<rect x="4" y="4" width="592" height="352" rx="8" fill="{bg}" stroke="{ink}" stroke-width="8"/>'
         f'<rect x="20" y="20" width="560" height="320" fill="none" stroke="{ink}" stroke-width="2.5"/>')
    for cx, cy in [(20, 20), (580, 20), (20, 340), (580, 340)]:
        b += f'<circle cx="{cx}" cy="{cy}" r="12" fill="{bg}" stroke="{ink}" stroke-width="2.5"/>'
    b += f'<text x="300" y="68" text-anchor="middle" fill="{ink}" style="font:32px Anton;letter-spacing:.3em">ẨM THỰC</text>'
    b += NL.taco(170, 66, 38, ink, bg, tilt=-16) + NL.taco(430, 66, 38, ink, bg, tilt=16)
    b += f'<text x="306" y="228" text-anchor="middle" fill="{shadow}" style="font:132px Anton;letter-spacing:.05em">AN TÂM</text>'
    b += f'<text x="300" y="222" text-anchor="middle" fill="{ink}" style="font:132px Anton;letter-spacing:.05em" stroke="{bg}" stroke-width="3" paint-order="stroke">AN TÂM</text>'
    b += f'<path d="M40,244 H560 L544,266 L560,288 H40 L56,266 Z" fill="{band}"/>'
    b += f'<text x="300" y="278" text-anchor="middle" fill="{band_ink}" style="font:30px Anton;letter-spacing:.08em">BÁNH TORTILLAS · DONER KEBAB</text>'
    if phone:
        b += f'<text x="300" y="322" text-anchor="middle" fill="{ink}" style="font:22px Anton;letter-spacing:.12em">ĐT: 0348.635.222 · ANTAMFOODS.COM</text>'
    return svg("0 0 600 360", b)


def sign_mark():
    b = (f'<rect x="4" y="4" width="192" height="192" rx="10" fill="{VANG}" stroke="{DO}" stroke-width="8"/>'
         f'<rect x="18" y="18" width="164" height="164" fill="none" stroke="{DO}" stroke-width="2.5"/>'
         f'<text x="104" y="150" text-anchor="middle" fill="{MUC}" style="font:120px Anton">AT</text>'
         f'<text x="100" y="146" text-anchor="middle" fill="{DO}" style="font:120px Anton">AT</text>'
         f'<text x="100" y="172" text-anchor="middle" fill="{DO}" style="font:15px Anton;letter-spacing:.2em">ẨM THỰC</text>')
    return svg("0 0 200 200", b, "Biểu tượng An Tâm")


# ---------- 2. Chữ viết tay xe bánh ----------
def script(bg=DO, fg=KEM, accent=VANG):
    b = f'<rect width="600" height="360" rx="28" fill="{bg}"/>' if bg else ""
    b += f'<text x="300" y="86" text-anchor="middle" fill="{accent}" style="font:30px Anton;letter-spacing:.34em">ẨM THỰC</text>'
    b += f'<text x="306" y="222" text-anchor="middle" fill="{accent}" style="font:132px Pacifico">An Tâm</text>'
    b += f'<text x="300" y="216" text-anchor="middle" fill="{fg}" style="font:132px Pacifico">An Tâm</text>'
    b += f'<path d="M120,256 C220,236 380,236 492,250 C430,252 360,256 330,272" fill="none" stroke="{accent}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<text x="300" y="318" text-anchor="middle" fill="{fg}" style="font:28px Anton;letter-spacing:.1em">BÁNH TORTILLAS &amp; DONER KEBAB</text>'
    return svg("0 0 600 360", b)


def script_mark():
    b = (f'<circle cx="100" cy="100" r="96" fill="{DO}"/><circle cx="100" cy="100" r="84" fill="none" stroke="{VANG}" stroke-width="3"/>'
         f'<text x="104" y="136" text-anchor="middle" fill="{VANG}" style="font:96px Pacifico">Â</text>'
         f'<text x="100" y="132" text-anchor="middle" fill="{KEM}" style="font:96px Pacifico">Â</text>')
    return svg("0 0 200 200", b, "Biểu tượng An Tâm")


# ---------- 3. Tem linh vật ----------
def badge(uid, ring=DO, face=VANG, txt=KEM):
    b = (f'<defs><path id="{uid}t" d="M60,200 A140,140 0 0 1 340,200"/><path id="{uid}b" d="M52,200 A148,148 0 0 0 348,200"/></defs>'
         f'<circle cx="200" cy="200" r="196" fill="{ring}"/>'
         f'<circle cx="200" cy="200" r="186" fill="none" stroke="{txt}" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"/>'
         f'<circle cx="200" cy="200" r="118" fill="{face}"/>'
         f'<text fill="{txt}" style="font:40px Anton;letter-spacing:.12em"><textPath href="#{uid}t" startOffset="50%" text-anchor="middle">ẨM THỰC AN TÂM</textPath></text>'
         f'<text fill="{txt}" style="font:25px Anton;letter-spacing:.12em"><textPath href="#{uid}b" startOffset="50%" text-anchor="middle">BÁNH TORTILLAS · DONER KEBAB</textPath></text>'
         f'<text x="40" y="212" fill="{face}" style="font:30px Anton" text-anchor="middle">★</text><text x="360" y="212" fill="{face}" style="font:30px Anton" text-anchor="middle">★</text>')
    m = NL.mascot(uid + "m", "chao").replace('<svg ', '<svg x="100" y="96" width="200" height="188" ', 1)
    return svg("0 0 400 400", b + m)


# ---------- 4. Chữ là món ăn ----------
AM, AM_XS, AM_W = outline("an", "Baloo", 150)
AM2, AM2_XS, AM2_W = outline("am", "Baloo", 150)
A_TOP = outline("a", "Baloo", 150)[0].bounds[1]
X_H = -A_TOP


def spit_t(x, fg, meat=NAU):
    """Chữ t là trụ doner: xiên dọc, khối thịt thuôn, thanh ngang đỏ."""
    w = 62
    s = f'<rect x="{x + w / 2 - 4}" y="-156" width="8" height="156" rx="4" fill="{MUC}"/>'
    s += f'<path d="M{x + 6},-128 Q{x + w / 2},-142 {x + w - 6},-128 L{x + w - 14},-12 Q{x + w / 2},-2 {x + 14},-12 Z" fill="{meat}"/>'
    for i, y in enumerate(range(-104, -10, 16)):
        s += f'<path d="M{x + 8 + i * .6},{y} Q{x + w / 2},{y + 7} {x + w - 8 - i * .6},{y}" stroke="#6B3519" stroke-width="3" fill="none" opacity=".7"/>'
    s += f'<path d="M{x + 12},-100 q4,40 0,80" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".22" fill="none"/>'
    s += f'<rect x="{x - 14}" y="{A_TOP - 2:.1f}" width="{w + 28}" height="20" rx="10" fill="{fg}"/>'
    return s, w


def food_word(fg=DO, bg=KEM, sub=MUC, taco_fill=VANG, top=True, subl=True):
    b = f'<path fill="{fg}" d="{d(AM)}"/>'
    x = AM_W + 48
    t, tw = spit_t(x, fg)
    b += t
    x += tw + 18
    b += f'<path transform="translate({x:.1f} 0)" fill="{fg}" d="{d(AM2)}"/>'
    ax = x + AM2_XS[0][0] + AM2_XS[0][1] / 2
    b += NL.taco(ax + 4, A_TOP - 8, 66, taco_fill, bg, tilt=-14)
    W = x + AM2_W
    if top:
        b += f'<text x="4" y="{A_TOP - 44:.0f}" fill="{fg}" style="font:34px Anton;letter-spacing:.2em">ẨM THỰC</text>'
    if subl:
        b += f'<text x="{W / 2:.0f}" y="62" text-anchor="middle" fill="{sub}" style="font:30px Anton;letter-spacing:.1em" textLength="{W - 8:.0f}" lengthAdjust="spacing">BÁNH TORTILLAS &amp; DONER KEBAB</text>'
    y0 = A_TOP - 90 if top else -160
    return svg(f"-14 {y0:.0f} {W + 28:.0f} {(80 if subl else 30) - y0:.0f}", b)


def food_mark():
    t, tw = spit_t(69, DO)
    b = f'<rect width="200" height="200" rx="46" fill="{KEM}"/><g transform="translate(0 176)">{t}</g>'
    b += NL.taco(142, 70, 56, VANG, KEM, tilt=-14)
    return svg("0 0 200 200", b, "Biểu tượng An Tâm")


# ---------- mô phỏng chung ----------
def bag(logo_svg, body, handle, w=180):
    inner = logo_svg.replace('class="lg"', f'x="{(220 - w) / 2:.0f}" y="120" width="{w}" height="{w * .62:.0f}"', 1)
    return (f'<svg class="mk" viewBox="0 0 300 330" aria-hidden="true"><ellipse cx="150" cy="316" rx="110" ry="9" fill="#000" opacity=".18"/>'
            f'<path d="M100,80 C100,20 170,20 170,80" fill="none" stroke="{handle}" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M240,70 L272,60 L272,302 L240,310 Z" fill="#000" opacity=".12"/><path d="M240,70 L272,60 L272,302 L240,310 Z" fill="{body}" opacity=".85"/>'
            f'<rect x="20" y="70" width="220" height="240" fill="{body}"/>{inner}</svg>')


def storefront(logo_svg, fascia, wall, glow="#FFE3A3"):
    inner = logo_svg.replace('class="lg"', 'x="150" y="8" width="300" height="130"', 1)
    return (f'<svg class="mk" viewBox="0 0 600 330" aria-hidden="true"><rect width="600" height="330" fill="#2A1512"/>'
            f'<rect x="30" y="20" width="540" height="310" fill="{wall}"/><rect x="30" y="0" width="540" height="146" fill="{fascia}"/>{inner}'
            f'<rect x="60" y="176" width="210" height="154" fill="{glow}" stroke="#2A1512" stroke-width="8"/>'
            f'<rect x="300" y="176" width="100" height="154" fill="#2A1512"/><rect x="310" y="186" width="80" height="144" fill="{glow}" opacity=".8"/>'
            f'<rect x="430" y="176" width="110" height="154" fill="{glow}" stroke="#2A1512" stroke-width="8"/></svg>')


CSS = """
:root{--do:#D7150E;--do2:#A90F09;--vang:#FFC53D;--kem:#FFF6E6;--muc:#3A1410;--xam:#6D5049;--line:#EDD9BD;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--muc);font:400 16px/1.6 'BVP',system-ui,sans-serif}
.w{max-width:1200px;margin:0 auto;padding-inline:40px}
header{padding-block:64px 24px}
.k{font:18px/1 Anton,sans-serif;letter-spacing:.08em;color:var(--do)}
h1{font:clamp(44px,6vw,76px)/1 Anton,sans-serif;text-transform:uppercase;margin-top:12px}
header p{max-width:62ch;margin-top:14px;color:var(--xam)}
section{padding-block:40px 64px}
.top{display:flex;align-items:baseline;gap:18px;border-top:4px solid var(--muc);padding-top:18px;flex-wrap:wrap}
.num{font:72px/.8 Anton,sans-serif;color:var(--do)}
.top h2{font:40px/1 Anton,sans-serif;text-transform:uppercase}
.top p{flex-basis:100%;max-width:70ch;color:var(--xam)}
.grid{display:grid;grid-template-columns:1.5fr 1fr;gap:16px;margin-top:24px}
.main{border-radius:28px;display:grid;place-items:center;padding:48px 36px;min-height:420px}
.main svg.lg{width:100%;max-width:560px;max-height:440px;height:auto;display:block}
.side{display:grid;grid-template-rows:1fr 1fr;gap:16px}
.side > div{border-radius:28px;overflow:hidden;display:grid;place-items:center;padding:20px}
svg.mk{width:100%;height:auto;display:block}
.minis{display:flex;gap:18px;align-items:center;justify-content:center;flex-wrap:wrap}
.minis svg.lg{width:150px;height:auto;display:block}
.minis .av{width:150px;height:150px;border-radius:50%;overflow:hidden;display:grid;place-items:center}
.minis .av svg.lg{width:100%}
.pros{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.pros span{font:13px/1 Anton,sans-serif;letter-spacing:.08em;padding:9px 12px;border-radius:999px;background:var(--muc);color:var(--kem)}
footer{padding-block:40px 64px;color:var(--xam)}
footer b{color:var(--muc)}
@media (max-width:900px){.w{padding-inline:18px}.grid{grid-template-columns:1fr}.main{min-height:0;padding:32px 18px}.side{grid-template-rows:auto}}
"""


def section(n, name, desc, pros, main_bg, logo, side1, side1_bg, side2, side2_bg):
    return f"""<section><div class="w">
 <div class="top"><span class="num">{n}</span><h2>{name}</h2><p>{desc}</p></div>
 <div class="grid"><div class="main" style="background:{main_bg}">{logo}</div>
  <div class="side"><div style="background:{side1_bg}">{side1}</div><div style="background:{side2_bg}">{side2}</div></div></div>
 <div class="pros">{"".join(f"<span>{p}</span>" for p in pros)}</div>
</div></section>"""


def page():
    s1 = sign(); s1b = sign(VANG, DO, MUC, DO, KEM, False)
    s2 = script(); s2n = script(None, DO, VANG)
    fw = food_word(); fw_do = food_word(KEM, DO, VANG, VANG)
    secs = [
        section(1, "Bảng hiệu Sài Gòn", "Lấy cảm hứng từ bảng hiệu vẽ tay của các tiệm ăn Sài Gòn xưa: nền vàng, chữ đỏ in hoa có bóng, khung viền đôi, số điện thoại ngay trên bảng. Rất Việt, rất quán ăn.",
                ["NÉT VIỆT RÕ NHẤT", "HỢP BIỂN CỬA HÀNG", "DỄ NHỚ"], "#F4E3C3", s1,
                storefront(s1b, VANG, KEM), "#2A1512",
                f'<div class="minis">{sign_mark()}<div class="av" style="background:{VANG}">{sign_mark()}</div></div>', "#FFE9B8"),
        section(2, "Chữ viết tay xe bánh", "Chữ viết tay tròn, bay bổng như bảng tên xe bánh, xe taco. Dòng gạch dưới vàng như nét cọ. Trẻ, vui, hợp mạng xã hội.",
                ["TRẺ, VUI", "HỢP FACEBOOK, TIKTOK", "THÂN THIỆN"], "#fff", s2,
                bag(s2n, KEM, DO2), "#F6D9A8",
                f'<div class="minis">{script_mark()}</div>', DO),
        section(3, "Tem linh vật", "Tem tròn kiểu tiệm đồ ăn nhanh: chữ chạy vòng quanh, giữa là linh vật Bé Tâm. Trẻ em, dân văn phòng đều nhớ mặt.",
                ["CÓ LINH VẬT", "HỢP TEM, LY, HỘP", "NỔI BẬT TỪ XA"], VANG, badge("b1"),
                bag(badge("b2").replace('viewBox="0 0 400 400"', 'viewBox="-40 0 480 400"'), DO, DO2), "#FBE3B2",
                f'<div class="minis"><div class="av" style="background:{DO}">{badge("b3")}</div></div>', "#fff"),
        section(4, "Chữ là món ăn", "Chữ an tâm viết thường, nét tròn đậm. Chữ t là trụ thịt doner xoay, dấu mũ chữ â là chiếc taco. Hai sản phẩm chính nằm ngay trong tên, giống cách Nonla đặt hạt cà phê vào chữ o.",
                ["SẢN PHẨM TRONG CHỮ", "HIỆN ĐẠI", "GỌN TRÊN BAO BÌ"], "#fff", fw,
                storefront(fw_do, DO, KEM), "#2A1512",
                f'<div class="minis">{food_mark()}<div class="av" style="background:{KEM}">{food_mark()}</div></div>', DO),
    ]
    return f"""<title>Bốn hướng logo An Tâm</title>
<style>{fontfaces()}
{CSS}</style>
<header><div class="w"><p class="k">ẨM THỰC AN TÂM · CHỌN HƯỚNG</p><h1>Bốn hướng khác nhau</h1>
<p>Mỗi hướng có logo, một mô phỏng biển hiệu hoặc túi, và biểu tượng nhỏ cho ảnh đại diện. Anh chị chọn một hướng (hoặc ghép), tôi sẽ làm kỹ toàn bộ bộ nhận diện theo hướng đó.</p></div></header>
{"".join(secs)}
<footer><div class="w"><p><b>Anh chị chọn 1, 2, 3 hay 4?</b> Có thể ghép, ví dụ khung bảng hiệu của hướng 1 với linh vật của hướng 3. Minh hoạ sản phẩm và chữ bậc thang vẫn giữ để dùng trong hướng được chọn.</p></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

"""Trang hướng trẻ trung hiện đại. Chạy: python3 build_tre.py OUT.html"""
import sys

from build_cam_nang import fontfaces, ill
import tre as T

DO, VANG, RAU, HONG, KEM, MUC = T.DO, T.VANG, T.RAU, T.HONG, T.KEM, T.MUC


def sized(svg, w, h, x=0, y=0):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


CSS = """
:root{--do:#E8341C;--vang:#FFC72C;--rau:#22B573;--hong:#FF8FA3;--kem:#FFF8EC;--muc:#1E1A17;--xam:#6B625B;
--f:'BVP','Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--muc);font:400 16px/1.6 var(--f);-webkit-font-smoothing:antialiased}
svg{max-width:100%}
.w{max-width:1240px;margin:0 auto;padding-inline:40px}
header{padding-block:56px 40px}
.eb{display:inline-block;font:600 12px/1 var(--f);letter-spacing:.2em;text-transform:uppercase;background:var(--muc);color:var(--kem);padding:9px 14px;border-radius:999px}
h1{font:600 clamp(40px,6vw,80px)/1 var(--f);letter-spacing:-.04em;margin-top:18px}
h1 span{color:var(--do)}
header p{max-width:60ch;color:var(--xam);margin-top:14px;font-size:17px}
.pal{display:flex;gap:10px;margin-top:22px;flex-wrap:wrap}
.pal i{display:flex;align-items:end;width:120px;height:72px;border-radius:18px;padding:10px 12px;font:600 11px/1.2 var(--f);font-style:normal}
section{padding-block:56px}
.oh{display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.oh .n{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--do);color:var(--kem);font:600 26px/1 var(--f)}
.oh h2{font:600 34px/1.1 var(--f);letter-spacing:-.03em}
.oh p{flex-basis:100%;max-width:64ch;color:var(--xam)}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:24px}
.g > div{border-radius:28px;overflow:hidden;position:relative}
.g .cap{position:absolute;left:14px;top:12px;font:600 11px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;background:#fff;color:var(--muc);padding:8px 11px;border-radius:999px;z-index:2}
.s5{grid-column:span 5}.s4{grid-column:span 4}.s3{grid-column:span 3}.s7{grid-column:span 7}.s6{grid-column:span 6}.s12{grid-column:span 12}
.pane{display:grid;place-items:center;padding:48px 28px;min-height:340px}
.pane > svg{width:100%;max-width:560px;height:auto;display:block}
svg.mk{width:100%;height:auto;display:block}
footer{padding-block:40px 64px;color:var(--xam)}footer b{color:var(--muc)}
@media (max-width:900px){.w{padding-inline:18px}.s5,.s4,.s3,.s7,.s6,.s12{grid-column:1/-1}}
"""


def phone_post(logo_svg, bg, title, title2, food, accent):
    return f"""<svg class="mk" viewBox="0 0 520 640" role="img" aria-label="Bài đăng trên điện thoại">
<rect width="520" height="640" fill="{accent}"/>
<rect x="110" y="40" width="300" height="600" rx="40" fill="#111"/><rect x="122" y="52" width="276" height="588" rx="30" fill="#fff"/>
<rect x="122" y="110" width="276" height="345" fill="{bg}"/>
{sized(T.mark(), 26, 26, 136, 72)}<text x="170" y="90" style="font:600 13px BVP" fill="#111">Ẩm Thực An Tâm</text>
<image href="{ill(food)}" x="170" y="230" width="190" height="190"/>
<text x="140" y="160" style="font:600 30px BVP;letter-spacing:-1px" fill="{KEM}">{title}</text>
<text x="140" y="196" style="font:600 30px BVP;letter-spacing:-1px" fill="{VANG}">{title2}</text>
{sized(logo_svg, 120, 50, 268, 400)}
<text x="136" y="486" style="font:600 13px BVP" fill="#111">Thích · Bình luận · Chia sẻ</text>
<text x="136" y="510" style="font:400 12px BVP" fill="#444">Gọi 0348.635.222 để đặt bánh</text>
</svg>"""


def cup(logo_svg, body, lid):
    return f"""<svg class="mk" viewBox="0 0 520 640" role="img" aria-label="Ly nước">
<rect width="520" height="640" fill="{RAU}"/>
<ellipse cx="260" cy="580" rx="120" ry="14" fill="#000" opacity=".2"/>
<path d="M150,170 H370 L345,575 H175 Z" fill="{body}"/><rect x="138" y="140" width="244" height="36" rx="12" fill="{lid}"/>
<rect x="250" y="40" width="16" height="110" rx="8" fill="{VANG}" transform="rotate(10 258 95)"/>
{sized(logo_svg, 190, 96, 165, 300)}
</svg>"""


def tote(logo_svg, body):
    return f"""<svg class="mk" viewBox="0 0 520 640" role="img" aria-label="Túi vải giao hàng">
<rect width="520" height="640" fill="{HONG}"/>
<path d="M190,170 C190,70 330,70 330,170" fill="none" stroke="{MUC}" stroke-width="12" stroke-linecap="round"/>
<path d="M110,160 H410 L392,590 H128 Z" fill="{body}"/>
{sized(logo_svg, 260, 220, 130, 270)}
</svg>"""


def stickers():
    return f"""<svg class="mk" viewBox="0 0 520 640" role="img" aria-label="Tờ sticker">
<rect width="520" height="640" fill="{VANG}"/>
<rect x="60" y="50" width="400" height="540" rx="24" fill="#fff"/>
{sized(T.sticker(), 340, 130, 90, 80)}
<g transform="rotate(8 180 330)">{sized(T.mark(), 130, 130, 110, 260)}</g>
<g transform="rotate(-10 360 330)">{sized(T.mark(VANG, DO, MUC), 120, 120, 300, 270)}</g>
<g transform="rotate(-4 260 480)">{sized(T.o_mau(), 320, 120, 100, 420)}</g>
</svg>"""


def sign(logo_svg, bg):
    return f"""<svg class="mk" viewBox="0 0 1240 460" role="img" aria-label="Biển cửa hàng">
<rect width="1240" height="460" fill="#2B2522"/>
<rect x="80" y="30" width="1080" height="430" fill="{KEM}"/>
<rect x="80" y="30" width="1080" height="160" fill="{bg}"/>
{sized(logo_svg, 520, 150, 360, 36)}
{"".join(f'<rect x="{80 + i * 67.5}" y="190" width="34" height="40" fill="{[DO, VANG, RAU, HONG][i % 4]}"/>' for i in range(16))}
<rect x="140" y="260" width="400" height="200" rx="16" fill="#FFE2A6"/><image href="{ill('doner-cuon')}" x="250" y="270" width="180" height="180"/>
<rect x="580" y="260" width="120" height="200" fill="{MUC}"/>
<rect x="740" y="260" width="360" height="200" rx="16" fill="#FFE2A6"/><image href="{ill('taco')}" x="830" y="280" width="180" height="180"/>
</svg>"""


def section(n, name, desc, items):
    return f'<section><div class="w"><div class="oh"><span class="n">{n}</span><h2>{name}</h2><p>{desc}</p></div><div class="g">{items}</div></div></section>'


def page():
    s1 = section(1, "Sticker", "Chữ AN TÂM nét dày đều nằm trên viên bo tròn đỏ, nghiêng nhẹ, viền trắng như sticker dán. Nhãn ẨM THỰC vàng dán chéo, thêm vài ngôi sao lấp lánh.",
                 f'<div class="s7 pane" style="background:#fff"><span class="cap">Logo</span>{T.sticker()}</div>'
                 f'<div class="s5"><span class="cap">Bài đăng</span>{phone_post(T.sticker(), DO, "Bữa xế", "vui vẻ!", "doner-cuon", VANG)}</div>'
                 f'<div class="s4"><span class="cap">Ly nước</span>{cup(T.sticker(), KEM, DO)}</div>'
                 f'<div class="s4"><span class="cap">Tờ sticker</span>{stickers()}</div>'
                 f'<div class="s4"><span class="cap">Túi vải</span>{tote(T.sticker(), KEM)}</div>')
    s2 = section(2, "Ô màu", "Mỗi chữ một ô bo góc, mỗi ô một màu của món ăn: đỏ cà chua, vàng bánh, xanh rau, hồng. Các ô nghiêng nhẹ như đang nhảy múa.",
                 f'<div class="s7 pane" style="background:#fff"><span class="cap">Logo</span>{T.o_mau()}</div>'
                 f'<div class="s5"><span class="cap">Bài đăng</span>{phone_post(T.o_mau(), RAU, "Ăn xanh,", "sống vui", "taco", HONG)}</div>'
                 f'<div class="s12"><span class="cap">Biển cửa hàng</span>{sign(T.o_mau(), KEM)}</div>')
    s3 = section(3, "Nhún nhảy", "Chữ đỏ nhún lên xuống như đang nhảy, đặt trên nền vàng nắng. ẨM THỰC nằm trong bong bóng lời nói, dưới chân là nét sóng như mép bánh.",
                 f'<div class="s7 pane" style="background:var(--vang)"><span class="cap">Logo</span>{T.nhun()}</div>'
                 f'<div class="s5"><span class="cap">Túi vải</span>{tote(T.nhun(KEM, VANG, KEM), DO)}</div>'
                 f'<div class="s6"><span class="cap">Ly nước</span>{cup(T.nhun(), VANG, DO)}</div>'
                 f'<div class="s6"><span class="cap">Bài đăng</span>{phone_post(T.nhun(KEM, VANG, KEM), MUC, "Giao nhanh,", "ăn liền!", "doner-tru-quay", DO)}</div>')
    pal = "".join(f'<i style="background:{c};color:{t}">{n}<br>{c}</i>' for c, n, t in [(DO, "Đỏ cà chua", KEM), (VANG, "Vàng bánh", MUC), (RAU, "Xanh rau", KEM), (HONG, "Hồng", MUC), (MUC, "Mực", KEM)])
    return f"""<title>An Tâm trẻ trung</title>
<style>{fontfaces()}
{CSS}</style>
<header><div class="w"><span class="eb">Ẩm Thực An Tâm · Hướng trẻ trung</span>
<h1>Trẻ, tươi, <span>vui mắt</span></h1>
<p>Vẫn là bộ chữ AN TÂM đã vẽ: chữ A mái vòm, thanh ngang gợn như mép bánh, mũ là chiếc bánh có đốm nướng. Nét dày đều hơn, bỏ chân chữ, màu tươi của món ăn, bố cục vui.</p>
<div class="pal">{pal}</div></div></header>
{s1}{s2}{s3}
<footer><div class="w"><p><b>Anh chị chọn 1, 2 hay 3.</b> Ba bố cục dùng chung bộ chữ và bảng màu, nên có thể kết hợp: ví dụ bố cục 1 làm logo chính, bố cục 2 cho biển hiệu, bố cục 3 cho mạng xã hội.</p></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

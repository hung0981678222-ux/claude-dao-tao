"""Trang 3 logo kết hợp ấn tượng. Chạy: python3 build_ket_hop.py OUT.html"""
import sys

from build_cam_nang import fontfaces, ill
import ket_hop as K

RED, IVORY, INK, GOLD, DEEP = K.RED, K.IVORY, K.INK, K.GOLD, K.DEEP


def sized(svg, w, h, x=0, y=0):
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h}" ', 1)


CSS = """
:root{--red:#A8160F;--deep:#7E0F0A;--ivory:#F6F1E8;--paper:#FBF8F2;--ink:#1F1714;--gold:#C39443;--muted:#6E5F56;--line:#DCD0BD;
--f:'BVP','Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--ivory);color:var(--ink);font:400 16px/1.6 var(--f);-webkit-font-smoothing:antialiased}
svg{max-width:100%}
.w{max-width:1240px;margin:0 auto;padding-inline:40px}
header{background:#1C1210;color:var(--ivory);padding-block:56px 64px;overflow:hidden}
.eb{font:600 11px/1 var(--f);letter-spacing:.3em;text-transform:uppercase;color:var(--gold)}
h1{font:300 clamp(36px,5vw,64px)/1.05 var(--f);letter-spacing:-.03em;margin-top:14px;max-width:18ch}
h1 b{font-weight:600;color:var(--gold)}
.trio{display:grid;grid-template-columns:1fr 1.1fr 1.5fr;gap:28px;align-items:center;margin-top:48px}
.trio svg{width:100%;height:auto;display:block}
.trio .ng{background:var(--ivory);padding:28px 24px}
.trio p{font:600 12px/1 var(--f);letter-spacing:.2em;color:rgba(246,241,232,.7);margin-top:14px;text-align:center}
section{padding-block:80px;border-bottom:1px solid var(--line)}
.oh{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:end;margin-bottom:28px}
.num{font:300 96px/.8 var(--f);color:var(--red)}
.oh h2{font:600 32px/1.1 var(--f);letter-spacing:-.02em}
.oh p{color:var(--muted);max-width:64ch;margin-top:8px}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:16px}
.g > div{position:relative;overflow:hidden}
.g .cap{position:absolute;left:16px;top:14px;font:600 10px/1 var(--f);letter-spacing:.24em;text-transform:uppercase;background:var(--ivory);color:var(--ink);padding:7px 10px;z-index:2}
.s4{grid-column:span 4}.s5{grid-column:span 5}.s7{grid-column:span 7}.s8{grid-column:span 8}.s12{grid-column:span 12}.s6{grid-column:span 6}
.pane{display:grid;place-items:center;padding:40px 28px;min-height:380px}
.pane > svg{width:min(100%,420px);height:auto;display:block}
svg.mk{width:100%;height:auto;display:block}
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:20px}
.why div{border-top:2px solid var(--ink);padding-top:10px;font-size:14px;color:var(--muted)}
.why b{display:block;color:var(--ink);font-size:16px;margin-bottom:2px}
footer{padding-block:48px;color:var(--muted)}footer b{color:var(--ink)}
@media (max-width:900px){.w{padding-inline:18px}.trio,.why{grid-template-columns:1fr}.s4,.s5,.s7,.s8,.s12,.s6{grid-column:1/-1}.num{font-size:64px}}
"""


def menu_board():
    return f"""<svg class="mk" viewBox="0 0 600 640" role="img" aria-label="Bảng đứng trước cửa hàng">
<rect width="600" height="640" fill="#E9DFCF"/><rect y="560" width="600" height="80" fill="#CDBEA6"/>
<ellipse cx="300" cy="590" rx="170" ry="14" fill="#000" opacity=".18"/>
<path d="M190,590 L210,520 M410,590 L390,520" stroke="#3A2A20" stroke-width="10"/>
{sized(K.cua_vom(None, RED, GOLD, RED, "mb"), 330, 440, 135, 90)}
</svg>"""


def gift():
    return f"""<svg class="mk" viewBox="0 0 600 640" role="img" aria-label="Túi giấy">
<rect width="600" height="640" fill="#2A1A16"/>
<ellipse cx="300" cy="590" rx="190" ry="16" fill="#000" opacity=".5"/>
<path d="M240,150 C240,70 360,70 360,150" fill="none" stroke="{GOLD}" stroke-width="5"/>
<path d="M150,140 H450 V590 H150 Z" fill="{DEEP}"/><path d="M450,140 L490,128 V578 L450,590 Z" fill="#5E0B07"/>
{sized(K.cua_vom(None, RED, GOLD, RED, "gb"), 230, 307, 185, 200)}
</svg>"""


def cup_seal():
    return f"""<svg class="mk" viewBox="0 0 600 640" role="img" aria-label="Ly và tem">
<rect width="600" height="640" fill="#E3D6C2"/>
<ellipse cx="200" cy="560" rx="100" ry="12" fill="#000" opacity=".2"/>
<path d="M110,190 H290 L268,560 H132 Z" fill="{IVORY}"/><rect x="100" y="170" width="200" height="28" rx="8" fill="{RED}"/>
{sized(K.huy_hieu(RED, DEEP, GOLD, IVORY, "c1"), 150, 150, 125, 280)}
<g transform="rotate(-8 450 360)"><circle cx="450" cy="372" r="118" fill="#000" opacity=".15"/>
{sized(K.huy_hieu(RED, DEEP, GOLD, IVORY, "c2"), 236, 236, 332, 242)}</g>
</svg>"""


def avatar():
    return f"""<svg class="mk" viewBox="0 0 600 640" role="img" aria-label="Ảnh đại diện">
<rect width="600" height="640" fill="#F1EAE0"/>
<rect x="110" y="120" width="380" height="400" rx="28" fill="#fff"/>
<circle cx="300" cy="270" r="110" fill="#1C1210"/>
{sized(K.huy_hieu(RED, DEEP, GOLD, IVORY, "av"), 200, 200, 200, 170)}
<text x="300" y="430" text-anchor="middle" fill="{INK}" style="font:600 22px BVP">Ẩm Thực An Tâm</text>
<text x="300" y="460" text-anchor="middle" fill="#6E5F56" style="font:400 15px BVP">Bánh tortillas, doner kebab</text>
</svg>"""


def fascia():
    return f"""<svg class="mk" viewBox="0 0 1240 520" role="img" aria-label="Mặt tiền cửa hàng">
<defs><linearGradient id="glw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE3B0"/><stop offset="1" stop-color="#E29E52"/></linearGradient></defs>
<rect width="1240" height="520" fill="#2A1A16"/>
<rect x="100" y="40" width="1040" height="480" fill="{IVORY}"/>
<rect x="100" y="40" width="1040" height="170" fill="{IVORY}" stroke="{INK}" stroke-width="2"/>
{sized(K.ngang(), 620, 164, 310, 44)}
<rect x="100" y="210" width="1040" height="10" fill="{RED}"/>
<rect x="150" y="260" width="400" height="260" fill="url(#glw)"/><image href="{ill('doner-tru-quay')}" x="250" y="290" width="210" height="210"/>
<rect x="590" y="260" width="130" height="260" fill="{INK}"/>
<rect x="760" y="260" width="330" height="260" fill="url(#glw)"/><image href="{ill('taco')}" x="820" y="300" width="210" height="210"/>
</svg>"""


def card():
    return f"""<svg class="mk" viewBox="0 0 600 640" role="img" aria-label="Danh thiếp">
<rect width="600" height="640" fill="#CDBEA6"/>
<g transform="rotate(-6 300 230)"><rect x="80" y="110" width="440" height="264" rx="6" fill="{IVORY}"/>
{sized(K.ngang(), 380, 100, 110, 190)}</g>
<g transform="rotate(4 300 470)"><rect x="80" y="340" width="440" height="264" rx="6" fill="{RED}"/>
<text x="110" y="440" fill="{IVORY}" style="font:600 26px BVP">[Cần điền: Họ tên]</text>
<text x="110" y="468" fill="{GOLD}" style="font:400 15px BVP">[Cần điền: Chức danh]</text>
<text x="110" y="560" fill="{IVORY}" style="font:400 14px BVP;letter-spacing:1px">0348.635.222 · antamfoods.com</text></g>
</svg>"""


def section(n, name, desc, why, items):
    return f"""<section><div class="w"><div class="oh"><span class="num">{n}</span><div><h2>{name}</h2><p>{desc}</p></div></div>
<div class="g">{items}</div><div class="why">{"".join(f"<div><b>{a}</b>{b}</div>" for a, b in why)}</div></div></section>"""


def page():
    s1 = section(1, "Cửa vòm", "Khung vòm đỏ như cửa tiệm bánh, viền chỉ vàng đôi. Nhãn ẨM THỰC vàng trên đỉnh, chữ AN / TÂM nét đậm có đường khắc vàng, dải băng đỏ thẫm mang dòng sản phẩm vắt ngang.",
                 [("Ấn tượng nhất khi đứng", "Hợp biển đứng, menu, túi, hộp quà."), ("Sang kiểu nhà hàng lâu năm", "Đường khắc vàng như biển đồng."), ("Rõ là đồ ăn", "Dấu mũ là chiếc bánh có đốm nướng, thanh ngang gợn như mép bánh.")],
                 f'<div class="s5 pane" style="background:var(--ivory);border:1px solid var(--line)"><span class="cap">Logo</span>{K.cua_vom(None, RED, GOLD, RED, "a1")}</div>'
                 f'<div class="s4"><span class="cap">Bảng đứng trước cửa</span>{menu_board()}</div>'
                 f'<div class="s3" style="grid-column:span 3"><span class="cap">Túi giấy</span>{gift()}</div>')
    s2 = section(2, "Huy hiệu", "Huy hiệu tròn hai vòng, vạch chia như mặt đồng hồ. Trên đỉnh là chiếc taco trong ô vòm, giữa là ẨM THỰC và AN / TÂM viền khắc, dải băng sản phẩm vắt ngang.",
                 [("Như tem chất lượng", "Tạo cảm giác đáng tin, có bảo chứng."), ("Hợp đồ tròn", "Tem niêm phong, ly, hộp tròn, ảnh đại diện."), ("Có hình món ăn", "Chiếc taco trên đỉnh nói ngay ngành hàng.")],
                 f'<div class="s5 pane" style="background:#1C1210"><span class="cap">Logo</span>{K.huy_hieu(RED, DEEP, GOLD, IVORY, "b1")}</div>'
                 f'<div class="s4"><span class="cap">Ly và tem niêm phong</span>{cup_seal()}</div>'
                 f'<div class="s3" style="grid-column:span 3"><span class="cap">Ảnh đại diện</span>{avatar()}</div>')
    s3 = section(3, "Ngang mạnh", "Biểu tượng taco trong ô vòm bên trái. Bên phải là chữ AN TÂM nét đậm, chữ M bị cắn một miếng, nhãn ẨM THỰC đỏ trên đầu chữ AN T, nét gạch vàng uốn như mép bánh và dòng sản phẩm.",
                 [("Đọc nhanh từ xa", "Hợp biển ngang, xe giao hàng, băng rôn."), ("Có điểm vui", "Miếng cắn ở chữ M làm logo dễ nhớ."), ("Giữ ý ẨM THỰC trên AN T", "Đúng vị trí anh chị muốn.")],
                 f'<div class="s12"><span class="cap">Mặt tiền cửa hàng</span>{fascia()}</div>'
                 f'<div class="s7 pane" style="background:var(--ivory);border:1px solid var(--line)"><span class="cap">Logo</span>{K.ngang()}</div>'
                 f'<div class="s5"><span class="cap">Danh thiếp</span>{card()}</div>')
    return f"""<title>Logo kết hợp An Tâm</title>
<style>{fontfaces()}
{CSS}</style>
<header><div class="w"><p class="eb">Ẩm Thực An Tâm · Logo kết hợp</p><h1>Ba bản ghép <b>ấn tượng hơn</b></h1>
<div class="trio"><div>{K.cua_vom(None, RED, GOLD, RED, "h1")}<p>1 · CỬA VÒM</p></div><div>{K.huy_hieu(RED, DEEP, GOLD, IVORY, "h2")}<p>2 · HUY HIỆU</p></div>
<div><div class="ng">{K.ngang()}</div><p>3 · NGANG MẠNH</p></div></div></div></header>
{s1}{s2}{s3}
<footer><div class="w"><p><b>Anh chị chọn 1, 2 hay 3.</b> Ba bản dùng chung một bộ chữ nên có thể dùng cùng lúc: ví dụ bản 3 cho biển hiệu, bản 2 cho tem và ảnh đại diện, bản 1 cho túi và hộp quà.</p></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

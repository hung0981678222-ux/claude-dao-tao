"""Cẩm nang nhận diện Ẩm Thực An Tâm, hướng Vòm cao cấp.
Chạy: python3 build_cam_nang.py OUT.html
Cần: logo_cao_cap.py, thư mục be-vietnam-pro/ (npm @fontsource/be-vietnam-pro), ảnh minh hoạ trong plugins/design/assets/minh-hoa.
"""
import base64, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MH = os.environ.get("MINH_HOA", "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa")
LOGO = os.environ.get("LOGO_GOC", "/home/user/claude-dao-tao/plugins/design/assets/logo-am-thuc-an-tam.jpg")
g = json.loads(subprocess.check_output([sys.executable, os.path.join(HERE, "logo_cao_cap.py")]))

RED, RED2, IVORY, PAPER, INK, GOLD, FLOUR, MUTED, LINE = (
    "#A8160F", "#D7150E", "#F6F1E8", "#FBF8F2", "#1F1714", "#C39443", "#E9DFCC", "#7A6A60", "#DCD0BD")


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def ill(name):
    return b64(f"{MH}/{name}.svg", "image/svg+xml")


def fontfaces():
    ranges = {
        "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
        "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
    }
    out = []
    for w in (300, 400, 500, 600):
        for sub, rg in ranges.items():
            uri = b64(os.path.join(HERE, f"be-vietnam-pro/files/be-vietnam-pro-{sub}-{w}-normal.woff2"), "font/woff2")
            out.append(f"@font-face{{font-family:'BVP';font-style:normal;font-weight:{w};font-display:swap;src:url({uri}) format('woff2');unicode-range:{rg}}}")
    return "\n".join(out)


# ---------- ký hiệu SVG dùng chung ----------
def sprite():
    return f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="wm" viewBox="0 -27 494 128"><path fill="currentColor" d="{g['wm']}"/><path fill="var(--hat,{GOLD})" d="{g['wm_hat']}"/></symbol>
<symbol id="amt" viewBox="0 -38 237 46"><path fill="currentColor" d="{g['amt']}"/></symbol>
<symbol id="a" viewBox="-2 -27 76 128"><path fill="currentColor" d="{g['mk']}"/><path fill="var(--hat,{GOLD})" d="{g['mk_hat']}"/></symbol>
<symbol id="badge" viewBox="0 0 170 230"><path d="M0,230 V85 a85,85 0 0 1 170,0 V230 Z" fill="var(--bb,{RED})"/>
 <path d="M9,221 V85 a76,76 0 0 1 152,0 V221 Z" fill="none" stroke="var(--hat,{GOLD})" stroke-width="1.4"/>
 <use href="#a" x="47" y="72" width="76" height="128" style="color:var(--ba,{IVORY})"/></symbol>
<symbol id="stack" viewBox="0 -30 494 208"><use href="#wm" x="0" y="-27" width="494" height="128"/>
 <path d="M0,161 H132 M362,161 H494" stroke="currentColor" stroke-width="1.3" opacity=".55"/>
 <use href="#amt" x="152" y="140" width="189.6" height="36.8"/></symbol>
<symbol id="horiz" viewBox="0 0 795 230"><use href="#badge" x="0" y="0" width="170" height="230"/>
 <path d="M212,46 V184" stroke="currentColor" stroke-width="1.3" opacity=".4"/>
 <use href="#stack" x="252" y="0" width="543" height="229"/></symbol>
<filter id="noise"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>
</defs></svg>"""


def use(sym, cls="", style="", label="Ẩm Thực An Tâm"):
    vb = {"wm": "0 -27 494 128", "amt": "0 -38 237 46", "a": "-2 -27 76 128", "badge": "0 0 170 230",
          "stack": "0 -30 494 208", "horiz": "0 0 795 230"}[sym]
    x, y, w, h = vb.split()
    return (f'<svg class="{sym} {cls}" viewBox="{vb}" style="{style}" role="img" aria-label="{label}">'
            f'<use href="#{sym}" x="{x}" y="{y}" width="{w}" height="{h}"/></svg>')


def cmyk(h):
    r, gg, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    k = 1 - max(r, gg, b)
    if k >= 1:
        return "0 0 0 100"
    c, m, y = ((1 - v - k) / (1 - k) for v in (r, gg, b))
    return " ".join(str(round(v * 100)) for v in (c, m, y, k))


def rgb(h):
    return " ".join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))


# ---------- sơ đồ dựng hình ----------
def construction():
    xs = [(0, 72, "A"), (96, 166, "N"), (220, 286, "T"), (310, 382, "Â"), (406, 494, "M")]
    L = []
    for y, t in [(-1.6, "vượt đỉnh 1,6"), (0, "đỉnh chữ 0"), (64, "thanh ngang 64"), (100, "chân chữ 100"), (-10.6, ""), (-25.6, "dấu mũ")]:
        L.append(f'<line x1="-30" x2="524" y1="{y}" y2="{y}" stroke="{RED}" stroke-width=".35" stroke-dasharray="{"2 2" if t != "chân chữ 100" else "0"}" opacity=".8"/>')
        if t:
            L.append(f'<text x="530" y="{y + 1.6}" class="cx">{t}</text>')
    for x0, x1, _ in xs:
        L.append(f'<rect x="{x0}" y="-1.6" width="{x1 - x0}" height="101.6" fill="none" stroke="{MUTED}" stroke-width=".3"/>')
    for i in range(len(xs) - 1):
        a, b = xs[i][1], xs[i + 1][0]
        L.append(f'<rect x="{a}" y="104" width="{b - a}" height="6" fill="{GOLD}" opacity=".55"/>')
        L.append(f'<text x="{(a + b) / 2}" y="119" class="cx" text-anchor="middle">{"24" if b - a == 24 else "54"}</text>')
    for x0 in (0, 310):
        L.append(f'<circle cx="{x0 + 36}" cy="34.4" r="36" fill="none" stroke="{RED}" stroke-width=".45"/>')
        L.append(f'<circle cx="{x0 + 36}" cy="34.4" r="25" fill="none" stroke="{RED}" stroke-width=".45" stroke-dasharray="1.5 1.5"/>')
        L.append(f'<circle cx="{x0 + 36}" cy="34.4" r="1.2" fill="{RED}"/>')
    L.append(f'<circle cx="346" cy="-10.6" r="15" fill="none" stroke="{RED}" stroke-width=".45" stroke-dasharray="1.5 1.5"/>')
    L.append(f'<path d="M96,40 h11" stroke="{RED}" stroke-width=".5"/><text x="101.5" y="36" class="cx" text-anchor="middle">x = 11</text>')
    return (f'<svg class="cons" viewBox="-34 -44 640 172" role="img" aria-label="Lưới dựng chữ AN TÂM">'
            f'<path fill="{INK}" d="{g["wm"]}"/><path fill="{GOLD}" d="{g["wm_hat"]}"/>{"".join(L)}</svg>')


# ---------- hoạ tiết ----------
def patterns():
    def wrap(bg, body, name, note):
        return (f'<figure class="pat"><svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
                f'<rect width="400" height="400" fill="{bg}"/>{body}</svg><figcaption><b>{name}</b>{note}</figcaption></figure>')
    a = "".join(f'<path d="M{x},{y + 64} V{y + 22} a22,22 0 0 1 44,0 V{y + 64}" fill="none" stroke="{GOLD}" stroke-width="1.3"/>'
                for r in range(6) for c in range(7) for x, y in [(c * 64 - (32 if r % 2 else 0) + 10, r * 72 - 20)])
    b = "".join(f'<path d="M{x - 9},{y} a9,9 0 0 1 18,0 z" fill="{"#D9CCB4" if (r + c) % 5 else GOLD}"/>'
                for r in range(12) for c in range(12) for x, y in [(c * 36 + (18 if r % 2 else 0), r * 36 + 22)])
    cc = "".join(f'<use href="#a" x="{c * 100 + 30}" y="{r * 130 + 10}" width="40" height="67" style="color:#4A3730;--hat:#5E4A40"/>'
                 for r in range(4) for c in range(4))
    cc += f'<use href="#a" x="230" y="140" width="40" height="67" style="color:{IVORY}"/>'
    d = "".join(f'<path d="M{200 - w},{420} V{200 - w + 150} a{w},{w} 0 0 1 {2 * w},0 V420" fill="none" stroke="{IVORY}" stroke-width="1.2" opacity="{.25 + i * .12:.2f}"/>'
                for i, w in enumerate([190, 160, 130, 100, 70, 40]))
    return "".join([
        wrap(RED, a, "Hàng vòm", "Nét vàng mảnh trên đỏ. Dùng cho túi, hộp, nền biển hiệu."),
        wrap(IVORY, b, "Bán nguyệt", "Nửa chiếc bánh, cùng tông kem. Giấy gói, lót khay."),
        wrap(INK, cc, "Chữ Â chìm", "Chữ Â cùng tông trên nền mực, một chữ sáng. Bìa hồ sơ."),
        wrap(RED, d, "Cổng lồng", "Vòm lồng nhau, mờ dần. Nền bài đăng, màn hình chờ."),
    ])


# ---------- ứng dụng ----------
def card_scene():
    return f"""<div class="scene sc-card">
 <div class="nc front">{use("badge", "", f"--bb:{IVORY};--ba:{RED}")}{use("stack", "", f"color:{IVORY}")}</div>
 <div class="nc back"><div class="nc-top">{use("a", "", f"color:{RED};height:34px;width:auto")}<span>ẨM THỰC AN TÂM</span></div>
  <div class="nc-name"><b>[Cần điền: Họ tên]</b><span>[Cần điền: Chức danh]</span></div>
  <div class="nc-ct"><span>0348.635.222</span><span>antamfoods.com</span><span>TP. Hồ Chí Minh</span></div></div>
</div>"""


def bag_svg():
    return f"""<svg class="mock" viewBox="0 0 600 640" role="img" aria-label="Túi giấy kraft">
<defs><linearGradient id="kf" x1="0" x2="1"><stop offset="0" stop-color="#C7A27A"/><stop offset=".55" stop-color="#D2AF87"/><stop offset="1" stop-color="#BE976D"/></linearGradient>
<linearGradient id="ks" x1="0" x2="1"><stop offset="0" stop-color="#9E7A55"/><stop offset="1" stop-color="#B08A62"/></linearGradient></defs>
<ellipse cx="300" cy="600" rx="220" ry="20" fill="#000" opacity=".22" filter="url(#soft)"/>
<path d="M210,170 C210,70 330,70 330,170" fill="none" stroke="#8E6A45" stroke-width="7" stroke-linecap="round"/>
<path d="M150,600 L150,170 L400,170 L400,600 Z" fill="url(#kf)"/>
<path d="M400,170 L470,150 L470,590 L400,600 Z" fill="url(#ks)"/>
<path d="M435,160 L435,595" stroke="#8E6A45" stroke-width="1" opacity=".5"/>
<path d="M150,170 L400,170 L400,200 L150,200 Z" fill="#000" opacity=".06"/>
<path d="M230,176 C230,90 320,90 320,176" fill="none" stroke="#A07A52" stroke-width="7" stroke-linecap="round"/>
<g style="color:{RED}"><use href="#badge" x="232" y="250" width="86" height="116.4"/></g>
<use href="#stack" x="190" y="390" width="170" height="71.6" style="color:{INK};--hat:{RED}"/>
<text x="275" y="560" text-anchor="middle" class="mk-t" fill="{INK}" opacity=".7">ANTAMFOODS.COM</text>
<rect x="150" y="170" width="320" height="430" filter="url(#noise)" fill="#fff"/>
</svg>"""


def pack_svg():
    return f"""<svg class="mock" viewBox="0 0 600 640" role="img" aria-label="Gói bánh tortillas">
<defs><linearGradient id="pk" x1="0" x2="1"><stop offset="0" stop-color="#F3EDE2"/><stop offset=".5" stop-color="#FFFDF8"/><stop offset="1" stop-color="#E8E0D2"/></linearGradient>
<linearGradient id="pr" x1="0" x2="1"><stop offset="0" stop-color="#8F120C"/><stop offset=".5" stop-color="{RED}"/><stop offset="1" stop-color="#8A110B"/></linearGradient>
<clipPath id="win"><path d="M225,470 V330 a75,75 0 0 1 150,0 V470 Z"/></clipPath></defs>
<ellipse cx="300" cy="610" rx="200" ry="18" fill="#000" opacity=".22" filter="url(#soft)"/>
<path d="M140,80 Q300,62 460,80 L472,600 Q300,618 128,600 Z" fill="url(#pk)"/>
<path d="M140,80 Q300,62 460,80 L462,120 Q300,104 138,120 Z" fill="#DCD2C2"/>
<path d="M150,84 Q300,68 450,84" stroke="#C9BDAA" stroke-width="1" fill="none" stroke-dasharray="3 4"/>
<path d="M134,230 Q300,214 466,230 L470,600 Q300,618 130,600 Z" fill="url(#pr)"/>
<path d="M221,474 V330 a79,79 0 0 1 158,0 V474 Z" fill="none" stroke="{GOLD}" stroke-width="1.5"/>
<path d="M225,470 V330 a75,75 0 0 1 150,0 V470 Z" fill="#F4E6C8"/>
<image href="{ill('banh-tortillas')}" x="215" y="330" width="170" height="170" clip-path="url(#win)"/>
<use href="#stack" x="205" y="130" width="190" height="80" style="color:{INK};--hat:{RED}"/>
<text x="300" y="530" text-anchor="middle" class="mk-t" fill="{IVORY}" style="letter-spacing:.32em;font-size:15px">BÁNH TORTILLAS</text>
<text x="300" y="560" text-anchor="middle" class="mk-t" fill="{IVORY}" opacity=".7" style="font-size:10px">[Cần điền: khối lượng, hạn dùng]</text>
<rect x="128" y="62" width="344" height="556" filter="url(#noise)" fill="#fff"/>
</svg>"""


def store_svg():
    win = lambda x, w, glow=True: (f'<path d="M{x},560 V{330 + w / 2} a{w / 2},{w / 2} 0 0 1 {w},0 V560 Z" fill="url(#glow)"/>'
                                   f'<path d="M{x},560 V{330 + w / 2} a{w / 2},{w / 2} 0 0 1 {w},0 V560" fill="none" stroke="{GOLD}" stroke-width="3"/>')
    return f"""<svg class="mock" viewBox="0 0 1200 700" role="img" aria-label="Mặt tiền cửa hàng">
<defs><linearGradient id="glow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE3B0"/><stop offset="1" stop-color="#E9A95A"/></linearGradient>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8F120C"/><stop offset="1" stop-color="{RED}"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A211E"/><stop offset="1" stop-color="#3B2F2A"/></linearGradient></defs>
<rect width="1200" height="700" fill="url(#sky)"/>
<rect x="150" y="120" width="900" height="460" fill="url(#wall)"/>
<rect x="150" y="120" width="900" height="110" fill="{INK}"/>
<use href="#horiz" x="405" y="140" width="390" height="112.9" style="color:{IVORY};--bb:{RED};--ba:{IVORY}"/>
{win(210, 200)}{win(790, 200)}
<path d="M510,580 V380 a90,90 0 0 1 180,0 V580 Z" fill="#2B201C"/>
<path d="M510,580 V380 a90,90 0 0 1 180,0 V580" fill="none" stroke="{GOLD}" stroke-width="3"/>
<path d="M600,300 V580" stroke="{GOLD}" stroke-width="1.5" opacity=".6"/>
<use href="#a" x="578" y="340" width="44" height="74" style="color:{IVORY}"/>
<image href="{ill('doner-tru-quay')}" x="220" y="380" width="180" height="180"/>
<image href="{ill('doner-cuon')}" x="800" y="390" width="180" height="170"/>
<rect x="100" y="580" width="1000" height="16" fill="#140E0C"/>
<rect x="0" y="596" width="1200" height="104" fill="#241B18"/>
<ellipse cx="600" cy="600" rx="420" ry="16" fill="#FFD9A0" opacity=".18" filter="url(#soft)"/>
<text x="600" y="660" text-anchor="middle" class="mk-t" fill="{IVORY}" opacity=".55" style="font-size:13px;letter-spacing:.3em">MÔ PHỎNG MẶT TIỀN CỬA HÀNG NHƯỢNG QUYỀN</text>
</svg>"""


def seal_svg():
    return f"""<svg class="mock seal" viewBox="0 0 300 300" role="img" aria-label="Tem niêm phong">
<defs><path id="ring" d="M150,150 m-104,0 a104,104 0 1 1 208,0 a104,104 0 1 1 -208,0"/></defs>
<circle cx="150" cy="156" r="132" fill="#000" opacity=".25" filter="url(#soft)"/>
<circle cx="150" cy="150" r="136" fill="{RED}"/>
<circle cx="150" cy="150" r="126" fill="none" stroke="{GOLD}" stroke-width="1.2"/>
<circle cx="150" cy="150" r="84" fill="none" stroke="{GOLD}" stroke-width="1.2"/>
<text class="mk-t" fill="{IVORY}" style="font-size:15px;letter-spacing:.34em"><textPath href="#ring">ẨM THỰC AN TÂM · ANTAMFOODS.COM · 0348.635.222 ·</textPath></text>
<use href="#a" x="118" y="92" width="64" height="108" style="color:{IVORY}"/>
</svg>"""


def letter_html():
    return f"""<div class="a4">
 <div class="a4-h">{use("horiz", "", f"color:{INK};--bb:{RED}")}<span>BÁO GIÁ<br><em>Số: [Cần điền]</em></span></div>
 <div class="a4-to"><span>Kính gửi</span><b>[Cần điền: tên doanh nghiệp]</b></div>
 <div class="a4-l"><i style="width:92%"></i><i style="width:84%"></i><i style="width:88%"></i><i style="width:60%"></i></div>
 <table><tr><th>Sản phẩm</th><th>Quy cách</th><th>Đơn giá</th></tr>
  <tr><td>Bánh tortillas</td><td>[Cần điền]</td><td>[Cần điền]</td></tr>
  <tr><td>Doner kebab</td><td>[Cần điền]</td><td>[Cần điền]</td></tr></table>
 <div class="a4-f"><span>Công ty TNHH SX-TM Ẩm Thực An Tâm</span><span>0348.635.222 · antamfoods.com</span></div>
</div>"""


def phone_html():
    return f"""<div class="phone"><div class="ph-scr">
 <div class="ph-bar"><span class="ph-av">{use("badge", "", "--bb:" + RED)}</span><span><b>Ẩm Thực An Tâm</b><small>Được tài trợ</small></span></div>
 <div class="ph-post"><svg viewBox="0 0 1080 1350" aria-hidden="true"><rect width="1080" height="1350" fill="{RED}"/>
  {"".join(f'<path d="M{540 - w},1350 V{900 - w} a{w},{w} 0 0 1 {2 * w},0 V1350" fill="none" stroke="{IVORY}" stroke-width="3" opacity="{.18 + i * .1:.2f}"/>' for i, w in enumerate([520, 440, 360]))}
  <path d="M290,1350 V770 a250,250 0 0 1 500,0 V1350 Z" fill="{IVORY}"/>
  <image href="{ill('doner-cuon')}" x="330" y="720" width="420" height="420"/>
  <use href="#stack" x="300" y="110" width="480" height="202" style="color:{IVORY}"/>
  <text x="540" y="430" text-anchor="middle" fill="{IVORY}" style="font:300 70px 'BVP',sans-serif;letter-spacing:-.02em">Bữa nhẹ văn phòng,</text>
  <text x="540" y="510" text-anchor="middle" fill="{IVORY}" style="font:600 70px 'BVP',sans-serif;letter-spacing:-.02em">giao tận nơi.</text>
 </svg></div>
 <div class="ph-cap">Bánh tortillas, doner kebab cho bữa nhẹ văn phòng. Gọi 0348.635.222.</div>
</div></div>"""


PRODUCTS = [("banh-tortillas", "Bánh tortillas", "Bánh nền, bán sỉ cho doanh nghiệp", FLOUR),
            ("taco", "Taco", "Gập đôi, nhân đầy", "#EADCC0"),
            ("doner-tru-quay", "Doner kebab", "Thịt nướng trụ quay", "#E4D3B8"),
            ("doner-cuon", "Doner cuộn", "Cuộn chặt, ăn gọn", "#DDCCB0")]

MISUSE = [
    ("Kéo méo tỉ lệ", 'style="transform:scaleX(1.45)"'),
    ("Xoay nghiêng", 'style="transform:rotate(-14deg)"'),
    ("Đổi màu ngoài bảng màu", f'style="color:#2D6CDF;--hat:#35B26B"'),
    ("Thêm bóng đổ, hiệu ứng", 'style="filter:drop-shadow(6px 6px 0 #C39443) drop-shadow(10px 10px 6px rgba(0,0,0,.5))"'),
    ("Chỉ vẽ viền", f'style="color:transparent;stroke:{RED};stroke-width:1.4;--hat:transparent"'),
    ("Đặt trên nền rối", 'data-busy="1"'),
]


CSS = """
/* Bố cục: cẩm nang dạng trang in, mỗi phần là một trang có số trang; lưới 12 cột, nhiều khoảng trắng. */
:root{--red:#A8160F;--red2:#D7150E;--ivory:#F6F1E8;--paper:#FBF8F2;--ink:#1F1714;--gold:#C39443;--flour:#E9DFCC;--muted:#6E5F56;--line:#DCD0BD;
--f:'BVP','Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--ivory);color:var(--ink);font:400 16px/1.65 var(--f);-webkit-font-smoothing:antialiased;padding-inline:0}
img,svg{max-width:100%}
.w{max-width:1200px;margin:0 auto;padding-inline:40px}
.page{padding-block:112px;border-top:1px solid var(--line)}
.page.dark{background:var(--ink);color:var(--ivory);border-color:var(--ink)}
.page.red{background:var(--red);color:var(--ivory);border-color:var(--red)}
.page.paper{background:var(--paper)}
.ph{display:flex;justify-content:space-between;align-items:baseline;font:500 11px/1 var(--f);letter-spacing:.24em;text-transform:uppercase;color:var(--muted);padding-bottom:18px;border-bottom:1px solid var(--line);margin-bottom:64px}
.dark .ph,.red .ph{color:rgba(246,241,232,.62);border-color:rgba(246,241,232,.2)}
.ph b{font-weight:600;color:var(--red)}.dark .ph b,.red .ph b{color:var(--gold)}
.head{display:grid;grid-template-columns:5fr 7fr;gap:48px;align-items:end;margin-bottom:64px}
h2{font:300 clamp(36px,5.2vw,64px)/1.04 var(--f);letter-spacing:-.035em;text-wrap:balance}
h2 strong{font-weight:600}
.head p{color:var(--muted);max-width:58ch;font-size:16px}
.dark .head p,.red .head p{color:rgba(246,241,232,.75)}
h3{font:600 15px/1.3 var(--f);letter-spacing:-.005em}
.lab{font:500 11px/1.3 var(--f);letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.dark .lab,.red .lab{color:rgba(246,241,232,.6)}
svg.wm,svg.stack,svg.horiz,svg.badge,svg.a,svg.amt{display:block;height:auto}

/* bìa */
.cover{background:var(--red);color:var(--ivory);min-height:760px;display:flex;flex-direction:column;padding-block:40px;position:relative;overflow:hidden}
.cover .w{width:100%;flex:1;display:flex;flex-direction:column}
.cv-top{display:flex;justify-content:space-between;font:500 11px/1 var(--f);letter-spacing:.26em;text-transform:uppercase;opacity:.75}
.cv-mid{flex:1;display:grid;grid-template-columns:1fr auto;align-items:center;gap:40px;padding-block:72px}
.cv-mid svg.stack{width:min(100%,620px)}
.cv-mid svg.badge{width:190px;--bb:var(--ivory);--ba:var(--red)}
.cv-bot{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;border-top:1px solid rgba(246,241,232,.25);padding-top:20px;font-size:13px;opacity:.85}
.cv-bot b{display:block;font:500 11px/1.2 var(--f);letter-spacing:.22em;text-transform:uppercase;opacity:.7;margin-bottom:6px}
.cv-arcs{position:absolute;right:-160px;bottom:-240px;width:720px;opacity:.16;pointer-events:none}

/* mục lục + ý tưởng */
.toc{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--line)}
.toc div{padding:20px 20px 20px 0;border-bottom:1px solid var(--line);display:flex;gap:16px;font-size:15px}
.toc span{font:500 12px/1.9 var(--f);color:var(--red);font-variant-numeric:tabular-nums;min-width:22px}
.idea{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);margin-top:72px}
.idea > div{background:var(--ivory);padding:36px 32px 32px;display:flex;flex-direction:column;gap:14px}
.idea svg{height:150px;width:100%}
.idea p{font-size:14px;color:var(--muted)}
.quote{margin-top:72px;font:300 clamp(26px,3.2vw,40px)/1.3 var(--f);letter-spacing:-.02em;max-width:26ch}
.quote em{font-style:normal;font-weight:600;color:var(--red)}

/* logo */
.hero-logo{background:var(--paper);border:1px solid var(--line);display:grid;place-items:center;padding:110px 40px;position:relative}
.hero-logo svg.stack{width:min(100%,640px);color:var(--ink)}
.corner{position:absolute;font:500 10px/1 var(--f);letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.corner.tl{top:18px;left:20px}.corner.br{bottom:18px;right:20px}
.cons{width:100%;height:auto;display:block;margin-top:48px;overflow:visible}
.cons .cx{font:500 6px var(--f);fill:var(--red);letter-spacing:.06em}
.spec3{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:40px}
.spec3 div{border-top:1px solid var(--ink);padding-top:14px}
.spec3 p{font-size:14px;color:var(--muted);margin-top:6px}

/* biến thể */
.vars{display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
.v{display:grid;place-items:center;padding:56px 36px;min-height:280px;position:relative}
.v .lab{position:absolute;left:18px;bottom:16px}
.v1{grid-column:span 4;background:var(--paper);border:1px solid var(--line)}
.v2{grid-column:span 2;background:var(--red)}
.v3{grid-column:span 2;background:var(--ink)}
.v4{grid-column:span 2;background:var(--flour)}
.v5{grid-column:span 2;background:var(--paper);border:1px solid var(--line)}
.v6{grid-column:span 3;background:var(--red)}
.v7{grid-column:span 3;background:#fff;border:1px solid var(--line)}
.v2 .lab,.v3 .lab,.v6 .lab{color:rgba(246,241,232,.65)}
.vars svg.horiz{width:min(100%,560px)}
.vars svg.stack{width:min(100%,300px)}
.vars svg.badge{width:110px}
.vars svg.a{width:62px}

/* vùng an toàn */
.safe{display:grid;grid-template-columns:7fr 5fr;gap:16px}
.safe .box{background:var(--paper);border:1px solid var(--line);padding:64px 40px;display:grid;place-items:center}
.cz{position:relative;padding:34px;background:repeating-linear-gradient(45deg,rgba(168,22,15,.07) 0 6px,transparent 6px 12px)}
.cz::before{content:"";position:absolute;inset:34px;background:var(--paper)}
.cz svg{position:relative;width:min(100%,420px);color:var(--ink)}
.cz i{position:absolute;font:600 11px/1 var(--f);color:var(--red);font-style:normal}
.cz i.t{top:12px;left:50%}.cz i.l{left:12px;top:50%}
.mins{display:flex;gap:40px;align-items:end;flex-wrap:wrap;justify-content:center}
.mins div{text-align:center;display:flex;flex-direction:column;align-items:center;gap:14px}
.mins small{font:500 11px/1.4 var(--f);color:var(--muted);letter-spacing:.06em}

/* không được */
.dont{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.dont figure{background:var(--paper);border:1px solid var(--line);aspect-ratio:3/2;display:grid;place-items:center;position:relative;overflow:hidden;padding:24px}
.dont figure svg.stack{width:62%;color:var(--ink)}
.dont figcaption{position:absolute;left:16px;bottom:14px;display:flex;gap:10px;align-items:center;font:500 13px/1.2 var(--f)}
.dont figcaption::before{content:"";width:18px;height:18px;border-radius:50%;background:var(--red) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M6 6l6 6M12 6l-6 6' stroke='%23fff' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E") center/100% no-repeat;flex:none}
.dont figure svg{position:relative}
.dont .busy{position:absolute;inset:0;background-size:120px;opacity:.9}

/* màu */
.pal{display:grid;grid-template-columns:repeat(12,1fr);gap:16px}
.sw{display:flex;flex-direction:column;min-height:360px}
.sw .chip{flex:1;padding:22px;display:flex;align-items:flex-start;justify-content:space-between;font:300 44px/1 var(--f);letter-spacing:-.03em}
.sw .chip small{font:500 11px/1.4 var(--f);letter-spacing:.14em;text-transform:uppercase;text-align:right}
.sw dl{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;padding:16px 2px 0;font-size:13px;font-variant-numeric:tabular-nums}
.sw dt{color:var(--muted);font:500 11px/1.9 var(--f);letter-spacing:.14em}
.sw h3{padding:16px 2px 0}
.c1{grid-column:span 5}.c2{grid-column:span 4}.c3{grid-column:span 3}.c4{grid-column:span 4}.c5{grid-column:span 4}.c6{grid-column:span 4}
.c4 .chip,.c5 .chip,.c6 .chip{min-height:150px}
.c4,.c5,.c6{min-height:0}
.ratio{display:flex;height:22px;margin-top:40px;border:1px solid var(--line)}
.ratio span{display:block}
.note{font-size:13px;color:var(--muted);margin-top:16px;max-width:80ch}

/* chữ */
.type{display:grid;grid-template-columns:5fr 7fr;gap:16px}
.tspec{background:var(--paper);border:1px solid var(--line);padding:40px}
.glyph{white-space:nowrap;font:300 140px/.9 var(--f);letter-spacing:-.05em;color:var(--red)}
.glyph b{font-weight:600}
.weights{display:flex;gap:22px;margin-top:28px;font-size:22px;flex-wrap:wrap}
.chars{margin-top:24px;font:400 15px/1.8 var(--f);color:var(--muted);letter-spacing:.06em;word-break:break-all}
.scale > div{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:baseline;padding:22px 0;border-bottom:1px solid var(--line)}
.scale small{font:500 11px/1.5 var(--f);color:var(--muted);letter-spacing:.1em;text-align:right;white-space:nowrap}
.t1{font:300 56px/1.02 var(--f);letter-spacing:-.04em}.t1 b{font-weight:600}
.t2{font:500 26px/1.2 var(--f);letter-spacing:-.02em}
.t3{font:500 12px/1 var(--f);letter-spacing:.24em;text-transform:uppercase;color:var(--red)}
.t4{font:400 16px/1.65 var(--f);max-width:48ch}
.t5{font:400 12px/1.5 var(--f);color:var(--muted)}

/* hoạ tiết */
.pats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.pat svg{width:100%;aspect-ratio:1;display:block}
.pat figcaption{padding-top:14px;font-size:13px;color:var(--muted)}
.pat figcaption b{display:block;color:var(--ink);font:600 14px/1.4 var(--f)}
.dark .pat figcaption{color:rgba(246,241,232,.65)}.dark .pat figcaption b{color:var(--ivory)}

/* sản phẩm */
.prod{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.prod .arch{aspect-ratio:3/4;border-radius:999px 999px 0 0;display:grid;place-items:end center;padding:0 12% 14%;position:relative}
.prod .arch::after{content:"";position:absolute;inset:10px 10px 0;border-radius:999px 999px 0 0;border:1px solid rgba(168,22,15,.35);border-bottom:0}
.prod h3{margin-top:18px;font-size:17px}
.prod p{font-size:14px;color:var(--muted)}
.photo{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:56px}
.photo div{border-top:1px solid var(--ink);padding-top:16px}
.photo ul{padding-left:18px;margin-top:8px;font-size:14px;color:var(--muted);display:grid;gap:4px}

/* ứng dụng */
.apps{display:grid;grid-template-columns:repeat(12,1fr);gap:16px}
.app{position:relative;overflow:hidden}
.app .lab{margin-top:14px;display:block}
.scene{display:grid;place-items:center;overflow:hidden}
.span12{grid-column:span 12}.span7{grid-column:span 7}.span5{grid-column:span 5}.span6{grid-column:span 6}.span4{grid-column:span 4}.span8{grid-column:span 8}
.sc-card{background:linear-gradient(160deg,#E7DDCC,#D6C8B1);aspect-ratio:7/5;position:relative;perspective:1400px}
.nc{position:absolute;width:52%;aspect-ratio:90/54;box-shadow:0 1px 1px rgba(0,0,0,.08),0 18px 30px -12px rgba(40,20,10,.45),0 40px 60px -30px rgba(40,20,10,.35)}
.nc.front{background:var(--red);left:10%;top:18%;transform:rotate(-8deg);display:flex;align-items:center;gap:8%;padding:0 9%}
.nc.front svg.badge{width:17%}
.nc.front svg.stack{width:58%}
.nc.back{background:var(--paper);right:8%;bottom:14%;transform:rotate(5deg);padding:6% 7%;display:grid;grid-template-rows:auto 1fr auto;font-size:clamp(8px,1vw,12px);color:var(--ink)}
.nc-top{display:flex;align-items:center;gap:10px;font:600 .8em/1 var(--f);letter-spacing:.24em;color:var(--red)}
.nc-top svg{height:2.6em !important}
.nc-name{align-self:center}
.nc-name b{display:block;font:600 1.3em/1.3 var(--f)}.nc-name span{color:var(--muted)}
.nc-ct{display:flex;gap:1.6em;flex-wrap:wrap;border-top:1px solid var(--line);padding-top:.8em;font-variant-numeric:tabular-nums}
.mock{display:block;width:100%;height:auto}
.mk-t{font-family:'BVP',sans-serif;font-weight:500;font-size:11px;letter-spacing:.24em}
.bg-bag{background:linear-gradient(180deg,#EDE5D7,#DDD1BD)}
.bg-pack{background:linear-gradient(180deg,#2B211D,#1A1311)}
.bg-seal{background:linear-gradient(160deg,#EFE7D9,#E0D4C0);display:grid;place-items:center;padding:48px}
.seal{width:min(100%,280px)}
.bg-paper{background:linear-gradient(160deg,#D9CDB8,#C7B89E);display:grid;place-items:center;padding:48px 32px}
.a4{background:#fff;width:min(100%,430px);aspect-ratio:210/297;padding:8% 8% 6%;display:flex;flex-direction:column;gap:6%;box-shadow:0 30px 50px -20px rgba(40,20,10,.5);transform:rotate(-2deg);font-size:clamp(7px,.9vw,11px)}
.a4-h{display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid var(--gold);padding-bottom:5%}
.a4-h svg.horiz{width:55%}
.a4-h span{font:600 1.3em/1.3 var(--f);letter-spacing:.2em;text-align:right;color:var(--red)}
.a4-h em{font:400 .8em/1 var(--f);letter-spacing:0;color:var(--muted);font-style:normal}
.a4-to span{display:block;color:var(--muted)}.a4-to b{font-weight:600}
.a4-l{display:grid;gap:.9em}.a4-l i{display:block;height:.45em;background:#ECE5D9}
.a4 table{border-collapse:collapse;width:100%;font-size:.82em}
.a4 th{text-align:left;font-weight:600;border-bottom:1px solid var(--ink);padding:.6em 0}
.a4 td{border-bottom:1px solid var(--line);padding:.6em 0;color:var(--muted)}
.a4-f{margin-top:auto;display:flex;justify-content:space-between;gap:1em;border-top:1px solid var(--line);padding-top:4%;color:var(--muted);font-size:.85em}
.bg-phone{background:linear-gradient(160deg,var(--red),#7E100A);display:grid;place-items:center;padding:48px 24px}
.phone{width:min(100%,300px);background:#111;border-radius:40px;padding:12px;box-shadow:0 30px 60px -20px rgba(0,0,0,.6)}
.ph-scr{background:#fff;border-radius:30px;overflow:hidden;color:#1c1e21}
.ph-bar{display:flex;gap:10px;align-items:center;padding:16px 14px 10px;font-size:12px}
.ph-bar b{display:block;font-weight:600;font-size:13px}.ph-bar small{color:#65676b}
.ph-av{width:34px;height:34px;border-radius:50%;background:var(--ivory);display:grid;place-items:center;overflow:hidden;flex:none}
.ph-av svg{width:48%}
.ph-post svg{display:block;width:100%;height:auto}
.ph-cap{padding:12px 14px 18px;font-size:12px;line-height:1.5}

/* bìa sau */
.back{background:var(--ink);color:var(--ivory);padding-block:96px 48px}
.back .w{display:grid;grid-template-columns:1fr auto;gap:48px;align-items:end}
.back svg.stack{width:min(100%,380px)}
.back p{margin-top:28px;font-size:13px;color:rgba(246,241,232,.62);max-width:56ch}
.back .ct{text-align:right;font:500 14px/1.9 var(--f);font-variant-numeric:tabular-nums}
.back .ct small{display:block;font:500 11px/1.4 var(--f);letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}

a:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
@media (max-width:900px){
 .w{padding-inline:20px}.page{padding-block:72px}.ph{margin-bottom:40px}
 .head{grid-template-columns:1fr;gap:18px;margin-bottom:40px}
 .cover{min-height:0}.cv-mid{grid-template-columns:1fr;padding-block:56px}.cv-mid svg.badge{width:120px}.cv-bot{grid-template-columns:1fr}
 .toc{grid-template-columns:1fr 1fr}.idea{grid-template-columns:1fr}
 .spec3{grid-template-columns:1fr;gap:20px}
 .vars{grid-template-columns:1fr 1fr}.v1,.v6,.v7{grid-column:1/-1}.v2,.v3,.v4,.v5{grid-column:span 1}.v{min-height:200px;padding:44px 20px}
 .safe{grid-template-columns:1fr}.dont{grid-template-columns:1fr 1fr}
 .pal{grid-template-columns:1fr 1fr}.c1,.c2,.c3,.c4,.c5,.c6{grid-column:span 1}.sw{min-height:220px}.c1{grid-column:1/-1}
 .type{grid-template-columns:1fr}.glyph{font-size:120px}.t1{font-size:40px}
 .pats,.prod{grid-template-columns:1fr 1fr}.photo{grid-template-columns:1fr}
 .span7,.span5,.span6,.span4,.span8{grid-column:1/-1}
 .back .w{grid-template-columns:1fr}.back .ct{text-align:left}
}
@media (max-width:480px){.dont{grid-template-columns:1fr}.toc{grid-template-columns:1fr}.scale > div{grid-template-columns:1fr;gap:6px}.scale small{text-align:left}}
"""


def page_head(num, title):
    return f'<div class="ph"><span>Ẩm Thực An Tâm · Cẩm nang nhận diện</span><span>{title} · <b>{num:02d}</b></span></div>'


def color_block():
    cols = [
        ("c1", RED, IVORY, "Đỏ An Tâm", "Màu chính. Nền lớn, bao bì, biển hiệu.", "25%"),
        ("c2", IVORY, INK, "Kem bột", "Nền chủ đạo của mọi ấn phẩm.", "60%"),
        ("c3", INK, IVORY, "Mực", "Chữ, nền tối cao cấp.", "10%"),
        ("c4", GOLD, INK, "Vàng lúa", "Chỉ cho dấu mũ, nét viền mảnh.", "5%"),
        ("c5", RED2, IVORY, "Đỏ logo gốc", "Giữ cho tem khuyến mãi, nhấn nhỏ.", ""),
        ("c6", FLOUR, INK, "Bột mì", "Nền phụ, ô sản phẩm.", ""),
    ]
    out = []
    for cls, bg, fg, name, use_, pct in cols:
        border = "border:1px solid var(--line);" if bg in (IVORY, FLOUR) else ""
        out.append(f'<div class="sw {cls}"><div class="chip" style="background:{bg};color:{fg};{border}">{pct}<small>{name}</small></div>'
                   f'<h3>{name}</h3><dl><dt>HEX</dt><dd>{bg}</dd><dt>RGB</dt><dd>{rgb(bg)}</dd><dt>CMYK</dt><dd>{cmyk(bg)}</dd></dl>'
                   f'<p class="note" style="margin-top:6px">{use_}</p></div>')
    ratio = "".join(f'<span style="flex:{f};background:{c}"></span>' for f, c in [(60, IVORY), (25, RED), (10, INK), (5, GOLD)])
    return "".join(out), ratio


def page():
    idea_arch = f'<svg viewBox="0 0 200 150" aria-hidden="true"><path d="M60,150 V70 a40,40 0 0 1 80,0 V150" fill="none" stroke="{RED}" stroke-width="1.5"/><path d="M72,150 V70 a28,28 0 0 1 56,0 V150" fill="none" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 3"/></svg>'
    idea_moon = f'<svg viewBox="0 0 200 150" aria-hidden="true"><path d="M58,110 a42,42 0 0 1 84,0 z" fill="{GOLD}"/><path d="M40,110 H160" stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/></svg>'
    idea_a = f'<svg viewBox="0 0 200 150" aria-hidden="true"><use href="#a" x="72" y="12" width="56" height="94" style="color:{RED}"/></svg>'
    colors, ratio = color_block()
    prods = "".join(f'<div><div class="arch" style="background:{bg}"><img src="{ill(n)}" alt="{t}"></div><h3>{t}</h3><p>{d}</p></div>' for n, t, d, bg in PRODUCTS)
    busy = ill("nguyen-lieu")
    donts = "".join(
        f'<figure>{f"<div class=busy style=background-image:url({busy})></div>" if "busy" in s else ""}'
        f'<svg class="stack" viewBox="0 -30 494 208" {s if "busy" not in s else ""} aria-hidden="true"><use href="#stack" x="0" y="-30" width="494" height="208"/></svg>'
        f'<figcaption>{t}</figcaption></figure>'
        for t, s in MISUSE)
    # sửa: style trên svg phải gộp với position
    cover_arcs = "".join(f'<path d="M{360 - w},720 V{360} a{w},{w} 0 0 1 {2 * w},0 V720" fill="none" stroke="{IVORY}" stroke-width="2"/>' for w in (340, 280, 220, 160, 100))
    return f"""<title>Cẩm nang An Tâm</title>
<style>{fontfaces()}
{CSS}</style>
{sprite()}

<header class="cover"><div class="w">
 <div class="cv-top"><span>Cẩm nang nhận diện thương hiệu</span><span>Bản đề xuất · 09/2026</span></div>
 <div class="cv-mid">{use("stack", "", f"color:{IVORY}")}{use("badge")}</div>
 <div class="cv-bot"><div><b>Công ty</b>Công ty TNHH SX-TM Ẩm Thực An Tâm</div><div><b>Sản phẩm</b>Bánh tortillas, taco, doner kebab</div><div><b>Liên hệ</b>0348.635.222 · antamfoods.com</div></div>
</div><svg class="cv-arcs" viewBox="0 0 720 720" aria-hidden="true">{cover_arcs}</svg></header>

<section class="page"><div class="w">
 {page_head(1, "Ý tưởng")}
 <div class="head"><h2>Mái vòm <strong>và nửa chiếc bánh</strong></h2><p>Mái vòm là cửa hàng đón khách, là nơi yên tâm. Nửa chiếc bánh là tortilla gập đôi, sản phẩm của công ty. Hai hình ghép lại thành chữ Â của chữ Tâm.</p></div>
 <div class="toc"><div><span>02</span>Logo chính</div><div><span>03</span>Dựng hình</div><div><span>04</span>Các bản logo</div><div><span>05</span>Vùng an toàn</div><div><span>06</span>Không được làm</div><div><span>07</span>Màu</div><div><span>08</span>Chữ</div><div><span>09</span>Hoạ tiết, hình ảnh, ứng dụng</div></div>
 <div class="idea">
  <div>{idea_arch}<h3>Mái vòm</h3><p>Cổng cửa hàng, ô cửa sổ. Hình của sự đón tiếp, che chở.</p></div>
  <div>{idea_moon}<h3>Nửa chiếc bánh</h3><p>Tortilla gập đôi thành hình bán nguyệt, đặt làm dấu mũ.</p></div>
  <div>{idea_a}<h3>Chữ Â</h3><p>Vòm thành chữ A, bánh thành dấu mũ. Biểu tượng rút gọn của An Tâm.</p></div>
 </div>
 <p class="quote">Sản Phẩm Tận Tâm, <em>Phát Triển Xứng Tầm.</em></p>
</div></section>

<section class="page paper"><div class="w">
 {page_head(2, "Logo chính")}
 <div class="head"><h2>Logo <strong>chính</strong></h2><p>Chữ AN TÂM vẽ riêng: nét mảnh đều, khoảng chữ rộng, hai chữ A là mái vòm. Dòng ẨM THỰC đặt dưới, kẹp giữa hai đường kẻ. Dấu mũ in vàng lúa.</p></div>
 <div class="hero-logo"><span class="corner tl">Bản đứng · dùng chính</span><span class="corner br">Mực trên kem</span>{use("stack")}</div>
</div></section>

<section class="page"><div class="w">
 {page_head(3, "Dựng hình")}
 <div class="head"><h2>Dựng trên <strong>lưới 100</strong></h2><p>Chiều cao chữ là 100 đơn vị. Mọi nét đứng dày 11 (gọi là x). Thanh ngang mảnh hơn một chút, 9,5, để mắt thấy đều. Đỉnh vòm vượt lên 1,6 để bù cảm giác chữ tròn thấp hơn chữ vuông.</p></div>
 {construction()}
 <div class="spec3">
  <div><h3>Vòm đồng tâm</h3><p>Vòm ngoài bán kính 36, vòm trong 25. Lòng chữ A là một ô cửa vòm thu nhỏ.</p></div>
  <div><h3>Khoảng chữ 24, khoảng từ 54</h3><p>Khoảng chữ rộng hơn chữ thường, tạo cảm giác thong thả, cao cấp. Không co giãn khoảng chữ.</p></div>
  <div><h3>Dấu mũ bán kính 15</h3><p>Cách đỉnh chữ 9 đơn vị. Luôn là nửa hình tròn, cạnh phẳng nằm dưới.</p></div>
 </div>
</div></section>

<section class="page paper"><div class="w">
 {page_head(4, "Các bản logo")}
 <div class="head"><h2>Một hệ, <strong>bốn cách đặt</strong></h2><p>Bản đứng dùng chính. Bản ngang cho biển hiệu, đầu thư. Biểu tượng vòm cho ảnh đại diện, tem, bao bì nhỏ. Chữ Â đơn khi chỗ đặt rất hẹp.</p></div>
 <div class="vars">
  <div class="v v1">{use("horiz", "", f"color:{INK}")}<span class="lab">Bản ngang</span></div>
  <div class="v v2">{use("badge", "", f"--bb:{IVORY};--ba:{RED}")}<span class="lab">Biểu tượng vòm</span></div>
  <div class="v v3">{use("stack", "", f"color:{IVORY}")}<span class="lab">Trên nền mực</span></div>
  <div class="v v4">{use("stack", "", f"color:{RED}")}<span class="lab">Đỏ trên bột mì</span></div>
  <div class="v v5">{use("a", "", f"color:{RED}")}<span class="lab">Chữ Â đơn</span></div>
  <div class="v v6">{use("horiz", "", f"color:{IVORY};--bb:{IVORY};--ba:{RED}")}<span class="lab">Bản ngang trên đỏ</span></div>
  <div class="v v7">{use("horiz", "", f"color:#000;--hat:#000;--bb:#000;--ba:#fff")}<span class="lab">Một màu, in đen trắng, con dấu</span></div>
 </div>
</div></section>

<section class="page"><div class="w">
 {page_head(5, "Vùng an toàn")}
 <div class="head"><h2>Chừa <strong>khoảng thở</strong></h2><p>Quanh logo luôn chừa khoảng trống bằng chiều cao chữ A (100 đơn vị trên lưới), đo từ mép ngoài cùng. Không đặt chữ, hình hay mép giấy vào vùng này.</p></div>
 <div class="safe">
  <div class="box"><div class="cz"><i class="t">A</i><i class="l">A</i>{use("stack")}</div></div>
  <div class="box"><div class="mins">
   <div>{use("stack", "", f"width:120px;color:{INK}")}<small>Bản đứng<br>nhỏ nhất 30 mm, 120 px</small></div>
   <div>{use("badge", "", "width:40px")}<small>Biểu tượng<br>nhỏ nhất 8 mm, 32 px</small></div>
   <div>{use("a", "", f"width:16px;color:{RED}")}<small>Chữ Â<br>nhỏ nhất 16 px</small></div>
  </div></div>
 </div>
</div></section>

<section class="page paper"><div class="w">
 {page_head(6, "Không được làm")}
 <div class="head"><h2>Giữ logo <strong>nguyên vẹn</strong></h2><p>Chỉ dùng file logo gốc. Không vẽ lại, không sửa, không thêm hiệu ứng. Khi không chắc, dùng bản mực trên nền kem.</p></div>
 <div class="dont">{donts}</div>
</div></section>

<section class="page"><div class="w">
 {page_head(7, "Màu")}
 <div class="head"><h2>Kem làm nền, <strong>đỏ làm chủ</strong></h2><p>Kem bột chiếm phần lớn diện tích để ấn phẩm thoáng và sang. Đỏ An Tâm là đỏ sâu hơn đỏ logo gốc, dùng cho mảng lớn. Vàng lúa chỉ xuất hiện ở dấu mũ và nét viền mảnh.</p></div>
 <div class="pal">{colors}</div>
 <div class="ratio" role="img" aria-label="Tỉ lệ màu: kem 60, đỏ 25, mực 10, vàng 5">{ratio}</div>
 <p class="note">Tỉ lệ diện tích: kem 60, đỏ 25, mực 10, vàng 5. Mã CMYK là quy đổi tham khảo, cần in thử và chỉnh với nhà in. Không đặt chữ vàng trên nền đỏ. Chữ kem trên đỏ An Tâm đạt tương phản 6,7:1.</p>
</div></section>

<section class="page paper"><div class="w">
 {page_head(8, "Chữ")}
 <div class="head"><h2>Be Vietnam Pro, <strong>từ mảnh tới đậm</strong></h2><p>Một họ chữ cho mọi ấn phẩm, do người Việt thiết kế, dấu tiếng Việt chuẩn. Tiêu đề dùng nét mảnh 300 kèm vài chữ đậm 600 để nhấn, giống cách logo phối nét mảnh với dấu mũ đặc.</p></div>
 <div class="type">
  <div class="tspec"><div class="glyph">Ẩm <b>Ự</b></div>
   <div class="weights"><span style="font-weight:300">Mảnh 300</span><span style="font-weight:400">Thường 400</span><span style="font-weight:500">Vừa 500</span><span style="font-weight:600">Đậm 600</span></div>
   <p class="chars">AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY áàảãạ ắằẳẵặ ấầẩẫậ éèẻẽẹ ếềểễệ óòỏõọ ốồổỗộ ớờởỡợ ứừửữự 0123456789</p></div>
  <div class="tspec scale">
   <div><span class="t1">Gập đôi là <b>ngon</b></span><small>Tiêu đề lớn<br>300 + 600, 56 px</small></div>
   <div><span class="t2">Bánh tortillas giao tận nơi</span><small>Tiêu đề phụ<br>500, 26 px</small></div>
   <div><span class="t3">Nhượng quyền cửa hàng</span><small>Nhãn<br>500, 12 px, giãn 24%</small></div>
   <div><span class="t4">Bữa nhẹ tiện lợi cho nhân viên văn phòng. Đặt qua hotline 0348.635.222 hoặc antamfoods.com.</span><small>Nội dung<br>400, 16 px</small></div>
   <div><span class="t5">Công ty TNHH SX-TM Ẩm Thực An Tâm · TP. Hồ Chí Minh</span><small>Chú thích<br>400, 12 px</small></div>
  </div>
 </div>
</div></section>

<section class="page dark"><div class="w">
 {page_head(9, "Hoạ tiết")}
 <div class="head"><h2>Cắt ra từ <strong>chính logo</strong></h2><p>Bốn hoạ tiết dùng lại hình vòm, nửa chiếc bánh và chữ Â. Mỗi ấn phẩm chỉ dùng một hoạ tiết, để làm nền, không cạnh tranh với logo.</p></div>
 <div class="pats">{patterns()}</div>
</div></section>

<section class="page"><div class="w">
 {page_head(10, "Hình ảnh")}
 <div class="head"><h2>Mỗi món <strong>một ô vòm</strong></h2><p>Minh hoạ sản phẩm luôn đặt trong khung vòm có viền mảnh, trên nền bột mì. Ảnh chụp thật theo cùng nguyên tắc.</p></div>
 <div class="prod">{prods}</div>
 <div class="photo">
  <div><h3>Ảnh chụp nên</h3><ul><li>Bánh thật, thấy rõ đốm nướng.</li><li>Ánh sáng ấm, tự nhiên, bóng mềm.</li><li>Nền kem, gỗ sáng hoặc vải lanh. Nhiều khoảng trống.</li><li>Cắt khung vòm khi đặt lên ấn phẩm.</li></ul></div>
  <div><h3>Ảnh chụp tránh</h3><ul><li>Ảnh mạng, ảnh kho có sẵn.</li><li>Đèn trắng lạnh, đèn flash gắt.</li><li>Nền rối, nhiều đạo cụ.</li><li>Mũ rộng vành, xương rồng, ria mép.</li></ul></div>
 </div>
</div></section>

<section class="page paper"><div class="w">
 {page_head(11, "Ứng dụng")}
 <div class="head"><h2>Từ tấm danh thiếp <strong>tới mặt tiền</strong></h2><p>Các mô phỏng dưới đây dùng đúng logo, màu và chữ của cẩm nang. Những chỗ ghi [Cần điền] chờ thông tin thật từ công ty.</p></div>
 <div class="apps">
  <div class="app span7">{card_scene()}<span class="lab">Danh thiếp · 90 × 54 mm</span></div>
  <div class="app span5"><div class="scene bg-bag">{bag_svg()}</div><span class="lab">Túi giấy kraft</span></div>
  <div class="app span12"><div class="scene">{store_svg()}</div><span class="lab">Mặt tiền cửa hàng nhượng quyền</span></div>
  <div class="app span4"><div class="scene bg-pack">{pack_svg()}</div><span class="lab">Gói bánh tortillas</span></div>
  <div class="app span4"><div class="scene bg-paper">{letter_html()}</div><span class="lab">Báo giá cho doanh nghiệp · A4</span></div>
  <div class="app span4"><div class="scene bg-phone">{phone_html()}</div><span class="lab">Bài đăng Facebook · 1080 × 1350</span></div>
  <div class="app span4"><div class="scene bg-seal">{seal_svg()}</div><span class="lab">Tem niêm phong · 50 mm</span></div>
  <div class="app span8"><div class="scene" style="background:{INK};padding:56px 32px;display:flex;gap:40px;justify-content:center;flex-wrap:wrap">
    <div style="width:140px;aspect-ratio:1;border-radius:50%;background:{RED};display:grid;place-items:center">{use("a", "", f"width:50px;color:{IVORY}")}</div>
    <div style="width:140px;aspect-ratio:1;border-radius:32px;background:{IVORY};display:grid;place-items:center">{use("badge", "", "width:62px")}</div>
    <div style="width:140px;aspect-ratio:1;border-radius:50%;background:{IVORY};display:grid;place-items:center">{use("a", "", f"width:50px;color:{RED}")}</div>
  </div><span class="lab">Ảnh đại diện Facebook, Zalo OA, biểu tượng ứng dụng</span></div>
 </div>
</div></section>

<footer class="back"><div class="w">
 <div>{use("stack", "", f"color:{IVORY}")}<p>Bản đề xuất hướng Vòm, chờ công ty duyệt. Logo gốc vẫn là logo chính thức cho tới khi duyệt. Chữ Be Vietnam Pro dùng theo giấy phép SIL Open Font License.</p></div>
 <div class="ct"><small>Liên hệ</small>0348.635.222<br>antamfoods.com<br>TP. Hồ Chí Minh</div>
</div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

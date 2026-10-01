"""Bảng 5 ý tưởng mới cho Ẩm Thực An Tâm (màu đỏ làm nền tảng). Chạy: python3 y_tuong.py OUT.html"""
import base64
import math
import os
import random
import sys
from functools import lru_cache

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
FONTS = {"b9": "fonts-bv/BeVietnamPro-900.ttf", "b8": "fonts-bv/BeVietnamPro-800.ttf", "b6": "fonts-bv/BeVietnamPro-600.ttf", "b4": "fonts-bv/BeVietnamPro-400.ttf",
         "nen": "fonts-tem/bsd-900.ttf", "nen7": "fonts-tem/bsd-700.ttf", "tay": "fonts-hand/shantell-sans-800.ttf"}
DO, DO2, KEM, NGO, DEN, XANHSN, LA = "#D2141E", "#8F0D14", "#FFF6EA", "#F5B82E", "#231716", "#1F5AA6", "#3E8A3A"


@lru_cache(None)
def _f(k):
    f = TTFont(os.path.join(HERE, FONTS[k])); return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm


def T(t, size, x=0, y=0, fill=DO, k="b8", anchor="start", track=0.0):
    f, gs, cm, upm = _f(k); s = size / upm; cx = 0; parts = []
    for ch in t:
        n = cm.get(ord(ch))
        if not n:
            continue
        pen = SVGPathPen(gs); gs[n].draw(pen); d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({cx:.1f} 0) scale({s:.4f} {-s:.4f})" d="{d}"/>')
        cx += f["hmtx"][n][0] * s + size * track
    w = cx - size * track; ox = {"start": 0, "middle": -w / 2, "end": -w}[anchor]
    return f'<g fill="{fill}" transform="translate({x + ox:.1f} {y:.1f})">{"".join(parts)}</g>'


def Tw(t, size, k="b8", track=0.0):
    f, gs, cm, upm = _f(k); s = size / upm
    return sum(f["hmtx"][cm[ord(c)]][0] * s + size * track for c in t if ord(c) in cm) - size * track


def svg(w, h, body, label, bg=None):
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{r}{body}</svg>'


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def img(n, x, y, w, h):
    return f'<image href="{b64(f"{MH}/{n}.svg", "image/svg+xml")}" x="{x}" y="{y}" width="{w}" height="{h}"/>'


# ===== 1. Bảng số nhà Sài Gòn =====
def so_nha(x, y, w, h, bg=DO, fg=KEM, top="XƯỞNG BÁNH", big="AN TÂM", bot="TP. HỒ CHÍ MINH"):
    """Biển số nhà tráng men kiểu Sài Gòn: chữ nhật bo góc, viền trắng kép, hai đinh vít."""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h * .14:.0f}" fill="{bg}"/>'
    s += f'<rect x="{x + h * .06:.1f}" y="{y + h * .06:.1f}" width="{w - h * .12:.1f}" height="{h - h * .12:.1f}" rx="{h * .1:.0f}" fill="none" stroke="{fg}" stroke-width="{h * .03:.1f}"/>'
    for sx in (x + h * .17, x + w - h * .17):
        s += f'<circle cx="{sx:.1f}" cy="{y + h / 2:.1f}" r="{h * .045:.1f}" fill="{fg}"/><path d="M{sx - h * .03:.1f},{y + h / 2:.1f} h{h * .06:.1f}" stroke="{bg}" stroke-width="{h * .012:.1f}"/>'
    s += f'<path d="M{x + h * .32:.1f},{y + h * .3:.1f} H{x + w - h * .32:.1f} M{x + h * .32:.1f},{y + h * .74:.1f} H{x + w - h * .32:.1f}" stroke="{fg}" stroke-width="{h * .012:.1f}"/>'
    s += T(top, h * .13, x + w / 2, y + h * .24, fg, "b8", "middle", .28)
    s += T(big, h * .42, x + w / 2, y + h * .66, fg, "nen", "middle", .03)
    s += T(bot, h * .11, x + w / 2, y + h * .88, fg, "b6", "middle", .3)
    return s


def y1_logo():
    return svg(520, 300, so_nha(30, 40, 460, 220), "Logo biển số nhà An Tâm")


def y1_ung_dung():
    s = '<rect width="520" height="360" fill="#E8DCCB"/><rect y="300" width="520" height="60" fill="#CDBFAA"/>'
    s += '<rect x="40" y="70" width="440" height="230" fill="#F4EAD9"/><rect x="40" y="70" width="440" height="20" fill="#B9A88E"/>'
    s += so_nha(150, 104, 220, 106)
    s += f'<rect x="80" y="232" width="360" height="68" fill="{DO2}"/>' + T("BÁNH TORTILLA · TACO · DONER", 17, 260, 274, KEM, "b8", "middle", .14)
    return svg(520, 360, s, "Mặt tiền xưởng có biển số nhà An Tâm")


# ===== 2. Mẻ bánh sáng =====
def me_sang(cx, cy, s, sun=NGO, banh=KEM, line=DO, bg=DO):
    """Mặt trời nhô lên sau chồng bánh: các lớp bánh là đường chân trời."""
    o = f'<circle cx="{cx}" cy="{cy}" r="{s * .5:.1f}" fill="{bg}"/>'
    o += f'<clipPath id="ms{int(cx)}{int(cy)}"><circle cx="{cx}" cy="{cy}" r="{s * .5:.1f}"/></clipPath><g clip-path="url(#ms{int(cx)}{int(cy)})">'
    o += f'<circle cx="{cx}" cy="{cy + s * .06:.1f}" r="{s * .24:.1f}" fill="{sun}"/>'
    for k in range(9):
        a = math.radians(-180 + k * 22.5)
        o += f'<path d="M{cx + s * .3 * math.cos(a):.1f},{cy + s * .06 + s * .3 * math.sin(a):.1f} L{cx + s * .42 * math.cos(a):.1f},{cy + s * .06 + s * .42 * math.sin(a):.1f}" stroke="{sun}" stroke-width="{s * .035:.1f}" stroke-linecap="round"/>'
    for i in range(3):
        y = cy + s * (.12 + i * .1)
        o += f'<ellipse cx="{cx}" cy="{y:.1f}" rx="{s * (.36 + i * .03):.1f}" ry="{s * .05:.1f}" fill="{banh}" stroke="{line}" stroke-width="{s * .018:.1f}"/>'
    o += "</g>"
    return o


def y2_logo():
    s = me_sang(130, 150, 220) + T("an tâm", 92, 260, 168, DO, "b9", track=-.03) + T("MẺ BÁNH MỚI MỖI SÁNG", 15, 264, 202, DEN, "b8", track=.22)
    return svg(int(260 + Tw("an tâm", 92, "b9", -.03) + 30), 300, s, "Logo Mẻ Sáng")


def y2_ung_dung():
    s = f'<rect width="520" height="360" fill="{NGO}"/>' + me_sang(260, 150, 230, DO, KEM, DO2, KEM)
    s += T("Bánh ra lò lúc [giờ] sáng", 26, 260, 300, DO2, "b9", "middle") + T("giao tận bếp trước giờ mở quán", 16, 260, 330, DEN, "b6", "middle")
    return svg(520, 360, s, "Bài đăng Mẻ Sáng")


# ===== 3. Lát cắt cuộn =====
def xoan(cx, cy, R, turns=3.2, w=None, outer=NGO, fill1=DO, fill2=LA):
    """Lát cắt ngang chiếc bánh cuộn: vòng xoắn bánh vàng, nhân đỏ và rau xanh xen giữa."""
    w = w or R * .14
    o = f'<circle cx="{cx}" cy="{cy}" r="{R:.1f}" fill="{fill1}"/>'
    pts = []
    for k in range(400):
        t = k / 399; a = t * turns * 2 * math.pi; r = R * (.08 + .86 * t)
        pts.append((cx + r * math.cos(a - math.pi / 2), cy + r * math.sin(a - math.pi / 2)))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o += f'<path d="{d}" fill="none" stroke="{fill2}" stroke-width="{w * .45:.1f}" stroke-linecap="round" transform="rotate(40 {cx} {cy})"/>'
    o += f'<path d="{d}" fill="none" stroke="{outer}" stroke-width="{w:.1f}" stroke-linecap="round"/>'
    o += f'<circle cx="{cx}" cy="{cy}" r="{R:.1f}" fill="none" stroke="{outer}" stroke-width="{w:.1f}"/>'
    return o


def y3_logo():
    s = xoan(140, 150, 100) + T("an tâm", 96, 268, 170, DO, "b9", track=-.03) + T("CUỘN TRỌN TẬN TÂM", 15, 272, 204, DEN, "b8", track=.24)
    return svg(int(268 + Tw("an tâm", 96, "b9", -.03) + 30), 300, s, "Logo Lát Cắt Cuộn")


def y3_ung_dung():
    s = f'<rect width="520" height="360" fill="{KEM}"/>'
    s += f'<path d="M150,40 L370,40 L384,330 L136,330 Z" fill="{DO}"/>' + xoan(260, 150, 76, outer=NGO, fill1=DO2, fill2=LA)
    s += T("an tâm", 52, 260, 278, KEM, "b9", "middle", -.02) + T("BÁNH TORTILLA", 13, 260, 304, NGO, "b8", "middle", .26)
    return svg(520, 360, s, "Túi bánh Lát Cắt Cuộn")


# ===== 4. Trao tận tay =====
def tay(cx, cy, s, fill=DO, banh=NGO):
    """Hai bàn tay đỡ chiếc bánh tròn – hai lòng bàn tay ghép thành hình trái tim."""
    o = f'<circle cx="{cx}" cy="{cy - s * .14:.1f}" r="{s * .2:.1f}" fill="{banh}"/>'
    rr = random.Random(2)
    for _ in range(7):
        a = rr.uniform(0, 6.28); d = rr.uniform(0, s * .14)
        o += f'<ellipse cx="{cx + d * math.cos(a):.1f}" cy="{cy - s * .14 + d * math.sin(a):.1f}" rx="{s * .02:.1f}" ry="{s * .012:.1f}" fill="#B9772F"/>'
    for sx in (-1, 1):
        o += (f'<path fill="{fill}" d="M{cx:.1f},{cy + s * .42:.1f} C{cx + sx * s * .08:.1f},{cy + s * .3:.1f} {cx + sx * s * .44:.1f},{cy + s * .16:.1f} {cx + sx * s * .46:.1f},{cy - s * .06:.1f} '
              f'C{cx + sx * s * .47:.1f},{cy - s * .16:.1f} {cx + sx * s * .4:.1f},{cy - s * .2:.1f} {cx + sx * s * .34:.1f},{cy - s * .12:.1f} '
              f'C{cx + sx * s * .3:.1f},{cy - s * .02:.1f} {cx + sx * s * .2:.1f},{cy + s * .08:.1f} {cx:.1f},{cy + s * .1:.1f} Z"/>')
        for j in range(3):
            fy = cy - s * .02 + j * s * .07
            o += f'<path d="M{cx + sx * s * (.36 - j * .02):.1f},{fy:.1f} q{sx * s * .06:.1f},{-s * .02:.1f} {sx * s * .1:.1f},{s * .03:.1f}" stroke="{KEM}" stroke-width="{s * .012:.1f}" fill="none" stroke-linecap="round" opacity=".7"/>'
    return o


def y4_logo():
    s = tay(130, 150, 230) + T("An Tâm", 88, 262, 166, DO, "b9", track=-.02) + T("TRAO TẬN TAY · TẬN TÂM", 15, 266, 200, DEN, "b8", track=.22)
    return svg(int(262 + Tw("An Tâm", 88, "b9", -.02) + 30), 300, s, "Logo Trao Tận Tay")


def y4_ung_dung():
    s = f'<rect width="520" height="360" fill="{DO}"/>' + tay(260, 150, 230, KEM, NGO)
    s += T("Trao tận tay từng mẻ bánh", 26, 260, 312, KEM, "b9", "middle")
    return svg(520, 360, s, "Bài đăng Trao Tận Tay")


# ===== 5. Từ hạt đến bếp =====
def hat(cx, cy, s, fill=DO, banh=NGO):
    """Hạt lúa mì lớn, bên trong là chiếc bánh tròn – nguồn gốc nguyên liệu."""
    o = (f'<path fill="{fill}" d="M{cx:.1f},{cy - s * .5:.1f} C{cx + s * .36:.1f},{cy - s * .3:.1f} {cx + s * .36:.1f},{cy + s * .3:.1f} {cx:.1f},{cy + s * .5:.1f} '
         f'C{cx - s * .36:.1f},{cy + s * .3:.1f} {cx - s * .36:.1f},{cy - s * .3:.1f} {cx:.1f},{cy - s * .5:.1f} Z"/>')
    o += f'<path d="M{cx:.1f},{cy - s * .38:.1f} V{cy + s * .4:.1f}" stroke="{KEM}" stroke-width="{s * .02:.1f}" stroke-dasharray="{s * .04:.1f} {s * .03:.1f}"/>'
    o += f'<circle cx="{cx}" cy="{cy + s * .06:.1f}" r="{s * .15:.1f}" fill="{banh}" stroke="{KEM}" stroke-width="{s * .02:.1f}"/>'
    for sx in (-1, 1):
        o += f'<path d="M{cx + sx * s * .28:.1f},{cy - s * .5:.1f} L{cx + sx * s * .36:.1f},{cy - s * .66:.1f}" stroke="{fill}" stroke-width="{s * .02:.1f}" stroke-linecap="round"/>'
    return o


def y5_logo():
    s = hat(110, 150, 220) + T("ẨM THỰC", 26, 220, 112, DEN, "b8", track=.3) + T("AN TÂM", 92, 216, 190, DO, "b9", track=-.01) + T("TỪ HẠT ĐẾN BẾP", 15, 222, 222, DEN, "b8", track=.3)
    return svg(int(216 + Tw("AN TÂM", 92, "b9", -.01) + 30), 300, s, "Logo Từ Hạt Đến Bếp")


def y5_ung_dung():
    s = f'<rect width="520" height="360" fill="{KEM}"/>'
    steps = [("Bột mì", "[nguồn]"), ("Nhào – cán", "tại xưởng"), ("Nướng mẻ", "mỗi ngày"), ("Giao bếp", "TP.HCM")]
    for i, (a, b) in enumerate(steps):
        x = 70 + i * 128
        s += f'<circle cx="{x}" cy="150" r="46" fill="{DO if i % 2 == 0 else NGO}"/>' + T(str(i + 1), 40, x, 166, KEM if i % 2 == 0 else DO2, "nen", "middle")
        s += T(a, 17, x, 228, DEN, "b8", "middle") + T(b, 13, x, 250, DO, "b6", "middle")
        if i < 3:
            s += f'<path d="M{x + 54},150 h20" stroke="{DO}" stroke-width="4" stroke-linecap="round"/><path d="M{x + 70},144 l6,6 l-6,6" stroke="{DO}" stroke-width="4" fill="none"/>'
    s += T("Hành trình chiếc bánh An Tâm", 24, 260, 72, DO, "b9", "middle")
    return svg(520, 360, s, "Infographic Từ Hạt Đến Bếp")


IDEAS = [
    dict(num="01", name="Biển Số Nhà Sài Gòn", logo=y1_logo, app=y1_ung_dung, pal=[DO, KEM, DO2, DEN],
         insight="Katinat thành công với hình ảnh \"Sài Gòn đương đại\"; khách B2B của An Tâm phần lớn ở TP.HCM.",
         idea="Logo là tấm biển số nhà tráng men quen thuộc của Sài Gòn – nền đỏ, viền trắng, hai đinh vít, chữ AN TÂM nén đậm. Thông điệp: một xưởng bánh có địa chỉ thật, ở ngay trong thành phố, gần bếp của bạn.",
         hop="Rất dễ nhớ, rất Sài Gòn, dễ làm biển thật (tráng men, mica). Hợp in tem, nhãn, biển xưởng.", luu="Nét Sài Gòn mạnh – nếu mở rộng ra tỉnh khác vẫn dùng được nhưng cần thay dòng địa danh."),
    dict(num="02", name="Mẻ Bánh Sáng", logo=y2_logo, app=y2_ung_dung, pal=[DO, NGO, KEM, DO2],
         insight="Chủ quán cần bánh có sẵn trước giờ mở cửa; \"tươi mỗi ngày\" là điều khách B2B quan tâm nhất.",
         idea="Mặt trời nhô lên sau chồng ba chiếc bánh – mỗi lớp bánh là một đường chân trời. Biểu tượng cho mẻ bánh mới mỗi sáng và sự phát triển đi lên.",
         hop="Ấm áp, tích cực, kể ngay lời hứa \"tươi mỗi sáng\". Dễ làm hoạt hình (mặt trời mọc).", luu="Giờ ra lò, giờ giao phải là cam kết thật – cần công ty xác nhận trước khi dùng."),
    dict(num="03", name="Lát Cắt Cuộn", logo=y3_logo, app=y3_ung_dung, pal=[DO, NGO, LA, KEM],
         insight="Tortilla, doner, taco đều là món cuộn; mặt cắt chiếc bánh cuộn là hình ảnh ngon miệng mà ai cũng nhận ra.",
         idea="Biểu tượng là lát cắt ngang của chiếc bánh cuộn: vòng xoắn bánh vàng, nhân đỏ, rau xanh. Vòng xoắn đi từ trong ra ngoài – lớn dần như sự phát triển.",
         hop="Hiện đại, đơn giản, cực dễ nhận diện ở cỡ nhỏ (biểu tượng ứng dụng, tem). Nói thẳng sản phẩm.", luu="Hình xoắn khá phổ biến trong logo – cần tinh chỉnh kỹ để thành của riêng."),
    dict(num="04", name="Trao Tận Tay", logo=y4_logo, app=y4_ung_dung, pal=[DO, NGO, KEM, DEN],
         insight="Đối tác chọn nhà cung cấp vì con người: được hỗ trợ, được giao tận nơi, có người lo cho mình.",
         idea="Hai bàn tay nâng chiếc bánh tròn; hai lòng bàn tay ghép lại thành hình trái tim – chữ \"Tâm\". Trao tận tay, làm bằng cả tấm lòng.",
         hop="Cảm xúc, ấm, nói về con người và sự tận tâm – đúng tên thương hiệu.", luu="Hình bàn tay cần người vẽ minh hoạ tinh chỉnh để thật đẹp; bản phác này mới là ý."),
    dict(num="05", name="Từ Hạt Đến Bếp", logo=y5_logo, app=y5_ung_dung, pal=[DO, NGO, KEM, DEN],
         insight="Phê La tạo khác biệt bằng câu chuyện nguồn gốc nguyên liệu; xu hướng 2026 đòi hỏi minh bạch.",
         idea="Hạt lúa mì lớn chứa chiếc bánh tròn bên trong; đường nét đứt là hành trình từ hạt bột tới bếp khách. Mọi ấn phẩm kể chuỗi: bột – nhào – nướng – giao.",
         hop="Minh bạch, đáng tin, hợp hồ sơ năng lực và chào hàng B2B.", luu="Cần thông tin thật về nguồn bột, quy trình – những chỗ [ ] phải điền đúng."),
]


CSS = """
:root{--do:#D2141E;--do2:#8F0D14;--kem:#FFF6EA;--ngo:#F5B82E;--den:#231716}
*{box-sizing:border-box;margin:0}html,body{overflow-x:clip}
body{background:var(--kem);color:var(--den);font:16px/1.6 'Be Vietnam Pro',system-ui,sans-serif}
:not(svg)>svg{display:block;width:100%;height:auto}
header{background:var(--do);color:var(--kem)}
header .in{max-width:1200px;margin:0 auto;padding:60px 20px 48px}
.k{font-weight:800;font-size:12px;letter-spacing:.26em;text-transform:uppercase;color:var(--ngo)}
h1{font-weight:900;font-size:clamp(40px,6vw,80px);line-height:1.02;margin:12px 0 16px;letter-spacing:-.02em}
header p{max-width:760px;color:#FFE3E3}
.find{max-width:1200px;margin:36px auto 0;padding:0 20px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.find div{background:#fff;padding:18px;border-radius:14px;font-size:14px}.find b{display:block;color:var(--do);font-size:15px;margin-bottom:4px}
.idea{max-width:1200px;margin:44px auto 0;padding:0 20px}
.c{background:#fff;border-radius:24px;overflow:hidden;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.c .l{padding:28px}.c .r{background:#FBF1E4;padding:20px;display:grid;gap:14px;align-content:start}
.n{font-weight:900;font-size:14px;letter-spacing:.2em;color:var(--do)}
.c h2{font-weight:900;font-size:clamp(28px,3.4vw,40px);line-height:1.05;color:var(--do2);margin:4px 0 12px;letter-spacing:-.01em}
.c h3{font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--do);margin:14px 0 2px}
.pal{display:flex;gap:6px;margin-top:14px}.pal span{width:44px;height:44px;border-radius:10px;border:1px solid #0001}
.r .box{background:#fff;border-radius:16px;padding:14px}
.end{max-width:1200px;margin:56px auto 80px;padding:0 20px;text-align:center}
.end h2{font-weight:900;font-size:clamp(28px,4vw,48px);color:var(--do)}
.src{max-width:1200px;margin:24px auto 0;padding:0 20px;font-size:13px;color:#6b5a55}.src a{color:var(--do)}
@media (max-width:860px){.c,.find{grid-template-columns:minmax(0,1fr)}}
"""


def faces():
    out = []
    for w in (400, 600, 800, 900):
        for s in ("latin", "vietnamese"):
            out.append(f"@font-face{{font-family:'Be Vietnam Pro';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, 'be-vietnam-pro', 'files', f'be-vietnam-pro-{s}-{w}-normal.woff2'), 'font/woff2')}) format('woff2')}}")
    return "\n".join(out)


def page():
    cards = ""
    for d in IDEAS:
        pal = "".join(f'<span style="background:{c}"></span>' for c in d["pal"])
        cards += f"""<section class="idea" id="y{d['num']}"><div class="c"><div class="l"><div class="n">Ý TƯỞNG {d['num']}</div><h2>{d['name']}</h2>
<h3>Từ tìm hiểu</h3><p>{d['insight']}</p><h3>Ý tưởng</h3><p>{d['idea']}</p><h3>Điểm mạnh</h3><p>{d['hop']}</p><h3>Cần lưu ý</h3><p>{d['luu']}</p><div class="pal">{pal}</div></div>
<div class="r"><div class="box">{d['logo']()}</div><div class="box">{d['app']()}</div></div></div></section>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ý Tưởng Mới An Tâm</title><style>{faces()}\n{CSS}</style></head><body>
<header><div class="in"><div class="k">Tìm hiểu & lên ý tưởng · Đỏ làm nền tảng</div><h1>5 ý tưởng mới cho Ẩm Thực An Tâm</h1>
<p>Mỗi ý tưởng xuất phát từ một điều tìm hiểu được về thị trường và khách hàng, kèm phác thảo logo và một ứng dụng mẫu. Đây là bản phác để chọn hướng – hướng nào được chọn sẽ làm hoàn chỉnh như các bộ trước.</p></div></header>
<div class="find"><div><b>F&B 2025: bản sắc là sống còn</b>72% thương hiệu F&B mới sao chép thực đơn đối thủ; thương hiệu sống sót là thương hiệu có bản sắc rõ.</div>
<div><b>Câu chuyện Việt thắng thế</b>Phê La kể chuyện nguồn gốc nguyên liệu Việt; Katinat dựng hình ảnh "Sài Gòn đương đại".</div>
<div><b>Ngành kebab: đỏ, cam, que thịt</b>Các chuỗi kebab và nhượng quyền dùng cam, đỏ, xanh dương và hình que thịt quay – rất giống nhau.</div>
<div><b>Thương hiệu tortilla lớn</b>Guerrero (thuộc GRUMA) dùng con dấu tròn "từ xưởng làm bánh" – nhấn vào nguồn gốc xưởng.</div></div>
{cards}
<div class="end"><h2>Bạn chọn ý tưởng số mấy?</h2><p>Có thể ghép: ví dụ biểu tượng của 03 với cách kể chuyện của 05. Chọn xong mình làm hoàn chỉnh logo, màu, chữ, bao bì, biển hiệu và đưa vào Figma.</p></div>
<p class="src">Nguồn: <a href="https://kinhtedouong.vn/thi-truong-fb-viet-nam-2025-khi-ban-sac-tro-thanh-gia-vi-lam-nen-suc-bat-thuong-hieu-128659.html">Kinh tế Đồ uống – F&B 2025: khi bản sắc trở thành gia vị</a> · <a href="https://cafef.vn/cuoc-dua-song-con-cua-cac-thuong-hieu-fb-trong-nam-thanh-loc-2025-dep-doc-khuay-dao-thi-truong-nghin-ty-loat-dai-gia-tat-tay-dua-voi-cac-ong-lon-ngan-hang-188251230103845865.chn">CafeF – Cuộc đua F&B 2025</a> · <a href="https://torkifood.vn/cau-chuyen-thuong-hieu/">Torki Food</a> · <a href="https://www.gruma.com/en/our-brands/locate-a-brand/guerrero.aspx">GRUMA – Guerrero</a> · <a href="https://www.brandsvietnam.com/congdong/topic/5-thuong-hieu-thay-dien-mao-trong-nam-2025-khi-doi-dien-mao-khong-chi-la-thay-logo">Brands Vietnam – 5 thương hiệu thay diện mạo 2025</a></p>
<div style="height:60px"></div></body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

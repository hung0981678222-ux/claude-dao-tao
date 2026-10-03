"""Bộ ứng dụng Điểm Chỉ 1.1 – thiết kế lại 11 hạng mục: ly giấy, áo thun, áo văn phòng, tạp dề, mũ bếp,
quầy kiosk, xe giao hàng, hộp taco, túi tortilla, standee, hồ sơ năng lực.
Mỗi hàm trả về một SVG hoàn chỉnh (mockup trình bày). Chỗ [ ] là thông tin công ty điền thật.
"""
import base64
import io
import math
import os
import re

import bo_ung_dung as U

V, B = U.V, U.B
DO, DO2, SON, KEM, MUC, NGO = U.DO, U.DO2, U.SON, U.KEM, U.MUC, U.NGO
KRAFT, KRAFT2 = U.KRAFT, U.KRAFT2
TRANG = "#FFFDF8"
HOTLINE = "0398 431 300"
W, place = U.W, U.place
ANH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "anh-that")


def S(w, h, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{body}</svg>'


def fit(svg, cx, cy, w=None, h=None):
    """Đặt một SVG con vào tâm (cx, cy) theo bề rộng hoặc chiều cao, giữ tỉ lệ."""
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    r = vb[2] / vb[3]
    if w is None:
        w = h * r
    h = w / r
    return place(svg, f"{cx - w / 2:.1f}", f"{cy - h / 2:.1f}", f"{w:.1f}", f"{h:.1f}")


def mark(cx, cy, r, c=KEM, rings=11):
    return V.van_tay(cx, cy, r, c, rings=rings, aspect=1.15)


def nen(w, h, uid):
    """Phông chụp sản phẩm: tường kem ấm + sàn."""
    return (f'<defs><linearGradient id="bg{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6EEE3"/><stop offset="1" stop-color="#EADFCF"/></linearGradient>'
            f'<filter id="sd{uid}" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#3a2420" flood-opacity=".25"/></filter>'
            f'<filter id="bl{uid}"><feGaussianBlur stdDeviation="10"/></filter>'
            f'<linearGradient id="cy{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".22"/>'
            f'<stop offset=".22" stop-color="#000" stop-opacity="0"/><stop offset=".34" stop-color="#fff" stop-opacity=".28"/><stop offset=".46" stop-color="#fff" stop-opacity="0"/>'
            f'<stop offset=".82" stop-color="#000" stop-opacity=".05"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>'
            f'<linearGradient id="vf{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#bg{uid})"/><rect y="{h * .8:.0f}" width="{w}" height="{h * .2:.0f}" fill="#E2D4C0"/>')


def bong(cx, cy, rx, ry, uid, o=.3):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#3a2420" opacity="{o}" filter="url(#bl{uid})"/>'


def nhan(t, x, y, anchor="middle"):
    return W(t, 13, x, y, "#8A6F63", "xb", anchor, .22)


def thong_so(t, w, h):
    return W(t, 14, 28, h - 22, "#6b5a55", "md")


def anh(n, size=560):
    from PIL import Image
    im = Image.open(os.path.join(ANH, n + ".jpg")); im.thumbnail((size, size))
    b = io.BytesIO(); im.save(b, "JPEG", quality=80)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


# ───────────────────────────── 1. LY GIẤY
def _ly(cx, top, s, body_bg, band, logo_c, uid, big_mark=True, cid="a"):
    tw, bw, hh = 120 * s, 84 * s, 300 * s
    y1 = top + hh
    pts = f"{cx - tw},{top} {cx + tw},{top} {cx + bw},{y1} {cx - bw},{y1}"
    o = f'<clipPath id="c{cid}{uid}"><polygon points="{pts}"/></clipPath>'
    o += f'<g clip-path="url(#c{cid}{uid})"><rect x="{cx - tw}" y="{top}" width="{2 * tw}" height="{hh}" fill="{body_bg}"/>'
    wave = " ".join(f"L{cx - tw + i * 2 * tw / 24:.1f},{top + hh * .56 + 6 * s * math.sin(i / 2.2):.1f}" for i in range(25))
    o += f'<path d="M{cx - tw},{y1} {wave} L{cx + tw},{y1} Z" fill="{band}"/>'
    if big_mark:
        o += f'<g opacity=".95">{mark(cx + 62 * s, top + hh * .86, 58 * s, KEM if band == DO else DO)}</g>'
    o += f'<rect x="{cx - tw}" y="{top}" width="{2 * tw}" height="{hh}" fill="url(#cy{uid})"/></g>'
    o += fit(V.logo_dung(logo_c, MUC if logo_c == DO else KEM), cx, top + hh * .3, w=120 * s)
    # nắp
    o += f'<path d="M{cx - tw - 8 * s},{top + 4 * s} Q{cx},{top - 26 * s} {cx + tw + 8 * s},{top + 4 * s} L{cx + tw + 8 * s},{top + 14 * s} L{cx - tw - 8 * s},{top + 14 * s} Z" fill="#F2ECE4"/>'
    o += f'<rect x="{cx - tw - 10 * s}" y="{top + 2 * s}" width="{2 * tw + 20 * s}" height="{14 * s}" rx="{6 * s}" fill="#E7DFD4"/>'
    o += f'<ellipse cx="{cx + 30 * s}" cy="{top - 12 * s}" rx="{18 * s}" ry="{5 * s}" fill="#D9D0C4"/>'
    return o


def ly_giay():
    u = "ly"; w, h = 900, 640
    s = nen(w, h, u)
    s += bong(330, 556, 120, 16, u) + bong(625, 556, 95, 13, u)
    s += _ly(330, 180, 1.25, KEM, DO, DO, u, cid="a")
    s += _ly(625, 288, .9, DO, DO2, KEM, u, big_mark=False, cid="b")
    s += nhan("LY 12 OZ", 330, 600) + nhan("LY 8 OZ", 625, 600)
    s += thong_so("Ly giấy 2 lớp · in flexo 2 màu Đỏ An Tâm + Kem · logo đứng · 1 dấu vân tay lớn ở dải đỏ", w, h)
    return S(w, h, s, "Ly giấy An Tâm")


# ───────────────────────────── 2–3. ÁO
def _ao_path(cx, cy, s, tay=1.0):
    p = [(-40, -150), (0, -128), (40, -150), (96, -136), (150 * tay + 0 * (1 - tay), -84), (124, -38 if tay == 1 else -56),
         (94, -64), (94, 152), (-94, 152), (-94, -64), (-124, -38 if tay == 1 else -56), (-150 * tay, -84), (-96, -136)]
    if tay != 1:
        p[4] = (138, -92); p[11] = (-138, -92)
    d = "M" + " L".join(f"{cx + x * s:.1f},{cy + y * s:.1f}" for x, y in p) + "Z"
    return d


def _ao(cx, cy, s, fill, uid, cid, tay=1.0, collar=None):
    d = _ao_path(cx, cy, s, tay)
    o = f'<clipPath id="ao{cid}{uid}"><path d="{d}"/></clipPath><g filter="url(#sd{uid})"><path d="{d}" fill="{fill}" stroke="{fill}" stroke-width="{10 * s}" stroke-linejoin="round"/></g>'
    o += f'<g clip-path="url(#ao{cid}{uid})"><rect x="{cx - 160 * s}" y="{cy - 160 * s}" width="{320 * s}" height="{320 * s}" fill="url(#vf{uid})"/>'
    for x0, x1 in ((-60, -30), (40, 70), (-10, 10)):
        o += f'<path d="M{cx + x0 * s},{cy - 40 * s} Q{cx + (x0 + x1) / 2 * s},{cy + 50 * s} {cx + x1 * s},{cy + 150 * s}" stroke="#000" stroke-opacity=".07" stroke-width="{6 * s}" fill="none"/>'
    o += "</g>"
    if collar is None:
        o += f'<path d="M{cx - 40 * s},{cy - 150 * s} Q{cx},{cy - 122 * s} {cx + 40 * s},{cy - 150 * s}" fill="none" stroke="#000" stroke-opacity=".25" stroke-width="{9 * s}" stroke-linecap="round"/>'
    return o


def ao_thun():
    u = "at"; w, h = 900, 640
    s = nen(w, h, u)
    s += _ao(240, 300, 1.25, DO, u, "f") + _ao(660, 300, 1.25, DO, u, "b")
    # mặt trước: biểu tượng ngực trái (bên phải người xem)
    s += mark(240 + 58, 300 - 82, 20, KEM) + W("An Tâm", 15, 240 + 58, 300 - 44, KEM, "xb", "middle")
    # mặt sau
    s += fit(V.logo_dung(KEM, KEM), 660, 230, w=165)
    s += W("Mỗi mẻ bánh, một lời cam kết", 17, 660, 352, KEM, "xb", "middle")
    s += W("antamfoods.com", 13, 660, 378, "#FFD6D3", "md", "middle")
    s += nhan("MẶT TRƯỚC", 240, 525) + nhan("MẶT SAU", 660, 525)
    s += thong_so("Áo thun cotton màu Đỏ An Tâm · in lụa màu Kem · ngực trái biểu tượng 8 cm · lưng logo đứng 24 cm", w, h)
    return S(w, h, s, "Áo thun nhân viên")


def _polo(cx, cy, s, fill, trim, u, cid, logo_c):
    o = _ao(cx, cy, s, fill, u, cid, tay=.8, collar=False)
    # cổ bẻ + nẹp
    o += f'<path d="M{cx - 40 * s},{cy - 150 * s} L{cx - 4 * s},{cy - 104 * s} L{cx - 30 * s},{cy - 96 * s} L{cx - 56 * s},{cy - 140 * s} Z" fill="{trim}"/>'
    o += f'<path d="M{cx + 40 * s},{cy - 150 * s} L{cx + 4 * s},{cy - 104 * s} L{cx + 30 * s},{cy - 96 * s} L{cx + 56 * s},{cy - 140 * s} Z" fill="{trim}"/>'
    o += f'<rect x="{cx - 9 * s}" y="{cy - 120 * s}" width="{18 * s}" height="{72 * s}" fill="#000" opacity=".07"/>'
    for k in range(3):
        o += f'<circle cx="{cx}" cy="{cy - (106 - k * 22) * s}" r="{3.6 * s}" fill="{trim}"/>'
    # viền tay
    o += f'<path d="M{cx + 138 * s},{cy - 92 * s} L{cx + 124 * s},{cy - 56 * s}" stroke="{trim}" stroke-width="{9 * s}"/><path d="M{cx - 138 * s},{cy - 92 * s} L{cx - 124 * s},{cy - 56 * s}" stroke="{trim}" stroke-width="{9 * s}"/>'
    o += fit(V.logo_ngang(logo_c, MUC if logo_c == DO else KEM), cx + 52 * s, cy - 70 * s, w=74 * s)
    return o


def ao_polo():
    u = "ap"; w, h = 900, 640
    s = nen(w, h, u)
    s += _polo(170, 300, 1.0, TRANG, DO, u, "a", DO)
    s += _polo(450, 300, 1.0, MUC, DO, u, "b", KEM)
    s += _ao(730, 300, 1.0, TRANG, u, "c", tay=.8, collar=False)
    s += f'<path d="M690,150 Q730,168 770,150" fill="none" stroke="{DO}" stroke-width="12" stroke-linecap="round"/>'
    s += W("ẨM THỰC AN TÂM", 12, 730, 196, DO, "xb", "middle", .3)
    s += nhan("NHÂN VIÊN VĂN PHÒNG", 170, 520) + nhan("QUẢN LÝ / BÁN HÀNG", 450, 520) + nhan("MẶT SAU", 730, 520)
    s += thong_so("Áo polo cá sấu · nền Kem hoặc Mực, cổ + viền tay Đỏ An Tâm · thêu logo ngang 7 cm ngực trái · sau cổ chữ ẨM THỰC AN TÂM", w, h)
    return S(w, h, s, "Áo văn phòng")


# ───────────────────────────── 4. TẠP DỀ
def _tap_de(cx, cy, s, fill, ink, u, cid, logo=True):
    d = (f"M{cx - 52 * s},{cy - 210 * s} L{cx + 52 * s},{cy - 210 * s} Q{cx + 58 * s},{cy - 120 * s} {cx + 112 * s},{cy - 70 * s} "
         f"L{cx + 122 * s},{cy + 230 * s} Q{cx},{cy + 242 * s} {cx - 122 * s},{cy + 230 * s} L{cx - 112 * s},{cy - 70 * s} Q{cx - 58 * s},{cy - 120 * s} {cx - 52 * s},{cy - 210 * s} Z")
    o = f'<path d="M{cx - 46 * s},{cy - 210 * s} Q{cx},{cy - 330 * s} {cx + 46 * s},{cy - 210 * s}" fill="none" stroke="{ink}" stroke-width="{9 * s}"/>'
    o += f'<path d="M{cx - 112 * s},{cy - 66 * s} q-40,10 -66,{60 * s} M{cx + 112 * s},{cy - 66 * s} q40,10 66,{60 * s}" fill="none" stroke="{ink}" stroke-width="{8 * s}" stroke-linecap="round"/>'
    o += f'<clipPath id="td{cid}{u}"><path d="{d}"/></clipPath><g filter="url(#sd{u})"><path d="{d}" fill="{fill}"/></g>'
    o += f'<g clip-path="url(#td{cid}{u})"><rect x="{cx - 130 * s}" y="{cy - 220 * s}" width="{260 * s}" height="{470 * s}" fill="url(#vf{u})"/>'
    o += f'<path d="M{cx - 120 * s},{cy - 60 * s} L{cx + 120 * s},{cy - 60 * s}" stroke="{ink}" stroke-opacity=".5" stroke-width="{3 * s}" stroke-dasharray="{7 * s} {5 * s}"/></g>'
    if logo:
        o += mark(cx, cy - 140 * s, 34 * s, ink)
        o += W("An Tâm", 30 * s, cx, cy - 68 * s + 34 * s, ink, "xb", "middle")
    # túi trước
    o += f'<rect x="{cx - 90 * s}" y="{cy + 60 * s}" width="{180 * s}" height="{92 * s}" rx="{8 * s}" fill="#000" opacity=".1"/>'
    o += f'<rect x="{cx - 86 * s}" y="{cy + 64 * s}" width="{172 * s}" height="{84 * s}" rx="{6 * s}" fill="none" stroke="{ink}" stroke-opacity=".6" stroke-width="{2 * s}" stroke-dasharray="{6 * s} {4 * s}"/>'
    o += f'<path d="M{cx},{cy + 64 * s} L{cx},{cy + 148 * s}" stroke="{ink}" stroke-opacity=".6" stroke-width="{2 * s}" stroke-dasharray="{6 * s} {4 * s}"/>'
    o += W("Mỗi mẻ bánh, một lời cam kết", 13 * s, cx, cy + 178 * s, ink, "xb", "middle")
    return o


def tap_de():
    u = "td"; w, h = 900, 640
    s = nen(w, h, u)
    s += bong(300, 548, 130, 14, u) + bong(660, 548, 110, 12, u)
    s += _tap_de(300, 300, 1.0, DO, KEM, u, "a")
    s += _tap_de(660, 318, .82, MUC, KEM, u, "b")
    s += nhan("TẠP DỀ BẾP / QUẦY", 300, 600) + nhan("TẠP DỀ XƯỞNG (MÀU MỰC)", 660, 600)
    s += thong_so("Kaki chống thấm · in lụa Kem · dây cổ chỉnh được · 2 túi trước · dấu vân tay ngực 10 cm", w, h)
    return S(w, h, s, "Tạp dề")


# ───────────────────────────── 5. MŨ BẾP
def mu_bep():
    u = "mb"; w, h = 900, 640
    s = nen(w, h, u)
    s += bong(300, 520, 130, 14, u) + bong(650, 500, 120, 12, u)
    # mũ đầu bếp
    cx, by = 300, 440
    puff = f"M{cx - 110},{by - 70} C{cx - 170},{by - 140} {cx - 120},{by - 250} {cx - 50},{by - 230} C{cx - 30},{by - 300} {cx + 60},{by - 300} {cx + 70},{by - 230} C{cx + 140},{by - 250} {cx + 170},{by - 140} {cx + 110},{by - 70} Z"
    s += f'<g filter="url(#sd{u})"><path d="{puff}" fill="{TRANG}"/></g>'
    for k in range(-3, 4):
        s += f'<path d="M{cx + k * 30},{by - 75} Q{cx + k * 34},{by - 160} {cx + k * 26},{by - 220}" stroke="#000" stroke-opacity=".07" stroke-width="5" fill="none"/>'
    s += f'<path d="M{cx - 112},{by - 80} L{cx + 112},{by - 80} L{cx + 116},{by} Q{cx},{by + 14} {cx - 116},{by} Z" fill="{DO}"/>'
    s += f'<path d="M{cx - 112},{by - 80} L{cx + 112},{by - 80} L{cx + 116},{by} Q{cx},{by + 14} {cx - 116},{by} Z" fill="url(#cy{u})"/>'
    s += mark(cx - 62, by - 38, 22, KEM) + W("AN TÂM", 30, cx + 18, by - 26, KEM, "xb", "middle", .14)
    # mũ giấy xưởng (forage cap)
    cx2, by2 = 650, 420
    cap = f"M{cx2 - 150},{by2} L{cx2 - 120},{by2 - 90} Q{cx2},{by2 - 120} {cx2 + 120},{by2 - 90} L{cx2 + 150},{by2} Z"
    s += f'<g filter="url(#sd{u})"><path d="{cap}" fill="{TRANG}"/></g>'
    s += f'<path d="M{cx2 - 150},{by2} L{cx2 + 150},{by2} L{cx2 + 146},{by2 - 30} L{cx2 - 146},{by2 - 30} Z" fill="{DO}"/>'
    s += f'<path d="{cap}" fill="url(#cy{u})"/>'
    s += W("Mỗi mẻ bánh, một lời cam kết", 15, cx2, by2 - 10, KEM, "xb", "middle")
    s += mark(cx2, by2 - 70, 20, DO)
    s += nhan("MŨ BẾP – QUẦY / BẾP ĐỐI TÁC", 300, 600) + nhan("MŨ GIẤY – XƯỞNG SẢN XUẤT", 650, 600)
    s += thong_so("Mũ bếp vải cotton trắng, đai Đỏ An Tâm in Kem · mũ giấy dùng một lần cho xưởng, dải đỏ in câu thương hiệu", w, h)
    return S(w, h, s, "Mũ bếp")


# ───────────────────────────── 6. QUẦY KIOSK
def kiosk():
    u = "kq"; w, h = 1000, 680
    s = nen(w, h, u)
    s += bong(500, 600, 330, 22, u, .35)
    dx, dy = 110, -60      # chiều sâu (mặt bên)
    x0, x1, y0, y1 = 200, 640, 380, 590
    # trụ + bảng hiệu
    for x in (x0 + 20, x1 - 20):
        s += f'<rect x="{x - 8}" y="150" width="16" height="{y0 - 150}" fill="{MUC}"/><rect x="{x - 8 + dx}" y="{150 + dy}" width="14" height="{y0 - 150}" fill="#3b2a27"/>'
    s += f'<polygon points="{x1},{100} {x1 + dx},{100 + dy} {x1 + dx},{190 + dy} {x1},{190}" fill="{DO2}"/>'
    s += f'<rect x="{x0 - 20}" y="100" width="{x1 - x0 + 20}" height="90" fill="{DO}"/>' + fit(V.logo_ngang(KEM, KEM), (x0 + x1) / 2 - 10, 145, h=70)
    s += f'<polygon points="{x0 - 20},{100} {x0 - 20 + dx},{100 + dy} {x1 + dx},{100 + dy} {x1},{100}" fill="#E8303A"/>'
    # bảng thực đơn phía sau
    s += f'<rect x="{x0 + 60}" y="210" width="{x1 - x0 - 120}" height="120" rx="6" fill="{MUC}"/>'
    for i, (m, c) in enumerate((("Tortilla", "22·25·28·31 cm"), ("Taco", "[giá]"), ("Doner kebab", "[giá]"))):
        xx = x0 + 74 + i * 96
        s += W(m, 15, xx, 248, NGO, "xb") + W(c, 12, xx, 270, KEM, "md")
    s += W(f"Đặt hàng: {HOTLINE}", 15, (x0 + x1) / 2, 308, KEM, "xb", "middle")
    # quầy
    s += f'<polygon points="{x1},{y0} {x1 + dx},{y0 + dy} {x1 + dx},{y1 + dy} {x1},{y1}" fill="{DO2}"/>'
    s += f'<polygon points="{x0 - 14},{y0 - 12} {x0 - 14 + dx},{y0 - 12 + dy} {x1 + 14 + dx},{y0 - 12 + dy} {x1 + 14},{y0 - 12}" fill="#D9C2A0"/>'
    s += f'<rect x="{x0 - 14}" y="{y0 - 12}" width="{x1 - x0 + 28}" height="14" fill="#C9AE88"/>'
    s += f'<svg x="{x0}" y="{y0 + 2}" width="{x1 - x0}" height="{y1 - y0 - 2}" viewBox="0 0 {x1 - x0} {y1 - y0 - 2}" preserveAspectRatio="none">{B.nen_van(x1 - x0, y1 - y0).split(">", 1)[1].rsplit("</svg>", 1)[0]}</svg>'
    s += f'<rect x="{x0 + 70}" y="{y0 + 40}" width="{x1 - x0 - 140}" height="{y1 - y0 - 80}" rx="10" fill="{KEM}"/>'
    s += W("Vỏ bánh tươi mỗi ngày", 25, (x0 + x1) / 2, y0 + 98, DO, "xb", "middle")
    s += W("Tortilla · Taco · Doner kebab", 18, (x0 + x1) / 2, y0 + 130, MUC, "md", "middle")
    s += mark((x0 + x1) / 2, y0 + 158, 1, DO) if False else ""
    s += U.img("doner-tru-quay", x0 - 40, y0 - 120, 90, 110) + U.img("banh-tortillas", x1 - 140, y0 - 80, 110, 70)
    s += thong_so(f"Quầy kiosk 2,4 × 1 m · bảng hiệu hộp đèn logo kem trên đỏ · mặt quầy nền đường vân, khung kem · thực đơn nền Mực", w, h)
    return S(w, h, s, "Quầy kiosk")


# ───────────────────────────── 7. XE GIAO HÀNG
def xe_giao_hang():
    u = "xg"; w, h = 1100, 620
    s = nen(w, h, u)
    s += bong(430, 512, 360, 18, u, .4) + bong(910, 512, 120, 14, u, .4)
    bx0, bx1, by0, by1 = 90, 600, 150, 450
    s += f'<clipPath id="hop{u}"><rect x="{bx0}" y="{by0}" width="{bx1 - bx0}" height="{by1 - by0}" rx="10"/></clipPath>'
    s += f'<g filter="url(#sd{u})"><rect x="{bx0}" y="{by0}" width="{bx1 - bx0}" height="{by1 - by0}" rx="10" fill="{DO}"/></g>'
    s += f'<g clip-path="url(#hop{u})"><g opacity=".22">{mark(bx1 - 40, by0 + 170, 190, KEM)}</g>'
    s += f'<rect x="{bx0}" y="{by1 - 46}" width="{bx1 - bx0}" height="46" fill="{DO2}"/><rect x="{bx0}" y="{by0}" width="{bx1 - bx0}" height="{by1 - by0}" fill="url(#vf{u})"/></g>'
    s += fit(V.logo_ngang(KEM, KEM), 280, 245, w=340)
    s += W("Mỗi mẻ bánh, một lời cam kết", 22, bx0 + 34, 352, KEM, "xb")
    s += W(f"Đặt hàng · Zalo  {HOTLINE}", 20, bx0 + 34, 390, NGO, "xb")
    s += W("antamfoods.com", 16, bx1 - 30, by0 + 40, KEM, "md", "end")
    # cabin
    cab = f"M{bx1 + 8},{by0 + 70} L{bx1 + 150},{by0 + 70} Q{bx1 + 175},{by0 + 72} {bx1 + 196},{by0 + 150} L{bx1 + 214},{by0 + 180} L{bx1 + 214},{by1 + 10} L{bx1 + 8},{by1 + 10} Z"
    s += f'<g filter="url(#sd{u})"><path d="{cab}" fill="{TRANG}"/></g><path d="{cab}" fill="url(#vf{u})"/>'
    s += f'<path d="M{bx1 + 30},{by0 + 88} L{bx1 + 142},{by0 + 88} Q{bx1 + 160},{by0 + 92} {bx1 + 178},{by0 + 160} L{bx1 + 30},{by0 + 160} Z" fill="#A9C6D4"/>'
    s += f'<path d="M{bx1 + 30},{by0 + 88} L{bx1 + 80},{by0 + 88} L{bx1 + 40},{by0 + 160} L{bx1 + 30},{by0 + 160} Z" fill="#fff" opacity=".35"/>'
    s += f'<rect x="{bx1 + 8}" y="{by0 + 200}" width="206" height="26" fill="{DO}"/>' + mark(bx1 + 60, by0 + 262, 30, DO)
    s += W("An Tâm", 26, bx1 + 140, by0 + 272, DO, "xb", "middle")
    s += f'<rect x="{bx1 + 196}" y="{by1 - 30}" width="26" height="24" rx="4" fill="#C7BBAE"/><rect x="{bx1 + 206}" y="{by0 + 180}" width="12" height="18" rx="3" fill="{NGO}"/>'
    for x in (200, 470, bx1 + 120):
        s += f'<circle cx="{x}" cy="{by1 + 20}" r="44" fill="#231716"/><circle cx="{x}" cy="{by1 + 20}" r="22" fill="#9a8f86"/><circle cx="{x}" cy="{by1 + 20}" r="8" fill="#5b524c"/>'
    # mặt sau xe
    rx0, rx1, ry0, ry1 = 830, 1010, 150, 450
    s += f'<g filter="url(#sd{u})"><rect x="{rx0}" y="{ry0}" width="{rx1 - rx0}" height="{ry1 - ry0}" rx="8" fill="{DO}"/></g>'
    s += f'<line x1="{(rx0 + rx1) / 2}" y1="{ry0 + 10}" x2="{(rx0 + rx1) / 2}" y2="{ry1 - 10}" stroke="{DO2}" stroke-width="4"/>'
    s += fit(V.logo_dung(KEM, KEM), (rx0 + rx1) / 2, 250, w=130)
    s += W(HOTLINE, 22, (rx0 + rx1) / 2, 380, NGO, "xb", "middle") + W("antamfoods.com", 13, (rx0 + rx1) / 2, 404, KEM, "md", "middle")
    for x in (rx0 + 30, rx1 - 30):
        s += f'<rect x="{x - 22}" y="{ry1}" width="44" height="58" rx="10" fill="#231716"/>'
    s += f'<rect x="{rx0 + 8}" y="{ry1 - 6}" width="18" height="12" fill="{NGO}"/><rect x="{rx1 - 26}" y="{ry1 - 6}" width="18" height="12" fill="{NGO}"/>'
    s += nhan("THÂN XE", 380, 566) + nhan("MẶT SAU", 920, 566)
    s += thong_so("Decal dán thùng xe tải nhẹ · logo kem trên Đỏ An Tâm · hotline vàng bánh cỡ lớn đọc được từ 15 m", w, h)
    return S(w, h, s, "Xe giao hàng")


# ───────────────────────────── 8. HỘP TACO
def _hop(cx, cy, s, u, mo=False):
    a, b, hgt = 150 * s, 70 * s, 70 * s      # nửa rộng, nửa sâu (chiếu), cao
    top = [(cx - a, cy), (cx, cy - b), (cx + a, cy), (cx, cy + b)]
    front_l = [(cx - a, cy), (cx, cy + b), (cx, cy + b + hgt), (cx - a, cy + hgt)]
    front_r = [(cx, cy + b), (cx + a, cy), (cx + a, cy + hgt), (cx, cy + b + hgt)]
    P = lambda pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o = bong(cx, cy + b + hgt + 6, a * 1.05, 14 * s, u)
    o += f'<polygon points="{P(front_l)}" fill="{KEM}"/><polygon points="{P(front_r)}" fill="#EBDDCB"/>'
    o += f'<g transform="translate({cx - a * .55:.1f} {cy + b * .55 + hgt * .55:.1f}) skewY(25)">' + W("TACO", 26 * s, 0, 0, DO, "xb", "middle", .1) + "</g>"
    o += f'<g transform="translate({cx + a * .5:.1f} {cy + b * .5 + hgt * .5:.1f}) skewY(-25)">' + W(HOTLINE, 13 * s, 0, 0, MUC, "xb", "middle") + "</g>"
    if not mo:
        o += f'<polygon points="{P(top)}" fill="{DO}"/>'
        o += f'<g transform="translate({cx} {cy}) scale(1 .47) rotate(45)">{mark(0, 0, 70 * s, KEM)}</g>'
    else:
        inner = [(cx - a + 12 * s, cy), (cx, cy - b + 6 * s), (cx + a - 12 * s, cy), (cx, cy + b - 6 * s)]
        o += f'<polygon points="{P(top)}" fill="#E2D2BC"/><polygon points="{P(inner)}" fill="#F6EBDD"/>'
        o += U.img("taco", cx - 80 * s, cy - 50 * s, 160 * s, 90 * s)
        lid = [(cx - a, cy), (cx, cy - b), (cx, cy - b - 150 * s), (cx - a, cy - 150 * s)]
        o += f'<polygon points="{P(lid)}" fill="{DO}"/><polygon points="{P(lid)}" fill="url(#vf{u})"/>'
        o += f'<g transform="translate({cx - a / 2:.1f} {cy - b / 2 - 75 * s:.1f}) skewY(-25)">{mark(0, -10 * s, 34 * s, KEM)}' + W("An Tâm", 24 * s, 0, 46 * s, KEM, "xb", "middle") + "</g>"
    return o


def hop_taco():
    u = "ht"; w, h = 900, 640
    s = nen(w, h, u)
    s += _hop(270, 360, 1.15, u) + _hop(640, 380, 1.15, u, mo=True)
    s += nhan("HỘP ĐÓNG", 270, 600) + nhan("HỘP MỞ", 640, 600)
    s += thong_so("Hộp giấy kraft tráng PE · nắp in Đỏ An Tâm, thân Kem · vừa 2 taco · đáy in hotline + web", w, h)
    return S(w, h, s, "Hộp taco")


# ───────────────────────────── 9. TÚI TORTILLA (dùng file in thật, phương án AN TÂM)
def tui_tortilla():
    import tui_ten as TT
    import tui_tortilla as T
    T.mat_truoc = TT.mat_truoc_ten; T.WIN = TT.WIN
    s = T.mockup()
    return s.replace('aria-label="Mô phỏng túi bánh tortilla An Tâm"', 'aria-label="Túi bánh tortilla"')


# ───────────────────────────── 10. STANDEE
def standee():
    u = "sd"; w, h = 900, 1000
    s = nen(w, h, u)
    sx0, sw, sy0, sh = 290, 320, 70, 800
    s += bong(450, 912, 220, 16, u, .35)
    s += f'<rect x="{sx0 - 30}" y="{sy0 + sh}" width="{sw + 60}" height="34" rx="8" fill="#B9B2AA"/><rect x="{sx0 - 30}" y="{sy0 + sh}" width="{sw + 60}" height="34" rx="8" fill="url(#cy{u})"/>'
    s += f'<rect x="{sx0 - 30}" y="{sy0 + sh + 28}" width="{sw + 60}" height="8" fill="#8f877e"/>'
    s += f'<g filter="url(#sd{u})"><rect x="{sx0}" y="{sy0}" width="{sw}" height="{sh}" fill="{KEM}"/></g>'
    s += f'<rect x="{sx0 - 4}" y="{sy0 - 8}" width="{sw + 8}" height="10" rx="3" fill="#9e968d"/>'
    s += f'<clipPath id="st{u}"><rect x="{sx0}" y="{sy0}" width="{sw}" height="{sh}"/></clipPath><g clip-path="url(#st{u})">'
    s += f'<rect x="{sx0}" y="{sy0}" width="{sw}" height="300" fill="{DO}"/>'
    s += fit(V.logo_ngang(KEM, KEM), sx0 + sw / 2, sy0 + 70, w=230)
    s += W("Vỏ bánh tươi", 40, sx0 + sw / 2, sy0 + 175, KEM, "xb", "middle") + W("cho quán của bạn", 34, sx0 + sw / 2, sy0 + 222, NGO, "xb", "middle")
    s += W("Tortilla · Taco · Doner kebab", 15, sx0 + sw / 2, sy0 + 262, "#FFD6D3", "md", "middle")
    s += U.img("banh-tortillas", sx0 + 20, sy0 + 320, 90, 70) + U.img("taco", sx0 + 116, sy0 + 320, 90, 70) + U.img("doner-cuon", sx0 + 212, sy0 + 316, 90, 76)
    for i, t in enumerate(("Dây chuyền tự động khép kín", "Chất lượng đều tay mọi mẻ", "Giá xưởng, nói thẳng, rõ ràng")):
        yy = sy0 + 440 + i * 50
        s += mark(sx0 + 38, yy - 6, 13, DO) + W(t, 17, sx0 + 62, yy, MUC, "xb")
    s += f'<rect x="{sx0}" y="{sy0 + sh - 210}" width="{sw}" height="210" fill="{DO}"/>'
    s += f'<rect x="{sx0 + 24}" y="{sy0 + sh - 186}" width="96" height="96" fill="#fff"/>' + W("[QR]", 16, sx0 + 72, sy0 + sh - 132, "#8a7a74", "xb", "middle")
    s += W("Đặt hàng · Zalo", 15, sx0 + 136, sy0 + sh - 160, "#FFD6D3", "md") + W(HOTLINE, 30, sx0 + 136, sy0 + sh - 124, NGO, "xb")
    s += W("antamfoods.com", 16, sx0 + 136, sy0 + sh - 96, KEM, "md")
    s += W("Mỗi mẻ bánh, một lời cam kết", 18, sx0 + sw / 2, sy0 + sh - 40, KEM, "xb", "middle")
    s += f'<rect x="{sx0}" y="{sy0}" width="{sw}" height="{sh}" fill="url(#cy{u})" opacity=".35"/></g>'
    s += thong_so("Standee cuốn 80 × 200 cm · in bạt PP · vùng chữ quan trọng trong 80 cm trên cùng · QR dẫn về Zalo/antamfoods.com", w, h)
    return S(w, h, s, "Standee")


# ───────────────────────────── 11. HỒ SƠ NĂNG LỰC
def _trang(x, y, pw, ph, rot, body, u, cid):
    return (f'<g transform="rotate({rot} {x + pw / 2} {y + ph / 2})"><g filter="url(#sd{u})"><rect x="{x}" y="{y}" width="{pw}" height="{ph}" fill="{TRANG}"/></g>'
            f'<clipPath id="tr{cid}{u}"><rect x="{x}" y="{y}" width="{pw}" height="{ph}"/></clipPath><g clip-path="url(#tr{cid}{u})">{body}</g></g>')


def ho_so_nang_luc():
    u = "hs"; w, h = 1200, 760
    s = nen(w, h, u)
    pw, ph = 330, 467
    # trang 3 – sản phẩm & liên hệ
    x, y = 800, 140
    b = f'<rect x="{x}" y="{y}" width="{pw}" height="64" fill="{DO}"/>' + W("SẢN PHẨM & LIÊN HỆ", 16, x + 22, y + 40, KEM, "xb", track=.12)
    b += f'<image href="{anh("xuong-gia-banh-2")}" x="{x}" y="{y + 64}" width="{pw}" height="120" preserveAspectRatio="xMidYMid slice"/>'
    for i, (k, v) in enumerate((("Tortilla", "22 · 25 · 28 · 31 cm"), ("Đóng gói", "15 chiếc / túi"), ("Loại", "Tươi · Nướng · Nguyên cám"), ("Vỏ kebab", "Vàng · Mè đen · Mè trắng · Than tre"))):
        yy = y + 214 + i * 34
        b += f'<rect x="{x + 18}" y="{yy - 22}" width="{pw - 36}" height="30" fill="{"#F7E6D3" if i % 2 == 0 else TRANG}"/>' + W(k, 12, x + 28, yy - 2, DO, "xb") + W(v, 12, x + 110, yy - 2, MUC, "md")
    b += f'<rect x="{x}" y="{y + ph - 110}" width="{pw}" height="110" fill="{MUC}"/>' + W(HOTLINE, 24, x + 22, y + ph - 62, NGO, "xb")
    b += W("antamfoods.com · Zalo", 13, x + 22, y + ph - 38, KEM, "md") + W("[Cần điền: địa chỉ xưởng]", 11, x + 22, y + ph - 18, "#cbb", "md")
    s += _trang(x, y, pw, ph, 5, b, u, "c")
    # trang 2 – về An Tâm
    x, y = 470, 120
    b = W("VỀ AN TÂM", 13, x + 24, y + 42, DO, "xb", track=.2) + W("Nhà sản xuất vỏ bánh", 24, x + 24, y + 76, MUC, "xb") + W("tortilla, taco & kebab", 24, x + 24, y + 104, DO, "xb")
    b += f'<image href="{anh("xuong-nguoi-lam")}" x="{x + 24}" y="{y + 122}" width="{pw - 48}" height="150" preserveAspectRatio="xMidYMid slice"/>'
    b += W("Ảnh thật tại xưởng An Tâm", 10, x + 24, y + 288, "#8a7a74", "md")
    for i in range(4):
        b += f'<rect x="{x + 24}" y="{y + 302 + i * 14}" width="{pw - 48 - (60 if i == 3 else 0)}" height="6" rx="3" fill="#E9DFD2"/>'
    for i, (big, small) in enumerate((("[ ]", "chiếc/ngày"), ("[ ]", "dây chuyền"), ("[ ]", "đối tác"))):
        xx = x + 24 + i * 96
        b += f'<rect x="{xx}" y="{y + 372}" width="88" height="70" rx="6" fill="{DO}"/>' + W(big, 22, xx + 44, y + 408, KEM, "xb", "middle") + W(small, 11, xx + 44, y + 430, "#FFD6D3", "md", "middle")
    s += _trang(x, y, pw, ph, -2, b, u, "b")
    # bìa
    x, y = 100, 150
    b = f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" fill="{DO}"/>'
    b += f'<svg x="{x}" y="{y}" width="{pw}" height="{ph}" viewBox="0 0 {pw} {ph}" preserveAspectRatio="none">{B.nen_van(pw, ph).split(">", 1)[1].rsplit("</svg>", 1)[0]}</svg>'
    b += f'<g opacity=".9">{mark(x + pw - 40, y + ph - 70, 120, KEM)}</g>'
    b += fit(V.logo_ngang(KEM, KEM), x + 130, y + 56, w=210)
    b += f'<rect x="{x + 24}" y="{y + 150}" width="{pw - 48}" height="150" fill="{KEM}"/>'
    b += W("HỒ SƠ NĂNG LỰC", 13, x + 44, y + 186, DO, "xb", track=.24) + W("Ẩm Thực An Tâm", 30, x + 44, y + 226, MUC, "xb")
    b += W("Vỏ bánh Tortilla · Taco · Doner Kebab", 13, x + 44, y + 254, DO, "md") + W("2026", 13, x + 44, y + 282, "#8a7a74", "xb")
    s += _trang(x, y, pw, ph, -6, b, u, "a")
    s += nhan("BÌA", 270, 700) + nhan("GIỚI THIỆU · NĂNG LỰC", 635, 700) + nhan("SẢN PHẨM · LIÊN HỆ", 965, 700)
    s += thong_so("Hồ sơ năng lực A4 · 8–12 trang · giấy couché mờ 150 gsm, bìa 250 gsm cán mờ · số liệu thật điền vào ô [ ] trước khi in", w, h)
    return S(w, h, s, "Hồ sơ năng lực")


MOI = [
    ("ly-giay", "Ly giấy", ly_giay), ("ao-thun", "Áo thun nhân viên", ao_thun), ("ao-van-phong", "Áo văn phòng", ao_polo),
    ("tap-de", "Tạp dề", tap_de), ("mu-bep", "Mũ bếp", mu_bep), ("quay-kiosk", "Quầy kiosk", kiosk),
    ("xe-giao-hang", "Xe giao hàng", xe_giao_hang), ("hop-taco", "Hộp taco", hop_taco), ("tui-tortilla", "Túi bánh tortilla", tui_tortilla),
    ("standee", "Standee", standee), ("ho-so-nang-luc", "Hồ sơ năng lực", ho_so_nang_luc),
]

if __name__ == "__main__":
    import sys
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for slug, _, f in MOI:
        open(os.path.join(out, slug + ".svg"), "w").write(f())
    print("ok")

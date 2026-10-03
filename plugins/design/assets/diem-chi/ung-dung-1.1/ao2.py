"""Vẽ lại đồng phục An Tâm (Điểm Chỉ 1.1): áo thun nhân viên, áo polo văn phòng, tạp dề – dáng mềm, nếp vải, đường may."""
import ud2 as U2

V = U2.V
DO, DO2, KEM, MUC, NGO, TRANG = U2.DO, U2.DO2, U2.KEM, U2.MUC, U2.NGO, U2.TRANG
W, fit, mark, nen, bong, nhan, thong_so, S = U2.W, U2.fit, U2.mark, U2.nen, U2.bong, U2.nhan, U2.thong_so, U2.S


def _defs(u):
    return (f'<defs><filter id="mo{u}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>'
            f'<filter id="mo2{u}"><feGaussianBlur stdDeviation="3"/></filter>'
            f'<radialGradient id="sang{u}" cx=".42" cy=".3" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="#000" stop-opacity=".16"/></radialGradient></defs>')


def _P(cx, cy, s, pts):
    """pts: chuỗi lệnh path với toạ độ tương đối (x,y) -> tuyệt đối."""
    out = []
    for tok in pts.split():
        if "," in tok:
            x, y = tok.split(","); out.append(f"{cx + float(x) * s:.1f},{cy + float(y) * s:.1f}")
        else:
            out.append(tok)
    return " ".join(out)


TEE = ("M -38,-152 C -22,-118 22,-118 38,-152 L 98,-140 C 122,-132 142,-116 160,-92 L 134,-32 C 122,-38 110,-45 98,-52 "
       "C 101,0 103,100 104,152 C 40,161 -40,161 -104,152 C -103,100 -101,0 -98,-52 C -110,-45 -122,-38 -134,-32 L -160,-92 "
       "C -142,-116 -122,-132 -98,-140 Z")
TEE_BACK = TEE.replace("C -22,-118 22,-118 38,-152", "C -20,-142 20,-142 38,-152")


def _than(cx, cy, s, fill, u, cid, d_rel, sleeve_band=None):
    d = _P(cx, cy, s, d_rel)
    o = f'<g filter="url(#sd{u})"><path d="{d}" fill="{fill}"/></g>'
    o += f'<clipPath id="k{cid}{u}"><path d="{d}"/></clipPath><g clip-path="url(#k{cid}{u})">'
    # nếp vải mềm
    for x0, y0, x1, y1, op in ((-70, -40, -55, 150, .10), (60, -30, 48, 150, .09), (-15, 40, 5, 150, .07), (-140, -80, -118, -40, .1), (140, -80, 118, -40, .1)):
        o += f'<path d="M{cx + x0 * s:.1f},{cy + y0 * s:.1f} Q{cx + (x0 + x1) / 2 * s + 10 * s:.1f},{cy + (y0 + y1) / 2 * s:.1f} {cx + x1 * s:.1f},{cy + y1 * s:.1f}" stroke="#000" stroke-opacity="{op}" stroke-width="{14 * s:.1f}" fill="none" filter="url(#mo{u})"/>'
        o += f'<path d="M{cx + (x0 + 9) * s:.1f},{cy + y0 * s:.1f} Q{cx + ((x0 + x1) / 2 + 19) * s:.1f},{cy + (y0 + y1) / 2 * s:.1f} {cx + (x1 + 9) * s:.1f},{cy + y1 * s:.1f}" stroke="#fff" stroke-opacity="{op * .9}" stroke-width="{8 * s:.1f}" fill="none" filter="url(#mo{u})"/>'
    o += f'<rect x="{cx - 170 * s}" y="{cy - 170 * s}" width="{340 * s}" height="{340 * s}" fill="url(#sang{u})"/>'
    # đường may vai, gấu, tay
    o += f'<path d="{_P(cx, cy, s, "M -98,-140 C -100,-110 -99,-80 -98,-52 M 98,-140 C 100,-110 99,-80 98,-52")}" stroke="#000" stroke-opacity=".12" stroke-width="{1.6 * s}" fill="none"/>'
    o += f'<path d="{_P(cx, cy, s, "M -104,140 C -40,149 40,149 104,140")}" stroke="#000" stroke-opacity=".14" stroke-width="{1.4 * s}" fill="none" stroke-dasharray="{4 * s} {3 * s}"/>'
    sb = sleeve_band or "#000"
    so = 1 if sleeve_band else .14
    o += f'<path d="{_P(cx, cy, s, "M -149,-58 L -126,-44 M 149,-58 L 126,-44")}" stroke="{sb}" stroke-opacity="{so}" stroke-width="{(11 if sleeve_band else 1.4) * s}" fill="none"/>'
    o += "</g>"
    return o


def _co_tron(cx, cy, s, fill, back=False):
    rel = "M -38,-152 C -20,-142 20,-142 38,-152" if back else "M -38,-152 C -22,-118 22,-118 38,-152"
    o = f'<path d="{_P(cx, cy, s, rel)}" fill="none" stroke="{fill}" stroke-width="{9 * s}" stroke-linecap="round"/>'
    o += f'<path d="{_P(cx, cy, s, rel)}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="{9 * s}" stroke-linecap="round" stroke-dasharray="{1.2 * s} {2.2 * s}"/>'
    if not back:
        o += f'<path d="{_P(cx, cy, s, "M -32,-150 C -16,-140 16,-140 32,-150 C 18,-146 -18,-146 -32,-150 Z")}" fill="#000" opacity=".35"/>'
    return o


def ao_thun():
    u = "at2"; w, h = 960, 660
    s = nen(w, h, u) + _defs(u)
    s += bong(250, 530, 150, 14, u) + bong(710, 530, 150, 14, u)
    s += _than(250, 320, 1.3, DO, u, "f", TEE) + _co_tron(250, 320, 1.3, DO2)
    s += _than(710, 320, 1.3, DO, u, "b", TEE_BACK) + _co_tron(710, 320, 1.3, DO2, back=True)
    # trước: ngực trái (bên phải người xem) + tay áo
    s += mark(250 + 66, 320 - 98, 22, KEM) + W("An Tâm", 17, 250 + 66, 320 - 58, KEM, "xb", "middle")
    s += f'<g transform="rotate(-58 {250 - 176} {320 - 96})">' + W("AN TÂM", 11, 250 - 176, 320 - 92, KEM, "xb", "middle", .25) + "</g>"
    # sau: logo đứng + câu thương hiệu + nhãn bộ phận
    s += W("ẨM THỰC AN TÂM", 11, 710, 320 - 160, KEM, "xb", "middle", .3) if False else ""
    s += fit(V.logo_dung(KEM, KEM), 710, 320 - 50, w=170)
    s += W("Mỗi mẻ bánh, một lời cam kết", 17, 710, 320 + 74, KEM, "xb", "middle")
    s += f'<rect x="{710 - 74}" y="{320 + 98}" width="148" height="30" rx="15" fill="{KEM}"/>' + W("NHÂN VIÊN", 13, 710, 320 + 118, DO, "xb", "middle", .25)
    s += nhan("MẶT TRƯỚC", 250, 600) + nhan("MẶT SAU", 710, 600)
    s += thong_so("Áo thun cotton 65/35 Đỏ An Tâm · cổ bo Đỏ đậm · in lụa Kem: ngực trái biểu tượng 8 cm, tay trái AN TÂM, lưng logo đứng 24 cm + nhãn bộ phận", w, h)
    return S(w, h, s, "Áo thun nhân viên")


POLO = TEE.replace("M -38,-152 C -22,-118 22,-118 38,-152", "M -38,-152 C -20,-142 20,-142 38,-152").replace(
    "L 98,-140 C 122,-132 142,-116 160,-92 L 134,-32 C 122,-38 110,-45 98,-52", "L 98,-140 C 118,-132 134,-118 146,-100 L 124,-50 C 116,-54 106,-58 98,-62").replace(
    "C -110,-45 -122,-38 -134,-32 L -160,-92 C -142,-116 -122,-132 -98,-140", "C -106,-58 -116,-54 -124,-50 L -146,-100 C -134,-118 -118,-132 -98,-140").replace(
    "C 101,0 103,100 104,152", "C 101,0 103,100 104,148").replace("C 40,161 -40,161 -104,152 C -103,100", "C 40,157 -40,157 -104,148 C -103,100")


def _polo(cx, cy, s, fill, trim, u, cid, logo_c, back=False):
    o = _than(cx, cy, s, fill, u, cid, POLO.replace("M -149,-58", "M -136,-74"), sleeve_band=None)
    # viền tay áo màu trim
    o += f'<path d="{_P(cx, cy, s, "M -146,-100 L -124,-50")}" stroke="{trim}" stroke-width="{9 * s}" stroke-linecap="butt"/>'
    o += f'<path d="{_P(cx, cy, s, "M 146,-100 L 124,-50")}" stroke="{trim}" stroke-width="{9 * s}"/>'
    # chân cổ (đứng sau gáy)
    o += f'<path d="{_P(cx, cy, s, "M -40,-150 C -20,-160 20,-160 40,-150")}" fill="none" stroke="{trim}" stroke-width="{9 * s}" stroke-linecap="round"/>'
    if back:
        o += f'<path d="{_P(cx, cy, s, "M -44,-150 C -20,-138 20,-138 44,-150 L 40,-128 C 18,-118 -18,-118 -40,-128 Z")}" fill="{trim}"/>'
        return o
    # nẹp áo + cúc
    o += f'<path d="{_P(cx, cy, s, "M -11,-140 L 11,-140 L 11,-62 L -11,-62 Z")}" fill="#000" opacity=".06"/>'
    o += f'<path d="{_P(cx, cy, s, "M -11,-140 L -11,-62 L 11,-62 L 11,-140")}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="{1.4 * s}"/>'
    for k in range(3):
        o += f'<circle cx="{cx}" cy="{cy + (-122 + k * 24) * s:.1f}" r="{3.4 * s}" fill="{trim}" stroke="#000" stroke-opacity=".2" stroke-width="{.8 * s}"/>'
    # hai vạt cổ bẻ
    for sg in (-1, 1):
        flap = f"M {sg * 3},-140 C {sg * 16},-148 {sg * 30},-154 {sg * 42},-152 C {sg * 44},-138 {sg * 42},-122 {sg * 34},-104 C {sg * 24},-112 {sg * 12},-124 {sg * 3},-140 Z"
        o += f'<g filter="url(#sd{u})"><path d="{_P(cx, cy, s, flap)}" fill="{trim}"/></g>'
        o += f'<path d="{_P(cx, cy, s, flap)}" fill="#fff" opacity=".08"/>'
    o += fit(V.logo_ngang(logo_c, MUC if logo_c == DO else KEM), cx + 56 * s, cy - 84 * s, w=70 * s)
    return o


def ao_polo():
    u = "ap2"; w, h = 980, 660
    s = nen(w, h, u) + _defs(u)
    for x in (180, 490, 800):
        s += bong(x, 520, 120, 12, u)
    s += _polo(180, 330, 1.12, TRANG, DO, u, "a", DO)
    s += _polo(490, 330, 1.12, MUC, DO, u, "b", KEM)
    s += _polo(800, 330, 1.12, TRANG, DO, u, "c", DO, back=True)
    s += W("ẨM THỰC AN TÂM", 12, 800, 330 - 104, DO, "xb", "middle", .3)
    s += mark(800, 330 + 60, 26, DO) if False else ""
    s += nhan("VĂN PHÒNG – NỀN KEM", 180, 600) + nhan("QUẢN LÝ / BÁN HÀNG – NỀN MỰC", 490, 600) + nhan("MẶT SAU", 800, 600)
    s += thong_so("Polo cá sấu cotton · nền Kem hoặc Mực · cổ, chân cổ, viền tay Đỏ An Tâm · thêu logo ngang 7 cm ngực trái · dưới cổ sau ẨM THỰC AN TÂM", w, h)
    return S(w, h, s, "Áo văn phòng")


def _yem(cx, cy, s, fill, ink, u, cid):
    body = ("M -54,-206 L 54,-206 C 56,-150 76,-92 118,-66 L 126,214 C 126,224 120,228 110,228 L -110,228 C -120,228 -126,224 -126,214 "
            "L -118,-66 C -76,-92 -56,-150 -54,-206 Z")
    d = _P(cx, cy, s, body)
    o = f'<path d="{_P(cx, cy, s, "M -48,-204 C -50,-300 50,-300 48,-204")}" fill="none" stroke="{ink}" stroke-width="{8 * s}"/>'
    # dây buộc eo buông xuống
    for sg in (-1, 1):
        o += f'<path d="{_P(cx, cy, s, f"M {sg * 118},-64 C {sg * 138},-62 {sg * 146},-44 {sg * 140},0 C {sg * 136},40 {sg * 146},70 {sg * 142},96")}" fill="none" stroke="{ink}" stroke-width="{8 * s}" stroke-linecap="round"/>'
    o += f'<g filter="url(#sd{u})"><path d="{d}" fill="{fill}"/></g>'
    o += f'<clipPath id="y{cid}{u}"><path d="{d}"/></clipPath><g clip-path="url(#y{cid}{u})">'
    for x0, op in ((-60, .1), (40, .09), (90, .08)):
        o += f'<path d="M{cx + x0 * s},{cy - 60 * s} Q{cx + (x0 + 12) * s},{cy + 80 * s} {cx + (x0 - 4) * s},{cy + 230 * s}" stroke="#000" stroke-opacity="{op}" stroke-width="{16 * s}" fill="none" filter="url(#mo{u})"/>'
    o += f'<rect x="{cx - 140 * s}" y="{cy - 220 * s}" width="{280 * s}" height="{460 * s}" fill="url(#sang{u})"/>'
    o += f'<path d="{_P(cx, cy, s, body)}" fill="none" stroke="{ink}" stroke-opacity=".55" stroke-width="{1.6 * s}" stroke-dasharray="{5 * s} {4 * s}" transform="translate({cx} {cy}) scale(.955) translate({-cx} {-cy})"/>'
    o += "</g>"
    o += mark(cx, cy - 140 * s, 30 * s, ink)
    o += W("An Tâm", 32 * s, cx, cy - 64 * s, ink, "xb", "middle")
    o += W("Mỗi mẻ bánh, một lời cam kết", 13 * s, cx, cy + 6 * s, ink, "xb", "middle")
    # túi
    po = "M -92,62 L 92,62 L 92,150 C 92,158 86,162 80,162 L -80,162 C -86,162 -92,158 -92,150 Z"
    o += f'<path d="{_P(cx, cy, s, po)}" fill="#000" opacity=".08"/>'
    o += f'<path d="{_P(cx, cy, s, po)}" fill="none" stroke="{ink}" stroke-opacity=".7" stroke-width="{1.6 * s}" stroke-dasharray="{5 * s} {4 * s}"/>'
    o += f'<path d="{_P(cx, cy, s, "M 0,62 L 0,162 M -28,62 L -28,162")}" stroke="{ink}" stroke-opacity=".7" stroke-width="{1.6 * s}" stroke-dasharray="{5 * s} {4 * s}"/>'
    o += f'<path d="{_P(cx, cy, s, "M -92,62 L 92,62")}" stroke="{ink}" stroke-width="{3 * s}"/>'
    return o


def _ngang_eo(cx, cy, s, fill, ink, u):
    """Tạp dề ngang eo (bán hàng / thu ngân)."""
    body = "M -130,-40 L 130,-40 L 136,110 C 136,120 128,124 120,124 L -120,124 C -128,124 -136,120 -136,110 Z"
    d = _P(cx, cy, s, body)
    o = f'<path d="{_P(cx, cy, s, "M -130,-36 C -152,-34 -160,-16 -156,20 C -152,52 -162,74 -158,96 M 130,-36 C 152,-34 160,-16 156,20 C 152,52 162,74 158,96")}" fill="none" stroke="{ink}" stroke-width="{8 * s}" stroke-linecap="round"/>'
    o += f'<g filter="url(#sd{u})"><path d="{d}" fill="{fill}"/></g>'
    o += f'<path d="{_P(cx, cy, s, "M -130,-40 L 130,-40 L 130,-24 L -130,-24 Z")}" fill="{ink}"/>'
    o += f'<clipPath id="ne{u}"><path d="{d}"/></clipPath><g clip-path="url(#ne{u})"><rect x="{cx - 140 * s}" y="{cy - 50 * s}" width="{280 * s}" height="{180 * s}" fill="url(#sang{u})"/></g>'
    o += fit(V.logo_ngang(ink, ink), cx, cy + 22 * s, w=150 * s)
    po = "M -100,62 L 100,62 L 100,108 L -100,108 Z"
    o += f'<path d="{_P(cx, cy, s, po)}" fill="#000" opacity=".1"/><path d="{_P(cx, cy, s, po + " M -34,62 L -34,108 M 34,62 L 34,108")}" fill="none" stroke="{ink}" stroke-opacity=".7" stroke-width="{1.6 * s}" stroke-dasharray="{5 * s} {4 * s}"/>'
    return o


def tap_de():
    u = "td2"; w, h = 980, 680
    s = nen(w, h, u) + _defs(u)
    s += bong(220, 586, 140, 14, u) + bong(530, 586, 130, 14, u) + bong(830, 520, 110, 12, u)
    s += _yem(220, 340, 1.05, DO, KEM, u, "a")
    s += _yem(530, 340, 1.05, MUC, KEM, u, "b")
    s += _ngang_eo(830, 400, .82, DO, KEM, u)
    s += nhan("BẾP / QUẦY – ĐỎ", 220, 630) + nhan("XƯỞNG – MỰC", 530, 630) + nhan("BÁN HÀNG – NGANG EO", 830, 630)
    s += thong_so("Kaki chống thấm · in lụa Kem · dây cổ chỉnh được, dây eo dài · túi 3 ngăn (bút, sổ, điện thoại) · đường may Kem lộ chỉ", w, h)
    return S(w, h, s, "Tạp dề")

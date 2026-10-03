"""Đồng phục An Tâm – 3 hướng ý tưởng mới (áo thun nhân viên, áo văn phòng, tạp dề)."""
import math

import ao2 as A
import build_van as B

V = A.V
DO, DO2, KEM, MUC, NGO, TRANG = A.DO, A.DO2, A.KEM, A.MUC, A.NGO, A.TRANG
SON = V.SON
KRAFT, KRAFT2 = "#C9A57A", "#A9835A"
W, fit, mark, nen, bong, nhan, S, _P = A.W, A.fit, A.mark, A.nen, A.bong, A.nhan, A.S, A._P

APRON = ("M -54,-206 L 54,-206 C 56,-150 76,-92 118,-66 L 126,214 C 126,224 120,228 110,228 L -110,228 C -120,228 -126,224 -126,214 "
         "L -118,-66 C -76,-92 -56,-150 -54,-206 Z")


def van_nen(x, y, w, h, color, step=13, sw=4.5, ph=0.0):
    """Đường vân chảy (lấy từ hoạ tiết nền) vẽ trực tiếp, không nền."""
    out = []
    for i in range(-8, int(h / step) + 10):
        y0 = y + i * step; pts = []
        for xx in range(int(x) - 20, int(x + w) + 30, 14):
            pts.append((xx, y0 + 40 * math.sin((xx - x) / 180 + i * .05 + ph) + 18 * math.sin((xx - x) / 60 + i * .12)))
        out.append('<path d="M' + " L".join(f"{a:.0f},{b:.1f}" for a, b in pts) + f'" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')
    return "".join(out)


def garm(cx, cy, s, fill, u, cid, rel, deco="", seams=True):
    d = _P(cx, cy, s, rel)
    o = f'<g filter="url(#sd{u})"><path d="{d}" fill="{fill}"/></g>'
    o += f'<clipPath id="g{cid}{u}"><path d="{d}"/></clipPath><g clip-path="url(#g{cid}{u})">{deco}'
    for x0, y0, x1, y1, op in ((-70, -40, -55, 230, .10), (60, -30, 48, 230, .09), (-15, 40, 5, 230, .07), (-140, -80, -118, -40, .1), (140, -80, 118, -40, .1)):
        o += f'<path d="M{cx + x0 * s:.1f},{cy + y0 * s:.1f} Q{cx + ((x0 + x1) / 2 + 10) * s:.1f},{cy + (y0 + y1) / 2 * s:.1f} {cx + x1 * s:.1f},{cy + y1 * s:.1f}" stroke="#000" stroke-opacity="{op}" stroke-width="{14 * s:.1f}" fill="none" filter="url(#mo{u})"/>'
    o += f'<rect x="{cx - 170 * s}" y="{cy - 240 * s}" width="{340 * s}" height="{480 * s}" fill="url(#sang{u})"/>'
    if seams:
        o += f'<path d="{_P(cx, cy, s, "M -98,-140 C -100,-110 -99,-80 -98,-52 M 98,-140 C 100,-110 99,-80 98,-52")}" stroke="#000" stroke-opacity=".12" stroke-width="{1.6 * s}" fill="none"/>'
    o += "</g>"
    return o


def tie(cx, cy, s, ink):
    o = f'<path d="{_P(cx, cy, s, "M -48,-204 C -50,-300 50,-300 48,-204")}" fill="none" stroke="{ink}" stroke-width="{8 * s}"/>'
    for sg in (-1, 1):
        o += f'<path d="{_P(cx, cy, s, f"M {sg * 118},-64 C {sg * 138},-62 {sg * 146},-44 {sg * 140},0 C {sg * 136},40 {sg * 146},70 {sg * 142},96")}" fill="none" stroke="{ink}" stroke-width="{8 * s}" stroke-linecap="round"/>'
    return o


def stitch(cx, cy, s, ink, rel=APRON):
    return f'<path d="{_P(cx, cy, s, rel)}" fill="none" stroke="{ink}" stroke-opacity=".6" stroke-width="{1.6 * s}" stroke-dasharray="{5 * s} {4 * s}" transform="translate({cx} {cy}) scale(.955) translate({-cx} {-cy})"/>'


def collar_polo(cx, cy, s, trim, u):
    o = f'<path d="{_P(cx, cy, s, "M -40,-150 C -20,-160 20,-160 40,-150")}" fill="none" stroke="{trim}" stroke-width="{9 * s}" stroke-linecap="round"/>'
    o += f'<path d="{_P(cx, cy, s, "M -11,-140 L -11,-62 L 11,-62 L 11,-140")}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="{1.4 * s}"/>'
    for k in range(3):
        o += f'<circle cx="{cx}" cy="{cy + (-122 + k * 24) * s:.1f}" r="{3.4 * s}" fill="{trim}"/>'
    for sg in (-1, 1):
        f = f"M {sg * 3},-140 C {sg * 16},-148 {sg * 30},-154 {sg * 42},-152 C {sg * 44},-138 {sg * 42},-122 {sg * 34},-104 C {sg * 24},-112 {sg * 12},-124 {sg * 3},-140 Z"
        o += f'<g filter="url(#sd{u})"><path d="{_P(cx, cy, s, f)}" fill="{trim}"/></g>'
    return o


def bang(title, sub, items, u, w=1080, h=560):
    s = nen(w, h, u) + A._defs(u)
    for x in (190, 540, 890):
        s += bong(x, 470, 120, 12, u)
    s += items
    s += W(title, 26, 40, 50, DO, "xb")
    words, lines, cur = sub.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) > 62:
            lines.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    lines.append(cur)
    for i, ln in enumerate(lines[:3]):
        s += W(ln, 14, 40, 76 + i * 19, "#6b5a55", "md")
    s += nhan("ÁO THUN NHÂN VIÊN", 190, 530) + nhan("ÁO VĂN PHÒNG", 540, 530) + nhan("TẠP DỀ", 890, 530)
    return S(w, h, s, title)


# ───────── Hướng 1 · DẢI VÂN: nền kem, một dải đường vân đỏ chạy chéo cơ thể
def huong_1():
    u = "h1"; ts = .95
    band = lambda cx, cy, ang, wd: (f'<clipPath id="bd{u}"><rect x="{cx - 260}" y="{cy - wd / 2}" width="520" height="{wd}"/></clipPath>'
                                     f'<g transform="rotate({ang} {cx} {cy})"><g clip-path="url(#bd{u})"><rect x="{cx - 260}" y="{cy - wd / 2}" width="520" height="{wd}" fill="{DO}"/>'
                                     f'{van_nen(cx - 260, cy - wd / 2, 520, wd, SON, 11, 3.6)}</g></g>')
    # áo thun kem, dải vân chéo từ vai phải xuống hông trái
    t = garm(190, 290, ts, KEM, u, "t", A.TEE, band(190, 330, -28, 60))
    t += A._co_tron(190, 290, ts, DO)
    t += mark(190 + 52, 290 - 92, 17, DO) + W("An Tâm", 13, 190 + 52, 290 - 62, DO, "xb", "middle")
    # polo trắng: tay áo là dải vân, logo ngực
    sl = lambda: "".join(f'<g>{van_nen(540 + sg * 150 - 40, 160, 80, 120, SON, 10, 3.4)}</g>' for sg in (-1, 1))
    slv = "M -98,-140 C -118,-132 -134,-118 -146,-100 L -124,-50 C -116,-54 -106,-58 -98,-62 Z M 98,-140 C 118,-132 134,-118 146,-100 L 124,-50 C 116,-54 106,-58 98,-62 Z"
    pdeco = (f'<clipPath id="sl{u}"><path d="{_P(540, 290, ts, slv)}"/></clipPath><g clip-path="url(#sl{u})"><rect x="360" y="140" width="360" height="200" fill="{DO}"/>'
             + van_nen(360, 140, 360, 200, SON, 10, 3.2) + '</g>'
             + f'<rect x="{540 - 6}" y="{290 - 60 * ts}" width="12" height="{220 * ts}" fill="{DO}"/>')
    p = garm(540, 290, ts, TRANG, u, "p", A.POLO, pdeco) + collar_polo(540, 290, ts, DO, u)
    p += fit(V.logo_ngang(), 540 + 52 * ts, 290 - 82 * ts, w=66 * ts)
    # tạp dề kem, gấu là dải vân + túi đỏ
    ad = (f'<clipPath id="ab{u}"><rect x="{890 - 140}" y="{300 + 150 * .9}" width="280" height="140"/></clipPath><g clip-path="url(#ab{u})">'
          f'<rect x="{890 - 140}" y="{300 + 150 * .9}" width="280" height="140" fill="{DO}"/>' + van_nen(750, 300 + 150 * .9, 280, 140, SON, 11, 3.6) + '</g>')
    a = tie(890, 300, .9, DO) + garm(890, 300, .9, KEM, u, "a", APRON, ad, seams=False) + stitch(890, 300, .9, DO)
    a += mark(890, 300 - 130 * .9, 28 * .9, DO) + W("An Tâm", 28 * .9, 890, 300 - 62 * .9, DO, "xb", "middle")
    a += W("Mỗi mẻ bánh, một lời cam kết", 11.5, 890, 300 + 6 * .9, MUC, "xb", "middle")
    return bang("Hướng 1 · Dải vân", "Nền kem sạch sẽ; một dải đường vân đỏ chạy chéo người, viền tay, gấu tạp dề – như vệt mực son quệt qua.", t + p + a, u)


# ───────── Hướng 2 · DẤU TAY LỚN: một dấu vân tay rất lớn, cắt mép, in tông-trên-tông
def huong_2():
    u = "h2"; ts = .95
    big = lambda cx, cy, r, c, op: f'<g opacity="{op}">{mark(cx, cy, r, c)}</g>'
    t = garm(190, 290, ts, DO, u, "t", A.TEE, big(190 + 70, 290 + 60, 150, DO2, 1)) + A._co_tron(190, 290, ts, DO2)
    t += W("An Tâm", 22, 190 - 40, 290 - 70, KEM, "xb", "middle") + W("ẨM THỰC", 9, 190 - 40, 290 - 94, KEM, "xb", "middle", .3)
    p = garm(540, 290, ts, MUC, u, "p", A.POLO, big(540 - 80, 290 + 90, 160, "#3a2a27", 1)) + collar_polo(540, 290, ts, "#3a2a27", u)
    p += mark(540 + 52 * ts, 290 - 84 * ts, 13, DO) + W("An Tâm", 11, 540 + 52 * ts, 290 - 58 * ts, KEM, "xb", "middle")
    a = tie(890, 300, .9, MUC) + garm(890, 300, .9, MUC, u, "a", APRON, big(890 + 70, 300 + 150, 170, "#3a2a27", 1), seams=False) + stitch(890, 300, .9, DO)
    a += W("An Tâm", 26, 890, 300 - 120, KEM, "xb", "middle") + mark(890, 300 - 170, 14, DO)
    a += W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 - 92, KEM, "md", "middle")
    return bang("Hướng 2 · Dấu tay lớn", "Một dấu vân tay rất lớn, cắt mép, in cùng tông với nền (đỏ trên đỏ, mực trên mực) – sang, kín đáo, nhìn gần mới thấy.", t + p + a, u)


# ───────── Hướng 3 · THỦ CÔNG: kraft, áo đầu bếp, con dấu son
def huong_3():
    u = "h3"; ts = .95
    # áo thun màu kem, nửa dưới đỏ, đường chia lượn sóng như ly giấy
    wave = " ".join(f"L{190 - 170 + i * 340 / 24:.1f},{290 + 40 + 10 * math.sin(i / 2.2):.1f}" for i in range(25))
    td = f'<path d="M{190 - 170},{290 + 260} {wave} L{190 + 170},{290 + 260} Z" fill="{DO}"/>'
    t = garm(190, 290, ts, KEM, u, "t", A.TEE, td) + A._co_tron(190, 290, ts, DO)
    t += fit(V.logo_ngang(), 190, 290 - 50, w=150)
    t += W("Mỗi mẻ bánh, một lời cam kết", 12, 190, 290 + 100, KEM, "xb", "middle")
    # áo văn phòng: sơ mi kiểu áo đầu bếp hai hàng cúc (kem, viền đỏ)
    CHEF = A.POLO
    pd = f'<path d="M{540 - 10},{290 - 150} L{540 + 70},{290 - 150} L{540 + 70},{290 + 160} L{540 - 10},{290 + 160} Z" fill="#000" opacity=".04"/>'
    p = garm(540, 290, ts, TRANG, u, "p", CHEF, pd)
    p += f'<path d="{_P(540, 290, ts, "M -40,-150 C -20,-160 20,-160 40,-150 L 40,-134 C 20,-142 -20,-142 -40,-134 Z")}" fill="{DO}"/>'
    p += f'<path d="{_P(540, 290, ts, "M -10,-136 L -10,148")}" stroke="{DO}" stroke-width="{3 * ts}"/>'
    for k in range(4):
        for dx in (8, 44):
            p += f'<circle cx="{540 + dx * ts:.1f}" cy="{290 + (-110 + k * 42) * ts:.1f}" r="{4.6 * ts}" fill="{DO}"/>'
    p += f'<path d="{_P(540, 290, ts, "M -146,-100 L -124,-50 M 146,-100 L 124,-50")}" stroke="{DO}" stroke-width="{8 * ts}"/>'
    p += mark(540 - 52 * ts, 290 - 84 * ts, 15, DO) + W("An Tâm", 12, 540 - 52 * ts, 290 - 56 * ts, DO, "xb", "middle")
    # tạp dề vải bố kraft, dây da đỏ, con dấu tròn
    a = tie(890, 300, .9, DO2) + garm(890, 300, .9, KRAFT, u, "a", APRON, "", seams=False) + stitch(890, 300, .9, KEM)
    a += f'<rect x="{890 - 112 * .9}" y="{300 - 70 * .9}" width="{224 * .9}" height="9" fill="{DO2}"/>'
    a += f'<g transform="rotate(-8 890 {300 - 118 * .9})">' + fit(V.con_dau(DO, KEM), 890, 300 - 118 * .9, w=86) + "</g>"
    a += f'<rect x="{890 - 80}" y="{300 + 60}" width="160" height="80" rx="6" fill="{KRAFT2}" opacity=".6"/>'
    a += W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 + 104, KEM, "xb", "middle")
    return bang("Hướng 3 · Thủ công", "Ấm, thủ công: áo thun chia sóng đỏ–kem, áo văn phòng kiểu áo bếp hai hàng cúc, tạp dề vải bố kraft đóng con dấu son.", t + p + a, u)


HUONG = [("huong-1-dai-van", huong_1), ("huong-2-dau-tay-lon", huong_2), ("huong-3-thu-cong", huong_3)]


SLV = "M -98,-140 C -118,-132 -134,-118 -146,-100 L -124,-50 C -116,-54 -106,-58 -98,-62 Z M 98,-140 C 118,-132 134,-118 146,-100 L 124,-50 C 116,-54 106,-58 98,-62 Z"
SLV_TEE = "M -98,-140 C -122,-132 -142,-116 -160,-92 L -134,-32 C -122,-38 -110,-45 -98,-52 Z M 98,-140 C 122,-132 142,-116 160,-92 L 134,-32 C 122,-38 110,-45 98,-52 Z"


def _clip(cid, d, inner):
    return f'<clipPath id="{cid}"><path d="{d}"/></clipPath><g clip-path="url(#{cid})">{inner}</g>'


# ───────── Hướng 4 · KHỐI MÀU: thân Mực, cầu vai + tay Đỏ, đường cắt chéo – kiểu đồng phục thể thao
def huong_4():
    u = "h4"; ts = .95
    yoke = lambda cx, cy: f'<path d="M{cx - 200},{cy - 200} L{cx + 200},{cy - 200} L{cx + 200},{cy - 70} L{cx - 200},{cy - 30} Z" fill="{DO}"/>'
    td = yoke(190, 290) + _clip(f"s4t", _P(190, 290, ts, SLV_TEE), f'<rect x="0" y="0" width="400" height="600" fill="{DO}"/>')
    td += f'<path d="M{190 - 200},{290 - 26} L{190 + 200},{290 - 66}" stroke="{NGO}" stroke-width="5"/>'
    t = garm(190, 290, ts, MUC, u, "t", A.TEE, td) + A._co_tron(190, 290, ts, DO2)
    t += W("AN TÂM", 26, 190, 290 + 40, KEM, "xb", "middle", .12) + mark(190, 290 + 92, 22, DO)
    pd = f'<path d="M{540 - 200},{290 - 200} L{540 + 200},{290 - 200} L{540 + 200},{290 - 76} L{540 - 200},{290 - 40} Z" fill="{DO}"/>'
    pd += f'<path d="M{540 - 200},{290 - 36} L{540 + 200},{290 - 72}" stroke="{NGO}" stroke-width="4"/>'
    p = garm(540, 290, ts, MUC, u, "p", A.POLO, pd) + collar_polo(540, 290, ts, MUC, u)
    p += fit(V.logo_ngang(KEM, KEM), 540 + 54 * ts, 290 - 8 * ts, w=66 * ts)
    ad = f'<path d="M{890 - 160},{300 - 260} L{890 + 160},{300 - 260} L{890 + 160},{300 - 20} L{890 - 160},{300 + 30} Z" fill="{DO}"/>'
    ad += f'<path d="M{890 - 160},{300 + 34} L{890 + 160},{300 - 16}" stroke="{NGO}" stroke-width="5"/>'
    a = tie(890, 300, .9, MUC) + garm(890, 300, .9, MUC, u, "a", APRON, ad, seams=False) + stitch(890, 300, .9, KEM)
    a += mark(890, 300 - 130 * .9, 26, KEM) + W("An Tâm", 24, 890, 300 - 60, KEM, "xb", "middle")
    a += W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 + 100, KEM, "xb", "middle")
    return bang("Hướng 4 · Khối màu", "Thân màu Mực, cầu vai và tay Đỏ An Tâm, cắt chéo bằng một sọc vàng bánh – khoẻ, nhanh nhẹn như đồng phục thể thao, ít bám bẩn.", t + p + a, u)


# ───────── Hướng 5 · CHỮ LỚN: chữ AN TÂM rất lớn, cắt mép – kiểu streetwear
def huong_5():
    u = "h5"; ts = .95
    big = lambda cx, cy, size, c, rot=0: f'<g transform="rotate({rot} {cx} {cy})">' + W("AN TÂM", size, cx, cy, c, "xb", "middle", -.02) + "</g>"
    t = garm(190, 290, ts, KEM, u, "t", A.TEE, big(190, 290 + 120, 118, DO)) + A._co_tron(190, 290, ts, DO)
    t += mark(190 + 52, 290 - 94, 15, DO) + W("Mỗi mẻ bánh, một lời cam kết", 10, 190, 290 - 18, MUC, "xb", "middle")
    p = garm(540, 290, ts, TRANG, u, "p", A.POLO, big(540 - 20, 290 + 150, 100, DO)) + collar_polo(540, 290, ts, DO, u)
    p += fit(V.logo_ngang(), 540 - 50 * ts, 290 - 82 * ts, w=66 * ts)
    a = tie(890, 300, .9, DO) + garm(890, 300, .9, DO, u, "a", APRON, big(890, 300 + 196, 112, DO2), seams=False) + stitch(890, 300, .9, KEM)
    a += mark(890, 300 - 130 * .9, 26, KEM) + W("Ẩm Thực An Tâm", 20, 890, 300 - 62, KEM, "xb", "middle")
    a += W("Mỗi mẻ bánh, một lời cam kết", 11, 890, 300 - 34, "#FFD6D3", "md", "middle")
    return bang("Hướng 5 · Chữ lớn", "Chữ AN TÂM bằng font riêng in rất lớn, tràn và cắt mép áo – trẻ, kiểu streetwear, dấu mũ vân tay nhìn rõ từ xa.", t + p + a, u)


def _lap(x, y, w, h, c, r=11, gap=46, op=1):
    o = ""
    for j, yy in enumerate(range(int(y), int(y + h) + gap, gap)):
        for xx in range(int(x) - (gap // 2 if j % 2 else 0), int(x + w) + gap, gap):
            o += f'<g opacity="{op}">{mark(xx, yy, r, c, rings=6)}</g>'
    return o


# ───────── Hướng 6 · HOẠ TIẾT LẶP: vân tay nhỏ lặp kín (monogram)
def huong_6():
    u = "h6"; ts = .95
    t = garm(190, 290, ts, DO, u, "t", A.TEE, _lap(10, 110, 360, 380, DO2, 11, 44)) + A._co_tron(190, 290, ts, DO2)
    t += f'<rect x="{190 - 80}" y="{290 - 8}" width="160" height="56" rx="28" fill="{KEM}"/>' + W("An Tâm", 26, 190, 290 + 30, DO, "xb", "middle")
    pd = _clip("s6p", _P(540, 290, ts, SLV), f'<rect x="360" y="120" width="360" height="240" fill="{DO}"/>' + _lap(360, 130, 360, 200, KEM, 7, 26))
    p = garm(540, 290, ts, KEM, u, "p", A.POLO, pd) + collar_polo(540, 290, ts, DO, u)
    p += f'<rect x="{540 + 30 * ts}" y="{290 - 100 * ts}" width="{46 * ts}" height="{50 * ts}" rx="4" fill="{DO}"/>' + _clip("pk6", f"M{540 + 30 * ts},{290 - 100 * ts} h{46 * ts} v{50 * ts} h{-46 * ts}Z", _lap(540 + 20, 290 - 104, 70, 60, KEM, 6, 20))
    p += fit(V.logo_ngang(), 540 - 52 * ts, 290 - 82 * ts, w=60 * ts)
    a = tie(890, 300, .9, DO) + garm(890, 300, .9, KEM, u, "a", APRON, _lap(740, 90, 300, 440, DO, 10, 42, .22), seams=False) + stitch(890, 300, .9, DO)
    a += f'<rect x="{890 - 96}" y="{300 - 150}" width="192" height="120" rx="10" fill="{KEM}"/>'
    a += mark(890, 300 - 112, 26, DO) + W("An Tâm", 26, 890, 300 - 52, DO, "xb", "middle")
    return bang("Hướng 6 · Hoạ tiết lặp", "Dấu vân tay nhỏ lặp kín như hoa văn monogram: áo thun đỏ vân chìm, polo kem có tay và túi ngực in hoạ tiết, tạp dề in lặp mờ.", t + p + a, u)


# ───────── Hướng 7 · TỐI GIẢN: chỉ một chấm son – nét riêng của biểu tượng 1.1
def huong_7():
    u = "h7"; ts = .95
    dot = lambda cx, cy, r: f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{DO}"/>'
    t = garm(190, 290, ts, KEM, u, "t", A.TEE, "") + A._co_tron(190, 290, ts, KEM)
    t += dot(190 + 54, 290 - 96, 9) + W("an tâm", 12, 190 + 54, 290 - 72, MUC, "xb", "middle", .2)
    t += f'<rect x="{190 - 104 * ts}" y="{290 + 120 * ts}" width="{208 * ts}" height="6" fill="{DO}"/>'
    p = garm(540, 290, ts, MUC, u, "p", A.POLO, "") + collar_polo(540, 290, ts, MUC, u)
    p += f'<path d="{_P(540, 290, ts, "M -40,-150 C -20,-160 20,-160 40,-150")}" fill="none" stroke="{DO}" stroke-width="3"/>'
    p += dot(540 + 54 * ts, 290 - 90 * ts, 7) + W("an tâm", 10, 540 + 54 * ts, 290 - 68 * ts, KEM, "xb", "middle", .2)
    a = tie(890, 300, .9, MUC) + garm(890, 300, .9, "#EDE3D6", u, "a", APRON, "", seams=False) + stitch(890, 300, .9, MUC)
    a += dot(890, 300 - 130, 14) + W("an tâm", 18, 890, 300 - 92, MUC, "xb", "middle", .2)
    a += f'<rect x="{890 - 112}" y="{300 + 150}" width="224" height="5" fill="{DO}"/>'
    return bang("Hướng 7 · Tối giản chấm tâm", "Bỏ hết, chỉ giữ chấm son – lõi của dấu vân tay chấm tâm – và chữ an tâm nhỏ. Cao cấp, hợp văn phòng, showroom, sự kiện.", t + p + a, u)


HUONG += [("huong-4-khoi-mau", huong_4), ("huong-5-chu-lon", huong_5), ("huong-6-hoa-tiet-lap", huong_6), ("huong-7-toi-gian", huong_7)]

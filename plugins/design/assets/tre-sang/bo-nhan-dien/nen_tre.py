"""Bộ nền thương hiệu An Tâm (hướng Trẻ & Sang) và đường nét đứt.
nen(kieu, w, h) -> SVG; net(kieu) -> SVG dải 1200 x 60.
Chạy trực tiếp: xuất file vào thư mục đích (đối số 1), 8 nền x 3 cỡ + 6 đường nét đứt.
"""
import math
import os
import random
import sys

import bac_thang as BT
import logo_tre as T

CH, CH2, KEM, HONG, BO, DEN, BANH, DOM = T.CHERRY, T.CHERRY2, T.KEM, T.HONG, T.BO, T.DEN, "#F4D59B", "#A7652E"
SIZES = {"ngang-1920x1080": (1920, 1080), "bai-dang-1080x1350": (1080, 1350), "doc-1080x1920": (1080, 1920)}


def _svg(w, h, body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{label}">{body}</svg>'


def hat(cx, cy, w, fill, cut, ang):
    return f'<g transform="rotate({ang:.0f} {cx:.0f} {cy:.0f})">{T.hat(cx, cy, w, fill, cut, 0)}</g>'


def n_cham(w, h):
    r = random.Random(1); b = [f'<rect width="{w}" height="{h}" fill="{CH}"/>']
    st = 360
    for yy in range(0, h + st, st):
        for xx in range(0, w + st, st):
            if r.random() < .55:
                R = r.choice([40, 70, 110, 150])
                b.append(f'<circle cx="{xx + r.uniform(-90, 90):.0f}" cy="{yy + r.uniform(-90, 90):.0f}" r="{R}" fill="{r.choice([KEM, HONG, BO, CH2])}"/>')
    return _svg(w, h, "".join(b), "Nền cherry chấm bánh")


def n_duong_may(w, h):
    b = [f'<rect width="{w}" height="{h}" fill="{KEM}"/>']
    for i, y in enumerate(range(80, h, 120)):
        d = f"M-40,{y} " + " ".join(f"q60,{-26 if k % 2 == 0 else 26} 120,0" for k in range(w // 120 + 2))
        b.append(f'<path d="{d}" fill="none" stroke="{CH if i % 2 == 0 else HONG}" stroke-width="7" stroke-dasharray="26 18" stroke-linecap="round"/>')
    r = random.Random(3)
    for _ in range(int(w * h / 140000)):
        b.append(hat(r.uniform(0, w), r.uniform(0, h), 150, r.choice([BO, CH]), KEM, r.uniform(-30, 30)))
    return _svg(w, h, "".join(b), "Nền kem đường may")


def n_sticker(w, h):
    b = [f'<rect width="{w}" height="{h}" fill="{BO}"/>']; r = random.Random(5)
    step = 170
    for yy in range(0, h + step, step):
        for xx in range(0, w + step, step):
            x = xx + (step / 2 if (yy // step) % 2 else 0) + r.uniform(-25, 25); y = yy + r.uniform(-25, 25)
            b.append(hat(x, y, 96, r.choice([CH, CH, KEM, HONG]), BO, r.uniform(0, 360)))
    return _svg(w, h, "".join(b), "Nền vàng bơ sticker bánh")


def n_neon(w, h):
    wm = T.wordmark("none", BO, "none", False, False).replace('fill="none" d', 'fill="none" stroke="#FFB3BA" stroke-width="2.6" d', 1)
    ww = min(w * .7, 1400); hh = ww * .42
    b = (f'<defs><filter id="g" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
         f'<radialGradient id="rg" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#3A0F14"/><stop offset="1" stop-color="#120608"/></radialGradient></defs>'
         f'<rect width="{w}" height="{h}" fill="url(#rg)"/>')
    b += "".join(f'<rect x="{x}" y="0" width="1.5" height="{h}" fill="#fff" opacity=".035"/>' for x in range(0, w, 60))
    b += f'<g filter="url(#g)" opacity=".9">{wm.replace("<svg ", f"<svg x={(w - ww) / 2:.0f} y={(h - hh) / 2:.0f} width={ww:.0f} height={hh:.0f} ", 1)}</g>'
    return _svg(w, h, b, "Nền đêm neon")


def n_chu_lon(w, h):
    wm = T.wordmark(CH, BO, HONG, False, False)
    ww = w * 1.5; hh = ww * .42
    b = f'<rect width="{w}" height="{h}" fill="{HONG}"/>' + wm.replace("<svg ", f'<svg x="{-w * .18:.0f}" y="{h * .5 - hh * .5:.0f}" width="{ww:.0f}" height="{hh:.0f}" ', 1)
    return _svg(w, h, b, "Nền hồng chữ lớn")


def n_bac_thang(w, h):
    b = [f'<rect width="{w}" height="{h}" fill="{CH}"/>']
    C, S = BT.C, BT.S
    for j in range(-8, int((w + h) / 160) + 4):
        x, y = -200, j * 220 - 200
        pts = []
        for k in range(30):
            pts += [(x, y), (x + C * 200, y + S * 200)]
            x, y = x + C * 200, y + S * 200 - 140
        d = "M" + " L".join(f"{a:.0f},{c:.0f}" for a, c in pts)
        b.append(f'<path d="{d}" fill="none" stroke="{CH2 if j % 2 else "#D02A33"}" stroke-width="10" stroke-linejoin="round"/>')
    return _svg(w, h, "".join(b), "Nền bậc thang")


def n_dom_nuong(w, h):
    b = [f'<rect width="{w}" height="{h}" fill="{BANH}"/>']; r = random.Random(9)
    for _ in range(int(w * h / 5200)):
        x, y = r.uniform(0, w), r.uniform(0, h); L = r.uniform(8, 28)
        b.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{L:.1f}" ry="{L * r.uniform(.45, .7):.1f}" transform="rotate({r.randint(0, 180)} {x:.0f} {y:.0f})" fill="{r.choice([DOM, "#8E4E1C", "#C08048"])}" opacity="{r.choice([.3, .45, .6])}"/>')
    return _svg(w, h, "".join(b), "Nền đốm nướng")


def n_mai_hien(w, h):
    sw = 160; b = [f'<rect width="{w}" height="{h}" fill="{KEM}"/>']
    top = int(h * .26)
    for i in range(w // sw + 2):
        b.append(f'<rect x="{i * sw}" y="0" width="{sw / 2}" height="{top}" fill="{CH}"/>')
        b.append(f'<path d="M{i * sw},{top} a{sw / 4},{sw / 4} 0 0 0 {sw / 2},0 Z" fill="{CH}"/>')
        b.append(f'<path d="M{i * sw + sw / 2},{top} a{sw / 4},{sw / 4} 0 0 0 {sw / 2},0 Z" fill="{KEM}"/>')
    b.append(f'<rect y="{top + 40}" width="{w}" height="10" fill="{CH}" opacity=".18"/>')
    return _svg(w, h, "".join(b), "Nền mái hiên")


NEN = {
    "cham-banh": ("Chấm bánh", "Cherry, chấm tròn như những chiếc bánh. Nền chính cho mạng xã hội.", n_cham),
    "duong-may": ("Đường may", "Kem, đường chỉ khâu đứt quãng và bánh nhỏ. Bao bì, giấy gói.", n_duong_may),
    "sticker": ("Bánh sticker", "Vàng bơ rải bánh nhỏ nhiều màu. Bài khuyến mãi, ly, hộp.", n_sticker),
    "dem-neon": ("Đêm neon", "Nền tối, chữ an tâm phát sáng. Màn hình cửa hàng, story buổi tối.", n_neon),
    "chu-lon": ("Chữ lớn", "Hồng phấn, chữ an tâm cắt mép. Bìa, băng rôn, trang chủ.", n_chu_lon),
    "bac-thang": ("Bậc thang", "Cherry, đường bậc thang chéo 30 độ. Nền cho chữ bậc thang.", n_bac_thang),
    "dom-nuong": ("Đốm nướng", "Màu bánh với đốm cháy. Nền chụp, đặt ảnh sản phẩm.", n_dom_nuong),
    "mai-hien": ("Mái hiên", "Sọc đỏ kem như mái hiên quán. Biển, quầy, đầu thực đơn.", n_mai_hien),
}


# ---------- đường nét đứt (1200 x 60) ----------
def _strip(body, label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" role="img" aria-label="{label}">{body}</svg>'


def net_chi():
    return _strip(f'<path d="M0,30 H1200" stroke="{CH}" stroke-width="6" stroke-dasharray="26 16" stroke-linecap="round"/>', "Đường chỉ khâu")


def net_banh():
    return _strip("".join(T.hat(30 + i * 60, 44, 40, CH if i % 2 == 0 else BO, KEM, 0) for i in range(20)), "Chuỗi bánh")


def net_bac():
    return _strip("".join(f'<path d="M{x},46 l26,-15 l0,15" fill="none" stroke="{CH}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>' for x in range(4, 1200, 42)), "Đường bậc thang")


def net_cham():
    return _strip("".join(f'<circle cx="{x}" cy="30" r="{8 if (x // 40) % 3 == 0 else 5}" fill="{[CH, BO, HONG][(x // 40) % 3]}"/>' for x in range(20, 1200, 40)), "Chuỗi chấm")


def net_song():
    d = "M0,30 " + " ".join("q15,-16 30,0 q15,16 30,0" for _ in range(20))
    return _strip(f'<path d="{d}" fill="none" stroke="{CH}" stroke-width="5" stroke-dasharray="14 10" stroke-linecap="round"/>', "Sóng nét đứt")


def net_cat():
    s = f'<path d="M70,30 H1200" stroke="{DEN}" stroke-width="3" stroke-dasharray="14 10"/>'
    s += f'<g transform="translate(14 12)" fill="none" stroke="{CH}" stroke-width="4" stroke-linecap="round"><circle cx="10" cy="8" r="7"/><circle cx="10" cy="28" r="7"/><path d="M16,12 L46,26 M16,24 L46,10"/></g>'
    return _strip(s, "Đường cắt")


NET = {"chi-khau": ("Chỉ khâu", net_chi), "chuoi-banh": ("Chuỗi bánh", net_banh), "bac-thang": ("Bậc thang", net_bac),
       "chuoi-cham": ("Chuỗi chấm", net_cham), "song": ("Sóng nét đứt", net_song), "duong-cat": ("Đường cắt", net_cat)}


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(os.path.join(out, "nen"), exist_ok=True); os.makedirs(os.path.join(out, "net-dut"), exist_ok=True)
    n = 0
    for k, (_, _, fn) in NEN.items():
        for sz, (w, h) in SIZES.items():
            open(os.path.join(out, "nen", f"nen-{k}-{sz}.svg"), "w").write(fn(w, h) + "\n"); n += 1
    for k, (_, fn) in NET.items():
        open(os.path.join(out, "net-dut", f"net-{k}.svg"), "w").write(fn() + "\n"); n += 1
    print("đã xuất", n, "file")

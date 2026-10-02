"""Phương án B: mặt trước lấy tên AN TÂM làm chủ (chữ lớn), cửa sổ vân tay bên dưới. Dùng chung khổ, mặt sau với tui_tortilla.py.
Chạy: python3 tui_ten.py OUTDIR"""
import os
import sys

import tui_tortilla as T

V, W, place = T.V, T.W, T.place
DO, DO2, KEM, MUC, NGO = T.DO, T.DO2, T.KEM, T.MUC, T.NGO
WIN = (150, 213, 45)
RING = 68


def mat_truoc_ten(window=None):
    cx, cy, rw = WIN
    s = f'<rect x="{-T.BL}" y="{-T.BL}" width="{T.TW + 2 * T.BL}" height="{T.TH + 2 * T.BL}" fill="{DO}"/>'
    s += f'<mask id="cs2"><rect x="-10" y="-10" width="320" height="350" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="{rw}" fill="#000"/></mask><g mask="url(#cs2)">'
    s += T.nen(-T.BL, -T.BL, T.TW + 2 * T.BL, 40 + T.BL) + f'<rect x="{-T.BL}" y="39" width="{T.TW + 2 * T.BL}" height="1.6" fill="{DO2}"/>'
    s += T.vong_van(cx, cy, rw + 4, RING, KEM, n=12, seed=17, sw=1.8)
    s += f'<circle cx="{cx}" cy="{cy}" r="{rw + 1.2}" fill="none" stroke="{KEM}" stroke-width="2.4"/></g>'
    if window == "banh":
        s += T.banh_qua_cua_so(cx, cy, rw)
    s += W("ẨM THỰC", 7, 150, 58, NGO, "xb", "middle", .42)
    s += W("AN TÂM", 70, 150, 122, KEM, "xb", "middle", -.01)
    s += W("Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm", 5.2, 150, 134, KEM, "md", "middle", .02)
    s += f'<g transform="rotate(-12 245 268)">{place(V.con_dau(KEM, DO), 224, 247, 42, 42)}</g>'
    s += f'<rect x="85" y="288" width="130" height="16" rx="8" fill="{KEM}"/>' + W("BÁNH TORTILLA", 8.4, 150, 299.4, DO, "xb", "middle", .1)
    s += W("Cỡ [ ] inch  ·  [ ] chiếc  ·  Khối lượng tịnh: [     ] g", 4.4, 150, 312, KEM, "md", "middle", .02)
    return s


if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    T.mat_truoc = mat_truoc_ten          # mockup & bản kỹ thuật dùng mặt mới
    T.WIN = WIN
    files = {
        "tui-an-tam-mat-truoc.svg": T.doc(mat_truoc_ten(), "Túi tortilla AN TÂM – mặt trước (file in)"),
        "tui-an-tam-mat-sau.svg": T.doc(T.mat_sau(), "Túi tortilla AN TÂM – mặt sau (file in)"),
        "ky-thuat-an-tam-mat-truoc.svg": T.doc(mat_truoc_ten() + T.ky_thuat("truoc"), "Bản kỹ thuật mặt trước", mm=False),
        "mockup-an-tam.svg": T.mockup(),
    }
    for n, s in files.items():
        open(os.path.join(out, n), "w").write(s)
    print("ok")

"""Xuất bộ logo Điểm Chỉ 1.1 (Chấm tâm): SVG + danh sách PNG cần chụp. Chạy: python3 xuat_logo.py LOGO_DIR"""
import json
import os
import sys

import build_chuan as C

V = C.V
DO, KEM, MUC = V.DO, V.KEM, V.MUC

SVG = {
    "logo-ngang.svg": V.logo_ngang(),
    "logo-ngang-nen-do.svg": V.logo_ngang(KEM, KEM, bg=DO),
    "logo-dung.svg": V.logo_dung(),
    "logo-dung-nen-do.svg": V.logo_dung(KEM, KEM, bg=DO),
    "bieu-tuong.svg": V.bieu_tuong(),
    "bieu-tuong-nho.svg": V.bieu_tuong_nho(),
    "dau-tron.svg": V.con_dau(),
}
# PNG nền trong suốt 2000 px (cạnh dài)
PNG = {
    "logo-ngang-do.png": V.logo_ngang(),
    "logo-ngang-kem.png": V.logo_ngang(KEM, KEM),
    "logo-dung-do.png": V.logo_dung(),
    "logo-dung-kem.png": V.logo_dung(KEM, KEM),
    "bieu-tuong-van-tay-do.png": V.van_tay(0, 0, 96, DO, aspect=1.15).join(['<svg xmlns="http://www.w3.org/2000/svg" viewBox="-104 -116 208 232">', '</svg>']),
    "bieu-tuong-van-tay-kem.png": V.van_tay(0, 0, 96, KEM, aspect=1.15).join(['<svg xmlns="http://www.w3.org/2000/svg" viewBox="-104 -116 208 232">', '</svg>']),
    "bieu-tuong-nho-do.png": V.van_tay_nho(0, 0, 96, DO).join(['<svg xmlns="http://www.w3.org/2000/svg" viewBox="-104 -116 208 232">', '</svg>']),
    "dau-tron.png": V.con_dau(),
}

if __name__ == "__main__":
    d = sys.argv[1]
    os.makedirs(os.path.join(d, "svg"), exist_ok=True); os.makedirs(os.path.join(d, "png-src"), exist_ok=True)
    for n, s in SVG.items():
        open(os.path.join(d, "svg", n), "w").write(s)
    for n, s in PNG.items():
        open(os.path.join(d, "png-src", n.replace(".png", ".svg")), "w").write(s)
    print("ok")

"""Đóng gói font "An Tam Tron Banh" (An Tâm Tròn Bánh) để cài và dùng: đặt tên chuẩn họ font, 3 độ đậm, TTF + WOFF2.
Chạy: python3 dong_goi_font.py <thư mục đích>
"""
import os
import shutil
import sys

from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FAM = "An Tam Tron Banh"
PS = "AnTamTronBanh"
STYLES = [("ChamNganThuong", "Regular", 400), ("ChamNganVua", "SemiBold", 600), ("ChamNgan", "ExtraBold", 800)]
COPY = ("Copyright 2019 The Baloo 2 Project Authors (https://github.com/EkType/Baloo2). "
        "Modified 2026 for Am Thuc An Tam: fingerprint-ridge circumflex, fingerprint-whorl dots, ink-spread corners.")


def set_names(f, style, weight):
    full = FAM if style == "Regular" else f"{FAM} {style}"
    legacy_fam = FAM if style == "Regular" else f"{FAM} {style}"
    vals = {0: COPY, 1: legacy_fam, 2: "Regular", 3: f"1.000;{PS}-{style}", 4: full, 5: "Version 1.000",
            6: f"{PS}-{style}", 13: "This Font Software is licensed under the SIL Open Font License, Version 1.1.",
            14: "https://openfontlicense.org", 16: FAM, 17: style}
    name = f["name"]
    name.names = [r for r in name.names if r.nameID not in vals and r.nameID < 256]
    for nid, v in vals.items():
        name.setName(v, nid, 3, 1, 0x409)
        name.setName(v, nid, 1, 0, 0)
    os2 = f["OS/2"]; os2.usWeightClass = weight
    os2.fsSelection = (os2.fsSelection & ~0b1100001) | 0b1000000   # REGULAR, không italic/bold
    f["head"].macStyle = 0
    f["head"].fontRevision = 1.0
    if "CFF " not in f:
        f["post"].formatType = 2.0


def main(out):
    os.makedirs(out, exist_ok=True)
    for src, style, w in STYLES:
        f = TTFont(os.path.join(HERE, "fonts-tron", f"AnTamTron{src}.ttf"))
        set_names(f, style, w)
        f.flavor = None; f.save(os.path.join(out, f"{PS}-{style}.ttf"))
        f.flavor = "woff2"; f.save(os.path.join(out, f"{PS}-{style}.woff2"))
    shutil.copy(os.path.join(HERE, "baloo-2", "LICENSE"), os.path.join(out, "OFL.txt"))
    print("đã đóng gói", len(STYLES), "độ đậm vào", out)


if __name__ == "__main__":
    main(sys.argv[1])

"""Bộ nhận diện bản tinh chỉnh: logo bánh gập đôi + linh vật Bé Cuộn có khối 3D.
Dùng lại bố cục build_nl.py, thay logo, linh vật, hoạ tiết. Chạy: python3 build_nl2.py OUT.html
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "nl"))
import logo_nl as NL  # noqa: E402
import logo2 as L2  # noqa: E402
from mascot3d import mascot  # noqa: E402

# chiếc bánh gập đôi thay cho chiếc taco trong hoạ tiết
NL.taco = lambda x, y, w, fill, cut, tilt=-12: L2.hat(x, y, w, fill, cut, None, tilt)

NL.OUT.update({
    "wm_do": L2.wordmark(L2.VANG, L2.DO),
    "wm_kem": L2.wordmark(L2.DO, L2.KEM, L2.MUC),
    "wm_bo": L2.wordmark(L2.DO, L2.BO, L2.MUC),
    "wm_muc": L2.wordmark(L2.VANG, L2.MUC),
    "wm_den": L2.wordmark("#000", "#fff"),
    "wm_gon_do": L2.wordmark(L2.VANG, L2.DO, top=False, sub=False),
    "mark_do": L2.mark(), "mark_vang": L2.mark(L2.DO, L2.VANG, L2.VANG), "mark_kem": L2.mark(L2.DO, L2.KEM, L2.KEM),
    "mascot": mascot("ma", "chao"), "mascot2": mascot("mb", "like"), "mascot3": mascot("mc", "cam"),
})

import build_nl as B  # noqa: E402

REPL = [
    ("<title>An Tâm Đỏ Vàng</title>", "<title>An Tâm Bé Cuộn</title>"),
    ("Đỏ và vàng, <span>một chiếc taco</span> làm dấu mũ", "Đỏ và vàng, <span>chiếc bánh</span> làm dấu mũ"),
    ("An Tâm đặt chiếc taco làm dấu mũ chữ â.", "An Tâm đặt chiếc bánh tortilla gập đôi làm dấu mũ chữ â."),
    ("Bé Tâm: chiếc taco biết cười, má hồng, dùng trên bao bì, bài đăng, cửa hàng.", "Bé Cuộn: chiếc bánh cuộn doner biết cười, có khối 3D, dùng trên bao bì, bài đăng, cửa hàng."),
    ("thay nón lá và hạt cà phê bằng chiếc bánh của An Tâm", "thay nón lá và hạt cà phê bằng chiếc bánh của An Tâm"),
    ("dấu mũ là chiếc taco nghiêng", "dấu mũ là chiếc bánh gập đôi có đốm nướng, đặt nghiêng"),
    ("Chiếc taco nằm ngay trong tên", "Chiếc bánh nằm ngay trong tên"),
    ("Chiếc taco nằm đúng chỗ dấu mũ", "Chiếc bánh nằm đúng chỗ dấu mũ"),
    ("Bé Tâm, <span>chiếc taco biết cười</span>", "Bé Cuộn, <span>chiếc bánh cuộn biết cười</span>"),
    ("Vỏ bánh vàng có đốm nướng, nhân thịt, rau, cà chua: nhìn là biết taco.", "Thân là bánh tortilla cuộn có đốm nướng, gói giấy đỏ, miệng đầy thịt, rau, cà chua: nhìn là biết doner cuộn."),
    ("Đây là bản vẽ phẳng. Muốn có bản 3D như Nonla thì cần người dựng hình 3D làm theo bản này.", "Khối 3D dựng bằng đổ bóng trên bản vẽ vector, in rõ ở mọi cỡ. Muốn bản dựng 3D thật (xoay, hoạt hình) thì người dựng hình làm theo bản này."),
    ("Hàng taco <span>như hàng nón</span>", "Hàng bánh <span>như hàng nón</span>"),
    ("An Tâm lặp hàng taco nhỏ nghiêng", "An Tâm lặp hàng bánh gập đôi nhỏ nghiêng"),
    ("<b>Hàng taco</b>", "<b>Hàng bánh</b>"),
    (".sw .n{font:400 72px/1 var(--hep)}", ".sw .n{font:400 72px/1 var(--hep)}.pal .sw:last-child .n{font-size:40px}"),
]


def page():
    h = B.page()
    for a, b in REPL:
        h = h.replace(a, b)
    # thêm tư thế thứ ba vào hàng linh vật
    h = h.replace('<div class="mnotes">', f'<div class="mcard" style="background:#2A1512;color:var(--kem)">{B.lg("mascot3")}<b>Mời bánh</b></div><div class="mnotes">', 1)
    h = h.replace(".masc-row{display:grid;grid-template-columns:1fr 1fr 1.2fr;", ".masc-row{display:grid;grid-template-columns:1fr 1fr 1fr;")
    h = h.replace(".mnotes{background:#fff;", ".mnotes{grid-column:1/-1;grid-template-columns:1fr 1fr;background:#fff;")
    return h


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

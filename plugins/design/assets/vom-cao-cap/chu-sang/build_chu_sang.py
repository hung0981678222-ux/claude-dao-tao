"""Trang 3 phương án logo với chữ AN TÂM mới (tương phản cao, sang trọng, có chi tiết món ăn).
Dùng lại bố cục build_phuong_an.py. Chạy: python3 build_chu_sang.py OUT.html"""
import sys

import chu_sang as C
import phuong_an
phuong_an.OUT.update(C.OUT)
import build_phuong_an as BP  # noqa: E402


def a_mark(fg, hat, bg):
    return C.a_mark(fg, hat)


BP.a_mark = a_mark

SPEC_CSS = """
.spec{background:#fff;border-bottom:1px solid var(--line);padding-block:64px}
.spec .big{background:var(--ivory);border:1px solid var(--line);padding:64px 48px;display:grid;place-items:center}
.spec .big svg{width:min(100%,900px);height:auto;display:block}
.notes{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:24px}
.notes div{border-top:2px solid var(--ink);padding-top:12px;font-size:14px;color:var(--muted)}
.notes b{display:block;color:var(--ink);font-weight:600;font-size:16px;margin-bottom:4px}
.zoom{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:16px}
.zoom div{background:var(--red);display:grid;place-items:center;padding:28px;aspect-ratio:4/3}
.zoom svg{height:100%;max-height:200px;width:auto}
@media (max-width:900px){.notes,.zoom{grid-template-columns:1fr 1fr}}
"""


def zoom_svg(vb):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill="#F6F1E8" d="{C.WM}"/><path fill="#C39443" d="{C.HATD}"/></svg>'


def page():
    h = BP.page()
    ax = C.XS["Â"][0]
    spec = f"""<section class="spec"><div class="w">
 <p class="eyebrow">Chữ AN TÂM vẽ riêng</p>
 <div class="big">{C.OUT['wm_kem']}</div>
 <div class="notes">
  <div><b>Dày mảnh rõ rệt</b>Nét đậm và nét chỉ mảnh xen nhau như chữ của các nhãn thời trang, nước hoa: nhìn là thấy sang.</div>
  <div><b>Chữ A mái vòm</b>Đỉnh tròn như cửa tiệm bánh, nét đậm dồn về bên phải như một nét bút lông.</div>
  <div><b>Thanh ngang gợn sóng</b>Thanh ngang của hai chữ A uốn nhẹ như mép bánh cuộn, chi tiết riêng của ngành bánh.</div>
  <div><b>Mũ là chiếc bánh</b>Dấu mũ chữ Â là bánh tortilla gập đôi có đốm nướng, in vàng đồng.</div>
 </div>
 <div class="zoom">
  <div>{zoom_svg("-8 -6 96 112")}</div>
  <div>{zoom_svg(f"{ax - 8:.0f} -36 96 142")}</div>
  <div>{zoom_svg(f"{C.XS['T'][0] - 8:.0f} -6 {C.XS['T'][1] + 16:.0f} 112")}</div>
 </div>
</div></section>"""
    h = h.replace("<title>Phương án logo An Tâm</title>", "<title>Chữ An Tâm sang trọng</title>")
    h = h.replace("</style>", SPEC_CSS + "</style>", 1)
    h = h.replace("<h1>Ba cách đặt chữ, <b>rõ là đồ ăn</b></h1>", "<h1>Chữ AN TÂM mới, <b>sang và rõ là đồ ăn</b></h1>")
    h = h.replace("<div><b>Chữ AN TÂM giữ nguyên</b>Chỉ đổi vị trí ẨM THỰC và cách thể hiện ngành thực phẩm.</div>",
                  "<div><b>Chữ AN TÂM vẽ lại</b>Nét dày mảnh sang trọng, chữ A mái vòm, thanh ngang gợn như mép bánh.</div>")
    h = h.replace("</header>", "</header>" + spec, 1)
    return h


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

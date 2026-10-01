"""Trang chữ AN TÂM: thêm 6 kiểu nét chữ và 2 bố cục mới (khung vòm đứng, tem tròn).
Chạy: python3 build_chu_sang2.py OUT.html"""
import sys

import build_chu_sang as BC
import bien_the as V

RED, IVORY, INK, GOLD = V.RED, V.IVORY, V.INK, V.GOLD

KIEU = [
    ("A", "Thanh lịch", "thanh_lich", 0, False, "Bản gốc: dày mảnh rõ, chân mảnh. Sang, dễ đọc."),
    ("B", "Đậm", "dam", 0, False, "Nét dày hơn, nổi bật trên biển hiệu và nhìn từ xa."),
    ("C", "Không chân", "khong_chan", 0, False, "Bỏ chân chữ, hiện đại và gọn hơn, vẫn giữ tương phản."),
    ("D", "Viền khắc", "khac", 0, True, "Đường chỉ khắc bên trong nét, như biển đồng của nhà hàng lâu năm."),
    ("E", "Miếng cắn", "mieng_can", 0, False, "Chữ M bị cắn một miếng ở góc: dí dỏm, rõ là đồ ăn."),
    ("F", "Nghiêng", "nghieng", -12, False, "Nghiêng như nét viết tay, có chuyển động, hợp đồ ăn nhanh."),
]

CSS = """
.kieu{padding-block:64px;border-bottom:1px solid var(--line)}
.kgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px}
.k{display:flex;flex-direction:column;gap:10px}
.k .tile{background:var(--red);padding:34px 26px;display:grid;place-items:center;aspect-ratio:16/9}
.k .tile.kem{background:var(--ivory);border:1px solid var(--line)}
.k .tile svg{width:100%;height:auto;display:block}
.k .duo{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.k b{font:600 17px/1.2 var(--f)}.k b i{font-style:normal;color:var(--red);margin-right:8px}
.k p{font-size:14px;color:var(--muted)}
.bocuc{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px}
.bocuc > div{display:grid;place-items:center;padding:40px;min-height:520px}
.bocuc svg{width:min(100%,360px);height:auto;display:block}
@media (max-width:900px){.kgrid,.bocuc{grid-template-columns:1fr}}
"""


def page():
    h = BC.page()
    cards = ""
    for code, name, key, sk, inl, desc in KIEU:
        red = V.word_svg(key, IVORY, GOLD, RED, sk, inl, "r" + code)
        kem = V.word_svg(key, INK, GOLD, IVORY, sk, inl, "k" + code)
        cards += (f'<div class="k"><div class="tile">{red}</div><div class="tile kem">{kem}</div>'
                  f'<b><i>{code}</i>{name}</b><p>{desc}</p></div>')
    kieu = f"""<section class="kieu"><div class="w">
 <p class="eyebrow">Thêm phương án · 6 kiểu nét chữ</p>
 <div class="kgrid">{cards}</div>
 <p style="margin-top:20px;color:var(--muted);font-size:14px">Mỗi kiểu chữ dùng được với cả 5 bố cục bên dưới.</p>
</div></section>"""
    bocuc = f"""<section><div class="w">
 <div class="oh"><span class="num">4–5</span><div><h2>Thêm bố cục: khung vòm đứng, tem tròn</h2>
 <p>Bố cục 4 xếp AN trên TÂM trong khung vòm viền vàng, như nhãn chai cao cấp. Hợp hộp quà, túi, menu đứng. Bố cục 5 là tem tròn, chữ chạy vòng quanh, hợp tem niêm phong, ly, hộp tròn.</p></div><span class="tag">Thêm bố cục</span></div>
 <div class="bocuc">
  <div style="background:var(--ivory);border:1px solid var(--line)">{V.vom_dung(INK, GOLD, GOLD, None, "v1")}</div>
  <div style="background:var(--red)">{V.vom_dung(IVORY, GOLD, GOLD, None, "v2")}</div>
  <div style="background:#2A211E">{V.tem_tron(IVORY, GOLD, GOLD, RED, "t1")}</div>
  <div style="background:var(--ivory);border:1px solid var(--line)">{V.tem_tron(INK, GOLD, GOLD, "#FBF8F2", "t2")}</div>
 </div>
</div></section>"""
    h = h.replace("</style>", CSS + "</style>", 1)
    h = h.replace('<section id="pa1">', kieu + '<section id="pa1">', 1)
    h = h.replace("<footer>", bocuc + "<footer>", 1)
    h = h.replace("<b>Anh chị chọn phương án 1, 2 hoặc 3</b>", "<b>Anh chị chọn một kiểu chữ (A đến F) và một bố cục (1 đến 5)</b>")
    return h


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

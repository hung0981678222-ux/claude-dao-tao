"""Trang: giữ vân tay Điểm Chỉ, lồng cách điệu thương hiệu. Chạy: python3 build_van_rieng.py OUT.html"""
import sys

import build_chuan as C
import build_dau_rieng as BD
import van_rieng as R

DO, K = R.DO, R.KEM
Y = {
    "goc": "Dấu vân tay xoáy như thiết kế hiện tại.",
    "loi-a": "Ba vòng vân trong cùng nhường chỗ cho chữ A nét mảnh – lõi vân tay chính là chữ đầu của An Tâm. Nhìn xa vẫn là vân tay, nhìn gần thấy A.",
    "mu-van": "Ba đường vân trên cùng được nhấc lên thành dấu mũ – đúng như dấu mũ vân tay trong font An Tâm Tròn Bánh. Dấu vân tay \"đội\" dấu mũ của chữ Tâm.",
    "cham-tam": "Lõi vân là một chấm son tròn – \"tâm\" của dấu tay, cũng là chữ Tâm. Tinh giản nhất, giữ gần như nguyên bản.",
    "mu-a": "Kết hợp mũ vân + lõi A: trên là dấu mũ của font, giữa là chữ A. Đọc được thành \"Â\" – chữ cái riêng của An Tâm – mà vẫn là một dấu vân tay.",
    "mu-tam": "Kết hợp mũ vân + chấm tâm: dấu mũ trên đầu, chấm tâm ở giữa – như chữ â tròn. Mềm, dễ nhớ, rõ ở cỡ nhỏ.",
}


def card(key, name, o):
    f = lambda c=DO: R.van(color=c, **o)
    mk = lambda c=DO: f'<g transform="scale(.82) translate(0 8)">{f(c)}</g>'
    small = "".join(R.svg(f(), s) for s in (20, 28, 40, 64))
    return f"""<section class="s" id="{key}"><div class="num">{'Tham chiếu' if key == 'goc' else 'Biến thể'}</div><h2>{name}</h2><p class="lead">{Y[key]}</p>
<div class="g g4"><div class="card">{R.svg(f(), 260)}</div><div class="card d">{R.svg(f(K), 260)}</div>
<div class="card">{BD.avatar(mk(K))}<p class="cap">Ảnh đại diện</p></div><div class="card">{BD.tui(mk())}<p class="cap">Trên túi bánh</p></div></div>
<div class="g g2" style="margin-top:18px"><div class="card">{BD.lockup(mk())}</div><div class="card d">{BD.lockup(mk(K), K, K)}</div></div>
<div class="card" style="margin-top:18px"><div class="sm">{small}</div><p class="cap">Cỡ nhỏ 20 · 28 · 40 · 64 px</p></div></section>"""


def page():
    css = C.CSS + ".card svg{display:block;width:100%;height:auto}.sm{display:flex;gap:18px;align-items:end}.sm svg{width:auto!important}.hm{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.verdict{max-width:1200px;margin:56px auto 0;padding:0 20px}"
    secs = "".join(card(*b) for b in R.BIEN_THE)
    toc = "".join(f'<a href="#{k}">{n.split(" · ")[0]}</a>' for k, n, _ in R.BIEN_THE)
    hero = "".join(R.svg(R.van(**o), 120) for k, n, o in R.BIEN_THE if k in ("loi-a", "mu-a", "mu-tam"))
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vân tay cách điệu</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Giữ vân tay, lồng dấu riêng</div><h1>Vân tay An Tâm</h1>
<p>Giữ nguyên dấu vân tay đang dùng (cùng nét, cùng dáng). Chỉ lồng thêm chi tiết riêng: chữ A ở lõi, dấu mũ của font, chấm tâm – để dấu tay này chỉ có thể là của An Tâm.</p></div>
<div class="card hm">{hero}</div></div></header><nav class="toc">{toc}</nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>4 · Mũ vân + lõi A</b>: giữ trọn hình vân tay, nhưng ghép lại đọc ra chữ <b>Â</b> – dấu mũ vân tay là nét riêng đã có trong font, chữ A là chữ đầu thương hiệu. Logo, font và biểu tượng thành một hệ.</p>
<p>Nếu muốn nhẹ nhàng, gần bản cũ nhất: <b>3 · Chấm tâm</b>. Ở cỡ rất nhỏ (dưới 24 px) nên dùng bản rút gọn ít vân hơn – sẽ làm khi chốt.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Chọn biến thể nào?</h2></div></body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

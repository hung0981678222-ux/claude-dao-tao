"""Trang 4 kiểu chữ "an tâm" cá nhân hoá (hướng Trẻ & Sang). Chạy: python3 build_chu_rieng.py OUT.html"""
import sys

import build_tre as B
import chu_rieng as R
import logo_tre as T

CH, CH2, KEM, HONG, BO, DEN = T.CHERRY, T.CHERRY2, T.KEM, T.HONG, T.BO, T.DEN

KIEU = [
    ("tron", "Bánh tròn", "Chữ a vẽ lại thành chiếc đĩa bánh tròn trịa, lòng chữ có ba đốm nướng nhỏ. Chữ t vát góc trên. Nhìn như hai chiếc bánh đứng trong tên.",
     ["Dễ thương, dễ nhớ", "Rõ là bánh", "Hợp linh vật, sticker"]),
    ("dao", "Nét dao", "Đầu nét và chân chữ cắt vát như nhát dao thái thịt doner. Gọn, sắc, hiện đại, có chút cá tính đường phố.",
     ["Sắc sảo, hiện đại", "Gợi dao thái doner", "Hợp biển hiệu, áo"]),
    ("sot", "Sốt chảy", "Sốt phô mai màu bơ chảy xuống từ chân chữ a, t, m. Trẻ, vui, nhìn là thèm.",
     ["Gây thèm ăn", "Trẻ, vui nhất", "Hợp mạng xã hội, ly, hộp"]),
    ("khuon", "Khuôn in", "Khe hở kiểu chữ in khuôn lên thùng hàng. Gợi hàng làm sẵn, giao tận nơi, bán sỉ. Hiện đại, gọn gàng.",
     ["Chuyên nghiệp, sạch", "Gợi giao hàng, bán sỉ", "Hợp thùng, túi, xe giao"]),
]

CSS = """
.kv{padding-block:72px;border-top:1px solid var(--line)}
.kv .hd{display:grid;grid-template-columns:auto 1fr;gap:24px;align-items:end}
.kv .n{font:800 110px/.8 var(--f);letter-spacing:-.06em;color:var(--ch)}
.kv h3{font:800 40px/1 var(--f);letter-spacing:-.04em}
.kv p.d{color:var(--xam);max-width:62ch;margin-top:10px}
.kv .grid{display:grid;grid-template-columns:1.4fr 1fr;gap:16px;margin-top:28px}
.kv .t{border-radius:32px;display:grid;place-items:center;padding:56px 40px}
.kv .t > svg{width:100%;max-width:620px;height:auto;display:block}
.kv .col{display:grid;grid-template-rows:1fr auto;gap:16px}
.kv .tags{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.kv .tags span{font:600 12px/1 var(--f);padding:9px 14px;border-radius:999px;background:var(--den);color:var(--kem)}
.kv .mk2{border-radius:32px;overflow:hidden}
.kv .mk2 > svg{display:block;width:100%;height:auto}
.cmp{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:40px}
.cmp div{border-radius:24px;background:var(--ch);padding:22px 18px;display:flex;flex-direction:column;gap:10px}
.cmp div > svg{width:100%;height:auto;display:block}
.cmp b{color:var(--kem);font:800 15px/1 var(--f)}
@media (max-width:900px){.kv .grid,.cmp{grid-template-columns:1fr}.kv .n{font-size:72px}}
"""


def cup(svg_word, uid):
    w = svg_word.replace("<svg ", '<svg x="80" y="250" width="200" height="110" ', 1)
    return f"""<svg viewBox="0 0 600 520" role="img" aria-label="Ly và túi">
<rect width="600" height="520" fill="{HONG}"/><circle cx="470" cy="120" r="110" fill="{BO}"/>
<ellipse cx="180" cy="480" rx="110" ry="12" fill="#000" opacity=".12"/>
<path d="M80,130 H280 L256,470 H104 Z" fill="{CH}"/><rect x="68" y="108" width="224" height="32" rx="12" fill="{DEN}"/>
{w}
<ellipse cx="440" cy="480" rx="120" ry="12" fill="#000" opacity=".12"/>
<path d="M360,250 C360,190 520,190 520,250" fill="none" stroke="{DEN}" stroke-width="10" stroke-linecap="round"/>
<rect x="330" y="250" width="220" height="225" rx="10" fill="{KEM}"/>
{R.svg(uid, CH, BO, KEM).replace("<svg ", '<svg x="350" y="320" width="180" height="96" ', 1)}
</svg>"""


def page():
    secs = ""
    cmp = ""
    for i, (k, name, desc, tags) in enumerate(KIEU, 1):
        red = R.svg(k, KEM, BO, CH)
        kem = R.svg(k, CH, BO, KEM)
        cmp += f"<div>{red}<b>{i} · {name}</b></div>"
        secs += f"""<section class="kv"><div class="w">
 <div class="hd"><span class="n">{i}</span><div><h3>{name}</h3><p class="d">{desc}</p></div></div>
 <div class="grid"><div class="t" style="background:{CH}">{red}</div>
  <div class="col"><div class="t" style="background:#fff;border:1px solid var(--line)">{kem}</div><div class="mk2">{cup(red, k)}</div></div></div>
 <div class="tags">{"".join(f"<span>{t}</span>" for t in tags)}</div>
</div></section>"""
    return f"""<title>Chữ an tâm riêng</title>
<style>{B.fontfaces()}
{B.CSS}{CSS}</style>
<section style="padding-block:64px 24px"><div class="w">
 <span class="chip"><i></i>Hướng Trẻ &amp; Sang · Chữ riêng</span>
 <h2>Bốn kiểu chữ <span>chỉ An Tâm có</span></h2>
 <p class="lead">Giữ khung chữ tròn khít và chiếc bánh làm dấu mũ của hướng Trẻ &amp; Sang. Mỗi kiểu thêm một chi tiết vẽ riêng để chữ có tính cách, không lẫn với font có sẵn.</p>
 <div class="cmp">{cmp}</div>
</div></section>
{secs}
<footer><div class="w"><div>{R.svg("tron", KEM, BO, CH).replace("<svg ", '<svg class="lg" ', 1)}<p>Anh chị chọn kiểu 1, 2, 3 hay 4, hoặc ghép (ví dụ chữ a Bánh tròn với sốt chảy). Chọn xong tôi đưa kiểu chữ đó vào toàn bộ bộ nhận diện.</p></div>
<div class="ct">0348.635.222<br>antamfoods.com</div></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

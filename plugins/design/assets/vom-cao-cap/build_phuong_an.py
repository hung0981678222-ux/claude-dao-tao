"""Trang so sánh 3 phương án logo. Chạy: python3 build_phuong_an.py OUT.html"""
import sys

from build_cam_nang import fontfaces, ill
from phuong_an import OUT

OPTS = [
    ("1", "Canh giữa", "pa1", "ẨM THỰC canh giữa phía trên, chữ nhỏ giãn thoáng. Dưới chân có dòng BÁNH TORTILLAS · DONER KEBAB kẹp giữa hai nét vàng.",
     ["Cân đối, dễ đặt lên biển hiệu và bao bì.", "Dòng mô tả nói thẳng sản phẩm.", "Dấu mũ là chiếc bánh gập đôi có đốm nướng."], "Đơn giản, dễ dùng nhất"),
    ("2", "Nhãn trên AN T", "pa2", "ẨM THỰC nằm trong một nhãn bo tròn, đặt trên đầu chữ AN T, ngang hàng với chiếc bánh trên chữ Â. Dòng mô tả dưới chân, căn trái.",
     ["Giữ đúng vị trí ẨM THỰC trên chữ AN T như anh chị muốn.", "Nhãn đỏ giống tem trên bao bì thực phẩm.", "Dòng trên cùng cân: nhãn bên trái, bánh bên phải."], "Đúng ý đặt ẨM THỰC trên AN T"),
    ("3", "Biểu tượng taco", "pa3", "Bên trái là khung vòm chứa chiếc taco nghiêng: vỏ bánh vàng có đốm nướng, thịt, rau, cà chua. Bên phải là ẨM THỰC, AN TÂM và dòng mô tả.",
     ["Nhìn biểu tượng biết ngay là đồ ăn.", "Biểu tượng tách riêng làm ảnh đại diện, tem, biển nhỏ.", "Màu món ăn tạo cảm giác ngon, tươi."], "Rõ ngành thực phẩm nhất"),
]

CSS = """
:root{--red:#A8160F;--ivory:#F6F1E8;--paper:#FBF8F2;--ink:#1F1714;--gold:#C39443;--muted:#6E5F56;--line:#DCD0BD;
--f:'BVP','Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--ivory);color:var(--ink);font:400 16px/1.6 var(--f);-webkit-font-smoothing:antialiased}
.w{max-width:1200px;margin:0 auto;padding-inline:40px}
header{padding-block:72px 48px;border-bottom:1px solid var(--line)}
.eyebrow{font:500 11px/1 var(--f);letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
h1{font:300 clamp(36px,5vw,60px)/1.05 var(--f);letter-spacing:-.035em;margin-top:18px;max-width:20ch;text-wrap:balance}
h1 b{font-weight:600;color:var(--red)}
.intro{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}
.intro div{border-top:1px solid var(--ink);padding-top:12px;font-size:14px;color:var(--muted)}
.intro b{display:block;color:var(--ink);font-weight:600;font-size:15px}
section{padding-block:80px;border-bottom:1px solid var(--line)}
.oh{display:grid;grid-template-columns:auto 1fr auto;gap:28px;align-items:end;margin-bottom:36px}
.num{font:300 96px/.8 var(--f);color:var(--red);letter-spacing:-.05em}
.oh h2{font:600 30px/1.1 var(--f);letter-spacing:-.02em}
.oh p{color:var(--muted);max-width:62ch;margin-top:8px;font-size:15px}
.tag{font:600 11px/1 var(--f);letter-spacing:.16em;text-transform:uppercase;background:var(--ink);color:var(--ivory);padding:10px 14px;border-radius:999px;white-space:nowrap}
.grid{display:grid;grid-template-columns:7fr 5fr;gap:16px}
.big{background:var(--paper);border:1px solid var(--line);display:grid;place-items:center;padding:72px 48px;min-height:360px}
.big svg{width:min(100%,560px);height:auto;display:block}
.col{display:grid;grid-template-rows:1fr auto;gap:16px}
.onred{background:var(--red);display:grid;place-items:center;padding:40px 32px}
.onred svg{width:min(100%,380px);height:auto;display:block}
.small{background:#fff;border:1px solid var(--line);display:flex;align-items:end;justify-content:space-around;gap:16px;padding:24px 20px 18px;flex-wrap:wrap}
.small div{display:flex;flex-direction:column;align-items:center;gap:10px;font:500 11px/1 var(--f);color:var(--muted)}
.small svg{height:auto;display:block}
.apps{display:grid;grid-template-columns:2fr 1fr 1fr;gap:16px;margin-top:16px}
.sign{background:#2A211E;padding:28px 24px 0;display:flex;flex-direction:column;gap:0}
.sign .board{background:var(--red);padding:22px 28px;display:grid;place-items:center;box-shadow:0 18px 30px -18px rgba(0,0,0,.8)}
.sign .board svg{width:min(100%,360px);height:auto;display:block}
.sign .shop{height:64px;display:grid;grid-template-columns:1fr 1.2fr 1fr;gap:14px;padding:14px 16px 0}
.sign .shop i{display:block;background:linear-gradient(#FFE0A8,#E6A355);border-radius:999px 999px 0 0;border:2px solid var(--gold);border-bottom:0}
.sticker{background:linear-gradient(160deg,#D9CDB8,#C7B89E);display:grid;place-items:center;padding:28px}
.sticker .s{background:var(--paper);border-radius:14px;padding:20px 18px;width:100%;display:grid;place-items:center;box-shadow:0 14px 26px -14px rgba(40,20,10,.55)}
.sticker .s svg{width:100%;height:auto;display:block}
.avatar{background:#E9E4DC;display:grid;place-items:center;padding:28px}
.fb{background:#fff;border-radius:16px;padding:16px;width:100%;max-width:220px;box-shadow:0 10px 24px -14px rgba(0,0,0,.35);display:grid;gap:10px;justify-items:center;text-align:center;font-size:12px}
.fb .av{width:96px;aspect-ratio:1;border-radius:50%;overflow:hidden;display:grid;place-items:center}
.fb .av svg{width:62%;height:auto;display:block}.fb .av span svg{width:100%}
.fb b{font-size:14px}
.cap{font:500 11px/1.4 var(--f);letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-top:10px}
ul.pros{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px;padding:0;list-style:none}
ul.pros li{border-top:1px solid var(--ink);padding-top:12px;font-size:14px}
footer{padding-block:56px;font-size:14px;color:var(--muted)}
footer b{color:var(--ink)}
@media (max-width:900px){.w{padding-inline:20px}.intro,.grid,.apps,ul.pros{grid-template-columns:1fr}.oh{grid-template-columns:auto 1fr}.oh .tag{grid-column:1/-1;justify-self:start}.num{font-size:64px}.big{padding:48px 20px;min-height:0}}
"""


def a_mark(fg, hat, bg):
    import logo_cao_cap as L
    from phuong_an import tortilla_hat
    a, w = L.A(0)
    h = tortilla_hat(cx=w / 2, base=-9.6, r=18)
    return (f'<svg viewBox="-20 -34 {w + 40:.0f} 140" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            f'<path fill="{fg}" d="{L.d(a)}"/><path fill="{hat}" d="{L.d(h)}"/></svg>')


def section(n, name, key, desc, pros, tag):
    kem, do = OUT[key + "_kem"], OUT[key + "_do"]
    if key == "pa3":
        av = f'<div class="av" style="background:var(--ivory);padding-top:8px"><span style="width:52%;display:block">{OUT["badge_do"]}</span></div>'
        small = (f'<div><span style="width:200px;display:block">{kem}</span>200 px</div>'
                 f'<div><span style="width:40px;display:block">{OUT["badge_do"]}</span>Biểu tượng 40 px</div>')
    else:
        av = f'<div class="av" style="background:var(--red)">{a_mark("#F6F1E8", "#C39443", "")}</div>'
        small = (f'<div><span style="width:180px;display:block">{kem}</span>180 px</div>'
                 f'<div><span style="width:34px;display:block">{a_mark("#A8160F", "#C39443", "")}</span>Chữ Â 34 px</div>')
    return f"""<section id="pa{n}"><div class="w">
 <div class="oh"><span class="num">{n}</span><div><h2>{name}</h2><p>{desc}</p></div><span class="tag">{tag}</span></div>
 <div class="grid">
  <div class="big">{kem}</div>
  <div class="col"><div class="onred">{do}</div><div class="small">{small}</div></div>
 </div>
 <div class="apps">
  <div><div class="sign"><div class="board">{do}</div><div class="shop"><i></i><i></i><i></i></div></div><p class="cap">Biển hiệu cửa hàng</p></div>
  <div><div class="sticker"><div class="s">{kem}</div></div><p class="cap">Tem dán hộp, túi</p></div>
  <div><div class="avatar"><div class="fb">{av}<b>Ẩm Thực An Tâm</b><span>Bánh tortillas, doner kebab</span></div></div><p class="cap">Ảnh đại diện Facebook, Zalo</p></div>
 </div>
 <ul class="pros">{"".join(f"<li>{p}</li>" for p in pros)}</ul>
</div></section>"""


def page():
    return f"""<title>Phương án logo An Tâm</title>
<style>{fontfaces()}
{CSS}</style>
<header><div class="w">
 <p class="eyebrow">Ẩm Thực An Tâm · Chọn bố cục logo</p>
 <h1>Ba cách đặt chữ, <b>rõ là đồ ăn</b></h1>
 <div class="intro">
  <div><b>Dấu mũ là chiếc bánh</b>Nửa chiếc tortilla gập đôi, thêm đốm nướng để nhìn ra là bánh.</div>
  <div><b>Nói thẳng sản phẩm</b>Cả ba phương án có dòng BÁNH TORTILLAS · DONER KEBAB.</div>
  <div><b>Chữ AN TÂM giữ nguyên</b>Chỉ đổi vị trí ẨM THỰC và cách thể hiện ngành thực phẩm.</div>
 </div>
</div></header>
{"".join(section(*o) for o in OPTS)}
<footer><div class="w"><p><b>Anh chị chọn phương án 1, 2 hoặc 3</b>, hoặc ghép (ví dụ nhãn của phương án 2 với biểu tượng taco của phương án 3). Sau khi chọn, tôi cập nhật toàn bộ cẩm nang và file logo theo phương án đó.</p></div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

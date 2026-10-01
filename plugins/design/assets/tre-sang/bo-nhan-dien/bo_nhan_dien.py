"""Bộ nhận diện tổng thể Ẩm Thực An Tâm (hướng Trẻ & Sang, font An Tâm Sans).
Chạy: python3 bo_nhan_dien.py OUT.html"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "nl2"))

import bac_thang as BT  # noqa: E402
import build_font_page as FP  # noqa: E402
import build_font_page2 as FP2  # noqa: E402
import build_tre as BTR  # noqa: E402
import logo_tre as T  # noqa: E402
import nen_tre as N  # noqa: E402
from mascot4 import be_cuon  # noqa: E402

CH, CH2, KEM, HONG, BO, DEN = T.CHERRY, T.CHERRY2, T.KEM, T.HONG, T.BO, T.DEN


def lg(svg, cls="lg", style=""):
    return svg.replace("<svg ", f'<svg class="{cls}" style="{style}" ', 1)


def fill(svg):
    return svg.replace("<svg ", '<svg style="width:100%;height:100%;display:block" ', 1)


def cmyk(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    k = 1 - max(r, g, b)
    c, m, y = ((1 - v - k) / (1 - k) for v in (r, g, b)) if k < 1 else (0, 0, 0)
    return " ".join(str(round(v * 100)) for v in (c, m, y, k))


def rgb(h):
    return " ".join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))


CSS = """
:root{--f:'An Tam Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
.cover{background:var(--ch);color:var(--kem);overflow:hidden;padding-block:28px 0;position:relative}
.cover .top{display:flex;justify-content:space-between;font:800 12px/1 var(--f);letter-spacing:.14em}
.cover .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:24px;align-items:center;padding-block:56px 64px}
.cover .lg{max-width:640px}
.cover h1{font:400 clamp(26px,3vw,40px)/1.2 var(--f);margin-top:28px;letter-spacing:-.02em}
.cover h1 b{font-weight:800;color:var(--bo)}
.cover .st svg{width:100%;height:auto;display:block}
.toc{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid rgba(255,244,232,.3)}
.toc a{color:var(--kem);text-decoration:none;font:800 14px/1.3 var(--f);padding:16px 14px 18px 0;border-bottom:1px solid rgba(255,244,232,.3)}
.toc a span{display:block;font-weight:400;opacity:.7;font-size:12px}
.toc a:hover{color:var(--bo)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:48px}
.card{background:#fff;border:1px solid var(--line);border-radius:32px;padding:32px}
.card h3{font:800 26px/1.15 var(--f);letter-spacing:-.03em;margin-bottom:10px}
.card p,.card li{color:var(--xam);font-size:16px}
.tag-line{font:800 clamp(60px,9vw,140px)/.9 var(--f);letter-spacing:-.06em;color:var(--ch);margin-top:36px}
.tag-line span{color:var(--den)}
.traits4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:24px}
.traits4 div{border-radius:28px;padding:24px;min-height:200px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}
.traits4 b{font:800 28px/1 var(--f);letter-spacing:-.03em}
.traits4 p{font-size:14px;opacity:.85}
.voice{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}
.voice ul{list-style:none;padding:0;display:grid;gap:8px;margin-top:6px}
.voice li{padding-left:24px;position:relative}
.voice .ok li::before{content:"✓";position:absolute;left:0;color:#2F7D24;font-weight:800}
.voice .no li{text-decoration:line-through;text-decoration-color:rgba(181,18,27,.5)}
.voice .no li::before{content:"✕";position:absolute;left:0;color:var(--ch);font-weight:800}
.rulebox{display:grid;grid-template-columns:1.2fr 1fr;gap:16px;margin-top:16px}
.clear{background:#fff;border:1px solid var(--line);border-radius:32px;display:grid;place-items:center;padding:48px}
.clear .z{position:relative;padding:40px;background:repeating-linear-gradient(45deg,rgba(181,18,27,.09) 0 7px,transparent 7px 14px);border-radius:16px}
.clear .z::before{content:"";position:absolute;inset:40px;background:#fff}
.clear .z svg{position:relative;width:min(100%,380px);height:auto;display:block}
.mins{background:#fff;border:1px solid var(--line);border-radius:32px;display:flex;gap:30px;align-items:end;justify-content:center;padding:40px;flex-wrap:wrap}
.mins div{display:flex;flex-direction:column;gap:10px;align-items:center;font:400 12px/1.4 var(--f);color:var(--xam);text-align:center}
.dont{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:16px}
.dont figure{background:#fff;border:1px solid var(--line);border-radius:24px;aspect-ratio:4/3;display:grid;place-items:center;padding:24px 24px 44px;position:relative;overflow:hidden}
.dont figure svg{width:80%;height:auto}
.dont figcaption{position:absolute;left:16px;bottom:12px;font:800 13px/1 var(--f);display:flex;gap:8px;align-items:center}
.dont figcaption::before{content:"✕";display:grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--ch);color:#fff;font-size:11px}
.ratio{display:flex;height:26px;border-radius:999px;overflow:hidden;margin-top:24px;border:1px solid var(--line)}
.sw5{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:40px}
.sw5 div{display:flex;flex-direction:column;gap:6px;font:400 13px/1.5 var(--f);color:var(--xam);font-variant-numeric:tabular-nums}
.sw5 i{display:block;aspect-ratio:1;border-radius:50%;margin-bottom:6px}
.sw5 b{font:800 20px/1.1 var(--f);color:var(--den)}
.fam4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px}
.fam4 div{border-radius:28px;padding:24px;min-height:240px;display:flex;flex-direction:column;justify-content:space-between}
.fam4 .s{font-size:76px;line-height:.95;letter-spacing:-.04em}
.fam4 b{font:800 12px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;opacity:.75}
.hier div{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:baseline;padding:16px 0;border-bottom:1px solid var(--line)}
.hier small{font:400 12px/1.4 var(--f);color:var(--xam);text-align:right;white-space:nowrap}
.stairs3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.stairs3 > div{border-radius:32px;display:grid;place-items:center;padding:28px;min-height:440px}
.stairs3 svg{width:100%;height:auto;max-height:420px}
.srules{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:20px}
.srules div{border-top:2px solid var(--den);padding-top:10px;font-size:14px;color:var(--xam)}
.srules b{display:block;color:var(--den);font-weight:800;font-size:16px}
.bgs{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px}
.bgs figure{display:flex;flex-direction:column;gap:10px}
.bgs .th{border-radius:22px;overflow:hidden;aspect-ratio:16/9}
.bgs .sz{display:grid;grid-template-columns:1fr .56fr .56fr;gap:8px;align-items:end}
.bgs .sz span{border-radius:10px;overflow:hidden;display:block}
.bgs figcaption{font-size:13px;color:var(--xam)}
.bgs figcaption b{display:block;color:var(--den);font:800 17px/1.2 var(--f)}
.lines{display:grid;gap:10px;margin-top:40px}
.lines div{background:#fff;border:1px solid var(--line);border-radius:18px;padding:12px 18px;display:grid;grid-template-columns:140px 1fr;gap:16px;align-items:center;font:800 14px/1 var(--f)}
.lines svg{width:100%;height:auto;display:block}
.prod4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px}
.prod4 div{border-radius:28px;aspect-ratio:1;display:grid;place-items:center;padding:14%}
.prod4 img{width:100%}
.masc3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:16px}
.masc3 div{border-radius:28px;display:grid;place-items:center;padding:28px}
.masc3 svg{width:min(100%,220px);height:auto}
.story{border-radius:28px;overflow:hidden;position:relative;aspect-ratio:9/16}
.story .bg{position:absolute;inset:0}
.story .in{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:space-between;padding:58px 22px 22px}
.story .in svg.lg{width:52%}
.story .in svg.st{width:100%;height:auto}
.story .in p{font:800 14px/1.3 var(--f);color:var(--kem)}
@media (max-width:900px){.cover .grid,.two,.voice,.rulebox{grid-template-columns:1fr}.toc{grid-template-columns:1fr 1fr}
 .traits4,.dont,.sw5,.fam4,.srules,.bgs,.prod4{grid-template-columns:1fr 1fr}.stairs3,.masc3{grid-template-columns:1fr}.fam4 .s{font-size:56px}}
@media (max-width:480px){.traits4,.dont,.sw5,.fam4,.srules,.bgs,.prod4{grid-template-columns:1fr}.lines div{grid-template-columns:1fr}}
"""


def sec(id_, chip, title, lead, body, bg=""):
    st = f' style="background:{bg}"' if bg else ""
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<section id="{id_}"{st}><div class="w"><span class="chip"><i></i>{chip}</span><h2>{title}</h2>{lead_html}{body}</div></section>'


def page():
    W = BTR
    stair_cover = BT.stairs(["ăn là", "an tâm"], KEM, hi=BO, hi_idx=(1,))
    st1 = BT.stairs(["ăn là", "an tâm"], KEM, hi=BO, hi_idx=(1,))
    st2 = BT.stairs(["bữa", "nhẹ", "văn", "phòng"], CH, hi=DEN, hi_idx=(3,), F=.6, H=170)
    st3 = BT.stairs(["tận", "tâm"], BO, style="NetDut", hi=KEM, hi_idx=(1,))
    toc = "".join(f'<a href="#{i}">{n}<span>{d}</span></a>' for i, n, d in [
        ("nen-tang", "01 Nền tảng", "Câu chuyện, tính cách"), ("logo", "02 Logo", "Hệ logo, quy tắc"), ("mau", "03 Màu", "5 màu, tỉ lệ"),
        ("chu", "04 Chữ", "An Tâm Sans"), ("bac-thang", "05 Chữ bậc thang", "Dựng, quy tắc"), ("nen", "06 Nền", "8 nền, 3 cỡ"),
        ("net", "07 Nét đứt", "6 đường"), ("hinh", "08 Hình", "Minh hoạ, linh vật"), ("ung-dung", "09 Ứng dụng", "Bao bì, cửa hàng"), ("lien-he", "10 Liên hệ", "Thông tin")])

    nen_tang = sec("nen-tang", "01 · Nền tảng", "Một chiếc bánh, <span>làm tử tế</span>",
                   "Ẩm Thực An Tâm làm bánh tortillas và doner kebab cho văn phòng, cửa hàng và đối tác nhượng quyền ở TP.HCM. Thương hiệu hứa một điều đơn giản: ăn là an tâm.",
                   f"""<div class="tag-line">ăn là <span>an tâm.</span></div>
<div class="traits4">
 <div style="background:{CH};color:{KEM}"><b>Tận tâm</b><p>Chăm từng chiếc bánh như làm cho người nhà.</p></div>
 <div style="background:{BO}"><b>Đúng hẹn</b><p>Giao đúng giờ, đúng số lượng đã hứa.</p></div>
 <div style="background:{HONG}"><b>Rõ ràng</b><p>Giá minh bạch, báo giá bằng văn bản.</p></div>
 <div style="background:{DEN};color:{KEM}"><b>Vui vẻ</b><p>Nói chuyện gần gũi, như người quen.</p></div>
</div>
<div class="voice">
 <div class="card ok"><h3>Nói thế này</h3><ul><li>Bánh vừa ra lò, anh chị đặt liền nha.</li><li>Đơn đang trên đường, sắp tới rồi ạ.</li><li>Gửi báo giá trong ngày.</li></ul></div>
 <div class="card no"><h3>Không nói thế này</h3><ul><li>Chất lượng số 1 thị trường.</li><li>Ưu đãi khủng, rẻ nhất.</li><li>Cam kết lợi nhuận nhượng quyền.</li></ul></div>
</div>
<div class="two" style="margin-top:16px"><div class="card"><h3>Khẩu hiệu công ty</h3><p>Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm. Dùng trên hồ sơ năng lực, báo giá, tài liệu nhượng quyền.</p></div>
<div class="card"><h3>Câu thương hiệu</h3><p>"ăn là an tâm." Dùng trên bao bì, bài đăng, biển hiệu. Viết thường, có dấu chấm cuối.</p></div></div>""", "#fff")

    donts = "".join(f'<figure>{W.WM_CH.replace("<svg ", f"<svg style={chr(34)}{s}{chr(34)} ", 1)}<figcaption>{t}</figcaption></figure>' for t, s in [
        ("Kéo méo", "transform:scaleX(1.45)"), ("Xoay nghiêng", "transform:rotate(-16deg)"), ("Đổi màu", "filter:hue-rotate(150deg)"), ("Thêm hiệu ứng", "filter:drop-shadow(6px 6px 0 #2F7D24)")])
    logo = sec("logo", "02 · Logo", "Gọn, tròn, <span>có chiếc bánh</span>",
               "Chữ an tâm viết thường, dấu mũ là chiếc bánh gập đôi màu bơ. ẨM THỰC nằm trên, dòng sản phẩm nằm dưới. Biểu tượng là chữ â trong hình tròn.",
               f"""<div class="bento">
 <div class="b c8 bg-kem">{lg(W.WM_CH)}<span class="cap">Logo chính</span></div>
 <div class="b c4 bg-hong">{lg(W.MARK, "lg m")}<span class="cap">Biểu tượng</span></div>
 <div class="b c4 bg-den">{lg(W.MARK_SQ, "lg m")}<span class="cap">Ô ứng dụng</span></div>
 <div class="b c8 bg-ch">{lg(W.WM_KEM)}<span class="cap">Trên nền cherry</span></div>
 <div class="b c6 bg-bo">{lg(W.WM_GON_CH)}<span class="cap">Bản gọn</span></div>
 <div class="b c6 bg-kem">{lg(W.WM_DEN)}<span class="cap">Một màu</span></div>
</div>
<div class="rulebox"><div class="clear"><div class="z">{W.WM_CH}</div></div>
 <div class="mins"><div>{lg(W.WM_CH, "x", "width:140px")}Logo chính<br>nhỏ nhất 30 mm, 140 px</div><div>{lg(W.WM_GON_CH, "x", "width:90px")}Bản gọn<br>nhỏ nhất 18 mm, 90 px</div><div>{lg(W.MARK, "x", "width:32px")}Biểu tượng<br>nhỏ nhất 32 px</div>
 <p style="font-size:13px;color:var(--xam);width:100%;text-align:center">Vùng trống quanh logo bằng chiều cao chữ a.</p></div></div>
<div class="dont">{donts}</div>""")

    cols = [(CH, "Cherry", "Màu chính"), (KEM, "Kem", "Nền"), (DEN, "Đen", "Chữ"), (HONG, "Hồng phấn", "Điểm nhấn"), (BO, "Vàng bơ", "Chiếc bánh")]
    sw = "".join(f'<div><i style="background:{c};{"border:1px solid var(--line)" if c == KEM else ""}"></i><b>{n}</b>{u}<br>HEX {c}<br>RGB {rgb(c)}<br>CMYK {cmyk(c)}</div>' for c, n, u in cols)
    mau = sec("mau", "03 · Màu", "Cherry dẫn đầu, <span>chấm màu vui</span>",
              "Cherry và kem cho cảm giác sang. Hồng phấn và vàng bơ là chấm màu trẻ, dùng ít như topping. Mã CMYK là quy đổi tham khảo, cần in thử.",
              f'<div class="ratio"><span style="flex:45;background:{CH}"></span><span style="flex:30;background:{KEM}"></span><span style="flex:12;background:{DEN}"></span><span style="flex:8;background:{HONG}"></span><span style="flex:5;background:{BO}"></span></div>'
              f'<p style="font-size:13px;color:var(--xam);margin-top:8px">Tỉ lệ diện tích gợi ý: cherry 45, kem 30, đen 12, hồng 8, bơ 5.</p><div class="sw5">{sw}</div>', "#fff")

    chu = sec("chu", "04 · Chữ", "Một họ chữ, <span>An Tâm Sans</span>",
              "Font riêng của thương hiệu, 4 kiểu, đủ dấu tiếng Việt. Dấu mũ là chiếc bánh, nét có vết cắt như nhát dao.",
              f"""<div class="fam4">
 <div style="background:{CH};color:{KEM}"><b>Đậm</b><span class="s" style="font-weight:800">âm</span><small>Tên, tiêu đề</small></div>
 <div style="background:#fff;border:1px solid var(--line)"><b>Thường</b><span class="s" style="font-weight:400">âm</span><small>Nội dung</small></div>
 <div style="background:{BO}"><b>Nét Đứt</b><span class="s f-nd" style="color:{CH}">âm</span><small>Tiêu đề lớn, tem</small></div>
 <div style="background:{DEN};color:{KEM}"><b>Đốm Nướng</b><span class="s f-dn" style="color:{BO}">âm</span><small>Bao bì, biển hiệu</small></div>
</div>
<div class="card hier" style="margin-top:16px">
 <div><span style="font:800 56px/1 var(--f);letter-spacing:-.05em;color:var(--ch)">gập đôi là ngon.</span><small>Tiêu đề · Đậm · khít −5%</small></div>
 <div><span style="font:800 26px/1.2 var(--f);letter-spacing:-.02em">Bánh tortillas giao tận văn phòng</span><small>Tiêu đề phụ · Đậm</small></div>
 <div><span style="font:800 12px/1 var(--f);letter-spacing:.16em">NHƯỢNG QUYỀN CỬA HÀNG</span><small>Nhãn · Đậm · giãn 16%</small></div>
 <div><span style="font:400 17px/1.6 var(--f)">Bữa nhẹ cho nhân viên văn phòng. Đặt qua hotline 0348.635.222.</span><small>Nội dung · Thường</small></div>
</div>""", "")

    bac = sec("bac-thang", "05 · Chữ bậc thang", "Chữ leo <span>bậc thang</span>",
              "Chữ dựng bằng An Tâm Sans trên góc 30 độ: dòng chẵn nằm ngang như mặt bậc, dòng lẻ đứng như thành bậc. Dòng cuối đổi màu để nhấn.",
              f"""<div class="stairs3"><div style="background:{CH}">{st1}</div><div style="background:{BO}">{st2}</div><div style="background:{DEN}">{st3}</div></div>
<div class="srules"><div><b>2 đến 6 dòng</b>Mỗi dòng 1 đến 2 từ ngắn.</div><div><b>Dòng cuối đổi màu</b>Màu nhấn: bơ trên đỏ, đen trên bơ.</div><div><b>Một lần mỗi ấn phẩm</b>Không đặt hai khối bậc thang cạnh nhau.</div><div><b>Nền gợi ý</b>Cherry, vàng bơ, đen, hoặc nền Bậc thang.</div></div>""", "#fff")

    bgs = ""
    for k, (name, desc, fn) in N.NEN.items():
        bgs += (f'<figure><div class="th">{fill(fn(1920, 1080))}</div>'
                f'<div class="sz"><span style="aspect-ratio:16/9">{fill(fn(1920, 1080))}</span><span style="aspect-ratio:4/5">{fill(fn(1080, 1350))}</span><span style="aspect-ratio:9/16">{fill(fn(1080, 1920))}</span></div>'
                f'<figcaption><b>{name}</b>{desc}</figcaption></figure>')
    nen = sec("nen", "06 · Nền thương hiệu", "Tám nền, <span>ba cỡ</span>",
              "Mỗi nền có 3 cỡ: ngang 1920×1080 (màn hình, slide), bài đăng 1080×1350, dọc 1080×1920 (story, standee). File SVG phóng to không vỡ.",
              f'<div class="bgs">{bgs}</div>')

    lines = "".join(f"<div>{name}{fn()}</div>" for k, (name, fn) in N.NET.items())
    net = sec("net", "07 · Đường nét đứt", "Đường chỉ <span>của An Tâm</span>",
              "Dùng làm đường viền, đường phân cách, đường cắt trên tem, phiếu. Mỗi ấn phẩm chọn một đường.", f'<div class="lines">{lines}</div>', "#fff")

    prods = "".join(f'<div style="background:{bg}"><img src="{BTR.ill(n)}" alt="{t}"></div>' for n, t, bg in [
        ("banh-tortillas", "Bánh tortillas", BO), ("taco", "Taco", HONG), ("doner-tru-quay", "Doner kebab", "#fff"), ("doner-cuon", "Doner cuộn", CH)])
    hinh = sec("hinh", "08 · Hình", "Minh hoạ và <span>Bé Cuộn</span>",
               "Tranh sản phẩm vẽ phẳng đặt trên ô màu. Linh vật Bé Cuộn dùng cho mạng xã hội, sticker Zalo, cửa hàng: mỗi ấn phẩm tối đa một linh vật.",
               f"""<div class="prod4">{prods}</div>
<div class="masc3"><div style="background:{BO}">{be_cuon("m1", "cuoi", "chao")}</div><div style="background:{HONG}">{be_cuon("m2", "nhay", "like")}</div><div style="background:{DEN}">{be_cuon("m3", "mat_tim", "tim")}</div></div>""")

    story = lambda bgk, txt, stair: (f'<div class="story"><div class="bg">{fill(N.NEN[bgk][2](1080, 1920))}</div>'  # noqa: E731
                                     f'<div class="in">{lg(W.WM_GON_KEM if bgk != "sticker" else W.WM_GON_CH)}{stair.replace("<svg ", "<svg class=" + chr(34) + "st" + chr(34) + " ", 1)}<p style="color:{DEN if bgk == "sticker" else KEM}">{txt}</p></div></div>')
    ung = sec("ung-dung", "09 · Ứng dụng", "Từ ly nước <span>tới biển neon</span>", "Chỗ ghi [Cần điền], [giá] chờ thông tin thật từ công ty.",
              f"""<div class="bento apps">
 <div class="b c8" style="min-height:0"><span class="cap">Biển neon</span>{W.neon()}</div>
 <div class="b c4" style="min-height:0"><span class="cap">Story bậc thang</span>{story("bac-thang", "antamfoods.com · 0348.635.222", BT.stairs(["ăn là", "an tâm"], KEM, hi=BO, hi_idx=(1,)))}</div>
 <div class="b c4" style="min-height:0"><span class="cap">Ly và hộp</span>{W.cup()}</div>
 <div class="b c4" style="min-height:0"><span class="cap">Túi vải</span>{W.tote()}</div>
 <div class="b c4" style="min-height:0"><span class="cap">Đặt món</span>{W.phone()}</div>
 <div class="b c4" style="min-height:0"><span class="cap">Story khuyến mãi</span>{story("sticker", "Giao tận văn phòng", BT.stairs(["bánh", "nóng", "giao", "liền"], CH, hi=DEN, hi_idx=(3,), F=.6, H=170))}</div>
 <div class="b c8" style="min-height:0;background:{KEM}"><span class="cap">Hộp giao hàng</span>{W.box()}</div>
 <div class="b c12" style="min-height:0"><span class="cap">Bài đăng</span>{W.post()}</div>
</div>""", "#fff")

    h = f"""<title>Bộ nhận diện An Tâm</title>
<style>{FP.faces()}
{FP2.faces2()}
{BTR.CSS}{FP2.CSS2}{CSS}</style>
<header class="cover"><div class="w">
 <div class="top"><span>ẨM THỰC AN TÂM</span><span>BỘ NHẬN DIỆN THƯƠNG HIỆU · BẢN ĐỀ XUẤT</span></div>
 <div class="grid"><div>{lg(W.WM_KEM)}<h1>Bánh tortillas và doner kebab. <b>Ăn là an tâm.</b></h1></div><div class="st">{stair_cover}</div></div>
 <nav class="toc" aria-label="Mục lục">{toc}</nav>
</div></header>
{nen_tang}{logo}{mau}{chu}{bac}{nen}{net}{hinh}{ung}
<footer id="lien-he"><div class="w"><div>{lg(W.WM_KEM)}<p>Công ty TNHH SX-TM Ẩm Thực An Tâm · TP. Hồ Chí Minh. Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm. Bản đề xuất, chờ công ty duyệt; logo gốc vẫn là logo chính thức cho tới khi duyệt. Font An Tâm Sans dựng từ Lexend (SIL OFL 1.1).</p></div>
<div class="ct">0348.635.222<br>antamfoods.com</div></div></footer>
"""
    return h.replace("px Lexend", "px 'An Tam Sans'")


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())

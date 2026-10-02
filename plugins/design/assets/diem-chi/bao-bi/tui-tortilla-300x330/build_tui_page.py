"""Trang trình bày túi bánh tortilla 300 × 330 mm. Chạy sau tui_tortilla.py: python3 build_tui_page.py OUTDIR"""
import os
import sys

import build_chuan as C
import tui_tortilla as T

SPEC = [
    ("Khổ thành phẩm", "300 × 330 mm (rộng × cao), mỗi mặt"),
    ("Tràn lề", "3 mm mỗi cạnh – file in 306 × 336 mm"),
    ("Kiểu túi (giả định)", "Túi 3 biên hàn, miệng zip – đối chiếu khuôn của nhà in"),
    ("Biên hàn", "10 mm hông & đáy; zip cách mép trên 35 mm; vết xé 25 mm"),
    ("Vùng an toàn chữ", "Cách mép cắt 15 mm, nằm dưới zip"),
    ("Cửa sổ", "Tròn Ø108 mm, tâm cách mép trên 184 mm – không in mực, không lót trắng"),
    ("Màu", "Đỏ An Tâm #D2141E · Đỏ sẫm #8F0D14 · Kem #FFF6EA · Mực #231716 · lót trắng dưới toàn bộ trừ cửa sổ"),
    ("Chữ", "An Tam Tron Banh – đã chuyển nét, nhà in không cần cài font"),
    ("Vừa bánh", "Bánh Ø 10 inch (≈ 254 mm) vừa lòng túi 280 mm; bánh 12 inch (≈ 305 mm) không vừa"),
]
CAN = ["Thành phần, thông tin dị ứng theo công thức thật", "Khối lượng tịnh, số chiếc, cỡ bánh", "Điều kiện bảo quản, thời gian dùng sau khi mở, thời gian làm nóng",
       "Xuất xứ, địa chỉ công ty", "Mã vạch EAN-13 thật (vạch trong file chỉ là chỗ giữ vị trí) và mã QR", "NSX / HSD / số lô in phun tại ô trống ở mặt sau khi đóng gói"]


def run(out):
    def fig(src, cap, cls=""):
        return f'<figure class="it {cls}"><a href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{cap}"></a><figcaption>{cap}</figcaption></figure>'
    spec = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in SPEC)
    legend = "".join(f'<li><i style="background:{c}"></i>{t}</li>' for c, t in T.chu_thich())
    can = "".join(f"<li>{t}</li>" for t in CAN)
    dl = [("tui-tortilla-300x330-in.pdf", "PDF in 2 trang (306 × 336 mm, có tràn lề)"), ("tui-tortilla-mat-truoc.svg", "SVG mặt trước – mở bằng Illustrator"),
          ("tui-tortilla-mat-sau.svg", "SVG mặt sau – mở bằng Illustrator"), ("ky-thuat-mat-truoc.svg", "Bản kỹ thuật mặt trước"), ("ky-thuat-mat-sau.svg", "Bản kỹ thuật mặt sau"),
          ("mockup-tui.png", "Ảnh mô phỏng PNG")]
    dls = "".join(f'<a class="dl" href="{f}" download>{t}<span>{f}</span></a>' for f, t in dl)
    css = C.CSS + """
.it{background:#fff;border-radius:6px;padding:14px;margin:0}.it img{display:block;width:100%;height:auto}.it figcaption{font-size:14px;margin-top:10px;color:#4a3a36}
.hero .mk{background:#EFE7DC;border-radius:6px;overflow:hidden}.hero .mk img{display:block;width:100%}
.spec td:first-child{font-weight:800;color:var(--do);width:30%}
ul.lg{list-style:none;padding:0;margin:14px 0 0;display:grid;gap:8px}ul.lg li{display:flex;gap:10px;align-items:center;font-size:14px}ul.lg i{flex:none;width:22px;height:6px;border-radius:3px}
ul.can{margin:8px 0 0 20px}ul.can li{margin:4px 0}
.dls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.dl{display:block;background:#fff;border-radius:6px;padding:16px;color:var(--muc);text-decoration:none;font-weight:800;border-left:5px solid var(--do)}
.dl span{display:block;font-weight:400;font-size:12px;color:#6b5a55;margin-top:4px;overflow-wrap:anywhere}
@media (max-width:860px){.dls{grid-template-columns:minmax(0,1fr)}}
"""
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Túi Tortilla An Tâm</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Bao bì · Túi 300 × 330 mm</div><h1>Túi bánh tortilla</h1>
<p>Ý tưởng: <b>chiếc bánh là tâm của dấu vân tay</b>. Cửa sổ tròn để khách thấy bánh thật, quanh cửa sổ là các vòng vân tay son đỏ, như lời cam kết điểm chỉ lên từng mẻ bánh. Mặt sau đủ các mục ghi nhãn, ô in phun ngày và gợi ý dùng cho quán.</p></div>
<div class="mk"><img src="mockup-tui.png" alt="Mô phỏng túi bánh tortilla mặt trước và mặt sau"></div></div></header>
<nav class="toc"><a href="#in">File in</a><a href="#kt">Kỹ thuật</a><a href="#ts">Thông số</a><a href="#dien">Cần điền</a><a href="#tai">Tải về</a></nav>
<section class="s" id="in"><div class="num">01 · File in</div><h2>Hai mặt túi</h2><p class="lead">Tỷ lệ 1 : 1 (đơn vị mm), đã gồm tràn lề 3 mm. Cửa sổ ở mặt trước để trống, không in mực.</p>
<div class="g g2">{fig("tui-tortilla-mat-truoc.svg", "Mặt trước – logo, cửa sổ nhìn bánh, tên sản phẩm, khối lượng tịnh")}{fig("tui-tortilla-mat-sau.svg", "Mặt sau – thông tin sản phẩm, gợi ý dùng, ô in phun, mã vạch, liên hệ")}</div></section>
<section class="s" id="kt"><div class="num">02 · Kỹ thuật</div><h2>Đường cắt, biên hàn, vùng an toàn</h2>
<div class="g g2">{fig("ky-thuat-mat-truoc.svg", "Mặt trước kèm chỉ dẫn")}{fig("ky-thuat-mat-sau.svg", "Mặt sau kèm chỉ dẫn")}</div>
<div class="card" style="margin-top:18px"><h4>Chú thích</h4><ul class="lg">{legend}</ul></div></section>
<section class="s" id="ts"><div class="num">03 · Thông số</div><h2>Gửi kèm cho nhà in</h2><table class="spec">{spec}</table></section>
<section class="s" id="dien"><div class="num">04 · Trước khi in</div><h2>Những chỗ cần điền</h2>
<div class="card"><p>Các ô <code>[ ]</code> trên túi là thông tin công ty phải điền đúng thực tế – tôi không tự đặt số liệu:</p><ul class="can">{can}</ul>
<p class="cap">Đối chiếu nội dung nhãn với quy định ghi nhãn hàng hoá hiện hành, và xin nhà in bản in thử màu trước khi chạy số lượng.</p></div></section>
<section class="s" id="tai"><div class="num">05 · Tải về</div><h2>Tệp</h2><div class="dls">{dls}</div></section>
<div class="end"><h2 style="color:var(--do);font-weight:800;font-size:clamp(28px,4vw,44px)">Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm</h2></div>
</body></html>"""
    open(os.path.join(out, "tui-tortilla.html"), "w").write(html)


if __name__ == "__main__":
    run(sys.argv[1])

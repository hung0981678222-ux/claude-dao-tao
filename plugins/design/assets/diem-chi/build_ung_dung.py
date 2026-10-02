"""Trang trình bày bộ ứng dụng nhận diện Điểm Chỉ. Chạy: python3 build_ung_dung.py OUTDIR
Ghi OUTDIR/bo-ung-dung.html và OUTDIR/ud/<nhóm>/<mẫu>.svg (trang tham chiếu các SVG này)."""
import os
import re
import sys

import bo_ung_dung as U
import build_chuan as C

LEAD = {
    "mxh": "Ảnh đại diện là vân tay trên nền đỏ – nhận ra ngay cả khi chỉ còn 40 px. Mẫu bài dùng chung khung: dải đỏ trên, chữ Tròn Bánh, logo góc dưới. Thay ảnh và chữ, giữ khung.",
    "an-pham": "Giấy tờ giao dịch ưu tiên nền kem, chữ mực, đỏ chỉ dùng cho logo và tiêu đề. Mọi số liệu, giá, địa chỉ trong ngoặc vuông là chỗ công ty điền thông tin thật.",
    "bao-bi": "Bao bì đi tới bếp đối tác nên phải dễ nhận ra trên kệ: mặt chính đỏ, vân tay lớn, tên sản phẩm to. Nhãn phụ để trống các mục bắt buộc theo quy định ghi nhãn để điền đúng thực tế.",
    "dong-phuc": "Đồng phục dùng hai màu: đỏ cho bếp và giao hàng, kem/mực cho văn phòng. Vân tay in ở ngực trái và lưng – dấu cam kết người làm bánh mang theo.",
    "diem-ban": "Ở ngoài đường, logo phải đọc được từ xa: biển hiệu và thùng xe chỉ dùng logo, vân tay lớn, slogan và hotline – không thêm chữ khác.",
}


def ratio(svg):
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', svg)
    return float(m.group(3)) / float(m.group(4))


def run(out):
    cards = {}
    for g, title, items in U.GROUPS:
        os.makedirs(os.path.join(out, "ud", g), exist_ok=True)
        cs = []
        for slug, cap, fn in items:
            s = fn()
            open(os.path.join(out, "ud", g, slug + ".svg"), "w").write(s)
            r = ratio(s); span = 3 if r > 2.2 else 2 if r > 1.45 else 1
            src = f"ud/{g}/{slug}.svg"
            cs.append(f'<figure class="it sp{span}"><a href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{cap}" loading="lazy"></a>'
                      f'<figcaption>{cap}</figcaption></figure>')
        cards[g] = "".join(cs)
    secs = "".join(f'<section class="s" id="{g}"><div class="num">{i:02d} · {len(items)} mẫu</div><h2>{t}</h2><p class="lead">{LEAD[g]}</p>'
                   f'<div class="grid">{cards[g]}</div></section>' for i, (g, t, items) in enumerate(U.GROUPS, 1))
    toc = "".join(f'<a href="#{g}">{t}</a>' for g, t, _ in U.GROUPS)
    total = sum(len(i) for _, _, i in U.GROUPS)
    css = C.CSS + """
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;grid-auto-flow:dense;align-items:start}
.it{background:#fff;border-radius:6px;padding:14px;margin:0}.it img{display:block;width:100%;height:auto;border-radius:3px}
.it figcaption{font-size:14px;line-height:1.45;margin-top:10px;color:#4a3a36}.sp2{grid-column:span 2}.sp3{grid-column:1/-1}
.note{max-width:1200px;margin:0 auto;padding:0 20px}.note .card{border-left:6px solid var(--do)}
@media (max-width:860px){.grid{grid-template-columns:minmax(0,1fr)}.sp2,.sp3{grid-column:auto}}
"""
    hero = U.LOGO_DK()
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ứng dụng An Tâm</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Bộ ứng dụng 1.0</div><h1>Nhận diện ở mọi nơi khách gặp An&nbsp;Tâm</h1>
<p>{total} mẫu dựng sẵn theo cẩm nang: mạng xã hội, ấn phẩm văn phòng, bao bì, đồng phục, điểm bán và xe giao hàng. Bấm vào mẫu để mở tệp SVG gốc.</p></div>
<div>{hero}</div></div></header>
<nav class="toc">{toc}</nav>
<div class="note" style="margin-top:36px"><div class="card"><h4>Trước khi in</h4><p>Các chỗ trong <code>[ ]</code> (giá, ngày, địa chỉ, mã số, thành phần, hạn dùng…) là thông tin công ty cần điền thật – không in khi còn để trống. Màu in cần chốt mã CMYK/Pantone với nhà in bằng bản in thử. Ảnh sản phẩm trong mẫu là hình minh hoạ, thay bằng ảnh chụp thật.</p></div></div>
{secs}
<div class="end"><h2 style="color:var(--do);font-weight:800;font-size:clamp(30px,4vw,48px)">Sản Phẩm Tận Tâm – Phát Triển Xứng Tầm</h2><p>antamfoods.com · 0348.635.222</p></div>
</body></html>"""
    open(os.path.join(out, "bo-ung-dung.html"), "w").write(html)


if __name__ == "__main__":
    run(sys.argv[1])

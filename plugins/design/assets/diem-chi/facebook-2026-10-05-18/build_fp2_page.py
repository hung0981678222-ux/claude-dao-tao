"""Trang xem bài Facebook 05–18/10/2026. Chạy sau fanpage_1018.py: python3 build_fp2_page.py OUTDIR"""
import os
import sys
from collections import OrderedDict

import build_chuan as C
import fanpage_1018 as F

DA_CO = {
    "1": "Ảnh thật: giá vỏ bánh kebab tại xưởng (Drive › HÌNH ẢNH KEBAB › DJI_…0316).",
    "2": "MP4 19 giây: đoạn quay thật ép bánh (Drive › VIDEO KEBAB › IMG_5896.MOV) + 3 ảnh thật (nướng, làm nguội trên giá, kiểm tra) + lớp chữ + thẻ kết.",
    "6": "Ảnh thật: hàng vỏ bánh kebab trên giá (DJI_…0319).",
    "7": "Bìa dùng ảnh thật kiểm tra bánh, tay đeo găng (IMG_5929).",
}
THIEU = {
    "1": "Ảnh đang dùng là vỏ kebab; nếu muốn đúng tortilla: chụp chồng bánh tortilla tại xưởng.",
    "2": "Còn thiếu cảnh bột vào máy và đóng gói; các video dài hơn trong kho (>10 MB) chưa tải được qua kết nối Drive – thêm ở bản dựng sau.",
    "3": "1 góc máy cố định từ trên/chéo, quay liền 10 lần cuốn kebab (20–30 giây, có thể tua nhanh).",
    "4": "4 ảnh vỏ bánh 22/25/28/31 cm đặt cạnh thước đo + món tương ứng; 1 ảnh 4 size xếp cạnh nhau. Xác nhận lại món gợi ý cho từng size.",
    "5": "Quay tại 1 cửa hàng đối tác (có đồng ý): chuẩn bị quầy, lò doner, vỏ bánh An Tâm, giờ cao điểm, lời chủ quán.",
    "6": "Số liệu: công suất (chiếc/ngày), số dây chuyền.",
    "7": "Video: đo đường kính bằng thước, cân từng chiếc, gập thử bánh không nứt.",
    "8": "Cảnh làm 3 món từ 1 chiếc tortilla: wrap gà, taco, quesadilla (tay người, góc trên xuống).",
    "9": "3 đánh giá thật nguyên văn + tên quán + đồng ý đăng; ảnh 3 quán/chủ quán.",
    "10": "Video khách thật (chủ xe bánh mì) kể chuyện, có đồng ý bằng văn bản; tên, tên xe, khu vực.",
}


def groups():
    g = OrderedDict()
    for bai, ngay, slug, _, note in F.all_items():
        g.setdefault(bai, (ngay, []))[1].append((slug, note))
    return g


def run(out):
    secs = []
    for bai, (ngay, files) in groups().items():
        num = bai.split(".")[0]
        cards = "".join(f'<figure class="it {"lop" if ("-lop-" in s or "-dem-" in s) else ""}" id="{s}"><img src="{s}.png" alt="{s}" loading="lazy"><figcaption><code>{s}.png</code><br>{n}</figcaption></figure>' for s, n in files)
        miss = (f'<div class="card ok"><b>Đã dùng ảnh/video thật:</b> {DA_CO[num]}</div>' if num in DA_CO else "")
        miss += f'<div class="card miss"><b>Còn thiếu:</b> {THIEU.get(num, "")}</div>' if num in THIEU else ""
        if num == "2":
            cards = '<figure class="it" id="reel-r1-mp4"><video src="reel-r1-vo-banh-lam-the-nay.mp4" controls playsinline preload="metadata" poster="b02-r1-vo-banh-lam-the-nay-bia.png" style="width:100%;display:block"></video><figcaption><code>reel-r1-vo-banh-lam-the-nay.mp4</code><br>19 giây · 1080×1920</figcaption></figure>' + cards
        secs.append(f'<section class="s" id="b{num}"><div class="num">{ngay}</div><h2>{bai}</h2>{miss}<div class="grid">{cards}</div></section>')
    toc = "".join(f'<a href="#b{b.split(".")[0]}">{b.split(" – ")[0]}</a>' for b in groups())
    css = C.CSS + """.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;align-items:start;margin-top:14px}
.it{background:#fff;border-radius:6px;padding:10px;margin:0;scroll-margin-top:70px}.it img{display:block;width:100%;height:auto}
.it.lop img{background:repeating-conic-gradient(#5a4d4a 0 25%,#6b5d59 0 50%) 0 0/24px 24px}
.it figcaption{font-size:12px;margin-top:6px;overflow-wrap:anywhere}.miss{border-left:6px solid var(--ngo);margin-top:10px}.ok{border-left:6px solid #2F7D45}
@media (max-width:860px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}"""
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Facebook 05–18/10</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Bản nháp · không đăng</div><h1>Bài Facebook 05–18/10/2026</h1>
<p>Khung mẫu Điểm Chỉ. Ảnh và video thật lấy từ kho Drive của An Tâm; chỗ chưa có ảnh thật để KHUNG ẢNH THẬT. Reels gồm ảnh bìa, lớp chữ nền trong suốt để đặt lên video, và thẻ kết chung.</p></div>
<div class="card">{F.V.logo_ngang()}</div></div></header><nav class="toc">{toc}</nav>{"".join(secs)}<div class="end"><p>Hotline trên ảnh: {F.HOTLINE}</p></div></body></html>"""
    open(os.path.join(out, "facebook-0510-1810.html"), "w").write(html)


if __name__ == "__main__":
    run(sys.argv[1])

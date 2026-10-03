# Thiết kế: 10 bài Facebook bánh tortillas (05/10 – 11/10/2026)

Ngày: 2026-10-03. Người làm: designer. Không dùng Canva/Figma; bản mẫu dựng bằng HTML, chụp PNG bằng Playwright.

## 0. Quy tắc nền (đọc trước)
1. **Ảnh thật của chủ trang luôn ưu tiên hơn ảnh AI.** Khi chủ trang có ảnh/video thật của sản phẩm, dùng ảnh thật ở mọi vị trí "KHUNG ẢNH THẬT".
2. **Ảnh AI không được giả làm ảnh sản phẩm thật của trang.** Chỉ dùng ảnh AI cho nền, món minh hoạ, không gian bếp, họa tiết. Không dùng ảnh AI để thể hiện bao bì, hình dáng, độ dày, màu, số lượng của bánh đang bán. Nếu đăng ảnh AI món ăn thì ghi chú "Ảnh minh hoạ" ở góc hoặc cuối bài.
3. Không logo/thương hiệu người khác, không bao bì có chữ/nhãn, không người thật nổi tiếng. Prompt AI luôn có: `no text, no logo, no brand packaging, no watermark`.
4. Không đưa lên hình: giá, ưu đãi, chứng nhận, đánh giá, công dụng sức khoẻ, hạn dùng khi chưa có xác nhận. Dùng ô trống: `[GIÁ]`, `[ƯU ĐÃI]`, `[CÁCH ĐẶT HÀNG]`, `[TÊN THƯƠNG HIỆU]`, `[LOẠI BÁNH]`, `[KÍCH CỠ/QUY CÁCH]`, `[KHU VỰC GIAO]`, `[HẠN DÙNG/BẢO QUẢN]`.
5. Con số thời gian hâm (chảo 10–15 giây/mặt, lò vi sóng 15–30 giây, hấp 30–45 giây) lấy từ nghien-cuu.md (độ tin cậy trung bình): luôn kèm chú thích "tham khảo, tuỳ loại bánh". Chủ trang nên thử lại bằng bánh thật trước khi đăng.

## 1. Bộ nhận diện TẠM (đề xuất của designer, chưa phải thương hiệu thật)
Chưa biết tên, logo, màu thương hiệu (trang Facebook không truy cập được). Bộ dưới đây là đề xuất, thay hết bằng nhận diện thật khi chủ trang gửi. Mọi bản mẫu có ô `[LOGO / TÊN THƯƠNG HIỆU]` để thay.

| Tên màu | HEX | Dùng cho |
|---|---|---|
| Kem bánh | `#FFF4DC` | Nền chính |
| Bột mì | `#F3DDB0` | Nền phụ, khung ảnh |
| Vàng ngô | `#E9A23B` | Nhấn chính, nền bìa |
| Ớt đỏ | `#C8452D` | Nhãn, chỗ trống cần điền, CTA |
| Xanh rau | `#3F7D4E` | Công thức, bước, nhãn "mẹo" |
| Nâu cà phê | `#2B1D14` | Chữ chính, nền tối |
| Nâu xám | `#6B5A4A` | Chữ phụ, chú thích |

Tỉ lệ: 60% kem/bột mì, 25% vàng, 10% nâu, 5% ớt/xanh. Độ tương phản chữ nâu `#2B1D14` trên kem/vàng đạt tốt; chữ kem trên nâu đạt tốt. Không đặt chữ vàng nhỏ trên nền kem.

**Font** (hỗ trợ tiếng Việt đầy đủ, miễn phí Google Fonts): tiêu đề **Be Vietnam Pro** ExtraBold 800; nội dung **Be Vietnam Pro** Regular/SemiBold. Phương án thay: Nunito, Montserrat. Lưu ý: PNG mẫu trong `mau/` được chụp bằng font dự phòng Liberation Sans do máy dựng không có Be Vietnam Pro; HTML đã khai báo Be Vietnam Pro đứng đầu nên khi máy có font hoặc dựng lại sẽ đổi sang font đề xuất.

## 2. Phong cách ảnh món ăn (khi chụp ảnh thật)
- Ánh sáng: cửa sổ ban ngày, ánh sáng mềm bên hông hoặc chéo sau, không flash trực diện. Dùng tấm xốp trắng/giấy trắng hắt sáng cho bóng mềm.
- Góc: 45 độ cho wrap/burrito (thấy lớp nhân); top-down 90 độ cho pizza tortilla, thẻ công thức và ảnh xếp bánh; cận cảnh tay cuốn/gập bánh cho video.
- Đạo cụ: thớt gỗ, khăn vải màu kem/xanh rau, đĩa gốm trơn, tô rau thơm, chanh, ớt, đũa/nĩa. Tránh đạo cụ có logo.
- Màu thực phẩm: ấm, hơi bão hoà; rau xanh tươi là điểm nhấn.
- Bánh phải "mềm": chụp lúc vừa hâm, có độ cong, gập đôi không nứt, có hơi nóng nhẹ nếu được.
- Để trống 20–30% khung hình (thường nửa trên hoặc một góc) để đặt chữ.

## 3. Quy tắc chữ trên ảnh
- Tối đa **10 chữ** trên ảnh chính. Tiêu đề 1–2 dòng, mỗi dòng ≤ 6 chữ.
- Cỡ chữ tối thiểu trên khung 1080 px: tiêu đề 90–130 px, phụ 40–46 px, chú thích 28–32 px (đọc được trên điện thoại).
- Tiêu đề Be Vietnam Pro 800, chữ thường có dấu, không viết hoa toàn bộ trừ nhãn ngắn (≤ 3 chữ).
- Chừa lề an toàn 80 px mỗi cạnh (Facebook cắt viền khi hiển thị); với Reels chừa 250 px dưới và 180 px trên cho giao diện.
- Một ý một hình. Chữ không đè lên phần nhân món ăn.
- Chỗ trống cần điền: viền đứt đỏ `#C8452D`, nền trắng, để người đăng không sót khi chưa điền.
- Dấu tiếng Việt: kiểm lại trên ảnh xuất cuối (Ậ, Ể, Ữ, Ợ đều phải rõ, không bị cắt dòng trên/dưới).

## 4. Kích thước theo kênh
| Dạng | Kích thước |
|---|---|
| Ảnh đơn / thẻ công thức / bán hàng | 1080x1350 (4:5) |
| Carousel | 1080x1350 mỗi slide, 3–5 slide |
| Reels / Story | 1080x1920 (9:16) |
| Ảnh share/link | 1200x630 (nếu cần) |

## 5. 10 bài

Phần "prompt" luôn dùng cho nền/minh hoạ, theo quy tắc 0.2. Hậu tố chung cho mọi prompt: `Warm natural window light, soft shadows, shallow depth of field, 4:5 vertical composition, clean empty space on the upper third for text, warm palette of cream, golden yellow, fresh green and chili red, photorealistic food photography, no text, no logo, no brand packaging, no watermark.` (gọi tắt là **[HẬU TỐ]**).

### Bài 1 · T2 05/10 11:30 · Giới thiệu sản phẩm · ảnh đơn 1080x1350
- Bố cục: nửa trên nền kem, chữ; nửa dưới khung ảnh thật (bánh xếp chồng, một cái gập đôi). Góc dưới trái ô logo, góc dưới phải tên trang.
- Chữ trên ảnh: "Bánh tortilla: cuốn gì cũng được." (6 chữ). Nhãn nhỏ: "LÀM QUEN NHÉ".
- Ảnh: ưu tiên ảnh thật chồng bánh. Thay thế nếu chưa có ảnh: bàn bếp minh hoạ, không thể hiện bánh của trang.
- Prompt: `Top-down view of a rustic kitchen table with a wooden board, small bowls of shredded lettuce, sliced cucumber, grilled chicken strips, lime wedges and chili, soft folded flour tortillas as generic flatbread, cheerful Vietnamese home kitchen mood. [HẬU TỐ]`

### Bài 2 · T2 05/10 19:30 · Tương tác · ảnh đơn 1080x1350
- Bố cục: câu hỏi lớn giữa khung, 3 lựa chọn dạng thẻ bo tròn xếp dọc, mỗi thẻ có icon vẽ (gà, bò, rau).
- Chữ trên ảnh: "Nhà bạn hay cuốn gì?" (5 chữ). Thẻ: "Gà", "Bò xào", "Rau trứng" (bình luận để chọn).
- Màu: nền vàng ngô, thẻ kem, chữ nâu.
- Ảnh: không cần ảnh món; dùng hình vẽ phẳng. Nếu muốn, nền họa tiết bánh tròn mờ.
- Prompt (tuỳ chọn, nền họa tiết): `Seamless flat illustration pattern of round flatbreads, chili peppers, lime slices and herb leaves on a golden yellow background, minimal vector style, low contrast, large empty center. no text, no logo, no watermark.`

### Bài 3 · T3 06/10 11:00 · Công thức wrap gà 10 phút · thẻ công thức 1080x1350
- **Có bản mẫu:** `mau/b-the-cong-thuc-wrap-ga.html` + `.png`.
- Bố cục: nhãn "CÔNG THỨC · 10 PHÚT", tiêu đề, khung ảnh thật wrap cắt đôi (ngang, cao ~290 px), 2 thẻ trắng: "Chuẩn bị" (4 nguyên liệu) và "Làm nhanh" (4 bước đánh số).
- Chữ trên ảnh: "Wrap gà mềm, dễ cuốn" (6 chữ) + 4 bước ngắn (là nội dung thẻ, biên tập sẽ khớp theo bài viết). Định lượng để trống `[THEO CÔNG THỨC BÀI VIẾT]` đến khi bài viết chốt.
- Prompt: `45-degree close-up of a chicken wrap cut in half on a wooden board, showing layers of seared chicken, crisp lettuce, cucumber and creamy lime mayo, soft folded tortilla, a hand holding one half, light steam. [HẬU TỐ]`

### Bài 4 · T4 07/10 17:30 · Mẹo hâm bánh mềm 3 cách · carousel 5 slide 1080x1350
- **Có bản mẫu:** `mau/a-carousel-ham-banh.html` + `a-carousel-ham-banh-1..5.png`.
- Slide 1 bìa: "Hâm bánh mềm, không khô: 3 cách" (nền vàng, khung ảnh thật). Slide 2: Chảo, "10–15 giây". Slide 3: Lò vi sóng, "15–30 giây", bọc khăn ẩm. Slide 4: Hấp, "30–45 giây". Slide 5: "Hâm vừa đủ, sốt vừa đủ." + kêu gọi lưu bài + `[CÁCH ĐẶT HÀNG]`.
- Mỗi slide một con số cực lớn, một ảnh minh hoạ cách hâm (ảnh thật càng tốt).
- Prompts (mỗi slide 1 ảnh, dùng nếu chưa có ảnh thật; không thể hiện bánh của trang):
  - Chảo: `Close-up of a flatbread warming in a dry non-stick pan, gentle puff of steam, wooden spatula, warm kitchen light. [HẬU TỐ]`
  - Lò vi sóng: `A flatbread wrapped in a slightly damp white kitchen towel on a ceramic plate beside a microwave, home kitchen. [HẬU TỐ]`
  - Hấp: `A bamboo steamer with soft flatbreads folded inside, rising steam, wooden table. [HẬU TỐ]`

### Bài 5 · T5 08/10 11:30 · Hỏi đáp: sợ khô/nứt · ảnh đơn 1080x1350
- Bố cục: dạng "hỏi - đáp": bong bóng hỏi trên cùng (nền ớt, chữ kem), bong bóng đáp bên dưới (nền xanh rau), giữa là khung ảnh thật bánh gập đôi không nứt.
- Chữ trên ảnh: hỏi "Bánh bị khô, nứt?" (4 chữ); đáp "Hâm ẩm, đừng hâm lâu." (5 chữ).
- Không nêu bảo quản/hạn dùng nếu chưa xác minh; chỗ trống nhỏ `[HẠN DÙNG/BẢO QUẢN]` ở chân hình nếu bài viết có nhắc.
- Prompt: `Close-up of hands gently folding a soft warm flatbread in half without cracking, flour-dusted wooden counter, a small bowl of filling in soft focus. [HẬU TỐ]`

### Bài 6 · T6 09/10 11:30 · Bán hàng/đặt cuối tuần · ảnh đơn 1080x1350 (nên chạy thử quảng cáo)
- **Có bản mẫu:** `mau/c-bai-ban-hang.html` + `.png`.
- Bố cục: đầu trang nền vàng với tiêu đề, khung ảnh thật sản phẩm, bảng 7 dòng chỗ trống (thương hiệu, loại bánh, quy cách, giá, ưu đãi, khu vực giao, cách đặt) trên nền nâu; chân trang logo.
- Chữ trên ảnh: "Bánh mềm, cuốn là ngon." (6 chữ), nhãn "ĐẶT BÁNH CUỐI TUẦN". Mọi thông tin khác là chỗ trống phải điền.
- Bắt buộc ảnh thật sản phẩm ở khung ảnh. Nếu chưa có thì không đăng bài này (ảnh AI không thay được).
- Prompt (chỉ làm nền cho phần phụ, không đặt vào khung sản phẩm): `Flat-lay of fresh herbs, lime, chili and a linen napkin on a warm cream surface, large empty center for product photo, soft light. [HẬU TỐ]`

### Bài 7 · T6 09/10 18:00 · Pizza tortilla chảo · Reels 1080x1920, 20 giây
- Kịch bản cảnh:
  1. 0–2s: top-down chảo trống, chữ "Pizza 10 phút." (3 chữ).
  2. 2–6s: đặt bánh lên chảo, quệt sốt cà (cận cảnh tay).
  3. 6–10s: rắc phô mai, xúc xích/nấm.
  4. 10–15s: đậy nắp, cut cảnh phô mai chảy.
  5. 15–18s: cắt miếng, kéo sợi phô mai.
  6. 18–20s: đĩa thành phẩm + "Lưu lại làm tối nay." (5 chữ) + logo.
- Nhạc vui nhịp nhanh (nhạc không bản quyền hoặc có sẵn trong thư viện Facebook). Phụ đề tiếng Việt bám theo từng cảnh, mỗi cảnh ≤ 6 chữ.
- Bìa video: top-down pizza cắt miếng, chữ "Pizza 10 phút" nền vàng.
- Prompt bìa/nền: `Top-down view of a round pizza made on a thin flatbread in a skillet, melted cheese stretching from a lifted slice, tomato sauce, mushrooms, sliced sausage, rustic wooden table. [HẬU TỐ, 9:16 vertical]` 

### Bài 8 · T7 10/10 10:00 · Tortilla cuốn kiểu Việt · carousel 4 slide 1080x1350
- Slide 1 bìa: "Cuốn kiểu Việt: gà sả, bò xào" (6 chữ), nhãn "TORTILLA KIỂU VIỆT". Slide 2: nhân gà sả + rau thơm. Slide 3: nhân bò xào + dưa leo. Slide 4: nước mắm chua ngọt chấm kèm + "Bạn thích nhân nào?".
- Ảnh thật cho mỗi slide; ảnh AI chỉ dùng cho nền rau thơm/nước chấm, không thay món của trang.
- Prompt slide 1: `45-degree shot of a tortilla wrap filled with lemongrass chicken, herbs, cucumber and pickled vegetables, a small bowl of sweet-sour fish sauce dipping, Vietnamese home dining table, banana leaf placemat. [HẬU TỐ]`
- Prompt slide 2–3: `Close-up of stir-fried beef with onions and herbs in a pan, steam rising, warm light. [HẬU TỐ]`

### Bài 9 · CN 11/10 10:00 · Khách sỉ cho quán nhỏ · ảnh đơn 1080x1350
- Bố cục: nền nâu đậm, tiêu đề kem, 3 ô biểu tượng (Số lượng, Giao hàng, Đặt trước) mỗi ô một chỗ trống: `[KÍCH CỠ/QUY CÁCH]`, `[KHU VỰC GIAO]`, `[CÁCH ĐẶT HÀNG]`. Giá sỉ: `[GIÁ SỈ]`.
- Chữ trên ảnh: "Bán taco, wrap? Nhắn mình nhé." (6 chữ).
- Không nêu giá/số lượng tối thiểu/hạn dùng khi chưa có. Hình ảnh: quầy xe đồ ăn minh hoạ (ảnh AI được phép vì là minh hoạ ngữ cảnh, không phải sản phẩm).
- Prompt: `Small street food cart at golden hour with a row of wraps and tacos on a wooden counter, a friendly cook wrapping food, no readable signs, no logos, warm and busy mood, 4:5 vertical.` thêm `no text, no logo, no brand packaging, no watermark`.

### Bài 10 · CN 11/10 19:00 · Tổng kết tuần + nhắn tin đặt hàng · ảnh đơn 1080x1350
- Bố cục: lưới 2x2 ảnh thật các món trong tuần (wrap gà, pizza, cuốn kiểu Việt, mẹo hâm) trên nền kem, tiêu đề phía trên, dải CTA cuối.
- Chữ trên ảnh: "Tuần bánh mềm: bạn thích món nào?" (7 chữ) + "Nhắn mình để đặt" + `[CÁCH ĐẶT HÀNG]`.
- Ảnh: dùng ảnh thật/kết quả của các bài trước. Không cần ảnh AI.

## 6. Bản mẫu dựng sẵn (thư mục `mau/`)
| File | Nội dung | Kích thước |
|---|---|---|
| `a-carousel-ham-banh.html`, `a-carousel-ham-banh-1.png` … `-5.png` | Bài 4: carousel mẹo hâm bánh mềm 3 cách | 1080x1350 x5 |
| `b-the-cong-thuc-wrap-ga.html`, `.png` | Bài 3: thẻ công thức wrap gà 10 phút | 1080x1350 |
| `c-bai-ban-hang.html`, `.png` | Bài 6: ảnh bán hàng có chỗ trống | 1080x1350 |
| `chung.css`, `chup.js` | Style chung, script chụp PNG | |

Ghi chú bản mẫu: khung "KHUNG ẢNH THẬT" là hình khối minh hoạ (SVG), không phải ảnh sản phẩm; thay bằng ảnh thật của chủ trang. Viền đứt đỏ là chỗ trống cần điền. Muốn dựng lại PNG: chạy `node chup.js` trong thư mục `mau/` (cần playwright).

## 7. Cần chủ trang cung cấp
Logo, tên thương hiệu, màu thương hiệu thật; ảnh/video thật sản phẩm (bánh chồng, bánh gập đôi, bánh trong tay, wrap cắt đôi); thông tin điền vào các ô trống; xác nhận thời gian hâm cho đúng loại bánh.

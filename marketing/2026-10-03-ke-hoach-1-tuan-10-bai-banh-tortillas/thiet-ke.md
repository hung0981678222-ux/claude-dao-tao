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
- Bố cục: nửa trên nền kem, chữ; nửa dưới khung ảnh thật (bánh xếp chồng, một cái gập đôi). Góc dưới trái ô logo, góc dưới phải ô trống `[TÊN THƯƠNG HIỆU]` viền đỏ.
- Chữ trên ảnh (khớp bài viết): "Một tấm bánh, cuốn gì cũng ngon". Nhãn nhỏ: "LÀM QUEN NHÉ".
- Ảnh: ưu tiên ảnh thật chồng bánh. Thay thế nếu chưa có ảnh: bàn bếp minh hoạ, không thể hiện bánh của trang (ghi "Ảnh minh hoạ").
- Prompt: `Top-down view of a rustic kitchen table with a wooden board, small bowls of shredded lettuce, sliced cucumber, grilled chicken strips, lime wedges and chili, soft folded flour tortillas as generic flatbread, cheerful Vietnamese home kitchen mood. [HẬU TỐ]`

### Bài 2 · T2 05/10 18:30 · Tương tác · ảnh đơn 1080x1350
- Bố cục: câu hỏi lớn ở nửa trên; nửa dưới lưới 2x2 bốn thẻ bo tròn, mỗi thẻ một chữ cái lớn và icon vẽ phẳng.
- Chữ trên ảnh (khớp bài viết): "Cuốn gì tối nay? A, B, C hay D?". Bốn thẻ đúng 4 lựa chọn của bài viết: **A** Gà áp chảo + rau sống; **B** Bò xào + hành tây; **C** Trứng + phô mai; **D** Nhân khác (kể mình nghe).
- Màu: nền vàng ngô, thẻ kem, chữ nâu, chữ cái ớt đỏ trong vòng tròn kem. Chân hình: "Bình luận chữ cái bạn chọn".
- Ảnh: không cần ảnh món; hình vẽ phẳng. Nếu muốn, nền họa tiết bánh tròn mờ.
- Prompt (tuỳ chọn, nền họa tiết): `Seamless flat illustration pattern of round flatbreads, chili peppers, lime slices and herb leaves on a golden yellow background, minimal vector style, low contrast, large empty center. no text, no logo, no watermark.`

### Bài 3 · T3 06/10 11:00 · Wrap gà 10 phút · Reels 30–45 giây, 1080x1920 (gợi ý chạy quảng cáo)
- **Có bản mẫu thẻ công thức (ảnh bìa/ảnh đăng kèm):** `mau/b-the-cong-thuc-wrap-ga.html` + `.png` (1080x1350). Thẻ ghi: "Bánh [LOẠI BÁNH]", gà ướp tỏi muối tiêu, xà lách–dưa leo–cà chua–rau thơm, mayo chanh; bước 3 "Xếp rau, gà, rưới sốt vừa phải"; định lượng "2 tấm bánh · 1–2 phần · khoảng 10 phút (ước tính)".
- Chữ trên ảnh/bìa (khớp bài viết): "Wrap gà mềm, dễ cuốn", nhãn "CÔNG THỨC · 10 PHÚT".
- **Kịch bản Reels (tổng khoảng 42 giây).** Chữ an toàn: chừa 180 px trên, 250 px dưới. Phụ đề mỗi cảnh ≤ 6 chữ.
  1. 0–3s, hook: thành phẩm wrap cắt đôi, nhìn thấy lớp nhân. Phụ đề: "Wrap gà 10 phút" + nhãn CÔNG THỨC · 10 PHÚT.
  2. 3–8s: bày nguyên liệu trên thớt (2 tấm bánh, gà, rau, mayo chanh). Phụ đề: "2 tấm bánh, 1–2 phần".
  3. 8–16s: ướp gà với tỏi, muối, tiêu; áp chảo cho chín vàng. Phụ đề: "Áp chảo gà vàng".
  4. 16–23s: hâm bánh trên chảo nóng, mỗi mặt 10–15 giây. Phụ đề: "Hâm bánh cho mềm" + chú thích nhỏ "tham khảo, tuỳ loại bánh".
  5. 23–31s: xếp rau, gà; rưới sốt vừa phải. Phụ đề: "Rưới sốt vừa phải".
  6. 31–37s: gập hai mép, cuốn chặt, cắt đôi. Phụ đề: "Cuốn chặt, cắt đôi".
  7. 37–42s, chốt: thành phẩm + mẹo "Đừng rưới quá nhiều sốt kẻo nhão" + "Lưu bài làm tối nay" + ô `[TÊN THƯƠNG HIỆU]`.
- Bìa Reels: thẻ công thức hoặc khung wrap cắt đôi, chữ "Wrap gà mềm, dễ cuốn" nền kem. Khi có video, dựng lại bìa 9:16 theo cùng chữ; thẻ 4:5 đăng kèm làm ảnh lưu công thức.
- Quay bằng đồ thật của chủ trang; thời gian nấu là ước tính, nấu thử và bấm giờ trước khi quay, sửa phụ đề nếu khác.
- Prompt (bìa/nền minh hoạ nếu chưa có ảnh): `45-degree close-up of a chicken wrap cut in half on a wooden board, showing layers of seared chicken, crisp lettuce, cucumber and creamy lime mayo, soft folded tortilla, a hand holding one half, light steam. [HẬU TỐ]`

### Bài 4 · T4 07/10 17:30 · Mẹo hâm bánh mềm 3 cách · carousel 5 slide 1080x1350
- **Có bản mẫu:** `mau/a-carousel-ham-banh.html` + `a-carousel-ham-banh-1..5.png`.
- Slide 1 bìa: nhãn "MẸO BẾP NHANH", "Hâm bánh mềm, không khô: 3 cách" (nền vàng, khung ảnh thật). Slide 2: Chảo, "10–15 giây", "Mỗi mặt trên chảo nóng". Slide 3: Lò vi sóng, "15–30 giây", "Bọc khăn/giấy bếp ẩm". Slide 4: Hấp, "30–45 giây". Slide 5: "Hâm vừa đủ, sốt vừa đủ." + tóm 3 mốc thời gian kèm "Thời gian tham khảo, tuỳ loại bánh" + kêu gọi lưu bài + `[CÁCH ĐẶT HÀNG]`.
- Chữ "giây" màu ớt đỏ (không dùng vàng trên nền kem). Mỗi slide một con số cực lớn, một ảnh minh hoạ cách hâm (ảnh thật càng tốt).
- Prompts (mỗi slide 1 ảnh, dùng nếu chưa có ảnh thật; không thể hiện bánh của trang):
  - Chảo: `Close-up of a flatbread warming in a dry non-stick pan, gentle puff of steam, wooden spatula, warm kitchen light. [HẬU TỐ]`
  - Lò vi sóng: `A flatbread wrapped in a slightly damp white kitchen towel on a ceramic plate beside a microwave, home kitchen. [HẬU TỐ]`
  - Hấp: `A bamboo steamer with soft flatbreads folded inside, rising steam, wooden table. [HẬU TỐ]`

### Bài 5 · T5 08/10 11:30 · Hỏi đáp: sợ khô/nứt · ảnh đơn 1080x1350
- Bố cục: dạng "hỏi - đáp": bong bóng hỏi trên cùng (nền ớt, chữ kem), bong bóng đáp bên dưới (nền xanh rau), giữa là khung ảnh thật bánh gập đôi không nứt.
- Chữ trên ảnh (khớp bài viết): hỏi/tiêu đề "Bánh khô, nứt? Mình giải đáp"; đáp "Hâm vừa đủ, đừng hâm lâu." (chú thích nhỏ "10–15 giây mỗi mặt trên chảo, tham khảo, tuỳ loại bánh").
- Không nêu bảo quản/hạn dùng nếu chưa xác minh; chỗ trống nhỏ `[HẠN DÙNG/BẢO QUẢN]` ở chân hình.
- Prompt: `Close-up of hands gently folding a soft warm flatbread in half without cracking, flour-dusted wooden counter, a small bowl of filling in soft focus. [HẬU TỐ]`

### Bài 6 · T6 09/10 11:30 · Bán hàng/đặt cuối tuần · ảnh đơn 1080x1350 (gợi ý chạy quảng cáo)
- **Có bản mẫu:** `mau/c-bai-ban-hang.html` + `.png`. Định dạng chốt: ảnh đơn.
- Bố cục: đầu trang nền vàng với tiêu đề, khung ảnh thật sản phẩm, bảng 7 dòng chỗ trống (thương hiệu, loại bánh, quy cách, giá, ưu đãi, khu vực giao, cách đặt) trên nền nâu; chân trang logo và ô `[TÊN THƯƠNG HIỆU]`.
- Chữ trên ảnh (khớp bài viết): "Cuối tuần cuốn gì? Nhắn mình!", nhãn "ĐẶT BÁNH CUỐI TUẦN". Không dùng "Bánh mềm". Mọi thông tin khác là chỗ trống phải điền.
- Bắt buộc ảnh thật sản phẩm ở khung ảnh. Nếu chưa có thì không đăng bài này (ảnh AI không thay được).
- Prompt (chỉ làm nền cho phần phụ, không đặt vào khung sản phẩm): `Flat-lay of fresh herbs, lime, chili and a linen napkin on a warm cream surface, large empty center for product photo, soft light. [HẬU TỐ]`

### Bài 7 · T6 09/10 18:00 · Pizza tortilla chảo · Reels 30 giây, 1080x1920
- Chữ trên video (khớp bài viết): "Pizza chảo 10 phút, khỏi lò". Phụ đề mỗi cảnh ≤ 6 chữ; chừa 180 px trên, 250 px dưới.
- Kịch bản cảnh (30 giây):
  1. 0–3s, hook: top-down chảo trống, rồi cắt sang pizza thành phẩm. Chữ: "Pizza chảo 10 phút, khỏi lò".
  2. 3–8s: bày nguyên liệu (1 tấm bánh, sốt cà, phô mai, xúc xích hoặc nấm). Phụ đề: "Chỉ cần 4 món".
  3. 8–13s: đặt bánh vào chảo, lửa nhỏ. Phụ đề: "Bánh vào chảo, lửa nhỏ".
  4. 13–19s: phết sốt cà, rải phô mai và xúc xích (hoặc nấm) (cận cảnh tay). Phụ đề: "Sốt, phô mai, topping".
  5. 19–25s: đậy nắp cho phô mai chảy; cắt cảnh nắp mở. Phụ đề: "Đậy nắp cho phô mai chảy".
  6. 25–28s: cắt miếng, kéo sợi phô mai. Phụ đề: "Cắt miếng, ăn nóng".
  7. 28–30s: đĩa thành phẩm + "Lưu bài, làm xong khoe mình" + ô `[TÊN THƯƠNG HIỆU]`.
- Lưu ý an toàn thực phẩm (chuyển viet-bai ở mục C1 của biên tập): xúc xích/nấm sống nên xào sơ hoặc thái mỏng, đậy nắp đến khi chín; chỉnh phụ đề cảnh 4–5 theo bản bài viết chốt.
- Nhạc vui nhịp nhanh (không bản quyền hoặc thư viện Facebook).
- Bìa video: top-down pizza cắt miếng, chữ "Pizza chảo 10 phút" nền vàng.
- Prompt bìa/nền: `Top-down view of a round pizza made on a thin flatbread in a skillet, melted cheese stretching from a lifted slice, tomato sauce, mushrooms, sliced sausage, rustic wooden table. [HẬU TỐ, 9:16 vertical]`

### Bài 8 · T7 10/10 11:30 · Tortilla cuốn bò xào sả (kiểu Việt) · carousel 5 slide 1080x1350
- Chữ bìa (khớp bài viết): "Tortilla cuốn bò xào sả", nhãn "TORTILLA KIỂU VIỆT".
- Slide 1 bìa: tiêu đề + khung ảnh thật bánh cuốn bò xào. Slide 2 "Nguyên liệu": `[LOẠI BÁNH]`, thịt bò thái mỏng, sả băm, tỏi, dưa leo, rau thơm, hành tây, nước mắm chua ngọt. Slide 3 "Bước 1–2": xào bò với sả, tỏi trên lửa lớn cho thơm (ghi nhỏ: "thay gà nướng sả cũng được"); hâm bánh trên chảo nóng 10–15 giây mỗi mặt (tham khảo, tuỳ loại bánh). Slide 4 "Bước 3–4": xếp dưa leo, rau thơm, hành tây, bò xào; rưới ít nước mắm chua ngọt, cuốn chặt. Slide 5 "Mẹo + CTA": "Rưới nước mắm vừa phải, bánh mới không nhão." + "Lưu bài, cuối tuần thử liền" + `[CÁCH ĐẶT HÀNG]`.
- Mỗi slide có chân trang logo và ô `[TÊN THƯƠNG HIỆU]`. Thời gian "khoảng 10–12 phút (ước tính)" ghi ở slide 2.
- Ảnh thật cho mỗi slide; ảnh AI chỉ dùng cho nền rau thơm/nước chấm, không thay món của trang (ghi "Ảnh minh hoạ" nếu dùng).
- Prompt slide 1: `45-degree shot of a tortilla wrap filled with stir-fried lemongrass beef, herbs, cucumber and onion, a small bowl of sweet-sour fish sauce dipping, Vietnamese home dining table. [HẬU TỐ]`
- Prompt slide 3: `Close-up of stir-fried sliced beef with lemongrass, garlic and onions in a pan, steam rising, warm light. [HẬU TỐ]`

### Bài 9 · CN 11/10 11:30 · Khách sỉ cho quán nhỏ · ảnh đơn 1080x1350
- Bố cục: nền nâu đậm, tiêu đề kem; khung ảnh khay bánh + món mẫu; dưới là bảng 8 ô trống chuẩn viền đỏ.
- Chữ trên ảnh (khớp bài viết): "Bánh tortillas cho quán nhỏ".
- 8 chỗ trống chuẩn, đủ như bài viết: `[TÊN THƯƠNG HIỆU]`, `[LOẠI BÁNH]`, `[KÍCH CỠ/QUY CÁCH]`, `[GIÁ]` (dòng "Giá sỉ"), `[HẠN DÙNG/BẢO QUẢN]`, `[KHU VỰC GIAO]`, `[ƯU ĐÃI]`, `[CÁCH ĐẶT HÀNG]`. Không dùng `[GIÁ SỈ]`.
- Không nêu giá/số lượng tối thiểu/hạn dùng khi chưa có. Ưu tiên ảnh thật khay bánh + món mẫu (theo lịch). Nếu dùng ảnh AI quầy xe thì phải ghi "Ảnh minh hoạ" ở góc ảnh; ảnh AI chỉ để minh hoạ ngữ cảnh, không phải sản phẩm.
- Prompt (chỉ khi dùng ảnh minh hoạ): `Small street food cart at golden hour with a row of wraps and tacos on a wooden counter, a friendly cook wrapping food, no readable signs, no logos, warm and busy mood, 4:5 vertical, no text, no logo, no brand packaging, no watermark.`

### Bài 10 · CN 11/10 18:30 · Tổng kết tuần + nhắn tin đặt hàng · ảnh đơn 1080x1350 (ảnh ghép 4 món)
- Bố cục: lưới 2x2 ảnh thật 4 món đúng mục "Tuần qua mình chia sẻ": (1) 3 cách làm mềm bánh, (2) Wrap gà 10 phút, (3) Pizza tortilla chảo, (4) Tortilla cuốn bò xào sả. Nền kem, tiêu đề phía trên, dải CTA cuối.
- Chữ trên ảnh (khớp bài viết): "Cuốn tiếp tuần mới nào!" + "Nhắn mình để đặt" + `[CÁCH ĐẶT HÀNG]`.
- Ảnh: dùng ảnh thật/kết quả của các bài trước. Không cần ảnh AI.

## 6. Bản mẫu dựng sẵn (thư mục `mau/`)
| File | Nội dung | Kích thước |
|---|---|---|
| `a-carousel-ham-banh.html`, `a-carousel-ham-banh-1.png` … `-5.png` | Bài 4: carousel mẹo hâm bánh mềm 3 cách | 1080x1350 x5 |
| `b-the-cong-thuc-wrap-ga.html`, `.png` | Bài 3: thẻ công thức wrap gà (ảnh bìa/đăng kèm của Reels) | 1080x1350 |
| `c-bai-ban-hang.html`, `.png` | Bài 6: ảnh bán hàng có chỗ trống | 1080x1350 |
| `chung.css`, `chup.js` | Style chung, script chụp PNG | |

Ghi chú bản mẫu: khung "KHUNG ẢNH THẬT" là hình khối minh hoạ (SVG), không phải ảnh sản phẩm; thay bằng ảnh thật của chủ trang. Viền đứt đỏ là chỗ trống cần điền (kể cả ô `[TÊN THƯƠNG HIỆU]` ở chân trang). Muốn dựng lại PNG: chạy `node chup.js` trong thư mục `mau/` (cần playwright).

## 7. Cần chủ trang cung cấp
Logo, tên thương hiệu, màu thương hiệu thật; ảnh/video thật sản phẩm (bánh chồng, bánh gập đôi, bánh trong tay, wrap cắt đôi); thông tin điền vào các ô trống; xác nhận thời gian hâm cho đúng loại bánh.

## Nhật ký sửa vòng 1 (2026-10-03)
Nguồn chốt: lich-dang.md và bai-viet.md. Không sửa bai-viet.md, lich-dang.md, bien-tap.md.
- Giờ đăng: bài 2 18:30, bài 8 11:30, bài 9 11:30, bài 10 18:30 (theo lịch).
- Bài 1, 2, 5, 9, 10: chữ trên ảnh khớp bài viết. Bài 2 dùng 4 thẻ A/B/C/D.
- Bài 3: giữ Reels 30–45 giây, thêm kịch bản 7 cảnh (~42s); thẻ công thức giữ làm bìa/ảnh đăng kèm. PNG: bỏ `[THEO CÔNG THỨC BÀI VIẾT]`, thay bằng "2 tấm bánh · 1–2 phần · khoảng 10 phút (ước tính)"; "Chuẩn bị" gồm `[LOẠI BÁNH]`, gà ướp tỏi muối tiêu, rau, mayo chanh; bước 3 "Xếp rau, gà, rưới sốt vừa phải".
- Bài 6: PNG đổi tiêu đề "Cuối tuần cuốn gì? Nhắn mình!", bỏ "Bánh mềm"; chốt ảnh đơn.
- Bài 7: Reels 30 giây (kịch bản 7 cảnh), chữ theo bài viết; ghi chú an toàn thực phẩm cho viet-bai (C1).
- Bài 8: carousel 5 slide, chỉ bò xào sả (ghi "thay gà nướng sả cũng được"); bỏ "pickled vegetables", "banana leaf" khỏi prompt.
- Bài 9: chỉ dùng 8 chỗ trống chuẩn (`[GIÁ]` thay `[GIÁ SỈ]`), đủ ô như bài viết; ảnh AI ghi "Ảnh minh hoạ".
- Bài 10: ảnh ghép 4 món, bỏ "bánh mềm".
- Carousel bài 4 (PNG chụp lại): slide 1 "MẸO BẾP NHANH" (bỏ "10 GIÂY"); slide 2 bỏ "Không cần dầu...phồng nhẹ và thơm"; slide 3 đổi "Bọc khăn/giấy bếp ẩm" (bỏ "1 lớp"); slide 5 thêm "Thời gian tham khảo, tuỳ loại bánh"; chữ "giây" đổi sang ớt đỏ ở slide 2–4.
- Cả 3 mẫu: thay "@trang-cua-ban" bằng ô trống viền đỏ `[TÊN THƯƠNG HIỆU]`.
- Chụp lại 7 PNG (giữ nguyên tên file) bằng `node chup.js`, đã xem lại cả 7 sau lần chụp cuối: không tràn chữ, dấu tiếng Việt rõ.
- Còn tồn: slide 4 carousel còn dòng "Hợp khi hâm nhiều cái cùng lúc cho cả nhà" và slide 3 còn "Hơi ẩm giữ bánh mềm, dễ cuốn, ít nứt" (biên tập không nêu, nhưng không có trong nghien-cuu.md; có thể bỏ nếu muốn bám nguồn tuyệt đối). PNG vẫn dùng font dự phòng Liberation Sans.

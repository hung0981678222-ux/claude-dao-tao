# Thiết kế: 10 bài Facebook Ẩm Thực An Tâm (bản 2, bộ nhận diện chính thức)

Ngày: 2026-10-03. Bộ nhận diện tạm cũ (kem/vàng ngô) đã bỏ. Góc chủ đạo: "Bánh tươi mỗi ngày, giao tận bếp, gọi là có". 7 bài chủ quán (1, 2, 4, 5, 6, 8, 10) và 3 bài công thức (3, 7, 9), theo khung 10 bài trong `nghien-cuu.md` bản 2. Chữ trên ảnh tự viết ngắn; biên tập khớp với `bai-viet.md` sau.

## Cập nhật mới từ sếp (đã áp dụng)
- Giá chỉ báo qua Zalo 0398 431 300: không có ô giá trên ảnh. Ảnh bán hàng dùng "Nhắn Zalo 0398 431 300 để nhận báo giá".
- Chưa có thử mẫu: không dùng chữ "thử mẫu", "bánh mẫu", "dùng thử" trên ảnh (bài 6 đã là "nhận báo giá").

## Quy tắc nhận diện áp dụng
- Màu: Đỏ #D2141E (~60%), Kem #FFF6EA (~25%), Mực #231716 (~10%), Vàng #F5B82E (≤5%: nhãn và huy hiệu, chữ vàng chỉ cỡ ≥24 px, chữ trên vàng dùng Đỏ đậm #8F0D14), Đỏ son #E2332B chỉ cho vân tay (có trong file logo/vân), Đỏ đậm #8F0D14 cho chữ trên vàng.
- Cặp chữ: kem trên đỏ, đỏ trên kem, mực trên kem. Không dùng vàng trên đỏ cho chữ nhỏ.
- Font: An Tâm Tròn Bánh qua @font-face (`nhan-dien/font/*.woff2`): ExtraBold cho tiêu đề và nhãn (chữ hoa giãn +20%), SemiBold phụ đề, Regular chú thích. Thân ≥26 px.
- Khổ: 1080×1350, lề 72 px; Story/Reels 1080×1920 (trống trên 250, dưới 340), logo ngang phía trên.
- Logo: nền đỏ dùng bản kem, nền kem dùng bản đỏ; chừa quanh logo ≥ nửa chiều cao dấu vân tay; không đổi màu, xoay, đổ bóng, vẽ lại. Chỉ dùng file trong `nhan-dien/logo/`.
- Hoạ tiết: tối đa một vân tay lớn mỗi ấn phẩm; vân tay nhỏ chỉ làm biểu tượng dòng; không đặt chữ nhỏ trên nền đường vân (chữ nằm trên panel kem).
- Ảnh: ảnh thật xưởng, tay người làm bánh, món tại quán; tông ấm, nền gỗ/kraft/kem. Ảnh AI chỉ khi thiếu ảnh thật, ghi "Ảnh minh hoạ AI" (chữ kem trên nền Mực, góc dưới). Không ảnh mạng, không bịa giá, %, đánh giá, tên quán, chứng nhận. Chỗ chưa biết: `[Cần điền: ...]`.
- Giọng: ngắn, thật, ấm; tránh "ngon nhất", "số 1", "giá rẻ", "!!!".

## Bản mẫu đã dựng (`mau/`)
| Mẫu | HTML | PNG | Dùng cho bài |
|---|---|---|---|
| A giới thiệu "bánh tươi mỗi ngày, giao tận bếp" | `mau/a-gioi-thieu.html` | `mau/a-gioi-thieu.png` | 1 |
| B chọn cỡ bánh | `mau/b-chon-co-banh.html` | `mau/b-chon-co-banh.png` | 2 (và 4, 5 đổi nội dung) |
| C nhận báo giá qua Zalo | `mau/c-nhan-bang-gia.html` | `mau/c-nhan-bang-gia.png` | 6, 8 |
| D thẻ công thức nấu ở nhà | `mau/d-the-cong-thuc.html` | `mau/d-the-cong-thuc.png` | 3, 7, 9 |

Chụp lại: `cd mau && node chup.js`. Khung "Ảnh thật: ..." trong mẫu là hình khối giữ chỗ; thay bằng ảnh thật trước khi đăng. Có 3 chỗ `[Cần điền]` trong mẫu (món gợi ý theo cỡ, giờ chốt đơn, định lượng công thức).

## Chi tiết từng bài
### Bài 1 (T2 05/10): Hậu trường xưởng, bánh tươi mỗi ngày, giao tận bếp
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/a-gioi-thieu` (dựng từ ý bai-uu-dai: khung vân + panel kem)
- Bố cục: khung vân (một vân lớn) > panel kem: logo, nhãn, tiêu đề 2 dòng, khung ảnh thật, dòng "Làm mới mỗi ngày tại xưởng TP.HCM", nút Zalo; huy hiệu vàng "Gọi là có"
- Chữ trên ảnh (≤10 chữ): "Bánh tươi mỗi ngày, giao tận bếp" (6 chữ)
- Logo: logo ngang đỏ, trên trái panel kem
- Ảnh thật cần: Đôi tay người làm bánh xếp mẻ vừa ra lò; góc xưởng; xe/túi bánh chuẩn bị giao (cần người làm bánh đồng ý lên hình)
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Warm natural-light photo of a baker's hands stacking freshly baked flour tortillas on a wooden bench in a small Vietnamese bakery workshop, steam rising, kraft paper, warm tones, no brand logos, no text, 4:5

### Bài 2 (T3 06/10): Chọn cỡ bánh cho món (22/25/28/31 cm)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/b-chon-co-banh` (cấu trúc bai-san-pham: đầu đỏ + thân kem + chân đỏ)
- Bố cục: đầu đỏ: logo kem, nhãn vàng, tiêu đề; thân kem: 4 vòng tròn tỉ lệ theo cỡ + tên cỡ + món gợi ý; chân đỏ: Zalo
- Chữ trên ảnh (≤10 chữ): "Món nào, cỡ bánh nấy" (5 chữ)
- Logo: logo ngang kem, trên trái nền đỏ
- Ảnh thật cần: Ảnh 4 cỡ bánh xếp cạnh nhau, đặt thước/đĩa để thấy chênh lệch (tuỳ chọn). Mục "món gợi ý theo cỡ" cần An Tâm xác nhận
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh AI (đồ hoạ). Tuỳ chọn thêm ảnh: top-down flat lay of four flour tortillas of different sizes side by side on a wooden table, warm light, no text

### Bài 3 (T4 07/10 11:30): Wrap gà 10 phút (công thức nấu ở nhà)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/d-the-cong-thuc` (đầu đỏ + khung ảnh + 3 bước)
- Bố cục: tiêu đề lớn, ảnh món, 3 bước đánh số, dòng nguyên liệu, logo + "Lưu bài"
- Chữ trên ảnh (≤10 chữ): "Wrap gà 10 phút" (4 chữ)
- Logo: logo ngang đỏ, dưới trái
- Ảnh thật cần: Wrap gà thành phẩm cắt đôi; tay cuộn bánh. Định lượng chờ bài viết
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Overhead photo of a chicken wrap cut in half showing shredded chicken and fresh lettuce, on a wooden board with kraft paper, warm natural light, home kitchen, no logos, no text, 4:5

### Bài 4 (T4 07/10 21:00): Giới thiệu 3 dòng tortilla: tươi, nướng, nguyên cám
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-san-pham.svg`
- Bố cục: đầu đỏ nhãn "BÁNH TORTILLA" + tiêu đề; giữa: 3 khung ảnh tròn/ngang cho 3 dòng; chân: "15 chiếc/túi · 22/25/28/31 cm"; nút Zalo
- Chữ trên ảnh (≤10 chữ): "Ba dòng bánh, đủ bốn cỡ" (6 chữ)
- Logo: biểu tượng vân tay trong ô trắng bo góc phải trên (như mẫu), hoặc logo ngang kem ở đầu đỏ
- Ảnh thật cần: Chụp 3 loại bánh cạnh nhau, thấy rõ màu/độ nướng/hạt cám
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Three stacks of tortillas (plain, toasted with light brown spots, wholewheat with visible bran) on a kraft paper background, warm light, no logos, no text, 4:5

### Bài 5 (T5 08/10): 4 loại vỏ kebab: bánh vàng, mè đen, mè trắng, than tre
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-san-pham.svg` (bản lưới 2×2) 
- Bố cục: đầu đỏ + tiêu đề; lưới 2×2 khung ảnh thật, mỗi ô có nhãn tên vỏ (chữ ≥28 px, nền kem, không nằm trên vân); chân đỏ Zalo. Quy cách: [Cần điền]
- Chữ trên ảnh (≤10 chữ): "Bốn loại vỏ kebab" (4 chữ)
- Logo: logo ngang kem, đầu đỏ
- Ảnh thật cần: Ảnh từng loại vỏ (vàng, mè đen, mè trắng, than tre), kèm một chiếc doner cuộn ở quán đối tác nếu được phép
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Four kinds of doner kebab flatbread wraps (golden, black sesame, white sesame, bamboo charcoal black) laid on wooden board, warm light, no logos, no text, 4:5

### Bài 6 (T6 09/10 10:00): Nhận bảng giá đại lý qua Zalo (không dùng "thử mẫu")
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/c-nhan-bang-gia` (cấu trúc bai-doi-tac.svg)
- Bố cục: đầu đỏ: logo, nhãn vàng, tiêu đề 2 dòng; 4 dòng ý với dấu vân tay nhỏ; nút bo tròn Zalo. Không có ô giá
- Chữ trên ảnh (≤10 chữ): "Nhắn Zalo để nhận báo giá" (6 chữ)
- Logo: logo ngang kem, trên trái đầu đỏ
- Ảnh thật cần: Không cần
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh (mẫu chữ).

### Bài 7 (T6 09/10 18:30): Pizza tortilla chảo (công thức nấu ở nhà)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/d-the-cong-thuc` (đổi tiêu đề và 3 bước)
- Bố cục: như bài 3
- Chữ trên ảnh (≤10 chữ): "Pizza tortilla chảo" (3 chữ)
- Logo: logo ngang đỏ, dưới trái
- Ảnh thật cần: Pizza chảo thành phẩm, cảnh cắt miếng kéo phô mai
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Overhead photo of a round tortilla pizza with melted cheese and toppings in a cast-iron pan, warm natural light, wooden table, no logos, no text, 4:5

### Bài 8 (T7 10/10): Mở điểm bán tortilla – kebab cùng An Tâm
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-doi-tac.svg` (dựng lại như mẫu c, 4 dòng: bảng giá rõ ràng, giao tận nơi, Hỗ trợ: [Cần điền], Chính sách: [Cần điền])
- Bố cục: đầu đỏ, 4 dòng có vân tay nhỏ, nút Zalo
- Chữ trên ảnh (≤10 chữ): "Mở điểm bán tortilla – kebab" (6 chữ)
- Logo: logo ngang kem, trên trái đầu đỏ
- Ảnh thật cần: Ảnh quầy/xe đối tác thật (khi được đồng ý), hoặc không dùng
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh (mẫu chữ). Tuỳ chọn: Vietnamese street food stall owner preparing wraps, warm light, no logos, no text

### Bài 9 (CN 11/10 10:30): Quesadilla gà phô mai (công thức nấu ở nhà)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/d-the-cong-thuc`
- Bố cục: như bài 3
- Chữ trên ảnh (≤10 chữ): "Quesadilla gà phô mai" (4 chữ)
- Logo: logo ngang đỏ, dưới trái
- Ảnh thật cần: Quesadilla cắt miếng, phô mai kéo sợi
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Close-up of a sliced golden-brown chicken and cheese quesadilla with melted cheese pulling, wooden board, warm light, no logos, no text, 4:5

### Bài 10 (CN 11/10 21:00): Lịch giao tuần mới; "Cần thêm bánh gấp? Gọi An Tâm, tụi mình lo."
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-thong-bao.svg` (khung viền đỏ, dấu tròn, bảng 3 dòng)
- Bố cục: dấu tròn "Cam kết từ tâm" trên (một hoạ tiết lớn), nhãn, tiêu đề, bảng giờ giao/giờ chốt: [Cần điền], câu "Cần thêm bánh gấp?..." và số Zalo/Gọi
- Chữ trên ảnh (≤10 chữ): "Cần thêm bánh gấp? Gọi An Tâm." (7 chữ)
- Logo: dấu tròn (không cần logo ngang), nền kem
- Ảnh thật cần: Không cần
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh.

## Việc cần người quyết định
1. Ảnh thật xưởng, tay người làm bánh, 3 dòng bánh, 4 loại vỏ kebab, và sự đồng ý của người làm bánh khi lên hình.
2. Món gợi ý theo cỡ (bài 2) cần An Tâm xác nhận; giờ chốt đơn, giờ giao (bài 10), quy cách vỏ kebab (bài 5), chính sách đối tác (bài 8).
3. Định lượng công thức (bài 3, 7, 9) chờ `bai-viet.md`.

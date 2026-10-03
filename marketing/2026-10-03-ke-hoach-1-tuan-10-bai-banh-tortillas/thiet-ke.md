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
| A giới thiệu "Bánh làm mới mỗi ngày" | `mau/a-gioi-thieu.html` | `mau/a-gioi-thieu.png` | 1 |
| B chọn cỡ bánh | `mau/b-chon-co-banh.html` | `mau/b-chon-co-banh.png` | 2 (và 4, 5 đổi nội dung) |
| C nhận báo giá qua Zalo | `mau/c-nhan-bang-gia.html` | `mau/c-nhan-bang-gia.png` | 6, 8 |
| D1 thẻ công thức bài 3 | `mau/d-cong-thuc-bai-3.html` | `mau/d-cong-thuc-bai-3.png` | 3 |
| D2 thẻ công thức bài 7 | `mau/d-cong-thuc-bai-7.html` | `mau/d-cong-thuc-bai-7.png` | 7 |
| D3 thẻ công thức bài 9 | `mau/d-cong-thuc-bai-9.html` | `mau/d-cong-thuc-bai-9.png` | 9 |

Chụp lại: `cd mau && node chup.js`. Khung "Ảnh thật: ..." trong mẫu là hình khối giữ chỗ; thay bằng ảnh thật trước khi đăng. Không còn dòng `[Cần điền]` nào trên ảnh. Gợi ý cỡ–món trên ảnh bài 2 và các bước công thức trên ảnh bài 3, 7, 9 chép đúng từ `bai-viet.md`; xưởng/bếp phải duyệt và nấu thử trước khi đăng (việc này nằm trong danh sách việc của sếp, không để trên ảnh). Câu chân thẻ công thức khớp lời kêu gọi cuối từng bài.

## Chi tiết từng bài
### Bài 1 (T2 05/10): Hậu trường xưởng, bánh tươi mỗi ngày, giao tận bếp
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/a-gioi-thieu` (bố cục: khung vân + panel kem; không phải bài ưu đãi)
- Bố cục: khung vân (một vân lớn) > panel kem: logo, tiêu đề 2 dòng, khung ảnh thật, nút Zalo. Không nhãn, không huy hiệu, không dòng phụ
- Chữ trên ảnh (≤10 chữ): "Bánh làm mới mỗi ngày" (5 chữ) + nút "Nhắn Zalo: 0398 431 300"
- Logo: logo ngang đỏ, trên trái panel kem
- Ảnh thật cần: Đôi tay người làm bánh xếp mẻ vừa ra lò; góc xưởng; xe/túi bánh chuẩn bị giao (cần người làm bánh đồng ý lên hình)
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Warm natural-light photo of a baker's hands stacking freshly baked flour tortillas on a wooden bench in a small Vietnamese bakery workshop, steam rising, kraft paper, warm tones, no brand logos, no text, 4:5

### Bài 2 (T3 06/10): Chọn cỡ bánh cho món (22/25/28/31 cm)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/b-chon-co-banh` (đầu đỏ + thân kem + chân đỏ)
- Bố cục: đầu đỏ: logo kem, nhãn vàng, tiêu đề; thân kem: 4 vòng tròn tỉ lệ theo cỡ + tên cỡ + món gợi ý; chân đỏ: Zalo
- Chữ trên ảnh (≤10 chữ): "Đúng cỡ cho đúng món" (5 chữ). Gợi ý từng cỡ đúng chữ bài 2: 22 cm "Món cuốn nhỏ, taco, phần ăn nhẹ"; 25 cm "Wrap suất vừa"; 28 cm "Wrap đầy nhân, burrito"; 31 cm "Burrito lớn, phần cuốn nhiều nhân"; chú thích "Cả 3 dòng tươi · nướng · nguyên cám có đủ 4 cỡ, 15 chiếc/túi."
- Logo: logo ngang kem, trên trái nền đỏ
- Ảnh thật cần: Ảnh 4 cỡ bánh xếp cạnh nhau, đặt thước/đĩa để thấy chênh lệch (tuỳ chọn). Gợi ý cỡ–món cần xưởng duyệt trước khi đăng (việc của sếp, không ghi trên ảnh)
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh AI (đồ hoạ). Tuỳ chọn thêm ảnh: top-down flat lay of four flour tortillas of different sizes side by side on a wooden table, warm light, no text

### Bài 3 (T4 07/10 11:30): Wrap gà, 10 phút (công thức nấu ở nhà)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/d-cong-thuc-bai-3` (đầu đỏ + khung ảnh + 4 bước)
- Bố cục: tiêu đề lớn, khung ảnh món, 4 bước đánh số, dòng nguyên liệu, logo + câu chân
- Chữ trên ảnh (≤10 chữ): "Wrap gà, 10 phút" (4 chữ). Bước: 1 Áp chảo gà với muối tiêu, cắt miếng; 2 Làm nóng bánh, mỗi mặt 10–15 giây (tham khảo); 3 Xếp rau, gà, quét sốt vừa phải; 4 Cuộn chặt tay, cắt đôi. Nguyên liệu: 1 chiếc tortilla · gà áp chảo hoặc gà xé · xà lách, dưa leo · mayonnaise trộn chút nước cốt chanh. Chân: "Lưu bài để mai nấu nhé"
- Logo: logo ngang đỏ, dưới trái
- Ảnh thật cần: Wrap gà thành phẩm cắt đôi; tay cuộn bánh. Định lượng theo bài viết (chỉ "1 chiếc tortilla")
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Overhead photo of a chicken wrap cut in half showing shredded chicken and fresh lettuce, on a wooden board with kraft paper, warm natural light, home kitchen, no logos, no text, 4:5

### Bài 4 (T4 07/10 21:00): Giới thiệu 3 dòng tortilla: tươi, nướng, nguyên cám
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-san-pham.svg`
- Bố cục: đầu đỏ nhãn "BÁNH TORTILLA" + tiêu đề; giữa: 3 khung ảnh tròn/ngang cho 3 dòng; chân: "15 chiếc/túi · 22/25/28/31 cm"; nút Zalo
- Chữ trên ảnh (≤10 chữ): "3 dòng tortilla, 4 cỡ" (5 chữ)
- Logo: biểu tượng vân tay trong ô trắng bo góc phải trên (như mẫu), hoặc logo ngang kem ở đầu đỏ
- Ảnh thật cần: Chụp 3 loại bánh cạnh nhau, thấy rõ màu/độ nướng/hạt cám
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Three stacks of tortillas (plain, toasted with light brown spots, wholewheat with visible bran) on a kraft paper background, warm light, no logos, no text, 4:5

### Bài 5 (T5 08/10): 4 loại vỏ kebab: bánh vàng, mè đen, mè trắng, than tre
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-san-pham.svg` (bản lưới 2×2) 
- Bố cục: đầu đỏ + tiêu đề; lưới 2×2 khung ảnh thật, mỗi ô có nhãn tên vỏ (chữ ≥28 px, nền kem, không nằm trên vân); chân đỏ Zalo. Quy cách: [Cần điền]
- Chữ trên ảnh (≤10 chữ): "4 loại vỏ kebab" (4 chữ)
- Logo: logo ngang kem, đầu đỏ
- Ảnh thật cần: Ảnh từng loại vỏ (vàng, mè đen, mè trắng, than tre), kèm một chiếc doner cuộn ở quán đối tác nếu được phép
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Four kinds of doner kebab flatbread wraps (golden, black sesame, white sesame, bamboo charcoal black) laid on wooden board, warm light, no logos, no text, 4:5

### Bài 6 (T6 09/10 10:00): Nhận bảng giá đại lý qua Zalo (không dùng "thử mẫu")
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/c-nhan-bang-gia` (bố cục riêng, không phải bài đối tác; tuần này không đăng bài đối tác)
- Bố cục: đầu đỏ: logo, nhãn vàng, tiêu đề 2 dòng; 3 dòng ý với dấu vân tay nhỏ (bảng giá đại lý rõ ràng; giao bánh tận nơi tại TP.HCM; báo giá gửi qua Zalo); nút bo tròn Zalo. Không có ô giá, không giờ chốt đơn
- Chữ trên ảnh (≤10 chữ): "Nhắn Zalo nhận báo giá" (5 chữ)
- Logo: logo ngang kem, trên trái đầu đỏ
- Ảnh thật cần: Không cần
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh (mẫu chữ).

### Bài 7 (T6 09/10 18:30): Pizza tortilla chảo (công thức nấu ở nhà)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/d-cong-thuc-bai-7`
- Bố cục: như bài 3 (tiêu đề 2 dòng)
- Chữ trên ảnh (≤10 chữ): "Pizza tortilla trên chảo" (4 chữ). Bước: 1 Đặt bánh vào chảo chống dính, lửa nhỏ; 2 Phết sốt cà, rải phô mai, xếp xúc xích hoặc nấm; 3 Đậy nắp vài phút cho phô mai chảy; 4 Cắt miếng, ăn nóng. Nguyên liệu: 1 chiếc tortilla · sốt cà chua · phô mai bào · xúc xích hoặc nấm thái lát. Chân: "Chia sẻ bài cho cả nhà"
- Logo: logo ngang đỏ, dưới trái
- Ảnh thật cần: Pizza chảo thành phẩm, cảnh cắt miếng kéo phô mai
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Overhead photo of a round tortilla pizza with melted cheese and toppings in a cast-iron pan, warm natural light, wooden table, no logos, no text, 4:5

### Bài 8 (T7 10/10): Mở điểm bán tortilla – kebab cùng An Tâm
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/c-nhan-bang-gia` (đổi nội dung các dòng ý; chưa dựng file riêng. Dòng nào chưa có thông tin xưởng xác nhận thì bỏ khỏi ảnh, không để [Cần điền] trên ảnh)
- Bố cục: đầu đỏ, 4 dòng có vân tay nhỏ, nút Zalo
- Chữ trên ảnh (≤10 chữ): "Mở điểm bán cùng An Tâm" (6 chữ)
- Logo: logo ngang kem, trên trái đầu đỏ
- Ảnh thật cần: Ảnh quầy/xe đối tác thật (khi được đồng ý), hoặc không dùng
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh (mẫu chữ). Tuỳ chọn: Vietnamese street food stall owner preparing wraps, warm light, no logos, no text

### Bài 9 (CN 11/10 10:30): Tortilla cuốn kiểu Việt (công thức nấu ở nhà)
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `mau/d-cong-thuc-bai-9`
- Bố cục: như bài 3
- Chữ trên ảnh (≤10 chữ): "Tortilla cuốn kiểu Việt" (4 chữ). Bước: 1 Làm nóng bánh, mỗi mặt 10–15 giây (tham khảo); 2 Xếp rau, dưa leo, thịt lên bánh; 3 Rưới ít nước mắm chua ngọt, vừa đủ; 4 Cuộn chặt, ăn ngay khi còn ấm. Nguyên liệu: 1 chiếc tortilla · gà nướng sả (hoặc bò xào) · rau thơm, dưa leo, xà lách · nước mắm chua ngọt. Chân: "Lưu bài để lần sau làm nhé"
- Logo: logo ngang đỏ, dưới trái
- Ảnh thật cần: Tortilla cuốn gà nướng sả, rau thơm, dưa leo, cắt đôi, kèm chén nước mắm chua ngọt
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Close-up of a tortilla wrap filled with lemongrass grilled chicken, herbs, cucumber and lettuce, cut in half, small bowl of sweet fish sauce beside it, wooden board, warm light, no logos, no text, 4:5

### Bài 10 (CN 11/10 21:00): Lịch giao tuần mới; "Cần thêm bánh gấp? Gọi An Tâm, tụi mình lo."
- Định dạng: 1080×1350 px, lề 72 px
- Mẫu nền: `bai-thong-bao.svg` (khung viền đỏ, dấu tròn, bảng 3 dòng)
- Bố cục: dấu tròn "Cam kết từ tâm" trên (một hoạ tiết lớn), nhãn, tiêu đề, bảng giờ giao/giờ chốt: [Cần điền], câu "Cần thêm bánh gấp?..." và số Zalo/Gọi
- Chữ trên ảnh (≤10 chữ): "Cần thêm bánh gấp? Gọi An Tâm" (6 chữ)
- Logo: dấu tròn (không cần logo ngang), nền kem
- Ảnh thật cần: Không cần
- Prompt AI (chỉ khi thiếu ảnh thật; phải ghi "Ảnh minh hoạ AI" trên ảnh): Không cần ảnh.

## Việc cần người quyết định
1. Ảnh thật xưởng, tay người làm bánh, 3 dòng bánh, 4 loại vỏ kebab, và sự đồng ý của người làm bánh khi lên hình.
2. Xưởng duyệt gợi ý cỡ–món (bài 2); giờ chốt đơn, giờ giao (bài 10), quy cách vỏ kebab (bài 5), chính sách đối tác (bài 8).
3. Người nấu thử, bấm giờ công thức bài 3, 7, 9 trước khi đăng (ảnh đã chép đúng bài viết).

## Nhật ký sửa vòng 1 (bản 2)
Theo `bien-tap.md` (kết luận CẦN SỬA), ngày 2026-10-03.
- T1: ảnh bài 1 chỉ còn chữ chốt "Bánh làm mới mỗi ngày" (bỏ nhãn, dòng chữ lớn thừa, huy hiệu "Gọi là có", dòng phụ); giữ nút Zalo.
- T2, T3: ảnh bài 2 đổi tiêu đề "Đúng cỡ cho đúng món"; gợi ý cỡ–món đúng từng chữ bài 2; bỏ dòng `[Cần điền: An Tâm xác nhận]` (việc xưởng duyệt nằm trong danh sách việc của sếp).
- T4: ảnh bài 6 dùng "Nhắn Zalo nhận báo giá". T5: bỏ dòng "Đặt trước [Cần điền: giờ] nhận trong ngày" (còn 3 dòng ý).
- T6: xoá `d-the-cong-thuc.*`; tách 3 file `d-cong-thuc-bai-3/7/9` (.html/.png): tiêu đề = chữ chốt, đủ 4 bước, nguyên liệu đúng bài, không `[Cần điền]`, câu chân khớp lời kêu gọi cuối bài ("lưu bài để mai nấu nhé", "chia sẻ bài cho cả nhà", "lưu bài để cuối tuần làm nhé").
- T7: bỏ cách ghi "dựng từ ý bai-uu-dai" và "cấu trúc bai-doi-tac.svg" ở bài 1 và 6 cho khớp lich-dang (tuần này không dùng hai mẫu đó).
- `mau/chup.js` không cần sửa (tự quét `[a-z]-*.html`); đã chụp lại cả 6 PNG và xem lại từng ảnh: font An Tâm Tròn Bánh nạp đủ, dấu tiếng Việt đúng, không tràn chữ, logo đúng màu theo nền, mỗi ảnh tối đa một vân lớn (chỉ ảnh bài 1). Dấu hai chấm và dấu chấm trong font thương hiệu hiển thị dạng vòng nhỏ: đó là nét của font.

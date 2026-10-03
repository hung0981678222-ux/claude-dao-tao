# Thiết kế: chiến dịch Facebook 7 ngày, khoá "Làm chủ Claude trong công việc"

Ngày: 2026-10-03 · Người làm: Designer · Góc: "Claude là nhân viên mới rất nhanh: giao việc rõ, kiểm tra kỹ"

Chữ trên ảnh viết tạm theo góc trên; biên tập sẽ khớp với `bai-viet.md`. Mọi nội dung khoá (5 dòng, 5 bước, 5 nguyên tắc) lấy đúng từ `index.html`.

## 1. Nhận diện dùng chung

### Bảng màu (lấy từ :root của index.html)
| Vai trò | Tên | HEX | Dùng cho |
|---|---|---|---|
| Nền ảnh | tint | #F3F1EE | nền chính mọi ảnh |
| Chữ chính | ink | #262524 | tiêu đề, chữ thân |
| Chủ đạo / nhấn | clay | #C96442 | thanh trên cùng, nút CTA, số thứ tự |
| Clay nhạt / đậm | clayl / clayd | #F6E3DB / #993C1D | nhãn (pill), chữ nhấn trong tiêu đề |
| Nhóm "Làm", kết quả tốt | teal | #1F6F6B | ô "giao việc rõ", số bước ví dụ |
| Teal nhạt / đậm | teall / teald | #DDEEEC / #085041 | nền ô, chữ trên nền teal nhạt |
| Nhóm "An toàn", cảnh báo nhẹ | amb | #BA7517 | biểu tượng cảnh báo |
| Amber nhạt / đậm | ambl / ambd | #FAEEDA / #633806 | nền ô, chữ trên nền amber nhạt |
| Sai / mơ hồ / Từ chối | red / redl | #A32D2D / #FCEBEB | ô "giao việc mơ hồ" |
| Chữ phụ / viền | mute / line | #5F5E5A / #D3D1C7 | chú thích, khung |

Quy ước nhóm: Hiểu = clay, Làm = teal, An toàn = amber (đúng như slide "Sau khoá học, anh chị làm được gì?"). Tương phản chữ/nền đã chọn cặp đậm trên nhạt (ví dụ #993C1D trên #F6E3DB), không dùng amber #BA7517 làm chữ nhỏ.

### Font
- Tiêu đề: Cambria (dự phòng Georgia, Liberation Serif), đậm. Cùng font tiêu đề với bộ slide.
- Chữ thân: Calibri (dự phòng Segoe UI, Liberation Sans), đậm cho nhãn.
- Cả hai hỗ trợ tiếng Việt có dấu. Khi dựng ảnh thật ngoài trình duyệt, nhớ dùng font có đủ dấu (Cambria, Calibri có sẵn trên Windows/Office).
- Bản PNG mẫu chụp trong môi trường chỉ có Liberation/DejaVu nên hình dáng chữ hơi khác Cambria/Calibri; bố cục không đổi.

### Quy tắc chữ trên ảnh
1. Tiêu đề ≤ 12 chữ, tối đa 3 dòng, cỡ ≥ 76px trên khung 1080 (đọc được khi thu nhỏ còn ~360px chiều rộng điện thoại).
2. Chữ phụ ≥ 28px; chú thích pháp lý ≥ 23px; không chữ nhỏ hơn.
3. Mỗi ảnh một ý chính. Carousel: mỗi slide một ý, ≤ 5 khối chữ.
4. Chữ đậm tối trên nền sáng; không chữ trên ảnh nền phức tạp (nếu dùng ảnh AI làm nền thì phủ khối màu đặc dưới chữ).
5. Chân ảnh luôn có: tên khoá + "Khoá học độc lập, không phải sản phẩm chính thức của Anthropic." (bài T2, ads, slide cuối carousel; các ảnh khác có thể thu gọn còn dòng thứ hai).
6. Không dùng logo Anthropic/Claude, không vẽ lại biểu tượng tia nắng của Claude. Dùng chữ "Claude" bình thường trong câu. Hình minh hoạ dùng hình học đơn giản, người vẽ phẳng, hoặc ảnh chụp màn hình slide của khoá.
7. Không số liệu thống kê, không lời chứng thực, không nêu giá: để `[GIÁ]`, `[LINK ĐĂNG KÝ]`, `[HẠN ƯU ĐÃI]`.
8. Dấu ngoặc kép kiểu “ ” cho câu mẫu giao việc. Viết "anh chị/bạn" theo bài-viết; ảnh ưu tiên câu không xưng hô.

### Kích thước theo kênh
- Bài fanpage ảnh đơn và carousel: 1080x1350 (4:5, chiếm nhiều chỗ nhất trên điện thoại). Dùng 1080x1080 khi ảnh có nhiều chữ ngang hoặc cho ads.
- Ads feed: 1080x1080 (có thêm biến thể 1080x1350). Story/Reels nếu chạy: 1080x1920, chừa 250px trên và 340px dưới khỏi bị đè giao diện.
- Ảnh bìa fanpage (nếu muốn đổi cho tuần này): 1640x624, an toàn chữ ở vùng giữa 820x312.
- Xuất PNG, sRGB, ≤ 1MB mỗi ảnh để tải nhanh.

## 2. Hai hướng thiết kế tổng thể

**Hướng A (khuyên chọn): "Bảng ghi chú văn phòng"**: nền be ấm #F3F1EE, thẻ trắng/nhạt bo góc, tiêu đề serif lớn, màu theo nhóm Hiểu/Làm/An toàn. Hợp với giọng đồng nghiệp, đồng bộ bộ slide, dựng được hoàn toàn bằng HTML (đã có mẫu), dễ sửa chữ khi biên tập đổi lời. Là hướng toàn bộ mục 3 dưới đây theo.

**Hướng B: "Ảnh người thật làm việc"**: ảnh AI/ảnh minh hoạ nhân viên văn phòng ngồi cạnh một "đồng nghiệp mới" vẽ trừu tượng, chữ phủ trên khối màu đặc. Cảm xúc hơn nhưng khó giữ nhất quán 7 ngày, tốn thời gian chỉnh ảnh AI, rủi ro mặt/tay méo. Chỉ dùng cho T2 và ads nếu muốn A/B test. Prompt ở mục 4.

Khuyên chọn Hướng A cho cả tuần, thử Hướng B như một biến thể ads.

## 3. Từng bài trong 7 ngày (Hướng A)

### T2 05/10: Mở màn, vấn đề + ẩn dụ nhân viên mới (ảnh đơn)
- Kích thước: 1080x1350. Mẫu dựng sẵn: `mau/t2-mo-man.html` / `.png`.
- Bố cục từ trên xuống: (1) thanh clay 16px; nhãn "Thứ Hai · Mở màn tuần này"; (2) tiêu đề serif 88px, hai chữ cuối tô clayd; (3) hai thẻ chồng dọc: đỏ nhạt "GIAO VIỆC MƠ HỒ" + “Làm cho tôi cái báo cáo”, teal nhạt "GIAO VIỆC RÕ" + câu báo cáo doanh thu tháng 8; (4) câu chốt in đậm, "rất nhanh" màu teal; (5) chân ảnh có tên khoá và tuyên bố độc lập.
- Chữ: Tiêu đề "Dùng AI vẫn mệt? Hãy giao việc như với nhân viên mới." (11 chữ). Câu chốt: "Claude là nhân viên mới rất nhanh. Giao việc rõ, kiểm tra kỹ."
- Prompt ảnh AI (chỉ nếu muốn thêm ảnh minh hoạ, không thay bản HTML): xem mục 4, hướng B.

### T3 06/10: Bản đồ nút / giao diện (ảnh đơn)
- Kích thước: 1080x1350.
- Bố cục: tiêu đề trên; giữa là ảnh chụp màn hình giao diện Claude đã đơn giản hoá, tự vẽ bằng khối (không chụp nguyên giao diện chính thức, không logo), có 4 đánh số tròn clay chỉ vào: Ô nhập tin nhắn, Nút Đính kèm, Hộp xin phép (Cho phép/Từ chối), Nút Dừng. Dưới là 4 dòng chú thích ngắn.
- Chữ: Tiêu đề "Nhiều nút quá? Nhớ 4 nút này là đủ bắt đầu." (11 chữ). Chú thích lấy từ khoá: "Ô nhập: nói việc bằng tiếng Việt" · "Đính kèm: đưa file, ảnh cho Claude đọc" · "Cho phép / Từ chối: Claude hỏi trước khi làm" · "Dừng: Claude sai hướng thì dừng ngay". Ghi chú nhỏ cuối: "Khoá có 20 slide bản đồ nút."
- Cần xác nhận với sếp: giao diện đúng là của app nào, có thể trích hình ở mức nào. Nếu không chắc, giữ hình vẽ khối đơn giản như trên.
- Prompt AI: không cần (vẽ bằng HTML/SVG). Nếu dùng nền: "flat vector, empty light beige desktop app window mockup, no text, no logo, simple rounded rectangles, soft shadow, 4:5, warm palette #F3F1EE #C96442 #1F6F6B".

### T4 07/10: Công thức 5 dòng (carousel 6 slide)
- Kích thước: 6 slide 1080x1350. Mẫu dựng sẵn: `mau/t4-carousel-cong-thuc-5-dong.html` và `mau/t4-slide-1..6.png`.
| Slide | Nội dung | Bố cục |
|---|---|---|
| 1 | Tiêu đề "5 dòng giúp Claude làm đúng việc"; phụ "Công thức giao việc cho nhân viên mới rất nhanh. Mất 1 phút viết, đỡ nhiều lần sửa."; 5 nhãn teal: Mục tiêu, Ai dùng, Kết quả, Hạn chót, Ràng buộc; "Vuốt để xem ví dụ →" | bìa, chữ 118px |
| 2 | "Một dòng mơ hồ": thẻ đỏ nhạt “Làm cho tôi cái báo cáo”; "Claude phải đoán: báo cáo gì, cho ai, dài bao nhiêu." | trước |
| 3 | "5 dòng, theo thứ tự này": 5 thẻ số 1..5 với mô tả (Việc cần đạt được; Ai sẽ đọc, dùng kết quả; File Excel, email, bản báo cáo?; Cần xong lúc nào; Thứ không được làm, giới hạn) | danh sách |
| 4 | "Cùng việc đó, viết lại": 5 thẻ đã điền: Báo cáo doanh thu tháng 8 · Giám đốc · 1 bảng và 3 nhận xét · Trước 5 giờ chiều · Không dùng số liệu ước đoán | điền mẫu, số màu teal |
| 5 | "Gộp lại thành một câu": thẻ teal với câu đầy đủ; "Claude làm nhanh. Anh chị vẫn là người đọc kỹ, kiểm tra số liệu rồi mới dùng." | sau |
| 6 | "Công thức này là 1 trong 100 slide" · khối clay "Nhắn tin để nhận khoá" + `[LINK ĐĂNG KÝ]` + `Giá: [GIÁ] · Hạn ưu đãi: [HẠN ƯU ĐÃI]` · tuyên bố độc lập | CTA |
- Lưu ý: slide 5 dùng xưng "anh chị"; nếu bài-viết dùng "bạn" thì đổi một chỗ này.
- Ví dụ và 5 dòng lấy đúng từ slide "Công thức giao việc 5 dòng" của khoá.

### T5 08/10: An toàn, khi nào Cho phép / Từ chối (ảnh đơn)
- Kích thước: 1080x1350.
- Bố cục: tiêu đề; một hộp xin phép vẽ giữa ảnh (khung trắng bo góc, dòng "Claude xin phép làm việc này", hai nút: "Cho phép" teal, "Từ chối" đỏ #A32D2D); dưới hộp là hai cột: trái "Cho phép khi" (đúng việc anh chị giao, hiểu Claude định làm gì), phải "Từ chối khi" (không hiểu, không chắc); dải amber cuối ảnh "Từ chối không làm hỏng gì."
- Chữ: Tiêu đề "Hộp xin phép hiện lên: bấm gì?" (7 chữ). Phụ: "Không chắc thì Từ chối, rồi hỏi lại Claude." Dải cuối: "Claude soạn, người duyệt, người bấm gửi."
- Không nói quá tay, không hứa bảo mật; chỉ nói quy tắc dùng.
- Prompt AI: không cần. Nếu muốn nền: "flat vector, calm abstract shield and checklist shapes, no text, no logo, beige background #F3F1EE with teal #1F6F6B and amber #BA7517 accents, 4:5".

### T6 09/10: Quy trình làm dự án 5 bước (infographic 1 ảnh)
- Kích thước: 1080x1350 (1 ảnh dọc, 5 bậc thang đi xuống). Phương án khác: carousel 6 slide, bìa + mỗi bước một slide, cùng kiểu với T4.
- Bố cục: tiêu đề; 5 thẻ nối bằng mũi tên dọc, số tròn clay: 1 Ý tưởng (viết 5 dòng tóm tắt) · 2 Kế hoạch (chia bước, so sánh cách làm) · 3 Làm từng bước (mỗi bước một kết quả) · 4 Chỉnh sửa (chỉ chỗ sai, sửa đúng chỗ) · 5 Chốt và lưu (cập nhật sổ tay, sao lưu). Mũi tên vòng nhỏ giữa 3 và 4 ghi "lặp lại".
- Chữ: Tiêu đề "Làm dự án với Claude: 5 bước, không quên, không lặp." (11 chữ). Chân: nút CTA mềm "Nhắn tin để xem ví dụ báo cáo tháng".
- Chốt ví dụ: báo cáo tháng (theo nghiên cứu). Không số liệu.

### T7 10/10: Bên trong khoá, 8 phần 100 slide (ảnh hoặc video ngắn quay màn hình)
- Kích thước: ảnh 1080x1350; video dọc 1080x1920 hoặc 1080x1350, 15–25 giây.
- Ảnh: lưới 8 ô số theo đúng khoá: Mở đầu, làm quen (8) · Bản đồ nút, thanh công cụ (20) · Cách viết yêu cầu (15) · Nguyên tắc an toàn (12) · Quy trình làm dự án (12) · Ứng dụng cho công ty (15) · Bài tập thực hành (13) · Tổng kết, kiểm tra (5). Màu ô theo nhóm Hiểu/Làm/An toàn. Dải dưới: "Slide bấm và gõ được · Bản PowerPoint sửa được · Chạy không cần mạng".
- Video: quay màn hình khoá (index.html): bìa → mục lục → slide Bản đồ nút → slide Công thức 5 dòng → slide Hộp xin phép → bài tập có khung gõ. Mỗi cảnh 3–4 giây, chữ phủ 1 dòng ≤ 6 chữ ("Bấm được", "Gõ được", "Sửa được"). Thêm cảnh cuối CTA `[LINK ĐĂNG KÝ]`. Cảnh quay cần có chữ phụ đề (nhiều người xem tắt tiếng).
- Chữ: Tiêu đề "Bên trong khoá: 8 phần, 100 slide, có bài tập." (10 chữ).
- Nếu hình thức học chưa chốt (tự học/lớp), đừng ghi, chờ sếp.

### CN 11/10: Câu hỏi hay gặp + chốt (ảnh đơn)
- Kích thước: 1080x1350.
- Bố cục: tiêu đề; 4 thẻ hỏi–đáp ngắn xếp dọc; dưới là khối CTA clay.
- Chữ: Tiêu đề "Còn băn khoăn? Anh chị hỏi, mình trả lời." (9 chữ). Thẻ (cần khớp bài-viết): "Có cần biết tiếng Anh không?" → `[CHỜ XÁC NHẬN]` · "Có cần trả tiền gói Claude không?" → "Bài tập thiết kế làm vừa gói miễn phí." · "Học trên máy hay cần mạng?" → "Slide chạy trên máy, không cần mạng." · "Dùng cho cả phòng được không?" → "Có bản PowerPoint sửa được." CTA: "Nhắn tin để nhận khoá · `[LINK ĐĂNG KÝ]` · `[HẠN ƯU ĐÃI]`".
- Đáp án về tiếng Việt: để chờ xác nhận (nghiên-cứu ghi chưa rõ giao diện Claude tiếng Việt đến đâu), đừng in khi chưa chắc.

### Ads mẫu 1080x1080
- File: `mau/ads-1080.html` / `ads-1080.png`.
- Bố cục: nhãn "Khoá cho dân văn phòng" · tiêu đề serif 92px · ba ô màu Hiểu (clay) / Làm (teal) / An toàn (amber) với một dòng phụ · nút CTA clay "Nhắn tin nhận khoá · [LINK ĐĂNG KÝ]" · chân: "8 phần, 100 slide, có bài tập. Giá [GIÁ]." + tuyên bố độc lập.
- Chữ: "Giao việc rõ, kiểm tra kỹ. Dùng Claude yên tâm hơn." (10 chữ).
- Biến thể test: (1) tiêu đề vấn đề "Dùng AI vẫn mệt?" (như T2); (2) tiêu đề an toàn "Cho phép hay Từ chối?" (như T5); (3) hướng B có ảnh người. Giữ chân ảnh y nguyên. Chữ trên ảnh ads nên ≤ 20% diện tích là tuỳ chính sách Meta hiện hành; kiểm lại trước khi chạy.

## 4. Prompt ảnh AI (tiếng Anh)

Dùng cho Hướng B hoặc nền minh hoạ. Luôn thêm chữ vào bằng HTML sau, không để AI tự viết chữ (AI hay sai dấu tiếng Việt).

**B1: T2 / ads, "nhân viên mới" (ảnh dọc 4:5)**
```
Flat editorial illustration, warm beige background (#F3F1EE). A Vietnamese office worker in a light shirt sits at a laptop on a tidy desk and hands a neatly written checklist on paper to a friendly abstract "new colleague" shown as a simple rounded teal (#1F6F6B) figure with a soft round head and a small clay-orange (#C96442) accent, no face details, no logo, no brand symbols. Speech-bubble-free, no text, no letters, no numbers. Clean geometric shapes, soft shadows, generous empty space at the top third for a headline. Warm, calm, practical mood. 4:5 vertical, 1080x1350.
Negative prompt: text, letters, watermark, logo, sunburst or star symbol, robot with glowing eyes, futuristic neon, realistic faces, extra fingers.
```

**B2: T5, an toàn, không doạ**
```
Flat vector illustration, beige background (#F3F1EE). A simple rounded dialog box floating in the center with two blank buttons, one teal (#1F6F6B) and one red (#A32D2D), a small amber (#BA7517) shield beside it. A hand cursor hovering over the red button. No text, no letters, no logos, no padlock cliches, friendly and calm, not alarming. 4:5 vertical, 1080x1350, empty space at top for title.
Negative prompt: text, letters, hacker, skull, red alert siren, dark theme, logo.
```

**B3: T7 / bìa tuần, bàn làm việc**
```
Top-down flat-lay of a tidy Vietnamese office desk: laptop showing a blank slide with colored cards, a notebook with a hand-drawn five-line checklist (scribbles only, no readable text), a cup of coffee, a pen. Warm beige tones with clay-orange (#C96442) and teal (#1F6F6B) accents, soft natural light, minimal, editorial style. No readable text, no logos, no brand marks. 4:5 vertical, 1080x1350, space at the top for a headline.
Negative prompt: readable text, logo, watermark, cluttered, neon, robot.
```

## 5. Việc còn lại / cần sếp quyết
1. Xác nhận cách trích hình giao diện ở T3 (hình tự vẽ hay chụp màn hình thật).
2. `[GIÁ]`, `[LINK ĐĂNG KÝ]`, `[HẠN ƯU ĐÃI]` đang là chỗ trống trong ads và slide cuối T4.
3. Tuyên bố "Khoá học độc lập, không phải sản phẩm chính thức của Anthropic" giữ nguyên trên T2, ads, T4 slide 6, CN.
4. Sau khi biên tập chốt lời, sửa chữ trong HTML rồi chạy lại bước chụp PNG (xem dưới).
5. Đáp án câu hỏi tiếng Việt ở CN chờ xác nhận.

## 6. File mẫu và cách chụp lại
- `mau/t2-mo-man.html`, `mau/t2-mo-man.png` (1080x1350)
- `mau/t4-carousel-cong-thuc-5-dong.html`, `mau/t4-slide-1.png` … `t4-slide-6.png` (mỗi cái 1080x1350)
- `mau/ads-1080.html`, `mau/ads-1080.png` (1080x1080)
- Chụp lại: dùng Playwright (Chromium tại /opt/pw-browsers), viewport rộng 1100, chụp phần tử `#f` (T2), `.slide` (T4), `.frame` (ads). Mở file HTML bằng trình duyệt cũng xem được; mỗi slide là một khung 1080 rộng.

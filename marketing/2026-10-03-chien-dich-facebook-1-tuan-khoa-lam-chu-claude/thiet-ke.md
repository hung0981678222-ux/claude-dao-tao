# Thiết kế: chiến dịch Facebook 7 ngày, khoá "Làm chủ Claude trong công việc"

Ngày: 2026-10-03 · Người làm: Designer · Góc: "Claude là nhân viên mới rất nhanh: giao việc rõ, kiểm tra kỹ"

Chữ trên ảnh theo `bai-viet.md` (mục "Chữ trên ảnh (chốt)" và "Chữ từng slide (chốt)"); đã sửa vòng 1 theo `bien-tap.md`. Mọi nội dung khoá (5 dòng, 5 bước, 5 nguyên tắc) lấy đúng từ `index.html`.

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
5. Chân ảnh luôn có: tên khoá + "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic." (T2, 3 ảnh ads, T4 slide cuối, T7, CN; T3, T5, T6 có thể thu gọn còn dòng thứ hai). Không vẽ nút giả trong ảnh: nút CTA là của Facebook.
6. Không dùng logo Anthropic/Claude, không vẽ lại biểu tượng tia nắng của Claude. Dùng chữ "Claude" bình thường trong câu. Hình minh hoạ dùng hình học đơn giản, người vẽ phẳng, hoặc ảnh chụp màn hình slide của khoá.
7. Không số liệu thống kê, không lời chứng thực, không nêu giá: để `[GIÁ]`, `[LINK ĐĂNG KÝ]`, `[HẠN ƯU ĐÃI]`.
8. Dấu ngoặc kép kiểu “ ” cho câu mẫu giao việc. Xưng hô theo bài viết ("anh chị", không dùng "bạn"); ảnh ưu tiên câu không xưng hô.

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
- Bố cục từ trên xuống: (1) thanh clay 16px; nhãn "Thứ Hai · Mở màn tuần này"; (2) tiêu đề serif 88px, hai chữ cuối tô clayd; (3) hai thẻ chồng dọc: đỏ nhạt "GIAO VIỆC MƠ HỒ" + “Làm cho tôi cái báo cáo”, teal nhạt "GIAO VIỆC RÕ" + câu báo cáo doanh thu tháng 9; (4) câu chốt in đậm, "rất nhanh" màu teal; (5) chân ảnh có tên khoá và câu "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic."
- Chữ: Tiêu đề "Dùng AI vẫn mệt? Hãy giao việc như với nhân viên mới." (12 chữ). Câu chốt: "Claude là nhân viên mới rất nhanh. Giao việc rõ, kiểm tra kỹ."
- Prompt ảnh AI (chỉ nếu muốn thêm ảnh minh hoạ, không thay bản HTML): xem mục 4, hướng B.

### T3 06/10: Bản đồ nút / giao diện (ảnh đơn)
- Kích thước: 1080x1350.
- Bố cục: tiêu đề trên; giữa là hình giao diện đơn giản tự vẽ bằng khối (không chụp giao diện chính thức, không logo), có 3 số tròn clay chỉ vào 3 chỗ: Hộp xin phép (Cho phép/Từ chối), Nút Dừng, Ô nhập tin nhắn. Dưới là 3 dòng chú thích ngắn. Nút Đính kèm chỉ là ghi chú nhỏ trong chú thích ô nhập, không đánh số.
- Chữ: Tiêu đề "Nhiều nút quá? Nhớ 3 chỗ này là đủ bắt đầu." (11 chữ). Chú thích: "Hộp xin phép: Claude hỏi trước khi làm" · "Nút Dừng: Claude sai hướng thì dừng ngay" · "Ô nhập: nói việc bằng tiếng Việt; có file thì Đính kèm". Ghi chú nhỏ cuối: "Khoá có 20 slide bản đồ nút."
- Cần xác nhận với sếp: nếu muốn dùng ảnh chụp giao diện thật thì xin phép trích; mặc định giữ hình vẽ khối.
- Prompt AI: không cần (vẽ bằng HTML/SVG). Nếu dùng nền: "flat vector, empty light beige desktop app window mockup, no text, no logo, simple rounded rectangles, soft shadow, 4:5, warm palette #F3F1EE #C96442 #1F6F6B".

### T4 07/10: Công thức 5 dòng (carousel 7 slide)
- Kích thước: 7 slide 1080x1350. Mẫu dựng sẵn: `mau/t4-carousel-cong-thuc-5-dong.html` và `mau/t4-slide-1..7.png`. Chữ lấy đúng "Chữ từng slide (chốt)" của Bài 3.
- Bố cục chung: pill nhãn + số trang (x/7) ở đầu; vùng nội dung chiếm hết phần còn lại, chia đều theo chiều dọc (không slide nào trống quá ~1/4 chiều cao); tiêu đề 76-124px, chữ thân ≥ 38px.
| Slide | Nội dung | Bố cục |
|---|---|---|
| 1 | "5 dòng giúp Claude làm đúng việc"; phụ "Công thức giao việc cho nhân viên mới rất nhanh. Mất 1 phút viết, đỡ nhiều lần sửa."; 5 nhãn teal; "Vuốt để xem ví dụ" | bìa, tiêu đề 124px |
| 2 | "Một dòng mơ hồ": thẻ đỏ nhạt “Làm cho tôi cái báo cáo”; "Claude phải đoán: báo cáo gì, cho ai, dài bao nhiêu."; 3 thẻ "Báo cáo gì?" · "Cho ai?" · "Dài bao nhiêu?" | trước |
| 3 | "5 dòng, theo thứ tự này": 5 thẻ số 1-5 (Mục tiêu: việc cần đạt được; Ai dùng: ai sẽ đọc kết quả; Kết quả: email, bảng Excel hay báo cáo?; Hạn chót: cần xong lúc nào; Ràng buộc: thứ không được làm, giới hạn) | công thức |
| 4 | "Viết lại cho đủ 5 dòng": 5 thẻ điền (Lập báo cáo doanh thu tháng 9 · Giám đốc đọc · 1 bảng và 3 nhận xét · Trước 5 giờ chiều · Không dùng số liệu ước đoán); chú thích "Đủ người đọc, kết quả, hạn chót, ràng buộc." | sau, số màu teal |
| 5 | "Cùng cách ấy với tin nhắn khách": dòng Trước “Viết tin nhắn cho khách”; 5 thẻ Sau (Mời khách xin báo giá chính thức · Chủ doanh nghiệp nhỏ đọc · 1 tin Zalo ngắn · Gửi trong hôm nay · Giọng lịch sự, không nêu giá); "Cùng 5 thành phần, đổi việc là dùng được." | sau |
| 6 | "Chưa biết viết gì?": khung “Hãy hỏi tôi 3 câu trước khi làm.”; "Để Claude hỏi lại, anh chị chỉ cần trả lời ngắn."; nhãn "Claude có thể hỏi" + 3 thẻ (Mục tiêu là gì? · Ai sẽ đọc? · Cần xong khi nào?) | mẹo |
| 7 | "Viết xong, nhớ đọc lại kết quả trước khi dùng"; "Phần Cách viết yêu cầu trong khoá còn nhiều ví dụ theo từng phòng ban"; khối clay "Lưu bài để dùng lần sau"; "Muốn xem khoá, nhắn tin cho page."; chân ảnh có tuyên bố "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic." | kết, không có [GIÁ], [HẠN ƯU ĐÃI] |
- Khối clay ở slide 7 là chữ nhấn, không phải nút bấm.

### T5 08/10: An toàn, khi nào Cho phép / Từ chối (ảnh đơn)
- Kích thước: 1080x1350.
- Bố cục: tiêu đề; một hộp xin phép vẽ giữa ảnh (khung trắng bo góc, dòng "Claude xin phép làm việc này", hai nút: "Cho phép" teal, "Từ chối" đỏ #A32D2D); dưới hộp là hai cột: trái "Cho phép khi" (đúng việc anh chị giao, hiểu Claude định làm gì), phải "Từ chối khi" (không hiểu, không chắc, thấy việc lạ như xin xoá file); dải amber cuối ảnh "Từ chối không làm hỏng gì."
- Chữ: Tiêu đề "Hộp xin phép hiện lên: bấm gì?" (7 chữ). Phụ: "Không chắc thì Từ chối, rồi hỏi lại Claude." Dải cuối (chốt): "Từ chối không làm hỏng gì." ("3 thói quen" để ở caption, không lên ảnh).
- Không nói quá tay, không hứa bảo mật; chỉ nói quy tắc dùng.
- Prompt AI: không cần. Nếu muốn nền: "flat vector, calm abstract shield and checklist shapes, no text, no logo, beige background #F3F1EE with teal #1F6F6B and amber #BA7517 accents, 4:5".

### T6 09/10: Quy trình làm dự án 5 bước (infographic 1 ảnh)
- Kích thước: chốt 1 ảnh đơn 1080x1350 (5 bậc thang đi xuống), đúng lịch và bài. Không làm carousel.
- Bố cục: tiêu đề; 5 thẻ nối bằng mũi tên dọc, số tròn clay: 1 Ý tưởng (viết 5 dòng tóm tắt) · 2 Kế hoạch (chia bước, so sánh cách làm) · 3 Làm từng bước (mỗi bước một kết quả) · 4 Chỉnh sửa (chỉ chỗ sai, sửa đúng chỗ) · 5 Chốt và lưu (cập nhật sổ tay, sao lưu). Mũi tên vòng nhỏ giữa 3 và 4 ghi "lặp lại".
- Chữ (chốt): Tiêu đề "5 bước từ ý tưởng đến kết quả" (8 chữ). Chân ảnh: "Bình luận XEM KHOÁ để nhận thông tin" (dòng chữ, không vẽ như nút).
- Chốt ví dụ: báo cáo tháng (theo nghiên cứu). Không số liệu.

### T7 10/10: Bên trong khoá, 8 phần 100 slide (ảnh là bản chính; video là tuỳ chọn)
- Kích thước: ảnh 1080x1350 (bản chính theo lịch). Video dọc 15–25 giây chỉ là tuỳ chọn, không có trong lịch.
- Ảnh: lưới 8 ô số theo đúng khoá: Mở đầu, làm quen (8) · Bản đồ nút, thanh công cụ (20) · Cách viết yêu cầu (15) · Nguyên tắc an toàn (12) · Quy trình làm dự án (12) · Ứng dụng cho công ty (15) · Bài tập thực hành (13) · Tổng kết, kiểm tra (5). Màu ô theo nhóm Hiểu/Làm/An toàn. Dải dưới: "Slide bấm và gõ được · Bản PowerPoint sửa được · Slide chạy không cần mạng". Chân ảnh: "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic."
- Video: quay màn hình khoá (index.html): bìa → mục lục → slide Bản đồ nút → slide Công thức 5 dòng → slide Hộp xin phép → bài tập có khung gõ. Mỗi cảnh 3–4 giây, chữ phủ 1 dòng ≤ 6 chữ ("Bấm được", "Gõ được", "Sửa được"). Thêm cảnh cuối CTA `[LINK ĐĂNG KÝ]`. Cảnh quay cần có chữ phụ đề (nhiều người xem tắt tiếng).
- Chữ (chốt): Tiêu đề "Bên trong khoá: 8 phần, 100 slide, có bài tập." (10 chữ).
- Nếu hình thức học chưa chốt (tự học/lớp), đừng ghi, chờ sếp.

### CN 11/10: Câu hỏi hay gặp + chốt (ảnh đơn)
- Kích thước: 1080x1350.
- Bố cục: tiêu đề; 4 thẻ hỏi–đáp ngắn xếp dọc; dưới là dòng CTA chữ (không vẽ như nút).
- Chữ (chốt theo bài 7): Tiêu đề "Còn phân vân? Mình trả lời trước vài câu hỏi hay gặp." (12 chữ; nếu chật rút còn "Còn phân vân? Mình trả lời trước."). 4 thẻ: "Mới dùng AI có theo được không?" · "Có cần trả tiền gói Claude không?" · "Dùng cho cả phòng được không?" · "Đây có phải khoá chính thức của Anthropic không? Không." (ý trả lời cho thẻ 1-3 lấy từ bài 7: học từ dễ đến khó; bài tập vừa gói miễn phí; có PowerPoint sửa được). CTA chân ảnh: "Đăng ký tại [LINK ĐĂNG KÝ] trước [HẠN ƯU ĐÃI]". Chân ảnh: "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic."
- Không có thẻ tiếng Anh, không có [CHỜ XÁC NHẬN]. Chỗ trống dùng chung 5 tên: [ĐƠN VỊ], [GIÁ], [LINK ĐĂNG KÝ], [HẠN ƯU ĐÃI], [HÌNH THỨC HỌC].

### Ads 3 hình 1080x1080 (theo 3 mẫu ads trong bai-viet.md)
- File: `mau/ads-a.html/.png`, `mau/ads-b.html/.png`, `mau/ads-c.html/.png`. Cùng bố cục: nhãn "Khoá cho dân văn phòng" · tiêu đề serif lớn · dòng phụ · khối minh hoạ phía dưới · chân ảnh (tên khoá, "8 phần, 100 slide, có bài tập", câu tuyên bố). Không vẽ nút, không giá. Chỉ đổi chữ và khối minh hoạ để A/B test sạch.
| Hình | Chữ trên ảnh (chốt) | Dòng phụ | Khối dưới |
|---|---|---|---|
| A | "Claude: nhân viên mới rất nhanh" | Giao việc rõ, kiểm tra kỹ. | 3 ô Hiểu / Làm / An toàn |
| B | "Không chắc thì Từ chối" | Từ chối không làm hỏng gì. | 2 thẻ "Cho phép khi" / "Từ chối khi" (thẻ phẳng, không giống nút) |
| C | "Mục tiêu · Ai dùng · Kết quả · Hạn chót · Ràng buộc" | Công thức 5 dòng để giao việc cho AI. | thẻ ví dụ báo cáo tháng 9 đủ 5 thành phần |
- Cả 3 cùng nút Facebook "Tìm hiểu thêm" và cùng đích [LINK ĐĂNG KÝ]; nút do Facebook hiển thị, không vẽ trong ảnh. Không dùng "yên tâm hơn".
- Biến thể hướng B (có ảnh người) chỉ thử sau khi 3 hình trên có kết quả. Chữ trên ảnh ads nên ≤ 20% diện tích là tuỳ chính sách Meta hiện hành; kiểm lại trước khi chạy.

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
2. Điền [ĐƠN VỊ] (có trên mọi ảnh nhắc khoá), [LINK ĐĂNG KÝ], [HẠN ƯU ĐÃI] (CN), [GIÁ] và [HÌNH THỨC HỌC] (T7 nếu dùng).
3. Sau khi sửa chữ trong HTML, chụp lại PNG (mục 6).

## 6. File mẫu và cách chụp lại
- `mau/t2-mo-man.html`, `mau/t2-mo-man.png` (1080x1350)
- `mau/t4-carousel-cong-thuc-5-dong.html`, `mau/t4-slide-1.png` … `t4-slide-7.png` (mỗi cái 1080x1350)
- `mau/ads-a.html/.png`, `ads-b`, `ads-c` (1080x1080)
- Chụp lại: Playwright (Node, Chromium tại /opt/pw-browsers), viewport rộng 1100, chụp phần tử `#f` (T2), `.slide` (T4), `.frame` (ads). Mở HTML bằng trình duyệt cũng xem được.

## 7. Nhật ký sửa vòng 1

| # | Đã xử lý |
|---|---|
| T1 | Dựng lại carousel T4 thành 7 slide đúng "Chữ từng slide (chốt)"; xoá PNG cũ, chụp `t4-slide-1..7.png`; sửa mục T4 trong file này (tiêu đề, bảng slide). |
| T2 | Đổi "tháng 8" thành "tháng 9" ở T2, T4 slide 4 (và trong mô tả); bỏ câu "lấy đúng từ slide của khoá" cho ví dụ này. |
| T3 | Mục T6: chốt 1 ảnh đơn 1080x1350, bỏ phương án carousel. |
| T4 | Slide T4 dàn đều theo chiều dọc (flex space-between), chữ to hơn (trích dẫn 84px, tiêu đề 80-124px); slide 2 thêm 3 thẻ câu hỏi, slide 6 thêm 3 thẻ; không slide nào trống quá ~1/4 khung. |
| T5 | Mục T3: chốt 3 chỗ (Hộp xin phép, Nút Dừng, Ô nhập), tiêu đề "Nhiều nút quá? Nhớ 3 chỗ này là đủ bắt đầu."; Đính kèm chỉ là ghi chú. |
| T6 | Mục T5: cột "Từ chối khi" thêm "thấy việc lạ, như xin xoá file"; "3 thói quen" để ở caption. Dải cuối theo chữ chốt "Từ chối không làm hỏng gì." |
| T7 | Mục T6: tiêu đề "5 bước từ ý tưởng đến kết quả"; chân ảnh "Bình luận XEM KHOÁ để nhận thông tin". |
| T8 | Mục T7: dải dưới "Slide chạy không cần mạng"; video đánh dấu tuỳ chọn, ảnh là bản chính. |
| T9 | T4 slide cuối: bỏ "học không cần mạng" và dòng [GIÁ]/[HẠN ƯU ĐÃI]; thay bằng "Lưu bài để dùng lần sau" và "Muốn xem khoá, nhắn tin cho page." |
| T10 | Mục CN: bỏ thẻ tiếng Anh và [CHỜ XÁC NHẬN], bỏ thẻ "học trên máy"; dùng 4 thẻ theo bài 7; CTA "Đăng ký tại [LINK ĐĂNG KÝ] trước [HẠN ƯU ĐÃI]". |
| T11 | Chân ảnh thống nhất "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic." (T2, T4 slide 7, 3 ads, T7, CN). |
| T12 | Xoá `ads-1080.*`; dựng 3 hình ads-a/b/c theo 3 mẫu trong bài; bỏ nút giả; bỏ "yên tâm hơn"; bỏ giá khỏi hình. |

Kiểm lần cuối: đã mở xem lại toàn bộ 11 PNG (7 slide T4, T2, 3 ads) sau lần chụp cuối; dấu tiếng Việt đúng, không tràn chữ. Không còn "tháng 8", "học không cần mạng" hay [CHỜ XÁC NHẬN] trong file thiết kế và HTML (còn dòng nhật ký nhắc lại lỗi cũ).

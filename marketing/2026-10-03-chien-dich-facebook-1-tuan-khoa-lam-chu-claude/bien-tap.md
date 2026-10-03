# Biên tập: chiến dịch Facebook 7 ngày, khoá "Làm chủ Claude trong công việc"

Ngày soát: 2026-10-03 · Người soát: Biên tập
Đã đọc: brief, nghien-cuu, lich-dang, bai-viet, thiet-ke, 3 file HTML và 8 PNG trong `mau/`; đối chiếu nội dung khoá với `/home/user/claude-dao-tao/index.html`.

## KẾT LUẬN: CẦN SỬA

Nội dung khoá, giọng văn và các điều cấm (số liệu, lời chứng thực, giá) cơ bản đạt. Chưa duyệt vì còn 5 chỗ lệch chữ và hình ở mức phải làm lại: carousel T4, ví dụ tháng 8 và tháng 9, định dạng T6, chữ trên ảnh các ngày, bố cục slide T4. Ngoài ra còn 2 chỗ sai nội dung khoá ở bài viết và hình, và ads chưa sạch để A/B test. Sửa xong thì gửi lại biên tập soát vòng 2. Chỉ cần soát phần đã sửa.

---

## A. Đã tự sửa trực tiếp trong `bai-viet.md` (lỗi nhỏ)

| # | Vị trí | Lỗi | Đã sửa |
|---|---|---|---|
| A1 | Toàn file (Bài 2 đến 6, 3 mẫu ads) | Câu chân bài "không phải khoá chính thức của Anthropic" khác với brief và `thiet-ke.md` ("sản phẩm chính thức") | Thống nhất thành "không phải sản phẩm chính thức của Anthropic" |
| A2 | Bài 3, đoạn caption cuối | "gửi cho đồng nghiệp hay viết yêu cầu hơi ngắn" (câu lủng củng, dễ hiểu sai) | "gửi cho đồng nghiệp hay gõ yêu cầu quá ngắn" |
| A3 | Bài 1, đoạn "Giao việc rõ..." | "đổi cả cách làm việc với AI" (thổi phồng nhẹ, gần với hứa kết quả) | "Hai việc nhỏ, nhưng làm đều thì khác nhiều." |
| A4 | Bài 1 và Bài 7 | Thiếu dòng chân bài, trong khi `lich-dang.md` quy định mọi bài đều có | Thêm dòng chân bài vào cả hai (Bài 7 trước đó chỉ có câu trả lời trong phần FAQ) |

Đã soát chính tả và dấu tiếng Việt toàn `bai-viet.md`, `lich-dang.md`, `thiet-ke.md`, chữ trong 3 HTML: không còn lỗi dấu hay dấu câu nào khác. Xưng hô nhất quán: page xưng "mình", gọi người đọc "anh chị". Chưa thấy "bạn" lẫn vào.

---

## B. Việc cần giao lại

### B1. Giao `viet-bai` (bài viết)

| # | File, vị trí | Lỗi | Cách sửa |
|---|---|---|---|
| V1 | `bai-viet.md`, Bài 3 (T4), mục "Chữ từng slide" | Bài ghi 7 slide, thiết kế làm 6 slide, nội dung từng slide khác nhau (xem mục C1). Chữ bìa cũng lệch: bài "Gõ ngắn quá, AI phải đoán", thiết kế "5 dòng giúp Claude làm đúng việc". | Viết lại mục "Chữ từng slide" theo bản 7 slide chốt ở mục C1 (chữ lấy theo thiết kế đã dựng, thêm 2 slide mới từ bài). Giữ tiêu đề bài là "Carousel 7 slide". |
| V2 | Bài 3, slide 5 ("Sau" tin nhắn khách) | "Soạn tin Zalo 5 dòng ..." dễ nhầm với "công thức 5 dòng" ngay trong bài nói về 5 dòng. Ví dụ "Sau" cũng chưa đủ 5 thành phần: thiếu hạn chót. | Viết lại ví dụ cho đủ 5 thành phần, tránh chữ "5 dòng" theo nghĩa độ dài. Ví dụ: "Soạn 1 tin Zalo ngắn gửi chủ doanh nghiệp nhỏ, mời xin báo giá chính thức, giọng lịch sự, gửi trong hôm nay, không nêu giá." |
| V3 | Bài 3, slide 7 và caption | Lịch ghi mục tiêu T4 có "bắt đầu nhắn tin", nhưng bài chỉ có CTA lưu và gửi. Thiết kế slide cuối lại có "Nhắn tin để nhận khoá + giá + hạn ưu đãi". | Thêm vào slide 7 và cuối caption một câu mềm: "Muốn xem khoá, nhắn tin cho page." Không đưa [GIÁ] và [HẠN ƯU ĐÃI] vào T4 (lịch chỉ yêu cầu điền từ T7). |
| V4 | Bài 4 (T5), đoạn "Từ chối khi..." | Đúng nội dung khoá, nhưng ghi "Chữ trên ảnh" không khớp thiết kế (mục D). Ngoài ra bài đếm được khoảng 198 chữ (không tính hashtag, chân bài). Nằm trong 80–200 nhưng sát trần và vượt chính quy ước 120–190 của file. | Cắt 10–20 chữ, ví dụ bỏ câu "Mình hay nhớ thế này:" và rút câu cuối đoạn kết. Đồng thời cập nhật "Chữ trên ảnh" theo mục D. |
| V5 | Bài 5 (T6), danh sách 5 bước | Lệch `index.html`, slide "Quy trình làm dự án 5 bước". Khoá: 2 = "Chia bước, so sánh cách làm"; 5 = "Cập nhật sổ tay, sao lưu". Bài viết: 2 = "nhờ Claude đề xuất vài cách làm, anh chị chọn"; 5 = "lưu đúng thư mục, ghi việc tiếp theo". | Viết lại bước 2 và 5 sát khoá (bước 5: cập nhật sổ tay, sao lưu). Bước 1, 3, 4 đã đúng. Ví dụ báo cáo cuối tháng ở đoạn dưới cũng sửa theo ("lưu file và ghi chú" đổi thành "cập nhật sổ tay và sao lưu"). |
| V6 | Bài 5, "Chữ trên ảnh" | Không khớp thiết kế (mục D). | Cập nhật theo mục D. |
| V7 | Bài 6 (T7) và Bài 7 (CN), "Chữ trên ảnh" | Không khớp thiết kế (mục D). Bài 7: thiết kế dùng 4 thẻ hỏi đáp khác với 5 câu trong bài. | Cập nhật theo mục D. |
| V8 | Bài 1 (T2), Bài 2 (T3), "Chữ trên ảnh" | Không khớp thiết kế (mục D). | Cập nhật theo mục D. |
| V9 | Ads, 3 mẫu: ô "CTA button" và "Link" | Ba nút khác nhau (Tìm hiểu thêm / Đăng ký / Gửi tin nhắn) và mẫu C đổi cả đích đến sang inbox. Xem mục E. | Dùng cùng 1 nút và 1 đích cho cả 3 mẫu. Xem khuyến nghị ở mục E. |
| V10 | Ads, "Chữ trên ảnh" mẫu C | "Mục tiêu · Ai dùng · Kết quả · Hạn · Giới hạn" gọi 2 thành phần khác tên trong bài (Hạn chót, Ràng buộc), trong khi khoá cũng dùng cả "Ràng buộc" và "giới hạn". | Dùng đúng tên của công thức: Mục tiêu · Ai dùng · Kết quả · Hạn chót · Ràng buộc. Cả ads primary text mẫu C (hiện ghi "giới hạn", "người đọc") lẫn bài 3 cần nhất quán: chọn "Ràng buộc" làm tên chính, có thể kèm "(giới hạn)" ở lần đầu. |
| V11 | Ads, mô tả mẫu B: "Học cách dùng Claude yên tâm hơn" | "Yên tâm hơn" là hứa kết quả mức nhẹ. Chưa vi phạm điều cấm (không có số), nhưng cần thận trọng với quy định quảng cáo. | Đổi thành "Học thói quen dùng Claude có kiểm soát" (cùng ý với primary text). |
| V12 | Bài 3, hashtag | #VietPromptChoDanVanPhong không có trong danh sách hashtag của nghiên cứu, lẫn Anh–Việt, chưa kiểm. Chính bài viết cũng đánh dấu "có thể bỏ". | Bỏ, thay bằng #HocClaude. |

### B2. Giao `thiet-ke` (thiết kế)

| # | File, vị trí | Lỗi | Cách sửa |
|---|---|---|---|
| T1 | `mau/t4-carousel-cong-thuc-5-dong.html` + `thiet-ke.md` mục T4 | Làm 6 slide, bài viết ghi 7 (mục C1) | Dựng lại thành 7 slide theo bản chốt ở C1, chụp lại 7 PNG `t4-slide-1..7.png` (xoá `t4-slide-6.png` cũ hoặc đổi thành slide 7), sửa `thiet-ke.md` (tiêu đề "carousel 7 slide", bảng slide, mục 6) |
| T2 | `mau/t2-mo-man.html` (+ PNG), `mau/t4-...html` slide 4 và 5 (+ PNG), `thiet-ke.md` mục T2 và T4 | Ví dụ "báo cáo doanh thu **tháng 8**", bài viết dùng "tháng 9" | Đổi thành "tháng 9" ở T2, T4 và mô tả trong `thiet-ke.md`. Bỏ câu "lấy đúng từ slide ... của khoá" cho ví dụ này, vì khoá dùng "tháng 8". Giữ nguyên 5 thành phần. |
| T3 | `thiet-ke.md` mục T6, dòng "Kích thước" | Ghi ảnh dọc hoặc phương án carousel 6 slide; lịch và bài đều ghi ảnh đơn | Bỏ phương án carousel. T6 chốt là 1 ảnh infographic 1080x1350 |
| T4 | `mau/t4-slide-2.png` và `mau/t4-slide-5.png` (HTML slide 2 và 5) | Gần nửa dưới khung 1080x1350 để trống (nội dung kết thúc khoảng y=750 trên slide 2 và y=700 trên slide 5) | Xem mục C2 |
| T5 | `thiet-ke.md` mục T3 | Thiết kế "4 nút" (Ô nhập, Đính kèm, Hộp xin phép, Dừng), tiêu đề "Nhớ 4 nút này". Lịch và bài ghi "3 chỗ" (Hộp xin phép, Nút Dừng, Ô nhập), khoá cũng có slide "3 điểm chạm anh chị cần nhớ nhất". | Chốt 3: bỏ Đính kèm khỏi 3 số tròn (có thể giữ làm ghi chú nhỏ). Tiêu đề: "Nhiều nút quá? Nhớ 3 chỗ này là đủ bắt đầu." |
| T6 | `thiet-ke.md` mục T5 | Cột "Từ chối khi" thiếu ý "thấy việc lạ (ví dụ xin xoá file)" có trong bài và khoá. Chữ trên ảnh chưa nhắc "3 thói quen" mà lịch đã ghi. | Thêm "thấy việc lạ, như xin xoá file" vào cột phải. "3 thói quen" để ở caption bài, không cần lên ảnh. |
| T7 | `thiet-ke.md` mục T6 | Tiêu đề "5 bước, không quên, không lặp" là lời hứa quá đà (không có nguồn). CTA chân ảnh là "Nhắn tin để xem ví dụ báo cáo tháng", bài và lịch mời "Bình luận XEM KHOÁ". | Tiêu đề: "5 bước từ ý tưởng đến kết quả" (đổi theo mục D). CTA: "Bình luận XEM KHOÁ để nhận thông tin". |
| T8 | `thiet-ke.md` mục T7 | Dải dưới "Chạy không cần mạng" dễ hiểu là cả khoá học không cần mạng. Khoá chỉ nói "Slide chạy trên máy, không cần mạng". Phần thử với Claude thật cần mạng. Phương án video 15–25 giây không có trong lịch. | Sửa thành "Slide chạy không cần mạng". Đánh dấu video là tuỳ chọn, ảnh là bản chính theo lịch. |
| T9 | `mau/t4-slide-6.png` / HTML slide 6 | "8 phần, có bài tập thực hành, **học không cần mạng**": sai như T8. Ngoài ra có [GIÁ] và [HẠN ƯU ĐÃI] sớm hơn lịch. | Sửa thành "slide chạy không cần mạng". Bỏ dòng Giá/Hạn ưu đãi (V3). |
| T10 | `thiet-ke.md` mục CN | Thẻ "Có cần biết tiếng Anh không? → [CHỜ XÁC NHẬN]": chỗ trống mới, không thống nhất với 5 chỗ trống chung, và bài không có câu này. Thẻ "Học trên máy hay cần mạng?" cũng không có trong bài. CTA "Nhắn tin để nhận khoá", bài viết là "Đăng ký tại [LINK ĐĂNG KÝ] trước [HẠN ƯU ĐÃI]". | Bỏ thẻ tiếng Anh. Dùng 4 thẻ khớp bài (xem mục D, CN). Không đưa chỗ trống mới. CTA theo bài. |
| T11 | `thiet-ke.md`, tuyên bố chân ảnh | Thiết kế: "Khoá học độc lập, không phải sản phẩm chính thức của Anthropic." Bài viết: "Khoá do [ĐƠN VỊ] biên soạn, ...". Hai câu khác nhau, và hình chưa có [ĐƠN VỊ]. | Dùng câu thống nhất: "Khoá do [ĐƠN VỊ] biên soạn, không phải sản phẩm chính thức của Anthropic." Áp dụng cho T2, ads, T4 slide cuối, T7, CN (các ảnh nhắc khoá). |
| T12 | `mau/ads-1080.html` + `thiet-ke.md` mục Ads | (a) Có "nút" giả "Nhắn tin nhận khoá · [LINK ĐĂNG KÝ]" trong hình, trùng và mâu thuẫn với nút CTA thật của Facebook. (b) Chỉ có 1 hình, còn "chữ trên ảnh" của 3 mẫu ads trong bài là 3 câu khác nhau. Biến thể trong thiết kế ("Dùng AI vẫn mệt?", "Cho phép hay Từ chối?") không trùng với bài. (c) Tiêu đề hình "Dùng Claude yên tâm hơn": hứa nhẹ (như V11). | Bỏ nút giả; thay bằng dòng chữ không giống nút hoặc bỏ hẳn. Dựng 3 hình cùng bố cục cho 3 mẫu, mỗi hình một chữ theo bài (mục D, Ads). Đổi "yên tâm hơn" thành "có kiểm soát". |

> `lich-dang.md`: không có lỗi nội dung riêng. Chỉ cần cập nhật dòng T4 nếu chốt khác 7 slide, và dòng ads "3 nhóm ... chỉ khác nội dung" (đã đúng với mục E). `nghien-cuu.md` (R&D) có cụm "học không cần mạng", "chạy không cần mạng" ở mục 4: chỉ là nghiên cứu nội bộ, nhưng nhắc R&D ghi "slide chạy không cần mạng" để không ai chép nguyên văn lên bài.

---

## C. Hai lệch lớn nhất: carousel T4

### C1. Xác nhận: 7 slide (bài, lịch) và 6 slide (thiết kế), nội dung từng slide khác nhau

| Slide | Bài viết | Thiết kế đã dựng |
|---|---|---|
| 1 | Bìa "Gõ ngắn quá, AI phải đoán" | Bìa "5 dòng giúp Claude làm đúng việc" + 5 nhãn |
| 2 | Trước: "Làm cho tôi cái báo cáo" | Trước: cùng câu, thêm chú thích |
| 3 | Công thức 5 dòng | Công thức 5 dòng (khớp) |
| 4 | Sau: câu gộp báo cáo tháng 9 | 5 thẻ điền đủ (báo cáo tháng 8) |
| 5 | Sau: tin nhắn khách | Gộp một câu (báo cáo tháng 8) |
| 6 | Mẹo "Hãy hỏi tôi 3 câu trước khi làm" | CTA: 1 trong 100 slide |
| 7 | Kết + CTA | không có |

Hai lệch lớn: (1) thiết kế thiếu ví dụ tin nhắn khách và mẹo "hỏi tôi 3 câu" mà caption bài đã hứa ("Vuốt qua xem thêm ví dụ trước và sau", "Chưa biết viết gì thì cứ gõ ..."); (2) thiết kế có 2 slide cùng về báo cáo (4 và 5) mà bài chỉ có một.

**Bản chốt đề xuất (7 slide, giữ tối đa phần đã dựng):**

1. Bìa: giữ nguyên bản thiết kế ("5 dòng giúp Claude làm đúng việc", phụ "Công thức giao việc cho nhân viên mới rất nhanh. Mất 1 phút viết, đỡ nhiều lần sửa.", 5 nhãn, "Vuốt để xem ví dụ").
2. Trước: giữ bản thiết kế ("Một dòng mơ hồ", “Làm cho tôi cái báo cáo”, "Claude phải đoán: báo cáo gì, cho ai, dài bao nhiêu.").
3. Công thức: giữ bản thiết kế ("5 dòng, theo thứ tự này", 5 thẻ). Chữ khớp khoá và bài.
4. Sau, ví dụ báo cáo: dùng bản thiết kế slide 4 (5 thẻ điền) với **tháng 9**, thêm chú thích "Đủ người đọc, kết quả, hạn, giới hạn." (chữ này của bài). Câu gộp đầy đủ để trong caption, đúng như bài đang làm.
5. Sau, ví dụ tin nhắn khách: **mới**, theo mẫu 5 thẻ như slide 4 hoặc cặp Trước/Sau ngắn. Chữ do viet-bai viết lại ở V2.
6. Mẹo: **mới**. “Hãy hỏi tôi 3 câu trước khi làm” + "Để Claude hỏi lại, anh chị chỉ cần trả lời ngắn." (khớp khoá, slide "Để Claude hỏi lại anh").
7. Kết: "Viết xong, nhớ đọc lại kết quả trước khi dùng" · "Phần Cách viết yêu cầu trong khoá còn nhiều ví dụ theo từng phòng ban" · "Lưu bài để dùng lần sau" · dòng mềm "Muốn xem khoá, nhắn tin cho page" · chân ảnh tuyên bố độc lập (T11). Không có Giá và Hạn ưu đãi.

Slide gộp một câu cũ (thiết kế slide 5) bị bỏ; câu "Claude làm nhanh. Anh chị vẫn là người đọc kỹ, kiểm tra số liệu rồi mới dùng." chuyển sang slide 7, thay cho dòng "Viết xong, nhớ đọc lại kết quả..." nếu thiết kế thấy chật.

Lý do chọn 7 chứ không rút bài về 6: lịch và caption đã hứa 7 slide, và hai slide mới (tin nhắn khách, hỏi lại 3 câu) là phần có ích nhất để người xem lưu bài.

### C2. Bố cục slide 2 và 5: xác nhận trống gần nửa dưới

Đã xem PNG: slide 2 nội dung dừng khoảng y=740 trên khung 1350, slide 5 dừng khoảng y=700. Cách sửa (áp dụng cho slide 2, slide 6 mẹo mới, và slide 5 mới nếu dùng bố cục thưa):

- Tăng cỡ chữ: thẻ trích dẫn từ 56px lên 76–84px (đúng quy tắc tiêu đề của chính thiết kế: ≥76px), chú thích từ 46px lên 52–56px.
- Giãn đều theo chiều dọc: đặt các khối trong flex `justify-content: space-between` hoặc chia vùng nội dung 3 phần đều thay vì dồn lên trên.
- Thêm một phần tử có ích nằm nửa dưới. Với slide 2: thẻ "Claude hiểu thế nào?" liệt kê 3 câu hỏi nó phải đoán (Báo cáo gì? Cho ai? Dài bao nhiêu?) dưới dạng 3 thẻ, thay vì một dòng chữ. Với slide mẹo: lặp lại 3 câu hỏi Claude có thể hỏi lại, dạng thẻ.
- Không thêm số liệu hay ảnh có logo.

---

## D. Chữ trên ảnh (`thiet-ke.md`) so với "Chữ trên ảnh" (`bai-viet.md`)

Nguyên tắc chọn: lấy bản thiết kế khi bản đó đã dựng và đúng khoá. Chỉ đổi bản thiết kế khi nó sai khoá hoặc hứa quá đà. Hình thức: bên bị lệch sửa theo bên còn lại.

| Ngày | Bài viết ghi | Thiết kế ghi | Chốt | Ai sửa |
|---|---|---|---|---|
| T2 | "AI làm chưa đúng ý? Có thể do cách giao việc" | "Dùng AI vẫn mệt? Hãy giao việc như với nhân viên mới." (đã dựng PNG) | Lấy thiết kế (khớp ẩn dụ và chủ đề lịch) | viet-bai |
| T3 | "3 nút cần nhớ khi mới dùng Claude" | "Nhiều nút quá? Nhớ 4 nút này là đủ bắt đầu." | "Nhiều nút quá? Nhớ 3 chỗ này là đủ bắt đầu." (T5 ở bảng B2) | thiet-ke sửa; viet-bai cập nhật theo |
| T4 | Xem C1 | Xem C1 | Bản 7 slide | viet-bai và thiet-ke |
| T5 | "Không chắc thì Từ chối. Không hỏng gì." | Tiêu đề "Hộp xin phép hiện lên: bấm gì?"; phụ "Không chắc thì Từ chối, rồi hỏi lại Claude."; dải "Từ chối không làm hỏng gì." | Lấy thiết kế. Thiết kế đã chứa cả ý của bài. | viet-bai |
| T6 | "5 bước từ ý tưởng đến kết quả" | "Làm dự án với Claude: 5 bước, không quên, không lặp." | "5 bước từ ý tưởng đến kết quả" (ngắn hơn, không hứa quá) | thiet-ke sửa (T7 ở bảng B2) |
| T7 | "8 phần, 100 slide, học bằng làm" | "Bên trong khoá: 8 phần, 100 slide, có bài tập." | Lấy thiết kế (nói rõ bài tập) | viet-bai |
| CN | "Còn phân vân? Hỏi trước, học sau" | "Còn băn khoăn? Anh chị hỏi, mình trả lời." + 4 thẻ khác bài | Tiêu đề: "Còn phân vân? Mình trả lời trước vài câu hỏi hay gặp." (khớp câu mở bài, 12 chữ). 4 thẻ: Mới dùng AI có theo được không? · Có cần trả tiền gói Claude không? · Dùng cho cả phòng được không? · Đây có phải khoá chính thức của Anthropic không? (Không.). CTA theo bài (Đăng ký tại [LINK ĐĂNG KÝ] trước [HẠN ƯU ĐÃI]). | thiet-ke sửa; viet-bai cập nhật theo |
| Ads A | "Claude: nhân viên mới rất nhanh" | 1 hình chung "Giao việc rõ, kiểm tra kỹ. Dùng Claude yên tâm hơn." | 3 hình theo bài (T12); tiêu đề hình A thay "yên tâm hơn" | thiet-ke |
| Ads B | "Không chắc thì Từ chối" | Biến thể "Cho phép hay Từ chối?" | Theo bài | thiet-ke |
| Ads C | "Mục tiêu · Ai dùng · Kết quả · Hạn · Giới hạn" | Không có biến thể | Theo V10 (dùng đủ tên) | thiet-ke và viet-bai |

Ghi chú: quy tắc thiết kế "tiêu đề ≤ 12 chữ": T2 (11), T3 (11), T5 (7), T7 (10), CN (12 nếu giữ bản chốt) đều đạt; nếu CN dài hơn thì thiet-ke rút còn "Còn phân vân? Mình trả lời trước." (6 chữ).

---

## E. Kiểm tra theo từng mục yêu cầu

### 1. Chính tả, giọng văn, xưng hô
- Đạt (xem A). Giọng thân thiện, ví dụ việc văn phòng (email, báo cáo, tóm tắt họp), không giật gân "AI thay thế". "Anh chị" nhất quán, "mình" là page. Ảnh ưu tiên câu không xưng hô; chỉ slide 5 cũ có "Anh chị" (sẽ bỏ ở C1).
- Chưa ghi giọng sai thương hiệu nào.

### 2. Khớp nội dung khoá với `index.html`
| Điểm | Khoá | Chiến dịch | Kết quả |
|---|---|---|---|
| 8 phần, 100 slide | 8+20+15+12+12+15+13+5 = 100 | Bài 6, T7, ads, brief đều đúng; lưới T7 liệt kê đúng 8 phần và số slide | Đạt |
| Công thức 5 dòng | Mục tiêu · Ai dùng · Kết quả · Hạn chót · Ràng buộc | Bài 3, slide 1 và 3 thiết kế: đủ 5, đúng tên. Ads C và chữ ảnh ads C: tên lệch | Đạt, trừ V10 |
| Quy trình 5 bước | Ý tưởng · Kế hoạch · Làm từng bước · Chỉnh sửa · Chốt và lưu | Thiết kế T6 đúng. Bài 5 lệch ở bước 2 và 5 | Cần sửa (V5) |
| Nguyên tắc an toàn | 5 nguyên tắc | Bài 4 dùng "3 thói quen nhỏ" (tập con: mật khẩu/OTP/thẻ; che dữ liệu nhạy cảm; kiểm tra kết quả + người bấm gửi). Không sai, không gọi nhầm là "5 nguyên tắc". Thiết kế không đưa "5 nguyên tắc" lên ảnh dù ghi chú đầu file có nhắc | Đạt |
| 3 chỗ cần nhớ | Hộp xin phép, Nút Dừng, Ô nhập | Bài 2 và lịch đúng 3. Thiết kế 4 | Cần sửa (T5) |
| "Không cần mạng" | Chỉ "Slide chạy trên máy, không cần mạng" | Bài 6, bài 7 và thiết kế CN đúng. Lệch ở T4 slide 6 và T7 | Cần sửa (T8, T9) |
| 6 bài tập, bản PowerPoint sửa được, giới hạn gói miễn phí | Đều có trong khoá | Bài 6, bài 7 đúng | Đạt |
| Mẹo "Hãy hỏi tôi 3 câu trước khi làm" | Có (slide "Để Claude hỏi lại anh") | Bài 3 dùng đúng | Đạt |
| Ví dụ báo cáo | Khoá dùng "tháng 8" | Chiến dịch chốt "tháng 9" (yêu cầu của trưởng phòng). Chấp nhận, vì đây là ví dụ minh hoạ chứ không phải trích dẫn khoá; chỉ cần bỏ câu "lấy đúng từ slide" (T2) | Chấp nhận có điều kiện |

### 3. Số liệu, lời chứng thực, hứa kết quả, chỗ trống
- Không có số liệu thống kê, lời chứng thực, số người đã học trong `bai-viet.md`, `thiet-ke.md`, các mẫu HTML/PNG. Số duy nhất là thông tin khoá (8 phần, 100 slide, 20 slide bản đồ nút, 6 bài tập), đều có trong `index.html`. Các số trong `nghien-cuu.md` (38%, 90%...) không bị đưa lên bài: đạt. Đã gạch đỏ: không có số nào cần gạch.
- Có dòng "không phải sản phẩm chính thức của Anthropic" ở Bài 2 đến 7, 3 mẫu ads, T2, ads, T4 slide cuối, CN. Bài 1 và Bài 7 đã được thêm (A4). Còn lại cần đồng bộ T11.
- Hứa quá đà (đã xử lý hoặc giao sửa): "đổi cả cách làm việc với AI" (A3, đã sửa); "5 bước, không quên, không lặp" (T7); "Dùng Claude yên tâm hơn" và "học cách dùng Claude yên tâm hơn" (V11, T12). Ba câu "Mất 1 phút viết, đỡ nhiều lần sửa" lấy từ khoá nên giữ.
- Chỗ trống: bài viết dùng [ĐƠN VỊ], [GIÁ], [LINK ĐĂNG KÝ], [HẠN ƯU ĐÃI], [HÌNH THỨC HỌC]; thiết kế dùng thêm [CHỜ XÁC NHẬN] (T10) và chưa có [ĐƠN VỊ] (T11). Sau khi sửa thì 5 tên này thống nhất. Brief chỉ liệt kê 3 chỗ trống đầu; hai cái còn lại là bổ sung hợp lý.
- Điều cấm khác: không dùng logo Anthropic (đã soát 3 HTML, không có), không công kích khoá khác, không nêu giá.

### 4. Khớp chữ và hình
Xem C và D. Ngoài ra đã đối chiếu từng ảnh PNG với HTML: chữ trong PNG và HTML khớp nhau. Không có lỗi hiển thị dấu tiếng Việt. Bản PNG dùng font thay thế (Liberation), nên hình dáng chữ khác Cambria nhưng bố cục không đổi (thiết kế đã ghi chú).

### 5. Độ dài bài và headline ads
- Bài T5 (Bài 4): đếm khoảng 198 chữ (không tính hashtag và chân bài). Nằm trong 80–200 nhưng sát trần; xem V4.
- Bài CN (Bài 7): đếm khoảng 169 chữ. Đạt.
- Các bài còn lại ước lượng 120–180 chữ: đạt (chưa đếm từng chữ).
- Headline ads: Mẫu A "Giao việc rõ cho Claude, kiểm tra kỹ" = 36 ký tự; Mẫu B "Khi nào Cho phép, khi nào Từ chối?" = 34; Mẫu C "Công thức 5 dòng để giao việc cho AI" = 36. Cả ba ≤ 40: đạt. Đã đếm lại câu đầu primary text: A = 94, B = 101, C = 95 ký tự (đúng số bài ghi, đều < 125).

### 6. Ads: nên dùng 1 nút CTA cho cả 3 mẫu? Có.
Hiện A = "Tìm hiểu thêm" (link), B = "Đăng ký" (link), C = "Gửi tin nhắn" (inbox hoặc link). Mẫu C khác cả đích đến, nên khác biệt kết quả có thể do nút hoặc đích chứ không phải do góc nội dung. Bài viết cũng đã tự cảnh báo điều này.

**Đề xuất:** dùng cùng 1 nút và cùng 1 đích cho cả 3 mẫu.
- Nút: "Tìm hiểu thêm", đích: [LINK ĐĂNG KÝ] (chưa có giá nên cam kết thấp, hợp với người mới; nút "Đăng ký" dễ bị bỏ khi chưa thấy giá).
- Chỉ đổi sang "Gửi tin nhắn" cho cả ba nếu trưởng phòng quyết định lấy nhắn tin làm chỉ số chuyển đổi chính và đã có người trực inbox.
- Giữ cố định: đối tượng, giờ chạy, ngân sách, định dạng hình, bố cục. Chỉ đổi 3 thứ gắn với góc nội dung: primary text, headline, chữ trên ảnh. Việc dựng 3 hình đúng bố cục là T12.
- Thêm vào ghi chú đọc kết quả: chỉ so mỗi cặp trên cùng chỉ số (lượt nhắn tin hoặc đăng ký trên lượt bấm), và đánh giá sau khi mỗi nhóm có số lượng đủ lớn (Meta thường khuyến nghị tối thiểu 50 lượt chuyển đổi/nhóm; trưởng phòng kiểm lại).

---

## F. Khi đạt thì cần gì
1. viet-bai xong V1–V12; thiet-ke xong T1–T12.
2. Chụp lại toàn bộ PNG bị ảnh hưởng: `t2-mo-man.png`, `t4-slide-1..7.png`, 3 hình ads.
3. Biên tập soát vòng 2: chữ ảnh so với bài, 7 slide T4 có mặt đủ, tháng 9 ở cả hai nơi, không còn "tháng 8" hay "học không cần mạng" trong file nào của chiến dịch.

Việc sếp quyết (không thuộc lỗi biên tập): điền [ĐƠN VỊ], [GIÁ], [LINK ĐĂNG KÝ], [HẠN ƯU ĐÃI], [HÌNH THỨC HỌC] trước T7; có người trực inbox cho CTA "XEM KHOÁ" của T6; Bài 7 chỉ dùng "ưu đãi" nếu thật sự có.

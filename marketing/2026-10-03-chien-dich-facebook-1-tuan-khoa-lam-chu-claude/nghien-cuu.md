# Nghiên cứu: chiến dịch Facebook 7 ngày, khoá "Làm chủ Claude trong công việc"

Ngày: 2026-10-03 · Người làm: R&D

Quy ước nhãn: [NGUỒN] = có link; [KN] = kinh nghiệm/giả định, cần test; [CHƯA XÁC MINH] = thấy trong kết quả tìm kiếm nhưng chưa mở được trang gốc (nhiều trang báo bị chặn mạng khi truy cập), nên copywriter chưa dùng làm số liệu in trên bài cho đến khi kiểm lại.

## 1. Tóm tắt 5 dòng
1. Dân văn phòng VN đã dùng AI nhiều (PwC: 38% dùng AI tạo sinh hằng ngày), nên nỗi đau không còn là "chưa biết AI" mà là "dùng chưa bài bản, ngại sai, lo lộ dữ liệu".
2. Mối lo dữ liệu rất lớn (khảo sát Decision Lab: 90% lo AI thu thập dữ liệu không có đồng ý) và phần "Nguyên tắc an toàn" là điểm khoá mình có mà khoá ChatGPT thường không nhấn.
3. Claude chưa có số liệu mức dùng riêng cho dân văn phòng VN. Đừng nói "ai cũng dùng Claude"; hãy định vị là "người mới bắt đầu có hướng dẫn".
4. Đối thủ chủ yếu bán công cụ/mẹo/kiếm tiền, giá thấp (vài trăm nghìn) hoặc lớp ngắn 3 buổi. Khoảng trống: dạy cách giao việc và kiểm tra kết quả, có bài tập thực hành, học không cần mạng.
5. Khuyên chọn góc 1: "Claude là nhân viên mới rất nhanh: giao việc rõ, kiểm tra kỹ". Giờ đăng gợi ý: 11h30–13h và 19h45–21h [KN, có nguồn tham khảo].

## 2. Chân dung khách hàng
Toàn bộ persona là giả định dựng từ brief và số liệu chung; không phải dữ liệu khách thật.

**Persona A: Linh, 27, kế toán/hành chính tổng hợp**
- Việc hằng ngày: soạn email, đối chiếu bảng tính, làm báo cáo cuối tháng.
- Đã thử ChatGPT vài lần, kết quả lúc hay lúc dở nên bỏ.
- Sợ: AI nói sai số liệu mà mình không biết; dán số liệu công ty lên là lộ.
- Muốn: một quy trình cố định để dùng mà yên tâm.

**Persona B: Minh, 33, marketing/sales admin**
- Việc hằng ngày: viết nội dung, tóm tắt họp, làm slide, soạn đề xuất.
- Hay dùng AI nhưng gõ yêu cầu ngắn nên kết quả chung chung, phải sửa nhiều.
- Muốn: viết yêu cầu đúng ngay từ lần đầu; có mẫu dùng lại.

**Persona C: Chị Hà, 38, trưởng nhóm/nhân sự (phụ)**
- Muốn cả nhóm dùng AI đồng đều và an toàn; không có thời gian tự soạn tài liệu đào tạo.
- Lo: nhân viên dán tài liệu nội bộ vào công cụ tuỳ ý.
- Muốn: tài liệu có sẵn, chỉnh được theo công ty (khoá có bản PowerPoint sửa được).

### Nỗi đau / rào cản (cách nói gần với lời khách, [KN])
| Rào cản | Cách khách tự nói | Khoá mình đáp bằng |
|---|---|---|
| Sợ sai | "Lỡ nó bịa số liệu rồi mình gửi sếp thì sao?" | Phần An toàn: kiểm tra kết quả trước khi dùng |
| Sợ lộ dữ liệu | "Dán hợp đồng lên đó có sao không?" | Phần An toàn: khi nào bấm Cho phép/Từ chối |
| Không biết viết yêu cầu | "Gõ gì nó cũng trả lời chung chung" | Công thức 5 dòng giao việc (phần Cách viết yêu cầu) |
| Rối giao diện | "Nhiều nút quá, không biết nút nào làm gì" | Phần Bản đồ nút (20 slide) |
| Rào cản tiếng Anh | "Giao diện/tài liệu toàn tiếng Anh" | Khoá bằng tiếng Việt [giả định: hãy xác nhận giao diện Claude hiển thị ngôn ngữ nào trước khi hứa] |
| Không có thời gian / ngại học dài | "Học xong lại quên" | Slide tương tác, bài tập ngắn làm vừa gói miễn phí |
| Sợ bị cho là lười/bị thay thế | "Dùng AI có bị coi là gian không?" | Giọng bài: AI là trợ lý, người quyết định (không giật gân) |

## 3. Bối cảnh: mức dùng AI và Claude tại VN (chỉ số liệu có nguồn)

| Số liệu | Nguồn | Ghi chú |
|---|---|---|
| 38% người lao động VN dùng AI tạo sinh hằng ngày, trên 2 lần mức trung bình toàn cầu 14%; khảo sát hơn 1.000 người lao động VN | [PwC VN, Hopes and Fears 2025](https://www.pwc.com/vn/en/publications/vietnam-publications/hopes-fears-vietnam-2025.html) | Đọc qua kết quả tìm kiếm; trang chính hãng, nên mở lại để chép nguyên văn |
| 74% cho rằng mình có tiếp cận nguồn học tập/phát triển ở nơi làm việc | cùng nguồn PwC ở trên | Tương đối cho thấy còn khoảng trống đào tạo [KN diễn giải] |
| 78% người dùng internet VN dùng ít nhất một nền tảng AI trong 3 tháng; khảo sát 600 người, cuối 07/2025; nhân viên văn phòng và chủ doanh nghiệp 78%, sinh viên 92% | [Decision Lab qua BrandsVietnam](https://www.brandsvietnam.com/congdong/topic/thoi-quen-su-dung-ai-tai-viet-nam-2025-78-nguoi-dung-internet-tung-tuong-tac-voi-ai) | [CHƯA XÁC MINH] chưa mở trang gốc; mẫu nhỏ (600) |
| Công cụ dùng nhiều: ChatGPT 81%, Gemini 51%, Meta AI 36% | cùng nguồn Decision Lab | [CHƯA XÁC MINH]. Không thấy tỷ lệ Claude. |
| 90% lo AI thu thập/dùng dữ liệu mà không có đồng ý rõ ràng | cùng nguồn Decision Lab; xem thêm [Kenh14](https://kenh14.vn/hon-40-nguoi-dung-quay-lung-voi-chatgpt-va-gemini-vi-lo-ngai-ro-ri-du-lieu-215260319235233859.chn) | [CHƯA XÁC MINH]. Khảo sát người tiêu dùng, không riêng văn phòng |
| 39% lao động tri thức VN là "AI pioneers" (người dùng nâng cao), gấp hơn 2 lần mức toàn cầu 16%; khảo sát 2.000 người; 89% người dùng coi kết quả AI là điểm khởi đầu, không phải đáp án cuối | Microsoft Work Trend Index 2026 ([bản tiếng Việt](https://news.microsoft.com/source/asia/2026/06/24/bao-cao-chi-so-xu-huong-cong-viec-nam-2026-luc-luong-lao-dong-viet-nam-da-san-sang-cho-ky-nguyen-ai-doanh-nghiep-can-chuyen-minh-de-but-pha/?lang=vi); tóm tắt thứ cấp: [Windows News](https://windowsnews.ai/article/39-of-vietnams-knowledge-workers-are-ai-pioneers-microsoft-survey-reveals-but-governance-lags-behind.430304)) | [CHƯA XÁC MINH] số liệu lấy từ bản tóm tắt thứ cấp; trang Microsoft bị chặn. Số 89% khớp với thông điệp "kiểm tra kết quả" của khoá |
| Báo cáo Anthropic Economic Index nhận xét VN có tỷ trọng cao ở yêu cầu liên quan lập trình và giáo dục | [Anthropic Economic Index (arXiv 2511.15080)](https://arxiv.org/pdf/2511.15080) | [CHƯA XÁC MINH] mới đọc tóm tắt. Gợi ý: Claude ở VN nghiêng về dev/giáo dục; mảng văn phòng còn ít người dạy bài bản [KN diễn giải] |

Không có số liệu: tỷ lệ dân văn phòng VN dùng riêng Claude; số người dùng Claude tại VN; tỷ lệ công ty VN có chính sách dùng AI (chưa tìm được số có nguồn). Ghi "chưa có số liệu" nếu cần nhắc.

Lưu ý khi dùng số trên bài: chỉ trích 1–2 số đã kiểm gốc (ưu tiên PwC 38%/14%), ghi tên nguồn và năm trong bài. Số 38% là "dùng hằng ngày", đừng viết thành "38% dân văn phòng".

## 4. Đối thủ và khoảng trống
Nguồn là trang bán khoá trong kết quả tìm kiếm; giá có thể đã đổi, [CHƯA XÁC MINH]. Không mở được bài quảng cáo Facebook của họ (Facebook không tìm được qua công cụ), nên phần "họ nói gì" dưới đây dựa vào mô tả trang khoá.

| Khoá | Họ nói gì | Giá ghi trên trang | Nguồn |
|---|---|---|---|
| ChatGPT và AI Đỉnh Cao (Unica) | Kết hợp ChatGPT với công cụ AI khác để làm content, hình ảnh, video, "kiếm tiền" | 599.000đ (giảm từ 1.990.000đ) | [link](https://unica.vn/khoa-hoc-chatgpt-va-ai-dinh-cao) |
| Ứng dụng AI tối ưu quản trị văn phòng (Redpola) | 3 buổi, tự động hoá, từ nội dung đến phân tích dữ liệu | 1.500.000đ (giảm 50% từ 3.000.000đ) | [link](https://redpola.com/ai-in-office/) |
| AI Facebook Marketing (Guru) | AI + Facebook Ads, Canva | 299.000đ (giảm từ 5.000.000đ) | [link](https://khokhoahoc.academy/khoa-hoc-ai-facebook-marketing-cung-guru-edu-vn/) |

Quan sát chung ([KN] từ mô tả các trang trên):
- Làm tốt: giá rõ, ưu đãi mạnh, hứa hẹn cụ thể (làm content, kiếm tiền), nhiều công cụ trong một khoá.
- Dở/khoảng trống: nặng "công cụ và mẹo", ít nói an toàn dữ liệu và kiểm tra kết quả; hầu hết dạy ChatGPT, rất ít khoá tiếng Việt cho Claude văn phòng; hứa kết quả lớn nhưng ít nói quy trình.

Điểm khác biệt khoá mình có thể khai thác (đều có trong brief):
1. An toàn là một phần riêng (12 slide) thay vì ghi chú cuối bài.
2. Công thức 5 dòng giao việc và quy trình dự án 5 bước: dễ nhớ, dùng lại được.
3. Ẩn dụ "nhân viên mới rất nhanh": giải thích rào cản tâm lý bằng một câu.
4. Học bằng làm: slide tương tác, 13 slide bài tập, bài tập vừa gói miễn phí (không cần trả tiền công cụ trước).
5. Có bản PowerPoint sửa được cho trưởng nhóm đào tạo phòng; chạy không cần mạng.
Không công kích đối thủ; chỉ nói "khoá này tập trung vào..." (đúng điều cấm của brief).

## 5. Từ khoá, hashtag, giờ đăng

**Từ khoá nội dung** [KN, chưa có số lượt tìm kiếm]: "dùng AI trong công việc văn phòng", "viết prompt/viết yêu cầu cho AI", "tóm tắt họp bằng AI", "viết email bằng AI", "AI cho kế toán/nhân sự/hành chính", "dùng AI an toàn", "Claude là gì", "cách dùng Claude". Nên viết "viết yêu cầu" kèm "prompt" lần đầu, vì dân văn phòng quen "prompt" hơn.

**Hashtag gợi ý** [KN, chưa kiểm lượng dùng; dùng 3–5 tag/bài, không nhồi]: #LamChuClaude #AIvanPhong #DungAIantoan #KyNangVanPhong #HocClaude #ClaudeChoDanVanPhong. Tag thương hiệu: #LamChuClaude (tự đặt, cần kiểm chưa bị trùng).

**Giờ đăng** (múi giờ VN):
- Có nguồn tham khảo: nhiều bài blog marketing VN khuyên với đối tượng dân văn phòng đăng 11h–13h và khoảng 19h45–20h, rộng hơn 19h–22h; sáng 7h–8h. Nguồn: [Sapo](https://www.sapo.vn/blog/gio-vang-dang-facebook), [Seongon](https://seongon.com/blog/facebook/khung-gio-vang-dang-bai-facebook.html). Đây là blog agency, không phải dữ liệu Facebook chính thức, [CHƯA XÁC MINH] về độ tin cậy.
- Đề xuất ([KN]): T2–T6 đăng 12h00 hoặc 19h45; thứ Bảy 9h30–10h; Chủ Nhật 20h00 (chốt chiến dịch). Test A/B hai khung 12h và 19h45 trong ngày 1–3 rồi dồn theo kết quả Insights của page.
- Mẹo [KN]: bài kêu gọi hành động (CTA) cuối ngày vào khung 19h45–21h vì lúc đó người ta rảnh đọc và nhắn tin.

## 6. Góc tiếp cận đề xuất (xếp hạng)

**Hạng 1: "Claude là nhân viên mới rất nhanh: giao việc rõ, kiểm tra kỹ"** (khuyên chọn)
- Lý do: là ẩn dụ chủ đạo của khoá; giải quyết cả "không biết viết yêu cầu" và "sợ sai" bằng một hình ảnh quen thuộc; giọng đồng nghiệp, không giật gân.
- Bằng chứng hỗ trợ: 89% người dùng VN coi kết quả AI là điểm khởi đầu (Microsoft 2026, [CHƯA XÁC MINH]).
- Rủi ro: hơi quen với nội dung AI khác; cần ví dụ việc văn phòng thật (email, báo cáo) để nổi bật.

**Hạng 2: "Dùng AI mà không lo lộ dữ liệu: khi nào Cho phép, khi nào Từ chối"**
- Lý do: khác biệt rõ nhất so với đối thủ; nỗi lo dữ liệu cao (90%, [CHƯA XÁC MINH]). Hợp với trưởng nhóm (persona C).
- Rủi ro: nếu nói quá tay thành doạ; không đưa lời hứa pháp lý về bảo mật.

**Hạng 3: "Một công thức 5 dòng thay cho ngồi nghĩ cách hỏi"**
- Lý do: lợi ích cụ thể, dễ lưu và chia sẻ (carousel/ảnh mẫu), hợp mục tiêu phụ "lượt lưu".
- Rủi ro: dễ thành mẹo rời rạc nếu không dẫn về khoá.

## 7. Khung câu chuyện 7 ngày gợi ý
Cấu trúc: nhận ra vấn đề, giải thích bằng ẩn dụ, ba kỹ năng, bằng chứng bằng ví dụ, giải toả nỗi sợ, mời hành động. Không dùng lời chứng thực (chưa có).

| Ngày | Chủ đề | Mục tiêu |
|---|---|---|
| T2 05/10 | Mở màn: "Dùng AI mà vẫn mệt, vì sao?" (gõ ngắn nên trả lời chung chung) + giới thiệu Claude như nhân viên mới rất nhanh | Tiếp cận, tương tác (hỏi bình luận) |
| T3 06/10 | Hiểu: Claude là gì, mỗi nút làm gì (ảnh bản đồ nút) | Lượt lưu, chia sẻ |
| T4 07/10 | Làm: công thức 5 dòng giao việc, ví dụ viết email/tóm tắt họp trước-sau | Lượt lưu, nhắn tin |
| T5 08/10 | An toàn: khi nào bấm Cho phép/Từ chối; kiểm tra trước khi dùng | Tin cậy, chia sẻ cho sếp/đồng nghiệp |
| T6 09/10 | Quy trình làm dự án 5 bước, ví dụ báo cáo tháng | Chuyển đổi (CTA mềm) |
| T7 10/10 | Bên trong khoá: 8 phần, 100 slide, bài tập thực hành, học không cần mạng | Chuyển đổi (CTA rõ, `[LINK ĐĂNG KÝ]`) |
| CN 11/10 | Chốt: câu hỏi hay gặp (giá, hình thức, có cần trả tiền gói Claude không) + `[HẠN ƯU ĐÃI]` | Chuyển đổi cuối |

Cần sếp điền: `[GIÁ]`, `[LINK ĐĂNG KÝ]`, `[HẠN ƯU ĐÃI]`, hình thức học (tự học online hay lớp). Cần xác nhận trước khi đăng: khoá không phải sản phẩm chính thức của Anthropic (ghi rõ ở chân bài/ads); giao diện Claude có tiếng Việt đến đâu; kiểm lại các số [CHƯA XÁC MINH] nếu muốn in lên bài.

## Nguồn đã dùng
- https://www.pwc.com/vn/en/publications/vietnam-publications/hopes-fears-vietnam-2025.html
- https://www.brandsvietnam.com/congdong/topic/thoi-quen-su-dung-ai-tai-viet-nam-2025-78-nguoi-dung-internet-tung-tuong-tac-voi-ai
- https://kenh14.vn/hon-40-nguoi-dung-quay-lung-voi-chatgpt-va-gemini-vi-lo-ngai-ro-ri-du-lieu-215260319235233859.chn
- https://news.microsoft.com/source/asia/2026/06/24/bao-cao-chi-so-xu-huong-cong-viec-nam-2026-luc-luong-lao-dong-viet-nam-da-san-sang-cho-ky-nguyen-ai-doanh-nghiep-can-chuyen-minh-de-but-pha/?lang=vi
- https://windowsnews.ai/article/39-of-vietnams-knowledge-workers-are-ai-pioneers-microsoft-survey-reveals-but-governance-lags-behind.430304
- https://arxiv.org/pdf/2511.15080
- https://unica.vn/khoa-hoc-chatgpt-va-ai-dinh-cao
- https://redpola.com/ai-in-office/
- https://khokhoahoc.academy/khoa-hoc-ai-facebook-marketing-cung-guru-edu-vn/
- https://www.sapo.vn/blog/gio-vang-dang-facebook
- https://seongon.com/blog/facebook/khung-gio-vang-dang-bai-facebook.html

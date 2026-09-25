# Plugin Design (bản tuỳ chỉnh cho công ty)

Dựa trên plugin [Design](https://github.com/anthropics/knowledge-work-plugins/tree/main/design) của Anthropic (bản 1.2.0), chỉnh lại cho An Tâm Foods (Công ty TNHH SX-TM Ẩm Thực An Tâm, antamfoods.com), công ty bánh tortillas và Doner kebab tại TP.HCM: bán cho doanh nghiệp SMEs, cửa hàng, nhượng quyền; kênh chính là Facebook và Zalo.

## Khác gì bản gốc

| Bản gốc | Bản công ty |
|---|---|
| Thiết kế giao diện phần mềm (app, web) | Bài đăng Facebook, ảnh Zalo, thực đơn, poster, bao bì, tài liệu bán hàng, nhượng quyền |
| Tiếng Anh | Tiếng Việt, giọng văn và luật cứng của công ty |
| Bàn giao cho lập trình viên | Bàn giao cho nhà in, người dựng Canva, và lập trình viên nếu có website |
| Nghiên cứu người dùng phần mềm | Ý kiến khách SMEs, khách cửa hàng, đối tác nhượng quyền |
| Slack, Linear, Jira, Intercom... | Canva, Figma, Google Drive, Gmail; Zalo và Facebook qua ảnh chụp, file xuất |

Thông tin công ty nằm ở [BRAND.md](BRAND.md). **Điền các ô [Cần điền] trước khi dùng** để Claude không phải hỏi lại mỗi lần.

## Cài đặt

Claude Code:

```bash
claude plugin marketplace add hung0981678222-ux/claude-dao-tao
claude plugin install design@claude-dao-tao
```

Cowork hoặc claude.ai: quản trị viên tổ chức thêm kho `hung0981678222-ux/claude-dao-tao` làm marketplace, rồi bật plugin `design`.

## Lệnh

| Lệnh | Dùng khi |
|---|---|
| `/design-critique` | Nhờ nhận xét một thiết kế: bài đăng, thực đơn, poster, bao bì |
| `/ux-copy` | Viết hoặc sửa chữ ngắn: tin Zalo, caption, tên món, nhãn, nút bấm |
| `/design-system` | Kiểm tra, ghi lại, mở rộng bộ nhận diện và bộ mẫu Canva |
| `/design-handoff` | Soạn thông số gửi nhà in, người dựng Canva, lập trình viên |
| `/accessibility-review` | Kiểm tra dễ đọc: trên điện thoại, từ xa, khi in, và chuẩn WCAG cho website |
| `/research-synthesis` | Tổng hợp bình luận, tin nhắn, khảo sát, khiếu nại thành việc cần làm |

Kỹ năng `user-research` tự chạy khi cần lập kế hoạch khảo sát, phỏng vấn khách, thử vị.

## Ví dụ

```
/design-critique [dán ảnh bài đăng Facebook] bài giới thiệu bánh tortillas cho SMEs, bản gần cuối
/ux-copy tin Zalo xin lỗi khách vì giao trễ, hẹn giao lại chiều nay
/design-handoff nhãn túi bánh tortillas 500g, in decal
/research-synthesis [đính kèm file bình luận Facebook tháng 9]
```

## Nguyên tắc chung

Claude soạn và nhận xét, người trong công ty duyệt. Giá, thành phần, hạn dùng, cam kết với khách và đối tác luôn phải được kiểm tra lại trước khi gửi ra ngoài.

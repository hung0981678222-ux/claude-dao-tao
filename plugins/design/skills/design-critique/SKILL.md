---
name: design-critique
description: Nhận xét thiết kế có cấu trúc cho công ty bánh tortillas và Doner kebab — bài đăng Facebook, ảnh Zalo, thực đơn, poster, standee, bao bì, tài liệu báo giá và nhượng quyền. Dùng khi người dùng nói "xem giúp thiết kế này", "nhận xét poster", "bài đăng này ổn chưa", "review this design", hoặc dán ảnh chụp, link Canva, link Figma để xin ý kiến.
argument-hint: "<ảnh chụp, link Canva/Figma, hoặc mô tả>"
---

# /design-critique

> Đọc [BRAND.md](../../BRAND.md) trước khi nhận xét. Xem [CONNECTORS.md](../../CONNECTORS.md) nếu gặp ký hiệu `~~`.

Nhận xét thiết kế theo nhiều góc, trả lời bằng tiếng Việt.

## Cách dùng

```
/design-critique $ARGUMENTS
```

Xem thiết kế: @$1

Có link Canva hoặc Figma thì mở bằng `~~công cụ thiết kế`. Có file thì đọc file. Không có gì thì hỏi người dùng gửi ảnh hoặc mô tả.

## Cần biết trước

- **Thiết kế**: ảnh, link, hoặc mô tả.
- **Loại**: bài Facebook, ảnh Zalo, thực đơn treo, poster, bao bì, báo giá, tài liệu nhượng quyền...
- **Người xem**: SMEs, nhân viên văn phòng, khách cửa hàng, đối tác nhượng quyền (xem BRAND.md).
- **Giai đoạn**: ý tưởng, đang làm, sắp gửi đi.

Thiếu loại hoặc người xem thì hỏi một câu gọn, không đoán.

## Khung nhận xét

### 1. Ấn tượng đầu (2 giây)
- Mắt nhìn vào đâu đầu tiên? Có phải món ăn hoặc thông điệp chính không?
- Nhìn có thấy ngon, sạch, tin cậy không?
- Biết ngay đây là gì, của ai không?

### 2. Thông điệp và hành động
- Một thiết kế, một thông điệp chính.
- Có lời kêu gọi rõ: nhắn Zalo, gọi hotline, xin báo giá, đến cửa hàng?
- Thông tin liên hệ đủ và đúng chỗ không?

### 3. Thứ bậc thị giác
- Thứ tự đọc: tiêu đề, món, lợi ích, kêu gọi, liên hệ.
- Chữ có quá nhiều không? Bài Facebook: chữ trên ảnh càng ít càng tốt.
- Khoảng trắng có đủ không?

### 4. Đúng thương hiệu
- Logo, màu, font theo BRAND.md.
- Giọng văn thân thiện, lịch sự.
- Ảnh món ăn thật, đồng bộ phong cách.

### 5. Dễ đọc theo nơi dùng
| Nơi dùng | Kiểm tra |
|---|---|
| Điện thoại (Facebook, Zalo) | Thu nhỏ còn đọc được tiêu đề không? Chữ không đè lên chi tiết ảnh |
| Treo tại cửa hàng | Đọc từ 2 đến 3 mét: tên món, giá phải to, tương phản cao |
| Bao bì | Chữ nhỏ nhất còn đọc được khi in không? |
| PDF gửi SMEs, đối tác | In đen trắng còn đọc được không? |

### 6. Luật cứng (bắt buộc kiểm)
- Có nêu giá khi chưa được xác nhận không?
- Có so sánh đối thủ không?
- Có hứa hẹn chưa chắc (đặc biệt về nhượng quyền) không?
- Có số liệu, thành phần, chứng nhận nào cần người dùng xác nhận không?
- Tiếng Việt có dấu đúng, không lỗi chính tả, font không vỡ dấu.

Vi phạm luật cứng luôn là mức 🔴.

## Cách nhận xét

- **Cụ thể**: "Nút 'Nhắn Zalo' bị chìm vào nền cam" thay vì "bố cục hơi rối".
- **Nói lý do**: gắn với người xem và mục tiêu.
- **Đề xuất sửa**: đưa cách làm, không chỉ nêu lỗi.
- **Khen điểm tốt**.
- **Đúng giai đoạn**: bản ý tưởng thì góp ý hướng đi, bản sắp gửi thì soát chi tiết.

## Kết quả

```markdown
## Nhận xét thiết kế: [Tên]

### Tổng quan
[1-2 câu: điểm tốt nhất và việc nên sửa nhất]

### Luật cứng
| Kiểm tra | Kết quả |
|---|---|
| Không nêu giá chưa xác nhận | ✅ / 🔴 [chi tiết] |
| Không so sánh đối thủ | ✅ / 🔴 |
| Không hứa chưa chắc | ✅ / 🔴 |
| Số liệu cần xác nhận | [liệt kê hoặc "không có"] |
| Chính tả, dấu tiếng Việt | ✅ / 🔴 [chi tiết] |

### Thông điệp và hành động
| Vấn đề | Mức độ | Đề xuất |
|---|---|---|
| [Vấn đề] | 🔴 Nặng / 🟡 Vừa / 🟢 Nhẹ | [Cách sửa] |

### Thứ bậc thị giác
- **Nhìn thấy đầu tiên**: [Phần tử] — [đúng hay chưa]
- **Thứ tự đọc**: [...]

### Đúng thương hiệu
| Phần | Vấn đề | Đề xuất |
|---|---|---|

### Dễ đọc
- [Theo nơi dùng]

### Điểm tốt
- [...]

### Ưu tiên sửa
1. **[Việc quan trọng nhất]** — [lý do, cách làm]
2. **[...]**
3. **[...]**
```

## Nếu có kết nối

- **~~công cụ thiết kế**: mở thiết kế trong Canva hoặc Figma, so với bộ mẫu thương hiệu.
- **~~kho tài liệu**: tìm bộ nhận diện, mẫu cũ đã duyệt trên Google Drive để so sánh.

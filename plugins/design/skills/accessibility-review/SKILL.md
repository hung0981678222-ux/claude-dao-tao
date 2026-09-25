---
name: accessibility-review
description: Kiểm tra thiết kế có dễ đọc, dễ dùng với mọi người không — bài đăng xem trên điện thoại, thực đơn và bảng giá đọc từ xa, bao bì in chữ nhỏ, tài liệu PDF, và chuẩn WCAG 2.1 AA cho website. Dùng khi người dùng nói "có dễ đọc không", "chữ có nhỏ quá không", "kiểm tra độ tương phản", "audit accessibility", "check a11y".
argument-hint: "<ảnh, link, hoặc mô tả>"
---

# /accessibility-review

> Đọc [BRAND.md](../../BRAND.md) để biết màu thương hiệu. Xem [CONNECTORS.md](../../CONNECTORS.md) nếu gặp ký hiệu `~~`.

Kiểm tra để khách lớn tuổi, khách nhìn kém, khách đứng xa, khách xem bằng điện thoại cũ đều đọc được.

## Cách dùng

```
/accessibility-review $ARGUMENTS
```

Kiểm tra: @$1

Hỏi trước thiết kế dùng ở đâu, vì mỗi nơi có tiêu chí riêng.

## Tiêu chí chung (mọi ấn phẩm)

| Tiêu chí | Mức đạt |
|---|---|
| Tương phản chữ thường | ≥ 4.5:1 |
| Tương phản chữ lớn (≥ 24px, hoặc ≥ 18.5px đậm) | ≥ 3:1 |
| Không dùng màu làm cách duy nhất để phân biệt | Ví dụ món cay: thêm biểu tượng hoặc chữ "cay", không chỉ tô đỏ |
| Chữ trên ảnh | Có lớp nền hoặc vùng ảnh trơn phía sau chữ |
| Dấu tiếng Việt | Font không vỡ dấu, dấu không bị cắt, dòng đủ giãn |
| Chữ in hoa | Hạn chế đoạn dài viết hoa toàn bộ, khó đọc |

Tính tỉ lệ tương phản từ mã màu khi có. Chỉ có ảnh thì ước lượng và ghi rõ là ước lượng.

## Theo nơi dùng

### Điện thoại (Facebook, Zalo)
- Xem ở kích thước thật của khung tin: tiêu đề còn đọc được không?
- Chữ trên ảnh không nhỏ hơn khoảng 1/20 chiều rộng ảnh.
- Số điện thoại, Zalo ghi dạng chữ trong bài, không chỉ nằm trong ảnh (để khách bấm, chép được).

### Treo tại cửa hàng (thực đơn, bảng giá, standee)
- Đọc từ 2 đến 3 mét: tên món và giá cao ít nhất khoảng 2,5 đến 4 cm.
- Nền và chữ tương phản cao, tránh nền ảnh rối sau chữ.
- Nhóm món rõ ràng, giá thẳng hàng.
- Ánh sáng cửa hàng: tránh giấy bóng gây loá nếu treo dưới đèn.

### Bao bì, nhãn
- Chữ nhỏ nhất (thành phần, hạn dùng) vẫn đọc được bằng mắt thường.
- Hạn sử dụng, ngày sản xuất đặt ở chỗ dễ thấy, tương phản tốt.
- Chất gây dị ứng (ví dụ gluten trong bột mì) nên in đậm hoặc tách dòng, theo nội dung người dùng xác nhận.

### PDF, PowerPoint gửi SMEs và đối tác
- In đen trắng vẫn phân biệt được biểu đồ, bảng.
- Tiêu đề thật (heading) để đọc bằng trình đọc màn hình; ảnh quan trọng có chữ mô tả.

### Website (nếu có) — WCAG 2.1 AA
- **1.1.1** Ảnh có chữ thay thế (alt), ảnh món ăn mô tả món.
- **1.4.3** Tương phản như bảng trên. **1.4.11** Viền nút, biểu tượng ≥ 3:1.
- **1.4.4** Phóng to 200% không vỡ trang.
- **2.1.1** Dùng được bằng bàn phím. **2.4.7** Thấy rõ ô đang chọn.
- **2.5.5** Nút bấm trên điện thoại đủ to (khuyến nghị ≥ 44×44px).
- **3.3.1** Form đặt hàng báo lỗi bằng chữ, nói rõ cách sửa.
- **4.1.2** Nút, ô nhập có tên đọc được bằng trình đọc màn hình.

## Kết quả

```markdown
## Kiểm tra dễ đọc: [Tên thiết kế]
**Nơi dùng:** [điện thoại / cửa hàng / bao bì / PDF / website]

### Tóm tắt
**Vấn đề:** [X] | 🔴 Nặng: [X] | 🟡 Vừa: [X] | 🟢 Nhẹ: [X]

### Vấn đề
| # | Vấn đề | Tiêu chí | Mức độ | Cách sửa |
|---|---|---|---|---|

### Tương phản màu
| Chữ | Nền | Tỉ lệ | Cần | Đạt? |
|---|---|---|---|---|

### Ưu tiên sửa
1. [...]
2. [...]
3. [...]
```

## Nếu có kết nối

- **~~công cụ thiết kế**: đọc mã màu, cỡ chữ chính xác từ Canva hoặc Figma thay vì ước lượng.

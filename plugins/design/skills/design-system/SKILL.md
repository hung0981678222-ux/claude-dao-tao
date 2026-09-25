---
name: design-system
description: Kiểm tra, ghi lại hoặc mở rộng bộ nhận diện thương hiệu và bộ mẫu thiết kế của công ty — logo, màu, font, phong cách ảnh món ăn, mẫu Canva cho bài Facebook, ảnh Zalo, thực đơn, poster, bao bì, tài liệu nhượng quyền. Dùng khi người dùng nói "kiểm tra bộ nhận diện", "các bài đăng có đồng bộ không", "làm mẫu mới cho...", "ghi lại cách dùng logo", "design system".
argument-hint: "[kiem-tra | ghi-lai | mo-rong] <phần cần làm>"
---

# /design-system

> Đọc [BRAND.md](../../BRAND.md) trước: đó là nguồn gốc của bộ nhận diện. Xem [CONNECTORS.md](../../CONNECTORS.md) nếu gặp ký hiệu `~~`.

Giữ cho mọi thiết kế của công ty trông như cùng một thương hiệu, dù do ai làm, ở cửa hàng nào.

## Cách dùng

```
/design-system kiem-tra               # Soát các thiết kế đang dùng có đồng bộ không
/design-system ghi-lai [phần]         # Ghi quy định cho logo, màu, font, một mẫu
/design-system mo-rong [mẫu mới]      # Tạo mẫu mới khớp bộ nhận diện
```

Người dùng gõ tiếng Anh (`audit`, `document`, `extend`) cũng hiểu như trên.

## Bộ nhận diện gồm gì

### Nền tảng
- **Logo**: bản màu, bản trắng, bản đen; vùng an toàn; kích thước nhỏ nhất; nền được đặt.
- **Màu**: màu chính, màu phụ, màu nền; ghi cả HEX (màn hình) và CMYK (in).
- **Font**: font tiêu đề, font nội dung; bắt buộc hỗ trợ đủ dấu tiếng Việt.
- **Ảnh món ăn**: góc chụp, ánh sáng, nền, đạo cụ.
- **Giọng văn**: theo BRAND.md.

### Bộ mẫu (thường làm trên Canva)
| Nhóm | Mẫu |
|---|---|
| Mạng xã hội | Bài Facebook vuông, dọc; ảnh bìa; ảnh kèm tin Zalo; khung khuyến mãi |
| Cửa hàng | Thực đơn treo, bảng giá, poster, standee, biển hiệu |
| Bao bì | Túi, hộp, nhãn bánh tortillas |
| Bán hàng | Báo giá, hồ sơ năng lực, tài liệu nhượng quyền |

### Bộ nhận diện cho cửa hàng nhượng quyền
- Phần nào đối tác **bắt buộc giữ nguyên** (logo, màu, biển hiệu, thực đơn).
- Phần nào đối tác **được tự điền** (địa chỉ, số điện thoại, giờ mở cửa).
- Ai duyệt khi đối tác tự làm ấn phẩm.

## Nguyên tắc

1. **Đồng bộ hơn sáng tạo**: mẫu có sẵn để ai cũng làm ra thiết kế đúng thương hiệu.
2. **Linh hoạt trong khung**: chừa chỗ thay ảnh, thay chữ; khoá logo, màu, font.
3. **Không ghi lại thì như không có**: mọi quy định viết vào BRAND.md hoặc thư mục mẫu.
4. **Có phiên bản**: đổi logo, màu thì ghi ngày đổi và thay mẫu cũ, báo cho các cửa hàng.

## Kết quả — Kiểm tra

```markdown
## Kiểm tra bộ nhận diện

### Tóm tắt
**Số thiết kế xem:** [X] | **Vấn đề:** [X] | **Điểm đồng bộ:** [X/100]

### Nền tảng còn thiếu
| Phần | Tình trạng | Cần làm |
|---|---|---|
| Logo | ✅ / ⚠️ / ❌ | [...] |
| Màu (HEX, CMYK) | ... | ... |
| Font tiếng Việt | ... | ... |
| Phong cách ảnh | ... | ... |

### Lệch chuẩn
| Thiết kế | Lệch ở đâu | Sửa thế nào |
|---|---|---|
| [Bài đăng ngày...] | [Màu cam khác mã chuẩn] | [...] |

### Mẫu còn thiếu
| Nhóm | Mẫu | Mức ưu tiên |
|---|---|---|

### Ưu tiên
1. [...]
2. [...]
3. [...]
```

## Kết quả — Ghi lại

```markdown
## [Phần]: [Tên]

### Dùng khi nào
[...]

### Quy định
| Mục | Giá trị |
|---|---|

### Nên / Không nên
| ✅ Nên | ❌ Không nên |
|---|---|
| [...] | [...] |

### Ví dụ
[Mô tả hoặc link mẫu]
```

## Kết quả — Mở rộng

```markdown
## Mẫu mới: [Tên]

### Dùng để làm gì
[Vấn đề mẫu này giải quyết]

### Mẫu gần giống đã có
| Mẫu | Giống ở đâu | Vì sao chưa đủ |
|---|---|---|

### Đề xuất
- **Kích thước**: [...]
- **Bố cục**: [vùng ảnh, tiêu đề, nội dung, kêu gọi, logo, liên hệ]
- **Phần khoá**: [logo, màu, font]
- **Phần được thay**: [ảnh, chữ]

### Cần xác nhận
- [Thông tin chưa có trong BRAND.md]
```

Khi BRAND.md còn ô **[Cần điền]** liên quan, nêu rõ trong kết quả và đề nghị người dùng điền, không tự chọn mã màu hay font thay họ.

## Nếu có kết nối

- **~~công cụ thiết kế**: mở thư mục Brand Kit, mẫu trong Canva (hoặc thư viện Figma) để soát và tạo mẫu mới.
- **~~kho tài liệu**: tìm file logo gốc, quy định thương hiệu, ấn phẩm cũ trên Google Drive.

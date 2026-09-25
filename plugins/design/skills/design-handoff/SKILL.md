---
name: design-handoff
description: Soạn thông số bàn giao thiết kế cho người làm tiếp — nhà in (bao bì, nhãn, thực đơn, poster, standee, biển hiệu), người dựng mẫu Canva, cửa hàng nhượng quyền, hoặc lập trình viên website. Dùng khi người dùng nói "gửi nhà in", "soạn thông số in", "bàn giao thiết kế", "gửi file cho đối tác nhượng quyền", "handoff", "dev spec".
argument-hint: "<ảnh, link Canva/Figma, hoặc mô tả ấn phẩm>"
---

# /design-handoff

> Đọc [BRAND.md](../../BRAND.md) để lấy mã màu, font, logo. Xem [CONNECTORS.md](../../CONNECTORS.md) nếu gặp ký hiệu `~~`.

Soạn bảng thông số để người nhận làm đúng ngay lần đầu, không phải hỏi lại.

## Cách dùng

```
/design-handoff $ARGUMENTS
```

Hỏi trước: **ai nhận** (nhà in, người dựng Canva, cửa hàng nhượng quyền, lập trình viên) và **ấn phẩm gì**. Mỗi người nhận dùng một mẫu bên dưới.

## Bàn giao cho nhà in

### Phải có
| Mục | Ghi chú |
|---|---|
| Kích thước thành phẩm | mm, ví dụ A4 210×297, standee 60×160 cm |
| Tràn lề (bleed) | Thường 3 mm mỗi cạnh; hỏi nhà in |
| Vùng an toàn | Chữ, logo cách mép cắt ít nhất 3 đến 5 mm |
| Hệ màu | CMYK cho in; ghi mã màu thương hiệu CMYK (hoặc Pantone nếu có) |
| Độ phân giải ảnh | 300 dpi ở kích thước thật |
| Font | Chuyển chữ thành nét (outline) hoặc gửi kèm font, tránh vỡ dấu tiếng Việt |
| Định dạng file | PDF in ấn (PDF/X nếu nhà in yêu cầu), kèm file gốc |
| Chất liệu, gia công | Giấy, decal, cán màng, bế, số lượng |
| Bản in thử | Có duyệt bản in thử trước khi in hàng loạt không |

### Riêng bao bì, nhãn thực phẩm
- Nội dung nhãn bắt buộc (tên sản phẩm, tên và địa chỉ đơn vị chịu trách nhiệm, định lượng, ngày sản xuất, hạn sử dụng, thành phần, hướng dẫn bảo quản, xuất xứ, cảnh báo nếu có) phải có đủ theo quy định ghi nhãn hàng hoá hiện hành.
- **Claude không tự soạn số liệu nhãn**. Ghi rõ trong bàn giao: "Nội dung nhãn đã được [người/phòng] xác nhận ngày [...]". Chưa có thì đánh dấu 🔴 và nhắc người dùng kiểm với bộ phận pháp lý.
- Vùng để trống cho in phun ngày sản xuất, hạn dùng, số lô.
- Mã vạch (nếu có): kích thước, vùng trắng quanh mã.

## Bàn giao cho người dựng Canva, cửa hàng nhượng quyền

- Link mẫu, phần nào **khoá** (logo, màu, font, bố cục), phần nào **được thay** (ảnh, chữ, địa chỉ, số điện thoại).
- Kích thước xuất file theo kênh (Facebook 1080×1080, 1080×1350; ảnh Zalo; PDF in).
- Quy trình duyệt: gửi ai, trong bao lâu, trước khi đăng hoặc in.

## Bàn giao cho lập trình viên (website, nếu có)

- Màu, font, khoảng cách theo BRAND.md; ghi tên biến nếu đã có.
- Kích thước các khối ở máy tính và điện thoại.
- Trạng thái nút: bình thường, di chuột, bấm, không bấm được, đang tải.
- Trường hợp đặc biệt: tên món dài, hết hàng, không tải được ảnh, form báo lỗi.
- Chữ thay thế (alt) cho ảnh món ăn.

## Kết quả

```markdown
## Bàn giao: [Tên ấn phẩm] → [Người nhận]

### Tổng quan
[Ấn phẩm gì, dùng ở đâu, số lượng, hạn chót]

### Thông số
| Mục | Giá trị |
|---|---|

### Màu và font
| Tên | HEX | CMYK | Dùng cho |
|---|---|---|---|

### Nội dung cần xác nhận trước khi làm
| Nội dung | Người xác nhận | Tình trạng |
|---|---|---|
| [Giá / nhãn / số liệu] | [...] | ✅ / 🔴 chưa |

### File gửi kèm
- [...]

### Liên hệ khi có thắc mắc
[Tên, số điện thoại — người dùng điền]
```

Ô nào chưa có thông tin thì ghi **[Cần điền]**, không đoán.

## Nếu có kết nối

- **~~công cụ thiết kế**: đọc kích thước, màu, font trực tiếp từ Canva hoặc Figma.
- **~~kho tài liệu**: lấy file logo gốc, nội dung nhãn đã duyệt trên Google Drive.
- **~~email**: soạn sẵn email gửi nhà in (chỉ soạn nháp, người dùng tự bấm gửi).

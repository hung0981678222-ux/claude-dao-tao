---
name: ux-copy
description: Viết hoặc sửa chữ ngắn cho công ty bánh tortillas và Doner kebab — tin nhắn Zalo, caption và tiêu đề Facebook, chữ trên ảnh, tên món và mô tả món trên thực đơn, chữ trên nhãn bao bì, khẩu hiệu, nút bấm và thông báo trên website. Dùng khi người dùng nói "viết giúp tin Zalo", "đặt tiêu đề", "sửa câu này", "nút này ghi gì", "write copy for".
argument-hint: "<bối cảnh hoặc câu cần sửa>"
---

# /ux-copy

> Đọc [BRAND.md](../../BRAND.md) trước khi viết: giọng văn và luật cứng ở đó. Xem [CONNECTORS.md](../../CONNECTORS.md) nếu gặp ký hiệu `~~`.

Viết hoặc sửa chữ ngắn, bằng tiếng Việt có dấu.

## Cách dùng

```
/ux-copy $ARGUMENTS
```

## Công thức 5 dòng

Trước khi viết, cần đủ 5 ý (thiếu thì hỏi gọn, không đoán):

| Ý | Ví dụ |
|---|---|
| Mục tiêu | Khách đồng ý xin báo giá chính thức |
| Ai đọc | Chủ doanh nghiệp SMEs |
| Kết quả | Tin Zalo 5 dòng |
| Hạn chót | Gửi trong hôm nay |
| Ràng buộc | Không nêu giá |

## Nguyên tắc

1. **Rõ**: nói đúng điều muốn nói, không dùng từ chuyên môn.
2. **Gọn**: ít chữ nhất mà vẫn đủ ý.
3. **Thống nhất**: một thứ, một tên gọi. Ví dụ luôn viết "bánh tortillas", không lúc "bánh tráng Mexico" lúc "tortilla".
4. **Có ích**: mỗi câu giúp người đọc làm bước tiếp theo.
5. **Như người thật nói**: lịch sự, ấm áp, không máy móc.

## Mẫu theo loại

### Tin Zalo
- Tối đa 5 dòng. Dòng 1 chào và nói lý do nhắn. Dòng cuối là một việc cụ thể cho khách làm.
- Ví dụ mở đầu: "Chào anh chị, em là [tên] từ An Tâm Foods."

### Bài Facebook
- Khoảng 120 chữ, kèm 3 gợi ý tiêu đề.
- Câu đầu phải giữ người đọc lại (lợi ích hoặc câu hỏi), không mở bằng giới thiệu công ty.
- Kết bằng kêu gọi: "Nhắn Zalo [số] để nhận báo giá cho công ty anh chị."

### Chữ trên ảnh, poster, standee
- Tiêu đề 3 đến 7 chữ. Tổng chữ trên ảnh Facebook càng ít càng tốt.

### Tên món, mô tả món trên thực đơn
- Tên món ngắn, dễ gọi. Mô tả 1 dòng: nhân chính, cách làm, vị.
- Không ghi thành phần, khối lượng, calo nếu người dùng chưa cung cấp.

### Nhãn bao bì
- Chỉ viết phần quảng bá (tên sản phẩm, câu mô tả, gợi ý dùng). Nội dung nhãn bắt buộc (thành phần, định lượng, ngày sản xuất, hạn dùng...) lấy nguyên từ người dùng, không tự soạn số liệu.

### Xin lỗi, xử lý khiếu nại
- Thứ tự: xin lỗi, nói rõ chuyện gì, cách xử lý và thời gian, kênh liên hệ.
- Ví dụ: "Em xin lỗi anh chị vì đơn hôm nay giao trễ. Bên em sẽ giao lại trước 15:00 chiều nay. Có gì anh chị nhắn Zalo này giúp em."

### Nút bấm, thông báo trên website (nếu có)
- Nút bắt đầu bằng động từ: "Xin báo giá", "Đặt hàng", "Gọi ngay".
- Báo lỗi: chuyện gì xảy ra + cách sửa. "Số điện thoại chưa đúng. Anh chị kiểm tra lại giúp em 10 số."

## Giọng theo tình huống

| Tình huống | Giọng |
|---|---|
| Giới thiệu, chào hàng | Thân thiện, tự tin, không khoe quá |
| Xin lỗi, khiếu nại | Nhận lỗi, cụ thể, có hẹn xử lý |
| Nhượng quyền | Chuyên nghiệp, rõ ràng, không hứa lợi nhuận |
| Khuyến mãi | Vui, ngắn, có hạn chót rõ |

## Kết quả

```markdown
## Chữ cho: [Bối cảnh]

### Đề xuất
[Nội dung]

### Phương án khác
| Phương án | Nội dung | Giọng | Hợp khi |
|---|---|---|---|
| A | [...] | [...] | [...] |
| B | [...] | [...] | [...] |

### Vì sao
[Ngắn gọn: người đọc, mục tiêu, lý do chọn chữ]

### Cần kiểm tra trước khi gửi
- [Số liệu, giá, ngày, cam kết cần người dùng xác nhận — hoặc "không có"]
```

## Nếu có kết nối

- **~~kho tài liệu**: tìm bài cũ đã duyệt, tài liệu giọng văn trên Google Drive để viết cho thống nhất.
- **~~công cụ thiết kế**: xem khung chữ trong Canva để viết vừa chỗ.

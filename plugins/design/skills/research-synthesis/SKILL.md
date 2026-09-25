---
name: research-synthesis
description: Tổng hợp ý kiến khách hàng thành chủ đề, nhận định và việc cần làm cho công ty bánh tortillas và Doner kebab — bình luận Facebook, tin nhắn Zalo, khiếu nại, khảo sát SMEs, ghi chú thử vị, câu hỏi của đối tác nhượng quyền. Dùng khi người dùng có nhiều ý kiến cần rút ra điểm chung, nói "tổng hợp phản hồi", "khách đang phàn nàn gì", "phân loại tin nhắn", "synthesize research".
argument-hint: "<file, ảnh chụp, hoặc nội dung dán vào>"
---

# /research-synthesis

> Đọc [BRAND.md](../../BRAND.md) để biết các nhóm khách. Xem [CONNECTORS.md](../../CONNECTORS.md) nếu gặp ký hiệu `~~`. Cách lập kế hoạch khảo sát nằm ở kỹ năng **user-research**.

Biến một đống ý kiến rời rạc thành vài việc rõ ràng để làm.

## Cách dùng

```
/research-synthesis $ARGUMENTS
```

## Nhận được gì

- Ảnh chụp hoặc file xuất bình luận Facebook, tin nhắn Zalo
- Ghi chú phỏng vấn, gọi điện với khách SMEs
- Kết quả khảo sát (Google Forms, Excel, CSV)
- Phiếu thử vị, góp ý tại cửa hàng
- Danh sách khiếu nại, đơn giao trễ
- Câu hỏi của người quan tâm nhượng quyền

## Bảo vệ thông tin khách

- Không chép tên, số điện thoại, ảnh khách vào kết quả. Gọi là "Khách SMEs 1", "Khách cửa hàng 3".
- Dữ liệu có thông tin nhạy cảm thì nhắc người dùng che trước khi chia sẻ tiếp.

## Cách phân loại

Gắn mỗi ý kiến vào một nhóm (thêm nhóm mới nếu cần):

| Nhóm | Ví dụ |
|---|---|
| Sản phẩm | Vị, độ dai của bánh, nhân kebab, khẩu phần |
| Giao hàng | Trễ, sai đơn, bao bì hỏng |
| Giá, báo giá | Hỏi giá, thấy đắt, muốn chiết khấu số lượng |
| Chăm sóc khách | Trả lời chậm, thái độ |
| Thiết kế, bao bì, thực đơn | Khó đọc, không rõ giá, không biết món gì |
| Nhượng quyền | Chi phí, hỗ trợ, mặt bằng, thời gian |
| Khen | Điều khách thích — giữ và nhấn mạnh |

## Nguyên tắc

- Đếm số lần xuất hiện, không suy từ một ý kiến.
- Tách **khách nói gì** (dẫn nguyên văn) và **mình hiểu là gì** (nhận định).
- Ghi rõ độ tin cậy: nhiều nguồn khớp nhau thì cao, một hai ý kiến thì thấp.
- Không bịa số liệu, phần trăm. Không đủ dữ liệu thì nói thiếu.

## Kết quả

```markdown
## Tổng hợp ý kiến: [Nguồn, thời gian]

### Tóm tắt
[3-4 câu: điều quan trọng nhất và nên làm gì]

### Dữ liệu
- **Nguồn:** [Facebook / Zalo / khảo sát...] | **Số ý kiến:** [X] | **Thời gian:** [...]

### Chủ đề chính
| # | Chủ đề | Nhóm khách | Số lần | Độ tin cậy |
|---|---|---|---|---|

#### Chủ đề 1: [Tên]
- **Khách nói:** "[trích nguyên văn]", "[...]"
- **Nhận định:** [...]
- **Ảnh hưởng:** [bán hàng / uy tín / chi phí]

### Theo nhóm khách
| Nhóm | Quan tâm nhất | Bực nhất |
|---|---|---|
| SMEs | ... | ... |
| Khách cửa hàng | ... | ... |
| Đối tác nhượng quyền | ... | ... |

### Việc nên làm
| Ưu tiên | Việc | Bộ phận | Dựa trên |
|---|---|---|---|
| 1 | [...] | [Sale / Marketing / Bếp / Giao hàng] | Chủ đề [X] |

### Còn chưa rõ
- [Câu hỏi cần khảo sát thêm]
```

## Nếu có kết nối

- **~~kho tài liệu**: đọc file khảo sát, bảng khiếu nại trên Google Drive.
- **~~email**: đọc email phản hồi từ khách SMEs, đối tác (chỉ đọc, không gửi).

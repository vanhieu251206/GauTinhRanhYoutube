# S0 — Tổng quan Quy trình Chiến lược

> Quy trình này **tách biệt** với `QuyTrinh/` (quy trình sản xuất 1 video). `QuyTrinh/` trả lời "làm video này thế nào", còn `QuyTrinh-Chien-Luoc/` trả lời "kênh đang đi đúng hướng không, có nên đổi gì không".
> Nguyên tắc nền tảng nằm ở `docs/chien-luoc-youtube.md` — đọc file đó trước khi chạy các bước dưới đây.

## Khi nào dùng quy trình này
- Sau khi 1 video đã đăng được 24-48h → chạy **S1**.
- Định kỳ (VD: mỗi 5-10 video, hoặc khi cảm thấy kênh chững) → chạy **S2** để tổng hợp và quyết định hướng đi.
- Trước khi bắt đầu 1 chủ đề/ngách hoàn toàn mới → chạy **S3**.

## Các bước
1. [S1-Theo-Doi-Hieu-Qua.md](S1-Theo-Doi-Hieu-Qua.md) — ghi nhận CTR/Retention/Impression của từng video sau 24-48h, đối chiếu ngưỡng tham khảo.
2. [S2-Duc-Ket-Dinh-Ky.md](S2-Duc-Ket-Dinh-Ky.md) — tổng hợp nhiều video, tìm pattern (thumbnail nào ăn, hook nào ăn, độ dài nào tốt), quyết định giữ/đổi công thức.
3. [S3-Danh-Gia-Ngach.md](S3-Danh-Gia-Ngach.md) — đánh giá lại ngách/định vị kênh khi có dấu hiệu bão hòa hoặc muốn mở rộng.

## Dữ liệu lưu ở đâu
Tất cả số liệu và đúc kết ghi vào `docs/nhat-ky-hieu-qua.md` (tạo mới khi chạy S1 lần đầu) — **không** lưu ở bộ nhớ Claude, để backup được qua git (xem quy tắc ở `CLAUDE.md` mục 2).

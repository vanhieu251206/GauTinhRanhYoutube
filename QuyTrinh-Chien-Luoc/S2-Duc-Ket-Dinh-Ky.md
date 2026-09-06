# S2 — Đúc kết định kỳ (mỗi 5-10 video)

## Khi nào chạy
Sau khi đã có dữ liệu S1 của ít nhất 5 video, hoặc khi người dùng cảm thấy kênh chững/muốn xem lại công thức.

## Các bước
1. Đọc toàn bộ `docs/nhat-ky-hieu-qua.md`.
2. So sánh các video theo từng biến: kiểu thumbnail, kiểu hook/tiêu đề, độ dài, nhịp kể — tìm xem biến nào tương quan với CTR/Retention cao.
2.1. **Đánh giá theo Pillar đề tài** (đối chiếu cột "Pillar" ở `docs/da-dung-de-tai.md`): gộp nhóm video theo 8 pillar ở `docs/Chu-De-goc.md` mục 1, so sánh CTR/Retention trung bình từng pillar. Cần ít nhất 2-3 video/pillar mới đủ để so sánh (số ít hơn thì chỉ ghi nhận, chưa kết luận). Pillar nào liên tục thấp hơn hẳn các pillar còn lại sau đủ dữ liệu → cân nhắc bỏ, ghi lại lý do + ngày vào `docs/da-dung-de-tai.md`.
2.5. **Tự kiểm tra rủi ro "Generic or Repetitive Content"**: xem lại N video gần nhất liên tiếp (đọc script hoặc xem thật), tự hỏi "nếu là người xem lạ xem liên tiếp mấy video này, có đoán được nhịp kể/kết cấu tiếp theo không?". Nếu có dấu hiệu đoán được rõ (lúc nào cũng chỉ nói COGS mà không đổi biến khác), điều chỉnh cho tập tiếp theo — đổi biến bóc tách (chi phí ẩn, mô hình môi giới, chiết khấu app...).
3. Nêu rõ đây là quan sát từ mẫu nhỏ, không phải kết luận chắc chắn — cần tiếp tục test để xác nhận.
4. Đề xuất 1-2 thay đổi cụ thể cho video tiếp theo (đổi 1-2 biến, không đổi tất cả cùng lúc — xem nguyên tắc test có hệ thống ở `docs/chien-luoc-youtube.md` mục 7).
5. Ghi đúc kết vào cuối `docs/nhat-ky-hieu-qua.md`, phần "## Đúc kết [ngày]":

```markdown
## Đúc kết YYYY-MM-DD (sau N video)
- Pattern quan sát được: [...]
- Thay đổi áp dụng cho video tiếp theo: [...]
- Giả thuyết cần test tiếp: [...]
```

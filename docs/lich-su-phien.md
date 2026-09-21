# lich-su-phien.md — Nhật ký sửa tay

> Ghi: bản gốc → bản sửa → lý do, mỗi khi có chỉnh sửa tay đáng kể so với bản nháp Claude tạo.

## Tập 3 — Xe Công Nghệ (Grab)

**1. Lỗi số liệu GrabCar/GrabBike lẫn lộn (phát hiện 2 lần, đã sửa)**
- Bản gốc: xăng 250.000-400.000đ/ngày, chiết khấu 28,3-32% — lấy nhầm từ nguồn nói về GrabCar (ô tô).
- Bản sửa: xăng 50.000-150.000đ/ngày, chiết khấu 27,27% — đúng nguồn GrabBike (xe máy), khớp case chính của video (cuốc 10km bằng xe máy).
- Lý do: người dùng thấy số liệu "cao hơn nhiều so với mức thực" → soát lại phát hiện lấy nhầm loại hình dịch vụ trong cùng 1 bài báo nguồn.

**2. Ngoại lệ phong cách thumbnail — Gấu cartoon + tài xế người thật + nền ảnh chụp thật**
- Bản gốc: toàn bộ ảnh (kể cả thumbnail) giữ đúng 1 phong cách flat cartoon nhất quán theo quy tắc cứng ở `QuyTrinh/C3-Prompt-Anh.md`.
- Bản sửa: riêng thumbnail tập này phá lệ — Gấu vẫn cartoon, nhóm tài xế vẽ theo phong cách người thật (photorealistic), nền là ảnh chụp đường phố thật làm mờ.
- Lý do: người dùng chủ động yêu cầu, xác nhận chấp nhận không nhất quán phong cách vì muốn hiệu ứng thị giác mạnh hơn cho thumbnail.

## Tập 7 — Thợ Hàn Đổi Đời

**1. Nền ảnh Gấu — đổi từ nền phẳng đơn sắc sang bối cảnh xuyên suốt**
- Bản gốc: nhiều scene Gấu dùng mô tả nền mơ hồ ("flat illustrated background, plain") → AI tự vẽ hoạ tiết mandala/đèn lồng/tre trúc không liên quan.
- Bản sửa: dựng 1 bối cảnh cố định "phòng làm việc phân tích của Gấu" (bàn gỗ, kệ sách, đèn đồng, cửa sổ skyline) dùng xuyên suốt mọi scene Gấu, khoá cứng "không hoạ tiết trang trí lấp chỗ trống".
- Lý do: người dùng phát hiện ảnh nền "khó hiểu", yêu cầu bỏ hẳn nền màu phẳng đơn sắc, phải có bối cảnh xuyên suốt.

**2. Lỗi phiên âm TTS lem sang chữ hiển thị trên ảnh ("6G" → "SÁU GỜ")**
- Bản gốc: áp dụng nhầm quy tắc phiên âm dành cho `voice-script.md` (đọc TTS) sang cả chữ trên chứng chỉ hiển thị trong ảnh/thumbnail.
- Bản sửa: chữ hiển thị trên ảnh giữ nguyên ký hiệu gốc; do công cụ gen ảnh vẫn tái tạo sai dù đã sửa, bỏ hẳn số hiệu "6G" khỏi chữ trên chứng chỉ, chỉ còn "CHỨNG CHỈ HÀN".
- Lý do: người dùng phát hiện qua ảnh thumbnail đã gen, thumbnail cuối cùng vẫn giữ bản có lỗi này vì đã ưng ý tổng thể, chỉ sửa cho các ảnh scene xuất sau.

**3. Hiệu chỉnh tốc độ đọc TTS (giây/ký tự)**
- Bản gốc: công thức 0,0585 giây/ký tự (chỉ đo từ 1 mẫu Tập 1).
- Bản sửa: 0,0557 giây/ký tự, gộp thêm mẫu thật Tập 3 (10:23, người dùng xác nhận từ video đã đăng).
- Lý do: số liệu thật từ tập đã đăng chính xác hơn ước lượng ban đầu.
- **Ghi chú thử nghiệm**: người dùng rất ưng kết quả — coi đây là 1 thử nghiệm, nếu hiệu quả (CTR tốt khi theo dõi ở S1) sẽ cân nhắc dùng lại ở các tập sau. KHÔNG mặc định áp dụng cho tập tiếp theo nếu chưa có xác nhận lại — vẫn giữ quy tắc cứng 1 phong cách nhất quán làm mặc định cho tới khi có đủ dữ liệu hiệu quả để quyết định đổi.

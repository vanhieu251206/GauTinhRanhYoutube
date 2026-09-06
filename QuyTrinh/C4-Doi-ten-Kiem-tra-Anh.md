# C4 — Đổi tên ảnh

> Sau khi gen xong ảnh từ `prompt-anh.txt` (C3) và bỏ vào `Anh Video/`, đổi tên theo STT scene. Việc kiểm tra chất lượng ảnh do người dùng tự làm thủ công (xem bằng mắt trực tiếp) — Claude KHÔNG tự xem/duyệt từng ảnh ở bước này.

## Đầu vào
- `scene-list.md` (từ C3) — lấy STT scene.
- Thư mục `Anh Video/` — chứa ảnh gen từ `prompt-anh.txt`.

## Đầu ra
- Ảnh trong `Anh Video/` được đổi tên `001.jpg`, `002.jpg`... (3 chữ số, vì 1 tập có thể >99 ảnh) khớp đúng STT scene.

## Bước 1 — Đổi tên
- Ghép ảnh với scene theo đúng thứ tự sinh ra = thứ tự dòng trong `prompt-anh.txt` = STT scene.
- Nếu công cụ gen ảnh tự tạo 1 thư mục con bên trong `Anh Video/` chứa ảnh (thường gặp, tên dạng `Task_HHMMSS_MMDDYYYY`) thay vì để ảnh ngay ở gốc: đổi tên từng ảnh theo đúng thứ tự trước, rồi đưa ảnh đã đổi tên ra thẳng `Anh Video/` gốc, xoá thư mục con rỗng — `Anh Video/` cuối cùng chỉ chứa các file `001.jpg`...`0NN.jpg`, không còn thư mục con.
- **Nếu có NHIỀU thư mục `Task_...` cùng lúc** (do gen nhiều lượt/nhiều batch khác nhau, timestamp khác nhau trong tên): **kiểm tra số lượng ảnh trong TỪNG thư mục trước** (không mặc định lấy thư mục đầu tiên tìm thấy) — thư mục nào có đủ số ảnh khớp tổng trong `scene-list.md` (VD đủ cả 0NN ảnh) mới là bộ đúng/đầy đủ cuối cùng, các thư mục còn lại thường là batch chạy dở/thiếu từ lần trước, bỏ qua không dùng.

## Kiểm tra chất lượng
Người dùng tự xem toàn bộ ảnh bằng mắt và quyết định ảnh nào cần gen lại — không thuộc phạm vi Claude tự động ở bước này.

## Cách sửa khi người dùng phát hiện ảnh lỗi
Không tự sửa ảnh bằng tay — viết lại prompt của đúng scene đó (dựa trên prompt gốc trong `prompt-anh.txt`, giữ nguyên phần mô tả style cố định, chỉ thêm câu nhấn mạnh đúng chỗ gây lỗi, VD: thêm "with absolutely no white rectangle, box, patch, or shape artifact of any kind in that corner" nếu lỗi artifact góc ảnh). Gen lại riêng ảnh đó, không cần gen lại cả bộ.

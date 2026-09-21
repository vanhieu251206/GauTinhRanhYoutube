# C4 — Đổi tên ảnh

> Sau khi gen xong ảnh từ `prompt-anh.txt` (C3) và bỏ vào `Anh Video/`, đổi tên theo STT scene. Việc kiểm tra chất lượng ảnh do người dùng tự làm thủ công (xem bằng mắt trực tiếp) — Claude KHÔNG tự xem/duyệt từng ảnh ở bước này.

## Đầu vào
- `scene-list.md` — STT scene + cột "Loại ảnh" (AI gen / Crop nguồn thật / Icon động).
- `Anh Video/` — ảnh hoạt cảnh gen từ `prompt-anh.txt` và ảnh tự crop theo `crop-nguon.md` (nếu có).
- `Icon Goc/` — ảnh icon nền trắng gen từ `prompt-icon.txt` (nếu tập có scene `Icon động`).

## Đầu ra
Thư mục `Anh Video/` chứa **đúng 1 file cho mỗi STT scene, gộp mọi loại vào 1 bộ duy nhất** — đây là bộ ảnh cuối cho C5:
- Scene `AI gen` và `Crop nguồn thật`: `001.jpg`, `002.jpg`... (3 chữ số vì 1 tập có thể >99 ảnh).
- Scene `Icon động`: `007.png`... (PNG nền trong suốt sau khi tách nền; đuôi `.png` là dấu phân biệt loại ở C5).
Ảnh icon gốc nền trắng giữ nguyên trong `Icon Goc/` (đổi tên `NNN.jpg` theo STT), không xoá.

## Bước 1 — Đổi tên theo STT (làm riêng từng loại)
Mỗi file prompt chỉ chứa các dòng của đúng 1 loại theo thứ tự STT (C3 Bước 4, không dòng trống). Cách ánh xạ: từ `scene-list.md`, lọc danh sách STT của loại đó theo thứ tự tăng dần → **ảnh thứ N (theo thứ tự sinh ra = thứ tự dòng trong file prompt) ↔ STT thứ N trong danh sách đã lọc**.
- Hoạt cảnh: lọc STT `AI gen`, ánh xạ với `prompt-anh.txt`. Ảnh `Crop nguồn thật` người dùng đặt theo đúng STT trong `crop-nguon.md` — đổi tên thẳng `0NN.jpg`, không qua ánh xạ.
- Icon: lọc STT `Icon động`, ánh xạ với `prompt-icon.txt`, đổi tên `Icon Goc/NNN.jpg`.
- **Tuyệt đối không mặc định "số trong tên file gen = STT scene"** (lỗi thật ở Tập 8): tool gen thường đánh số theo thứ tự dòng CÓ prompt. Luôn ánh xạ qua danh sách STT đã lọc từ `scene-list.md`. Kiểm tra: số ảnh mỗi loại phải bằng số scene loại đó, lệch thì dừng báo người dùng.
- Nếu công cụ gen tự tạo thư mục con dạng `Task_HHMMSS_MMDDYYYY`: đổi tên ảnh theo thứ tự rồi đưa ra thẳng thư mục đích, xoá thư mục con rỗng. Nếu có NHIỀU thư mục `Task_...`: đếm ảnh từng thư mục, chỉ dùng bộ có đủ số ảnh khớp số dòng prompt của loại đó, bỏ các batch dở dang.

## Bước 2 — Tách nền icon rồi ghép vào `Anh Video/` (chỉ khi có scene `Icon động`)
1. Đưa `Icon Goc/*.jpg` vào `Cong-Cu/remove-bg/app.py` (`python app.py`, kéo thả cả thư mục hoặc dán; sửa tay chỗ còn sót; "Tải tất cả (ZIP)"). Chi tiết: `docs/icon-dong.md`.
2. Giải nén, đổi tên `NNN_nobg.png` → `NNN.png` (đúng STT), bỏ vào `Anh Video/` cùng các file `.jpg` của scene khác.
3. Kiểm tra cuối: liệt kê `Anh Video/` — số file = tổng số scene, mỗi STT đúng 1 file, không trùng STT giữa `.jpg` và `.png`.

## Kiểm tra chất lượng
Người dùng tự xem toàn bộ ảnh bằng mắt và quyết định ảnh nào cần gen lại — không thuộc phạm vi Claude tự động ở bước này.

## Cách sửa khi người dùng phát hiện ảnh lỗi
- **Ảnh loại `AI gen`**: Không tự sửa ảnh bằng tay — viết lại prompt của đúng scene đó (dựa trên prompt gốc trong `prompt-anh.txt`, giữ nguyên phần mô tả style cố định, chỉ thêm câu nhấn mạnh đúng chỗ gây lỗi, VD: thêm "with absolutely no white rectangle, box, patch, or shape artifact of any kind in that corner" nếu lỗi artifact góc ảnh). Gen lại riêng ảnh đó, không cần gen lại cả bộ.
- **Ảnh loại `Icon động`**: viết lại prompt như ảnh `AI gen`, nhấn mạnh nền trắng tinh/không bóng/vật thể không bị cắt mép, rồi gen lại + tách nền lại riêng ảnh đó.
- **Ảnh loại `Crop nguồn thật`**: không "gen lại" — đối chiếu lại dòng hướng dẫn crop tương ứng trong `crop-nguon.md`, kiểm tra crop đúng đoạn/đúng trích dẫn chưa, chụp lại nếu sai vùng hoặc thiếu logo/tên báo trong khung.

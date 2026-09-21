# Icon động (scene dùng icon minh hoạ tách nền, ghép lên nền kẻ ô, chỉ có hiệu ứng xuất hiện)

Áp dụng cho scene mà ảnh là **icon/vật thể đơn lẻ đã tách nền** (xem `Cong-Cu/remove-bg/`). Các scene khác vẫn theo C5: ảnh tĩnh, cắt cứng, không zoom/pan.

## Vị trí trong quy trình sản xuất
- **C2**: cột "Loại ảnh" = `Icon động` (dùng chọn lọc).
- **C3 Bước 3b/4**: viết prompt icon minh hoạ 2D phẳng kiểu infographic (khối style cố định + `Composition:` riêng) vào **`prompt-icon.txt`**, tách khỏi `prompt-anh.txt` (hoạt cảnh).
- **C4**: đổi tên ảnh icon → `Icon Goc/NNN.jpg`; tách nền bằng `Cong-Cu/remove-bg/app.py`; đặt `NNN.png` vào `Anh Video/` để gộp 1 bộ ảnh cuối (mỗi STT 1 file).
- **C5 Bước 2b**: tra cột "Loại ảnh": scene `Icon động` chạy `icon_anim.py ... --bg Fanpage-Asset/Nen-Luoi-O/nen-luoi-o.png` → clip `.mp4` đã ghép nền kẻ ô, đúng số khung, nhẹ (1-3 MB).

## Ghi chú kỹ thuật (đã thử)
- Nền trong suốt chỉ giữ được bằng **.mov ProRes 4444**. MP4 không có alpha. **.webm (VP9 alpha) CapCut xuất ra video lỗi/sai định dạng — không dùng.**
- Bản không nền (`.mov` ProRes 4444) nặng (icon nhiều chi tiết: ~20-25 MB cho 2-5 giây ở khung 1920x1080), vì mỗi khung lưu gần như nguyên ảnh. Muốn nhẹ hơn: giảm `--dur`, hoặc thu nhỏ khung (`--width/--height`) rồi đặt lại vị trí trong CapCut.
- Mặc định **không bóng**; bật bằng `--shadow` nếu scene cần cảm giác lơ lửng trên nền phẳng.
- Icon nguồn nhỏ (~700px) phóng lên cao 700px trên khung 1080 hơi mềm; dùng bản gen độ phân giải cao hơn nếu có.

## Chọn hiệu ứng xuất hiện (CỐT LÕI — chọn linh hoạt, không lặp 1 kiểu cả tập)
Người dùng chốt 21/09/2026: **icon không chuyển động liên tục**, chỉ có hiệu ứng xuất hiện rồi đứng yên. `--entrance pop | rise | drop | slide-left | slide-right | fade` (mặc định `pop`), `--enter-dur` (mặc định 0,6s). Đổi kiểu theo ý câu voice: con số gây sốc → `pop`/`drop`; sơ đồ giải thích → `rise`/`fade`; hai icon liền nhau → xen kẽ `slide-left`/`slide-right`. Đừng để mọi icon trong 1 tập xuất hiện y hệt (dễ nhàm, rủi ro "reused content" — xem `chien-luoc-youtube.md` mục 8).
Các preset chuyển động liên tục cũ (`--preset float|drift|pulse|swing`) vẫn còn trong công cụ nhưng KHÔNG dùng trong quy trình.

## Nền kẻ ô chuyển động (quyết định 21/09/2026)
Nền kẻ ô của scene `Icon động` cuộn XUỐNG liên tục để scene không bị tĩnh (icon vẫn chỉ xuất hiện rồi đứng yên). `--bg-scroll <px/giây>` (mặc định của `xuat_clip.py` là 60; 0 = đứng yên). Nền lặp theo chu kỳ 100px (đúng ô lưới `nen-luoi-o.png`) nên cuộn liền mạch; nếu đổi nền lưới khác ô thì đặt `--bg-period` bằng chu kỳ ô mới.

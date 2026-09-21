# Icon chuyển động (scene dùng icon tách nền)

Áp dụng cho scene mà ảnh là **icon/vật thể đơn lẻ đã tách nền** (xem `Cong-Cu/remove-bg/`). Các scene khác vẫn theo C5: ảnh tĩnh, cắt cứng, không zoom/pan.

## Vị trí trong quy trình sản xuất
- **C2**: cột "Loại ảnh" = `Icon động` (dùng chọn lọc).
- **C3 Bước 3b/4**: viết prompt icon (khối style cố định + `Object:` riêng) vào **`prompt-icon.txt`**, tách khỏi `prompt-anh.txt` (hoạt cảnh).
- **C4**: đổi tên ảnh icon → `Icon Goc/NNN.jpg`; tách nền bằng `Cong-Cu/remove-bg/app.py`; đặt `NNN.png` vào `Anh Video/` để gộp 1 bộ ảnh cuối (mỗi STT 1 file).
- **C5 Bước 2b**: tra cột "Loại ảnh": scene `Icon động` chạy `python Cong-Cu/icon-anim/icon_anim.py "Anh Video/0NN.png" -o clips --fps 25 --frames <N> --name scene-0NN.mov --preset ...` → clip `.mov` nền trong suốt đúng số khung; trong CapCut đặt trên track phía trên nền người dùng chọn.

## Ghi chú kỹ thuật (đã thử)
- Nền trong suốt chỉ giữ được bằng **.mov ProRes 4444**. MP4 không có alpha. **.webm (VP9 alpha) CapCut xuất ra video lỗi/sai định dạng — không dùng.**
- ProRes 4444 nặng (icon nhiều chi tiết: ~20-25 MB cho 2-5 giây ở khung 1920x1080), vì mỗi khung lưu gần như nguyên ảnh. Muốn nhẹ hơn: giảm `--dur`, hoặc thu nhỏ khung (`--width/--height`) rồi đặt lại vị trí trong CapCut.
- Mặc định **không bóng**; bật bằng `--shadow` nếu scene cần cảm giác lơ lửng trên nền phẳng.
- Icon nguồn nhỏ (~700px) phóng lên cao 700px trên khung 1080 hơi mềm; dùng bản gen độ phân giải cao hơn nếu có.

## Chọn kiểu chuyển động (CỐT LÕI — chọn linh hoạt, không lặp 1 kiểu cả tập)
`--preset float | drift | pulse | swing | random`. Đổi preset/`--period`/`--dur` theo nhịp và ý của từng câu voice; đừng để mọi icon trong 1 tập chuyển động y hệt (dễ nhàm, rủi ro "reused content" — xem `chien-luoc-youtube.md` mục 8).

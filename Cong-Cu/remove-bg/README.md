# remove_bg.py — tách nền trắng, xuất PNG trong suốt (offline)

Cần: Python 3, `pip install pillow numpy scipy`.

    python remove_bg.py anh.jpg --preview            # 1 ảnh -> anh_nobg.png + anh_nobg_preview.jpg
    python remove_bg.py "Icon 3D/Task_x" -o ra       # cả thư mục
    python remove_bg.py anh.jpg --shadow             # ảnh có bóng đổ xám dưới vật thể
    python remove_bg.py anh.jpg --trim 24            # cắt sát vật, chừa lề 24 px

Gợi ý chỉnh: còn sót nền xám nhạt -> `--tol 25`; có bóng đổ dính vào -> `--shadow`
(không bật mặc định vì có thể ăn nhầm mép vật thể trắng/bạc — hãy xem preview); mép quá cứng -> `--band 4`.
Xem đủ tham số trong đầu file `remove_bg.py`.

## Giao diện web (tẩy thủ công)

    python app.py        # mở http://127.0.0.1:8765

Kéo thả nhiều ảnh (hoặc Ctrl+V dán). Tự tách nền, rồi sửa tay:
- **Tẩy (E)** / **Khôi phục (R)**: cọ có chỉnh cỡ + độ mềm; Khôi phục lấy lại pixel từ ảnh gốc.
- **Đũa thần (W)**: bấm vào vùng màu giống nhau để xoá cả mảng (chỉnh ngưỡng).
- Ctrl+Z / Ctrl+Shift+Z, `[` `]` đổi cỡ cọ, cuộn chuột zoom, giữ Space kéo ảnh.
- Đổi nền xem thử (caro/xanh/kem/đen/đỏ), giữ nút "xem ảnh gốc" để so sánh.
- Tải từng ảnh hoặc tất cả, có cắt sát vật thể.

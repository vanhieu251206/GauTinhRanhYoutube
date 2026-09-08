# End-screen / bìa kêu gọi đăng ký — "Gấu Tinh Ranh"

Dùng ở giây cuối video (outro) để kêu gọi subscribe, có thể tái dùng làm ảnh bìa đăng chéo Facebook/TikTok.

Kích thước chuẩn: 1280×720px (16:9), chừa khoảng trống góc phải dưới (~200×150px) để đặt nút Subscribe/nút kênh nổi bật do YouTube tự chèn (end screen element) — không vẽ chữ/chi tiết quan trọng đè vào vùng này.

## Mô tả
Gấu đứng full-body theo đúng charStyle đã chốt (`docs/Visual-Prompts-goc.md` mục 1, dựa trên ảnh tham chiếu `Fanpage-Asset/gau_mascot.jpg`) — tư thế nghiêng người, một tay đút túi quần, cằm cúi nhìn xuống qua gọng kính, nhếch mép cười khẩy lộ răng vàng. Gấu đặt lệch bên trái khung hình, tay còn lại chỉ/vẫy về phía góc phải dưới (nơi nút Subscribe của YouTube sẽ hiện) như đang "mời gọi" người xem bấm vào đó. Nền phẳng xanh navy (#0C447C) với vài chi tiết biểu tượng tài chính tối giản màu vàng đồng (#BA7517) (mũi tên tăng nhẹ, dấu $ cách điệu). Chữ lớn "ĐĂNG KÝ NGAY" hoặc "ĐỪNG BỎ LỠ TẬP SAU" font góc cạnh bold theo `docs/Style-Guide-goc.md` mục 6, đặt phía trên đầu Gấu, không đè vào góc phải dưới.

## Prompt gen ảnh (tiếng Anh, ghép từ charStyle cố định)

```
[charStyle cố định của Gấu — dán nguyên văn từ docs/Visual-Prompts-goc.md mục 1, không rút gọn] + full-body shot, positioned on the left side of the frame, leaning posture with one hand in his trouser pocket, the other arm raised and pointing/gesturing toward the bottom-right corner of the frame with a smug smirk showing his gold tooth, as if inviting the viewer to click something there. Flat navy blue background (#0C447C) with minimal bronze-gold (#BA7517) financial icon accents (a small upward arrow, a stylized dollar sign). Leave the bottom-right corner of the frame clean and empty (no character, no icons, no text) to reserve space for a YouTube subscribe button overlay. 16:9, no text, professional quality.
```

## Việc chưa làm
- [ ] Gen ảnh bìa kêu gọi đăng ký chính thức, lưu thành `Fanpage-Asset/end-screen.jpg`.
- [ ] Chèn chữ CTA ("ĐĂNG KÝ NGAY" / "ĐỪNG BỎ LỠ TẬP SAU") thủ công sau khi có ảnh nền.

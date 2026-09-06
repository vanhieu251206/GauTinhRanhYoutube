# Bảng màu thương hiệu — "Gấu Tinh Ranh"

> File gốc duy nhất cho bảng màu kênh — mọi nơi khác (avatar, banner, prompt ảnh scene ở C3, thumbnail) chỉ tham chiếu tới đây, không tự định nghĩa màu riêng. Nguồn: `docs/Style-Guide-goc.md` mục 6.

## Bảng màu cố định
| Vai trò | Màu | Mã hex | Dùng ở đâu |
|---|---|---|---|
| Background | Xanh navy đậm | `#0C447C` | Nền thumbnail/banner, trang phục vest của Gấu |
| Accent | Vàng đồng | `#BA7517` | Kính lão gọng tròn của Gấu, chi tiết nhấn |
| Text chính | Trắng (viền đen) | `#FFFFFF` / `#000000` | Chữ thumbnail |
| Nhấn cảnh báo | Đỏ | `#E24B4A` | Tia chớp/điểm nhấn cảnh báo duy nhất khi thể hiện thua lỗ/rủi ro |

## Nguyên tắc dùng màu
- Gấu luôn giữ đúng bảng màu cố định: lông nâu đậm/đen (#4A3728), vest xanh navy (#0C447C), kính vàng đồng (#BA7517) — không đổi giữa các tập.
- Bối cảnh xung quanh (nền ảnh thật hoặc nền phẳng minh hoạ) dùng bảng màu chủ đạo xanh navy - vàng đồng - trắng - đen, chỉ dùng đỏ (#E24B4A) làm điểm nhấn cảnh báo duy nhất, không lạm dụng.
- Không dùng màu quá chói/neon, giữ đúng tinh thần flat 2D cartoon.

## Áp dụng
- `docs/Visual-Prompts-goc.md` — charStyle/bgStyle cố định dùng bảng màu này.
- `QuyTrinh/C3-Prompt-Anh.md`, `QuyTrinh/C6-Thumbnail.md` — mô tả style cố định dùng chung cho mọi prompt ảnh.

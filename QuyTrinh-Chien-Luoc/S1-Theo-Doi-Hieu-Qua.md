# S1 — Theo dõi hiệu quả sau đăng (24-48h)

## Khi nào chạy
Sau khi 1 video đăng được 24-48 giờ, người dùng lấy số liệu từ YouTube Studio (Impression, CTR, Retention, Watch time) và cung cấp cho Claude.

## Các bước
1. Hỏi người dùng số liệu của video vừa đăng: Impression (24-48h), CTR (%), Retention trung bình (%), tổng watch time.
2. Đối chiếu ngưỡng tham khảo (kinh nghiệm cá nhân, không phải chuẩn chính thức của YouTube):

| Impression 24-48h | Đánh giá |
|---|---|
| 0–50 | Rất yếu → xem lại thumbnail/tiêu đề, có thể bỏ hướng này |
| 200–400 | Có thể dùng nhưng chưa mạnh |
| 1.000+ | Tín hiệu tốt |
| 2.000+ | Rất tốt |

3. Ghi lại vào `docs/nhat-ky-hieu-qua.md` theo mẫu:

```markdown
## Tập N - [Tên video] (ngày đăng: YYYY-MM-DD)
- Thumbnail: [mô tả ngắn hoặc kiểu A/B/C]
- Hook/tiêu đề: [mô tả ngắn]
- Độ dài video: [phút]
- Impression (24-48h): [số]
- CTR: [%]
- Retention TB: [%]
- Nhận xét: [tốt/chưa tốt, vì sao theo suy đoán]
```

4. Không kết luận vội từ 1 video — chỉ ghi nhận dữ liệu. Việc tìm pattern làm ở **S2**.

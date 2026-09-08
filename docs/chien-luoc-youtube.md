# Chiến lược tăng trưởng YouTube — áp dụng cho kênh

> Đúc kết từ kinh nghiệm chia sẻ về thuật toán/chiến lược YouTube. Dùng để tham khảo khi chọn chủ đề (`QuyTrinh/C0-Chon-Chu-De.md`) và đăng bài (`QuyTrinh/C7-Dang-bai.md`).

## Nguyên tắc chính

1. **Phân phối theo nhóm thử nghiệm**: YouTube đẩy video tới nhóm nhỏ trước, đo CTR (thumbnail/title có click không) + Retention (xem tiếp không) rồi mới mở rộng. Không nên nghĩ "đăng xong chờ vài tháng tự lên" — cần tối ưu ngay từ đầu.

2. **Trust score kênh**: tài khoản/kênh hoạt động lâu, bình thường, không spam thường được ưu ái impression hơn kênh mới/hàng loạt. Kênh tốt + nội dung tốt không đảm bảo có view nếu trust thấp.

3. **Chọn ngách theo công thức "cầu cao, cung thấp"**: tìm chủ đề nhiều người tìm kiếm nhưng ít kênh làm; dấu hiệu tốt là kênh nhỏ (ít sub) nhưng có video view cao bất thường so với subscriber. Ngách đã chọn của kênh (phân tích tài chính/mô hình kinh doanh đời thường VN — xem `docs/DNA.md` mục 1) đi theo hướng này — ưu tiên đào sâu thay vì đổi sang nội dung đại trà.

4. **Đừng copy đối thủ — hãy "Decode → Different Angle → Create"**: phân tích lý do các video cùng ngách đang thành công, rồi tìm góc tiếp cận khác (đổi ngành nghề, đổi biến bóc tách chi phí) cho cùng nhu cầu khán giả, thay vì bê nguyên tiêu đề/thumbnail/nội dung. Copy làm loãng tệp khán giả, khiến YouTube khó phân phối đúng người.

5. **Video dài hơn có thể lợi nếu giữ được retention tương đương** — watch time tuyệt đối tăng theo độ dài × retention%. Không phải cứ dài là thắng, phải thực sự giữ được người xem.

6. **Nhịp kể chậm, có "khoảng thở"** phù hợp nội dung storytelling/kể chuyện (đúng định dạng ảnh tĩnh của kênh) — không cần cắt cảnh/hiệu ứng liên tục kiểu video ngắn giật gân. Mục tiêu không chỉ Retention mà còn Session Time (giữ người xem ở lại YouTube lâu hơn).

7. **Test có hệ thống, không làm theo cảm tính**: mỗi video coi như 1 test case, chỉ đổi 1-2 biến (thumbnail, hook, tiêu đề, độ dài) mỗi lần, đo CTR + retention, đúc kết công thức riêng của kênh sau 20-30 video thay vì đoán mò hoặc rập khuôn công thức người khác.

8. **Tránh "reused content" (nội dung lặp lại) — YouTube phạt kênh vi phạm bằng cách hạn chế/huỷ kiếm tiền, thậm chí gỡ kênh**: chính sách YouTube coi là nội dung lặp lại khi (a) dùng đi dùng lại 1 hình ảnh/đoạn video/asset y hệt xuyên suốt nhiều video dù asset đó miễn phí/tự tạo, hoặc (b) nội dung là copy/tái chế mà không thay đổi đáng kể hoặc không tạo ra giá trị mới cho người xem. Đây là lý do **quy trình sản xuất của kênh không được ghi cứng thành công thức/motif lặp lại y hệt mỗi tập** — cả ở kịch bản (`QuyTrinh/C1-Script.md` — kho kỹ thuật kể chuyện chọn linh hoạt, không phải checklist nhét đủ mọi tập) lẫn ở hình ảnh (`QuyTrinh/C3-Prompt-Anh.md` — mỗi scene/mỗi tập phải có bối cảnh/góc quay riêng, không tái dùng y hệt 1 ảnh nền cho nhiều video). **Mỗi tập phải research chuyên sâu riêng** (đúng chuẩn Bước 0.5 ở C1) để tạo giá trị thật, thông tin thật, góc nhìn thật cho người xem — không sản xuất theo kiểu rập khuôn/tái chế để chạy số lượng.

## Cách áp dụng vào quy trình kênh

- Khi chọn chủ đề (C0) và viết tiêu đề/mô tả (C7): tránh trùng lặp góc kể với các kênh tài chính khác, ưu tiên "different angle" cho cùng nhu cầu khán giả.
- Khi viết script (C1) và viết prompt ảnh (C3): không rập khuôn cùng 1 tổ hợp kỹ thuật/bối cảnh giữa các tập — mỗi tập là 1 lần research và dàn dựng mới, không tái chế tập trước.
- Sau mỗi video đăng, nên theo dõi CTR + Retention (24-48h đầu) để tích lũy dữ liệu test theo thời gian — ghi vào `docs/nhat-ky-hieu-qua.md` (tạo khi chạy S1 lần đầu).

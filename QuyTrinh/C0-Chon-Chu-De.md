# C0 — Chọn Chủ Đề (làm trước C1-Script)

> Đọc trước: `docs/DNA.md` (định vị, persona Gấu, khung an toàn),
> `docs/da-dung-de-tai.md` (kho ý tưởng chờ sản xuất + tránh trùng đề tài đã dùng), `docs/Chu-De-goc.md` (8 pillar, 24 topic chi tiết).
> Đầu ra của bước này: 1 dòng ý tưởng đã chốt lấy từ "Kho ý tưởng chờ sản xuất" trong `docs/da-dung-de-tai.md`, sẵn sàng cho C1-Script Bước 0.

## Bước 1 — Chọn topic theo launch sequence
Mặc định lấy topic **theo đúng thứ tự** trong bảng "Kho ý tưởng chờ sản xuất" ở `docs/da-dung-de-tai.md` (đã xếp launch sequence 8 video đầu theo lý do chiến lược ở `docs/Chu-De-goc.md` mục 4). Chỉ đổi thứ tự khi có lý do cụ thể (VD tín hiệu trend mạnh ở Bước 1.5, hoặc người dùng muốn đổi).

Nếu đã dùng hết 8 topic launch sequence, chọn tiếp trong "Topic còn lại" (16 topic chưa xếp lịch) — ưu tiên theo điểm số ở `docs/Chu-De-goc.md` mục 5 (Topic Scoring) nếu đã có, hoặc theo Pillar chưa khai thác nhiều để đa dạng nội dung.

## Bước 1.5 — Tra xu hướng chủ động (lớp lọc, không phải nguồn topic mới)
Trước khi qua outlier detection, chủ động tra xem có hiện tượng/trend tài chính-kinh doanh nào đang thật sự được bàn tán gần đây (mạng xã hội, thời sự đời sống VN) có thể gắn được vào 1 topic sẵn có không (dùng WebSearch nếu cần). Nếu tìm được 1 trend thật khớp, ưu tiên đẩy topic đó lên làm trước; nếu không tìm được gì thật sự khớp, bỏ qua bước này, không ép tìm cho có.

## Bước 2 — Outlier detection (soi đối thủ)
Người dùng thao tác trực tiếp trên vidIQ free (Claude không có quyền truy cập công cụ này) — Claude đưa ra **từ khoá/kênh cụ thể cần tra** mỗi lần làm C0 (ưu tiên kênh reference "Ếch Biết Tuốt" và các kênh phân tích tài chính/kinh doanh khác), người dùng tra trên vidIQ rồi báo lại số liệu để Claude đối chiếu và quyết định tiếp.
Tiêu chí: video nào có tỷ lệ view/subscriber > 20-30 lần là tín hiệu chủ đề/góc kể đang "bắt trend" thật. Ghi lại chủ đề, tiêu đề, thumbnail của video đó làm tín hiệu tham khảo — **không sao chép số liệu/kịch bản**, chỉ tham khảo góc kể/ngành nghề đang được quan tâm.

## Bước 2.5 — Kiểm tra ý tưởng trước khi chốt
1. **Nghịch lý/số liệu đủ gây tò mò** — topic phải có sẵn 1 con số cụ thể hoặc 1 nghịch lý rõ ràng ngay trong Hook (VD "đông khách nhưng vẫn ế", "ly 25.000đ lãi được bao nhiêu"). Nếu topic chỉ là mô tả ngành nghề chung chung không có góc bất ngờ, quay lại tìm số liệu/nghịch lý cụ thể trước khi chốt.
2. **Góc kể unique không trùng tập trước** — đối chiếu cột "Góc kể unique" đã dùng ở `docs/da-dung-de-tai.md`, tránh lặp lại đúng 1 kiểu phân tích (VD lần nào cũng chỉ nói COGS mà không đổi biến khác như chi phí ẩn/mô hình môi giới/chiết khấu app).
3. **Ít rủi ro pháp lý** — không nêu đích danh 1 thương hiệu/chuỗi cụ thể kèm phán xét tiêu cực, giữ đúng khung an toàn `docs/DNA.md` mục 4.

## Bước 3 — Tìm số liệu/tình huống cụ thể
Không chỉ nói ngành nghề chung ("kinh doanh trà sữa") mà tìm được ít nhất 1-2 con số cụ thể làm chất liệu Hook (giá bán, giá vốn ước tính, số lượng cần bán để hoà vốn...) — dùng WebSearch nếu cần tra cứu mặt bằng giá/chi phí phổ biến tại Việt Nam, luôn gắn khung "ước tính/tổng hợp" theo disclaimer, không bịa số chính xác tuyệt đối.

## Bước 4 — Đối chiếu tránh trùng
Tra bảng "Đã dùng" trong `docs/da-dung-de-tai.md` — đảm bảo không trùng ngành nghề, góc kể, hoặc bối cảnh đã kể ở các tập trước.

## Bước 5 — Chốt ý tưởng cho tập này
Chốt 1 ý tưởng đủ dùng cho tập đang làm, theo format:
`[Ngành nghề/chủ đề cụ thể] — [Pillar] — [Formula tiêu đề A/B/C] — [Góc kể/số liệu dự kiến]`
Đưa thẳng ý tưởng này sang C1-Script (chỉ ghi vào bảng "Đã dùng" ở `docs/da-dung-de-tai.md` sau khi đã chốt script, theo `QuyTrinh/C1-Script.md` Bước 6, và xoá dòng tương ứng khỏi "Kho ý tưởng chờ sản xuất"). Nếu ý tưởng bị loại ở Bước 2.5, ghi vào mục "Ý tưởng đã xét nhưng loại bỏ" để không research trùng lần sau.

## Bước 6 — Phác ý tưởng thumbnail sớm (trước khi viết script)
Trước khi qua C1, nghĩ nhanh: khoảnh khắc/biểu cảm nào của Gấu (nheo mắt tính toán, cười khẩy, dò xét qua kính...) đủ mạnh để làm thumbnail, kết hợp con số/nghịch lý chính của tập. Tham khảo Thumbnail Text Bank ở `docs/Style-Guide-goc.md` mục 6. Đây chỉ là **định hướng ý tưởng**, asset thật làm ở `C6-Thumbnail.md` sau khi có ảnh từ C3.

## Lưu ý an toàn
Không tư vấn đầu tư trực tiếp, không nêu đích danh doanh nghiệp/cá nhân kèm phán xét tiêu cực, không dùng số liệu bịa — đối chiếu ngay khung an toàn nội dung ở `docs/DNA.md` mục 4 trước khi chốt.

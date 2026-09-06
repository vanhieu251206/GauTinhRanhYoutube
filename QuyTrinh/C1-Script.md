# C1 — Viết Kịch Bản (Script)

> Đọc trước khi bắt đầu: `docs/DNA.md` (định vị, persona Gấu, khung an toàn), `docs/cach-lam-chuan.md` (nguyên tắc ưu tiên),
> `docs/da-dung-de-tai.md` (tránh trùng đề tài), `docs/Style-Guide-goc.md` (voice rules block, benchmark passages).
> Đầu ra của bước này: `Bai-Dang/Tap N - [tên]/script.md` và `voice-script.txt`.

## Bước 0 — Chọn đề tài
Đã chốt ở `QuyTrinh/C0-Chon-Chu-De.md` — dùng ý tưởng vừa chốt ở bước C0 cho tập này.

## Bước 0.5 — Tra cứu số liệu thật (bắt buộc trước khi viết)
Trước khi dàn khung, chủ động tìm (dùng WebSearch nếu cần) số liệu/mặt bằng giá thực tế tại Việt Nam cho ngành nghề đang phân tích: giá bán phổ biến, ước tính giá vốn/nguyên liệu, chi phí mặt bằng/nhân công thường gặp, mức chiết khấu app (nếu có)... Ghi lại các con số dùng trong script — vì đây là kênh "ước tính/tổng hợp cá nhân" (đúng disclaimer), không cần số liệu chính xác tuyệt đối nhưng phải hợp lý/có căn cứ, không bịa số vô căn cứ.

## Bước 1 — Xác định khung video (theo `docs/DNA.md` mục 3)

| Bước | Thời lượng gợi ý | Nội dung |
|---|---|---|
| 1. Hook | 0-15 giây | Nêu nghịch lý/số liệu cụ thể gây tò mò ngay câu đầu (theo mẫu hook ở `docs/Channel-DNA-goc.md` mục 2) |
| 2. Disclaimer | ngay sau Hook | Đọc nguyên văn câu disclaimer cố định (`docs/DNA.md` mục 5) |
| 3. Bối cảnh ngành | ~10-15% | Giới thiệu mô hình/ngành nghề đang phân tích, quy mô phổ biến |
| 4. Bóc tách COGS + chi phí cố định | ~35-40% | Liệt kê từng khoản chi phí, giải thích ngay mọi thuật ngữ tài chính vừa nhắc (COGS, chi phí cố định, lãi gộp...) |
| 5. Điểm hoà vốn + chi phí ẩn/cơ hội | ~25-30% | Mở đầu bằng câu nối cố định "Giờ mới đến khúc xương khó nhằn đây..." — tính điểm hoà vốn cụ thể, nêu chi phí ẩn ít ai để ý |
| 6. Kết luận + catchphrase | ~5-10% | Bài học tài chính rút ra + câu hỏi tương tác cuối (KHÔNG teaser tập sau) + catchphrase kết cố định |

Ghi rõ ranh giới từng bước trong `script.md` (VD: "--- BƯỚC 4: BÓC TÁCH COGS ---") để dễ đối chiếu khi dựng.

## Bước 1.5 — Kỹ thuật viết
1. **Hook mở bằng số liệu/nghịch lý cụ thể**, không mở bằng câu hỏi tự soi hay lời chào dài dòng.
2. **Câu ngắn 10-20 từ là chủ đạo, không quá 25 từ** (theo `docs/Style-Guide-goc.md` mục 2) — nhịp câu ngắn-dài xen kẽ, câu dài hơn khi giải thích cơ chế, câu cực ngắn khi chốt ý.
3. **Mỗi thuật ngữ tài chính phải giải thích ngay lập tức** bằng ví von đời thường (xem benchmark ở `docs/Style-Guide-goc.md` mục 4) — không để thuật ngữ trôi qua mà không giải thích.
4. **Giữ giọng "tôi thấy vậy, anh em thấy sao"** — không áp đặt kiểu chuyên gia biết tuốt, đối chiếu `docs/Style-Guide-goc.md` mục 1-2.
5. **Không đưa lời khuyên đầu tư trực tiếp** — chỉ phân tích/bóc tách, không nói "nên làm"/"nên vay"/"nên đầu tư".
6. **Dùng đúng 2 câu cố định nguyên văn**: disclaimer (Bước 2) và câu nối "Giờ mới đến khúc xương khó nhằn đây..." (Bước 5) — không diễn đạt lại theo ý riêng.

## Bước 2 — Áp dụng công thức tiêu đề
Dùng đúng 1 trong 3 Formula (A/B/C) đã chốt ở `docs/Channel-DNA-goc.md` mục 1, đối chiếu công thức 3 yếu tố ở `docs/cach-lam-chuan.md` mục 10.

## Bước 3 — Viết script
1. Viết `Bai-Dang/Tap N - [tên]/script.md`: dàn ý theo bảng ở Bước 1, đánh dấu ranh giới từng bước bằng heading rõ ràng.
2. Viết `voice-script.txt`: bản chính tả đầy đủ, câu văn tự nhiên khi đọc thành tiếng, đúng văn phong Gấu (xem `docs/Style-Guide-goc.md` mục 3 — Voice Rules Block, có thể dùng trực tiếp làm system prompt nếu cần).
3. Cắt bỏ mọi chi tiết không phục vụ trực tiếp mạch bóc tách chi phí hoặc câu hỏi người xem đang tò mò.

## Bước 3.5 — Tự kiểm tra dấu hiệu "AI hoá"
Rà lại toàn bộ `voice-script.txt`: câu có đều đều máy móc không, có liệt kê đối xứng sáo rỗng không, có dùng cụm từ cấm ở `docs/DNA.md` mục 7 không, có câu nào quá 25 từ không. Sửa lại trước khi đưa người dùng đọc.

## Bước 4 — Checklist an toàn nội dung (BẮT BUỘC trước khi qua bước tiếp theo)
Đối chiếu với `docs/DNA.md` mục 4:
- [ ] Không tư vấn đầu tư cụ thể (không nói mua cổ phiếu/coin/mã nào, không nói "nên vay"/"nên đầu tư").
- [ ] Không nêu đích danh doanh nghiệp/cá nhân cụ thể kèm phán xét tiêu cực.
- [ ] Số liệu dùng có căn cứ hợp lý, đóng khung "ước tính/tổng hợp cá nhân" (không bịa số chính xác tuyệt đối).
- [ ] Có đủ disclaimer cố định và catchphrase kết cố định, đúng nguyên văn.
- [ ] **Người dùng đã tự đọc lại toàn bộ `script.md`/`voice-script.txt` và có ít nhất 1 chỗ chỉnh sửa/góp ý tay thực chất** — nếu không có gì cần sửa, người dùng xác nhận rõ bằng lời trước khi qua bước tiếp theo.
- [ ] Không dùng cụm từ cấm (xem `docs/DNA.md` mục 7).

## Bước 5 — Ước lượng & đề xuất bổ trợ
1. Ước lượng thời lượng đọc — đo tốc độ TTS thật sau khi có `voice.mp3` tập đầu tiên, cập nhật số từ/phút vào đây để dùng cho các tập sau. Mốc thời lượng mục tiêu: 7-9 phút/video (`docs/Style-Guide-goc.md` mục 7).
2. Đánh dấu 1-2 đoạn cao trào/hook mạnh nhất (thường là đoạn tính điểm hoà vốn) — gợi ý điểm cắt Shorts (30-60s).
3. Đề xuất 3-5 phương án tiêu đề (dùng cả 3 Formula nếu hợp) + concept thumbnail đi kèm (tham khảo Thumbnail Text Bank ở `docs/Style-Guide-goc.md` mục 6).

## Bước 6 — Cập nhật kho đề tài
Sau khi chốt script, thêm 1 dòng vào bảng "Đã dùng" trong `docs/da-dung-de-tai.md`, ghi rõ số tập, và xoá dòng tương ứng khỏi bảng "Kho ý tưởng chờ sản xuất".

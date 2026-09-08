# C1 — Viết Kịch Bản (Script)

> Đọc trước khi bắt đầu: `docs/DNA.md` (định vị, persona Gấu, khung an toàn), `docs/cach-lam-chuan.md` (nguyên tắc ưu tiên),
> `docs/da-dung-de-tai.md` (tránh trùng đề tài), `docs/Style-Guide-goc.md` (voice rules block, benchmark passages).
> Đầu ra của bước này: `Bai-Dang/Tap N - [tên]/script.md` và `voice-script.txt`.

## Bước 0 — Chọn đề tài
Đã chốt ở `QuyTrinh/C0-Chon-Chu-De.md` — dùng ý tưởng vừa chốt ở bước C0 cho tập này.

## Bước 0.5 — Tra cứu số liệu thật (bắt buộc trước khi viết, làm SÂU — đây là bước quan trọng nhất quyết định uy tín kênh)
Số liệu hời hợt/chung chung là thứ phá uy tín kênh nhanh nhất — khán giả trong ngành xem được là biết ngay có bịa hay không. Vì vậy bước này KHÔNG được làm qua loa 1-2 lượt tìm rồi chốt số, mà phải nghiên cứu nhiều lớp:

1. **Tra đủ 6 nhóm số liệu tối thiểu** cho ngành đang phân tích: (1) giá bán phổ biến theo phân khúc, (2) giá vốn/nguyên liệu hoặc chi phí đầu vào, (3) chi phí cố định thường gặp (mặt bằng, nhân công, điện nước, khấu hao), (4) quy mô thị trường/số lượng cơ sở kinh doanh có mốc năm cụ thể (để so sánh tăng/giảm theo thời gian), (5) khung pháp lý/quy định liên quan nếu ngành có (mức trần lãi suất, điều kiện kinh doanh, thuế...), (6) **1 thống kê gây sốc** dạng tỷ lệ (VD tỷ lệ thất bại năm đầu, tỷ lệ hộ kinh doanh thua lỗ, tỷ lệ đóng cửa...) — loại số liệu này rất mạnh làm nghịch lý phụ ở Bước 3 (Bối cảnh) vì tạo tương phản với hình ảnh "ngành đang bùng nổ".
2. **Đối chiếu tối thiểu 2-3 nguồn độc lập** cho mỗi nhóm số liệu quan trọng (không chỉ tin 1 bài viết) — nếu các nguồn lệch nhau nhiều, ghi rõ khoảng dao động thay vì chọn liều 1 số, và luôn đóng khung "ước tính/tổng hợp cá nhân" đúng disclaimer.
3. **Ưu tiên số liệu có mốc năm cụ thể** (VD "năm 2019 có X, năm 2020 còn Y, giảm Z%") thay vì chỉ 1 khoảng số chung chung — số liệu theo mốc thời gian tạo cảm giác đáng tin hơn nhiều so với số liệu tĩnh.
4. **Tìm ít nhất 1 thuật ngữ tài chính trung tâm** của tập (VD COGS, điểm hoà vốn, tỷ lệ cho vay trên giá trị tài sản...) và chuẩn bị sẵn 1 ví dụ số cụ thể đi kèm để quay lại minh hoạ nhiều lần trong script (theo Bước 1.5 mục 3).
5. **Nếu ngành có góc pháp lý/rủi ro/quy định đáng chú ý** (mức lãi trần, điều kiện cấp phép, thuế mới áp dụng...), tra cứu riêng để có thể dùng làm đoạn mở rộng rủi ro/xu hướng tương lai (xem kho kỹ thuật bổ trợ ở Bước 1.5) — không bắt ép nếu ngành không có gì đáng nói ở đây.
6. **Tìm 1 case study thật minh hoạ đúng nghịch lý chính của tập** (VD 1 doanh nghiệp có thật, số liệu công khai trên báo chí — doanh thu, số cửa hàng, lãi/lỗ theo năm) — case study thật có sức nặng hơn hẳn số liệu trung bình chung chung vì có tên tuổi/câu chuyện cụ thể đứng sau. **Bắt buộc ẩn danh khi đưa vào voice-script** (xem kho kỹ thuật bổ trợ ở Bước 1.5) — chỉ dùng số liệu công khai mang tính mô tả trung lập, không nêu tên thương hiệu.
7. Ghi lại toàn bộ số liệu + nguồn tham khảo vào `script.md` (mục "Số liệu dùng trong script") trước khi viết `voice-script.txt` — không nhớ nhẩm rồi viết trực tiếp.

## Bước 1 — Xác định khung video (theo `docs/DNA.md` mục 3 — khung lõi cố định thứ tự)

| Bước | Thời lượng gợi ý | Nội dung |
|---|---|---|
| 1. Hook | 0-15 giây | Nêu nghịch lý/số liệu cụ thể gây tò mò ngay câu đầu (theo mẫu hook ở `docs/Channel-DNA-goc.md` mục 2) |
| 2. Disclaimer | ngay sau Hook | Đọc nguyên văn câu disclaimer cố định (`docs/DNA.md` mục 5) |
| 3. Bối cảnh ngành | ~10-20% | Giới thiệu mô hình/ngành nghề đang phân tích, quy mô phổ biến |
| 4. Bóc tách COGS + chi phí cố định | ~30-40% | Liệt kê từng khoản chi phí, giải thích ngay mọi thuật ngữ tài chính vừa nhắc (COGS, chi phí cố định, lãi gộp...) |
| 5. Điểm hoà vốn + chi phí ẩn/cơ hội | ~20-30% | Mở đầu bằng câu nối cố định "Giờ mới đến khúc xương khó nhằn đây..." — tính điểm hoà vốn cụ thể, nêu chi phí ẩn ít ai để ý |
| 6. Kết luận + catchphrase | ~5-10% | Bài học tài chính rút ra + câu hỏi tương tác cuối (KHÔNG teaser tập sau) + catchphrase kết cố định |

Ghi rõ ranh giới từng bước trong `script.md` (VD: "--- BƯỚC 4: BÓC TÁCH COGS ---") để dễ đối chiếu khi dựng. % thời lượng co giãn tuỳ tập, không ép cứng.

## Bước 1.5 — Kỹ thuật viết

**Nguyên tắc bắt buộc:**
1. **Hook mở bằng số liệu/nghịch lý cụ thể**, không mở bằng câu hỏi tự soi hay lời chào dài dòng. 3 mẫu hook ở `docs/Channel-DNA-goc.md` mục 2 chỉ là kho tham khảo — **hỏi người dùng mỗi lần viết hook**: dùng 1 mẫu có sẵn hay tự viết câu mở mới cho tập này.
2. **Câu ngắn 10-20 từ là chủ đạo, không quá 25 từ** (theo `docs/Style-Guide-goc.md` mục 2) — nhịp câu ngắn-dài xen kẽ, câu dài hơn khi giải thích cơ chế, câu cực ngắn khi chốt ý.
3. **Mỗi thuật ngữ tài chính phải giải thích ngay lập tức** bằng ví von đời thường (xem benchmark ở `docs/Style-Guide-goc.md` mục 4) — không để thuật ngữ trôi qua mà không giải thích.
4. **Giữ giọng "tôi thấy vậy, anh em thấy sao"** — không áp đặt kiểu chuyên gia biết tuốt, đối chiếu `docs/Style-Guide-goc.md` mục 1-2.
5. **Không đưa lời khuyên đầu tư trực tiếp** — chỉ phân tích/bóc tách, không nói "nên làm"/"nên vay"/"nên đầu tư".
6. **Dùng đúng 2 câu cố định nguyên văn**: disclaimer (Bước 2) và câu nối "Giờ mới đến khúc xương khó nhằn đây..." (Bước 5) — không diễn đạt lại theo ý riêng.

**Kho kỹ thuật kể chuyện bổ trợ (chọn linh hoạt, KHÔNG phải công thức cố định):**
Đây là các "đạo cụ" có thể dùng để tăng chiều sâu/sức hút cho 1 tập, không phải checklist phải nhét đủ vào mọi video theo đúng 1 vị trí. Mỗi tập tự cân nhắc dùng cái nào, dùng bao nhiêu, đặt ở đâu — **tránh dùng lặp lại y hệt combo/vị trí như tập ngay trước đó**, để các tập không nghe rập khuôn:
- **Giai thoại mở bài**: hook có thể qua 1 tình huống cá nhân ngắn (kiểu "Tôi có ông anh họ...") thay vì luôn đi thẳng số liệu.
- **Số liệu theo mốc năm**: ưu tiên khi tìm được số liệu quy mô thị trường có mốc năm cụ thể (VD "2019 có X, 2020 còn Y") thay vì chỉ 1 khoảng số tĩnh.
- **Thuật ngữ trung tâm quay lại nhiều lần**: nếu tập có 1 thuật ngữ tài chính then chốt, có thể minh hoạ lại bằng ví dụ số ở nhiều đoạn khác nhau thay vì giải thích 1 lần rồi bỏ.
- **Case study thật (ẩn danh)**: nếu tìm được 1 doanh nghiệp thật có số liệu công khai minh hoạ đúng nghịch lý chính, có thể kể lại — **bắt buộc ẩn danh triệt để** (không tên thương hiệu, không chi tiết định danh được như logo/slogan/nhà sáng lập, chỉ giữ số liệu định lượng và mô tả chung). Không phải tập nào cũng cần có case study.
- **Mid-roll CTA**: 1 câu ngắn mời thích + đăng ký đặt tự nhiên ở giữa video, hợp với video dài/nhiều lớp phân tích — không bắt buộc, và nếu dùng thì đổi cách diễn đạt mỗi tập, không lặp câu y hệt.
- **Mở rộng rủi ro pháp lý/xu hướng tương lai**: nếu ngành có góc này đáng chú ý, có thể thêm đoạn riêng trước kết luận — bỏ qua nếu ngành không có gì đáng nói.

Trước khi chốt script, đối chiếu nhanh với 1-2 tập gần nhất (`docs/da-dung-de-tai.md`) xem có đang lặp lại y hệt tổ hợp kỹ thuật (VD tập nào cũng mở giai thoại + luôn có case study + luôn mid-roll ở đúng chỗ) — nếu có, chủ động đổi cách làm cho tập này.

## Bước 2 — Áp dụng công thức tiêu đề
Bắt buộc đạt đủ 3 yếu tố ở `docs/cach-lam-chuan.md` mục 10 (từ khoá, gây tò mò, đúng nội dung thật). 3 Formula (A/B/C) ở `docs/Channel-DNA-goc.md` mục 1 là kho mẫu có sẵn, không bắt buộc — **hỏi người dùng mỗi lần tới bước này**: dùng 1 trong 3 Formula có sẵn, hay tự viết cấu trúc tiêu đề mới cho tập này (để tránh nhiều tập liền dùng đúng 1 khuôn nghe rập khuôn).

## Bước 3 — Viết script
1. Viết `Bai-Dang/Tap N - [tên]/script.md`: dàn ý theo bảng ở Bước 1, đánh dấu ranh giới từng bước bằng heading rõ ràng.
2. Viết `voice-script.txt`: bản chính tả đầy đủ, câu văn tự nhiên khi đọc thành tiếng, đúng văn phong Gấu (xem `docs/Style-Guide-goc.md` mục 3 — Voice Rules Block, có thể dùng trực tiếp làm system prompt nếu cần).
3. Cắt bỏ mọi chi tiết không phục vụ trực tiếp mạch bóc tách chi phí hoặc câu hỏi người xem đang tò mò.

## Bước 3.5 — Tự kiểm tra dấu hiệu "AI hoá"
Rà lại toàn bộ `voice-script.txt`: câu có đều đều máy móc không, có liệt kê đối xứng sáo rỗng không, có dùng cụm từ cấm ở `docs/DNA.md` mục 7 không, có câu nào quá 25 từ không. Sửa lại trước khi đưa người dùng đọc.

**Kiểm tra riêng cho `voice-script.txt` (bắt buộc, vì file này đọc thẳng bằng AI voice, không qua chỉnh sửa thủ công):** AI đọc tốt tiếng Việt thuần, các từ tiếng Anh trọn vẹn phổ biến (VD "marketing"), và một số acronym phát âm được liền như 1 từ đã test thực tế đọc ổn (VD "COGS" — đã kiểm chứng đọc đúng, giữ nguyên không cần phiên âm). Nhưng AI vẫn đọc sai/đọc rời rạc với các từ viết tắt ghép ký hiệu hoặc chuỗi chữ cái không tạo thành âm đọc tự nhiên (VD "F&B", "SOP", "KPI", "P&L").

Xử lý: mặc định **viết ra đúng cách đọc từng chữ cái bằng chữ tiếng Việt** (theo tên chữ cái tiếng Anh phiên âm) cho các trường hợp có ký hiệu/không đọc tự nhiên được. Ví dụ: "F&B" → "Ép En Bi"; "SOP" → "Ét Ô Pi"; "KPI" → "Ca Pi Ai". Nếu không chắc một acronym cụ thể AI đọc được hay không, cứ thử để nguyên trước — nếu nghe voice.mp3 thật thấy đọc sai/lạ thì mới đổi sang phiên âm ở bản chỉnh sửa sau. Có thể giải thích nghĩa/tên đầy đủ ngay sau lần đầu xuất hiện, giống cách giải thích mọi thuật ngữ khác.

## Bước 4 — Checklist an toàn nội dung (BẮT BUỘC trước khi qua bước tiếp theo)
Đối chiếu với `docs/DNA.md` mục 4:
- [ ] Không tư vấn đầu tư cụ thể (không nói mua cổ phiếu/coin/mã nào, không nói "nên vay"/"nên đầu tư").
- [ ] Không nêu đích danh doanh nghiệp/cá nhân cụ thể kèm phán xét tiêu cực — nếu có dùng case study thật, đã ẩn danh triệt để theo kho kỹ thuật bổ trợ ở Bước 1.5 (không tên thương hiệu, không chi tiết định danh được).
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

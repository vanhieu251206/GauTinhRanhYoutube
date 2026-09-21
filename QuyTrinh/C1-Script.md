# C1 — Viết Kịch Bản (Script)

> Đọc trước khi bắt đầu: `docs/DNA.md` (định vị, persona Gấu, khung an toàn), `docs/cach-lam-chuan.md` (nguyên tắc ưu tiên),
> `docs/da-dung-de-tai.md` (tránh trùng đề tài), `docs/Style-Guide-goc.md` (voice rules block, benchmark passages),
> `docs/ky-thuat-ke-chuyen-doi-thu.md` (kho kỹ thuật kể chuyện đúc kết từ script đối thủ — dùng bổ trợ ở Bước 1.5).
> Đầu ra của bước này: `Bai-Dang/Tap N - [tên]/script.md` và `voice-script.md`.

## Bước 0 — Chọn đề tài
Đã chốt ở `QuyTrinh/C0-Chon-Chu-De.md` — dùng ý tưởng vừa chốt ở bước C0 cho tập này.

## Bước 0.5 — Tra cứu số liệu thật (bắt buộc trước khi viết, làm SÂU — đây là bước quan trọng nhất quyết định uy tín kênh)
Số liệu hời hợt/chung chung là thứ phá uy tín kênh nhanh nhất — khán giả trong ngành xem được là biết ngay có bịa hay không. Vì vậy bước này KHÔNG được làm qua loa 1-2 lượt tìm rồi chốt số, mà phải nghiên cứu nhiều lớp:

1. **Tra đủ 6 nhóm số liệu tối thiểu** cho ngành đang phân tích: (1) giá bán phổ biến theo phân khúc, (2) giá vốn/nguyên liệu hoặc chi phí đầu vào, (3) chi phí cố định thường gặp (mặt bằng, nhân công, điện nước, khấu hao), (4) quy mô thị trường/số lượng cơ sở kinh doanh có mốc năm cụ thể (để so sánh tăng/giảm theo thời gian), (5) khung pháp lý/quy định liên quan nếu ngành có (mức trần lãi suất, điều kiện kinh doanh, thuế...), (6) **1 thống kê gây sốc** dạng tỷ lệ (VD tỷ lệ thất bại năm đầu, tỷ lệ hộ kinh doanh thua lỗ, tỷ lệ đóng cửa...) — loại số liệu này rất mạnh làm nghịch lý phụ ở Bước 3 (Bối cảnh) vì tạo tương phản với hình ảnh "ngành đang bùng nổ".
2. **Đối chiếu tối thiểu 2-3 nguồn độc lập** cho mỗi nhóm số liệu quan trọng (không chỉ tin 1 bài viết) — nếu các nguồn lệch nhau nhiều, ghi rõ khoảng dao động thay vì chọn liều 1 số, và luôn đóng khung "ước tính/tổng hợp cá nhân" đúng disclaimer.
2.5. **QUY TẮC CỨNG — WebSearch chỉ dùng để TÌM đường dẫn bài viết, KHÔNG BAO GIỜ được trích số liệu/sự kiện/mốc thời gian trực tiếp từ bản tóm tắt do WebSearch tự tổng hợp. Mọi con số/sự kiện/mốc thời gian đưa vào `script.md` bắt buộc phải `WebFetch` đọc đúng bài gốc trước, không có ngoại lệ.** Áp dụng cho toàn bộ quy trình sản xuất (C0 tra trend, C1 tra số liệu, không riêng bước nào). Bản tóm tắt tự động của WebSearch có thể gộp nhầm nhiều nguồn/nhiều mốc thời gian khác nhau thành 1 con số duy nhất, hoặc gộp nhầm số liệu của 2 phân khúc/loại hình dịch vụ khác nhau của cùng 1 doanh nghiệp thành 1 con số chung (xem lỗi thật đã xảy ra ở mục 2.6). Khi WebFetch bài gốc, luôn lấy đúng **ngày đăng bài** khi số liệu gắn với mốc thời gian cụ thể.
2.6. **Khi doanh nghiệp/ngành đang phân tích có nhiều loại hình dịch vụ/phân khúc con khác nhau (VD GrabBike xe máy vs GrabCar ô tô; gói cước A vs gói cước B), phải kiểm tra kỹ mỗi con số cụ thể gắn với ĐÚNG loại hình nào trước khi dùng, không mặc định áp 1 con số chung cho toàn bộ doanh nghiệp.** Lỗi này từng xảy ra thật: dùng nhầm số chi phí xăng và % chiết khấu của GrabCar (ô tô) gán cho GrabBike (xe máy) dù case chính của video là xe máy — vì bản tóm tắt tìm kiếm không luôn nêu rõ loại hình dịch vụ, dễ đọc lướt qua mà không để ý. Khi fetch trực tiếp bài gốc (theo mục 2.5), đọc kỹ xem đoạn chứa con số đó có ghi rõ tên loại hình dịch vụ cụ thể hay không.
3. **Ưu tiên số liệu có mốc năm cụ thể** (VD "năm 2019 có X, năm 2020 còn Y, giảm Z%") thay vì chỉ 1 khoảng số chung chung — số liệu theo mốc thời gian tạo cảm giác đáng tin hơn nhiều so với số liệu tĩnh.
3.5. **Ưu tiên số liệu mới nhất hiện có** — chỉ dùng số liệu cũ khi so sánh quá khứ/hiện tại, kể vòng đời doanh nghiệp, hoặc số liệu quy định/định nghĩa ít đổi. Nguồn mới lệch nhau thì báo người dùng, không tự chọn liều (như mục 2).

4. **Tìm ít nhất 1 thuật ngữ tài chính trung tâm** của tập (VD COGS, điểm hoà vốn, tỷ lệ cho vay trên giá trị tài sản...) và chuẩn bị sẵn 1 ví dụ số cụ thể đi kèm để quay lại minh hoạ nhiều lần trong script (theo Bước 1.5 mục 3).
5. **Nếu ngành có góc pháp lý/rủi ro/quy định đáng chú ý** (mức lãi trần, điều kiện cấp phép, thuế mới áp dụng...), tra cứu riêng để có thể dùng làm đoạn mở rộng rủi ro/xu hướng tương lai (xem kho kỹ thuật bổ trợ ở Bước 1.5) — không bắt ép nếu ngành không có gì đáng nói ở đây.
6. **Tìm 1 case study thật minh hoạ đúng nghịch lý chính của tập** (VD 1 doanh nghiệp có thật, số liệu công khai trên báo chí — doanh thu, số cửa hàng, lãi/lỗ theo năm) — case study thật có sức nặng hơn hẳn số liệu trung bình chung chung vì có tên tuổi/câu chuyện cụ thể đứng sau. **Được nêu đích danh doanh nghiệp nếu mọi số liệu/sự kiện đã WebFetch xác nhận nguồn báo chí gốc** (theo `docs/DNA.md` mục 4) — chỉ thuật lại đúng sự kiện đã công bố, không suy diễn/phán xét thêm; nếu số liệu chưa kiểm chứng được chắc chắn, ẩn danh như kho kỹ thuật bổ trợ ở Bước 1.5.
7. **Ghi lại toàn bộ số liệu đã WebFetch xác nhận vào file riêng `Bai-Dang/Tap N - [tên]/so-lieu-xac-nhan.md`** (không gộp chung vào `script.md`) ngay khi xác nhận xong từng nguồn, trước khi viết `voice-script.md` — không nhớ nhẩm rồi viết trực tiếp. Mỗi dòng số liệu ghi đủ 4 cột: Nhóm / Số liệu cụ thể / Nguồn (link) + Ngày đăng / **Trích dẫn nguyên văn để Ctrl+F định vị đoạn crop** — đúng format bảng đã dùng ở Tập 7-8. File này là nhật ký nghiên cứu thật của tập, tách biệt khỏi `script.md` (kịch bản đã chọn lọc) để giữ lại đầy đủ dấu vết đối chiếu nguồn kể cả những số liệu sau đó bị loại khỏi bản đọc. **Đồng thời đây là nguồn để lập "danh sách nguồn số liệu" trong MÔ TẢ video ở C8** (số liệu không nêu tên nguồn trong lời thoại vẫn phải có đủ dòng ở đây, kèm link + ngày đăng).
7.1. **Cột trích dẫn nguyên văn phải là câu/cụm chữ có trong dấu ngoặc kép mà WebFetch trả về, KHÔNG phải phần diễn giải/tóm tắt lại của model đọc trang** — nếu kết quả WebFetch chỉ diễn giải lại 1 số liệu mà không có nguyên văn trong ngoặc kép, đánh dấu `⚠️` ở dòng đó và **WebFetch lại 1 lần nữa** với prompt yêu cầu rõ "trích nguyên văn trong dấu ngoặc kép, không diễn giải" trước khi coi số liệu đó là đã xác nhận xong — không được để sót dấu `⚠️` nào trong file trước khi chuyển qua viết `voice-script.md`. Mục đích: (a) tăng độ chính xác khi đọc số trong voice-script, (b) cho phép người dùng mở đúng link, Ctrl+F đúng cụm trích dẫn, chụp màn hình đúng đoạn văn bản đó (kèm tên báo/logo) để làm ảnh minh hoạ nguồn trong scene, không phải đọc lại cả bài để tìm.
7.5. **Quy tắc cứng — chọn lọc trước khi đưa vào `voice-script.md`:** sau khi research đủ 6 nhóm số liệu, không mặc định đưa hết vào bản đọc. Với mỗi số liệu, tự hỏi nó có phục vụ trực tiếp nghịch lý/hook/thesis chính của tập hay chỉ là thông tin liên quan chung chung. Nếu chỉ liên quan mà không đẩy mạch kể lên (VD trùng ý với 1 số liệu khác đã đủ mạnh, hoặc lạc sang nhánh phụ ngoài trọng tâm), giữ nguyên trong `so-lieu-xac-nhan.md` làm tham khảo và ghi rõ "loại khỏi voice-script" kèm lý do, không đưa vào bản đọc cuối.
8. Research thật qua các bài báo/nguồn uy tín (không bịa/đoán số liệu) để tìm góc hay, không chỉ tra số cho đủ 6 nhóm ở trên.
9. Nếu có `Bai-Dang/Tap N - [tên]/doi-thu/` (người dùng tự để sẵn), đọc để tham khảo góc kể/số liệu hay — chỉ lấy Ý, viết lại hoàn toàn bằng giọng Gấu, KHÔNG copy nguyên văn câu chữ đối thủ.
9.5. **Quy tắc cứng — khi người dùng đã mô tả cụ thể ý tưởng/khung nội dung của tập (ở C0 hoặc trực tiếp trong hội thoại), script đối thủ CHỈ được dùng để học kỹ thuật kể chuyện/cách diễn đạt hay (VD cách mở hook, cách ví von, cách chuyển ý), KHÔNG được dùng để mở rộng thêm nội dung/góc kể/case study/số liệu nằm ngoài phạm vi ý tưởng người dùng đã mô tả.** Nếu trong lúc research hoặc đọc script đối thủ phát hiện góc hay nhưng nằm ngoài khung ý tưởng gốc, phải hỏi lại người dùng có muốn mở rộng khung hay không trước khi đưa vào script.md, không tự ý thêm vào rồi mới hỏi sau. Vi phạm quy tắc này dẫn tới lệch khung ý tưởng đã chốt, phải viết lại từ đầu.

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

**Khung tự do (quy tắc cứng ở `docs/DNA.md` mục 3):** bảng trên là khung MẶC ĐỊNH. Người dùng được chọn khung tự do (sắp xếp mạch kể theo hành trình câu hỏi của khán giả, không bắt buộc khối "bối cảnh ngành" riêng), nhưng vẫn phải giữ hook 3 pha, disclaimer ngay sau hook, câu nối cố định trước phần hoà vốn/chi phí ẩn, giải thích thuật ngữ, catchphrase. **Claude không tự chọn khung tự do — hỏi người dùng chọn khung mặc định hay tự do ở bước "Chọn hướng triển khai" (Bước 1.5), sau khi đã có số liệu.** Ở `script.md` với khung tự do, ghi ranh giới theo từng câu hỏi khán giả thay vì theo 6 bước.

## Bước 1.5 — Kỹ thuật viết

**Nguyên tắc bắt buộc:**
1. **Hook mở bằng số liệu/nghịch lý cụ thể**, không mở bằng câu hỏi tự soi hay lời chào dài dòng. 3 mẫu hook ở `docs/Channel-DNA-goc.md` mục 2 chỉ là kho tham khảo — **hỏi người dùng mỗi lần viết hook**: dùng 1 mẫu có sẵn hay tự viết câu mở mới cho tập này.
   - **Nối với tập trước ngay đầu video (nguyên tắc cốt lõi, người dùng chốt 21/09/2026 ở Tập 9 — chọn linh hoạt, KHÔNG dùng thành công thức cố định):** mở bằng 1-2 câu NGẮN (~5 giây) nhắc lại tập trước qua 1 con số/ý chính rồi chuyển sang tập này bằng độ tương phản hoặc điểm chung (VD Tập 9: "Tập trước tôi mổ xiên cá viên chiên, lãi gộp gần 75 phần trăm. Hôm nay đổi món."). Cách nối đổi theo từng cặp tập, không lặp cùng một mẫu câu; chỉ dùng số liệu có thật trong voice-script tập trước; không nói "tuần trước/hôm qua" khi chưa chắc ngày đăng; câu nối phải đứng trước hook nhưng ngắn để số liệu/nghịch lý của Pha 1 vẫn vào trong ~10 giây đầu, không làm loãng hook. Tập đầu tiên hoặc tập không có mối liên hệ tự nhiên thì bỏ, không gượng ép.
   - **Cấu trúc 3 pha bắt buộc trong 30 giây đầu (thứ tự không đổi, nội dung mỗi pha chọn linh hoạt theo tập)** — dựa trên nghiên cứu retention YouTube: script nêu rõ giá trị cụ thể trong 15 giây đầu giữ chân trung bình 52% người xem, so với 44% nếu không nêu rõ:
     - **Pha 1 — Pattern interrupt (0-5s)**: số liệu/nghịch lý gây bất ngờ ngay câu đầu.
     - **Pha 2 — Payoff cụ thể (5-15s)**: nói thẳng kiến thức/con số cụ thể người xem sẽ nắm được sau khi xem hết — càng cụ thể càng tốt (VD "sẽ chỉ đúng khoản chi ẩn ăn hết X triệu lãi mỗi tháng"), KHÔNG mập mờ kiểu "video này có điều bất ngờ".
     - **Pha 3 — Commitment hook (15-30s)**: hé 1 chi tiết cụ thể sẽ giải đáp ở giữa/cuối video, tạo lý do ở lại xem hết.
   - **Ưu tiên giá trị/kiến thức thực chất hơn tò mò rỗng (mystery box)** — kênh nhắm tệp khán giả muốn tìm hiểu/học kiến thức kinh doanh thật (xem tệp khán giả ở memory), không phải tệp click ăn may vì tò mò thuần. Tò mò gap (kiểu "tí nữa tôi sẽ chỉ...") chỉ nên dùng làm gia vị giữa video để chống rớt đoạn giữa, không phải trụ cột mở đầu.
2. **Câu ngắn 10-20 từ là chủ đạo, không quá 25 từ** (theo `docs/Style-Guide-goc.md` mục 2) — nhịp câu ngắn-dài xen kẽ, câu dài hơn khi giải thích cơ chế, câu cực ngắn khi chốt ý.
3. **Mỗi thuật ngữ tài chính phải giải thích ngay lập tức** bằng ví von đời thường (xem benchmark ở `docs/Style-Guide-goc.md` mục 4) — không để thuật ngữ trôi qua mà không giải thích.
4. **Giữ giọng "tôi thấy vậy, anh em thấy sao"** — không áp đặt kiểu chuyên gia biết tuốt, đối chiếu `docs/Style-Guide-goc.md` mục 1-2.
5. **Không đưa lời khuyên đầu tư trực tiếp** — chỉ phân tích/bóc tách, không nói "nên làm"/"nên vay"/"nên đầu tư".
5.5. **Nêu tên nguồn ngay trong lời thoại CHỈ BẮT BUỘC với nội dung liên quan pháp luật/chính sách nhà nước** (thuế, nghị định/thông tư, mức phạt, số liệu xử phạt, thống kê nhà nước như Cục Thống kê/Tổng cục Thống kê...) — VD "theo Nghị định số 141 năm 2026 của Chính phủ" (xem `docs/DNA.md` mục 4, cập nhật theo yêu cầu người dùng 21/09/2026). **Các số liệu còn lại** (doanh nghiệp, thị trường, giá cả, ca kinh doanh...) đã `WebFetch` từ trang uy tín được kể lại bằng góc nhìn của kênh, KHÔNG đọc tên báo trong lời thoại (tránh "theo báo X, báo Y nêu…" dồn dập) — nhưng phải đủ 6 điều kiện minh bạch ở `docs/DNA.md` mục 4 (đặc biệt: disclaimer nói tổng hợp từ nhiều nguồn, nguồn từng số nằm ở phần mô tả video, số tự tính gắn "tôi tính/giả định của tôi", số cũ nêu mốc năm, số nước ngoài nói rõ, ca thật ẩn danh, không bịa trải nghiệm trực tiếp của kênh). Số đã tự ước tính cá nhân (VD tự tính giá vốn từ giá chợ) đóng khung "ước tính cá nhân", không cần gắn tên nguồn.
6. **Dùng đúng 2 câu cố định nguyên văn**: disclaimer (Bước 2) và câu nối "Giờ mới đến khúc xương khó nhằn đây..." (Bước 5) — không diễn đạt lại theo ý riêng.

**Kho kỹ thuật kể chuyện bổ trợ (chọn linh hoạt, KHÔNG phải công thức cố định):**
Đây là các "đạo cụ" có thể dùng để tăng chiều sâu/sức hút cho 1 tập, không phải checklist phải nhét đủ vào mọi video theo đúng 1 vị trí. Mỗi tập tự cân nhắc dùng cái nào, dùng bao nhiêu, đặt ở đâu — **tránh dùng lặp lại y hệt combo/vị trí như tập ngay trước đó**, để các tập không nghe rập khuôn. **Trước khi viết, đọc thêm kho kỹ thuật mở rộng ở `docs/ky-thuat-ke-chuyen-doi-thu.md`** (đúc kết từ script đối thủ — kỹ thuật/cách diễn đạt, không copy nội dung/case study/số liệu của họ, xem mục 9.5 ở trên):
- **Giai thoại mở bài**: hook có thể qua 1 tình huống cá nhân ngắn (kiểu "Tôi có ông anh họ...") thay vì luôn đi thẳng số liệu.
- **Số liệu theo mốc năm**: ưu tiên khi tìm được số liệu quy mô thị trường có mốc năm cụ thể (VD "2019 có X, 2020 còn Y") thay vì chỉ 1 khoảng số tĩnh.
- **Thuật ngữ trung tâm quay lại nhiều lần**: nếu tập có 1 thuật ngữ tài chính then chốt, có thể minh hoạ lại bằng ví dụ số ở nhiều đoạn khác nhau thay vì giải thích 1 lần rồi bỏ.
- **Case study thật**: nếu tìm được 1 doanh nghiệp thật có số liệu công khai minh hoạ đúng nghịch lý chính, có thể kể lại. Nêu đích danh được nếu mọi số liệu/sự kiện đã WebFetch xác nhận nguồn báo chí gốc (`docs/DNA.md` mục 4) — chỉ thuật đúng sự kiện, không suy diễn/phán xét thêm ngoài những gì báo đã đăng. Nếu số liệu chưa kiểm chứng chắc chắn được, ẩn danh triệt để (không tên thương hiệu, không chi tiết định danh được). Không phải tập nào cũng cần có case study.
- **Mid-roll CTA**: 1 câu ngắn mời thích + đăng ký đặt tự nhiên ở giữa video, hợp với video dài/nhiều lớp phân tích — không bắt buộc, và nếu dùng thì đổi cách diễn đạt mỗi tập, không lặp câu y hệt.
- **Mở rộng rủi ro pháp lý/xu hướng tương lai**: nếu ngành có góc này đáng chú ý, có thể thêm đoạn riêng trước kết luận — bỏ qua nếu ngành không có gì đáng nói.

**Chọn hướng triển khai (bắt buộc, làm SAU khi đã khai thác đủ số liệu/góc nhìn ở Bước 0.5, trước khi viết script.md — không chọn khung trước rồi mới đi tìm số liệu vừa khung, vì dễ bỏ sót góc/lớp mà chủ đề thực sự có nhưng không hợp khung chọn sẵn):**
Tra bảng "Đã dùng" ở `docs/da-dung-de-tai.md` (các cột Khung kể/Loại hook/Case study/Mid-roll/Dạng câu kết/Formula tiêu đề) của vài tập gần nhất, rồi chọn tổ hợp cho tập này theo đúng thứ tự ưu tiên sau (không đảo thứ tự):
1. **Phù hợp chủ đề** — lọc bỏ trước các lựa chọn không hợp bản chất tập này (VD chủ đề nghiêm túc thì loại giai thoại đùa cợt; ngành không có case study công khai thì loại case study).
2. **Hiệu quả/thú vị** — trong các lựa chọn còn phù hợp, chọn cái khai thác nghịch lý/số liệu của chủ đề này hay nhất, cho script hấp dẫn nhất.
3. **Không dễ đoán/không rõ trùng lặp** — chỉ dùng khi cân nhắc thêm: nếu tổ hợp cuối cùng nhìn tổng thể giống hẳn 1 tập gần đây, chủ động đổi phần diễn đạt cụ thể (ví von, cách mở, ví dụ minh hoạ) dù giữ nguyên khung/kỹ thuật.

Không ép né hoàn toàn kỹ thuật đã dùng — ưu tiên 1-2 luôn đứng trên việc "phải mới".

## Bước 2 — Áp dụng công thức tiêu đề
Bắt buộc đạt đủ 3 yếu tố ở `docs/cach-lam-chuan.md` mục 10 (từ khoá, gây tò mò, đúng nội dung thật). 3 Formula (A/B/C) ở `docs/Channel-DNA-goc.md` mục 1 là kho mẫu có sẵn, không bắt buộc — **hỏi người dùng mỗi lần tới bước này**: dùng 1 trong 3 Formula có sẵn, hay tự viết cấu trúc tiêu đề mới cho tập này (để tránh nhiều tập liền dùng đúng 1 khuôn nghe rập khuôn).

## Bước 3 — Viết script
1. Viết `Bai-Dang/Tap N - [tên]/script.md`: dàn ý theo bảng ở Bước 1, đánh dấu ranh giới từng bước bằng heading rõ ràng.
2. Viết `voice-script.md`: bản chính tả đầy đủ, câu văn tự nhiên khi đọc thành tiếng, đúng văn phong Gấu (xem `docs/Style-Guide-goc.md` mục 3 — Voice Rules Block, có thể dùng trực tiếp làm system prompt nếu cần).
3. Cắt bỏ mọi chi tiết không phục vụ trực tiếp mạch bóc tách chi phí hoặc câu hỏi người xem đang tò mò.

## Bước 3.5 — Tự kiểm tra dấu hiệu "AI hoá"
Rà lại toàn bộ `voice-script.md`: câu có đều đều máy móc không, có liệt kê đối xứng sáo rỗng không, có dùng cụm từ cấm ở `docs/DNA.md` mục 7 không, có câu nào quá 25 từ không. Sửa lại trước khi đưa người dùng đọc.

**Đối chiếu chéo với tập trước (bắt buộc):** tra `docs/cum-tu-da-dung.md` — nếu cụm nối câu hoặc ví von của tập này trùng/gần giống tập gần đây, đổi cách diễn đạt. Ví von nên bám sát ngành nghề đang phân tích, không dùng lại ví von chung chung của tập khác. Sau khi chốt, ghi lại cụm nối câu + ví von chính đã dùng vào sổ tay này.

**Quy tắc cứng — `voice-script.md` phải THUẦN TIẾNG VIỆT, KHÔNG NGOẠI LỆ (đã siết lại theo yêu cầu người dùng ở Tập 8 — bỏ hẳn các ngoại lệ "từ phổ biến"/"acronym test ổn" từng cho phép trước đây):** mọi từ/cụm tiếng Anh, mọi chữ viết tắt/acronym, mọi tên thương hiệu gốc nước ngoài xuất hiện trong `voice-script.md` đều phải chuyển sang tiếng Việt hoặc phiên âm tiếng Việt — không có trường hợp nào được giữ nguyên dạng gốc chỉ vì "quen thuộc"/"phổ biến"/"đã test đọc ổn". Áp dụng cho MỌI loại: từ vay mượn thông dụng, acronym ngành, tên thương hiệu/tổ chức, tên phần mềm...
- **Ưu tiên 1 — GIỮ NGUYÊN từ vay mượn (không dịch nghĩa sang từ khác), chỉ đổi CÁCH VIẾT sang âm đọc tiếng Việt mà TTS phát âm đúng** — đây là cách xử lý mặc định cho mọi từ vay mượn đã quen thuộc trong khẩu ngữ hàng ngày (VD "gas" → "ga", "nilon" → "ni lông", "online" → "on lai", "offline" → "ốp lai"). KHÔNG thay bằng 1 từ tiếng Việt có nghĩa khác dù gần đúng (VD KHÔNG dịch "online" thành "qua mạng" — người Việt ngoài đời vẫn nói "bán online" chứ không nói "bán qua mạng", chỉ cần viết lại đúng âm đọc).
- **Ưu tiên 2 — nếu từ đó không thực sự tồn tại trong khẩu ngữ hàng ngày** (tên thương hiệu, acronym ngành, thuật ngữ chuyên môn ít ai nói miệng...), lúc này mới cân nhắc dùng hẳn 1 cụm tiếng Việt thay thế có nghĩa tương đương (VD "fan" → "người mê"), hoặc phiên âm theo cách đọc từng chữ cái bằng chữ tiếng Việt (VD "F&B" → "Ép En Bi"; "SOP" → "Ét Ô Pi"; "KPI" → "Ca Pi Ai") hoặc theo cách đọc tên riêng phổ biến ngoài đời (xem mục "Cách chốt phiên âm" bên dưới).
- **Ưu tiên 3 — nếu 1 acronym/thuật ngữ không thực sự cần thiết phải nhắc bằng tên viết tắt** (VD "COGS" — bản chất chỉ cần nói "giá vốn hàng bán" là đủ, nhắc thêm tên viết tắt tiếng Anh không tăng giá trị cho khán giả phổ thông), cân nhắc **bỏ hẳn acronym đó**, chỉ dùng cụm tiếng Việt giải thích, thay vì cố phiên âm cho có.
- **KHÔNG có ngoại lệ, kể cả câu cố định**: quy tắc thuần Việt hoá cách viết áp dụng cho MỌI câu trong `voice-script.md`, kể cả disclaimer/câu nối/catchphrase kết cố định ở `docs/DNA.md` mục 5 — lỗi thật đã xảy ra ở Tập 8: catchphrase gốc "Hẹn anh em video sau" đã được sửa thành "Hẹn anh em vi-đê-ô sau" và cập nhật lại nguyên văn cố định ở `docs/DNA.md` mục 5, áp dụng cho mọi tập từ giờ.

**Quy tắc cứng — phân biệt phiên âm cho lời thoại vs chữ hiển thị trên ảnh (lỗi thật đã xảy ra ở Tập 7):** phiên âm (VD "6G" → "sáu Gờ") CHỈ áp dụng cho `voice-script.md` (lời đọc TTS). Khi ký hiệu/acronym đó xuất hiện dưới dạng **chữ hiển thị trong ảnh** (biển hiệu, chứng chỉ, giấy tờ... viết trong `QuyTrinh/C3-Prompt-Anh.md`/`prompt-anh.txt`), phải giữ nguyên ký hiệu gốc (VD vẫn viết "6G", không viết "SÁU GỜ") — vì đây là chữ để mắt đọc, không phải để AI voice phát âm. Đã xảy ra lỗi thật: dán nhầm "SÁU GỜ" lên chứng chỉ trong ảnh scene ở Tập 7.

**Quy tắc cứng — viết đầy đủ, không viết tắt địa danh/tên riêng trong `voice-script.md` (lỗi thật đã xảy ra ở Tập 8, đã sửa 2 lần)**: chữ viết tắt có dấu chấm ở giữa (VD "TP.HCM") khiến TTS hiểu nhầm dấu chấm là kết thúc câu, ngắt/tách rời phần sau sang câu kế tiếp gượng gạo (thử bỏ dấu chấm thành "TP HCM" vẫn chưa triệt để — cách đúng nhất là viết đầy đủ). Mặc định viết đầy đủ mọi viết tắt địa danh/tên riêng trong `voice-script.md` (VD "TP.HCM" → "thành phố Hồ Chí Minh"), không áp dụng cho `script.md` (giữ nguyên viết tắt chuẩn để tra cứu).

**Quy tắc mở rộng — mọi tên riêng/thương hiệu KHÔNG thuần tiếng Việt đều phải phiên âm, không chỉ acronym có ký hiệu:** bất kỳ tên thương hiệu/tên riêng gốc nước ngoài nào xuất hiện trong `voice-script.md` (tên công ty, tên chuỗi, tên người nước ngoài...) đều mặc định viết lại theo cách đọc gần đúng bằng chữ tiếng Việt, trừ khi đó là 1 từ tiếng Anh phổ biến đã Việt hoá quen thuộc trong lời nói hàng ngày (VD "marketing", "app", "online"). `script.md` vẫn giữ nguyên tên gốc để tra cứu nguồn, chỉ `voice-script.md` mới phiên âm.

**Cách chốt phiên âm (bắt buộc theo đúng thứ tự ưu tiên sau, không tự đoán bừa theo cách đọc chữ cái tiếng Anh):**
1. Ưu tiên tra xem **người Việt ngoài đời thực tế đang gọi tên đó như thế nào** (cách phát âm quen thuộc, phổ biến trên báo chí/mạng xã hội/đời sống) — dùng WebSearch để tìm, và WebFetch bài gốc nếu cần xác nhận cách viết/đọc cụ thể, không đoán theo trực giác cá nhân.
2. Nếu không tra được cách đọc phổ biến ngoài đời (công cụ lỗi, không có nguồn rõ ràng), hỏi thẳng người dùng cách họ quen nghe/đọc tên đó, thay vì tự bịa phiên âm.
3. Chỉ khi cả 2 cách trên đều không có, mới tạm dùng phiên âm ước lượng theo cách đọc chữ cái tiếng Anh như phương án cuối, và ghi rõ trong sổ tay là "ước lượng, chưa xác nhận" để ưu tiên kiểm tra lại sau.

**Sổ tay phiên âm tên thương hiệu/tên riêng đã dùng (áp dụng mọi tập sau, chỉ sửa trong `voice-script.md`, giữ nguyên tên gốc ở `script.md`):**
- "Circle K" → "Xơ Cồ Cây"
- "GS25" → "Gờ Ét Hai Lăm" (đã người dùng nghe/xác nhận chỉnh từ "Gi Ét Hai Lăm")
- "FamilyMart" → "Pha Mi Li Mắc" (đã người dùng nghe/xác nhận chỉnh từ "Phe Mơ Li Mát")
- "7-Eleven" → "Xê Vần I Lê Vần" (chưa được người dùng xác nhận qua voice.mp3 thật, có thể còn phải chỉnh)
- "6G" (tư thế hàn) → "sáu Gờ" (chưa được người dùng xác nhận qua voice.mp3 thật, có thể còn phải chỉnh)
- "buffet" → "búp phê" (**người dùng xác nhận 21/09/2026**; KHÔNG viết "bu phê")
- "yen" (tiền Nhật) → "yên" (Tập 9, chưa nghe voice.mp3 xác nhận)
- Tập 9 chủ động KHÔNG nêu tên tập đoàn/chuỗi/thương hiệu nước ngoài và không đọc tên báo trong lời thoại (dùng "một tập đoàn nhà hàng lẩu nướng", "một chuỗi lẩu búp phê lớn") để tránh phải phiên âm; tên gốc chỉ ở `so-lieu-xac-nhan.md`.
- Các dòng chưa ghi chú "đã người dùng xác nhận" là phiên âm ước lượng gần đúng — nếu nghe voice.mp3 thật thấy đọc vẫn sai/gượng, chỉnh lại và cập nhật vào đúng danh sách này (không tạo file riêng, tránh chồng chéo với sổ tay khác).

## Bước 4 — Checklist an toàn nội dung (BẮT BUỘC trước khi qua bước tiếp theo)
Đối chiếu với `docs/DNA.md` mục 4:
- [ ] Không tư vấn đầu tư cụ thể (không nói mua cổ phiếu/coin/mã nào, không nói "nên vay"/"nên đầu tư").
- [ ] Nếu có nêu đích danh doanh nghiệp, mọi số liệu/sự kiện gắn kèm đã WebFetch xác nhận nguồn báo chí gốc, không suy diễn/phán xét thêm ngoài sự kiện đã công bố (`docs/DNA.md` mục 4). Nếu số liệu chưa kiểm chứng chắc chắn được, đã ẩn danh triệt để theo kho kỹ thuật bổ trợ ở Bước 1.5. Không nêu đích danh cá nhân cụ thể kèm phán xét tiêu cực.
- [ ] Số liệu dùng có căn cứ hợp lý, đóng khung "ước tính/tổng hợp cá nhân" (không bịa số chính xác tuyệt đối).
- [ ] Nội dung liên quan pháp luật/chính sách (thuế, nghị định, mức phạt, thống kê nhà nước) đã nêu tên nguồn trong lời thoại; số liệu khác không nêu tên báo thì đã thoả 6 điều kiện minh bạch ở `docs/DNA.md` mục 4 (kể cả không bịa trải nghiệm trực tiếp của kênh).
- [ ] Có đủ disclaimer cố định và catchphrase kết cố định, đúng nguyên văn.
- [ ] **Người dùng đã tự đọc lại toàn bộ `script.md`/`voice-script.md` và có ít nhất 1 chỗ chỉnh sửa/góp ý tay thực chất** — nếu không có gì cần sửa, người dùng xác nhận rõ bằng lời trước khi qua bước tiếp theo.
- [ ] Không dùng cụm từ cấm (xem `docs/DNA.md` mục 7).

## Bước 5 — Ước lượng & đề xuất bổ trợ
1. Ước lượng thời lượng đọc — đo tốc độ TTS thật sau khi có `voice.mp3`, cập nhật vào đây để dùng cho các tập sau. **Tốc độ đo từ Tập 8:** khoảng 17,5 ký tự/giây tính cả khoảng trắng (9.375 ký tự ↔ 8 phút 56 giây; ≈ 13,5 ký tự/giây không tính khoảng trắng) → mốc 8 phút 30 giây ≈ 8.900 ký tự; đếm bằng Python `len()`, không dùng `wc -c`. Tập 9 sẽ đo lại khi có `voice.mp3`. Mốc thời lượng tối thiểu bắt buộc + cách đếm ký tự đúng chuẩn: xem `docs/DNA.md` mục 1 — nếu ước lượng chưa đạt mốc, quay lại đào sâu nội dung trước khi qua bước tiếp theo.
2. Đánh dấu 1-2 đoạn cao trào/hook mạnh nhất (thường là đoạn tính điểm hoà vốn) — gợi ý điểm cắt Shorts (30-60s).
3. Đề xuất 3-5 phương án tiêu đề (dùng cả 3 Formula nếu hợp) + concept thumbnail đi kèm (tham khảo Thumbnail Text Bank ở `docs/Style-Guide-goc.md` mục 6).

## Bước 6 — Cập nhật kho đề tài
Sau khi chốt script, thêm 1 dòng vào bảng "Đã dùng" trong `docs/da-dung-de-tai.md`, ghi rõ số tập **và đủ các cột Khung kể/Loại hook/Case study/Mid-roll/Dạng câu kết/Formula tiêu đề** đã chọn ở Bước 1.5, xoá dòng tương ứng khỏi bảng "Kho ý tưởng chờ sản xuất".

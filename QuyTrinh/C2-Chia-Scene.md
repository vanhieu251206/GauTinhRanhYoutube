# C2 — Chia Scene

> Đầu vào là **nội dung `script.md`/`voice-script.txt` từ C1** — KHÔNG phụ thuộc bước TTS thủ công (`voice.mp3`/`sub.srt`) đứng sau. Chia scene làm trực tiếp từ text, không cần đợi voice xuất xong.
> Đầu ra: `scene-list.md` trong `Bai-Dang/Tap N - [tên]/` — danh sách scene đầy đủ, dùng làm căn cứ trực tiếp cho C3 (viết prompt ảnh) và C5 (khớp timing thật khi đã có `sub.srt`).

## Nguyên tắc cốt lõi — Chia theo Ý NGỮ NGHĨA (Semantic Beat), KHÔNG chia theo giây

> **Đã đổi cách làm (bài học từ lỗi thật):** cách cũ tính `số ảnh = thời lượng đoạn / nhịp giây cố định` — sai gốc, vì ép số ảnh theo THỜI LƯỢNG thay vì theo NỘI DUNG thật có. Hậu quả: nhiều đoạn bị dư ảnh so với số ý thật, buộc phải "độn" bằng cách lặp lại cùng 1 ý dưới góc quay khác (VD nhiều ảnh liên tiếp chỉ cận màn hình điện thoại) — nhìn tổng thể thấy lặp/nhàm dù đã đổi góc.
>
> Theo đúng lý thuyết dựng phim/biên kịch chuẩn (khái niệm **Beatscript** — phân tách rõ lớp "ý nghĩa" và lớp "hình ảnh thực thi"): quan hệ giữa 1 beat (ý) và 1 shot (khung hình) KHÔNG cố định 1:1 — có lúc 1 ý quan trọng cần 1 ảnh riêng, có lúc cả 1 chuỗi ý nhỏ chỉ cần 1 ảnh biểu đạt. Số ảnh phải suy ra từ **số ý/chủ thể/hành động thực sự khác nhau có trong đoạn**, không phải chia đều theo thời lượng.

## Cách làm
1. Đọc `voice-script.txt` theo đúng khung các bước đã đánh dấu trong `script.md` (C1 Bước 1).
2. Trong mỗi bước, đọc kỹ từng câu, xác định **số ý/chủ thể/hành động thực sự khác nhau** — mỗi khi có 1 trong các dấu hiệu sau, tính là 1 ý mới cần 1 scene riêng:
   - Chủ thể/đối tượng đang nói tới đổi (từ "cuộc gọi" sang "tin nhắn", từ "sếp" sang "người thân"...).
   - Có ví dụ cụ thể mới (mỗi ví dụ trong 1 chuỗi ví dụ = 1 scene riêng, không gộp).
   - Có 1 bằng chứng/nghiên cứu/dẫn chứng cụ thể mới, hoặc twist/lật nhận thức — luôn tách riêng 1 scene vì là điểm nhấn.
   - Từ chuyển ý ("nhưng", "tuy nhiên", "điều thú vị là", "ít ai biết"...) — thường mở ra ý mới, cắt scene tại đó.
   - Liệt kê có đánh số ("một, hai, ba...", "4 việc nhỏ...") — mỗi mục 1 scene.
   - Cảm xúc/trạng thái nhân vật đổi rõ rệt dù chưa đổi chủ thể (từ lo lắng sang nhẹ nhõm).
3. Các câu chỉ diễn giải/bổ sung thêm cho CÙNG 1 ý vừa nêu (không có gì mới để vẽ) → gộp chung 1 scene với câu trước, KHÔNG tách thêm.
4. Nếu 1 ý duy nhất trải dài (nhiều câu/nhiều giây ước tính) nhưng không có gì mới để vẽ thêm — **giữ nguyên 1 scene đó** (chấp nhận scene dài hơi hơn mức lý tưởng), KHÔNG sinh thêm scene giả để "đủ nhịp". Thà 1 scene dài hơi còn hơn nhiều scene lặp ý.
5. Mỗi cụm scene liên tiếp thuộc cùng 1 bước (7 bước) nên giữ 1 bối cảnh/setup nền tảng nhất quán (địa điểm, đạo cụ) trừ khi nội dung đổi hẳn sang tình huống khác — nhưng SỐ SCENE do bước 2-4 quyết định, không phải công thức chia giây.
6. Tổng số scene toàn video sẽ dao động tự nhiên tuỳ mật độ ý thật của script — không ép về 1 con số mục tiêu cố định trước.

**Lưu ý khi 1 đoạn văn gốc chứa nhiều ý khác nhau cần tách thành nhiều scene con** (VD 1 đoạn chứa cả "né tránh" và "kiểm tra liên tục"): chia đúng theo ranh giới ý thật (đối chiếu text trực tiếp), không suy luận theo số thứ tự — đây là lỗi dễ xảy ra nhất khi 1 scene không tương ứng 1:1 với 1 đoạn văn gốc, từng gây lệch toàn bộ chỉ số các scene phía sau.

**Lỗi thật đã xảy ra ở tập 2 — sót 1 câu chuyển ý giữa 2 scene**: khi chia scene bằng cách đọc và ước lượng ranh giới ý (không đối chiếu từng câu 1:1 với `voice-script.txt` gốc), rất dễ vô tình nhảy cóc qua 1 câu chuyển ý ngắn nằm giữa 2 đoạn nội dung chính (VD câu "Có một điều cần nói rõ thêm, để không ai hiểu nhầm là..." bị bỏ sót giữa 2 scene khác, khiến câu đó không có scene/ảnh riêng, ảnh của scene trước bị kéo dài bất thường khi khớp timing ở C5). **Cách phòng tránh**: sau khi chia xong, đối chiếu ngược lại — ghép nối "Đoạn voice-script tương ứng" của TẤT CẢ scene theo đúng thứ tự, so với `voice-script.txt` gốc, đảm bảo không có câu/đoạn nào trong bản gốc bị thiếu giữa 2 scene liên tiếp (không chỉ kiểm tra không trùng lặp, mà còn phải kiểm tra không sót).

## Ước lượng thời lượng đọc (chỉ để tham khảo, KHÔNG dùng để tính số scene)
Dùng tốc độ TTS thật đã đo của kênh (xem mốc đã ghi ở `QuyTrinh/C1-Script.md` Bước 5 — nguồn duy nhất, không ghi lại số cụ thể ở đây để tránh lệch khi đo lại) để ước lượng khoảng thời gian mỗi scene chiếm — chỉ mang tính tham khảo cho việc hình dung nhịp video, KHÔNG dùng để ép số lượng scene. Timing chính xác thật sự sẽ được khớp lại bằng `sub.srt` thật ở C5.

## Cột cần điền cho `scene-list.md`
```
| STT | Bước (7 bước) | Đoạn voice-script tương ứng | Bối cảnh/setup | Mô tả ý chính của scene đó |
|---|---|---|---|---|
```
- **STT**: đánh số liên tục từ 001 (3 chữ số, vì có thể >99 scene), đúng thứ tự xuất hiện trong voice-script, không đảo.
- **Bối cảnh/setup**: địa điểm/đạo cụ cố định cho cụm scene liên tiếp cùng bối cảnh (xem `QuyTrinh/C3-Prompt-Anh.md` về nguyên tắc đa dạng bối cảnh giữa các cụm khác nhau).
- **Mô tả ý chính**: tóm tắt ngắn hành động/chủ thể/cảm xúc của scene đó — đây là căn cứ trực tiếp để C3 viết prompt chi tiết, KHÔNG cần viết sẵn prompt ở bước này. Tất cả scene đều là **1 ảnh AI gen thuần tuý trong 1 phong cách nhất quán** (theo `docs/Visual-Prompts-goc.md` mục 2 — bgStyle chỉ khác nhau ở loại nền phẳng minh hoạ hay nền phong-cách-ảnh-thật, không tách lớp/ghép ảnh thật ngoài đời).

## Đầu ra
`scene-list.md` trong `Bai-Dang/Tap N - [tên]/` — đưa người dùng xem lại trước khi qua C3 (viết prompt ảnh).

## Lưu ý
Đây là bước tách riêng khỏi việc viết prompt ảnh (C3) vì mục đích khác nhau: C2 lo đúng nhịp/số lượng scene ăn khớp nội dung, C3 lo dựng khung hình chi tiết cho từng scene đã chốt — làm chung 1 bước dễ sót cảnh hoặc chia scene không đều vì mải tập trung viết prompt.

# C8 — Đăng Bài (Publish)

> Đầu vào: `clip-hoan-chinh.mp4` (ghép trong CapCut từ các clip câm `clips/` đã xuất ở `QuyTrinh/C5-Timing-Xuat-Clip.md` + `voice.mp3` + nhạc nền/hiệu ứng/sub/logo thêm thủ công) + `thumbnail.jpg` (từ `C7-Thumbnail.md`) + phương án tiêu đề đã đề xuất ở C1 Bước 5.
> Đầu ra: video đã đăng trên kênh + `tieu-de-mo-ta.txt` lưu lại tiêu đề + mô tả đã đăng.
> **Không cần kiểm tra sự tồn tại của `clip-hoan-chinh.mp4` trước khi làm C8** — việc ghép/xuất clip là thao tác thủ công của người dùng ngoài phạm vi theo dõi của Claude; khi người dùng báo đã xong, cứ thực hiện C8 trực tiếp trên nội dung (tiêu đề/mô tả/tag), không cần verify file.

## Bước 0 — Nhắc lại thứ tự ưu tiên
Theo `docs/cach-lam-chuan.md` mục 0: Tiêu đề + Thumbnail quan trọng hơn nội dung trong việc quyết định video có được đề xuất hay không.

## Bước 1 — Chốt Tiêu đề
Áp dụng đúng 1 trong 3 Formula (A/B/C) ở `docs/Channel-DNA-goc.md` mục 1, đối chiếu công thức 3 yếu tố ở `docs/cach-lam-chuan.md` mục 10 (từ khoá + gây tò mò + đúng nội dung thật). Kiểm tra không dùng cụm từ cấm ở `docs/DNA.md` mục 7. Có thể đối chiếu thêm công thức tiêu đề đối thủ đang hiệu quả ở `docs/chien-luoc-youtube.md` mục Benchmark để tham khảo cấu trúc (không copy nguyên văn khuôn câu).

## Bước 2 — Viết mô tả & tag video
Ghi vào `tieu-de-mo-ta.txt`: tiêu đề, mô tả ngắn, timestamp theo từng bước nội dung (theo khung ở `docs/DNA.md` mục 3), disclaimer + disclosure dùng AI (dùng đúng 2 câu cố định ở `docs/DNA.md` mục 5), hashtag, từ khoá.

**Nguyên tắc riêng của kênh — đoạn mô tả KHÔNG được kể lại/tóm tắt toàn bộ nội dung video**, chỉ 2-3 câu ngắn, giọng tinh ranh/mỉa mai nhẹ đúng tinh thần Gấu (`docs/DNA.md` mục 6).

**Quy tắc cứng — mô tả KHÔNG tiết lộ nội dung chính/đáp án của video** (người dùng chốt 24/09/2026, Tập 10): đọc mô tả mà biết trước đáp án thì mất lý do bấm xem. Câu mở, các đoạn mô tả và mục lục timestamp **chỉ đặt câu hỏi/nghịch lý, gợi tò mò** — không nêu cơ chế giải thích, kết luận hay ẩn dụ chốt của tập. VD Tập 10 (đáp án: tiệm sống nhờ bảng giá 5 gói, "30K chỉ là cái cửa"): bỏ câu "bí mật là cái bảng giá 5 gói, 30K chỉ là cái cửa" → thay bằng "trừ tiền nước, điện, xà bông thì còn lại bao nhiêu — mà tiệm vẫn mở đều?"; chương "Chốt lại: 30K chỉ là cái cửa" → "Vậy rốt cuộc tiệm lời ở đâu?". Tự rà trước khi giao: xoá hết mọi câu trả lời được câu hỏi ở tiêu đề/thumbnail. **Mỗi câu/ý tách thành 1 đoạn riêng (xuống dòng trống giữa các câu)** — không viết dồn 2-3 câu liền thành 1 khối đặc, để dễ đọc lướt trên YouTube.

**Quy tắc cứng — câu MỞ ĐẦU mô tả phải viết như 1 cái hook, không phải câu tường thuật thường**: YouTube chỉ hiện khoảng 1-2 dòng đầu của mô tả (~100 ký tự) trước khi bị gập lại sau nút "Xem thêm" — đoạn hiện ra ngay trước mắt này đóng vai trò như hook thứ 2 của video (song song với hook mở đầu trong voice), ảnh hưởng tới việc người xem có bấm vào xem tiếp/đọc mô tả hay không, đặc biệt khi mô tả xuất hiện trong kết quả tìm kiếm. Vì vậy câu đầu tiên của mô tả (đoạn đầu, trước khi tách đoạn) phải chứa đúng nghịch lý/số liệu gây tò mò chính của tập, ở dạng câu hỏi chưa có lời giải (không kèm đáp án — xem quy tắc ngay trên) — giống hệt tinh thần viết hook ở `docs/Channel-DNA-goc.md` mục 2 — không mở đầu bằng câu thoại chung chung/lời chào/câu dẫn nhập rườm rà.

**Danh sách nguồn số liệu trong MÔ TẢ (bắt buộc từ Tập 9, theo `docs/DNA.md` mục 4-5):** vì lời thoại không đọc tên báo cho số liệu doanh nghiệp/thị trường, phần mô tả phải có khối riêng "📎 NGUỒN SỐ LIỆU" (đặt sau mục lục timestamp, trước disclosure AI/hashtag) liệt kê từng nguồn: tên báo/văn bản + link + ngày đăng, lấy từ `so-lieu-xac-nhan.md`; ghi rõ số nào là "tự tính". Khối này chỉ liệt kê số + nguồn, **không viết câu diễn giải kết luận** (VD không viết "tiền nằm ở gói cao") — giữ đúng quy tắc không tiết lộ ở trên. **Dòng "Số TỰ TÍNH / GIẢ ĐỊNH" chỉ ghi gọn 1 câu nêu NHÓM số nào là tự tính** (VD Tập 10: "thời gian rửa và vật tư từng gói, chi phí cố định mỗi tháng, điểm hoà vốn và các kịch bản ngày đông/ngày vắng") — KHÔNG liệt kê chi tiết từng con số/phép tính (người dùng chốt 24/09/2026: dài dòng, lộ nội dung; con số cụ thể đã có trong video). Chỉ liệt kê nguồn đã dùng trong `voice-script.md` (không liệt kê số đã loại). Khối này là nội dung copy thẳng khi đăng, không phải note giải thích.

**Format file `tieu-de-mo-ta.txt`: CHỈ chứa nội dung chính thức để copy thẳng khi đăng video** (Tiêu đề / Mô tả / Tag) — KHÔNG viết note giải thích lý do chọn, KHÔNG liệt kê phương án dự phòng, KHÔNG ghi chú lịch đăng hay hướng dẫn bên trong file này. Phần phân tích/lý do (nếu cần trình bày với người dùng) chỉ nói trong hội thoại, không lưu vào file. Mỗi mục (TIÊU ĐỀ / MÔ TẢ / TAG) đánh dấu bằng `###` ở đầu dòng để phân biệt rõ với nội dung copy được, VD:
```
### TIÊU ĐỀ
...
### MÔ TẢ
...
### TAG
...
```

**Mục lục timestamp trong MÔ TẢ**: có tiêu đề riêng "⏱️ NỘI DUNG" ngay trên danh sách mốc thời gian. Gộp các mốc nhỏ liền kề cùng 1 ý lớn thành 1 dòng — chỉ nên còn khoảng **6-8 mốc** cho cả video (Hook, Bối cảnh ngành, Bóc tách chi phí, Điểm hoà vốn, Kết luận...). Mỗi dòng rút gọn tối đa (vài từ khoá, không viết cả câu dài). **KHÔNG đưa mốc CTA (thích/chia sẻ/đăng ký) vào mục lục**.
- **Lấy mốc từ `sub-final.srt`** (C6): mốc mỗi chương = thời điểm câu mở đầu đúng ý đó trong voice.
- **Điều kiện để YouTube tự tạo chương (cứng)**: mốc đầu là `00:00`, ít nhất 3 mốc, mỗi chương dài ≥ 10 giây, mốc tăng dần.
- **Cách viết tên chương (cốt lõi, tối ưu theo Tập 10)**: viết theo câu người xem hay gõ tìm kiếm, dạng câu hỏi (VD "Rửa 1 xe máy lời bao nhiêu?", "Mở tiệm rửa xe máy cần bao nhiêu vốn?", "Rửa mấy xe mỗi ngày mới hoà vốn?") — tên chương có thể hiện trong kết quả tìm kiếm; tránh thuật ngữ người xem chưa biết (VD "giờ công") ở tên chương, thay bằng ý nghĩ đời thường gây tò mò ("Rửa 100 xe một ngày được không?"); mỗi dòng ≤ ~40 ký tự để không bị cắt trên điện thoại; không nêu đáp án (quy tắc không tiết lộ ở trên).

## Bước 3 — Checklist trước khi bấm đăng (bắt buộc)
- [ ] Đối chiếu lần cuối với khung an toàn nội dung `docs/DNA.md` mục 4.
- [ ] Kiểm tra không trùng đề tài trong `docs/da-dung-de-tai.md`.
- [ ] Nếu là video đầu tiên: áp dụng lịch "làm nóng" ở `docs/cach-lam-chuan.md` mục 9.
- [ ] KHÔNG xoá và đăng lại nếu video cũ chưa đạt kỳ vọng.
- [ ] **Rủi ro chính sách "Inauthentic content" (YouTube 2026)** — kênh dùng ảnh AI tĩnh + giọng TTS nên thuộc nhóm dễ bị soi nhất. Trước khi đăng, xác nhận đã qua đủ các lớp "dấu ấn sản xuất riêng" đã làm: giọng đọc đã được nghe/chỉnh lại (`docs/cach-lam-chuan.md` mục 5), ảnh đã áp dụng đúng quy tắc chống lặp bối cảnh/góc quay (`QuyTrinh/C3-Prompt-Anh.md`). Kiểm tra trong YouTube Studio xem tài khoản có được yêu cầu gắn nhãn "Nội dung bị thay đổi hoặc tổng hợp" (Altered or synthetic content) không — nếu có, bật đúng nhãn trước khi đăng.
- [ ] Video có đủ disclaimer và catchphrase kết cố định (`docs/DNA.md` mục 5), không tư vấn đầu tư trực tiếp.
- [ ] Mô tả (`tieu-de-mo-ta.txt`) có câu disclosure dùng AI cố định (`docs/DNA.md` mục 5) — không được bỏ.
- [ ] Mô tả có khối "📎 NGUỒN SỐ LIỆU" (link + ngày đăng từng nguồn đã dùng, số tự tính ghi rõ) nếu lời thoại không nêu tên báo cho số liệu doanh nghiệp/thị trường (`docs/DNA.md` mục 4).

## Bước 4 — Đăng & theo dõi
Đăng video, lưu tiêu đề/mô tả đã đăng. Hẹn người dùng quay lại sau 24-48h để chạy `QuyTrinh-Chien-Luoc/S1-Theo-Doi-Hieu-Qua.md` (ghi CTR/AVD/retention) — xem Bước 7 dưới đây.

## Bước 5 — Cắt Shorts (nếu có)
Dùng điểm cắt đã đánh dấu ở C1 Bước 5.

## Bước 6 — Ghi lại nhật ký (nếu có chỉnh sửa tay đáng kể)
Ghi vào `docs/lich-su-phien.md`: bản gốc → bản sửa → lý do.

## Bước 7 — Check tình trạng kênh, nhắc chạy quy trình chiến lược (BẮT BUỘC, làm cuối cùng)
Sau khi hoàn thành C8 cho tập này, kiểm tra và nhắc người dùng rõ ràng (không tự ý chạy thay nếu người dùng chưa xác nhận):
- **Luôn nhắc S1** — sau 24-48h nữa quay lại chạy `QuyTrinh-Chien-Luoc/S1-Theo-Doi-Hieu-Qua.md` để ghi Impression/CTR/Retention của tập vừa đăng vào `docs/nhat-ky-hieu-qua.md`.
- **Đếm số tập đã có dữ liệu S1** trong `docs/nhat-ky-hieu-qua.md` — nếu đã đạt bội số 5 (5, 10, 15...) hoặc người dùng nói kênh đang chững, nhắc chạy `QuyTrinh-Chien-Luoc/S2-Duc-Ket-Dinh-Ky.md` (đúc kết định kỳ, gồm cả đánh giá theo Pillar ở mục 2.1).
- **Nếu có dấu hiệu bão hoà** (nhiều tập liên tiếp Impression thấp dù đã đổi thumbnail/tiêu đề) hoặc người dùng muốn mở rộng nhánh mới trong ngách, nhắc chạy `QuyTrinh-Chien-Luoc/S3-Danh-Gia-Ngach.md`.
- Nếu chưa đủ dữ liệu để chạy S1/S2/S3 (VD mới đăng, chưa đủ 24h), chỉ cần nói rõ mốc thời gian nào cần quay lại, không cần làm gì thêm ở bước này.

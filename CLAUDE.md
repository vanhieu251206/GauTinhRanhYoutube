# CLAUDE.md — File tổng (Kênh "Gấu Tinh Ranh" — Video ảnh tĩnh)

> File này để Claude đọc đầu tiên mỗi phiên làm việc trong project này.
> Kênh phân tích **mô hình kiếm tiền/lỗ lãi thật của các ngành nghề/dịch vụ đời thường Việt Nam** (quán trà sữa, tiệm rửa xe, phòng gym, tài xế công nghệ...) và các quyết định tài chính cá nhân phổ biến (vay mua nhà, thẻ tín dụng...) — bóc tách COGS, chi phí cố định, điểm hoà vốn, chi phí ẩn. Giọng kể tinh ranh/mỉa mai nhẹ qua nhân vật mascot **Gấu**. Định dạng: **ảnh tĩnh + voice**, không animation, dựng thành video hoàn chỉnh đăng kênh.
> Project này là 1 project độc lập, không dùng chung git/tài nguyên với project khác.
> Chi tiết đầy đủ ở `docs/DNA.md`, `docs/Channel-DNA-goc.md`, `docs/Style-Guide-goc.md`, `docs/Visual-Prompts-goc.md`, `docs/Chu-De-goc.md` (4 file gốc do người dùng chốt).

## 0. BẮT ĐẦU MỖI PHIÊN (làm trước tiên)
Hỏi người dùng muốn làm gì:
1. **Tạo video mới** → đi theo quy trình `QuyTrinh/` (C0-Chọn-Chủ-Đề → C1-Script → C2-Chia-Scene → C3-Prompt-Ảnh → C4-Đổi-tên-Kiểm-tra-Ảnh → C5-Timing-Xuất-Clip → C6-Thumbnail → C7-Đăng-bài). C2 chia scene ngay từ text script, không cần đợi voice xuất xong. Sau C1 (làm song song hoặc sau C2 đều được), người dùng tự dán `voice-script.txt` vào TTS xuất `voice.mp3` + `sub.srt` đi kèm (thủ công, không thuộc quy trình có tài liệu riêng). C5 xuất sẵn clip câm đúng thời lượng từng scene bằng ffmpeg (ảnh tĩnh, cắt cứng giữa các ảnh, KHÔNG dùng hiệu ứng zoom/pan); người dùng chỉ còn ghép `voice.mp3` + nhạc nền + sub + logo thủ công bằng CapCut. Đọc `QuyTrinh/C0-Chon-Chu-De.md` trước tiên.
   - Trước C0, đọc toàn bộ `docs/` (giọng kể, quy ước, cụm từ cấm, kho ý tưởng).
   - Tra `docs/da-dung-de-tai.md` để không lặp ngành nghề/góc kể đã dùng — mỗi tập là 1 ngành nghề/chủ đề tài chính độc lập, các tập đã làm được ghi lại tại đây.
2. **Theo dõi/đúc kết hiệu quả kênh** → đi theo `QuyTrinh-Chien-Luoc/` (S0-Tổng-Quan → S1-Theo-Dõi-Hiệu-Quả / S2-Đúc-Kết-Định-Kỳ / S3-Đánh-Giá-Ngách). Quy trình này **tách biệt** với quy trình sản xuất video ở trên. Đọc `QuyTrinh-Chien-Luoc/S0-Tong-Quan.md` trước tiên.
3. **Việc khác** (chỉnh sửa quy trình, thử nghiệm...).

> Nguyên tắc chung: đi TỪNG BƯỚC, hỏi bước tiếp theo, người dùng đồng ý → làm. Không tự nhảy bước. Sau mỗi video hoàn chỉnh, ghi lại vào `docs/da-dung-de-tai.md`.

## 1. Cấu trúc thư mục
```
GauTinhRanh/
├── CLAUDE.md                   # File tổng (file này)
├── Bai-Dang/                    # ĐẦU RA: mỗi video 1 thư mục con (đánh số theo thứ tự)
│   └── Tap 1 - [ten]/
│       ├── script.md
│       ├── voice-script.txt     # bản chính tả đầy đủ, dán vào TTS
│       ├── voice.mp3            # người dùng tự xuất từ TTS
│       ├── sub.srt              # tải kèm voice.mp3 từ TTS, khớp timing thật — dùng lấy mốc ở C5
│       ├── scene-list.md        # danh sách scene (C2)
│       ├── prompt-anh.txt       # 1 dòng = 1 prompt/scene (C3 Bước 3)
│       ├── Anh Video/            # ảnh 001.jpg...0NN.jpg
│       ├── timing.md            # mốc thời gian mỗi scene (C5)
│       ├── clips/                # clip câm scene-001.mp4...scene-0NN.mp4 (ffmpeg, C5)
│       ├── clip-hoan-chinh.mp4  # ghép trong CapCut (voice + clips + nhạc/hiệu ứng/sub/logo)
│       ├── thumbnail-prompt.txt # prompt gen ảnh nền thumbnail đã chốt, KHÔNG chữ (C6 Bước 3)
│       ├── thumbnail-nen.jpg    # ảnh nền do AI tạo, không chữ, 1280×720px (C6 Bước 5)
│       ├── thumbnail.jpg        # ảnh bìa hoàn chỉnh sau khi chèn chữ thủ công
│       └── tieu-de-mo-ta.txt    # tiêu đề + mô tả + timestamp + hashtag + tag (C7)
├── QuyTrinh/                    # Quy trình sản xuất 1 video (chỉ đọc, không tự ý sửa)
├── QuyTrinh-Chien-Luoc/          # Quy trình chiến lược kênh (chỉ đọc, không tự ý sửa)
├── Fanpage-Asset/                # Bio, ảnh đại diện/bìa kênh, concept nhân vật Gấu
└── docs/
    ├── DNA.md                   # Định vị kênh, persona Gấu, giọng kể, cụm từ cấm (đúc kết vận hành)
    ├── Channel-DNA-goc.md        # File gốc: title patterns, hook patterns, video structure
    ├── Style-Guide-goc.md        # File gốc: persona, voice rules, benchmark passages, thumbnail text bank
    ├── Visual-Prompts-goc.md     # File gốc: charStyle/bgStyle/masterPrompt cho ảnh AI
    ├── Chu-De-goc.md             # File gốc: 8 pillar, 24 topic, series, launch sequence, scoring
    ├── cach-lam-chuan.md        # Quy trình chuẩn + checklist chất lượng
    ├── lich-su-phien.md         # Nhật ký sửa tay (bản gốc → bản sửa → lý do)
    ├── da-dung-de-tai.md        # Tra trước C0 — kho ý tưởng chờ sản xuất + đã dùng
    ├── chien-luoc-youtube.md    # Nguyên tắc chiến lược tăng trưởng YouTube
    └── nhat-ky-hieu-qua.md      # Số liệu CTR/Retention từng video (tạo khi chạy S1 lần đầu)
```

## 2. Yêu cầu chung
- Ngôn ngữ làm việc: tiếng Việt.
- Định dạng: **ảnh tĩnh + voice**, KHÔNG animation — mỗi scene là 1 ảnh AI tĩnh, ghép theo timeline voice.
- Mỗi tập là 1 ngành nghề/chủ đề tài chính độc lập, không nối tiếp cốt truyện. Nhân vật Gấu là người dẫn chuyện cố định, xuất hiện xuyên suốt — không tuỳ chọn, luôn có mặt.
- Không tự ý sửa file trong `QuyTrinh/` — chỉ sửa khi người dùng xác nhận đạt và yêu cầu cụ thể.
- Chống lặp/chồng chéo nội dung giữa `CLAUDE.md` ↔ `docs/DNA.md` ↔ `QuyTrinh/C*.md`: trước khi ghi quy tắc mới, kiểm tra đã có ở chỗ khác chưa; nếu có, sửa vào chỗ cũ hoặc trỏ tham chiếu thay vì chép lại.
- **Kinh nghiệm/đúc kết phải lưu file cứng trong project (thư mục `docs/`), KHÔNG chỉ lưu ở bộ nhớ Claude trên máy** — bộ nhớ đó nằm ngoài project, không được git backup, hư máy là mất. Mọi kiến thức/chiến lược/bài học người dùng chia sẻ hoặc rút ra trong quá trình làm phải ghi thành file `.md` trong `docs/` rồi commit + push lên GitHub để backup thật sự.
- **Khung an toàn nội dung bắt buộc** (`docs/DNA.md` mục 4): không tư vấn đầu tư cụ thể, không nêu đích danh doanh nghiệp/cá nhân kèm phán xét tiêu cực, luôn giữ khung "ước tính/tổng hợp cá nhân" cho mọi số liệu, luôn có disclaimer + catchphrase cố định.
- **Trước khi ghi thêm bất kỳ quy tắc/kỹ thuật mới nào vào project (docs/QuyTrinh), phải tự phân tích nên ghi CỨNG (bắt buộc, đúng thứ tự/vị trí/từ ngữ cố định) hay ghi CỐT LÕI (nguyên tắc/kho kỹ thuật chọn linh hoạt tuỳ tình huống)** — tuỳ vào bản chất nội dung, không mặc định ghi cứng cho tiện:
  - Ghi CỨNG khi: câu chữ pháp lý/an toàn bắt buộc y nguyên (disclaimer, catchphrase), thứ tự khung sản xuất không đổi (6 bước video, thứ tự C0→C7), nhận diện/tone giọng xuyên suốt không đổi giữa các tập (persona Gấu, giọng tinh ranh mỉa mai, charStyle nhân vật), hoặc quy tắc kỹ thuật có đúng/sai rõ ràng (không tái dùng ảnh cũ, không copy tên thương hiệu thật).
  - Ghi CỐT LÕI khi: đó là cách **triển khai nội dung cụ thể của từng chủ đề/bài viết** — mỗi tập một ngành nghề khác nhau nên cách dẫn dắt, ví dụ, số liệu, thủ pháp kể chuyện đương nhiên phải khác nhau; nếu ghi cứng thành "bước X luôn làm Y" thì mọi tập sẽ rập khuôn theo đúng 1 motif dễ đoán, rủi ro giống "reused content" bị YouTube phạt (xem `docs/chien-luoc-youtube.md` mục 8). Trường hợp này chỉ ghi thành nguyên tắc/kho lựa chọn, kèm nhắc rõ "chọn linh hoạt, không dùng thành công thức cố định". Tóm gọn: **cái gì là bản sắc/nhận diện cố định của kênh → ghi cứng; cái gì là cách kể 1 câu chuyện cụ thể → ghi cốt lõi**.
  - Nếu không chắc, hỏi lại người dùng thay vì tự chọn ghi cứng.

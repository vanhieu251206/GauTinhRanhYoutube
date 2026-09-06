# C5 — Lấy Timing & Xuất Clip Câm Theo Scene

> Đầu vào: `voice.mp3` + `sub.srt` (cả 2 người dùng tự xuất cùng lúc từ TTS sau C1 — công cụ TTS hỗ trợ tải sẵn file `.srt` khớp timing thật, không cần tạo riêng qua CapCut/speech-to-text khác) + `scene-list.md` + ảnh đã đổi tên `001.jpg`...`0NN.jpg` trong `Anh Video/` (từ C4).
> Đầu ra: `timing.md` (mốc thời gian mỗi scene) + các clip câm `clips/scene-001.mp4`...`scene-0NN.mp4` — ảnh tĩnh, cắt cứng giữa các scene, KHÔNG dùng hiệu ứng zoom/pan. Người dùng chỉ còn việc ghép `voice.mp3` + nhạc nền + sub + logo trong CapCut, không cần tự cắt ảnh theo tay.

## Bước 1 — Lấy mốc thời gian mỗi scene
`sub.srt` đã có sẵn (tải kèm lúc xuất `voice.mp3` từ công cụ TTS, khớp timing thật) — dùng trực tiếp, KHÔNG tạo lại qua CapCut/speech-to-text khác, không tốn thêm bước nào. Chỉ dùng để lấy mốc thời gian, không dùng làm phụ đề hiển thị cuối cùng (phụ đề thật làm riêng ở hậu kỳ theo văn phong đã chốt).

`scene-list.md` (từ `QuyTrinh/C2-Chia-Scene.md`) đã là danh sách scene phẳng, mỗi dòng 1 scene có ý nghĩa riêng (không còn cấu trúc 2 cấp beat→ảnh) — với MỖI scene, xác định mốc theo quy tắc:
1. **Mốc bắt đầu**: đối chiếu câu/đoạn "Đoạn voice-script tương ứng" của scene đó trong `scene-list.md` với `sub.srt`, lấy mốc bắt đầu (s) = mốc bắt đầu của cue đầu tiên khớp câu đó — **RIÊNG SCENE ĐẦU TIÊN, mốc bắt đầu LUÔN = 0s** (đầu video thật), KHÔNG lấy mốc của cue đầu tiên trong `sub.srt` (thường lệch vài trăm mili-giây do khoảng lặng trước khi TTS phát ra tiếng đầu tiên) — nếu lấy nhầm mốc cue đầu, toàn bộ scene phía sau sẽ bị dịch sớm hơn giọng đọc thật đúng bằng khoảng lặng đó, gây lệch tiếng xuyên suốt cả video (lỗi đã từng xảy ra thật).
2. **Mốc kết thúc = mốc bắt đầu của scene NGAY SAU nó** (không cắt đúng tại điểm câu cuối scene dứt lời, để khoảng ngừng/hơi thở thuộc về scene ĐỨNG TRƯỚC, tránh giật cắt). Scene CUỐI CÙNG: kết thúc tại mốc kết thúc của cue cuối cùng trong `sub.srt`.
3. **Làm tròn theo mốc luỹ kế (cumulative rounding), KHÔNG làm tròn từng scene riêng lẻ**: vì bước xuất clip ở Bước 2 buộc phải làm tròn theo khung hình (frame), nếu làm tròn thời lượng từng scene độc lập rồi cộng lại, sai số làm tròn sẽ cộng dồn qua hàng trăm scene, gây lệch tiếng tích luỹ ngày càng nặng về cuối video (lỗi đã từng xảy ra thật, ~0,5-0,6s lệch trên 1 video 15 phút nếu làm tròn ngây thơ). Cách đúng: quy đổi MỌI mốc thời gian sang số khung hình bằng `round(mốc_giây × fps)` tính trên trục thời gian TUYỆT ĐỐI từ 0, rồi số khung của 1 scene = hiệu số khung giữa mốc kết thúc và mốc bắt đầu của chính scene đó (không phải làm tròn riêng độ dài). Cách này đảm bảo tổng số khung của mọi scene cộng lại luôn khớp đúng tổng số khung thật của toàn video, sai số chỉ còn dưới 1 khung hình duy nhất ở cuối cùng thay vì cộng dồn.
4. Ghi vào `timing.md`:

| STT scene | Bắt đầu (s) | Kết thúc (s) |
|---|---|---|

Sau khi có `timing.md`, đưa người dùng xem lại trước khi xuất clip.

## Bước 2 — Xuất clip câm theo scene
Với mỗi scene, lấy **số khung hình (frame)** đã tính ở Bước 1.3 (không dùng lại số giây thời lượng thô để tránh làm tròn lần 2). Xuất 1 clip câm (chỉ video, không audio track) từ ảnh `0NN.jpg` tương ứng, đúng số khung đó, lưu vào `clips/`, đặt tên `scene-001.mp4`, `scene-002.mp4`...

### Lệnh ffmpeg chuẩn (clip câm, không audio, xuất theo số khung chính xác)
```
ffmpeg -y -loop 1 -i "Anh Video/0NN.jpg" -r 25 -frames:v <số khung hình> -c:v libx264 -tune stillimage -pix_fmt yuv420p -an "clips/scene-0NN.mp4"
```
- Dùng `-frames:v <N>` (số khung chính xác) thay vì `-t <giây>` — tránh ffmpeg tự làm tròn thời lượng theo cách riêng của nó, khớp đúng số khung đã tính cumulative rounding ở Bước 1.3.
- `-r 25` cố định khung hình/giây — đổi số này nếu kênh sau này dùng fps khác, nhưng phải dùng ĐÚNG 1 fps cho toàn bộ video (không đổi giữa các scene).
- `-an` = bỏ hẳn audio track khỏi clip xuất ra (audio thật ghép sau trong CapCut).
- Sau khi xuất, dùng `ffprobe` kiểm tra lại `duration` của vài clip đại diện, đối chiếu đúng bằng `Kết thúc - Bắt đầu` trong `timing.md` trước khi báo hoàn thành.
- **Kiểm tra dung lượng file mỗi clip sau khi xuất** (file quá nhỏ bất thường là dấu hiệu xuất lỗi/bị ngắt giữa chừng) — clip nào lỗi phải xuất lại ngay, không báo hoàn thành khi còn clip hỏng.
- **Lỗi thường gặp khi chạy hàng loạt bằng vòng lặp shell**: nếu file danh sách thời lượng (VD file trung gian tự tạo để loop qua) có ký tự xuống dòng kiểu Windows (`\r\n` thay vì `\n`), tham số `-t <thời lượng>` sẽ dính thêm `\r` ở cuối và làm ffmpeg lỗi/loop báo fail hàng loạt dù ảnh và số liệu đều đúng — trước khi chạy hàng loạt, chuẩn hoá file trung gian về `\n` thuần (VD `tr -d '\r'`) hoặc kiểm tra bằng `cat -A` nếu thấy toàn bộ lệnh cùng lúc báo lỗi.

## Luật / Quy tắc
- Không tự thêm nhạc nền/hiệu ứng chuyển cảnh/logo/phụ đề ở bước này — người dùng tự ghép các phần này trong CapCut ở hậu kỳ, dùng clip câm này làm nền hình ảnh đã đúng thời lượng. KHÔNG áp dụng zoom/pan cho bất kỳ scene nào (ảnh tĩnh giữ nguyên, cắt cứng khi chuyển scene).
- Giữ đúng thứ tự STT scene khi xuất clip, không bỏ sót scene nào.
- Không cắt/chỉnh sửa nội dung `voice.mp3` ở bước này.
- Báo rõ cho người dùng: khi ghép trong CapCut, thả các clip trong `clips/` theo đúng thứ tự vào track hình, thả `voice.mp3` vào track tiếng, rồi mới thêm nhạc nền/hiệu ứng/logo/sub đè lên trên.

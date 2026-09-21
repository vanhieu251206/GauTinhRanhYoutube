# C5 — Lấy Timing & Xuất Clip Câm Theo Scene

> Đầu vào: `voice.mp3` + **2 file phụ đề**: `sub.srt` (tải kèm `voice.mp3` từ công cụ TTS — chữ khớp 100% `voice-script.md`, **mốc chính xác hơn, là mốc chính**) và `sub-capcut.srt` (người dùng cho CapCut tự tạo phụ đề từ chính `voice.mp3` rồi xuất `.srt` — **chỉ dùng đối chứng**, chữ có thể sai dấu/số/tên) +  `scene-list.md` + bộ ảnh cuối trong `Anh Video/` (từ C4): mỗi STT đúng 1 file — `NNN.jpg` cho scene `AI gen`/`Crop nguồn thật`, `NNN.png` (nền trong suốt) cho scene `Icon động`.
> Đầu ra: `timing.md` (mốc thời gian mỗi scene) + các clip câm `clips/scene-001.mp4`...`scene-0NN.mp4` — ảnh tĩnh, cắt cứng giữa các scene, KHÔNG dùng hiệu ứng zoom/pan (ngoại lệ duy nhất: scene `Icon động`, xem Bước 2b). Người dùng chỉ còn việc ghép `voice.mp3` + nhạc nền + sub + logo trong CapCut, không cần tự cắt ảnh theo tay.

## Bước 1 — Lấy mốc thời gian mỗi scene (kết hợp `sub.srt` + `sub-capcut.srt`)
Hai file có mốc KHÁC nhau (cùng 1 câu, mỗi bên báo một giá trị). Người dùng đã xác nhận (21/09/2026) **mốc của TTS chính xác hơn**, nên:
- **`sub.srt` (TTS) → mốc CHÍNH**: vừa định vị câu (chữ trùng đúng `voice-script.md`, không nhầm câu) vừa cho mốc bắt đầu dùng để dựng clip.
- **`sub-capcut.srt` → ĐỐI CHỨNG**: dùng để phát hiện chỗ định vị nhầm hoặc mốc TTS bất thường (2 file lệch nhau quá nhiều là dấu hiệu). **Không tin chữ trong file này** (nhận dạng giọng nói có thể sai dấu/số/tên riêng), không lấy mốc từ đây trừ khi không định vị được bằng TTS.
Cả hai chỉ dùng để lấy mốc, không dùng làm phụ đề hiển thị cuối cùng (phụ đề thật làm riêng ở hậu kỳ theo văn phong đã chốt).

`scene-list.md` (từ `QuyTrinh/C2-Chia-Scene.md`) là danh sách scene phẳng, mỗi dòng 1 scene có ý nghĩa riêng — với MỖI scene, xác định mốc theo quy tắc:
1. **Mốc bắt đầu (làm 3 bước)**:
   - (a) **Định vị bằng `sub.srt`**: đối chiếu câu đầu của "Đoạn voice-script tương ứng" với `sub.srt` → mốc `S_tts` = mốc bắt đầu của cue chứa câu đó (nếu câu nằm giữa cue nhiều câu thì nội suy theo tỉ lệ ký tự trong cue). **`S_tts` là mốc bắt đầu được chọn.**
   - (b) **Đối chứng bằng `sub-capcut.srt`**: trong cửa sổ `S_tts ± 2s`, tìm cue chứa 4-6 từ đầu của câu (so khớp mờ: chữ thường, bỏ dấu tiếng Việt và dấu câu, số đọc/viết tương đương) → mốc `S_cc` = mốc bắt đầu của cue đó (nếu từ đầu nằm giữa cue thì nội suy theo số từ). Chỉ để so sánh.
   - (c) **Xử lý chênh lệch** `|S_cc − S_tts|`: `≤ 0,5s` → bình thường; `> 0,5s` → gắn cờ **"nghe lại"** trong `timing.md` để người dùng nghe đúng đoạn đó (mốc vẫn dùng `S_tts`); `> 1s` → dừng hỏi người dùng (thường là nhận nhầm câu lặp/na ná nhau ở 1 trong 2 file). Không tìm được `S_cc` → giữ `S_tts`, ghi chú "chỉ TTS". Trường hợp hiếm không định vị được câu trong `sub.srt` → dùng `S_cc`, ghi chú "chỉ CapCut" và gắn cờ "nghe lại".
   - **RIÊNG SCENE ĐẦU TIÊN, mốc bắt đầu LUÔN = 0s** (đầu video thật), KHÔNG lấy mốc của cue đầu tiên của bất kỳ file nào (thường lệch vài trăm mili-giây do khoảng lặng trước khi tiếng đầu tiên phát ra) — nếu lấy nhầm mốc cue đầu, toàn bộ scene phía sau bị dịch sớm hơn giọng đọc thật đúng bằng khoảng lặng đó, gây lệch tiếng xuyên suốt cả video (lỗi đã từng xảy ra thật).
   - Kiểm tra cuối: các mốc chọn phải **tăng dần nghiêm ngặt** theo STT; scene sau ≤ scene trước là lỗi định vị, dừng báo.
2. **Mốc kết thúc = mốc bắt đầu của scene NGAY SAU nó** (không cắt đúng tại điểm câu cuối scene dứt lời, để khoảng ngừng/hơi thở thuộc về scene ĐỨNG TRƯỚC, tránh giật cắt). Scene CUỐI CÙNG: kết thúc tại mốc kết thúc của cue cuối cùng — lấy giá trị **lớn hơn** giữa 2 file, đối chiếu thêm độ dài `voice.mp3` bằng `ffprobe`; lệch quá 1s thì báo người dùng.
3. **Làm tròn theo mốc luỹ kế (cumulative rounding), KHÔNG làm tròn từng scene riêng lẻ**: vì bước xuất clip ở Bước 2 buộc phải làm tròn theo khung hình (frame), nếu làm tròn thời lượng từng scene độc lập rồi cộng lại, sai số làm tròn sẽ cộng dồn qua hàng trăm scene, gây lệch tiếng tích luỹ ngày càng nặng về cuối video (lỗi đã từng xảy ra thật, ~0,5-0,6s lệch trên 1 video 15 phút nếu làm tròn ngây thơ). Cách đúng: quy đổi MỌI mốc thời gian sang số khung hình bằng `round(mốc_giây × fps)` tính trên trục thời gian TUYỆT ĐỐI từ 0, rồi số khung của 1 scene = hiệu số khung giữa mốc kết thúc và mốc bắt đầu của chính scene đó (không phải làm tròn riêng độ dài). Cách này đảm bảo tổng số khung của mọi scene cộng lại luôn khớp đúng tổng số khung thật của toàn video, sai số chỉ còn dưới 1 khung hình duy nhất ở cuối cùng thay vì cộng dồn.
4. Ghi vào `timing.md` (giữ cả 2 mốc để người dùng đối chiếu; các bước sau chỉ dùng cột "Bắt đầu chọn"):

| STT scene | Bắt đầu TTS (s) | Bắt đầu CapCut (s) | Chênh (s) | Bắt đầu chọn (s) | Kết thúc (s) | Ghi chú |
|---|---|---|---|---|---|---|

Cột "Ghi chú": `TTS` (bình thường, 2 file khớp) / `chỉ TTS` (không khớp được CapCut) / `chỉ CapCut` (không định vị được bằng TTS) / `nghe lại` (chênh > 0,5s) / `0s` (scene đầu). Cuối `timing.md` ghi thống kê: số scene bình thường, số scene chỉ TTS, số scene gắn cờ "nghe lại".

**Chạy C5 là làm liền cả Bước 1 và Bước 2: sau khi có `timing.md` KHÔNG dừng hỏi người dùng, xuất clip luôn** (người dùng đã chốt 21/09/2026). Chỉ dừng lại hỏi khi: có scene ghi chú `DỪNG HỎI` / `KHÔNG ĐỊNH VỊ ĐƯỢC`, lỗi thứ tự mốc, thiếu ảnh trong `Anh Video/`, hoặc `timing.md` lệch số scene với `scene-list.md`. Các scene gắn cờ `nghe lại` không chặn việc xuất clip — báo trong phần tổng kết để người dùng nghe kiểm sau.

**Công cụ có sẵn (dùng thay cho gõ lệnh từng scene):**
- Bước 1: `python Cong-Cu/timing-scene/timing_scene.py "Bai-Dang/Tap N - [tên]"` → `timing.md` (thư mục tập cần có `scene-list.md`, `sub.srt`, file `sub-capcut.srt` hoặc `sub capcut.srt`, `voice.mp3`).
- Bước 2: `python Cong-Cu/timing-scene/xuat_clip.py "Bai-Dang/Tap N - [tên]" --entrance "STT=kiểu,..."` → toàn bộ `clips/` (ảnh tĩnh bằng ffmpeg, icon bằng `icon_anim.py`), tự kiểm tra từng clip đủ số khung/1920x1080 và tổng số khung khớp `timing.md`. Kiểu xuất hiện của scene `Icon động` chọn theo ý từng câu voice rồi truyền qua `--entrance`; scene không chỉ định thì xoay vòng.

## Bước 2 — Xuất clip câm theo scene (phân loại theo cột "Loại ảnh" của `scene-list.md`)
Với mỗi scene, lấy **số khung hình (frame)** đã tính ở Bước 1.3 (không dùng lại số giây thời lượng thô để tránh làm tròn lần 2), rồi **tra cột "Loại ảnh" của đúng STT đó trong `scene-list.md`** để chọn cách xuất — không đoán theo đuôi file:
- `AI gen` / `Crop nguồn thật` → Bước 2a (ảnh tĩnh, `clips/scene-0NN.mp4`).
- `Icon động` → Bước 2b (chuyển động trên nền kẻ ô, `clips/scene-0NN.mp4`).
Đầu ra là 1 bộ `clips/` đủ mọi STT, mỗi STT đúng 1 clip. Trước khi chạy, đối chiếu đuôi file `Anh Video/NNN.*` với loại ảnh (`.png` ↔ `Icon động`); lệch thì dừng báo người dùng.

## Bước 2a — Clip ảnh tĩnh
Xuất 1 clip câm (chỉ video, không audio track) từ `Anh Video/0NN.jpg`, đúng số khung đã tính, đặt tên `scene-001.mp4`, `scene-002.mp4`...

### Lệnh ffmpeg chuẩn (clip câm, không audio, xuất theo số khung chính xác)
```
ffmpeg -y -loop 1 -i "Anh Video/0NN.jpg" -r 25 -frames:v <số khung hình> -vf "scale=1920:1080:flags=lanczos,setsar=1" -c:v libx264 -tune stillimage -pix_fmt yuv420p -an "clips/scene-0NN.mp4"
```
- `-vf scale=1920:1080` đưa mọi ảnh về cùng khổ 1920x1080 (ảnh gen ra thường 1376x768, ảnh crop 1920x1080, clip icon 1920x1080) để mọi clip trong `clips/` đồng nhất; ảnh đều 16:9 nên không méo. Nếu gặp ảnh khác tỉ lệ 16:9 thì báo người dùng, không tự kéo giãn.
- Dùng `-frames:v <N>` (số khung chính xác) thay vì `-t <giây>` — tránh ffmpeg tự làm tròn thời lượng theo cách riêng của nó, khớp đúng số khung đã tính cumulative rounding ở Bước 1.3.
- `-r 25` cố định khung hình/giây — đổi số này nếu kênh sau này dùng fps khác, nhưng phải dùng ĐÚNG 1 fps cho toàn bộ video (không đổi giữa các scene).
- `-an` = bỏ hẳn audio track khỏi clip xuất ra (audio thật ghép sau trong CapCut).
- Sau khi xuất, dùng `ffprobe` kiểm tra lại `duration` của vài clip đại diện, đối chiếu đúng bằng `Kết thúc - Bắt đầu` trong `timing.md` trước khi báo hoàn thành.
- **Kiểm tra dung lượng file mỗi clip sau khi xuất** (file quá nhỏ bất thường là dấu hiệu xuất lỗi/bị ngắt giữa chừng) — clip nào lỗi phải xuất lại ngay, không báo hoàn thành khi còn clip hỏng.
- **Lỗi thường gặp khi chạy hàng loạt bằng vòng lặp shell**: nếu file danh sách thời lượng (VD file trung gian tự tạo để loop qua) có ký tự xuống dòng kiểu Windows (`\r\n` thay vì `\n`), tham số `-t <thời lượng>` sẽ dính thêm `\r` ở cuối và làm ffmpeg lỗi/loop báo fail hàng loạt dù ảnh và số liệu đều đúng — trước khi chạy hàng loạt, chuẩn hoá file trung gian về `\n` thuần (VD `tr -d '\r'`) hoặc kiểm tra bằng `cat -A` nếu thấy toàn bộ lệnh cùng lúc báo lỗi.

## Bước 2b — Clip cho scene `Icon động`
Scene `Icon động` (cột "Loại ảnh" ở `scene-list.md`) KHÔNG xuất bằng lệnh ffmpeg ảnh tĩnh ở Bước 2a. Dùng ảnh `Anh Video/0NN.png` (từ C4, PNG nền trong suốt) ghép lên nền kẻ ô dùng chung, với `<N>` = số khung đã tính ở Bước 1.3 của đúng scene đó:
```
python Cong-Cu/icon-anim/icon_anim.py "Anh Video/0NN.png" -o clips --fps 25 --frames <N> --name scene-0NN.mp4 --bg Fanpage-Asset/Nen-Luoi-O/nen-luoi-o.png --bg-scroll 60 --entrance <pop|rise|drop|slide-left|slide-right|fade>
```
- **Nền kẻ ô cuộn xuống liên tục** (mặc định 60 px/giây, `--bg-scroll`; 0 = nền đứng yên) — chỉ nền chuyển động, icon thì **chỉ có hiệu ứng xuất hiện rồi đứng yên hoàn toàn** (không lơ lửng/lắc — quyết định của người dùng 21/09/2026). Hiệu ứng xuất hiện kéo dài ~0,6s đầu (`--enter-dur` chỉnh được).
- Ra `clips/scene-0NN.mp4` (H.264, 1920x1080, nền kẻ ô đã ghép sẵn, đúng số khung, nhẹ ~1-3 MB) — dùng y như clip ảnh tĩnh, không cần track nền riêng ở CapCut.
- Chọn `--entrance` **linh hoạt theo từng scene**, không dùng 1 kiểu cho mọi icon trong tập (VD `pop` cho con số gây sốc, `rise`/`fade` cho sơ đồ nhẹ nhàng, `slide-left`/`slide-right` xen kẽ khi 2 icon liên tiếp). Xem `docs/icon-dong.md`.
- Kiểm tra sau xuất: `ffprobe -count_frames` phải ra đúng `<N>` khung.
- Cần bản nền trong suốt (để tự đặt lên nền khác)? bỏ `--bg` và đặt tên `.mov` (ProRes 4444, nặng vài chục MB). Không xuất `.webm` (CapCut đọc alpha VP9 lỗi).

## Luật / Quy tắc
- Không tự thêm nhạc nền/hiệu ứng chuyển cảnh/logo/phụ đề ở bước này — người dùng tự ghép các phần này trong CapCut ở hậu kỳ, dùng clip câm này làm nền hình ảnh đã đúng thời lượng. KHÔNG áp dụng zoom/pan cho scene ảnh tĩnh (giữ nguyên, cắt cứng khi chuyển scene); chuyển động chỉ dành cho scene `Icon động` theo Bước 2b.
- Giữ đúng thứ tự STT scene khi xuất clip, không bỏ sót scene nào.
- Không cắt/chỉnh sửa nội dung `voice.mp3` ở bước này.
- Báo rõ cho người dùng: khi ghép trong CapCut, thả các clip trong `clips/` theo đúng thứ tự vào track hình, thả `voice.mp3` vào track tiếng, rồi mới thêm nhạc nền/hiệu ứng/logo/sub đè lên trên.

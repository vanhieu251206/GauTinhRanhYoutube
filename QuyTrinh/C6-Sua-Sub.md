# C6 — Sửa Sub (gộp `sub.srt` + `sub-capcut.srt` thành 1 file phụ đề mới)

> Đầu vào: `sub.srt` (TTS — chữ khớp `voice-script.md`, mốc chính xác) + `sub-capcut.srt` (CapCut tự tạo từ `voice.mp3` — cue ngắn, chữ có thể sai) + `voice.mp3` (từ C5; nếu thư mục tập chưa có `timing.md` thì vẫn làm được, C6 không phụ thuộc clip).
> Đầu ra: **`sub-final.srt`** trong `Bai-Dang/Tap N - [tên]/` — phụ đề hoàn chỉnh để nhập vào CapCut: mỗi dòng **vừa 1 dòng hiển thị (không bị xuống dòng), không ngắt ý**, chữ đúng chính tả/đúng chữ gốc, mốc theo giọng đọc thật.
> Vì sao cần bước này: `sub.srt` chia theo CÂU nên nhiều cue quá dài (100+ ký tự), bỏ vào CapCut bị xuống 2-3 dòng; `sub-capcut.srt` chia ngắn nhưng chữ sai (dấu, số, "buffet" thay vì chữ thật...) và ngắt tuỳ tiện. Kết hợp: **chữ của TTS + điểm ngắt/mốc của CapCut**.

## Bước 1 — Chạy công cụ
```
python Cong-Cu/sub-fix/sua_sub.py "Bai-Dang/Tap N - [tên]"          # mặc định: tối đa 42 ký tự/dòng, 4,5s/dòng
python Cong-Cu/sub-fix/sua_sub.py "Bai-Dang/Tap N - [tên]" --max-chars 38   # chỉnh nếu vào CapCut vẫn xuống dòng
```
Cần trong thư mục tập: `sub.srt`, `sub-capcut.srt` (hoặc `sub capcut.srt`). Công cụ đọc thêm sổ tay phiên âm ở `QuyTrinh/C1-Script.md`.

## Quy tắc công cụ áp dụng (cứng — tránh lỗi đã hiểu rõ)
1. **Chữ**: chỉ lấy từ `sub.srt` (khớp voice-script), KHÔNG lấy chữ của CapCut. Công cụ tự kiểm cuối: ghép mọi dòng mới lại phải trùng 100% chữ gốc (không mất, không thừa, không đảo).
2. **Khôi phục chữ gốc để mắt đọc** (lời đọc TTS đã phiên âm, chữ hiển thị thì không): "búp phê" → "buffet", các phiên âm ≥ 2 từ trong sổ tay C1 (VD "Xơ Cồ Cây" → "Circle K"); "N phần trăm" → "N%". Phiên âm 1 từ trùng từ tiếng Việt thường (VD "yên") KHÔNG đổi tự động. Thêm tên riêng mới vào sổ tay C1 thì công cụ tự dùng.
3. **Độ dài**: mỗi dòng ≤ `--max-chars` (mặc định 42 ký tự kể cả khoảng trắng — chỉnh sau khi thử trong CapCut nếu vẫn bị xuống dòng); mỗi dòng ≤ 4,5s; tối thiểu 0,8s nếu còn khoảng trống (không chồng dòng sau).
4. **Không ngắt ý** — thứ tự ưu tiên chỗ ngắt: sau dấu câu (`. ? !`, rồi `, ; :`) → trước liên từ/giới từ mở mệnh đề (và, nhưng, mà, vì, để, khi, nếu, thì, cho, với, "là"...) → cuối cùng mới ngắt giữa cụm. **Cấm ngắt**: giữa số và đơn vị ("199.000 | đồng", "36 | suất", "hai | tiếng"); giữa các từ trong cụm cố định (danh sách trong công cụ: búp phê, lãi gộp, giá vốn, chỗ ngồi, hộ kinh doanh, chủ quán, thương hiệu...); để đại từ chủ ngữ ("tôi", "nó"...) ở cuối dòng tách khỏi động từ; để từ nối/hư từ (là, và, của, ở, cho, với, để, các, những, một, mỗi, nhiều, từng, hơn, gần, khoảng...) ở cuối dòng. Cụm mới phát sinh ở tập nào → thêm vào danh sách `PROTECT` trong `sua_sub.py` (không tạo danh sách riêng chỗ khác).
5. **Câu ngắn** (< 10 ký tự) được gộp vào dòng liền kề nếu vẫn vừa; câu 1 từ đứng riêng (VD "Thuế.") giữ nguyên.
6. **Mốc**: đầu và cuối mỗi cue TTS giữ nguyên (TTS chính xác hơn); điểm ngắt bên trong 1 cue lấy từ mốc của `sub-capcut.srt` nếu khớp được (nội suy trong cue CapCut), không khớp thì chia theo tỉ lệ số ký tự.
7. **Trình bày**: bỏ dấu `.` `,` `;` `:` ở cuối dòng; giữ `?` `!`.

## Bước 2 — Đọc báo cáo của công cụ và xử lý
Công cụ in: số dòng mới, độ dài lớn nhất/trung bình, kiểm tra không mất chữ, danh sách dòng ngắn (< 8 ký tự) / dòng quá 4,5s / dòng đọc nhanh (> 24 ký tự/giây — nhanh do giọng đọc thật, không sửa được bằng cách chia lại, chỉ báo để người dùng biết).
- Nếu báo **LỆCH chữ** hoặc dòng vượt giới hạn: dừng, tìm nguyên nhân (thường là 1 từ dài bất thường hoặc file phụ đề lỗi định dạng), không giao `sub-final.srt` lỗi.
- Xem nhanh ~30 dòng rải đều `sub-final.srt` bằng mắt: dòng nào ngắt giữa cụm/để lại từ lơ lửng cuối dòng thì thêm cụm vào `PROTECT` hoặc từ vào `NOEND` rồi chạy lại (công cụ chạy lại vài giây, ghi đè `sub-final.srt`).

## Bước 3 — Giao người dùng
Nhắc: nhập `sub-final.srt` vào CapCut (Phụ đề → Nhập/Import phụ đề), kiểm tra vài chỗ có bị xuống dòng không; nếu còn xuống dòng, báo con số để chạy lại với `--max-chars` nhỏ hơn. `sub-final.srt` **thay thế** `sub.srt`/`sub-capcut.srt` làm phụ đề hiển thị trong video — 2 file cũ chỉ giữ để tra mốc/đối chứng.

## Lưu ý
- C6 chỉ làm phụ đề hiển thị; **không** đụng đến `timing.md` và các clip đã xuất ở C5 (mốc scene tách biệt với mốc phụ đề).
- Chữ phụ đề cuối cùng vẫn là chữ của `voice-script.md` — muốn đổi cách hiển thị một cụm (VD "sáu" → "6") thì làm ở bước Trình bày/`to_display` trong công cụ, đừng sửa tay từng dòng (sẽ mất khi chạy lại).

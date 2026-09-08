# C6 — Tạo Thumbnail

> Đầu vào: khoảnh khắc/biểu cảm đắt giá nhất của video (chọn từ `scene-list.md`/nội dung tập), tiêu đề video đã chốt (từ C1 Bước 5, chốt lại chính thức ở `C7-Dang-bai.md` Bước 1).
> Đầu ra: `Bai-Dang/Tap N - [tên]/thumbnail-nen.jpg` — ảnh nền do AI vẽ, **KHÔNG có chữ trong ảnh** — người dùng tự chèn chữ thủ công (Canva/Photoshop/CapCut) để ra `thumbnail.jpg` cuối cùng (kiểm soát chính tả/bố cục tốt hơn để AI tự vẽ chữ).
> Nhắc lại theo `docs/cach-lam-chuan.md` mục 0: Tiêu đề + Thumbnail quan trọng hơn nội dung trong việc quyết định video có được đề xuất hay không — không sa đà làm sơ sài bước này.

## Bước 1 — Chọn khoảnh khắc/biểu cảm của Gấu làm nền
Gấu **luôn xuất hiện** trong thumbnail (`docs/Channel-DNA-goc.md` mục 7 — "KHÔNG BAO GIỜ bỏ"). Cần 1 biểu cảm/tư thế đắt giá nhất khớp đúng con số/nghịch lý chính của tập. Danh sách biểu cảm ở `docs/Visual-Prompts-goc.md` mục 1 (nheo mắt tính toán, cười khẩy, dò xét qua kính, chỉ tay, khoanh tay tự tin) là kho tham khảo có sẵn, không bắt buộc — dùng đúng 5 biểu cảm này xoay vòng qua nhiều tập dễ khiến lưới thumbnail của kênh nhìn lặp. **Hỏi người dùng mỗi lần tới bước này**: chọn 1 biểu cảm có sẵn, hay nghĩ tư thế/biểu cảm mới phù hợp hơn với tập này.

Không lấy đại 1 phương án duy nhất — thử ít nhất 2-3 biểu cảm khác nhau cho cùng 1 khoảnh khắc rồi chọn bản "có hồn" nhất.

## Bước 2 — Viết chữ thumbnail
Thumbnail Text Bank ở `docs/Style-Guide-goc.md` mục 6 (4 nhóm: Question / Statement / Number / Emotion) là kho mẫu có sẵn, không bắt buộc — **hỏi người dùng mỗi lần tới bước này**: dùng nguyên văn/biến tấu 1 câu từ Text Bank, hay tự viết chữ mới cho tập này (để tránh nhiều tập dùng trùng cụm chữ).
- **Tối đa 4-5 từ, không quá 2 dòng** (đúng quy tắc `docs/Style-Guide-goc.md` mục 6).
- Giọng mỉa mai/cảm thán đúng tinh thần Gấu, không phải câu tóm tắt nội dung — thumbnail chỉ cần gây tò mò, tiêu đề video mới giải thích rõ.
- Đề xuất 2-3 phương án chữ, đưa người dùng chọn/chỉnh trước khi viết prompt.

## Bước 3 — Viết prompt thumbnail
Dùng lại **charStyle cố định của Gấu** ở `QuyTrinh/C3-Prompt-Anh.md` — mặc định giữ đúng 1 bộ nhận diện vest xanh navy + kính lão vàng đồng. Nếu tập này có dùng ảnh tham chiếu hoá trang riêng (xem C3), thumbnail nên ưu tiên vẫn dùng bộ vest gốc để giữ nhận diện kênh nhất quán trên trang chủ/lưới video, trừ khi bộ hoá trang đó chính là điểm nhấn hài hước cần lên thumbnail. Ghép prompt theo khuôn sau:

1. **Mở đầu cố định + shot**: `Cartoonish illustrative thumbnail, [shot type] focusing on the Gấu bear mascot character` + dán nguyên văn charStyle cố định (`QuyTrinh/C3-Prompt-Anh.md` Bước 2). Chọn `[shot type]`: medium close-up (đa số) hoặc wide shot (khi cần thấy trọn bối cảnh ngành).
2. **Bối cảnh nền** — 1 trong 2 dạng theo `docs/Visual-Prompts-goc.md` mục 2 (bgStyle): nền phẳng minh hoạ (biểu đồ, mô hình kinh doanh) hoặc nền ảnh thật liên quan ngành nghề của tập (mờ nhẹ để Gấu nổi bật), luôn đẩy hẳn về không gian Việt Nam nếu là ảnh thật.
3. **Bố cục khung hình + chừa chỗ chữ chèn tay sau**: Gấu chiếm 30-40% khung hình, đặt lệch trái hoặc phải (`docs/Style-Guide-goc.md` mục 6 — Thumbnail Composition Rules), chừa 1 khoảng trống liền mạch tự nhiên (không mô tả là "vùng dành cho chữ" tách biệt) ở phía đối diện để đè chữ đã chốt ở Bước 2.
4. **Câu kết cố định về phong cách + chặn chữ tự sinh**: `The entire image should have a distinct, flat 2D vector cartoon style with clean bold black outlines and minimal flat color fill — not photorealistic, not a cinematic render. Navy blue and gold-bronze color palette. Use strong color contrast between the character and the background. No text, letters, or writing anywhere in the image.`

**Sau khi gen, bắt buộc kiểm tra**: (1) đúng phong cách flat 2D vector, đúng charStyle cố định của Gấu (mắt híp, kính lão gọng tròn vàng đồng, vest xanh navy — không bị vẽ lệch màu/lệch chi tiết); (2) mảng trống dành cho chữ có sạch, đủ chỗ; (3) ảnh không tự sinh chữ/ký tự lạ. Phát hiện lỗi phải gen lại toàn bộ ảnh.

## Bước 4 — Quy cách kỹ thuật
- Kích thước xuất: **1280×720px** (16:9, chuẩn YouTube), dung lượng dưới 2MB, định dạng JPG/PNG.
- Tông màu tổng thể đồng bộ avatar/banner kênh: xanh navy (#0C447C) - vàng đồng (#BA7517) theo `docs/Style-Guide-goc.md` mục 6 — giữ nhận diện thương hiệu nhất quán qua các tập.

## Bước 5 — Lưu file
Lưu prompt đã chốt vào `Bai-Dang/Tap N - [tên]/thumbnail-prompt.txt`, ảnh nền gen ra (KHÔNG chữ) lưu thành `Bai-Dang/Tap N - [tên]/thumbnail-nen.jpg`. Đưa người dùng xem lại ảnh nền + cụm chữ đã chốt ở Bước 2 để người dùng tự chèn chữ thủ công (Canva/Photoshop/CapCut) ra `thumbnail.jpg` cuối cùng trước khi qua `C7-Dang-bai.md`.

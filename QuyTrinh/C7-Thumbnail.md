# C7 — Tạo Thumbnail

> Đầu vào: `voice-script.md` (để chốt góc nhìn của tập), khoảnh khắc/biểu cảm đắt giá nhất của video (chọn từ `scene-list.md`/nội dung tập), tiêu đề video đã chốt (từ C1 Bước 5, chốt lại chính thức ở `C8-Dang-bai.md` Bước 1).
> Đầu ra: `Bai-Dang/Tap N - [tên]/thumbnail-nen.jpg` — ảnh nền do AI vẽ, **KHÔNG có chữ trong ảnh** — người dùng tự chèn chữ thủ công (Canva/Photoshop/CapCut); bản làm việc có chữ có thể đặt tên `thumb-NN.jpg`; **bản cuối luôn xuất thành `thumbnail.jpg` 1280×720** (Bước 6).
> Nhắc lại theo `docs/cach-lam-chuan.md` mục 0: Tiêu đề + Thumbnail quan trọng hơn nội dung trong việc quyết định video có được đề xuất hay không — không sa đà làm sơ sài bước này.
> Cách làm ở bản này đúc kết từ Tập 9 (người dùng chốt 21/09/2026: thử thumbnail "cực đoan" theo mẫu kênh khác ngách; kỹ thuật tham khảo ở `docs/chien-luoc-youtube.md` mục "Thumbnail tham khảo từ kênh hoạt hình khác ngách"). Phần **kiểm tra** (Bước 0, 2, 5) là quy tắc cứng; phần **kho kỹ thuật** (Bước 1, 3) là cốt lõi — chọn linh hoạt, mỗi tập một kiểu, không dùng thành công thức cố định.

## Bước 0 — Chốt góc nhìn của tập TRƯỚC khi nghĩ hình và chữ (bắt buộc)
Đọc lại `voice-script.md` (không chỉ tiêu đề) và ghi 3 dòng ngắn:
1. **Nghịch lý/thông điệp chính của video** (VD Tập 9: "chủ quán buffet không sợ khách ăn nhiều, sợ bàn vắng").
2. **Video KHÔNG nói gì / phần dễ bị hiểu sai** (VD Tập 9: không nói "chủ không bao giờ lỗ", không phải mẹo ăn cho lời).
3. **Câu người xem sẽ mang theo khi thấy thumbnail** — thumbnail đặt câu hỏi hay tuyên bố điều gì, và video trả lời đúng điều đó không.
Lý do (lỗi thật ở Tập 9): cụm chữ "Khách lời nhưng chủ không lỗ" và hình Gấu ngồi trên núi tiền đều **trái với thông điệp** video (có ví dụ chủ quán lỗ 60 triệu/tháng); bản đầu "TÔI SỢ NGÀY VẮNG" đi kèm hình khách ăn khỏe khiến người xem hiểu ngược. Thumbnail lệch góc → người vào xem thấy video nói khác → giảm thời gian xem.

## Bước 1 — Chọn khoảnh khắc/biểu cảm của Gấu làm nền
Gấu **luôn xuất hiện** trong thumbnail (`docs/Channel-DNA-goc.md` mục 7 — "KHÔNG BAO GIỜ bỏ"). Cần 1 biểu cảm/tư thế đắt giá nhất khớp đúng nghịch lý ở Bước 0. Danh sách biểu cảm ở `docs/Visual-Prompts-goc.md` mục 1 (nheo mắt tính toán, cười khẩy, dò xét qua kính, chỉ tay, khoanh tay tự tin) là kho tham khảo có sẵn, không bắt buộc — dùng đúng 5 biểu cảm này xoay vòng dễ khiến lưới thumbnail nhìn lặp. **Hỏi người dùng mỗi lần tới bước này**: chọn 1 biểu cảm có sẵn, hay nghĩ tư thế/biểu cảm mới; và có làm kiểu **cực đoan** (mục dưới) không.

**Kho kỹ thuật "cực đoan" (CỐT LÕI — chọn vài kỹ thuật hợp tình huống, không dùng đủ mọi thứ, không lặp cùng 1 tổ hợp giữa các tập):**
- **Gấu tràn khung 40-55%** (thay cho mức 30-40% cũ ở `docs/Style-Guide-goc.md` mục 6 khi làm kiểu cực đoan), biểu cảm phóng đại hết cỡ: mắt lồi trong gọng kính, sao quay quanh đầu, hàm rớt lộ răng vàng, mồ hôi, một mắt nhắm một mắt lồi... Biểu cảm phải **ghi đè** (override) biểu cảm nghỉ mặc định của charStyle.
- **Góc máy động**: nghiêng khung 10-15° (Dutch angle), góc thấp/cận vừa, Gấu nghiêng người về phía người xem, ngón tay chỉ vào vật/đối tượng gây rắc rối.
- **Chiều sâu nhiều lớp**: vật thể lớn mờ ở tiền cảnh (khay thịt, đồng hồ taxi khổng lồ, đôi đũa), nhân vật phụ/đám đông ở hậu cảnh, có **đối trọng khổng lồ** tạo kịch tính về tỉ lệ.
- **Bối cảnh = chính tình huống của tiêu đề**, nền ảnh cảnh mờ nhẹ, **màu ấm bão hoà** (cam đỏ/vàng); Gấu giữ vest navy + kính vàng đồng để nổi trên nền ấm.
- **Điểm nhấn nhỏ vừa đủ**: vài ngôi sao, 1 dấu va chạm, vài đường tốc độ, giọt mồ hôi.
Không lấy đại 1 phương án duy nhất — **viết 2-3 biến thể prompt (mỗi biến thể là 1 hình huống/góc máy khác nhau)**, người dùng gen cả bộ rồi chọn bản "có hồn" nhất; chọn xong chỉ giữ đúng 1 dòng trong `thumbnail-prompt.txt`.

## Bước 2 — Viết chữ thumbnail
Thumbnail Text Bank ở `docs/Style-Guide-goc.md` mục 6 là kho mẫu có sẵn, không bắt buộc — **hỏi người dùng mỗi lần tới bước này**: dùng nguyên văn/biến tấu 1 câu từ Text Bank, hay tự viết chữ mới cho tập này (tránh nhiều tập trùng cụm chữ).
- **Tối đa 4-5 từ, không quá 2 dòng.** Chữ là câu nói đời thường, giọng mỉa mai/cảm thán của Gấu, không phải câu tóm tắt nội dung.
- **Kiểu chữ tham khảo** (chọn linh hoạt): (a) **câu hỏi mồi** — chữ hỏi điều người xem hay nghĩ sai, hình gợi câu trả lời sai, video trả lời ngược lại (VD Tập 9: "CHỦ QUÁN SỢ GÌ NHẤT?" + hình Gấu hoảng sợ chỉ vào khách ăn khỏe; video đáp: không phải khách ăn nhiều, mà là bàn vắng); (b) câu nói ngôi thứ nhất ("TÔI GHÉT HỌC THÊM"); (c) tên tình huống/từ khoá ngắn ("BÁN CHỖ NGỒI"); (d) con số (nếu là số giả định/ước tính thì thêm dấu "?" hoặc chữ "ƯỚC TÍNH" — theo `docs/DNA.md` mục 4).
- **Cách trình bày khi chèn chữ**: chữ khổng lồ chiếm ~30-40% thumbnail, chia 2 dòng, viền đen dày, vàng hoặc trắng, **tô 1 từ khoá màu khác** (đỏ/vàng), đặt ngay trong mảng trống của cảnh (không khung nền riêng), chừa **lề ≥ 4%** với mép khung (tránh sát mép phải; góc dưới phải sẽ bị YouTube đè nhãn thời lượng).
- **Kiểm tra bắt buộc trước khi chốt (3 thứ cùng chiều)**: *hình nói gì — chữ nói gì — video nói gì*. Nếu chữ trái với thông điệp video (kể cả nhìn "hấp dẫn"), đổi chữ. Chữ dạng mồi câu hỏi được phép "hình gợi đáp án sai" **chỉ khi** video thật sự đảo lại đúng như vậy và ghi rõ ở Bước 0.
- Đề xuất 2-3 phương án chữ, mỗi phương án ghi rõ số từ và đối chiếu Bước 0, đưa người dùng chọn/chỉnh trước khi viết prompt.
- Đối chiếu nhanh với công thức thumbnail đối thủ ở `docs/chien-luoc-youtube.md` mục Benchmark — không copy bố cục y hệt, chỉ dùng để kiểm tra hướng đi hiện tại còn đúng xu hướng ngách hay không.

## Bước 3 — Viết prompt thumbnail
Dùng lại **charStyle cố định của Gấu** ở `QuyTrinh/C3-Prompt-Anh.md` (Bước 2) — mặc định giữ đúng 1 bộ nhận diện vest xanh navy + kính lão vàng đồng (chi tiết hoá trang riêng của tập chỉ dùng nếu chính nó là điểm nhấn hài hước). Ghép prompt theo khuôn sau:

1. **Mở đầu cố định + shot**: `Cartoonish illustrative thumbnail, [shot type] focusing on the Gấu bear mascot character.` + dán nguyên văn charStyle cố định + câu chặn `no beard, no mustache, no extra facial hair, no extra accessories, no clothing details beyond what is explicitly described above.` + **câu ghi đè biểu cảm** (`IMPORTANT: the eye shape, eyebrow angle, and mouth shape described above are Gau's default resting state ONLY — the extreme expression described below MUST clearly override this default.`). `[shot type]`: tilted Dutch-angle medium close-up / dramatic low-angle close-up / extreme close-up dynamic shot (kiểu cực đoan), hoặc medium close-up/wide shot (kiểu thường).
2. **Tả Gấu chi tiết**: chiếm bao nhiêu % khung, nghiêng bao nhiêu độ, biểu cảm cụ thể từng bộ phận (mắt, mày, miệng, răng vàng), tư thế tay (ghi "rounded fingertips"), điểm nhấn nhỏ.
3. **Bối cảnh + lớp chiều sâu** (theo Bước 1): bối cảnh chính là tình huống của tiêu đề, nêu rõ vật ở tiền cảnh (mờ) và hậu cảnh; luôn là không gian Việt Nam; người phụ tả đầy đủ mặt/biểu cảm (`absolutely no black silhouettes or faceless figures`).
4. **Chừa mảng chữ**: 1 khoảng liền mạch, phẳng, sạch (VD `the upper-right 40 percent of the frame is a clean, open, flat warm coral-orange wall area with nothing important in it`) ở phía đối diện Gấu để chèn chữ tay sau; không mô tả là "vùng dành cho chữ".
5. **Câu kết**: `The entire image should have a distinct, flat 2D vector cartoon style with clean bold black outlines and minimal flat color fill — not photorealistic, not a cinematic render.` + màu (kiểu thường: `Navy blue and gold-bronze color palette`; kiểu cực đoan: `bold saturated warm [coral-red/orange] background with navy blue and gold-bronze accents on the character`) + `strong color contrast between the character and the background` + `No text, letters, numbers or writing anywhere in the image.` + `16:9 widescreen aspect ratio, landscape orientation.`

**Sau khi gen, bắt buộc kiểm tra**: (1) đúng phong cách flat 2D vector, đúng charStyle của Gấu (mắt/kính vàng đồng/vest navy/răng vàng — không lệch màu/chi tiết); (2) mảng trống chừa chữ sạch, đủ chỗ; (3) không tự sinh chữ/ký tự lạ; (4) **hình có nói cùng chiều với thông điệp ở Bước 0 không** (VD hình khách ăn khỏe + chữ "sợ ngày vắng" là lệch). Lỗi phải gen lại.

## Bước 4 — Quy cách kỹ thuật
- Kích thước xuất: **1280×720px** (16:9, chuẩn YouTube), dung lượng **dưới 2MB**, JPG/PNG. Ảnh gen/bản làm việc lớn hơn (VD 8000×4500, >5MB) phải thu nhỏ.
- Tông màu: kiểu thường giữ xanh navy (#0C447C) - vàng đồng (#BA7517) theo `docs/Style-Guide-goc.md` mục 6; kiểu cực đoan cho phép nền ấm bão hoà nhưng **Gấu luôn giữ vest navy + kính vàng đồng** để nhận diện thương hiệu nhất quán qua các tập.

## Bước 4.5 — Định dạng file prompt
`thumbnail-prompt.txt`: mỗi prompt viết thành **1 dòng duy nhất** (không xuống dòng giữa các đoạn) — dễ copy-paste nguyên khối. Khi còn đang thử nhiều biến thể thì mỗi biến thể 1 dòng; **chốt xong chỉ giữ đúng dòng đã dùng**.

## Bước 5 — Kiểm tra thu nhỏ (bắt buộc trước khi chốt)
Thu nhỏ bản làm việc xuống **360px và 168px bề ngang** (cỡ hiển thị lưới video/gợi ý) rồi xem lại: chữ vẫn đọc được, từ tô màu vẫn nổi, biểu cảm Gấu đọc được trong nửa giây, hình–chữ–video cùng chiều (Bước 2). Chữ đỏ trên nền cam/đỏ dễ kém tương phản — dùng viền đen dày hoặc đổi màu nếu đọc kém. Không đạt → sửa lại chữ/bố cục trước khi qua Bước 6.

## Bước 6 — Lưu file
Lưu prompt đã chốt vào `Bai-Dang/Tap N - [tên]/thumbnail-prompt.txt`, ảnh nền gen ra (KHÔNG chữ) lưu thành `thumbnail-nen.jpg`; người dùng chèn chữ ra bản làm việc rồi **xuất `thumbnail.jpg` 1280×720 (<2MB)** trước khi qua `C8-Dang-bai.md`. Claude xem lại bản có chữ theo Bước 3 (kiểm tra sau khi gen) và Bước 5 rồi nhận xét trước khi chốt; nếu người dùng gửi bản làm việc kích thước lớn, Claude xuất giúp `thumbnail.jpg` đúng quy cách.

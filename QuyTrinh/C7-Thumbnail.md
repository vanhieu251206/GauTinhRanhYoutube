# C7 — Tạo Thumbnail

> Đầu vào: `voice-script.md` (để chốt góc nhìn của tập), khoảnh khắc/biểu cảm đắt giá nhất của video (chọn từ `scene-list.md`/nội dung tập), tiêu đề video đã chốt (từ C1 Bước 5, chốt lại chính thức ở `C8-Dang-bai.md` Bước 1).
> Đầu ra: ảnh AI gen **KHÔNG có chữ trong ảnh** — Cách A (tách lớp): `thumb-gau.jpg` + `thumb-hoat-dong.jpg` (và bản tách nền `.png`); Cách B (1 cảnh): `thumbnail-nen.jpg` — người dùng tự ghép/chèn chữ thủ công (Canva/Photoshop/CapCut); bản làm việc có chữ đặt tên `thumb-NN.jpg`; **bản cuối luôn xuất thành `thumbnail.jpg` 1280×720** (Bước 6).
> Nhắc lại theo `docs/cach-lam-chuan.md` mục 0: Tiêu đề + Thumbnail quan trọng hơn nội dung trong việc quyết định video có được đề xuất hay không — không sa đà làm sơ sài bước này.
> Cách làm ở bản này đúc kết từ Tập 9 (người dùng chốt 21/09/2026: thử thumbnail "cực đoan" theo mẫu kênh khác ngách; kỹ thuật tham khảo ở `docs/chien-luoc-youtube.md` mục "Thumbnail tham khảo từ kênh hoạt hình khác ngách") và Tập 10 (24/09/2026: tách lớp Gấu + hoạt động chính trên nền trắng, người dùng tự ghép lên ảnh bối cảnh). Phần **kiểm tra** (Bước 0, 2, 3.5, 5) và **quy tắc nền trắng để tách nền** (Bước 3A) là quy tắc cứng; phần **kho kỹ thuật** (Bước 1, nội dung prompt ở Bước 3A/3B, lớp hoạt động/bối cảnh) là cốt lõi — chọn linh hoạt, mỗi tập một kiểu, không dùng thành công thức cố định.

## Bước 0 — Chốt góc nhìn của tập TRƯỚC khi nghĩ hình và chữ (bắt buộc)
Đọc lại `voice-script.md` (không chỉ tiêu đề) và ghi 3 dòng ngắn:
1. **Nghịch lý/thông điệp chính của video** (VD Tập 9: "chủ quán buffet không sợ khách ăn nhiều, sợ bàn vắng").
2. **Video KHÔNG nói gì / phần dễ bị hiểu sai** (VD Tập 9: không nói "chủ không bao giờ lỗ", không phải mẹo ăn cho lời).
3. **Câu người xem sẽ mang theo khi thấy thumbnail** — thumbnail đặt câu hỏi hay tuyên bố điều gì, và video trả lời đúng điều đó không.
Lý do (lỗi thật ở Tập 9): cụm chữ "Khách lời nhưng chủ không lỗ" và hình Gấu ngồi trên núi tiền đều **trái với thông điệp** video (có ví dụ chủ quán lỗ 60 triệu/tháng); bản đầu "TÔI SỢ NGÀY VẮNG" đi kèm hình khách ăn khỏe khiến người xem hiểu ngược. Thumbnail lệch góc → người vào xem thấy video nói khác → giảm thời gian xem.

## Bước 1 — Chọn cách dựng + khoảnh khắc/biểu cảm của Gấu
**Chọn 1 trong 2 cách dựng (hỏi người dùng; mặc định đề xuất Cách A):**
- **Cách A — Tách lớp rồi ghép (dùng từ Tập 10)**: gen riêng từng lớp trên **nền trắng tinh** — (1) **lớp Gấu** tạo dáng/biểu cảm (hoạt hình 2D), (2) **lớp hoạt động chính** là cảnh đặc trưng nhất của ngành (VD Tập 10: thợ rửa xe cầm súng xịt bọt + chiếc xe máy). Người dùng tách nền rồi tự ghép lên **ảnh bối cảnh** (VD Tập 10: đường phố thật, làm tối/mờ nhẹ). Ưu điểm: bố cục, cỡ chủ thể, chỗ chừa chữ chỉnh tự do khi ghép; mỗi lớp gen lại riêng được, không phải gen lại cả cảnh.
- **Cách B — 1 prompt cả cảnh (Tập 9)**: AI vẽ trọn cảnh kể cả nền và mảng chừa chữ (Bước 3B).
- Trong Cách A, **lớp hoạt động chính được chọn phong cách ảnh thật (photorealistic) hoặc hoạt hình 2D** tuỳ tập (CỐT LÕI) — ảnh thật giúp nhận ra ngay ngành nghề ở cỡ nhỏ; Gấu luôn giữ hoạt hình 2D đúng charStyle. Ảnh bối cảnh nền người dùng tự chọn (ảnh thật tự tìm hoặc gen), nên cùng ngành/không gian với tình huống tiêu đề và đủ tối/đơn giản để chủ thể và chữ nổi.

Gấu **luôn xuất hiện** trong thumbnail (`docs/Channel-DNA-goc.md` mục 7 — "KHÔNG BAO GIỜ bỏ"). Cần 1 biểu cảm/tư thế đắt giá nhất khớp đúng nghịch lý ở Bước 0. Danh sách biểu cảm ở `docs/Visual-Prompts-goc.md` mục 1 (nheo mắt tính toán, cười khẩy, dò xét qua kính, chỉ tay, khoanh tay tự tin) là kho tham khảo có sẵn, không bắt buộc — dùng đúng 5 biểu cảm này xoay vòng dễ khiến lưới thumbnail nhìn lặp. **Hỏi người dùng mỗi lần tới bước này**: chọn 1 biểu cảm có sẵn, hay nghĩ tư thế/biểu cảm mới; và có làm kiểu **cực đoan** (mục dưới) không.

**Kho kỹ thuật "cực đoan" (CỐT LÕI — chọn vài kỹ thuật hợp tình huống, không dùng đủ mọi thứ, không lặp cùng 1 tổ hợp giữa các tập):**
- **Gấu tràn khung 40-55%** (thay cho mức 30-40% cũ ở `docs/Style-Guide-goc.md` mục 6 khi làm kiểu cực đoan), biểu cảm phóng đại hết cỡ: mắt lồi trong gọng kính, sao quay quanh đầu, hàm rớt lộ răng vàng, mồ hôi, một mắt nhắm một mắt lồi... Biểu cảm phải **ghi đè** (override) biểu cảm nghỉ mặc định của charStyle.
- **Góc máy động**: nghiêng khung 10-15° (Dutch angle), góc thấp/cận vừa, Gấu nghiêng người về phía người xem, ngón tay chỉ vào vật/đối tượng gây rắc rối.
- **Chiều sâu nhiều lớp**: vật thể lớn mờ ở tiền cảnh (khay thịt, đồng hồ taxi khổng lồ, đôi đũa), nhân vật phụ/đám đông ở hậu cảnh, có **đối trọng khổng lồ** tạo kịch tính về tỉ lệ.
- **Bối cảnh = chính tình huống của tiêu đề**, nền ảnh cảnh mờ nhẹ, **màu ấm bão hoà** (cam đỏ/vàng); Gấu giữ vest navy + kính vàng đồng để nổi trên nền ấm.
- **Điểm nhấn nhỏ vừa đủ**: vài ngôi sao, 1 dấu va chạm, vài đường tốc độ, giọt mồ hôi.
Không lấy đại 1 phương án duy nhất — **viết 2-3 biến thể prompt (mỗi biến thể là 1 hình huống/góc máy khác nhau)**, người dùng gen cả bộ rồi chọn bản "có hồn" nhất (Cách A: viết biến thể cho lớp Gấu và/hoặc lớp hoạt động); chọn xong chỉ giữ đúng dòng đã dùng trong `thumbnail-prompt.txt` (Bước 4.5).

## Bước 2 — Viết chữ thumbnail
Thumbnail Text Bank ở `docs/Style-Guide-goc.md` mục 6 là kho mẫu có sẵn, không bắt buộc — **hỏi người dùng mỗi lần tới bước này**: dùng nguyên văn/biến tấu 1 câu từ Text Bank, hay tự viết chữ mới cho tập này (tránh nhiều tập trùng cụm chữ).
- **Tối đa 4-5 từ, không quá 2 dòng.** Chữ là câu nói đời thường, giọng mỉa mai/cảm thán của Gấu, không phải câu tóm tắt nội dung.
- **Ưu tiên chữ đơn giản, nói thẳng vấn đề** (người dùng chốt ở Tập 10): câu hỏi đúng điều người xem đang tự hỏi, đọc là hiểu ngay không cần suy luận, video trả lời thẳng câu đó (VD Tập 10: "Rửa xe 30K / Lãi bao nhiêu?"). Tránh câu chơi chữ/ẩn dụ khó hiểu nếu chưa xem video (VD "30K chỉ là cái cửa"). Nên có tên ngành hoặc con số thật để người lướt lưới nhận ra chủ đề.
- **Kiểu chữ tham khảo** (chọn linh hoạt): (a) **câu hỏi mồi** — chữ hỏi điều người xem hay nghĩ sai, hình gợi câu trả lời sai, video trả lời ngược lại (VD Tập 9: "CHỦ QUÁN SỢ GÌ NHẤT?" + hình Gấu hoảng sợ chỉ vào khách ăn khỏe; video đáp: không phải khách ăn nhiều, mà là bàn vắng); (b) câu nói ngôi thứ nhất ("TÔI GHÉT HỌC THÊM"); (c) tên tình huống/từ khoá ngắn ("BÁN CHỖ NGỒI"); (d) con số (nếu là số giả định/ước tính thì thêm dấu "?" hoặc chữ "ƯỚC TÍNH" — theo `docs/DNA.md` mục 4).
- **Cách trình bày khi chèn chữ**: chữ khổng lồ chiếm ~30-40% thumbnail, chia 2 dòng, viền đen dày, vàng hoặc trắng, **tô 1 từ khoá màu khác** (đỏ/vàng), đặt ngay trong mảng trống của cảnh (không khung nền riêng), chừa **lề ≥ 4%** với mép khung (tránh sát mép phải; góc dưới phải sẽ bị YouTube đè nhãn thời lượng).
- **Kiểm tra bắt buộc trước khi chốt (3 thứ cùng chiều)**: *hình nói gì — chữ nói gì — video nói gì*. Nếu chữ trái với thông điệp video (kể cả nhìn "hấp dẫn"), đổi chữ. Chữ dạng mồi câu hỏi được phép "hình gợi đáp án sai" **chỉ khi** video thật sự đảo lại đúng như vậy và ghi rõ ở Bước 0.
- Đề xuất 2-3 phương án chữ, mỗi phương án ghi rõ số từ và đối chiếu Bước 0, đưa người dùng chọn/chỉnh trước khi viết prompt.
- Đối chiếu nhanh với công thức thumbnail đối thủ ở `docs/chien-luoc-youtube.md` mục Benchmark — không copy bố cục y hệt, chỉ dùng để kiểm tra hướng đi hiện tại còn đúng xu hướng ngách hay không.

## Bước 3A — Viết prompt tách lớp (Cách A)
`thumbnail-prompt.txt` gồm **mỗi lớp 1 dòng**: dòng 1 = lớp Gấu, dòng 2 = lớp hoạt động chính (thêm dòng nếu cần lớp khác, VD đạo cụ khổng lồ ở tiền cảnh). Mẫu đầy đủ: `Bai-Dang/Tap 10 - Tiem Rua Xe/thumbnail-prompt.txt` (chỉ có trên máy — `Bai-Dang/` không đẩy lên Git).
- **Lớp Gấu**: mở đầu `Cartoonish illustrative character cutout, [cỡ cảnh, VD medium shot from the waist up] of the Gấu bear mascot character, isolated on a pure plain white background.` + charStyle cố định + câu chặn râu/phụ kiện + câu ghi đè biểu cảm (như mục 1 Bước 3B) + tư thế/biểu cảm cụ thể (hướng xoay người/ngón tay chỉ về phía lớp hoạt động sẽ đặt khi ghép; đạo cụ tay cầm nếu có) + câu kết flat 2D vector + `No text...` + `16:9...`.
- **Lớp hoạt động chính**: mở đầu nêu phong cách (`Photorealistic studio photograph...` hoặc flat 2D cartoon) + `isolated on a pure plain white seamless background` + tả người (người Việt, tuổi, trang phục cụ thể, biểu cảm có mặt rõ) và vật (đúng loại phổ biến ở Việt Nam hiện nay, thiết kế chung chung) + hành động đặc trưng của ngành.
- **Quy tắc nền trắng để tách nền (CỨNG — áp dụng mọi lớp):**
  1. Nền `completely flat pure white (#FFFFFF)`: không gradient, không sàn/vũng nước, không bóng đổ, không phản chiếu, không sương/tia nước mờ, không cảnh vật.
  2. Chủ thể nằm **trọn trong khung, chừa lề trắng mọi phía**, không cắt mép — kể cả phụ kiện dài (dây, vòi, cán).
  3. **Không để mảng trắng của vật thể chạm nền trắng** (công cụ tách sẽ ăn mất): đổi màu vật thể trắng (VD Tập 10: bọt tuyết trắng → bọt hồng nhạt), trang phục người tránh màu trắng; riêng Gấu (găng + áo sơ mi trắng là nhận diện, không đổi) thì thêm `a clean continuous bold black outline around the entire silhouette`.
  4. Không logo/nhãn hiệu, biển số để trống, tiền/đạo cụ có số thì để trống hoặc khoá rõ là VND (quy tắc tiền VND ở `QuyTrinh/C3-Prompt-Anh.md`).
  - Cùng nguyên tắc với icon nền trắng ở `QuyTrinh/C3-Prompt-Anh.md` Bước 3b.

## Bước 3B — Viết prompt 1 cảnh (Cách B)
Dùng lại **charStyle cố định của Gấu** ở `QuyTrinh/C3-Prompt-Anh.md` (Bước 2) — mặc định giữ đúng 1 bộ nhận diện vest xanh navy + kính lão vàng đồng (chi tiết hoá trang riêng của tập chỉ dùng nếu chính nó là điểm nhấn hài hước). Ghép prompt theo khuôn sau:

1. **Mở đầu cố định + shot**: `Cartoonish illustrative thumbnail, [shot type] focusing on the Gấu bear mascot character.` + dán nguyên văn charStyle cố định + câu chặn `no beard, no mustache, no extra facial hair, no extra accessories, no clothing details beyond what is explicitly described above.` + **câu ghi đè biểu cảm** (`IMPORTANT: the eye shape, eyebrow angle, and mouth shape described above are Gau's default resting state ONLY — the extreme expression described below MUST clearly override this default.`). `[shot type]`: tilted Dutch-angle medium close-up / dramatic low-angle close-up / extreme close-up dynamic shot (kiểu cực đoan), hoặc medium close-up/wide shot (kiểu thường).
2. **Tả Gấu chi tiết**: chiếm bao nhiêu % khung, nghiêng bao nhiêu độ, biểu cảm cụ thể từng bộ phận (mắt, mày, miệng, răng vàng), tư thế tay (ghi "rounded fingertips"), điểm nhấn nhỏ.
3. **Bối cảnh + lớp chiều sâu** (theo Bước 1): bối cảnh chính là tình huống của tiêu đề, nêu rõ vật ở tiền cảnh (mờ) và hậu cảnh; luôn là không gian Việt Nam; người phụ tả đầy đủ mặt/biểu cảm (`absolutely no black silhouettes or faceless figures`).
4. **Chừa mảng chữ**: 1 khoảng liền mạch, phẳng, sạch (VD `the upper-right 40 percent of the frame is a clean, open, flat warm coral-orange wall area with nothing important in it`) ở phía đối diện Gấu để chèn chữ tay sau; không mô tả là "vùng dành cho chữ".
5. **Câu kết**: `The entire image should have a distinct, flat 2D vector cartoon style with clean bold black outlines and minimal flat color fill — not photorealistic, not a cinematic render.` + màu (kiểu thường: `Navy blue and gold-bronze color palette`; kiểu cực đoan: `bold saturated warm [coral-red/orange] background with navy blue and gold-bronze accents on the character`) + `strong color contrast between the character and the background` + `No text, letters, numbers or writing anywhere in the image.` + `16:9 widescreen aspect ratio, landscape orientation.`

**Sau khi gen, bắt buộc kiểm tra** (cả 2 cách): (1) Gấu đúng phong cách flat 2D vector, đúng charStyle (mắt/kính vàng đồng/vest navy/răng vàng — không lệch màu/chi tiết); (2) Cách B: mảng trống chừa chữ sạch, đủ chỗ — Cách A: nền trắng sạch, chủ thể không bị cắt mép, không có mảng trắng dính nền; (3) không tự sinh chữ/ký tự lạ; (4) **hình có nói cùng chiều với thông điệp ở Bước 0 không** (VD hình khách ăn khỏe + chữ "sợ ngày vắng" là lệch). Lỗi phải gen lại (Cách A chỉ gen lại đúng lớp lỗi).

## Bước 3.5 — Tách nền + ghép (chỉ Cách A)
1. **Tách nền** từng lớp bằng `Cong-Cu/remove-bg` (`python app.py`, kéo thả ảnh, sửa tay chỗ sót bằng Tẩy/Khôi phục, tải PNG) — cùng công cụ dùng cho icon ở `QuyTrinh/C4-Doi-ten-Kiem-tra-Anh.md` Bước 2. Lưu bản tách nền cạnh ảnh gốc: `thumb-gau.png`, `thumb-hoat-dong.png`.
2. **Người dùng tự ghép** (Photoshop/Canva): ảnh bối cảnh làm tối/mờ nhẹ → đặt lớp hoạt động + Gấu (Gấu tràn khung 40-55%, ngón tay/ánh nhìn hướng vào lớp hoạt động) → thêm **viền sáng mảnh quanh từng chủ thể** để tách khỏi nền tối → vài điểm nhấn nhỏ (hạt lấp lánh...) → chừa **1 dải trống liền mạch cho chữ** (Tập 10: dải trên cùng).
3. **Claude kiểm tra bản ghép (CỨNG)** trước khi chèn chữ: đạo cụ tiền phải nhìn ra **VND** (lỗi thật Tập 10: tờ tiền Gấu cầm trắng xám, có chân dung — trông như đô la → chỉnh màu sang xanh dương/nâu vàng như tờ VND); không sót lớp thừa (ô trắng/khung chữ trống còn sót khi ghép); không logo/nhãn hiệu thật lộ ra từ ảnh bối cảnh; chủ thể không lẫn vào nền.

## Bước 4 — Quy cách kỹ thuật
- Kích thước xuất: **1280×720px** (16:9, chuẩn YouTube), dung lượng **dưới 2MB**, JPG/PNG. Ảnh gen/bản làm việc lớn hơn (VD 8000×4500, >5MB) phải thu nhỏ.
- Tông màu: kiểu thường giữ xanh navy (#0C447C) - vàng đồng (#BA7517) theo `docs/Style-Guide-goc.md` mục 6; kiểu cực đoan cho phép nền ấm bão hoà nhưng **Gấu luôn giữ vest navy + kính vàng đồng** để nhận diện thương hiệu nhất quán qua các tập.

## Bước 4.5 — Định dạng file prompt
`thumbnail-prompt.txt`: mỗi prompt viết thành **1 dòng duy nhất** (không xuống dòng giữa các đoạn) — dễ copy-paste nguyên khối. Khi còn đang thử nhiều biến thể thì mỗi biến thể 1 dòng; **chốt xong chỉ giữ đúng dòng đã dùng** — Cách B còn 1 dòng, Cách A còn mỗi lớp 1 dòng theo thứ tự lớp Gấu → lớp hoạt động → lớp khác (nếu có).

## Bước 5 — Kiểm tra thu nhỏ (bắt buộc trước khi chốt)
Thu nhỏ bản làm việc xuống **360px và 168px bề ngang** (360px ≈ cỡ thumbnail ở trang chủ/lưới video, 168px ≈ cỡ ở cột video gợi ý — phần lớn người xem thấy thumbnail ở 2 cỡ này) rồi xem lại: chữ vẫn đọc được, từ tô màu vẫn nổi, biểu cảm Gấu đọc được trong nửa giây, hình–chữ–video cùng chiều (Bước 2). Chữ đỏ trên nền cam/đỏ, hoặc trên nền xám tối, dễ kém tương phản (lỗi thật Tập 10: "30K" đỏ trên nền đường phố tối bị chìm ở 168px) — ưu tiên tô từ khoá màu **vàng**, hoặc giữ đỏ nhưng thêm viền trắng/đen dày; khối chữ nên chiếm ~30-40% khung, nhỏ hơn thì phóng to. Không đạt → sửa lại chữ/bố cục trước khi qua Bước 6.

## Bước 6 — Lưu file
Lưu prompt đã chốt vào `Bai-Dang/Tap N - [tên]/thumbnail-prompt.txt`; ảnh gen ra (KHÔNG chữ) lưu thành `thumb-gau.jpg` + `thumb-hoat-dong.jpg` (bản tách nền `.png` cùng tên) với Cách A, hoặc `thumbnail-nen.jpg` với Cách B; người dùng chèn chữ ra bản làm việc rồi **xuất `thumbnail.jpg` 1280×720 (<2MB)** trước khi qua `C8-Dang-bai.md`. Claude xem lại bản có chữ theo Bước 3B (kiểm tra sau khi gen), Bước 3.5 (kiểm tra bản ghép) và Bước 5 rồi nhận xét trước khi chốt; nếu người dùng gửi bản làm việc kích thước lớn, Claude xuất giúp `thumbnail.jpg` đúng quy cách.

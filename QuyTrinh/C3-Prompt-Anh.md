# C3 — Viết Prompt Ảnh

> Đầu vào: `scene-list.md` (từ C2, đã chia scene đầy đủ) + `script.md`/`voice-script.txt` (C1).
> Đầu ra: `prompt-anh.txt` (1 dòng = 1 prompt hoàn chỉnh) + ảnh trong `Anh Video/` của thư mục tập.
> Ghi nhớ: kênh dùng **ảnh tĩnh, cắt cứng giữa các ảnh** (KHÔNG zoom/pan, không chuyển động bên trong ảnh) — đúng định dạng đã chốt ở `docs/DNA.md` mục 1. Nguồn style/nhân vật gốc: `docs/Visual-Prompts-goc.md` (charStyle, bgStyle, masterPrompt mẫu). Việc chia scene đã làm xong ở `QuyTrinh/C2-Chia-Scene.md` — KHÔNG tự chia lại ở bước này, chỉ dựng prompt chi tiết cho từng scene đã có sẵn trong `scene-list.md`.

## Nguyên tắc viết prompt (bắt buộc)
- Viết prompt bằng **tiếng Anh**.
- **Mascot Gấu KHÔNG BAO GIỜ bỏ** (khác kênh chị em `TruyenTuDuy`) — xuất hiện trong đa số scene vì Gấu là người dẫn chuyện trực tiếp phân tích số liệu, chỉ bỏ Gấu ở scene thuần minh hoạ bối cảnh/biểu đồ trừu tượng không cần nhân vật bình luận.
- Bối cảnh chia 2 nhóm theo `docs/Visual-Prompts-goc.md` mục 2 (bgStyle): (1) nền phẳng minh hoạ (tòa nhà công ty, biểu đồ, mô hình kinh doanh) và (2) nền ảnh thật đường phố/văn phòng/quán xá Việt Nam mờ nhẹ để Gấu nổi bật. Mọi bối cảnh đời thực đều phải đẩy hẳn sang Việt Nam (xe máy, biển hiệu, quán vỉa hè, nội thất Việt quen thuộc) — không dùng bối cảnh phương Tây chung chung.

## Bước 1 — Chọn cảnh cho từng scene
Với mỗi scene trong `scene-list.md`:
- Minh hoạ đúng nội dung đoạn đó (Gấu đang tính toán/chỉ vào biểu đồ/dò xét qua kính, hoặc hình ảnh biểu tượng cho khoản chi phí/mô hình đang giải thích).
- Giữ **charStyle + sceneStyle cố định, tái sử dụng nguyên văn trong mọi prompt của tập** (`docs/Visual-Prompts-goc.md` mục 1 và 3) để cả bộ ảnh không bị rời rạc khi ghép lại.
- **Áp dụng quy tắc 30 độ (30-degree rule)**: 2 ảnh liên tiếp của CÙNG 1 chủ thể phải đổi góc camera tối thiểu ~30 độ HOẶC đổi cỡ cảnh rõ rệt (toàn cảnh → cận cảnh). Luân phiên các loại góc quay (toàn cảnh, trung cảnh, cận mặt, cận tay/vật dụng, góc nghiêng, góc thấp, góc cao, qua vai, cận vật thể) sao cho 2 ảnh cạnh nhau không cùng loại/cùng cỡ cảnh.
- Đánh dấu riêng 1-2 scene có bố cục bắt mắt nhất (Gấu rõ nét, có vùng trống để đè chữ) làm ứng viên thumbnail — xem `QuyTrinh/C6-Thumbnail.md`.

## Bước 2 — Viết prompt

> **Phân biệt rõ 2 loại yếu tố:**
> - **CỐ ĐỊNH xuyên suốt mọi tập** (không đổi): charStyle của Gấu (đầu to tròn, mắt híp, vest xanh navy `#0C447C`, kính lão gọng tròn vàng đồng `#BA7517`), sceneStyle (flat 2D cartoon, viền đen dày 3-4px).
> - **THAY ĐỔI theo từng tập/scene**: bối cảnh/địa điểm cụ thể (quán trà sữa, phòng gym, văn phòng ngân hàng, đường phố Việt Nam...) theo đúng ngành nghề tập đó, KHÔNG lặp lại y hệt 1 bối cảnh cho mọi tập.
>
> **Cảnh báo lỗi thường gặp:** vì mọi prompt đều tái sử dụng 1 charStyle cố định, rất dễ vô tình lặp lại gần như y hệt bối cảnh cho nhiều scene khác nhau trong cùng 1 tập. **Trước khi xuất `prompt-anh.txt`, rà lại toàn bộ danh sách bối cảnh của các scene trong CÙNG 1 tập** — đổi sang góc không gian/đồ vật khác nhau (quầy thu ngân, kho hàng, bàn làm việc, biển hiệu ngoài cửa, ghế chờ khách...) trừ khi nội dung thật sự tiếp diễn cùng 1 khoảnh khắc.

> **Character Lock — KHÔNG BAO GIỜ rút gọn**: khi viết prompt cho ảnh cận cảnh/crop hẹp, không được tự ý cắt bớt cụm mô tả cố định của Gấu (đặc biệt kính lão + mắt híp + vest xanh navy) để "cho gọn" — luôn dán ĐẦY ĐỦ nguyên văn charStyle, kể cả khi prompt đã dài. Ngoại lệ DUY NHẤT: nếu khung hình thật sự cắt cụt phần đó theo bố cục, phải ghi rõ lý do trong prompt (VD "cropped below the eyes so the glasses are not visible in this shot") thay vì âm thầm bỏ mô tả.
> **Chặn AI tự vẽ thêm chi tiết lạ không có trong mô tả** — mọi prompt PHẢI có câu chặn tường minh ngay sau mô tả nhân vật: "no beard, no mustache, no extra facial hair, no extra accessories, no clothing details beyond what is explicitly described above". Sau khi gen ảnh, kiểm tra kỹ ở bước QA (`C4-Doi-ten-Kiem-tra-Anh.md`) xem Gấu có bị vẽ thêm chi tiết lạ không (VD tự thêm râu, đổi màu vest), gen lại riêng ảnh đó nếu có.

**charStyle cố định** (dán nguyên văn mọi prompt có Gấu — lấy từ `docs/Visual-Prompts-goc.md` mục 1):
```
Bear cartoon character, stylized 2D style similar to meme mascot characters, large round head taking up about 40% of the body, chubby round body shape, dark brown/black fur color (#4A3728-like). Half-moon shaped squinty eyes, small sparkling black pupils giving a sly/cunning impression (distinct from big round bulging eyes), slightly slanted eyebrows creating a scrutinizing expression. Moderately wide mouth, light brown lips, usually smirking rather than open-mouthed. Small black triangular nose. Simplified cartoon limb structure, rounded 3-4 finger hands in a darker brown than the body, no clearly detailed claws. Outfit: dark navy blue business suit vest (#0C447C), navy or black bow tie, white dress shirt, round gold-bronze reading glasses (#BA7517) — the glasses are the key identifying detail. Thick even black outline strokes about 3-4px, flat shading with minimal gradient, occasional light shading for fabric fold volume. No beard, no mustache, no extra facial hair, no extra accessories, no clothing details beyond what is explicitly described above.
```

**sceneStyle cố định** (dán nguyên văn mọi prompt):
```
Flat 2D cartoon style, thick even black outline 3-4px, flat coloring with minimal gradient, large round head chubby body taking up ~40% of the body, sly squinty eyes instead of bulging eyes, blend of flat illustrated backgrounds and photo-realistic backgrounds, primary color palette navy blue - gold bronze - white - black.
```

Với mỗi scene, viết 1 prompt hoàn chỉnh gồm: sceneStyle + charStyle (nếu có Gấu trong scene) + **bối cảnh cụ thể của scene đó** (địa điểm rõ ràng, có đồ vật/ánh sáng/chi tiết không gian thật kiểu Việt Nam) + tư thế/hành động của Gấu (nheo mắt tính toán, chỉ tay vào biểu đồ, cười khẩy, khoanh tay...) + chi tiết minh hoạ ý của đoạn. Áp dụng các quy tắc kỹ thuật sau cho MỌI prompt:
- **Cho phép AI vẽ chữ TRONG bối cảnh khi thật sự cần** (bảng hiệu quán, màn hình máy tính hiển thị số liệu, biểu đồ có nhãn) — chỉ ghi rõ nguyên văn nội dung chữ và yêu cầu đọc rõ được khi chữ đó **đủ lớn/đủ gần khung hình để người xem thực sự đọc được**. **Nội dung chữ luôn phải là tiếng Việt, không dùng tiếng Anh** (VD "Giá vốn", "Lãi ròng" thay vì "COGS", "Net profit" — trừ khi bản thân video có nhắc thuật ngữ tiếng Anh đó).
- **Chữ nhỏ/ở xa**: mô tả là chữ mờ/không đọc rõ — dùng cụm "small blurry illegible text, not meant to be readable" thay vì ép AI viết chính xác.
- **Ngay cả khi chữ đủ to/là tiêu điểm chính, vẫn rút ngắn tối đa nội dung** (lý tưởng 3-6 từ) — câu càng dài, AI càng dễ vẽ sai chính tả/dấu.
- Sau khi gen ảnh, kiểm tra kỹ các đoạn chữ được yêu cầu đọc rõ có đúng chính tả/dấu tiếng Việt không, phát hiện lỗi phải gen lại riêng ảnh đó (theo `C4-Doi-ten-Kiem-tra-Anh.md`).
- **Vẫn BẮT BUỘC chặn chữ/logo NGẪU NHIÊN không được mô tả** — câu chặn cuối mỗi prompt phải nêu rõ: chỉ được xuất hiện chữ nếu đã mô tả tường minh ở trên, cấm mọi chữ/logo khác.
- **Tránh dùng từ "grid"/"grid line"** khi mô tả bố cục theo quy tắc 1/3 — mô tả vị trí chủ thể bằng lời thường (VD "positioned roughly one third of the way in from the right edge, not centered") và thêm câu chặn "no visible grid lines or ruler marks anywhere in the image".
- **Bắt buộc ghi rõ vị trí chủ thể trong khung ở MỌI prompt** — áp dụng quy tắc 1/3, đa số scene đặt Gấu lệch trái hoặc lệch phải khung hình, chỉ để giữa khung khi thật sự cần nhấn mạnh (hook mở đầu nhìn thẳng camera, khoảnh khắc cao trào/thumbnail). Luân phiên lệch trái/lệch phải giữa các scene liên tiếp.
- **Cách chừa vùng trống cho chữ (chỉ áp dụng cho scene ứng viên thumbnail):** mô tả không gian liền mạch tự nhiên, chỉ dồn Gấu về giữa-phải hoặc giữa-trái, phần còn lại đơn giản không đặt thêm đồ vật — không mô tả vùng trống như 1 mảng tách rời.
- Mỗi prompt kết thúc bằng câu chặn: `no random or unrelated text, letters, numbers, or logos anywhere in the image beyond what is explicitly described above, no random unrelated objects beyond what is described above`.

## Bước 3 — Xuất `prompt-anh.txt`
1 file `prompt-anh.txt` (text thường) — **mỗi dòng = 1 prompt hoàn chỉnh của 1 ảnh, nằm gọn trên 1 dòng** (không xuống dòng giữa chừng 1 prompt), **đúng thứ tự ảnh 001→0NN** khớp `scene-list.md`, không có dòng trống xen giữa, không có số thứ tự/tiêu đề ở đầu dòng.

**Vị trí lưu file**: lưu trực tiếp ở gốc `Bai-Dang/Tap N - [tên]/prompt-anh.txt` — **KHÔNG** để trong thư mục con `Anh Video/` (thư mục đó chỉ chứa ảnh output, không chứa file prompt).

Ngay sau khi xuất xong `prompt-anh.txt`, **tạo sẵn thư mục rỗng `Bai-Dang/Tap N - [tên]/Anh Video/`** để người dùng có chỗ lưu ảnh ngay khi gen xong, không phải tự tạo tay.

## Bước 4 — Tạo ảnh & đổi tên
Tạo ảnh từ `prompt-anh.txt`, lưu vào `Bai-Dang/Tap N - [tên]/Anh Video/`. Sau đó thực hiện đổi tên + kiểm tra chất lượng theo `QuyTrinh/C4-Doi-ten-Kiem-tra-Anh.md` trước khi qua bước timing/xuất clip.

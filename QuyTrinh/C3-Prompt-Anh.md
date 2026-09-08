# C3 — Viết Prompt Ảnh

> Đầu vào: `scene-list.md` (từ C2, đã chia scene đầy đủ) + `script.md`/`voice-script.txt` (C1).
> Đầu ra: `prompt-anh.txt` (1 dòng = 1 prompt hoàn chỉnh) + ảnh trong `Anh Video/` của thư mục tập.
> Ghi nhớ: kênh dùng **ảnh tĩnh, cắt cứng giữa các ảnh** (KHÔNG zoom/pan, không chuyển động bên trong ảnh) — đúng định dạng đã chốt ở `docs/DNA.md` mục 1. Nguồn style/nhân vật gốc: `docs/Visual-Prompts-goc.md` (charStyle, bgStyle, masterPrompt mẫu). Việc chia scene đã làm xong ở `QuyTrinh/C2-Chia-Scene.md` — KHÔNG tự chia lại ở bước này, chỉ dựng prompt chi tiết cho từng scene đã có sẵn trong `scene-list.md`.

## Nguyên tắc cứng (bắt buộc, không đổi giữa các tập)
- Viết prompt bằng **tiếng Anh**.
- **Mascot Gấu KHÔNG BAO GIỜ bỏ**, trừ scene thuần đồ hoạ/số liệu không cần nhân vật bình luận.
- **charStyle Phần A (nhận diện — đầu, mắt híp, vest xanh navy, kính, răng vàng) phải dán nguyên văn mọi prompt có Gấu, không rút gọn**, kể cả ảnh cận cảnh/crop hẹp. Ngoại lệ duy nhất: khung hình thật sự cắt cụt 1 phần theo bố cục thì ghi rõ lý do trong prompt thay vì âm thầm bỏ mô tả. **KHÔNG dán Phần B (tư thế mặc định của bảng reference sheet gốc)** vào prompt scene thật — Phần B chỉ dùng khi gen lại chính bảng reference sheet.
- Mỗi prompt có Gấu phải có câu chặn ngay sau mô tả nhân vật: `no beard, no mustache, no extra facial hair, no extra accessories, no clothing details beyond what is explicitly described above`.
- Mỗi prompt kết thúc bằng câu chặn chữ/vật thể lạ: `no random or unrelated text, letters, numbers, or logos anywhere in the image beyond what is explicitly described above, no random unrelated objects beyond what is described above, no visible grid lines or ruler marks anywhere in the image`.
- Mọi chữ đọc được trong ảnh phải là **tiếng Việt** hoặc số/ký hiệu tiền tệ — cấm AI tự bịa chữ tiếng Anh dù chung chung (VD "revenue", "profit").
- **Quy tắc 30 độ**: 2 ảnh liên tiếp của cùng 1 chủ thể phải đổi góc camera tối thiểu ~30 độ hoặc đổi cỡ cảnh rõ rệt — không để 2 ảnh cạnh nhau giống hệt bố cục.
- **Không tái dùng y hệt 1 ảnh/bối cảnh đã gen cho tập trước sang tập khác** — YouTube coi là "reused content", có thể bị hạn chế phân phối/kiếm tiền dù ảnh tự tạo miễn phí. Mỗi tập cần bối cảnh/góc quay dàn dựng riêng, dù dùng chung charStyle/sceneStyle cố định của Gấu.
- Toàn bộ ảnh luôn là **1 ảnh AI gen thuần tuý trong 1 phong cách nhất quán** theo bgStyle (`docs/Visual-Prompts-goc.md` mục 2) — KHÔNG tách lớp/ghép ảnh chụp thật ngoài đời, KHÔNG hiệu ứng xoá phông/phủ đen phức tạp.

## Kinh nghiệm thực tế khi viết prompt (rút ra từ thử nghiệm, cân nhắc linh hoạt theo từng scene — không phải checklist ép đủ mọi mục)
- **Bối cảnh phải cụ thể/chi tiết, không mô tả chung chung** (VD "quầy pha chế inox, ly nhựa xếp chồng, bảng giá viết tay dán băng keo" thay vì chỉ "quán trà sữa") — mô tả mơ hồ kiểu "shop backdrop" dễ khiến AI tự chọn nhầm loại bối cảnh khác hẳn (tiệm đồng hồ, bàn văn phòng...) không liên quan ngành nghề tập, phải khoá rõ đúng ngành nghề mỗi khi tả bối cảnh mờ phía sau.
- **Ưu tiên nền phong-cách-ảnh-thật (mờ nhẹ phía sau) hơn nền phẳng đơn sắc cho scene có Gấu**, kể cả cận cảnh — chỉ dùng nền phẳng 1 màu khi thật sự không có bối cảnh nào hợp lý.
- Chữ trong ảnh: cho phép AI vẽ chữ khi thật sự cần (biển hiệu, bảng số liệu) nhưng **rút ngắn tối đa 3-6 từ** — câu càng dài càng dễ sai chính tả/dấu; chữ nhỏ/ở xa thì mô tả mờ không đọc được thay vì ép đọc rõ. Sau khi gen, kiểm tra chính tả chữ được yêu cầu đọc rõ ở bước QA (`C4-Doi-ten-Kiem-tra-Anh.md`), gen lại riêng ảnh nếu sai.
- **Tránh icon dạng biểu tượng cảnh báo phổ biến kiểu logo** (tia chớp, dấu chấm than trong tam giác...) — dễ bị hệ thống lọc bản quyền/IP hiểu nhầm là nhãn hiệu có sẵn, gây từ chối tạo ảnh khó đoán mà đổi câu chữ khác trong cùng prompt không sửa được; phải đổi hẳn cách diễn đạt cảnh báo (qua biểu cảm/tư thế) mới hết.
- **Tránh bố cục "split composition" (cắt đôi khung hình đúng qua thân nhân vật)** — AI xử lý kém, dễ cắt lìa/lệch màu nhân vật. Cần thể hiện tương phản trước/sau thì đặt nhân vật nguyên vẹn 1 bên, phần tương phản chỉ nằm ở hậu cảnh.
- **Tránh bố cục "cực cận + cắt cúp 1 phần mặt nhân vật"** — có vẻ dễ bị kiểm duyệt từ chối nhầm hơn cỡ cảnh thấy trọn đầu/vai; ưu tiên cận vừa (medium close-up) khi cần tiêu điểm biểu cảm.
- **Khi tay/chi tiết cận cảnh là tiêu điểm chính, nhắc lại tường minh quy tắc nhận diện quan trọng ngay trong mô tả tư thế của scene đó** (VD "rounded fingertips, no claws") — chỉ dựa vào charStyle chung ở đầu prompt không đủ, càng cận cảnh AI càng dễ tự vẽ lệch.
- Tránh dùng từ "grid"/"grid line" khi mô tả bố cục 1/3 — mô tả vị trí bằng lời thường (VD "positioned roughly one third from the right edge, not centered") kèm câu chặn không có đường kẻ lưới.
- Ghi rõ vị trí chủ thể trong khung ở mọi prompt theo quy tắc 1/3 (đa số lệch trái/phải, luân phiên giữa các scene liên tiếp), chỉ để giữa khung khi cần nhấn mạnh (hook mở đầu, thumbnail).

## Bước 1 — Chọn cảnh cho từng scene
Với mỗi scene trong `scene-list.md`:
- Minh hoạ đúng nội dung đoạn đó. Gấu đóng vai trò như 1 "phóng viên" đứng tại hiện trường minh hoạ (tính toán/chỉ vào biểu đồ/dò xét qua kính...).
- **Scene thuần biểu đồ/số liệu/so sánh**: nếu có Gấu thì để biểu cảm đơn giản, trọng tâm dồn vào nội dung minh hoạ chứ không phải Gấu. Chỉ bỏ hẳn Gấu khi cảnh thật sự không cần ai đứng cạnh.
- Đánh dấu riêng 1-2 scene có bố cục bắt mắt nhất (Gấu rõ nét, có vùng trống để đè chữ) làm ứng viên thumbnail — xem `QuyTrinh/C6-Thumbnail.md`.
- Trước khi xuất `prompt-anh.txt`, rà lại toàn bộ danh sách bối cảnh của các scene trong CÙNG 1 tập — đổi góc không gian/đồ vật khác nhau, trừ khi nội dung thật sự tiếp diễn cùng 1 khoảnh khắc.

## Bước 1.5 — Hoá trang theo tập (tuỳ chọn sáng tạo, chỉ làm khi cần)
Mặc định Gấu giữ nguyên vest xanh navy mọi tập. Nếu tập này có 1 tình huống đủ hợp để Gấu hoá thân thành nhân vật trong câu chuyện (VD nhân viên pha chế, khách hàng, tài xế...) và thấy đáng làm để tăng sức hút, hỏi người dùng xác nhận trước khi làm. Nếu đồng ý:
1. Viết 1 prompt "ảnh tham chiếu hoá trang" riêng cho tập này: giữ nguyên phần nhận diện gương mặt (đầu, mắt híp, răng vàng, màu lông), chỉ đổi trang phục/đạo cụ theo vai diễn — sinh reference sheet tương tự `Fanpage-Asset/gau_mascot.jpg` gốc.
2. Lưu vào `Bai-Dang/Tap N - [tên]/gau-hoa-trang-ref.jpg`, dùng làm tham chiếu xuyên suốt cho MỌI scene hoá trang trong tập đó.
3. Các scene khác trong CÙNG tập không cần hoá trang vẫn có thể quay lại vest gốc — không bắt buộc hoá trang xuyên suốt cả video.

## Bước 1.6 — Kho kỹ thuật hình ảnh làm ảnh tĩnh sống động (chọn linh hoạt theo scene, không phải quay vòng cố định)
Ảnh tĩnh không animation/zoom/pan, nên "sức sống thị giác" phải đến từ góc máy, bố cục, ánh sáng — không lặp mãi 1 kiểu đứng thẳng nhìn thẳng camera. Đây là kho lựa chọn, mỗi scene tự cân nhắc dùng gì, không ép đủ mọi kỹ thuật vào 1 tập và không dùng đúng 1 trình tự cố định giữa các tập:

**Cỡ cảnh:** đại cảnh/thiết lập → toàn cảnh → trung cảnh → cận vừa → cận mặt → cực cận đặc tả (mắt, tay, chi tiết vật thể/con số).

**Góc máy — chọn theo cảm xúc muốn tạo:** ngang tầm mắt (trung tính); góc thấp ngước lên (uy quyền/áp lực, hợp chi phí lớn/rủi ro); góc cao nhìn xuống (nhỏ bé/bất lực, hợp thất bại/thua lỗ); góc nghiêng lệch trục (bất ổn, hợp rủi ro/bất thường); góc chim bay (tổng quan mô hình/sơ đồ); qua vai (quan sát 1 tình huống).

**Bố cục tạo cảm giác chuyển động dù ảnh đứng yên:** đường chéo dẫn mắt thay vì đối xứng tĩnh; lấy khung qua 1 lớp tiền cảnh mờ; dáng đứng như "đóng băng giữa chuyển động" (đang bước, tay đang vung) thay vì đứng yên hoàn toàn; tương phản sáng-tối/rim light tách lớp chủ thể khỏi nền.

Cross-check với quy tắc 30 độ: khi luân phiên góc/cỡ cảnh giữa các scene liên tiếp, ưu tiên lấy từ kho kỹ thuật này thay vì chỉ đổi qua đổi lại 2-3 kiểu quen thuộc.

## Bước 2 — Viết prompt

**charStyle cố định — CHỈ phần nhận diện (Phần A), dán nguyên văn mọi prompt có Gấu, KHÔNG kèm tư thế mặc định — lấy từ `docs/Visual-Prompts-goc.md` mục 1:**
```
Bear cartoon character, stylized 2D style similar to meme mascot characters, moderately large round head taking up about 30% of the body, tall and lean build with a dignified, statuesque stance (not chubby/rotund, not short/squat — long legs, confident posture like a distinguished gentleman). Consistent solid dark chocolate-brown fur color (hex approx #4A3728, a deep rich brown — NOT light tan, NOT caramel, NOT near-black) applied identically in every image. Half-moon shaped squinty eyes, small sparkling black pupils giving a sly/cunning impression (distinct from big round bulging eyes), slightly slanted thick eyebrows creating a scrutinizing expression. Moderately wide mouth, light brown lips, usually smirking with a single glinting gold tooth visible on one side — Gau's signature quirky detail. Small black triangular nose. Simplified cartoon limb structure, slender long arms and legs, rounded 3-4 finger hands in a darker brown than the body, no clearly detailed claws. Outfit: sharp, well-tailored dark navy blue business suit with vest fitted close to the body (#0C447C), navy or black bow tie, crisp white dress shirt, round gold-bronze reading glasses (#BA7517) — the glasses and the gold tooth are the key identifying details. Thick even black outline strokes about 3-4px, flat shading with minimal gradient, occasional light shading for fabric fold volume. Overall silhouette should feel tall, polished, and authoritative with a hint of mischief — rather than short, stiff, or cartoonishly round. No beard, no mustache, no extra facial hair, no extra accessories, no clothing details beyond what is explicitly described above.
```

Sau đoạn charStyle trên, mỗi prompt PHẢI viết tiếp riêng 1 cụm mô tả **tư thế + biểu cảm dành riêng cho scene đó** — không để trống, không tái dùng y hệt cụm tư thế của scene khác trong cùng 1 tập. Biểu cảm nên phong phú/hơi phóng đại kiểu meme theo nội dung từng đoạn (mắt trợn kinh ngạc, cười sằng sặc, ôm đầu giả vờ đau khổ...) thay vì mặc định lặp lại 1 dáng.

**sceneStyle cố định (dán nguyên văn mọi prompt):**
```
Flat 2D cartoon style, thick even black outline 3-4px, flat coloring with minimal gradient, moderately large round head on a tall, lean, statuesque body taking up ~30% of the body, sly squinty eyes instead of bulging eyes, blend of flat illustrated backgrounds and photo-realistic backgrounds, primary color palette navy blue - gold bronze - white - black.
```

Mỗi prompt hoàn chỉnh = sceneStyle + charStyle (nếu có Gấu) + bối cảnh cụ thể + tư thế/hành động + chi tiết minh hoạ ý của đoạn, áp dụng đủ các nguyên tắc cứng và kinh nghiệm ở trên.

## Bước 3 — Xuất `prompt-anh.txt`
1 file `prompt-anh.txt` (text thường) — **mỗi dòng = 1 prompt hoàn chỉnh của 1 ảnh, nằm gọn trên 1 dòng** (không xuống dòng giữa chừng 1 prompt), **đúng thứ tự ảnh 001→0NN** khớp `scene-list.md`, không có dòng trống xen giữa, không có số thứ tự/tiêu đề ở đầu dòng.

**Vị trí lưu file**: lưu trực tiếp ở gốc `Bai-Dang/Tap N - [tên]/prompt-anh.txt` — **KHÔNG** để trong thư mục con `Anh Video/` (thư mục đó chỉ chứa ảnh output, không chứa file prompt).

Ngay sau khi xuất xong `prompt-anh.txt`, **tạo sẵn thư mục rỗng `Bai-Dang/Tap N - [tên]/Anh Video/`** để người dùng có chỗ lưu ảnh ngay khi gen xong, không phải tự tạo tay.

## Bước 4 — Tạo ảnh & đổi tên
Tạo ảnh từ `prompt-anh.txt`, lưu vào `Bai-Dang/Tap N - [tên]/Anh Video/`. Sau đó thực hiện đổi tên + kiểm tra chất lượng theo `QuyTrinh/C4-Doi-ten-Kiem-tra-Anh.md` trước khi qua bước timing/xuất clip.

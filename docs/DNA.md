# DNA.md — Định vị kênh "Gấu Tinh Ranh"

> File này để Claude đọc đầu tiên mỗi phiên làm việc. Nội dung gốc do người dùng cung cấp ở 3 file:
> `docs/Channel-DNA-goc.md`, `docs/Style-Guide-goc.md`, `docs/Chu-De-goc.md`, `docs/Visual-Prompts-goc.md` — file này ĐÚC KẾT lại thành bản dùng vận hành hàng ngày. Khi có mâu thuẫn, ưu tiên file gốc (do người dùng chốt).

## 1. Ngách
Kênh phân tích **mô hình kiếm tiền/lỗ lãi thật của các ngành nghề/dịch vụ đời thường Việt Nam** (quán trà sữa, tiệm rửa xe, phòng gym, tài xế công nghệ, cầm đồ online, bảo hiểm nhân thọ...) và các quyết định tài chính cá nhân phổ biến (vay mua nhà, vay tiêu dùng, thẻ tín dụng...) — bóc tách COGS, chi phí cố định, điểm hoà vốn, chi phí ẩn mà người ngoài ít nghĩ tới. Giọng kể tinh ranh/mỉa mai nhẹ qua nhân vật mascot "Gấu". Định dạng: **ảnh tĩnh + voice**, không animation.

Kênh có identity nhân vật, bảng màu và chủ đề riêng, tập trung trọn vẹn vào tài chính/kinh doanh bình dân.

## 2. Persona — Gấu (Gấu Tinh Ranh)
Gấu từng là "tay chơi" quan sát đủ loại mô hình kiếm tiền ngoài đời — từ quán xá vỉa hè đến ngân hàng lớn — nên chẳng còn lạ gì mấy trò "vẽ vời" của người làm ăn. Giờ Gấu khoác vest lịch sự, kể lại cho anh em nghe sự thật đằng sau từng đồng tiền, không giấu giếm, không nể nang.

**5 tính cách:** tinh ranh nhìn thấu bản chất; hài hước mỉa mai nhẹ (không cợt nhả quá đà); thẳng thắn không nể nang; tự tin nhưng gần gũi; hoài nghi tinh quái khi đặt câu hỏi.

**Ngôi kể:** thứ nhất — Gấu xưng "tôi", gọi khán giả là "anh em".

**Ngoại hình:** gấu nâu, dáng tròn/mềm kiểu mascot-comic, đầu to hơn thân ~40-45% (cập nhật — trước đây cao gầy ~30%), mắt híp bán nguyệt (tinh ranh, KHÔNG đổi sang mắt to tròn), nhếch mép cười khẩy lộ răng vàng, tay đeo găng trắng kiểu cartoon cổ điển (cập nhật), vest xanh navy (#0C447C) + nơ bướm + kính lão gọng tròn vàng đồng (#BA7517) — chi tiết nhận diện riêng, cho phép biểu cảm phóng đại mạnh hơn trước. Chi tiết đầy đủ ở `docs/Visual-Prompts-goc.md`.

## 3. Cấu trúc video (khung lõi MẶC ĐỊNH — bắt buộc theo thứ tự, trừ khi người dùng chọn khung tự do, xem quy tắc cứng bên dưới)
1. **Hook mở đầu** (0-15s) — nêu nghịch lý/câu hỏi cụ thể kèm số liệu (VD "Ly trà sữa 25.000đ, tưởng lãi đậm lắm chứ gì?").
2. **Disclaimer ngắn cố định** (đặt ngay sau hook, nguyên văn mục 5).
3. **Bối cảnh ngành/hiện tượng** — giới thiệu mô hình đang phân tích.
4. **Bóc tách COGS + chi phí cố định** — giải thích ngay mọi thuật ngữ tài chính vừa nhắc.
5. **Điểm hoà vốn + chi phí ẩn/cơ hội** — dùng câu nối chuyển cảnh cố định: "Giờ mới đến khúc xương khó nhằn đây..."
6. **Kết luận bài học tài chính + catchphrase kết** (nguyên văn mục 5).

Thứ tự 6 bước lõi này là khung MẶC ĐỊNH và không đổi giữa các tập, trừ khi người dùng chọn khung tự do theo quy tắc cứng ngay dưới đây. Nhưng **cách triển khai bên trong mỗi bước phải đa dạng theo từng tập** — xem "Kỹ thuật kể chuyện bổ trợ" ở `QuyTrinh/C1-Script.md` Bước 1.5 (giai thoại mở bài, số liệu theo mốc năm, thống kê gây sốc, case study thật ẩn danh, mid-roll CTA, mở rộng rủi ro/xu hướng...). Đây là 1 **kho công cụ chọn linh hoạt**, KHÔNG phải công thức cố định phải nhét đủ vào mọi tập theo đúng 1 vị trí/tần suất — nếu tập nào cũng dùng y hệt combo kỹ thuật ở y hệt chỗ thì các tập sẽ nghe "rập khuôn" dù chủ đề khác nhau.

**Quy tắc cứng — khung tự do (người dùng chốt 21/09/2026, đã áp dụng thực tế ở Tập 3, 4, 7, 9):** ngoài khung 6 bước mặc định, người dùng được chọn **khung tự do**, sắp xếp mạch kể theo hành trình câu hỏi của khán giả (không bắt buộc có khối "bối cảnh ngành" đứng riêng, số liệu vào đúng chỗ nó gây bất ngờ). Khi dùng khung tự do **vẫn BẮT BUỘC giữ**: (a) hook 3 pha trong 30 giây đầu; (b) disclaimer ngay sau hook; (c) câu nối cố định "Giờ mới đến khúc xương khó nhằn đây..." đặt ngay trước phần điểm hoà vốn/chi phí ẩn; (d) giải thích ngay mọi thuật ngữ tài chính; (e) catchphrase kết. **Claude KHÔNG tự chọn khung tự do** — phải hỏi người dùng chọn khung mặc định hay khung tự do ở bước "Chọn hướng triển khai" (`QuyTrinh/C1-Script.md` Bước 1.5), sau khi đã có số liệu.

Thời lượng: tối thiểu **8 phút 30 giây** (nâng từ mốc 8 phút cũ — chừa biên an toàn vì tốc độ đọc thật của giọng AI có thể nhanh hơn mốc trung bình đã đo), không giới hạn trần trên — dài bao nhiêu tuỳ nội dung/số liệu có đủ chiều sâu để giữ chân người xem, không ép cắt ngắn cho vừa 1 khung cứng. **Khi ước lượng thời lượng ở C1 Bước 5/C2, phải đếm ký tự Unicode thật của `voice-script.md` (VD dùng `len()` trong Python hoặc công cụ đếm ký tự thật) — TUYỆT ĐỐI KHÔNG dùng lệnh đếm byte/dung lượng file (VD `wc -c` trong bash) làm số ký tự, vì tiếng Việt có dấu chiếm 2-3 byte/ký tự trong UTF-8, dùng nhầm sẽ ước tính thời lượng cao hơn thực tế rất nhiều** (lỗi thật đã xảy ra: ước tính 8,7 phút bằng đếm byte, đếm lại đúng ký tự chỉ ra 6,8 phút). Tần suất 2 video/tuần (điều chỉnh theo năng lực sản xuất thực tế). *Tốc độ đọc TTS đo từ Tập 8 (số đo, cập nhật khi đo lại): khoảng 17,5 ký tự/giây tính cả khoảng trắng (Tập 8: 9.375 ký tự ↔ 8 phút 56 giây), nên mốc 8 phút 30 giây ≈ 8.900 ký tự.*

## 4. Khung an toàn nội dung (BẮT BUỘC)
- Không tư vấn đầu tư cụ thể (không nói mua cổ phiếu/coin/mã nào) — chỉ phân tích, không tư vấn.
- Được nêu đích danh doanh nghiệp cụ thể **chỉ khi** số liệu/sự kiện gắn kèm có nguồn báo chí công khai kiểm chứng được (đã WebFetch xác nhận bài gốc theo `QuyTrinh/C1-Script.md` Bước 0.5 mục 2.5) — không tự suy diễn/phán xét thêm ngoài sự kiện đã đăng báo, chỉ thuật lại đúng sự kiện/số liệu đã công bố. Không nêu đích danh cá nhân cụ thể kèm phán xét tiêu cực (rủi ro pháp lý cao hơn doanh nghiệp). Mặc định gọi chung ("một tập đoàn nhà hàng lẩu nướng…", "một chuỗi cà phê"); tên thật doanh nghiệp chỉ ghi trong `so-lieu-xac-nhan.md`, chỉ nêu tên trong lời thoại khi thật cần và đã có nguồn xác nhận.
- Không dùng số liệu không kiểm chứng được — luôn giữ khung "ước tính/tổng hợp cá nhân" (đúng như disclaimer).
- **Nêu tên nguồn ngay trong lời thoại là BẮT BUỘC với nội dung liên quan pháp luật/chính sách nhà nước** (thuế, nghị định/thông tư, mức phạt, số liệu xử phạt, thống kê nhà nước như Cục Thống kê/Tổng cục Thống kê...) — VD "theo Nghị định số 141 năm 2026 của Chính phủ". Không đọc trần trụi con số pháp lý như thể Gấu tự khẳng định. (Cập nhật theo yêu cầu người dùng 21/09/2026; trước đây bắt buộc nêu tên báo cho cả số liệu doanh nghiệp/thống kê.) Không bắt buộc với số liệu đã tự ước tính cá nhân — loại đó đã có khung ước tính riêng ở trên.
- **Các số liệu còn lại (doanh nghiệp, thị trường, giá cả, ca kinh doanh...)** đã `WebFetch` từ trang uy tín được kể lại bằng góc nhìn của kênh, KHÔNG cần đọc tên báo trong lời thoại (tránh "theo báo X, báo Y nêu…" dồn dập, nghe như đọc danh sách nguồn). Khi không nêu tên nguồn trong lời thoại thì **BẮT BUỘC đủ 6 điều kiện minh bạch**: (1) disclaimer nói rõ tổng hợp từ nhiều nguồn và có chỗ tự tính; (2) **phần mô tả video liệt kê nguồn từng số liệu** (link + ngày đăng, lấy từ `so-lieu-xac-nhan.md`); (3) số tự tính/giả định gắn rõ "tôi tính/giả định của tôi"; (4) số cũ nêu mốc năm, số nước ngoài nói rõ là nước ngoài; (5) ca thật của cá nhân/quán/doanh nghiệp nhỏ phải ẩn danh; (6) **KHÔNG bịa trải nghiệm trực tiếp của kênh** (đã mở quán, đã ngồi quán, đã gặp người…) — "góc nhìn cá nhân" chỉ là cách nhìn và kết luận của kênh về số liệu đã có, không phải kinh nghiệm giả.
- Tránh chủ đề nhạy cảm chính trị/chính sách nhà nước gây tranh cãi không cần thiết.
- Disclaimer bắt buộc phải xuất hiện, không được bỏ.

## 5. Câu cố định (dùng nguyên văn mọi tập)
**Disclaimer** (sau hook mở đầu) — **bắt buộc đủ 2 ý sau, nhưng câu chữ diễn đạt viết lại khác nhau mỗi tập** (tránh nghe lặp lại y hệt qua nhiều video):
1. Thông tin là tổng hợp/góp nhặt từ nhiều nguồn, là ý kiến cá nhân, không phải tư vấn đầu tư chính thức.
2. Mời anh em góp ý/chỉnh sai ở phần bình luận.
3. **CẤM** nhắc trong lời thoại bất kỳ nội dung nào nằm ở phần mô tả video (VD "nguồn từng con số tôi để ở phần mô tả"). Lời đọc chỉ chứa 2 ý trên; mô tả video là chữ viết riêng, không được trỏ tới từ voice-script (người dùng chốt 21/09/2026).

Mẫu gốc tham khảo (KHÔNG bắt buộc dùng nguyên văn nữa, chỉ để định hướng tông giọng):
> "Thông tin dưới đây là tôi tổng hợp, góp nhặt từ nhiều nguồn, cũng là ý kiến cá nhân chứ không phải tư vấn đầu tư chính thức. Sai chỗ nào anh em cứ chửi thẳng ở comment cho tôi biết."

**Câu nối chuyển cảnh** (trước phần điểm hoà vốn/chi phí ẩn):
> "Giờ mới đến khúc xương khó nhằn đây..."

**Catchphrase kết** (mọi tập, đổi 21/09/2026 theo người dùng — bỏ chữ "ngu" vì không chê khán giả):
> "Tôi là Gấu. Tính kỹ thì giữ được tiền. Hẹn gặp anh em ở tập sau."

**Lời kêu gọi trước catchphrase** (chọn LINH HOẠT theo từng tập, không dùng thành công thức cố định): thêm 1–2 câu thân thiện ngay trước catchphrase, như mời đăng ký kênh, hoặc mời khán giả để lại ngành/chủ đề muốn xem tiếp ở bình luận. Không teaser tập sau. Tập 9 dùng: "Nếu mấy con số hôm nay giúp anh em nhìn quán lẩu rõ hơn một chút, anh em bấm đăng ký kênh để tập sau khỏi lỡ. Anh em muốn tôi mổ xẻ ngành nào tiếp theo, cứ để tên ngành ở bình luận, tôi sẽ đọc hết."
(Chỉ áp dụng cho câu ĐỌC trong voice-script; viết thuần Việt, không dùng "video" — theo `QuyTrinh/C1-Script.md`. Các tập 1–8 đã làm giữ nguyên câu cũ. Hai file gốc `Style-Guide-goc.md`, `Channel-DNA-goc.md` vẫn ghi câu cũ vì là bản gốc người dùng chốt ban đầu — DNA.md này là bản đúc kết vận hành và được ưu tiên.)

**Disclosure dùng AI trong MÔ TẢ video** (bắt buộc nguyên văn mọi tập, dán trong `tieu-de-mo-ta.txt` — KHÔNG đọc trong voice-script, chỉ là chữ viết trong mô tả): chủ động khai báo trước việc dùng AI + khẳng định mức biên tập của con người, đúng tinh thần chính sách "Inauthentic content" của YouTube (`QuyTrinh/C8-Dang-bai.md` Bước 3) — tránh bị xem là nội dung AI thuần không qua biên tập.
> "Video có dùng AI hỗ trợ viết kịch bản, tạo giọng đọc và vẽ hình ảnh minh hoạ. Toàn bộ nội dung vẫn được tôi tự tay biên tập, chọn lọc số liệu và chỉnh sửa lại trước khi lên video, không phải AI làm sẵn rồi đăng nguyên."

**Danh sách nguồn số liệu trong MÔ TẢ video** (bắt buộc mọi tập không nêu tên báo trong lời thoại, từ Tập 9; chỉ là chữ viết trong mô tả, KHÔNG nhắc/trỏ tới trong lời thoại — xem mục 5 điểm 3): liệt kê từng nguồn (tên báo/văn bản + link + ngày đăng) lấy từ `so-lieu-xac-nhan.md`, ghi rõ số nào là "tự tính". Đây là điều kiện bù cho việc bỏ nêu tên nguồn trong lời thoại (mục 4). (Đã đồng bộ vào `QuyTrinh/C8-Dang-bai.md` Bước 2-3 và `QuyTrinh/C1-Script.md` mục 5.5, ngày 21/09/2026.)

## 6. Giọng kể (voice rules)
Xem đầy đủ ở `docs/Style-Guide-goc.md` mục 2-3. Tóm tắt:
- Xưng "tôi", gọi "anh em". Dùng số liệu cụ thể tăng tin cậy. Câu ngắn 10-20 từ là chủ đạo, không quá 25 từ.
- Giải thích ngay mọi thuật ngữ tài chính vừa nhắc. Không thuyết giáo, không lên lớp. Giữ thái độ "tôi thấy vậy, anh em thấy sao" thay vì áp đặt "biết tuốt".
- Được mỉa mai nhẹ "ảo tưởng làm giàu", KHÔNG mỉa mai/hạ thấp khán giả.
- Kể số liệu như góc nhìn phân tích của kênh ("tôi mổ số của họ…", "theo tôi thấy…"), tránh lặp "theo báo X… báo Y nêu…" nhiều lần (đúng mục 4). Nên tự đặt tên gọi hình ảnh cho khái niệm chi phí/cơ chế (VD "đồng hồ chỗ ngồi" ở Tập 9) để người nghe nhớ một góc nhìn, không phải một danh sách nguồn. Không kể như thể kênh đã trực tiếp trải nghiệm điều không có thật.

## 6b. Văn phong & góc kể chuyện — BẮT BUỘC CAO (người dùng chốt 21/09/2026, sau khi Tập 9 bản đầu bị lạc hướng)
**Bản chất pillar:** mỗi tập là **phân tích cách một ngành nghề/mô hình kinh doanh KIẾM TIỀN — bán cái gì, tiền vào tiền ra thế nào, lãi lỗ ra sao — để người xem có góc nhìn thực tế.** KHÔNG phải bình luận tin tức/thống kê ngành, KHÔNG phải phân tích tập đoàn/báo cáo tài chính, KHÔNG phải bài học chung chung. **Chuẩn tham chiếu văn phong và góc kể: 3 script mẫu kênh gốc trong `script mau/` — đọc lại trước mỗi lần viết C1 (và trước khi giao bản nháp, đối chiếu lại).**

**Xương sống góc kể (BẮT BUỘC có đủ, thứ tự linh hoạt theo tập):**
1. **Một mô hình cụ thể, cỡ nhỏ-vừa bình dân** (quán/tiệm/xe/dịch vụ người xem có thể tự mở hoặc gặp hằng ngày) làm nhân vật chính. Doanh nghiệp/chuỗi lớn chỉ được dùng để **đối chiếu 1-2 câu**, không làm trục kể.
2. **Giải phẫu MỘT ĐƠN VỊ BÁN** (1 suất/1 ly/1 giờ/1 lượt): từng khoản chi trực tiếp bằng số tiền cụ thể → giá vốn, lãi gộp mỗi đơn vị.
3. **Chi phí cố định** theo tháng và quy ra mỗi ngày (mặt bằng, nhân công, điện nước, khấu hao vốn đầu tư...).
4. **Điểm hoà vốn tính bằng số đơn vị/ngày** (chi phí cố định/ngày ÷ lãi gộp mỗi đơn vị), rồi kịch bản đông/vắng (độ nhạy: doanh thu tụt 10-20%, giá nguyên liệu tăng...) với tiền lãi/lỗ cuối tháng.
5. **Chi phí ẩn/rủi ro thật của đúng mô hình đó**, rồi góc nhìn thực tế cho người muốn làm hoặc người ngoài cuộc ("nếu ngày mai anh em mở...", chỉ là cách nhìn, không phải lời khuyên).

**Quy tắc số:** ví dụ tính toán dùng số giả định làm tròn, gắn rõ "giả sử/số giả định của tôi" để người nghe nhẩm được; số ngành/thống kê/ca thật chỉ là **gia vị** (mỗi loại tối đa 1-2 đoạn ngắn), không được chiếm quá nửa kịch bản. Số tự tính phải khớp nhau (kiểm lại bằng Python trước khi giao).

**Văn phong (cứng, xuyên mọi tập):** nói như kể chuyện cho anh em nghe ("tôi", "anh em"), không đọc như báo cáo hay bản tin; tinh ranh/mỉa nhẹ nhưng không hạ thấp khán giả; mọi thuật ngữ giải thích ngay bằng lời đời thường; câu ngắn (≤ 25 từ); mỗi con số phải gắn với một khoản tiền/hình ảnh cụ thể chứ không thả số liệu trần.

**Dấu hiệu LẠC HƯỚNG (gặp là viết lại):** nhân vật chính là tập đoàn/chuỗi lớn; kể theo trình tự "năm A... năm B..." của một doanh nghiệp; nhiều số thống kê tiêu dùng/thị trường liền nhau; nghe như tóm tắt nhiều bài báo; không có điểm hoà vốn tính bằng số đơn vị/ngày; người nghe không nhẩm lại được phép tính bằng đầu.

**Phân loại cứng/cốt lõi (theo `CLAUDE.md` mục 2):** xương sống 5 điểm + văn phong ở trên = **CỨNG** (bản sắc pillar). Còn cách mở bài, ẩn dụ đặt tên, chọn ca thật, thủ pháp kể, thứ tự sắp xếp = **CỐT LÕI**, chọn linh hoạt theo tập, không rập khuôn (xem mục 3 và `docs/chien-luoc-youtube.md` mục 8).

## 7. Cụm từ / chủ đề cần tránh
- Lời khuyên đầu tư trực tiếp ("nên mua...", "chắc chắn lãi...").
- Cam kết tuyệt đối kiểu "làm vậy chắc giàu".
- Nêu đích danh doanh nghiệp mà không có nguồn báo chí kiểm chứng được, hoặc kèm phán xét/suy diễn tiêu cực ngoài sự kiện đã công bố. Nêu đích danh cá nhân cụ thể kèm phán xét tiêu cực.
- Số liệu không có nguồn/không thể kiểm chứng mà không gắn khung "ước tính cá nhân".
- Chủ đề chính trị/chính sách nhà nước nhạy cảm không cần thiết.

## 8. Bản sắc art style / cấu trúc video
Art style và cấu trúc video là bộ nhận diện riêng của kênh, chốt chi tiết ở `docs/Visual-Prompts-goc.md`.

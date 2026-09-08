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

**Ngoại hình:** gấu nâu/đen, dáng cao gầy, đứng thẳng đĩnh đạc như một quý ông lịch lãm (không mập tròn, không lùn), đầu to vừa phải ~30% cơ thể, mắt híp bán nguyệt (tinh ranh), nhếch mép cười khẩy, vest xanh navy may đo sắc sảo ôm dáng (#0C447C) + nơ bướm + kính lão gọng tròn vàng đồng (#BA7517) — chi tiết nhận diện riêng. Chi tiết đầy đủ ở `docs/Visual-Prompts-goc.md`.

## 3. Cấu trúc video (bắt buộc theo thứ tự — khung lõi, cố định)
1. **Hook mở đầu** (0-15s) — nêu nghịch lý/câu hỏi cụ thể kèm số liệu (VD "Ly trà sữa 25.000đ, tưởng lãi đậm lắm chứ gì?").
2. **Disclaimer ngắn cố định** (đặt ngay sau hook, nguyên văn mục 5).
3. **Bối cảnh ngành/hiện tượng** — giới thiệu mô hình đang phân tích.
4. **Bóc tách COGS + chi phí cố định** — giải thích ngay mọi thuật ngữ tài chính vừa nhắc.
5. **Điểm hoà vốn + chi phí ẩn/cơ hội** — dùng câu nối chuyển cảnh cố định: "Giờ mới đến khúc xương khó nhằn đây..."
6. **Kết luận bài học tài chính + catchphrase kết** (nguyên văn mục 5).

Thứ tự 6 bước lõi này KHÔNG đổi giữa các tập. Nhưng **cách triển khai bên trong mỗi bước phải đa dạng theo từng tập** — xem "Kỹ thuật kể chuyện bổ trợ" ở `QuyTrinh/C1-Script.md` Bước 1.5 (giai thoại mở bài, số liệu theo mốc năm, thống kê gây sốc, case study thật ẩn danh, mid-roll CTA, mở rộng rủi ro/xu hướng...). Đây là 1 **kho công cụ chọn linh hoạt**, KHÔNG phải công thức cố định phải nhét đủ vào mọi tập theo đúng 1 vị trí/tần suất — nếu tập nào cũng dùng y hệt combo kỹ thuật ở y hệt chỗ thì các tập sẽ nghe "rập khuôn" dù chủ đề khác nhau.

Thời lượng tham khảo: 7-9 phút/video (có thể dài hơn nếu nội dung/số liệu đủ chiều sâu để giữ chân người xem, không ép ngắn cho đủ mốc), tần suất 2 video/tuần (điều chỉnh theo năng lực sản xuất thực tế).

## 4. Khung an toàn nội dung (BẮT BUỘC)
- Không tư vấn đầu tư cụ thể (không nói mua cổ phiếu/coin/mã nào) — chỉ phân tích, không tư vấn.
- Không nêu đích danh doanh nghiệp/cá nhân cụ thể kèm phán xét tiêu cực (rủi ro pháp lý).
- Không dùng số liệu không kiểm chứng được — luôn giữ khung "ước tính/tổng hợp cá nhân" (đúng như disclaimer).
- Tránh chủ đề nhạy cảm chính trị/chính sách nhà nước gây tranh cãi không cần thiết.
- Disclaimer bắt buộc phải xuất hiện, không được bỏ.

## 5. Câu cố định (dùng nguyên văn mọi tập)
**Disclaimer** (sau hook mở đầu):
> "Thông tin dưới đây là tôi tổng hợp, góp nhặt từ nhiều nguồn, cũng là ý kiến cá nhân chứ không phải tư vấn đầu tư chính thức. Sai chỗ nào anh em cứ chửi thẳng ở comment cho tôi biết."

**Câu nối chuyển cảnh** (trước phần điểm hoà vốn/chi phí ẩn):
> "Giờ mới đến khúc xương khó nhằn đây..."

**Catchphrase kết** (mọi tập):
> "Tôi là Gấu. Khôn thì sống, ngu thì mất tiền. Hẹn anh em video sau."

## 6. Giọng kể (voice rules)
Xem đầy đủ ở `docs/Style-Guide-goc.md` mục 2-3. Tóm tắt:
- Xưng "tôi", gọi "anh em". Dùng số liệu cụ thể tăng tin cậy. Câu ngắn 10-20 từ là chủ đạo, không quá 25 từ.
- Giải thích ngay mọi thuật ngữ tài chính vừa nhắc. Không thuyết giáo, không lên lớp. Giữ thái độ "tôi thấy vậy, anh em thấy sao" thay vì áp đặt "biết tuốt".
- Được mỉa mai nhẹ "ảo tưởng làm giàu", KHÔNG mỉa mai/hạ thấp khán giả.

## 7. Cụm từ / chủ đề cần tránh
- Lời khuyên đầu tư trực tiếp ("nên mua...", "chắc chắn lãi...").
- Cam kết tuyệt đối kiểu "làm vậy chắc giàu".
- Nêu đích danh kèm phán xét tiêu cực 1 doanh nghiệp/cá nhân cụ thể.
- Số liệu không có nguồn/không thể kiểm chứng mà không gắn khung "ước tính cá nhân".
- Chủ đề chính trị/chính sách nhà nước nhạy cảm không cần thiết.

## 8. Bản sắc art style / cấu trúc video
Art style và cấu trúc video là bộ nhận diện riêng của kênh, chốt chi tiết ở `docs/Visual-Prompts-goc.md`.

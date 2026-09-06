# VISUAL PROMPTS — GẤU TINH RANH

Bộ 4 prompt dùng cho pipeline sản xuất video faceless YouTube. Adapt từ art family của kênh reference "Ếch Biết Tuốt", đổi palette và identity nhân vật sang "Gấu Tinh Ranh" theo Channel DNA và Style Guide đã chốt.

## 1. charStyle

```
Gấu nhân vật hoạt hình 2D phong cách cách điệu tương tự dòng meme mascot, đầu to tròn chiếm khoảng 40% cơ thể, dáng mập tròn, màu lông nâu đậm/đen (#4A3728 tương tự). Mắt híp hình bán nguyệt, con ngươi nhỏ đen lấp lánh tạo cảm giác tinh ranh/mưu mẹo (khác hẳn mắt lồi to tròn của Ếch), lông mày xếch nhẹ tạo biểu cảm dò xét. Miệng rộng vừa phải, môi màu nâu nhạt, thường nhếch mép cười khẩy thay vì mở to. Mũi nhỏ hình tam giác đen. Cấu trúc tay chân đơn giản hoá kiểu cartoon, bàn tay 3-4 ngón tròn trịa màu nâu đậm hơn thân, không chi tiết móng vuốt rõ. Trang phục: vest công sở màu xanh navy đậm (#0C447C), nơ bướm xanh navy hoặc đen, áo sơ mi trắng, đeo kính lão gọng tròn màu vàng đồng (#BA7517) — kính là chi tiết nhận diện thay thế hoa hồng đỏ của Ếch. Viền nét vẽ đen dày đồng đều khoảng 3-4px, tô màu phẳng (flat shading) không gradient phức tạp, thỉnh thoảng có shading nhẹ tạo khối ở nếp gấp vải. Kết thúc bằng: professional white background, TOP ROW 4 full-body views front/45-degree/side/back, BOTTOM ROW 6 expression close-ups (nheo mắt tính toán, cười khẩy, dò xét qua kính, chỉ tay, ngồi gõ máy tính, khoanh tay tự tin).
```

## 2. bgStyle

```
Bối cảnh chia hai nhóm phong cách song song, giữ nguyên cấu trúc kỹ thuật của kênh gốc: (1) Nền phẳng minh hoạ — nét vẽ flat 2D cartoon, viền đen dày đồng nhất với nhân vật chính, dùng cho các cảnh trừu tượng như toà nhà công ty, biểu đồ tài chính, mô hình kinh doanh; (2) Nền ảnh thật (photo-realistic) — chụp thực tế đường phố Việt Nam, văn phòng công sở, cửa hàng/quán xá, mờ nhẹ để nhân vật 2D nổi bật. Bảng màu chủ đạo: xanh navy (#0C447C), vàng đồng (#BA7517), trắng, đen — thay thế hoàn toàn tông đỏ-đen của kênh gốc. Mood: điềm tĩnh, sắc sảo khi Gấu đang "vạch trần" mô hình kinh doanh; căng thẳng, cảnh báo (kèm tia chớp đỏ #E24B4A làm điểm nhấn cảnh báo duy nhất còn giữ) khi thể hiện thua lỗ/rủi ro. Kết thúc bằng: NO characters, NO people, NO text, NO words, 16:9.
```

## 3. sceneStyle / Aesthetic (bản rút gọn ~40 từ)

```
Flat 2D cartoon style, đường viền đen dày đồng nhất 3-4px, tô màu phẳng ít gradient, đầu nhân vật to tròn dáng mập chiếm ~40% cơ thể, mắt híp tinh ranh thay vì mắt lồi, phối trộn nền minh hoạ phẳng và nền ảnh thật, bảng màu chủ đạo xanh navy - vàng đồng - trắng - đen.
```

## 4. masterPrompt / shotPrompt

```
[sceneStyle: flat 2D cartoon, viền đen dày, đầu to tròn dáng mập, mắt híp tinh ranh] + nhân vật Gấu [mặc vest xanh navy, nơ bướm, đeo kính lão gọng tròn vàng đồng] + đang [HÀNH ĐỘNG/POSE — ví dụ: "nheo mắt tính toán chi phí trên máy tính với vẻ mặt dò xét" / "chỉ tay vào biểu đồ lợi nhuận với nụ cười khẩy" / "khoanh tay đứng giữa văn phòng với vẻ tự tin"] + tại [bối cảnh cụ thể — ví dụ: "trên nền trắng với bảng tính chi phí bên cạnh" / "trước một quán trà sữa trên đường phố Việt Nam" / "trong văn phòng công sở thật"] + [text overlay nếu có, theo Thumbnail Text Bank đã có trong Style Guide, ví dụ: "Lãi thật không?", "Vỡ mộng rồi"], 16:9, professional quality.

Ghi chú áp dụng: mỗi cảnh chỉ cần thay [HÀNH ĐỘNG/POSE] và [bối cảnh cụ thể], giữ nguyên charStyle + sceneStyle để đảm bảo tính nhất quán nhân vật Gấu xuyên suốt mọi video.
```

## Đối chiếu với kênh reference (Ếch Biết Tuốt)

| Yếu tố | Ếch (gốc) | Gấu (kênh mới) |
|---|---|---|
| Mắt | To tròn, lồi | Híp, bán nguyệt |
| Chi tiết nhận diện | Hoa hồng đỏ ngực trái | Kính lão gọng tròn vàng đồng |
| Màu vest | Đen | Xanh navy |
| Bảng màu nền | Đỏ - vàng - trắng - đen | Xanh navy - vàng đồng - trắng - đen |
| Biểu cảm chủ đạo | Ngạc nhiên, lo lắng | Nheo mắt tính toán, cười khẩy |

# VISUAL PROMPTS — GẤU TINH RANH

Bộ 4 prompt dùng cho pipeline sản xuất video faceless YouTube, xây dựng riêng cho identity nhân vật "Gấu Tinh Ranh" theo Channel DNA và Style Guide đã chốt.

## 1. charStyle

**Quan trọng — phân biệt 2 phần của charStyle, KHÔNG dán lẫn lộn khi viết prompt cho scene thật:**
- **Phần A — Nhận diện cố định (Character Lock, BẮT BUỘC giữ nguyên mọi prompt có Gấu):** hình dáng đầu/thân, màu lông, kiểu mắt/lông mày, mũi, trang phục, kính, răng vàng, kiểu nét vẽ. Đây là thứ làm Gấu luôn LÀ Gấu dù đổi tư thế/biểu cảm.
- **Phần B — Tư thế mặc định (CHỈ dùng khi gen lại ảnh reference sheet gốc, KHÔNG paste vào prompt của scene thật):** đoạn "Default pose..." mô tả 1 tư thế cụ thể (đứng nghiêng, tay đút túi, cúi cằm nhìn qua kính) — đây từng là nguyên nhân khiến MỌI ảnh scene bị lặp lại y hệt đúng 1 dáng đứng dù đã yêu cầu hành động khác, vì mô tả này đứng cạnh mô tả hành động mới gây xung đột/lấn át. Khi viết prompt cho 1 scene cụ thể, **bỏ hẳn đoạn "Default pose..." này**, thay bằng tư thế/biểu cảm được mô tả riêng cho scene đó (xem `QuyTrinh/C3-Prompt-Anh.md` — biểu cảm phải phong phú, hơi meme/phóng đại, thay đổi theo ngữ cảnh, không lặp lại đúng 1 dáng đứng của bảng gốc).

```
Gau, a stylized 2D cartoon mascot character in a meme-mascot style, moderately large round head making up about 30% of the body, tall and lean build with a dignified, statuesque stance (not chubby/rotund, not short/squat — long legs, confident posture like a distinguished gentleman). Consistent solid dark chocolate-brown fur color (hex approx #4A3728, a deep rich brown — NOT light tan, NOT caramel, NOT near-black) applied identically in every image. Narrow crescent-shaped squinting eyes with small glinting black pupils giving a sly/cunning impression, slightly slanted thick eyebrows for a scrutinizing expression. Moderately wide mouth, light brown lips, usually a smug smirk that reveals a single glinting gold tooth on one side — Gau's signature quirky detail. Small black triangular nose. Simplified cartoon limb structure, slender long arms and legs, rounded 3-4 finger paws in a darker brown than the body, no distinct claw details. Outfit: sharp, well-tailored dark navy blue business suit with vest fitted close to the body (#0C447C), navy or black bow tie, crisp white dress shirt, round wire-rim glasses in bronze-gold (#BA7517) — the glasses and the gold tooth are Gau's signature identifying details. Thick, even black outline strokes about 3-4px, flat shading with no complex gradients, occasional light shading for volume on fabric folds. Overall silhouette should feel tall, polished, and authoritative — like a sharply dressed, distinguished figure with a hint of mischief — rather than short, stiff, or cartoonishly round.
```

**Phần B — chỉ dùng khi gen ảnh reference sheet gốc (không dùng cho scene thật):**
```
Default pose for the reference sheet only: body weight shifted onto one leg, torso tilted slightly, one hand casually tucked in the trouser pocket, chin tilted down so he is looking slightly downward over the top of his glasses at the viewer — a knowing, appraising stance. End with: professional white background, TOP ROW 4 full-body views front/45-degree/side/back, BOTTOM ROW 6 expression close-ups (squinting while calculating, smug smirk with gold tooth, peering down over glasses, pointing, typing at a computer, arms crossed confidently).
```

## 2. bgStyle

```
Backgrounds split into two parallel style groups: (1) Flat illustrated background — flat 2D cartoon linework, thick black outlines matching the main character, used for abstract scenes like corporate buildings, financial charts, business model diagrams; (2) Photo-realistic background — real Vietnamese street scenes, office interiors, shops/storefronts, slightly blurred so the 2D character stands out. Primary color palette: navy blue (#0C447C), bronze-gold (#BA7517), white, black. Mood: calm and sharp when Gau is "exposing" a business model; tense and alarming (with a red lightning-bolt accent #E24B4A as the sole warning highlight) when depicting losses/risk. End with: NO characters, NO people, NO text, NO words, 16:9.
```

## 3. sceneStyle / Aesthetic (short version, ~40 words)

```
Flat 2D cartoon style, thick even black outlines 3-4px, flat coloring with minimal gradients, moderately large round head on a tall, lean, statuesque build making up ~30% of the body, sly squinting eyes instead of bulging eyes, a mix of flat illustrated backgrounds and photo-realistic backgrounds, primary palette of navy blue - bronze-gold - white - black.
```

## 4. masterPrompt / shotPrompt

```
[sceneStyle: flat 2D cartoon, thick black outlines, moderately large round head on a tall lean statuesque build, sly squinting eyes] + the Gau character [wearing a navy blue vest, bow tie, round bronze-gold wire-rim glasses] + [ACTION/POSE — e.g. "squinting while calculating costs on a computer with a scrutinizing expression" / "pointing at a profit chart with a smug smirk" / "standing with arms crossed confidently in an office"] + at/in [specific setting — e.g. "a white background with a cost spreadsheet beside him" / "in front of a bubble tea shop on a Vietnamese street" / "inside a real office"] + [text overlay if any, from the Thumbnail Text Bank in the Style Guide, e.g. "Is it really profit?", "Reality check"], 16:9, professional quality.

Usage note: for each scene, only swap out [ACTION/POSE] and [specific setting], keeping charStyle + sceneStyle unchanged to preserve Gau's visual consistency across every video.
```

## Bảng nhận diện cố định của Gấu

| Yếu tố | Chốt cho Gấu Tinh Ranh |
|---|---|
| Mắt | Híp, bán nguyệt |
| Chi tiết nhận diện | Kính lão gọng tròn vàng đồng |
| Màu vest | Xanh navy |
| Bảng màu nền | Xanh navy - vàng đồng - trắng - đen |
| Biểu cảm chủ đạo | Nheo mắt tính toán, cười khẩy |

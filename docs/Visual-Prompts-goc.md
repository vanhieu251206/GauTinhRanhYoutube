# VISUAL PROMPTS — GẤU TINH RANH

Bộ 4 prompt dùng cho pipeline sản xuất video faceless YouTube, xây dựng riêng cho identity nhân vật "Gấu Tinh Ranh" theo Channel DNA và Style Guide đã chốt.

## 1. charStyle

**Quan trọng — phân biệt 2 phần của charStyle, KHÔNG dán lẫn lộn khi viết prompt cho scene thật:**
- **Phần A — Nhận diện cố định (Character Lock, BẮT BUỘC giữ nguyên mọi prompt có Gấu):** hình dáng đầu/thân, màu lông, kiểu mắt/lông mày, mũi, trang phục, kính, răng vàng, kiểu nét vẽ. Đây là thứ làm Gấu luôn LÀ Gấu dù đổi tư thế/biểu cảm.
- **Phần B — Tư thế mặc định (CHỈ dùng khi gen lại ảnh reference sheet gốc, KHÔNG paste vào prompt của scene thật):** đoạn "Default pose..." mô tả 1 tư thế cụ thể (đứng nghiêng, tay đút túi, cúi cằm nhìn qua kính) — đây từng là nguyên nhân khiến MỌI ảnh scene bị lặp lại y hệt đúng 1 dáng đứng dù đã yêu cầu hành động khác, vì mô tả này đứng cạnh mô tả hành động mới gây xung đột/lấn át. Khi viết prompt cho 1 scene cụ thể, **bỏ hẳn đoạn "Default pose..." này**, thay bằng tư thế/biểu cảm được mô tả riêng cho scene đó (xem `QuyTrinh/C3-Prompt-Anh.md` — biểu cảm phải phong phú, hơi meme/phóng đại, thay đổi theo ngữ cảnh, không lặp lại đúng 1 dáng đứng của bảng gốc).

```
Gau, a stylized 2D cartoon mascot character in a bold meme-mascot style with a rounder, more compact silhouette (head-to-body ratio closer to 40-45%, torso and limbs softer/rounder than a slender adult figure — think classic mascot-comic proportions, not a slim tall businessman silhouette). Consistent solid dark chocolate-brown fur color (hex approx #4A3728, a deep rich brown — NOT light tan, NOT caramel, NOT near-black) applied identically in every image. Narrow crescent-shaped squinting eyes with small glinting black pupils giving a sly/cunning impression, slightly slanted thick eyebrows for a scrutinizing expression — this squinting sly-eye look is Gau's non-negotiable signature and must NOT be swapped for generic big round eyes. Moderately wide mouth, light brown lips, usually a smug smirk that reveals a single glinting gold tooth on one side — Gau's signature quirky detail; allow the mouth to stretch/exaggerate more dramatically than before for stronger comic expressions (wide open shout, tiny pursed smirk, etc.) while keeping the gold tooth visible whenever the mouth is open. Small black triangular nose. Simplified cartoon limb structure with classic oversized white cartoon gloves (4-fingered, thick black outline, rounded) on the hands instead of bare paws — this is the key new graphic device borrowed from classic mascot-comic style, used for bigger/clearer gestures. Outfit: sharp, well-tailored dark navy blue business suit with vest fitted close to the body (#0C447C), navy or black bow tie, crisp white dress shirt, round wire-rim glasses in bronze-gold (#BA7517) — the glasses and the gold tooth remain Gau's signature identifying details. Thick, even black outline strokes about 3-4px, flat shading with no complex gradients, occasional light shading for volume on fabric folds. Overall feel: punchy, bold, high-contrast comic-mascot energy with exaggerated poses/expressions — while still reading unmistakably as the same sly, mischievous Gau in every image.
```

**Phần B — chỉ dùng khi gen ảnh reference sheet gốc (không dùng cho scene thật):**
```
Default pose for the reference sheet only: body weight shifted onto one leg, torso tilted slightly, one white-gloved hand casually resting on the hip, chin tilted down so he is looking slightly downward over the top of his glasses at the viewer — a knowing, appraising stance. End with: professional white background, TOP ROW 4 full-body views front/45-degree/side/back, BOTTOM ROW 6 expression close-ups (squinting while calculating, smug smirk with gold tooth, peering down over glasses, pointing with a gloved finger, exaggerated shocked wide-mouth shout, arms crossed confidently).
```

## 2. bgStyle

```
Backgrounds split into two parallel style groups: (1) Flat illustrated background — flat 2D cartoon linework, thick black outlines matching the main character, used for abstract scenes like corporate buildings, financial charts, business model diagrams; (2) Photo-realistic background — real Vietnamese street scenes, office interiors, shops/storefronts, slightly blurred so the 2D character stands out. Primary color palette: navy blue (#0C447C), bronze-gold (#BA7517), white, black. Mood: calm and sharp when Gau is "exposing" a business model; tense and alarming (with a red lightning-bolt accent #E24B4A as the sole warning highlight) when depicting losses/risk. End with: NO characters, NO people, NO text, NO words, 16:9.
```

## 3. sceneStyle / Aesthetic (short version, ~40 words)

```
Bold flat 2D cartoon-comic style, thick even black outlines 3-4px, flat coloring with minimal gradients, rounder compact mascot-comic proportions (head ~40-45% of body), sly squinting eyes instead of bulging eyes, oversized white cartoon gloves on the hands, punchy exaggerated poses/expressions, a mix of flat illustrated backgrounds and photo-realistic backgrounds, primary palette of navy blue - bronze-gold - white - black.
```

## 4. masterPrompt / shotPrompt

```
[sceneStyle: bold flat 2D cartoon-comic, thick black outlines, rounder compact mascot proportions, sly squinting eyes, oversized white gloves] + the Gau character [wearing a navy blue vest, bow tie, round bronze-gold wire-rim glasses, white cartoon gloves] + [ACTION/POSE, exaggerated/punchy — e.g. "squinting while calculating costs on a computer with a scrutinizing expression" / "pointing at a profit chart with a smug smirk, gloved finger extended" / "arms flung wide in an exaggerated shocked shout, mouth wide open showing the gold tooth"] + at/in [specific setting — e.g. "a white background with a cost spreadsheet beside him" / "in front of a bubble tea shop on a Vietnamese street" / "inside a real office"] + [optional bold comic graphic device — e.g. a starburst/impact shape behind a key number, oversized bold typography for a shocking figure, in the style of a comic sound-effect burst] + [text overlay if any, from the Thumbnail Text Bank in the Style Guide, e.g. "Is it really profit?", "Reality check"], 16:9, professional quality.

Usage note: for each scene, only swap out [ACTION/POSE], [specific setting], and the optional graphic device, keeping charStyle + sceneStyle unchanged to preserve Gau's visual consistency across every video.
```

## Bảng nhận diện cố định của Gấu

| Yếu tố | Chốt cho Gấu Tinh Ranh |
|---|---|
| Mắt | Híp, bán nguyệt — KHÔNG đổi sang mắt to tròn (giữ nguyên dù đổi kỹ thuật vẽ khác) |
| Chi tiết nhận diện | Kính lão gọng tròn vàng đồng, răng vàng khi cười khẩy, nơ bướm |
| Tay | Găng tay trắng kiểu cartoon cổ điển (cập nhật — thay cho bàn tay/móng trần trước đây) |
| Tỉ lệ đầu/thân | Đầu to hơn trước, ~40-45% thân người, dáng tròn/mềm hơn kiểu mascot-comic (cập nhật — trước đây là dáng cao gầy thanh lịch ~30%) |
| Màu vest | Xanh navy |
| Bảng màu nền | Xanh navy - vàng đồng - trắng - đen |
| Biểu cảm chủ đạo | Nheo mắt tính toán, cười khẩy — nay cho phép biểu cảm phóng đại mạnh hơn (miệng há to sốc, hét...) |
| Đồ hoạ bổ trợ | Có thể thêm hiệu ứng comic burst/starburst sau số liệu sốc, chữ to đậm kiểu comic — dùng linh hoạt, không bắt buộc mọi ảnh |

> Cập nhật theo yêu cầu người dùng (tham khảo phong cách vẽ từ 1 kênh khác) — vẫn giữ ảnh tĩnh + voice, KHÔNG chuyển sang animation. Nhận diện cốt lõi (mắt híp tinh ranh, kính lão, răng vàng, nơ bướm, bảng màu) giữ nguyên; chỉ đổi tỉ lệ cơ thể, thêm găng tay trắng, và cho phép biểu cảm/đồ hoạ phóng đại hơn.

# -*- coding: utf-8 -*-
"""
sua_sub.py — C6: gộp sub.srt (TTS) + sub-capcut.srt thành sub-final.srt: chia phụ đề vừa 1 dòng CapCut, không ngắt ý.

    python sua_sub.py "Bai-Dang/Tap 9 - Buffet Lau"
    python sua_sub.py <thư-mục-tập> --max-chars 42 --max-dur 4.5

Cách làm (xem QuyTrinh/C6-Sua-Sub.md):
  - CHỮ lấy từ sub.srt (khớp voice-script). Khôi phục chữ gốc cho phần đã phiên âm (sổ tay ở C1-Script.md), "N phần trăm" -> "N%".
  - Chia mỗi cue thành các dòng <= --max-chars ký tự: ưu tiên ngắt sau dấu câu, trước liên từ; cấm ngắt giữa số và đơn vị,
    trong cụm cố định, hoặc để từ nối (là, và, của...) ở cuối dòng.
  - MỐC: đầu/cuối mỗi cue TTS giữ nguyên; các điểm ngắt bên trong lấy từ sub-capcut.srt nếu khớp được, không thì chia theo tỉ lệ ký tự.
"""
import argparse
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

NUMWORDS = {"một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín", "mười", "mươi", "lăm", "mốt", "tư", "linh", "lẻ", "trăm", "nghìn", "triệu", "tỷ", "rưỡi", "vài", "mấy"}
UNITS = {"đồng", "suất", "khách", "người", "phần", "tiếng", "giờ", "phút", "ngày", "tháng", "năm", "triệu", "nghìn", "tỷ", "ký", "gam", "yên",
         "bàn", "điểm", "quán", "chỗ", "lượt", "lần", "cái", "khay", "vị", "bữa", "tuổi", "mét", "cây", "lớp", "khoản", "câu", "%"}
CONJ = {"và", "nhưng", "mà", "vì", "nên", "để", "thì", "khi", "nếu", "rồi", "hay", "hoặc", "còn", "tuy", "dù", "cho", "theo", "trong", "với", "cả", "kể", "tức"}
NOEND = {"là", "và", "của", "ở", "cho", "với", "để", "các", "những", "một", "mỗi", "cái", "thì", "mà", "nhưng", "vì", "nên", "khi", "nếu", "rằng",
         "sẽ", "đã", "đang", "cũng", "rất", "không", "chỉ", "còn", "hay", "hoặc", "tại", "từ", "trong", "theo", "bằng", "như", "do", "nào", "được", "bị",
         "nhiều", "mọi", "từng", "vài", "mấy", "hơn", "gần", "khoảng", "tầm", "chừng", "trên", "dưới", "chưa", "vẫn", "lại", "phải", "nên", "vừa", "mới", "chính", "đến", "tự"}
PRON = {"tôi", "nó", "họ", "mình", "chúng", "ta", "ai", "bạn", "ông", "bà", "anh", "chị"}
PROTECT = ["búp phê", "buffet", "lãi gộp", "lãi ròng", "giá vốn", "chi phí cố định", "chi phí", "điểm hòa vốn", "hòa vốn", "đồng hồ chỗ ngồi",
           "chỗ ngồi", "hóa đơn điện tử", "hộ kinh doanh", "nghị định", "phần trăm", "khấu hao", "mặt bằng", "dòng tiền", "lẩu mini", "ứng dụng giao hàng",
           "khách ăn khỏe", "suất lẩu", "quán lẩu", "ngày thường", "cuối tuần", "thanh toán", "tiền vé", "khay thịt bò",
           "chủ quán", "khách hàng", "nhân viên", "tiền thuê", "tiền điện", "hợp đồng", "hôm nay", "cuối tháng", "điều hòa", "nước lẩu", "ăn thả ga",
           "anh em", "không phải", "người ăn khỏe", "lời khuyên", "góc nhìn", "cá nhân", "nhà hàng", "tập đoàn", "ước tính", "mô tả", "bình luận",
           "thương hiệu", "sáng lập", "cà phê", "ông chủ", "chính phủ", "doanh thu", "lợi nhuận", "giá vé", "nguyên liệu", "quán ăn", "mặt phố", "tư vấn", "đầu tư",
           "cơ chế", "bọt tuyết", "rửa xe", "tiệm rửa xe", "bảng giá", "đánh bóng bằng máy", "nhựa nhám", "phút công", "dẫn khách",
           "bao nhiêu", "quyết định", "trung bình", "câu chuyện", "nằm ở", "trước khi", "chia cho", "dừng lại", "bù lại", "học lại", "đọc báo",
           "dễ vào", "vào này", "người tưởng", "người hên gặp", "biết tính được", "chịu nổi", "đỡ tốn", "mức nhất định", "xe hơn", "ngày làm", "số tiệm", "đường thoát nước",
           "tiền bạc", "tưởng dễ", "chuyện kiếm", "hai tiếng", "một tháng", "mỗi tháng", "mỗi ngày", "mỗi suất", "một ngày", "một năm", "cả năm"]


def norm(s):
    s = unicodedata.normalize("NFD", s.lower().replace("đ", "d"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"(?<=\d)[.,](?=\d)", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def ts(t):
    h, m, r = t.split(":")
    s, ms = r.replace(".", ",").split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def fmt(t):
    t = max(0, t)
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def read_srt(path):
    raw = open(path, encoding="utf-8-sig").read().replace("\r\n", "\n")
    out = []
    for blk in re.split(r"\n\s*\n", raw.strip()):
        ln = blk.split("\n")
        i = next((k for k, x in enumerate(ln) if "-->" in x), None)
        if i is None:
            continue
        a, b = [x.strip() for x in ln[i].split("-->")]
        out.append({"s": ts(a), "e": ts(b), "t": " ".join(ln[i + 1:]).strip()})
    return out


def load_reversals():
    """Sổ tay phiên âm ở C1-Script.md: "gốc" → "phiên âm". Chỉ khôi phục các phiên âm >= 2 từ (tránh đổi nhầm từ tiếng Việt thường như 'yên')."""
    rev = []
    p = os.path.join(ROOT, "QuyTrinh", "C1-Script.md")
    for l in open(p, encoding="utf-8"):
        m = re.match(r'^- "([^"]+)"(?: \([^)]*\))? → "([^"]+)"', l)
        if m and len(m.group(2).split()) >= 2:
            rev.append((m.group(2), m.group(1)))
    return rev


def to_display(text, rev):
    for spoken, orig in rev:
        def sub(m, orig=orig):
            w = m.group(0)
            return orig[0].upper() + orig[1:] if w[:1].isupper() else orig
        text = re.sub(re.escape(spoken), sub, text, flags=re.I)
    text = re.sub(r"(\d[\d.,]*)\s+phần trăm", r"\1%", text)
    return re.sub(r"\s+", " ", text).strip()


def strip_p(w):
    return re.sub(r"^[\W_]+|[\W_]+$", "", w.lower())


def split_pieces(text, max_chars):
    """Chia 1 câu thành các dòng <= max_chars; trả về list chuỗi."""
    tokens = text.split(" ")
    n = len(tokens)
    if len(text) <= max_chars:
        return [text]
    st = [strip_p(t) for t in tokens]
    # vị trí bị cấm ngắt do cụm cố định
    inside, ends = set(), set()
    for ph in PROTECT:
        pw = ph.split()
        for i in range(n - len(pw) + 1):
            if st[i:i + len(pw)] == pw:
                inside.update(range(i, i + len(pw) - 1))  # ngắt sau token i (giữa i và i+1) bị cấm
                ends.add(i + len(pw) - 1)
    def bcost(i):  # chi phí ngắt SAU token i (giữa i và i+1)
        t = tokens[i]
        forb = False
        if re.search(r"\d", t) or st[i] in NUMWORDS:
            if st[i + 1] in UNITS or tokens[i + 1] in UNITS:
                forb = True
        if st[i] in NUMWORDS and st[i + 1] in NUMWORDS and not re.search(r"[,;:.?!]$", t):
            forb = True  # số đọc bằng chữ ("ba | mươi", "mười | lăm"): không tách đôi
        if i in inside:
            forb = True
        punct = t[-1] in ".?!…"
        soft = t[-1] in ",;:"
        if st[i] in NOEND and not (punct or soft) and not (i in ends and st[i] in ("lại", "hơn")):  # "dừng lại", "nhiều xe hơn" được đứng cuối
            forb = True
        if st[i] in PRON and not (punct or soft) and not (i > 0 and st[i - 1] in ("của", "cho", "với", "về")):
            forb = True  # đại từ làm chủ ngữ: không tách khỏi động từ đi sau
        base = 0.0 if punct else 0.0 if soft else 2.0 if st[i + 1] in CONJ else 3.0 if st[i + 1] == "là" else 12.0
        return base + (60 if forb else 0)
    total = len(text)
    nest = -(-total // int(max_chars * 0.88))
    target = total / nest
    INF = 1e9
    dp = [INF] * (n + 1)
    back = [0] * (n + 1)
    dp[0] = 0.0
    for j in range(1, n + 1):
        for k in range(j):
            L = len(" ".join(tokens[k:j]))
            if L > max_chars or dp[k] >= INF:
                continue
            c = dp[k] + 2.5 + ((L - target) / max_chars) ** 2 * 5
            if L < 14:
                c += 6
            if j < n:
                c += bcost(j - 1)
            if c < dp[j]:
                dp[j], back[j] = c, k
    if dp[n] >= INF:  # có từ dài hơn giới hạn: không chia được
        return [text]
    cuts, j = [], n
    while j > 0:
        cuts.append((back[j], j))
        j = back[j]
    return [" ".join(tokens[a:b]) for a, b in reversed(cuts)]


def tidy(p):
    return re.sub(r"[,;:.\s]+$", "", p).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--max-chars", type=int, default=42)
    ap.add_argument("--max-dur", type=float, default=4.5)
    ap.add_argument("--min-dur", type=float, default=0.8)
    ap.add_argument("--out", default="sub-final.srt")
    a = ap.parse_args()
    F = a.folder
    tts = read_srt(os.path.join(F, "sub.srt"))
    capn = next(n for n in os.listdir(F) if n.lower() in ("sub-capcut.srt", "sub capcut.srt"))
    cap = read_srt(os.path.join(F, capn))
    rev = load_reversals()

    items = []  # {s,e,text}
    orig_norm = ""
    for c in tts:
        disp = to_display(c["t"], rev)
        orig_norm += norm(disp)
        sents = [x for x in re.split(r"(?<=[.?!…])\s+", disp) if x]
        pieces = []
        for s_ in sents:
            pieces += split_pieces(s_, a.max_chars)
        # gộp dòng quá ngắn (< 10 ký tự) vào dòng liền kề nếu vẫn vừa
        merged = []
        for p in pieces:
            if merged and (len(p) < 10 or len(merged[-1]) < 10) and len(merged[-1]) + 1 + len(p) <= a.max_chars:
                merged[-1] = merged[-1] + " " + p
            else:
                merged.append(p)
        pieces = merged
        S, E = c["s"], c["e"]
        # thời điểm ngắt: theo tỉ lệ ký tự, tinh chỉnh bằng CapCut nếu khớp
        lens = [len(norm(p)) or 1 for p in pieces]
        cum, acc = [], 0
        for L in lens:
            acc += L
            cum.append(acc)
        tot = acc
        bounds = [S + (E - S) * cum[i] / tot for i in range(len(pieces) - 1)]
        if len(pieces) > 1:
            win = [x for x in cap if S - 1 <= x["s"] <= E + 1 and norm(x["t"])]
            cb, cp = "", []
            for x in win:
                cp.append(len(cb))
                cb += norm(x["t"])
            cp.append(len(cb))
            for i in range(len(pieces) - 1):
                nxt = norm(pieces[i + 1])
                for L in (10, 7):
                    key = nxt[:L]
                    if len(key) < L:
                        continue
                    hits = [m.start() for m in re.finditer(re.escape(key), cb)]
                    times = []
                    for o in hits:
                        k = max(j for j in range(len(win)) if cp[j] <= o)
                        x = win[k]
                        times.append(x["s"] + (o - cp[k]) / max(1, cp[k + 1] - cp[k]) * (x["e"] - x["s"]))
                    times = [t for t in times if S + 0.25 < t < E - 0.25 and abs(t - bounds[i]) < 1.2]
                    if times:
                        bounds[i] = min(times, key=lambda t: abs(t - bounds[i]))
                        break
            for i in range(1, len(bounds)):  # đơn điệu, mỗi dòng >= 0,5s nếu có thể
                bounds[i] = max(bounds[i], bounds[i - 1] + 0.5)
            bounds = [min(b, E - 0.3) for b in bounds]
        edges = [S] + bounds + [E]
        for i, p in enumerate(pieces):
            items.append({"s": edges[i], "e": edges[i + 1], "t": tidy(p)})

    # chỉnh thời lượng: không chồng, tối thiểu min-dur nếu còn khoảng trống
    for i, it in enumerate(items):
        nxt = items[i + 1]["s"] if i + 1 < len(items) else it["e"] + 1
        it["e"] = min(it["e"], nxt)
        if it["e"] - it["s"] < a.min_dur:
            it["e"] = min(it["s"] + a.min_dur, nxt - 0.02)
        it["e"] = max(it["e"], it["s"] + 0.3)

    with open(os.path.join(F, a.out), "w", encoding="utf-8") as f:
        for i, it in enumerate(items, 1):
            f.write(f"{i}\n{fmt(it['s'])} --> {fmt(it['e'])}\n{it['t']}\n\n")

    # kiểm tra
    got = "".join(norm(it["t"]) for it in items)
    lens = [len(it["t"]) for it in items]
    over = [(i + 1, it["t"]) for i, it in enumerate(items) if len(it["t"]) > a.max_chars]
    short = [(i + 1, it["t"]) for i, it in enumerate(items) if len(it["t"]) < 8]
    long_dur = [(i + 1, round(it["e"] - it["s"], 2)) for i, it in enumerate(items) if it["e"] - it["s"] > a.max_dur]
    fast = [(i + 1, round(len(it["t"]) / max(0.1, it["e"] - it["s"]), 1)) for i, it in enumerate(items) if len(it["t"]) / max(0.1, it["e"] - it["s"]) > 24]
    print(f"TTS {len(tts)} cue, CapCut {len(cap)} cue -> {len(items)} dòng phụ đề")
    print(f"độ dài dòng: max {max(lens)}, TB {sum(lens)/len(lens):.1f}, ≤{a.max_chars}: {len(lens)-len(over)}/{len(lens)}")
    print("mất/thừa chữ:", "KHÔNG (đủ 100%)" if got == orig_norm else f"LỆCH {len(got)} vs {len(orig_norm)}")
    print("dòng vượt giới hạn:", over[:5], "| dòng < 8 ký tự:", short[:5], "| dòng > %.1fs:" % a.max_dur, long_dur[:5], "| tốc độ > 24 ký tự/s:", fast[:8])


if __name__ == "__main__":
    main()

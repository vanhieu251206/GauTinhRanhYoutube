# -*- coding: utf-8 -*-
"""
timing_scene.py — C5 Bước 1: lấy mốc thời gian mỗi scene từ sub.srt (TTS, mốc chính) + sub-capcut.srt (đối chứng).

    python timing_scene.py "Bai-Dang/Tap 9 - Buffet Lau"            # đọc scene-list.md, sub.srt, sub capcut.srt, voice.mp3 -> timing.md
    python timing_scene.py <thư-mục-tập> --fps 25

Quy tắc: xem QuyTrinh/C5-Timing-Xuat-Clip.md Bước 1. Ghi timing.md (có cột khung hình theo làm tròn luỹ kế).
"""
import argparse
import difflib
import os
import re
import subprocess
import sys
import unicodedata


def norm(s):
    s = unicodedata.normalize("NFD", s.lower().replace("đ", "d"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"(?<=\d)[.,](?=\d)", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def ts(t):
    h, m, r = t.split(":")
    s, ms = r.replace(".", ",").split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def read_srt(path):
    raw = open(path, encoding="utf-8-sig").read().replace("\r\n", "\n")
    cues = []
    for blk in re.split(r"\n\s*\n", raw.strip()):
        ln = blk.split("\n")
        m = next((re.match(r"(\S+)\s*-->\s*(\S+)", x) for x in ln if "-->" in x), None)
        if not m:
            continue
        text = " ".join(x for x in ln[ln.index(next(x for x in ln if "-->" in x)) + 1:]).strip()
        cues.append({"s": ts(m.group(1)), "e": ts(m.group(2)), "t": text, "n": norm(text)})
    return cues


def read_scenes(path):
    rows = []
    for l in open(path, encoding="utf-8-sig"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 7 and c[0].isdigit():
            rows.append({"stt": c[0], "text": c[2], "n": norm(c[2]), "kind": c[3]})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--fps", type=int, default=25)
    ap.add_argument("--out", default="timing.md")
    a = ap.parse_args()
    F = a.folder
    scenes = read_scenes(os.path.join(F, "scene-list.md"))
    tts = read_srt(os.path.join(F, "sub.srt"))
    cap_name = next(n for n in os.listdir(F) if n.lower() in ("sub-capcut.srt", "sub capcut.srt"))
    cap = read_srt(os.path.join(F, cap_name))

    # nối chữ TTS thành 1 chuỗi, nhớ ranh giới cue
    big, pos = "", []
    for c in tts:
        pos.append(len(big))
        big += c["n"]
    pos.append(len(big))

    def tts_time(off):
        i = max(k for k in range(len(tts)) if pos[k] <= off)
        c = tts[i]
        span = max(1, pos[i + 1] - pos[i])
        frac = (off - pos[i]) / span
        return c["s"] + frac * (c["e"] - c["s"]), frac > 0.02

    ptr = 0
    res = []
    for sc in scenes:
        key = sc["n"][:28]
        off = big.find(key, ptr)
        if off < 0:
            key = sc["n"][:14]
            off = big.find(key, ptr)
        if off < 0:
            res.append({"stt": sc["stt"], "tts": None, "mid": False})
            continue
        t, mid = tts_time(off)
        res.append({"stt": sc["stt"], "tts": t, "mid": mid})
        ptr = off + len(key)

    # đối chứng CapCut: nối chữ các cue quanh mốc TTS, tìm đầu câu (cả khi câu bắt đầu giữa/cuối 1 cue), nội suy theo ký tự
    for r, sc in zip(res, scenes):
        r["cc"] = None
        ref = r["tts"]
        if ref is None:
            continue
        win = [c for c in cap if c["s"] >= ref - 4 and c["s"] <= ref + 4 and c["n"]]
        if not win:
            continue
        cb, cp = "", []
        for c in win:
            cp.append(len(cb))
            cb += c["n"]
        cp.append(len(cb))
        found = None
        for L in (16, 11, 7):
            key = sc["n"][:L]
            if len(key) < L:
                continue
            hits = [m.start() for m in re.finditer(re.escape(key), cb)]
            if hits:
                # chọn vị trí có thời gian gần mốc TTS nhất
                def tt(o):
                    i = max(k for k in range(len(win)) if cp[k] <= o)
                    c = win[i]
                    return c["s"] + (o - cp[i]) / max(1, cp[i + 1] - cp[i]) * (c["e"] - c["s"])
                found = min((tt(o) for o in hits), key=lambda x: abs(x - ref))
                break
        if found is None:
            # đầu câu bị nhận dạng khác chữ (số/đọc khác) -> dò bằng đoạn sâu hơn trong câu rồi lùi về theo tốc độ đọc của cue
            for k in (10, 16, 22, 30):
                key = sc["n"][k:k + 11]
                if len(key) < 11:
                    continue
                hits = [m.start() for m in re.finditer(re.escape(key), cb)]
                if not hits:
                    continue
                o = hits[0]
                i = max(j for j in range(len(win)) if cp[j] <= o)
                c = win[i]
                rate = (c["e"] - c["s"]) / max(1, len(c["n"]))
                t0 = c["s"] + (o - cp[i]) * rate - k * rate
                found = t0
                break
        if found is None:
            pre = sc["n"][:30]
            best = None
            for c in win:
                m = difflib.SequenceMatcher(None, pre, c["n"]).find_longest_match(0, len(pre), 0, len(c["n"]))
                if m.size >= 8 and (best is None or m.size > best[0]):
                    off = max(0, m.b - m.a)
                    best = (m.size, c["s"] + off / max(1, len(c["n"])) * (c["e"] - c["s"]))
            found = best[1] if best else None
        r["cc"] = found

    # chọn mốc
    for i, r in enumerate(res):
        note = []
        if r["tts"] is None:
            r["pick"] = r["cc"]
            note.append("chỉ CapCut" if r["cc"] is not None else "KHÔNG ĐỊNH VỊ ĐƯỢC")
            note.append("nghe lại")
        else:
            r["pick"] = r["tts"]
            if r["cc"] is None:
                note.append("chỉ TTS")
            else:
                d = abs(r["cc"] - r["tts"])
                if d > 1.0:
                    note.append("DỪNG HỎI (chênh > 1s)")
                elif d > 0.5:
                    note.append("nghe lại")
            if r["mid"]:
                note.append("nội suy giữa cue")
        r["note"] = ", ".join(note) or "TTS"
    res[0]["pick"] = 0.0
    res[0]["note"] = (res[0]["note"] + ", 0s").replace("TTS, 0s", "0s")

    # kết thúc scene cuối
    last_end = max(tts[-1]["e"], cap[-1]["e"])
    try:
        dur = float(subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(F, "voice.mp3")]).decode().strip())
    except Exception:
        dur = None
    end_note = f"kết thúc cue cuối: TTS {tts[-1]['e']:.3f}s, CapCut {cap[-1]['e']:.3f}s" + (f", voice.mp3 {dur:.3f}s" if dur else "")

    # kiểm tra tăng dần
    bad = [(res[i - 1]["stt"], res[i]["stt"]) for i in range(1, len(res)) if res[i]["pick"] is None or res[i - 1]["pick"] is None or res[i]["pick"] <= res[i - 1]["pick"]]

    # khung hình luỹ kế
    fr = [round(r["pick"] * a.fps) if r["pick"] is not None else None for r in res]
    endf = round(last_end * a.fps)
    L = ["# timing.md — mốc thời gian mỗi scene (C5 Bước 1)", "",
         f"> Mốc chính: `sub.srt` (TTS). Đối chứng: `{cap_name}`. fps = {a.fps}. Khung hình tính luỹ kế: `round(mốc × fps)` từ 0; số khung = khung kết thúc − khung bắt đầu.",
         f"> {end_note}. Kết thúc scene cuối dùng {last_end:.3f}s (giá trị lớn hơn giữa 2 file).", "",
         "| STT scene | Bắt đầu TTS (s) | Bắt đầu CapCut (s) | Chênh (s) | Bắt đầu chọn (s) | Kết thúc (s) | Khung đầu | Số khung | Ghi chú |",
         "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(res):
        nxt = res[i + 1]["pick"] if i + 1 < len(res) else last_end
        end_s = nxt
        f0 = fr[i]
        f1 = fr[i + 1] if i + 1 < len(res) else endf
        cc = f"{r['cc']:.3f}" if r["cc"] is not None else "—"
        tt = f"{r['tts']:.3f}" if r["tts"] is not None else "—"
        d = f"{r['cc'] - r['tts']:+.3f}" if (r["cc"] is not None and r["tts"] is not None) else "—"
        pk = f"{r['pick']:.3f}" if r["pick"] is not None else "—"
        L.append(f"| {r['stt']} | {tt} | {cc} | {d} | {pk} | {end_s:.3f} | {f0} | {(f1 - f0) if (f0 is not None and f1 is not None) else '—'} | {r['note']} |")
    flag = sum("nghe lại" in r["note"] for r in res)
    only = sum(r["note"].startswith("chỉ TTS") for r in res)
    ok = sum(r["note"] in ("TTS", "0s") for r in res)
    L += ["", f"Thống kê: {len(res)} scene — bình thường {ok}, chỉ TTS {only}, gắn cờ \"nghe lại\" {flag}; lỗi thứ tự: {len(bad)}."]
    open(os.path.join(F, a.out), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{len(res)} scene | binh thuong {ok} | chi TTS {only} | nghe lai {flag} | loi thu tu {bad} | tong khung {endf}")


if __name__ == "__main__":
    main()

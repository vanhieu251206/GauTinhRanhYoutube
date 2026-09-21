# -*- coding: utf-8 -*-
"""
xuat_clip.py — C5 Bước 2: xuất toàn bộ clip câm theo timing.md + cột "Loại ảnh" của scene-list.md.

    python xuat_clip.py "Bai-Dang/Tap 9 - Buffet Lau"
    python xuat_clip.py <thư-mục-tập> --entrance "019=rise,020=pop"   # chỉ định kiểu xuất hiện icon theo STT (còn lại xoay vòng)

- AI gen / Crop nguồn thật -> clips/scene-NNN.mp4 từ Anh Video/NNN.jpg (ảnh tĩnh, phóng 1920x1080)
- Icon động -> clips/scene-NNN.mp4 từ Anh Video/NNN.png, ghép nền kẻ ô, hiệu ứng xuất hiện rồi đứng yên
Đọc số khung từ cột "Số khung" của timing.md (đã làm tròn luỹ kế). Kết thúc: in kiểm tra tổng số khung.
"""
import argparse
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CYCLE = ["pop", "rise", "slide-left", "fade", "drop", "slide-right"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--fps", type=int, default=25)
    ap.add_argument("--entrance", default="")
    ap.add_argument("--bg-scroll", type=float, default=60.0, help="tốc độ nền kẻ ô của scene Icon động cuộn xuống (px/giây), 0 = đứng yên")
    ap.add_argument("--only-icon", action="store_true", help="chỉ xuất lại các scene Icon động")
    ap.add_argument("--bg", default=os.path.join(ROOT, "Fanpage-Asset", "Nen-Luoi-O", "nen-luoi-o.png"))
    a = ap.parse_args()
    F = a.folder
    emap = dict(x.split("=") for x in a.entrance.split(",") if "=" in x)
    frames = {}
    for l in open(os.path.join(F, "timing.md"), encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 9 and c[0].isdigit():
            frames[c[0]] = int(c[7])
    kind = {}
    for l in open(os.path.join(F, "scene-list.md"), encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 7 and c[0].isdigit():
            kind[c[0]] = c[3]
    assert set(frames) == set(kind), "timing.md và scene-list.md lệch số scene"
    out = os.path.join(F, "clips")
    os.makedirs(out, exist_ok=True)
    k = 0
    fail = []
    for stt in sorted(frames):
        n = frames[stt]
        dst = os.path.join(out, f"scene-{stt}.mp4")
        if kind[stt] == "Icon động":
            src = os.path.join(F, "Anh Video", f"{stt}.png")
            ent = emap.get(stt) or CYCLE[k % len(CYCLE)]
            k += 1
            cmd = [sys.executable, os.path.join(ROOT, "Cong-Cu", "icon-anim", "icon_anim.py"), src, "-o", out, "--fps", str(a.fps),
                   "--frames", str(n), "--name", f"scene-{stt}.mp4", "--bg", a.bg, "--entrance", ent, "--bg-scroll", str(a.bg_scroll)]
        elif a.only_icon:
            continue
        else:
            src = os.path.join(F, "Anh Video", f"{stt}.jpg")
            cmd = ["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", src, "-r", str(a.fps), "-frames:v", str(n),
                   "-vf", "scale=1920:1080:flags=lanczos,setsar=1", "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-an", dst]
            ent = ""
        if not os.path.exists(src):
            fail.append((stt, "thiếu ảnh"))
            continue
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(dst):
            fail.append((stt, r.stderr[-200:]))
        else:
            print(f"scene-{stt}.mp4  {n} khung  {kind[stt]} {ent}", flush=True)
    # kiểm tra
    tot = 0
    bad = []
    for stt in sorted(frames):
        dst = os.path.join(out, f"scene-{stt}.mp4")
        if not os.path.exists(dst):
            bad.append((stt, "không có file"))
            continue
        o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames", "-show_entries", "stream=nb_read_frames,width,height",
                            "-of", "csv=p=0", dst], capture_output=True, text=True).stdout.strip().split(",")
        w, h, nb = int(o[0]), int(o[1]), int(o[2])
        tot += nb
        if nb != frames[stt] or (w, h) != (1920, 1080) or os.path.getsize(dst) < 2000:
            bad.append((stt, f"{nb} khung, {w}x{h}, {os.path.getsize(dst)}B (cần {frames[stt]})"))
    print(f"XONG: {len(frames) - len(bad)}/{len(frames)} clip đạt; tổng khung {tot} (timing.md: {sum(frames.values())}); lỗi: {fail + bad}")


if __name__ == "__main__":
    main()

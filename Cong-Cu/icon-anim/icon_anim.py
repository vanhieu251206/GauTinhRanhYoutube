# -*- coding: utf-8 -*-
"""
icon_anim.py — dựng clip chuyển động nền trong suốt (MOV ProRes 4444) từ icon PNG đã tách nền.

    python icon_anim.py icon.png                      # -> icon_anim.mov cạnh file gốc
    python icon_anim.py thu-muc-icon -o clips          # cả thư mục, mỗi icon 1 clip
    python icon_anim.py icon.png --dur 4 --preset drift --shadow
    python icon_anim.py icon.png --preset random       # chọn preset ngẫu nhiên (ổn định theo tên file)

Preset (chọn linh hoạt theo scene, đừng dùng 1 kiểu cho cả tập):
    still  (mặc định) chỉ có hiệu ứng xuất hiện, sau đó đứng yên hoàn toàn
    float  lơ lửng lên xuống + nghiêng nhẹ + trôi ngang chậm (mặc định)
    drift  trôi ngang là chính, ít nhấp nhô
    pulse  phồng xẹp nhẹ như thở, gần như đứng yên
    swing  lắc qua lại rõ hơn (nhấn mạnh)
Hiệu ứng xuất hiện (--entrance): pop (bật to, nảy nhẹ - mặc định) | rise (trồi lên + hiện dần) | drop (rơi xuống, nảy nhẹ)
    | slide-left / slide-right (trượt vào từ bên) | fade (hiện dần). Thời lượng --enter-dur (mặc định 0.6s). --nopop bỏ hiệu ứng.

    python icon_anim.py icon.png --bg ../../Fanpage-Asset/Nen-Luoi-O/nen-luoi-o.png   # ghép lên nền -> .mp4 (nhẹ, dùng thẳng như clip scene)

Không có --bg: ra .mov ProRes 4444 nền trong suốt (nặng). Có --bg: ra .mp4 H.264 đã có nền, không cần track nền ở CapCut.

Cần: Python 3, pillow, ffmpeg trong PATH. Khung 1920x1080 nền trong suốt: đặt lên timeline CapCut là icon nằm giữa.
"""
import argparse
import math
import os
import random
import subprocess
import sys
import zlib

from PIL import Image, ImageDraw, ImageFilter

ENTRANCES = ("pop", "rise", "drop", "slide-left", "slide-right", "fade")
PRESETS = {
    "still": (0, 0.0, 0, 0.0),   # mặc định: chỉ hiệu ứng xuất hiện rồi đứng yên
    #         bob_px  sway_deg  drift_px  breathe
    "float": (22, 3.2, 26, 0.0),
    "drift": (8, 1.5, 60, 0.0),
    "pulse": (6, 0.8, 0, 0.035),
    "swing": (14, 6.0, 20, 0.0),
}


def back(t, s=1.9):
    t = min(max(t, 0), 1) - 1
    return 1 + (s + 1) * t ** 3 + s * t ** 2


def make_shadow():
    sh = Image.new("L", (600, 90), 0)
    ImageDraw.Draw(sh).ellipse((40, 25, 560, 65), fill=255)
    return sh.filter(ImageFilter.GaussianBlur(18))


def render(src, out, a):
    W, H, FPS = a.width, a.height, a.fps
    item = Image.open(src).convert("RGBA")
    bbox = item.getchannel("A").getbbox()
    if bbox:
        item = item.crop(bbox)
    k0 = min(a.height_px / item.height, a.max_width / item.width)
    item = item.resize((max(1, round(item.width * k0)), max(1, round(item.height * k0))), Image.LANCZOS)
    bg = Image.open(a.bg).convert("RGBA").resize((W, H), Image.LANCZOS) if a.bg else None
    preset = a.preset
    if preset == "random":
        preset = sorted(PRESETS)[zlib.crc32(os.path.basename(src).encode()) % len(PRESETS)]
    bob_px, sway_deg, drift_px, breathe = PRESETS[preset]
    shadow = make_shadow() if a.shadow else None
    period = a.period

    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-"] + (
        ["-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-an", out] if bg
        else ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-qscale:v", "14", "-alpha_bits", "8", out])
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    ED = a.enter_dur
    cache = None
    static_layer = None
    scroll = bool(bg is not None and a.bg_scroll)
    if scroll:  # nền lặp theo chu kỳ ô lưới (bg_period px) để cuộn xuống liền mạch, không có mối nối
        P = a.bg_period
        tall = Image.new("RGBA", (W, H + 2 * P))
        tile = bg.crop((0, 0, W, P))
        for y in range(0, H + 2 * P, P):
            tall.paste(tile, (0, y))

    def bg_at(t):
        if not scroll:
            return bg.copy() if bg else Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dy = (a.bg_scroll * t) % P
        return tall.transform((W, H), Image.AFFINE, (1, 0, 0, 0, 1, P - dy), resample=Image.BILINEAR)
    for f in range(a.frames or round(FPS * a.dur)):
        t = f / FPS
        if cache is not None and t > ED + 0.7 and not scroll:
            p.stdin.write(cache)
            continue
        if static_layer is not None and scroll:
            fr = bg_at(t)
            fr.alpha_composite(static_layer)
            p.stdin.write(fr.tobytes())
            continue
        ox = oy = 0.0
        if a.nopop:
            pop, fade, settle = 1.0, 1.0, 1.0
        else:
            e = min(1.0, t / ED)
            cub = 1 - (1 - e) ** 3
            pop, fade, settle = 1.0, 1.0, min(1, max(0, (t - ED) / 0.6))
            if a.entrance == "pop":
                pop, fade = back(t / ED), min(1, t / (ED * 0.35))
            elif a.entrance == "rise":
                oy, fade = (1 - cub) * 140, min(1, e * 1.6)
            elif a.entrance == "drop":
                oy, fade = -(1 - back(e, 1.4)) * 220, min(1, e * 2.5)
            elif a.entrance == "slide-left":
                ox, fade = -(1 - cub) * 420, min(1, e * 2)
            elif a.entrance == "slide-right":
                ox, fade = (1 - cub) * 420, min(1, e * 2)
            elif a.entrance == "fade":
                fade = e
        ph = 2 * math.pi * t / period
        bob = math.sin(ph) * bob_px * settle
        sway = math.sin(ph + 0.6) * sway_deg * settle
        drift = math.sin(2 * math.pi * t / (period * 2)) * drift_px * settle
        sc = max(0.01, pop) * (1 + breathe * math.sin(ph) * settle)
        im = item.resize((max(1, round(item.width * sc)), max(1, round(item.height * sc))), Image.LANCZOS)
        im = im.rotate(sway, resample=Image.BICUBIC, expand=True)
        if fade < 1:
            r, g, b, al = im.split()
            im.putalpha(al.point(lambda v: int(v * fade)))
        frame = bg_at(t)
        if shadow is not None:
            k = (1 - bob / 90) * min(1, pop)
            s2 = shadow.resize((max(1, int(600 * k)), max(1, int(90 * k))), Image.LANCZOS)
            dark = Image.new("RGBA", s2.size, (70, 50, 30, 255))
            dark.putalpha(s2.point(lambda v: int(v * 0.30 * fade)))
            frame.alpha_composite(dark, (int(W / 2 + drift * 0.4 - s2.width / 2), int(H / 2 + a.height_px / 2 - 15 - s2.height / 2)))
        frame.alpha_composite(im, (int(W / 2 + drift + ox - im.width / 2), int(H / 2 + bob + oy - im.height / 2)))
        raw = frame.tobytes()
        if a.preset == "still" and t > ED + 0.65:
            cache = raw
            if scroll:
                static_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                static_layer.alpha_composite(im, (int(W / 2 + drift + ox - im.width / 2), int(H / 2 + bob + oy - im.height / 2)))
        p.stdin.write(raw)
    p.stdin.close()
    p.wait()
    return preset


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="file PNG hoặc thư mục chứa PNG")
    ap.add_argument("-o", "--out", help="thư mục xuất (mặc định: cạnh file gốc)")
    ap.add_argument("--dur", type=float, default=5.0, help="thời lượng giây (mặc định 5)")
    ap.add_argument("--preset", default="still", choices=list(PRESETS) + ["random"])
    ap.add_argument("--period", type=float, default=2.5, help="chu kỳ lơ lửng, giây")
    ap.add_argument("--height-px", type=int, default=700, help="chiều cao icon trên khung")
    ap.add_argument("--shadow", action="store_true", help="thêm bóng dưới sàn (mặc định tắt)")
    ap.add_argument("--bg", help="ảnh nền 1920x1080 để ghép sẵn (ra .mp4 thay vì .mov trong suốt)")
    ap.add_argument("--max-width", type=int, default=1500, help="bề ngang tối đa của icon/sơ đồ trên khung")
    ap.add_argument("--entrance", default="pop", choices=ENTRANCES, help="kiểu hiệu ứng xuất hiện")
    ap.add_argument("--enter-dur", type=float, default=0.6, help="thời lượng hiệu ứng xuất hiện (giây)")
    ap.add_argument("--bg-scroll", type=float, default=0.0, help="tốc độ nền cuộn XUỐNG (px/giây), 0 = nền đứng yên; gợi ý 60")
    ap.add_argument("--bg-period", type=int, default=100, help="chu kỳ lặp của nền theo chiều dọc (px) — nền kẻ ô mặc định là 100")
    ap.add_argument("--nopop", action="store_true", help="bỏ hiệu ứng bật vào")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--fps", type=int, default=30, help="C5 dùng 25 để khớp clip ảnh tĩnh")
    ap.add_argument("--frames", type=int, help="số khung hình chính xác (ưu tiên hơn --dur) — lấy từ timing C5")
    ap.add_argument("--name", help="tên file ra (chỉ khi input là 1 file), VD scene-007.mov")
    a = ap.parse_args()

    files = ([os.path.join(a.input, f) for f in sorted(os.listdir(a.input)) if f.lower().endswith(".png")]
             if os.path.isdir(a.input) else [a.input])
    if not files:
        sys.exit("Không thấy file PNG nào")
    for i, src in enumerate(files, 1):
        base = os.path.splitext(os.path.basename(src))[0].replace("_nobg", "")
        od = a.out or os.path.dirname(os.path.abspath(src))
        os.makedirs(od, exist_ok=True)
        out = os.path.join(od, a.name if (a.name and len(files) == 1) else base + ("_anim.mp4" if a.bg else "_anim.mov"))
        used = render(src, out, a)
        print(f"[{i}/{len(files)}] {os.path.basename(out)}  (preset {used})")


if __name__ == "__main__":
    main()

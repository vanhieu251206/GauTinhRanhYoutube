# -*- coding: utf-8 -*-
"""
remove_bg.py — Tách nền TRẮNG (hoặc nền đồng màu) khỏi ảnh icon/đồ vật, xuất PNG trong suốt.

Không cần AI/mạng. Chạy nhanh, offline, dành cho ảnh render nền trắng (VD icon 3D gen bằng AI).
Chất lượng tương đương công cụ trả phí cho nền trắng phẳng nhờ 5 kỹ thuật:
  1. Đoán màu nền từ viền ảnh (không giả định phải đúng #FFFFFF).
  2. Chỉ xoá vùng nền NỐI VỚI MÉP ẢNH  → phần trắng BÊN TRONG vật thể (mặt đồng hồ, đĩa sứ) được giữ.
  3. (Tuỳ chọn) xoá luôn "lỗ" nền kín bên trong (VD khoảng trống giữa quai nồi, tam giác cân) nếu trắng thuần.
  4. Alpha mềm ở đường viền bằng phép tách nền đã biết màu (alpha matting cho nền đơn sắc) → mép mượt, không răng cưa.
  5. Khử viền trắng (color decontamination): trả màu vật thể thật ở mép, không còn quầng trắng khi đặt lên nền tối.

Cách dùng:
  python remove_bg.py anh.jpg                       # → anh_nobg.png cạnh file gốc
  python remove_bg.py thu-muc-anh -o thu-muc-ra     # xử lý cả thư mục
  python remove_bg.py anh.jpg --preview             # thêm ảnh xem thử trên nền caro + nền tối
  python remove_bg.py anh.jpg --tol 20 --holes off  # chỉnh độ nhạy / không xoá lỗ kín
  python remove_bg.py anh.jpg --trim 24             # cắt sát vật thể, chừa lề 24 px

Tham số chính:
  --tol N        Độ lệch màu so với nền được coi là nền (0-60, mặc định 14). Tăng nếu còn sót nền xám nhạt / nhiễu JPEG.
  --band N       Bề rộng dải viền tính alpha mềm (px, mặc định 3). Tăng nếu mép còn cứng, giảm nếu mép bị mờ.
  --holes MODE   auto (mặc định) | on | off. Xoá các lỗ nền kín bên trong vật thể.
  --hole-tol N   Độ lệch tối đa để một lỗ kín được coi là nền (mặc định 4, chặt hơn --tol để không ăn nhầm vùng sáng của vật thể).
  --hole-min N   Diện tích tối thiểu (px) của lỗ kín để bị xoá (mặc định 250).
  --speck N      Xoá các đốm rời nhỏ hơn N px còn sót ngoài vật thể (mặc định 40).
  --trim N       Cắt sát vật thể, chừa lề N px (mặc định: không cắt).
  --size N       Thu nhỏ cạnh dài về N px (mặc định: giữ nguyên).
"""
import argparse
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

EXTS = (".jpg", ".jpeg", ".png", ".webp", ".bmp")


def estimate_bg(rgb):
    """Màu nền = trung vị các pixel ở viền ảnh."""
    h, w, _ = rgb.shape
    edge = np.concatenate([rgb[0, :, :], rgb[-1, :, :], rgb[:, 0, :], rgb[:, -1, :]], axis=0)
    return np.median(edge, axis=0).astype(np.float32)


def remove_bg(img, tol=14, band=3, holes="auto", hole_tol=4, hole_min=250, speck=None, shadow=False, shadow_sat=22, shadow_dark=90):
    rgb = np.asarray(img.convert("RGB")).astype(np.float32)
    h, w, _ = rgb.shape
    bg = estimate_bg(rgb)

    # khoảng cách màu (Chebyshev) tới nền
    dist = np.abs(rgb - bg).max(axis=2)
    near_bg = dist <= tol

    st8 = np.ones((3, 3), dtype=int)
    lab, n = ndi.label(near_bg, structure=st8)
    hard_bg = np.zeros((h, w), dtype=bool)
    if n:
        border_labels = np.unique(np.concatenate([lab[0, :], lab[-1, :], lab[:, 0], lab[:, -1]]))
        border_labels = border_labels[border_labels > 0]
        hard_bg = np.isin(lab, border_labels)

    # lỗ nền kín bên trong (không nối với mép)
    if holes != "off" and n:
        strict = dist <= hole_tol
        lab2, n2 = ndi.label(strict, structure=st8)
        if n2:
            sizes = ndi.sum(strict, lab2, index=np.arange(1, n2 + 1))
            touch = np.isin(np.arange(1, n2 + 1), border_labels_from(lab2))
            keep = np.zeros(n2 + 1, dtype=bool)
            for i, s in enumerate(sizes, start=1):
                if (not touch[i - 1]) and s >= hole_min:
                    keep[i] = True
            hard_bg |= keep[lab2]

    # bóng đổ mờ (xám nhạt, ít sắc độ) dính vào nền: coi là nền. Tuỳ chọn --shadow
    if shadow:
        mx, mn = rgb.max(axis=2), rgb.min(axis=2)
        cand = ((mx - mn) <= shadow_sat) & (mn >= bg.min() - shadow_dark) & ~hard_bg
        cand = ndi.binary_opening(cand, structure=np.ones((3, 3)), iterations=1) | (cand & ndi.binary_dilation(hard_bg, iterations=1))
        labc, nc = ndi.label(cand | hard_bg, structure=st8)
        if nc:
            seeds = np.unique(labc[hard_bg])
            seeds = seeds[seeds > 0]
            grown = np.isin(labc, seeds)
            # chỉ nhận phần mở rộng là vùng phẳng-mờ (gradient thấp), tránh ăn mép đĩa sứ có chi tiết
            gy, gx = np.gradient(rgb.mean(axis=2))
            smooth = ndi.uniform_filter(np.hypot(gx, gy), 7) < 3.0
            hard_bg |= grown & smooth

    fg = ~hard_bg

    # dọn đốm rời nhỏ (nhiễu JPEG) ở ngoài vật thể
    if speck is None:
        speck = max(40, int(h * w * 0.0006))
    if speck > 0:
        lab_fg, nf = ndi.label(fg, structure=st8)
        if nf:
            sizes = ndi.sum(fg, lab_fg, index=np.arange(1, nf + 1))
            small = np.zeros(nf + 1, dtype=bool)
            small[1:] = sizes < speck
            fg &= ~small[lab_fg]

    # ---- alpha mềm + khử viền trắng ở dải viền ----
    edt_bg = ndi.distance_transform_edt(fg)          # khoảng cách từ pixel vật thể tới nền gần nhất
    sure_fg = fg & (edt_bg > band)
    alpha = np.where(fg, 1.0, 0.0).astype(np.float32)
    out_rgb = rgb.copy()

    if sure_fg.any():
        dist_to_sure, (iy, ix) = ndi.distance_transform_edt(~sure_fg, return_indices=True)
        f_est = rgb[iy, ix]                             # màu vật thể "chắc chắn" gần nhất

        # dải viền: pixel vật thể sát nền + pixel nền sát vật thể
        edt_fg = ndi.distance_transform_edt(~fg)         # khoảng cách từ pixel nền tới vật thể gần nhất
        band_mask = (fg & (edt_bg <= band)) | ((~fg) & (edt_fg <= 1.5))

        e = bg[None, None, :] - f_est                    # vector nền - vật thể
        d = bg[None, None, :] - rgb                      # vector nền - pixel hiện tại
        ee = (e * e).sum(axis=2)
        de = (d * e).sum(axis=2)
        proj = np.clip(de / np.maximum(ee, 1.0), 0.0, 1.0)

        usable = band_mask & (ee > 900.0) & (dist_to_sure <= band + 6)   # màu vật thể đủ khác nền mới tách được
        a = alpha.copy()
        a[usable] = proj[usable]
        a[usable & (proj < 0.04)] = 0.0
        alpha = a

        # trả lại màu thật (bỏ phần trắng pha vào mép)
        m = usable & (alpha > 0.02)
        a3 = alpha[..., None]
        fgcol = (rgb - (1.0 - a3) * bg[None, None, :]) / np.maximum(a3, 0.02)
        fgcol = np.clip(fgcol, 0, 255)
        out_rgb[m] = fgcol[m]

    alpha8 = np.clip(alpha * 255.0 + 0.5, 0, 255).astype(np.uint8)
    rgba = np.dstack([np.clip(out_rgb, 0, 255).astype(np.uint8), alpha8])
    # pixel trong suốt: đặt RGB = màu vật thể gần nhất để khỏi loang viền khi phóng to/co giãn
    transparent = alpha8 == 0
    if sure_fg.any() and transparent.any():
        rgba[transparent, :3] = f_est[transparent].astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def border_labels_from(lab):
    b = np.unique(np.concatenate([lab[0, :], lab[-1, :], lab[:, 0], lab[:, -1]]))
    return b[b > 0]


def trim(rgba, margin):
    a = np.asarray(rgba)[..., 3]
    ys, xs = np.where(a > 8)
    if len(ys) == 0:
        return rgba
    y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    h, w = a.shape
    y0 = max(0, y0 - margin); x0 = max(0, x0 - margin)
    y1 = min(h, y1 + margin + 1); x1 = min(w, x1 + margin + 1)
    return rgba.crop((x0, y0, x1, y1))


def make_preview(rgba, path):
    """Ảnh xem thử: nền caro | nền tối navy | nền kem, để kiểm tra viền."""
    w, h = rgba.size
    scale = min(1.0, 600.0 / max(w, h))
    r = rgba.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    pw, ph = r.size

    def compose(bgc):
        base = Image.new("RGBA", (pw, ph), bgc)
        base.alpha_composite(r)
        return base

    check = Image.new("RGBA", (pw, ph), (255, 255, 255, 255))
    cs = 16
    px = check.load()
    for y in range(ph):
        for x in range(pw):
            if ((x // cs) + (y // cs)) % 2 == 0:
                px[x, y] = (204, 204, 204, 255)
    check.alpha_composite(r)
    sheet = Image.new("RGBA", (pw * 3, ph), (255, 255, 255, 255))
    sheet.paste(check, (0, 0))
    sheet.paste(compose((12, 40, 78, 255)), (pw, 0))
    sheet.paste(compose((245, 235, 215, 255)), (pw * 2, 0))
    sheet.convert("RGB").save(path)


def process_file(src, dst, args):
    img = Image.open(src)
    if args.size:
        img.thumbnail((args.size, args.size), Image.LANCZOS)
    out = remove_bg(img, tol=args.tol, band=args.band, holes=args.holes,
                    hole_tol=args.hole_tol, hole_min=args.hole_min, speck=args.speck, shadow=args.shadow)
    if args.trim is not None:
        out = trim(out, args.trim)
    os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
    out.save(dst, "PNG", optimize=True)
    if args.preview:
        make_preview(out, os.path.splitext(dst)[0] + "_preview.jpg")
    return dst


def main():
    ap = argparse.ArgumentParser(description="Tách nền trắng khỏi ảnh, xuất PNG trong suốt.")
    ap.add_argument("input", help="file ảnh hoặc thư mục ảnh")
    ap.add_argument("-o", "--output", help="file/thư mục đầu ra")
    ap.add_argument("--tol", type=float, default=14)
    ap.add_argument("--band", type=int, default=3)
    ap.add_argument("--holes", choices=["auto", "on", "off"], default="auto")
    ap.add_argument("--hole-tol", dest="hole_tol", type=float, default=4)
    ap.add_argument("--hole-min", dest="hole_min", type=int, default=250)
    ap.add_argument("--speck", type=int, default=None, help="xoá đốm rời < N px (mặc định tự tính ~0.06%% diện tích ảnh)")
    ap.add_argument("--shadow", action="store_true", help="xoá cả bóng đổ xám nhạt dính vào nền")
    ap.add_argument("--trim", type=int, default=None, help="cắt sát vật thể, chừa lề N px")
    ap.add_argument("--size", type=int, default=None, help="thu nhỏ cạnh dài về N px")
    ap.add_argument("--preview", action="store_true", help="xuất thêm ảnh xem thử trên nền caro/tối/kem")
    args = ap.parse_args()

    if os.path.isdir(args.input):
        out_dir = args.output or (args.input.rstrip("/\\") + "_nobg")
        files = [f for f in sorted(os.listdir(args.input)) if f.lower().endswith(EXTS)]
        if not files:
            print("Không có ảnh trong thư mục.")
            return 1
        for f in files:
            dst = os.path.join(out_dir, os.path.splitext(f)[0] + "_nobg.png")
            process_file(os.path.join(args.input, f), dst, args)
            print("OK", f, "->", dst)
    else:
        dst = args.output or (os.path.splitext(args.input)[0] + "_nobg.png")
        process_file(args.input, dst, args)
        print("OK", args.input, "->", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())

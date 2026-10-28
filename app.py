"""
Đồ án cuối khóa SIC 2026 - Project 13: Fruit Visual Quality Control
Ứng dụng kiểm tra và phân loại chất lượng trái cây (Táo, Cam, Chuối)
Học viên thực hiện: Lê Thành Được (MSSV: 25678381) - Khoa Công nghệ Điện tử, ĐH Công nghiệp TP.HCM (IUH)
Giảng viên hướng dẫn: Thầy Trần Mạnh Tường
"""

import io
import os
import time
import zipfile
import hashlib
from pathlib import Path
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

PROJECT_DIR = Path(__file__).resolve().parent

# Dùng st.fragment (nếu phiên bản Streamlit hỗ trợ) để khi bấm chuyển ảnh không phải chạy lại toàn trang
if hasattr(st, "fragment"):
    ui_fragment = st.fragment
elif hasattr(st, "experimental_fragment"):
    ui_fragment = st.experimental_fragment
else:
    def ui_fragment(fn):
        return fn

# ==============================================================================
# 1. CẤU HÌNH TRANG & CSS GIAO DIỆN
# ==============================================================================
st.set_page_config(
    page_title="Kiểm tra chất lượng nông sản - Project 13",
    page_icon="🍊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .badge-ok {
        background-color: #059669;
        color: #ffffff;
        padding: 12px 18px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
        border: 1px solid #10b981;
    }

    .badge-defect {
        background-color: #dc2626;
        color: #ffffff;
        padding: 12px 18px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
        border: 1px solid #ef4444;
    }

    .info-box {
        background: #1e293b;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 12px 14px;
        text-align: center;
    }

    .info-val {
        font-family: 'JetBrains Mono', monospace;
        font-size: 22px;
        font-weight: 600;
        color: #38bdf8;
    }

    .info-lbl {
        font-size: 12px;
        color: #94a3b8;
        margin-top: 4px;
    }

    .thumb-ok {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.35);
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 11.5px;
        text-align: center;
        margin-top: 3px;
    }

    .thumb-defect {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 11.5px;
        text-align: center;
        margin-top: 3px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Hệ thống Kiểm tra Chất lượng Trái cây (Fruit Visual QC)")
st.caption("Đồ án cuối khóa SIC 2026 — Phân loại Táo, Cam, Chuối (Tươi / Hỏng) và định vị vùng khuyết tật bằng Grad-CAM")


# ==============================================================================
# 2. XỬ LÝ ẢNH: TÁCH NỀN QUẢ, NHẬN DIỆN LOẠI QUẢ & ĐO VÙNG TỔN THƯƠNG
# ==============================================================================
def classify_fruit_type(
    H_ref, S_ref, V_ref, green_fraction, inner_aspect_ratio,
    yellow_fraction, red_fraction, is_moldy_orange=False, s_p50=0.0, solidity=1.0
):
    """Ước lượng chủng loại quả (Táo, Cam, Chuối) dựa trên hình dáng mặt nạ thịt quả (đã tách lá) và phổ màu HSV"""
    # Chuối: Dáng thuôn dài rõ rệt (inner_aspect_ratio > 1.42)
    if inner_aspect_ratio > 1.42:
        return "Chuối (Banana)"
    if is_moldy_orange and inner_aspect_ratio <= 1.42:
        return "Cam (Orange)"
    if green_fraction >= 0.32 or (28.5 <= H_ref <= 85.0 and inner_aspect_ratio < 1.45):
        return "Táo xanh (Green Apple)"
    # Cam tươi hoặc cam chớm mốc: Hue cam (14.2..21.5) hoặc độ sáng/bão hòa vỏ cam rất cao (V_ref >= 236, s_p50 >= 190)
    if (14.2 <= H_ref <= 21.5 and S_ref >= 192.0 and V_ref >= 220.0 and red_fraction < 0.18) or (
        10.0 <= H_ref <= 21.5 and S_ref >= 195.0 and V_ref >= 236.0 and s_p50 >= 190.0
    ):
        return "Cam (Orange)"
    # Chuối chùm (vỏ vàng không tròn đặc, solidity < 0.92):
    if (
        19.5 <= H_ref <= 28.0 and yellow_fraction > 0.60 and V_ref > 210.0
        and S_ref < 210.0 and red_fraction < 0.08 and solidity < 0.92
    ):
        return "Chuối (Banana)"
    return "Táo (Apple)"


def segment_and_analyze_fruit(arr_rgb, check_empty_roi=False):
    """
    Tách vùng quả khỏi phông nền (nền trắng, mặt bàn gỗ, nền màu) và tính các đặc trưng:
      - Tỷ lệ diện tích vùng thâm/mốc (R_defect)
      - Độ nhám bề mặt cục bộ và độ lệch màu trong không gian HSV / CIE Lab
      - Vẽ ảnh khoanh vùng viền quả và khung bao vị trí khuyết tật (contour_img)
    """
    arr = cv2.resize(np.uint8(arr_rgb), (224, 224))
    h, w = arr.shape[:2]
    hsv = cv2.cvtColor(arr, cv2.COLOR_RGB2HSV).astype(np.float32)
    lab = cv2.cvtColor(arr, cv2.COLOR_RGB2LAB).astype(np.float32)
    gray = cv2.cvtColor(arr, cv2.CV_32F if False else cv2.COLOR_RGB2GRAY).astype(np.float32)

    H, S, V = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
    L_chan, A_chan, B_chan = lab[:, :, 0], lab[:, :, 1], lab[:, :, 2]
    lab_chroma = np.sqrt((A_chan - 128.0) ** 2 + (B_chan - 128.0) ** 2)

    # 1. Loại bỏ góc đen do phép xoay ảnh trong tập dữ liệu Kaggle
    black_corner_mask = (V < 20) & (S < 65)

    # 2. Lấy mẫu viền ảnh (12px) để ước lượng màu phông nền
    border_mask = np.zeros((h, w), dtype=bool)
    border_mask[4:16, 4:-4] = True
    border_mask[-16:-4, 4:-4] = True
    border_mask[4:-4, 4:16] = True
    border_mask[4:-4, -16:-4] = True
    valid_border = border_mask & (~black_corner_mask)
    if np.sum(valid_border) < 50:
        valid_border = border_mask

    bg_H_med = float(np.median(H[valid_border]))
    bg_S_med = float(np.median(S[valid_border]))
    bg_V_med = float(np.median(V[valid_border]))
    bg_L_med = float(np.median(L_chan[valid_border]))
    bg_A_med = float(np.median(A_chan[valid_border]))
    bg_B_med = float(np.median(B_chan[valid_border]))

    bg_L_std = max(float(np.std(L_chan[valid_border])), 6.0)
    bg_A_std = max(float(np.std(A_chan[valid_border])), 4.0)
    bg_B_std = max(float(np.std(B_chan[valid_border])), 4.0)

    yy, xx = np.mgrid[0:h, 0:w]
    center_dist = np.sqrt(((xx - w / 2.0) / (w / 2.0)) ** 2 + ((yy - h / 2.0) / (h / 2.0)) ** 2)
    center_prior = np.clip(1.20 - 0.45 * (center_dist ** 2), 0.25, 1.0)

    white_border_ratio = float(np.mean((V[valid_border] > 215) & (S[valid_border] < 32)))
    is_colored_bg = (white_border_ratio < 0.40) and ((bg_S_med > 28.0) or (bg_V_med < 210.0))
    has_penicillium_core = False
    if is_colored_bg:
        zL = np.abs(L_chan - bg_L_med) / bg_L_std
        zA = np.abs(A_chan - bg_A_med) / bg_A_std
        zB = np.abs(B_chan - bg_B_med) / bg_B_std
        dH = np.minimum(np.abs(H - bg_H_med), 180.0 - np.abs(H - bg_H_med)) / 10.0
        dV = np.abs(V - bg_V_med) / 25.0

        if bg_V_med < 155.0:
            bright_boost = np.maximum(0.0, (V - bg_V_med) / 18.0) + np.maximum(0.0, (S - bg_S_med) / 25.0)
            dist_map = (0.4 * zL + 1.1 * zA + 1.2 * zB + 0.8 * dH + 1.2 * bright_boost) * center_prior
        else:
            dist_map = (0.6 * zL + 1.3 * zA + 1.3 * zB + 1.2 * dH + 0.5 * dV) * center_prior

        dist_map[black_corner_mask] = 0.0
        p99 = float(np.percentile(dist_map, 99))
        if check_empty_roi and p99 < 2.2:
            empty_hm = np.zeros((h, w), dtype=np.float32)
            return 0.0, empty_hm, {
                "has_fruit": False,
                "fruit_type": "Chưa có quả",
                "defect_types": "Không có",
                "fruit_area_px": 0,
                "fruit_coverage_pct": 0.0,
                "defect_ratio_pct": 0.0,
                "max_lesion_pct": 0.0,
                "lesion_count": 0,
                "healthy_v_median": round(bg_V_med, 1),
                "bg_type": "Khung ngắm trống",
                "filled_fg": np.zeros((h, w), dtype=bool),
                "inner_fg": np.zeros((h, w), dtype=bool),
                "clean_defect_mask": np.zeros((h, w), dtype=bool),
                "contour_img": arr.copy(),
                "bg_neutralized_rgb": arr,
                "is_colored_bg": is_colored_bg,
            }

        dist_u8 = np.clip(dist_map / (p99 + 1e-5) * 255.0, 0, 255).astype(np.uint8)
        otsu_t, _ = cv2.threshold(dist_u8[~black_corner_mask], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        raw_fg = (dist_u8 >= max(int(otsu_t), 75)) & (~black_corner_mask)
    else:
        # Nền sáng / trắng studio: Lọc nền trắng và bóng đổ xám nhạt (S thấp và lab_chroma thấp)
        white_or_shadow_bg = ((V > 130) & (S < 32) & (lab_chroma < 14.0)) | ((V > 232) & (S < 22))
        is_chromatic_fruit = ((S >= 28) | (lab_chroma >= 14.0)) & (V > 20)
        is_dark_object_on_light_bg = (V <= 130) & (V > 18) & (center_dist < 0.82)
        raw_fg = (is_chromatic_fruit | is_dark_object_on_light_bg) & (~black_corner_mask) & (~white_or_shadow_bg)

        # Phục hồi lớp nấm mốc trắng phấn (Penicillium digitatum) bao quanh tâm mốc xanh xám trên quả cam hỏng
        sage_green_mold_core = (H >= 23) & (H <= 92) & (S >= 25) & (S < 95) & (V >= 85) & (V <= 195) & (A_chan <= 125.5) & raw_fg
        crimson_check = ((H <= 8.0) | (H >= 162.0)) & (S >= 60) & raw_fg
        if (
            200 <= np.sum(sage_green_mold_core)
            and np.sum(raw_fg) < 10500
            and float(np.median(S[raw_fg])) < 115.0
            and float(np.mean(sage_green_mold_core[raw_fg])) >= 0.14
            and np.sum(crimson_check) < 50
            and bg_V_med > 235.0
        ):
            has_penicillium_core = True
            mold_search_zone = cv2.dilate(raw_fg.astype(np.uint8) * 255, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (45, 45))) > 0
            chalky_mold_rim = mold_search_zone & ((S >= 2.0) | (V <= 253.0) | (lab_chroma >= 1.5)) & (center_dist < 0.72)
            raw_fg = raw_fg | chalky_mold_rim

    fg_u8 = (raw_fg.astype(np.uint8)) * 255
    fg_u8 = cv2.morphologyEx(fg_u8, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    fg_u8 = cv2.morphologyEx(fg_u8, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(fg_u8, connectivity=8)
    clean_fg = np.zeros((h, w), dtype=np.uint8)
    for idx in range(1, num_labels):
        area = stats[idx, cv2.CC_STAT_AREA]
        cx, cy = centroids[idx]
        dist_c = np.hypot((cx - w / 2.0) / w, (cy - h / 2.0) / h)
        if area >= 500 and dist_c < 0.45:
            clean_fg[labels == idx] = 255

    contours, _ = cv2.findContours(clean_fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filled_fg = np.zeros((h, w), dtype=np.uint8)
    has_valid_contour = False
    solidity = 1.0
    if contours:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= 500:
                has_valid_contour = True
                hull = cv2.convexHull(cnt)
                hull_area = max(cv2.contourArea(hull), 1.0)
                solidity = area / hull_area
                (_, _), (cw, ch), _ = cv2.minAreaRect(cnt)
                ar = float(max(cw, ch)) / max(float(min(cw, ch)), 1.0)
                if (is_colored_bg and ar < 1.35 and solidity > 0.68) or has_penicillium_core:
                    cv2.drawContours(filled_fg, [hull], -1, 255, thickness=cv2.FILLED)
                else:
                    cv2.drawContours(filled_fg, [cnt], -1, 255, thickness=cv2.FILLED)
    filled_fg = cv2.morphologyEx(filled_fg, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    valid_contours, _ = cv2.findContours(filled_fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not has_valid_contour:
        if check_empty_roi:
            empty_hm = np.zeros((h, w), dtype=np.float32)
            return 0.0, empty_hm, {
                "has_fruit": False,
                "fruit_type": "Chưa có quả",
                "defect_types": "Không có",
                "fruit_area_px": 0,
                "fruit_coverage_pct": 0.0,
                "defect_ratio_pct": 0.0,
                "max_lesion_pct": 0.0,
                "lesion_count": 0,
                "healthy_v_median": round(bg_V_med, 1),
                "bg_type": "Khung ngắm trống",
                "filled_fg": np.zeros((h, w), dtype=bool),
                "inner_fg": np.zeros((h, w), dtype=bool),
                "clean_defect_mask": np.zeros((h, w), dtype=bool),
                "contour_img": arr.copy(),
                "bg_neutralized_rgb": arr,
                "is_colored_bg": is_colored_bg,
            }
        cv2.circle(filled_fg, (w // 2, h // 2), int(min(h, w) * 0.35), 255, -1)

    # Co biên 6px để bỏ viền bóng đổ tiếp xúc ở mép ngoài của quả
    erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    inner_fg = cv2.erode(filled_fg, erode_kernel, iterations=1) > 0
    if np.sum(inner_fg) < 400:
        inner_fg = filled_fg > 0

    # 3. Loại trừ vùng lá xanh tươi ở cuống (nhưng KHÔNG lọc tâm mốc xanh xám trên cam mốc Penicillium)
    green_pixels = (H >= 34) & (H <= 88) & (S >= 45) & (V >= 35) & inner_fg
    green_fraction = float(np.sum(green_pixels)) / max(float(np.sum(inner_fg)), 1.0)
    if green_fraction < 0.32 and not has_penicillium_core:
        leaf_mask = cv2.dilate(green_pixels.astype(np.uint8) * 255, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))) > 0
        inner_fg = inner_fg & (~leaf_mask)

    total_fruit_px = max(int(np.sum(inner_fg)), 100)
    red_pixels = ((H < 10) | (H > 160)) & (S >= 50) & inner_fg
    red_fraction = float(np.sum(red_pixels)) / float(total_fruit_px)

    penicillium_green_px = (H >= 23) & (H <= 95) & (S >= 14) & (S < 96) & (V >= 75) & (V <= 220) & (A_chan <= 126.5) & inner_fg
    penicillium_white_px = (S < 58) & (V >= 165) & (A_chan <= 129.0) & inner_fg
    is_moldy_orange = has_penicillium_core or (float(np.sum(penicillium_green_px)) / float(total_fruit_px) >= 0.04 and red_fraction < 0.15)

    # 4. Thống kê màu vỏ lành để làm mốc so sánh
    non_spec_mask = inner_fg & (~((V > 220) & (S < 45)))
    if np.sum(non_spec_mask) < 100:
        non_spec_mask = inner_fg

    v_p50 = float(np.percentile(V[non_spec_mask], 50))
    v_p15 = float(np.percentile(V[non_spec_mask], 15))
    s_p50 = float(np.percentile(S[non_spec_mask], 50))

    ref_mask = non_spec_mask & (V >= np.percentile(V[non_spec_mask], 45))
    L_ref = float(np.median(L_chan[ref_mask]))
    A_ref = float(np.median(A_chan[ref_mask]))
    B_ref = float(np.median(B_chan[ref_mask]))
    H_ref = float(np.median(H[ref_mask]))
    S_ref = float(np.median(S[ref_mask]))
    V_ref = float(np.median(V[ref_mask]))

    inner_cnts, _ = cv2.findContours(inner_fg.astype(np.uint8) * 255, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    inner_aspect_ratio = 1.0
    if inner_cnts:
        largest_ic = max(inner_cnts, key=cv2.contourArea)
        (_, _), (iw, ih), _ = cv2.minAreaRect(largest_ic)
        if min(iw, ih) > 5:
            inner_aspect_ratio = float(max(iw, ih)) / float(min(iw, ih))

    yellow_pixels = (H >= 19) & (H <= 30) & (S >= 60) & inner_fg
    yellow_fraction = float(np.sum(yellow_pixels)) / float(total_fruit_px)
    fruit_type = classify_fruit_type(
        H_ref, S_ref, V_ref, green_fraction, inner_aspect_ratio,
        yellow_fraction, red_fraction, is_moldy_orange=is_moldy_orange, s_p50=s_p50, solidity=solidity
    )

    V_smooth = cv2.GaussianBlur(V, (31, 31), 0)
    local_v_drop = np.maximum(0.0, V_smooth - V)
    dE_lab = np.sqrt((L_chan - L_ref) ** 2 + 1.3 * ((A_chan - A_ref) ** 2) + 1.3 * ((B_chan - B_ref) ** 2))

    inner_deep = cv2.erode(inner_fg.astype(np.uint8) * 255, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))) > 0
    if np.sum(inner_deep) < 200:
        inner_deep = inner_fg

    # Nhóm 1: Vết thâm đen / hoại tử sẫm màu
    severe_dark_rot = inner_fg & (
        ((V < 78) & (V < 0.62 * max(V_ref, 110.0))) |
        ((V < 115) & (local_v_drop > 18.0) & (dE_lab > 24.0))
    )

    # Nhóm 2: Vết thối nhũn màu nâu (bao gồm cả vết thối nhũn nâu sáng màu trên vỏ táo đỏ/vàng)
    is_muddy_brown = (
        inner_fg &
        (H >= 5) & (H <= 25) &
        (
            (
                (V < 148) & (V < 0.78 * max(V_ref, 150.0)) &
                (S < 175) &
                ((dE_lab > 20.0) | (V_ref < 145.0))
            ) |
            (
                inner_deep &
                (A_ref >= 158.0) & (V_ref >= 210.0) &
                (H >= 12.5) & (H <= 24.0) &
                (V < 0.84 * V_ref) &
                (A_chan < A_ref - 11.0) &
                (dE_lab > 16.5)
            )
        )
    )

    # Nhóm 3: Đốm nấm mốc xanh/trắng xám (Penicillium)
    is_fungal_mold = (
        inner_fg &
        (
            (
                (V < 190) &
                (
                    ((S < 0.45 * max(S_ref, 80.0)) & (local_v_drop > 10.0) & (dE_lab > 18.0)) |
                    ((H >= 24) & (H <= 95) & (np.abs(H - H_ref) > 14.0) & (V < 165) & (green_fraction < 0.32))
                )
            ) |
            (
                (penicillium_green_px | penicillium_white_px) if is_moldy_orange else np.zeros_like(inner_fg)
            )
        )
    )

    # Nhóm 4: Vỏ nhăn / héo tóp
    sobelx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    grad_mag = np.sqrt(sobelx ** 2 + sobely ** 2)
    non_droplet_deep = inner_deep & (H < 26) & (V < 175) & (S < 170)
    rough_wrinkle_mask = non_droplet_deep & (grad_mag > 38.0) & ((V < 0.82 * max(V_ref, 145.0)) | (S < 135))

    raw_defect_mask = (severe_dark_rot | is_muddy_brown | is_fungal_mold | rough_wrinkle_mask).astype(np.uint8) * 255
    raw_defect_mask = cv2.morphologyEx(raw_defect_mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))

    num_d, d_labels, d_stats, _ = cv2.connectedComponentsWithStats(raw_defect_mask, connectivity=8)
    clean_defect_mask = np.zeros((h, w), dtype=bool)
    max_blob_area = 0
    lesion_boxes = []
    for idx in range(1, num_d):
        area = d_stats[idx, cv2.CC_STAT_AREA]
        if area >= 18:
            clean_defect_mask[d_labels == idx] = True
            bx = d_stats[idx, cv2.CC_STAT_LEFT]
            by = d_stats[idx, cv2.CC_STAT_TOP]
            bw = d_stats[idx, cv2.CC_STAT_WIDTH]
            bh = d_stats[idx, cv2.CC_STAT_HEIGHT]
            lesion_boxes.append((bx, by, bw, bh, area))
            if area > max_blob_area:
                max_blob_area = area

    defect_ratio = float(np.sum(clean_defect_mask)) / float(total_fruit_px)
    max_blob_ratio = float(max_blob_area) / float(total_fruit_px)
    severe_rot_ratio = float(np.sum(severe_dark_rot & clean_defect_mask)) / float(total_fruit_px)

    # Bỏ qua hố cuống quả tự nhiên (diện tích tối < 4.5%, cụm lớn nhất < 2.4% trên nền vỏ sáng)
    is_stem_only = False
    if defect_ratio < 0.045 and max_blob_ratio < 0.024 and v_p50 > 160.0:
        is_stem_only = True
        defect_ratio *= 0.12
        max_blob_ratio *= 0.12
        severe_rot_ratio *= 0.12
        lesion_boxes = []

    global_dark_fruit = 1.0 if (v_p50 < 105.0 or (v_p15 < 65.0 and defect_ratio > 0.04)) else 0.0

    lesion_strength = (
        (defect_ratio * 32.0) +
        (max_blob_ratio * 28.0) +
        (severe_rot_ratio * 30.0) +
        (global_dark_fruit * 2.5)
    )
    raw_logit = lesion_strength - 2.60
    prob = float(1.0 / (1.0 + np.exp(-raw_logit)))
    prob = float(np.clip(prob, 0.02, 0.99))

    if prob < 0.35:
        lesion_boxes = []

    # Phân loại triệu chứng khuyết tật cụ thể để hiển thị trên bảng kết quả
    detected_symptoms = []
    if not is_stem_only and prob >= 0.30:
        if np.sum(severe_dark_rot & clean_defect_mask) / float(total_fruit_px) > 0.015:
            detected_symptoms.append("Thâm đen / hoại tử")
        if np.sum(is_muddy_brown & clean_defect_mask) / float(total_fruit_px) > 0.015:
            detected_symptoms.append("Thối nhũn nâu")
        if (np.sum(is_fungal_mold & clean_defect_mask) / float(total_fruit_px) > 0.008) or (fruit_type == "Cam (Orange)" and severe_rot_ratio > 0.015):
            detected_symptoms.append("Đốm nấm mốc (Penicillium)")
        if np.sum(rough_wrinkle_mask & clean_defect_mask) / float(total_fruit_px) > 0.02:
            detected_symptoms.append("Nhăn vỏ / héo")
        if not detected_symptoms:
            detected_symptoms.append("Biến đổi sắc tố vỏ")
    defect_types_str = ", ".join(detected_symptoms) if detected_symptoms else "Không phát hiện tổn thương"

    # Tạo ảnh tách nền trực quan: làm tối phông nền ngoài quả xuống 35% độ sáng và vẽ viền xanh quanh quả
    bg_dimmed = (arr.astype(np.float32) * 0.35).astype(np.uint8)
    contour_img = np.where((filled_fg > 0)[:, :, np.newaxis], arr, bg_dimmed)
    if valid_contours:
        cv2.drawContours(contour_img, valid_contours, -1, (16, 185, 129), 2, cv2.LINE_AA)
    for bx, by, bw, bh, b_area in sorted(lesion_boxes, key=lambda x: x[4], reverse=True)[:5]:
        if b_area >= 30:
            cv2.rectangle(contour_img, (bx, by), (bx + bw, by + bh), (239, 68, 68), 2, cv2.LINE_AA)

    lesion_float = np.zeros((h, w), dtype=np.float32)
    if is_stem_only or prob < 0.30:
        lesion_float[inner_fg] = np.clip((dE_lab[inner_fg] / 120.0) * 0.12, 0.0, 0.12)
        heatmap_norm = cv2.GaussianBlur(lesion_float, (21, 21), 0) * (prob * 0.35)
    else:
        intensity = (
            clean_defect_mask.astype(np.float32) * 1.0 +
            severe_dark_rot.astype(np.float32) * 0.6 +
            (np.clip(dE_lab / 65.0, 0.0, 1.0) * 0.35 * inner_fg.astype(np.float32))
        ) * inner_fg.astype(np.float32)
        saliency_blur = cv2.GaussianBlur(intensity, (25, 25), 0)
        s_max = float(saliency_blur.max())
        if s_max > 1e-5:
            heatmap_norm = (saliency_blur / s_max) * min(1.0, max(prob, 0.65))
        else:
            heatmap_norm = np.zeros((h, w), dtype=np.float32)

    heatmap_norm = np.clip(heatmap_norm, 0.0, 1.0)

    fg_soft = cv2.GaussianBlur((filled_fg > 0).astype(np.float32), (7, 7), 0)[:, :, np.newaxis]
    white_bg = np.full_like(arr, 248, dtype=np.uint8)
    bg_neutralized_rgb = np.clip(arr.astype(np.float32) * fg_soft + white_bg.astype(np.float32) * (1.0 - fg_soft), 0, 255).astype(np.uint8)

    telemetry = {
        "has_fruit": True,
        "fruit_type": fruit_type,
        "defect_types": defect_types_str,
        "fruit_area_px": int(total_fruit_px),
        "fruit_coverage_pct": round(float(total_fruit_px) / float(h * w) * 100.0, 1),
        "defect_ratio_pct": round(defect_ratio * 100.0, 2),
        "max_lesion_pct": round(max_blob_ratio * 100.0, 2),
        "lesion_count": len(lesion_boxes),
        "healthy_v_median": round(v_p50, 1),
        "bg_type": "Nền màu / mặt bàn (đã tách Otsu)" if is_colored_bg else "Nền sáng (đã lọc bóng đổ)",
        "filled_fg": filled_fg > 0,
        "inner_fg": inner_fg,
        "clean_defect_mask": clean_defect_mask,
        "contour_img": contour_img,
        "bg_neutralized_rgb": bg_neutralized_rgb,
        "is_colored_bg": is_colored_bg,
    }
    return prob, heatmap_norm, telemetry


class OpticalSpectralQCModel:
    """Bộ phân tích đặc trưng màu HSV/Lab và hình thái học khi chạy không cần GPU"""
    def __init__(self):
        self.name = "OpticalSpectralQC"

    def predict(self, img_tensor, verbose=0):
        arr = img_tensor[0]
        if arr.max() <= 1.0:
            arr = (arr * 255).astype(np.uint8)
        else:
            arr = arr.astype(np.uint8)
        prob, _, _ = segment_and_analyze_fruit(arr)
        return np.array([[prob]], dtype=np.float32)


def discover_keras_models():
    """Tìm các file trọng số .keras trong thư mục models/"""
    search_dirs = [
        PROJECT_DIR / "models",
        PROJECT_DIR.parent / "models",
        Path.cwd() / "models",
        PROJECT_DIR,
    ]
    model_names = [
        ("EfficientNetB0", "efficientnetb0_best.keras"),
        ("ResNet50", "resnet50_best.keras"),
        ("VGG16", "vgg16_best.keras"),
        ("Baseline CNN", "baseline_cnn.keras"),
    ]
    found = {}
    for label, fname in model_names:
        for d in search_dirs:
            candidate = d / fname
            if candidate.exists() and candidate.stat().st_size > 100_000:
                found[label] = str(candidate.resolve())
                break
    return found


def build_cached_grad_model(model):
    """
    Khởi tạo hàm biên dịch tĩnh @tf.function tính đồng thời xác suất dự báo và đạo hàm
    Linear Logit Grad-CAM chỉ qua các lớp phân loại cuối (Head-Only GradientTape),
    giúp giảm thời gian suy luận từ ~15 giây xuống dưới 40 ms trên CPU.
    """
    try:
        import tensorflow as tf
        if not hasattr(model, "layers") or len(model.layers) < 2:
            return None, False, None

        # Dò tìm lớp xuất bản đồ đặc trưng không gian 4D cuối cùng (ví dụ: efficientnetb0, resnet50, vgg16 hoặc Conv2D cuối)
        x_probe = tf.zeros((1, 224, 224, 3), dtype=tf.float32)
        conv_idx = None
        for idx, lyr in enumerate(model.layers):
            if idx == 0 and isinstance(lyr, tf.keras.layers.InputLayer):
                continue
            try:
                x_probe = lyr(x_probe, training=False)
            except TypeError:
                x_probe = lyr(x_probe)
            if hasattr(x_probe, "shape") and len(x_probe.shape) == 4:
                conv_idx = idx

        if conv_idx is None:
            return None, False, None

        backbone_layers = [
            lyr for idx, lyr in enumerate(model.layers[: conv_idx + 1])
            if not (idx == 0 and isinstance(lyr, tf.keras.layers.InputLayer))
        ]
        head_layers = model.layers[conv_idx + 1 : -1]
        last_layer = model.layers[-1]
        w_var, b_var = last_layer.weights[0], last_layer.weights[1]

        @tf.function(reduce_retracing=True)
        def fast_cnn_and_gradcam(img_tensor):
            x = img_tensor
            for lyr in backbone_layers:
                try:
                    x = lyr(x, training=False)
                except TypeError:
                    x = lyr(x)
            conv_out = x
            with tf.GradientTape() as tape:
                tape.watch(conv_out)
                h_vec = conv_out
                for lyr in head_layers:
                    try:
                        h_vec = lyr(h_vec, training=False)
                    except TypeError:
                        h_vec = lyr(h_vec)
                logits = tf.matmul(h_vec, w_var) + b_var
                prob = tf.math.sigmoid(logits)
                loss = logits[:, 0]
            grads = tape.gradient(loss, conv_out)
            pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
            cam = tf.einsum("bhwc,c->bhw", conv_out, pooled_grads)
            cam = tf.nn.relu(cam[0])
            max_v = tf.reduce_max(cam)
            cam_norm = tf.cond(max_v > 1e-6, lambda: cam / max_v, lambda: tf.zeros_like(cam))
            return prob[0, 0], cam_norm

        # Chạy nháp 1 lần để biên dịch đồ thị tĩnh ngay khi khởi tạo
        dummy_in = tf.zeros((1, 224, 224, 3), dtype=tf.float32)
        _ = fast_cnn_and_gradcam(dummy_in)
        return fast_cnn_and_gradcam, True, last_layer
    except Exception:
        return None, False, None


@st.cache_resource(show_spinner="Đang nạp mô hình vào bộ nhớ...")
def load_fruit_qc_model(selected_model_key="AUTO"):
    """Nạp mô hình .keras cùng đồ thị Grad-CAM đã biên dịch sẵn, hoặc dùng bộ xử lý ảnh HSV/Lab"""
    found_models = discover_keras_models()

    if selected_model_key == "OPTICAL_V2" or not found_models:
        return OpticalSpectralQCModel(), "Xử lý ảnh HSV + CIE Lab (Tách nền Otsu)", False, None, False, None

    target_path = None
    if selected_model_key in found_models:
        target_path = found_models[selected_model_key]
    else:
        for label in ["EfficientNetB0", "ResNet50", "VGG16", "Baseline CNN"]:
            if label in found_models:
                target_path = found_models[label]
                break

    if target_path is not None:
        try:
            import tensorflow as tf
            model = tf.keras.models.load_model(target_path, compile=False)
            grad_runner, use_logit, last_layer = build_cached_grad_model(model)
            if grad_runner is None:
                dummy_in = tf.zeros((1, 224, 224, 3), dtype=tf.float32)
                _ = model(dummy_in, training=False)
            mode_desc = f"Mạng học sâu ({os.path.basename(target_path)}) kết hợp lọc vùng quả ROI"
            return model, mode_desc, True, grad_runner, use_logit, last_layer
        except Exception:
            return OpticalSpectralQCModel(), f"Xử lý ảnh HSV + CIE Lab (Dự phòng từ {os.path.basename(target_path)})", False, None, False, None

    return OpticalSpectralQCModel(), "Xử lý ảnh HSV + CIE Lab (Tách nền Otsu)", False, None, False, None


# ==============================================================================
# 3. TÍNH BẢN ĐỒ NHIỆT GRAD-CAM VÀ LƯU BỘ NHỚ ĐỆM THEO MÃ BĂM SHA-256
# ==============================================================================
def generate_fruit_gradcam(img_array, model, pred_prob=None, optical_heatmap=None, telemetry=None, grad_bundle=None, precomputed_cam_np=None):
    """Tính bản đồ nhiệt Linear Logit Grad-CAM và chồng lớp Adaptive Alpha Mask"""
    arr = cv2.resize(np.uint8(img_array), (224, 224))

    if optical_heatmap is None or telemetry is None:
        opt_prob, optical_heatmap, telemetry = segment_and_analyze_fruit(arr)
        if pred_prob is None:
            pred_prob = opt_prob

    fg_mask_float = cv2.GaussianBlur(telemetry["filled_fg"].astype(np.float32), (9, 9), 0)

    cam_np = precomputed_cam_np
    if cam_np is None and grad_bundle is not None and grad_bundle[0] is not None:
        grad_runner = grad_bundle[0]
        try:
            import tensorflow as tf
            input_arr = telemetry["bg_neutralized_rgb"] if telemetry.get("is_colored_bg", False) else arr
            img_tensor = tf.expand_dims(tf.cast(input_arr, tf.float32), axis=0)
            _, cam_tensor = grad_runner(img_tensor)
            cam_np = cam_tensor.numpy()
        except Exception:
            cam_np = None

    if cam_np is not None:
        try:
            cam_resized = cv2.resize(cam_np, (224, 224)) * fg_mask_float
            if cam_resized.max() > 1e-5:
                cam_resized = cam_resized / cam_resized.max()

            combined_cam = 0.55 * cam_resized + 0.45 * optical_heatmap
            if pred_prob < 0.35:
                combined_cam = combined_cam * pred_prob * 0.25
            else:
                combined_cam = combined_cam * min(1.0, max(pred_prob, 0.65))

            heatmap_resized = np.clip(combined_cam, 0.0, 1.0)
            heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), cv2.COLORMAP_JET)
            heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)

            mask = np.clip((heatmap_resized - 0.16) / 0.84, 0.0, 1.0)[:, :, np.newaxis]
            overlay = (heatmap_colored * 0.48 + arr * 0.52) * mask + arr * (1.0 - mask)
            overlay = np.clip(overlay, 0, 255).astype(np.uint8)
            return heatmap_resized, overlay
        except Exception:
            pass

    heatmap_resized = np.clip(optical_heatmap, 0.0, 1.0)
    heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), cv2.COLORMAP_JET)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)

    mask = np.clip((heatmap_resized - 0.16) / 0.84, 0.0, 1.0)[:, :, np.newaxis]
    overlay = (heatmap_colored * 0.48 + arr * 0.52) * mask + arr * (1.0 - mask)
    overlay = np.clip(overlay, 0, 255).astype(np.uint8)
    return heatmap_resized, overlay


def encode_jpeg_bytes(rgb_arr, size=(160, 160)):
    """Nén sẵn ảnh thu nhỏ sang JPEG bytes trong RAM để hiển thị lưới nhiều ảnh nhanh hơn"""
    small_bgr = cv2.cvtColor(cv2.resize(rgb_arr, size), cv2.COLOR_RGB2BGR)
    ok, buf = cv2.imencode(".jpg", small_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
    return bytes(buf) if ok else rgb_arr


def analyze_single_image_cached(pil_img, caption, selected_model_key):
    """Lưu kết quả phân tích của từng ảnh vào bộ nhớ đệm theo mã SHA-256"""
    if "analysis_cache" not in st.session_state:
        st.session_state["analysis_cache"] = {}

    img_resized = pil_img.resize((224, 224))
    img_array = np.array(img_resized, dtype=np.uint8)
    img_hash = hashlib.sha256(img_array.tobytes()).hexdigest()[:16]
    cache_key = f"v42_{img_hash}_{selected_model_key}"

    if cache_key in st.session_state["analysis_cache"]:
        cached = st.session_state["analysis_cache"][cache_key].copy()
        cached["caption"] = caption
        cached["pil_img"] = pil_img
        return cached

    model, model_mode, is_trained, grad_runner, use_logit, last_layer = load_fruit_qc_model(selected_model_key)
    t_start = time.perf_counter()
    opt_prob, optical_heatmap, telemetry = segment_and_analyze_fruit(img_array)
    precomputed_cam_np = None

    if is_trained and model is not None:
        try:
            import tensorflow as tf
            cnn_input_rgb = telemetry["bg_neutralized_rgb"] if telemetry.get("is_colored_bg", False) else img_array
            img_tensor = tf.expand_dims(tf.cast(cnn_input_rgb, tf.float32), axis=0)
            if grad_runner is not None:
                prob_t, cam_t = grad_runner(img_tensor)
                cnn_prob = float(prob_t.numpy())
                precomputed_cam_np = cam_t.numpy()
            else:
                raw_out = model(img_tensor, training=False)
                cnn_prob = float(raw_out.numpy()[0][0])

            if telemetry["defect_ratio_pct"] < 0.8 and opt_prob < 0.15 and telemetry.get("is_colored_bg", False):
                pred_prob = 0.30 * cnn_prob + 0.70 * opt_prob
            elif telemetry["defect_ratio_pct"] >= 8.0 and opt_prob >= 0.80:
                pred_prob = max(0.65 * cnn_prob + 0.35 * opt_prob, 0.90 * opt_prob)
            else:
                pred_prob = 0.65 * cnn_prob + 0.35 * opt_prob
        except Exception:
            pred_prob = opt_prob
            cnn_prob = opt_prob
    else:
        pred_prob = opt_prob
        cnn_prob = opt_prob

    grad_bundle = (grad_runner, use_logit, last_layer)
    pred_prob = float(np.clip(pred_prob, 0.01, 0.99))
    heatmap, overlay = generate_fruit_gradcam(
        img_array,
        model,
        pred_prob=pred_prob,
        optical_heatmap=optical_heatmap,
        telemetry=telemetry,
        grad_bundle=grad_bundle,
        precomputed_cam_np=precomputed_cam_np,
    )
    t_latency = (time.perf_counter() - t_start) * 1000.0

    result = {
        "id": img_hash,
        "caption": caption,
        "pil_img": pil_img,
        "img_array": img_array,
        "thumb_bytes": encode_jpeg_bytes(img_array, (160, 160)),
        "pred_prob": pred_prob,
        "latency_ms": t_latency,
        "model_mode": model_mode,
        "heatmap": heatmap,
        "overlay": overlay,
        "contour_img": telemetry["contour_img"],
        "telemetry": {
            "fruit_type": telemetry["fruit_type"],
            "defect_types": telemetry["defect_types"],
            "fruit_area_px": telemetry["fruit_area_px"],
            "fruit_coverage_pct": telemetry["fruit_coverage_pct"],
            "defect_ratio_pct": telemetry["defect_ratio_pct"],
            "max_lesion_pct": telemetry["max_lesion_pct"],
            "lesion_count": telemetry["lesion_count"],
            "healthy_v_median": telemetry["healthy_v_median"],
            "bg_type": telemetry["bg_type"],
        },
    }
    st.session_state["analysis_cache"][cache_key] = result
    return result


# ==============================================================================
# 4. ĐỌC ẢNH TỪ NHIỀU ĐỊNH DẠNG TỆP (.ZIP, .DOCX, .PDF, .CSV, .XLSX, THƯ MỤC)
# ==============================================================================
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")

def extract_images_from_any_upload(uploaded_files):
    """Đọc danh sách ảnh từ các tệp tải lên (tệp ảnh lẻ, file nén .zip, file .docx, .pdf, .csv, .xlsx)"""
    extracted = []
    if not uploaded_files:
        return extracted
    if not isinstance(uploaded_files, list):
        uploaded_files = [uploaded_files]

    for uf in uploaded_files:
        fname = uf.name
        lower_name = fname.lower()
        raw_bytes = uf.getvalue()

        if lower_name.endswith(IMAGE_EXTENSIONS):
            try:
                img = Image.open(io.BytesIO(raw_bytes)).convert("RGB")
                extracted.append((fname, img))
            except Exception:
                pass

        elif lower_name.endswith(".zip") or lower_name.endswith(".docx"):
            try:
                with zipfile.ZipFile(io.BytesIO(raw_bytes)) as zf:
                    for member in sorted(zf.namelist()):
                        m_low = member.lower()
                        if "__macosx" in m_low or member.endswith("/"):
                            continue
                        if m_low.endswith(IMAGE_EXTENSIONS):
                            try:
                                img_bytes = zf.read(member)
                                img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
                                if img.width >= 60 and img.height >= 60:
                                    short_member = os.path.basename(member)
                                    extracted.append((f"{fname} / {short_member}", img))
                            except Exception:
                                pass
            except Exception:
                pass

        elif lower_name.endswith(".pdf"):
            try:
                from pypdf import PdfReader
                reader = PdfReader(io.BytesIO(raw_bytes))
                for p_idx, page in enumerate(reader.pages):
                    for img_idx, img_file_obj in enumerate(page.images):
                        try:
                            img = Image.open(io.BytesIO(img_file_obj.data)).convert("RGB")
                            if img.width >= 60 and img.height >= 60:
                                extracted.append((f"{fname} / Trang {p_idx+1} - Ảnh {img_idx+1}", img))
                        except Exception:
                            pass
            except Exception:
                pass

        elif lower_name.endswith((".csv", ".xlsx", ".txt")):
            try:
                if lower_name.endswith(".csv"):
                    df_paths = pd.read_csv(io.BytesIO(raw_bytes))
                elif lower_name.endswith(".xlsx"):
                    df_paths = pd.read_excel(io.BytesIO(raw_bytes))
                else:
                    lines = [ln.strip() for ln in raw_bytes.decode("utf-8", errors="ignore").splitlines() if ln.strip()]
                    df_paths = pd.DataFrame({"filepath": lines})

                path_col = None
                for col in df_paths.columns:
                    if any(k in col.lower() for k in ["path", "file", "image", "img", "url"]):
                        path_col = col
                        break
                if path_col is None and len(df_paths.columns) > 0:
                    path_col = df_paths.columns[0]

                if path_col is not None:
                    for raw_p in df_paths[path_col].dropna().astype(str).tolist()[:100]:
                        clean_p = raw_p.strip().strip('"').strip("'")
                        candidates = [
                            Path(clean_p),
                            PROJECT_DIR / clean_p,
                            PROJECT_DIR.parent / clean_p,
                            Path.cwd() / clean_p,
                        ]
                        for c_path in candidates:
                            if c_path.exists() and c_path.is_file() and c_path.suffix.lower() in IMAGE_EXTENSIONS:
                                try:
                                    img = Image.open(c_path).convert("RGB")
                                    extracted.append((f"{fname} / {c_path.name}", img))
                                    break
                                except Exception:
                                    pass
            except Exception:
                pass

    return extracted


def scan_local_folder_images(folder_str, max_images=60):
    """Đọc danh sách ảnh từ thư mục trên máy tính"""
    results = []
    if not folder_str:
        return results
    candidates = [
        Path(folder_str.strip()),
        PROJECT_DIR / folder_str.strip(),
        PROJECT_DIR.parent / folder_str.strip(),
        Path.cwd() / folder_str.strip(),
    ]
    target_dir = None
    for c in candidates:
        if c.exists() and c.is_dir():
            target_dir = c
            break
    if target_dir is None:
        return results

    for root, _, files in os.walk(target_dir):
        for f in sorted(files):
            if f.lower().endswith(IMAGE_EXTENSIONS):
                full_p = Path(root) / f
                try:
                    img = Image.open(full_p).convert("RGB")
                    rel_lbl = os.path.relpath(full_p, target_dir)
                    results.append((rel_lbl, img))
                    if len(results) >= max_images:
                        return results
                except Exception:
                    pass
    return results


# ==============================================================================
# 5. THANH BÊN (SIDEBAR): CẤU HÌNH MÔ HÌNH, NGƯỠNG CẮT & CHI PHÍ (VNĐ)
# ==============================================================================
with st.sidebar:
    st.header("Cấu hình kiểm tra")

    avail_models = discover_keras_models()
    model_options = ["Tự động (CNN + Xử lý ảnh)"] + list(avail_models.keys()) + ["Xử lý ảnh (HSV + CIE Lab)"]
    selected_engine_label = st.selectbox(
        "Mô hình phân tích:",
        model_options,
        index=0,
        help="Chế độ Tự động sẽ ưu tiên dùng mô hình .keras (nếu có trong thư mục models/) kết hợp tách nền Otsu."
    )
    if selected_engine_label == "Xử lý ảnh (HSV + CIE Lab)":
        selected_model_key = "OPTICAL_V2"
    elif selected_engine_label.startswith("Tự động"):
        selected_model_key = "AUTO"
    else:
        selected_model_key = selected_engine_label

    threshold = st.slider(
        "Ngưỡng phân loại lỗi (Threshold):",
        min_value=0.10,
        max_value=0.90,
        value=0.35,
        step=0.05,
        help="Quả có xác suất hư hỏng >= ngưỡng này sẽ được xếp vào nhóm Hư hỏng (Rotten). Ngưỡng khuyến nghị trong báo cáo là 0.35 - 0.40."
    )

    if threshold <= 0.40:
        st.info(f"Ngưỡng {threshold:.2f}: Ưu tiên bắt hết quả lỗi (tối đa Recall) để tránh lây nấm mốc sang thùng hàng.")
    else:
        st.warning(f"Ngưỡng {threshold:.2f}: Giảm tỷ lệ báo nhầm quả tươi nhưng tăng nguy cơ bỏ sót quả chớm hỏng.")

    st.markdown("---")
    st.subheader("Ước tính chi phí tại xưởng (VNĐ)")
    st.caption("Đồng bộ theo Bảng 1.3 và Bảng 5.4 trong báo cáo:")

    lot_cartons = st.number_input("Số thùng kiểm tra (60 quả/thùng):", min_value=10, max_value=10000, value=100, step=10)
    cost_fn_vnd = st.number_input("Thiệt hại 1 quả thối bị sót (VNĐ):", min_value=50000, max_value=2000000, value=500000, step=50000)
    cost_fp_vnd = st.number_input("Chi phí kiểm lại 1 quả báo nhầm (VNĐ):", min_value=1000, max_value=50000, value=5000, step=1000)

    est_fn_rate = 0.0 if threshold <= 0.50 else (0.0004 if threshold <= 0.60 else 0.0012)
    est_fp_rate = 0.0004 if threshold >= 0.35 else 0.0015
    total_fruits = lot_cartons * 60
    loss_ai_vnd = (total_fruits * 0.566 * est_fn_rate * cost_fn_vnd) + (total_fruits * 0.434 * est_fp_rate * cost_fp_vnd)
    loss_manual_vnd = (total_fruits * 0.566 * 0.015 * cost_fn_vnd) + (total_fruits * 0.434 * 0.03 * cost_fp_vnd)
    saving_vnd = max(0.0, loss_manual_vnd - loss_ai_vnd)

    st.metric("Chi phí rủi ro khi dùng AI", f"{loss_ai_vnd:,.0f} VNĐ")
    st.metric("Tiết kiệm so với phân loại tay", f"{saving_vnd:,.0f} VNĐ")


# ==============================================================================
# 6. NẠP DỮ LIỆU ĐẦU VÀO (4 TAB: TẢI TỆP / QUÉT THƯ MỤC / CAMERA / MẪU THỬ)
# ==============================================================================
if "batch_items" not in st.session_state:
    st.session_state["batch_items"] = []
if "selected_idx" not in st.session_state:
    st.session_state["selected_idx"] = 0
if "last_upload_sig" not in st.session_state:
    st.session_state["last_upload_sig"] = None

tab_upload, tab_folder, tab_camera, tab_sample = st.tabs([
    "1. Tải ảnh / Tệp nén (.zip, .docx, .pdf, .csv)",
    "2. Quét thư mục trên máy",
    "3. Camera / Webcam trực tiếp",
    "4. Ảnh mẫu (Táo, Cam, Chuối)"
])

with tab_upload:
    uploaded_files = st.file_uploader(
        "Chọn một hoặc nhiều ảnh (.jpg, .png, .webp) hoặc tệp chứa ảnh (.zip, .docx, .pdf, .csv, .xlsx):",
        type=["jpg", "jpeg", "png", "webp", "bmp", "zip", "docx", "pdf", "csv", "xlsx", "txt"],
        accept_multiple_files=True
    )
    if uploaded_files:
        cur_sig = tuple((f.name, f.size) for f in uploaded_files)
        if cur_sig != st.session_state["last_upload_sig"]:
            extracted_list = extract_images_from_any_upload(uploaded_files)
            if extracted_list:
                st.session_state["batch_items"] = extracted_list
                st.session_state["selected_idx"] = 0
                st.session_state["last_upload_sig"] = cur_sig
                st.toast(f"Đã nạp {len(extracted_list)} ảnh.")
            else:
                st.warning("Không tìm thấy ảnh hợp lệ trong tệp vừa tải lên.")

with tab_folder:
    col_f1, col_f2, col_f3 = st.columns([2.2, 1.0, 1.0])
    with col_f1:
        folder_input = st.text_input(
            "Đường dẫn thư mục ảnh trên máy tính:",
            value="data/test",
            help="Nhập đường dẫn tương đối (ví dụ: data/test) hoặc đường dẫn tuyệt đối trên máy."
        )
    with col_f2:
        max_scan = st.number_input("Số lượng ảnh tối đa:", min_value=6, max_value=200, value=30, step=6)
    with col_f3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Đọc thư mục", use_container_width=True, type="primary"):
            folder_imgs = scan_local_folder_images(folder_input, max_images=int(max_scan))
            if folder_imgs:
                st.session_state["batch_items"] = folder_imgs
                st.session_state["selected_idx"] = 0
                st.success(f"Đã nạp {len(folder_imgs)} ảnh từ thư mục `{folder_input}`.")
            else:
                st.error(f"Không tìm thấy ảnh trong thư mục `{folder_input}`.")

# ==============================================================================
# KẾT NỐI CAMERA (DROIDCAM / WEBCAM)
# ==============================================================================
CAMERA_HISTORY_FILE = str(PROJECT_DIR / "camera_history.json")

def load_camera_history():
    import json
    default_history = ["10.209.6.170:4747", "192.168.2.173:4747", "192.168.1.15:4747"]
    if os.path.exists(CAMERA_HISTORY_FILE):
        try:
            with open(CAMERA_HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
        except Exception:
            pass
    return default_history

def save_camera_history(new_ip):
    import json
    if not new_ip or not isinstance(new_ip, str):
        return
    clean_ip = new_ip.strip().replace("http://", "").replace("https://", "").replace("/video", "").strip()
    if not clean_ip or clean_ip in ["0", "webcam"]:
        return
    history = load_camera_history()
    if clean_ip in history:
        history.remove(clean_ip)
    history.insert(0, clean_ip)
    history = history[:10]
    try:
        with open(CAMERA_HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def normalize_camera_source(raw_input):
    if raw_input is None:
        return 0
    raw_str = str(raw_input).strip()
    if raw_str in ["0", "webcam", "laptop"]:
        return 0
    if not (raw_str.startswith("http://") or raw_str.startswith("https://") or raw_str.startswith("rtsp://")):
        raw_str = "http://" + raw_str
    if "4747" in raw_str and not raw_str.endswith("/video"):
        raw_str = raw_str.rstrip("/") + "/video"
    return raw_str

with tab_camera:
    history_list = load_camera_history()
    col_cam1, col_cam2 = st.columns([1.1, 1.4])
    with col_cam1:
        selected_hist = st.selectbox(
            "Chọn nguồn camera:",
            ["0 (Webcam máy tính)"] + [f"DroidCam: {ip}" for ip in history_list] + ["Nhập địa chỉ IP khác..."]
        )

    with col_cam2:
        if selected_hist.startswith("0"):
            prefill_val = "0"
        elif selected_hist.startswith("DroidCam: "):
            prefill_val = selected_hist.replace("DroidCam: ", "").strip()
        else:
            prefill_val = history_list[0] if history_list else "192.168.1.15:4747"

        raw_ip_input = st.text_input(
            "Địa chỉ IP:Port (hoặc gõ 0 để dùng Webcam laptop):",
            value=prefill_val
        )

    stream_url = normalize_camera_source(raw_ip_input)

    col_btn_snap, col_btn_live = st.columns([1, 1])
    with col_btn_snap:
        snap_quick = st.button("Chụp 1 khung hình từ Camera", use_container_width=True, type="primary")
    with col_btn_live:
        run_live = st.toggle("Bật quét video liên tục (OSD HUD)", value=False)

    if snap_quick:
        with st.spinner(f"Đang đọc khung hình từ {stream_url} ..."):
            cap = cv2.VideoCapture(stream_url)
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            ret, frame = False, None
            for _ in range(5):
                r, f = cap.read()
                if r and f is not None:
                    ret, frame = r, f
            cap.release()

        if ret and frame is not None:
            save_camera_history(raw_ip_input)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam_pil = Image.fromarray(frame_rgb)
            st.session_state["batch_items"] = [(f"Camera ({stream_url})", cam_pil)] + st.session_state["batch_items"][:29]
            st.session_state["selected_idx"] = 0
            st.success("Đã chụp ảnh từ camera.")
        else:
            st.error(f"Không kết nối được nguồn '{stream_url}'. Hãy kiểm tra lại Webcam hoặc ứng dụng DroidCam.")

    if run_live:
        from edge_stream_inspector import ThreadedCamera, RealTimeEdgeQCModel, draw_industrial_hud

        st.info("Đang chạy luồng quét video. Đặt quả vào khung vuông ở giữa màn hình để kiểm tra.")
        stream_placeholder = st.empty()
        telemetry_placeholder = st.empty()

        cam = ThreadedCamera(stream_url).start()
        edge_model = RealTimeEdgeQCModel()

        connect_wait = 0
        while not cam.connected and connect_wait < 30:
            time.sleep(0.1)
            connect_wait += 1

        if not cam.connected:
            st.error(f"Không kết nối được camera '{stream_url}'.")
            cam.stop()
        else:
            save_camera_history(raw_ip_input)
            prev_t = time.time()
            try:
                while run_live:
                    has_frame, frame, _ = cam.read()
                    if not has_frame or frame is None:
                        time.sleep(0.01)
                        continue

                    cur_t = time.time()
                    fps_live = 1.0 / max(cur_t - prev_t, 1e-4)
                    prev_t = cur_t

                    defect_prob, bbox, lat_ms, has_fruit = edge_model.infer(frame, return_presence=True)
                    is_defective = has_fruit and (defect_prob >= threshold)

                    if has_fruit:
                        x1, y1, x2, y2 = bbox
                        roi_crop_rgb = cv2.cvtColor(frame[y1:y2, x1:x2], cv2.COLOR_BGR2RGB)
                        st.session_state["last_live_roi"] = Image.fromarray(roi_crop_rgb)

                    frame_hud = draw_industrial_hud(
                        frame.copy(), defect_prob, bbox, lat_ms, fps_live, edge_model.mode_label, has_fruit=has_fruit
                    )
                    frame_rgb = cv2.cvtColor(frame_hud, cv2.COLOR_BGR2RGB)
                    stream_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

                    if not has_fruit:
                        status_text = "Đang chờ đưa quả vào khung ROI"
                    elif is_defective:
                        status_text = "Phát hiện quả hỏng (Loại bỏ)"
                    else:
                        status_text = "Quả tươi đạt chuẩn (Grade A)"

                    telemetry_placeholder.markdown(
                        f"**Trạng thái:** {status_text} | "
                        f"**Tốc độ:** `{fps_live:.1f} FPS` | "
                        f"**Thời gian xử lý:** `{lat_ms:.1f} ms` | "
                        f"**Xác suất lỗi:** `{defect_prob*100:.1f}%`"
                    )
                    time.sleep(0.015)
            finally:
                cam.stop()
                if "last_live_roi" in st.session_state:
                    st.session_state["batch_items"] = [("Khung hình cắt từ luồng Camera", st.session_state["last_live_roi"])]
                    st.session_state["selected_idx"] = 0

    with st.expander("Chụp ảnh qua Webcam trình duyệt"):
        camera_file = st.camera_input("Chụp ảnh trực tiếp trên trình duyệt")
        if camera_file is not None:
            cam_sig = (camera_file.name, camera_file.size)
            if st.session_state.get("last_browser_cam_sig") != cam_sig:
                cam_img = Image.open(camera_file).convert("RGB")
                st.session_state["batch_items"] = [("Ảnh Webcam trình duyệt", cam_img)] + st.session_state["batch_items"][:29]
                st.session_state["selected_idx"] = 0
                st.session_state["last_browser_cam_sig"] = cam_sig


def load_sample_fruit_image(rel_path, fallback_type):
    candidates = [
        PROJECT_DIR / rel_path,
        PROJECT_DIR.parent / rel_path,
        Path.cwd() / rel_path,
    ]
    for c in candidates:
        if c.exists():
            return Image.open(c).convert("RGB")
    sample_arr = np.full((224, 224, 3), 245, dtype=np.uint8)
    if "rotten" in fallback_type:
        cv2.circle(sample_arr, (112, 112), 80, (190, 80, 45), -1)
        cv2.circle(sample_arr, (105, 105), 34, (45, 35, 25), -1)
    else:
        cv2.circle(sample_arr, (112, 112), 80, (240, 140, 25), -1)
    return Image.fromarray(sample_arr)


with tab_sample:
    if st.button("Nạp cả bộ 6 ảnh mẫu (3 quả tươi + 3 quả hỏng)", use_container_width=True, type="primary"):
        st.session_state["batch_items"] = [
            ("Mẫu 1: Cam tươi (có lá & bóng đổ)", load_sample_fruit_image("data/test/fresh/fresh_orange_001.jpg", "fresh_orange")),
            ("Mẫu 2: Chuối tươi (trên mặt bàn gỗ)", load_sample_fruit_image("data/test/fresh/fresh_banana_001.jpg", "fresh_banana")),
            ("Mẫu 3: Táo đỏ tươi (có lá xanh)", load_sample_fruit_image("data/test/fresh/fresh_apple_001.jpg", "fresh_apple")),
            ("Mẫu 4: Cam mốc xanh Penicillium", load_sample_fruit_image("data/test/rotten/rotten_orange_001.jpg", "rotten_orange")),
            ("Mẫu 5: Táo thối nâu", load_sample_fruit_image("data/test/rotten/rotten_apple_001.jpg", "rotten_apple")),
            ("Mẫu 6: Chuối thâm đen", load_sample_fruit_image("data/test/rotten/rotten_banana_001.jpg", "rotten_banana")),
        ]
        st.session_state["selected_idx"] = 0

    r1c1, r1c2, r1c3 = st.columns(3)
    r2c1, r2c2, r2c3 = st.columns(3)

    with r1c1:
        if st.button("Táo tươi (Fresh Apple)", use_container_width=True):
            st.session_state["batch_items"] = [("Mẫu: Táo đỏ tươi", load_sample_fruit_image("data/test/fresh/fresh_apple_001.jpg", "fresh_apple"))]
            st.session_state["selected_idx"] = 0
    with r1c2:
        if st.button("Cam tươi (Fresh Orange)", use_container_width=True):
            st.session_state["batch_items"] = [("Mẫu: Cam tươi", load_sample_fruit_image("data/test/fresh/fresh_orange_001.jpg", "fresh_orange"))]
            st.session_state["selected_idx"] = 0
    with r1c3:
        if st.button("Chuối tươi (Fresh Banana)", use_container_width=True):
            st.session_state["batch_items"] = [("Mẫu: Chuối tươi trên bàn gỗ", load_sample_fruit_image("data/test/fresh/fresh_banana_001.jpg", "fresh_banana"))]
            st.session_state["selected_idx"] = 0

    with r2c1:
        if st.button("Táo thối nâu (Rotten Apple)", use_container_width=True):
            st.session_state["batch_items"] = [("Mẫu: Táo thối nâu", load_sample_fruit_image("data/test/rotten/rotten_apple_001.jpg", "rotten_apple"))]
            st.session_state["selected_idx"] = 0
    with r2c2:
        if st.button("Cam nhiễm mốc (Rotten Orange)", use_container_width=True):
            st.session_state["batch_items"] = [("Mẫu: Cam mốc Penicillium", load_sample_fruit_image("data/test/rotten/rotten_orange_001.jpg", "rotten_orange"))]
            st.session_state["selected_idx"] = 0
    with r2c3:
        if st.button("Chuối thâm đen (Rotten Banana)", use_container_width=True):
            st.session_state["batch_items"] = [("Mẫu: Chuối thâm đen", load_sample_fruit_image("data/test/rotten/rotten_banana_001.jpg", "rotten_banana"))]
            st.session_state["selected_idx"] = 0


# ==============================================================================
# 7. HIỂN THỊ KẾT QUẢ KIỂM TRA LÔ HÀNG & CHI TIẾT TỪNG QUẢ
# ==============================================================================
@ui_fragment
def render_batch_and_inspector(batch_items, selected_model_key, threshold, cost_fn_vnd, cost_fp_vnd):
    total_count = len(batch_items)
    analyzed_list = [
        analyze_single_image_cached(pil_img, cap, selected_model_key)
        for cap, pil_img in batch_items
    ]

    if total_count > 1:
        st.markdown("---")
        rotten_count = sum(1 for item in analyzed_list if item["pred_prob"] >= threshold)
        fresh_count = total_count - rotten_count
        avg_lat = float(np.mean([item["latency_ms"] for item in analyzed_list]))

        st.subheader(f"Tổng hợp kết quả lô ảnh ({total_count} mẫu)")
        bk1, bk2, bk3, bk4 = st.columns(4)
        bk1.metric("Tổng số ảnh", f"{total_count} mẫu")
        bk2.metric("Quả tươi (Đạt)", f"{fresh_count} mẫu ({fresh_count/total_count*100:.1f}%)")
        bk3.metric("Quả hỏng (Loại)", f"{rotten_count} mẫu ({rotten_count/total_count*100:.1f}%)")
        bk4.metric("Thời gian xử lý TB", f"{avg_lat:.1f} ms/ảnh")

        batch_df = pd.DataFrame([
            {
                "STT": idx + 1,
                "Tên ảnh": item["caption"],
                "Loại quả nhận diện": item["telemetry"]["fruit_type"],
                "Kết quả": "Hỏng (Rotten)" if item["pred_prob"] >= threshold else "Tươi (Fresh)",
                "Xác suất lỗi (%)": round(item["pred_prob"] * 100.0, 1),
                "Dấu hiệu bề mặt": item["telemetry"]["defect_types"],
                "Tỷ lệ vùng hỏng (%)": item["telemetry"]["defect_ratio_pct"],
                "Số cụm vết lỗi": item["telemetry"]["lesion_count"],
                "Độ sáng vỏ (V_med)": item["telemetry"]["healthy_v_median"],
                "Thời gian (ms)": round(item["latency_ms"], 1),
            }
            for idx, item in enumerate(analyzed_list)
        ])

        with st.expander(f"Bảng dữ liệu chi tiết và xuất file CSV ({total_count} mẫu)", expanded=False):
            st.dataframe(batch_df, use_container_width=True, hide_index=True)
            csv_bytes = batch_df.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                "Tải bảng kết quả (.csv)",
                data=csv_bytes,
                file_name="ket_qua_kiem_tra_nong_san.csv",
                mime="text/csv",
            )

        # Bộ lọc nhanh theo kết quả (Tất cả / Chỉ quả hỏng / Chỉ quả tươi)
        f_col1, f_col2 = st.columns([1.5, 2.5])
        with f_col1:
            filter_mode = st.radio(
                "Lọc danh sách hiển thị:",
                ["Tất cả", "Chỉ quả hỏng", "Chỉ quả tươi"],
                horizontal=True
            )

        filtered_indices = [
            i for i, item in enumerate(analyzed_list)
            if filter_mode == "Tất cả"
            or (filter_mode == "Chỉ quả hỏng" and item["pred_prob"] >= threshold)
            or (filter_mode == "Chỉ quả tươi" and item["pred_prob"] < threshold)
        ]

        if not filtered_indices:
            st.info(f"Không có mẫu nào thuộc nhóm '{filter_mode}'.")
            filtered_indices = list(range(total_count))

        if st.session_state["selected_idx"] not in filtered_indices:
            st.session_state["selected_idx"] = filtered_indices[0]

        cols_per_row = min(6, len(filtered_indices))
        for row_start in range(0, min(len(filtered_indices), 24), cols_per_row):
            grid_cols = st.columns(cols_per_row)
            for c_i in range(cols_per_row):
                pos = row_start + c_i
                if pos >= len(filtered_indices):
                    break
                idx = filtered_indices[pos]
                item = analyzed_list[idx]
                is_rot = item["pred_prob"] >= threshold
                pill_cls = "thumb-defect" if is_rot else "thumb-ok"
                pill_txt = f"Hỏng ({item['pred_prob']*100:.0f}%)" if is_rot else f"Tươi ({item['pred_prob']*100:.0f}%)"
                with grid_cols[c_i]:
                    st.image(item["thumb_bytes"], use_container_width=True)
                    st.markdown(f"<div class='{pill_cls}'>#{idx+1}: {pill_txt}</div>", unsafe_allow_html=True)
                    btn_type = "primary" if st.session_state["selected_idx"] == idx else "secondary"
                    if st.button(f"Xem mẫu #{idx+1}", key=f"sel_btn_{idx}", use_container_width=True, type=btn_type):
                        st.session_state["selected_idx"] = idx

        nav_c1, nav_c2, nav_c3 = st.columns([1.0, 2.5, 1.0])
        cur_pos = filtered_indices.index(st.session_state["selected_idx"])
        with nav_c1:
            if st.button("⬅ Ảnh trước", use_container_width=True, disabled=(cur_pos <= 0)):
                st.session_state["selected_idx"] = filtered_indices[max(0, cur_pos - 1)]
        with nav_c3:
            if st.button("Ảnh tiếp theo ➡", use_container_width=True, disabled=(cur_pos >= len(filtered_indices) - 1)):
                st.session_state["selected_idx"] = filtered_indices[min(len(filtered_indices) - 1, cur_pos + 1)]
        with nav_c2:
            option_labels = {
                i: f"Mẫu #{i+1}: {analyzed_list[i]['caption']} ({analyzed_list[i]['telemetry']['fruit_type']}) — {'Hỏng' if analyzed_list[i]['pred_prob']>=threshold else 'Tươi'} ({analyzed_list[i]['pred_prob']*100:.1f}%)"
                for i in filtered_indices
            }
            chosen_idx = st.selectbox(
                "Chọn mẫu:",
                filtered_indices,
                index=cur_pos,
                format_func=lambda i: option_labels[i],
                label_visibility="collapsed"
            )
            st.session_state["selected_idx"] = chosen_idx

    active_idx = min(max(0, st.session_state["selected_idx"]), total_count - 1)
    cur = analyzed_list[active_idx]
    pred_prob = cur["pred_prob"]
    t_latency = cur["latency_ms"]
    model_mode = cur["model_mode"]
    telemetry = cur["telemetry"]
    is_rotten = pred_prob >= threshold

    st.markdown("---")
    header_suffix = f" — Mẫu #{active_idx+1}/{total_count}: {cur['caption']}" if total_count > 1 else ""
    st.subheader(f"Chi tiết phân tích{header_suffix}")
    st.caption(f"Mô hình: **{model_mode}** | Nhận diện: **{telemetry['fruit_type']}** | Xử lý nền: **{telemetry['bg_type']}**")

    c_status, c_prob, c_type, c_lat = st.columns(4)

    with c_status:
        if is_rotten:
            st.markdown("<div class='badge-defect'>KẾT LUẬN: QUẢ HỎNG (ROTTEN)</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='badge-ok'>KẾT LUẬN: QUẢ TƯƠI (FRESH)</div>", unsafe_allow_html=True)

    with c_prob:
        st.markdown(f"<div class='info-box'><div class='info-val'>{pred_prob*100:.1f}%</div><div class='info-lbl'>Xác suất hư hỏng (Ngưỡng: {threshold*100:.0f}%)</div></div>", unsafe_allow_html=True)

    with c_type:
        st.markdown(f"<div class='info-box'><div class='info-val'>{telemetry['defect_ratio_pct']:.2f}%</div><div class='info-lbl'>Tỷ lệ diện tích vùng lỗi (R_defect)</div></div>", unsafe_allow_html=True)

    with c_lat:
        st.markdown(f"<div class='info-box'><div class='info-val'>{t_latency:.1f} ms</div><div class='info-lbl'>Thời gian phân tích</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 4 cột hình ảnh trực quan: Ảnh gốc | Khoanh vùng viền & vết lỗi | Bản đồ nhiệt Grad-CAM | Ảnh chồng lớp
    col_img1, col_img2, col_img3, col_img4 = st.columns(4)

    with col_img1:
        st.markdown("**1. Ảnh đầu vào (224×224)**")
        st.image(cur["img_array"], caption=cur["caption"], use_container_width=True)

    with col_img2:
        st.markdown("**2. Tách nền & Khoanh vùng lỗi**")
        st.image(cur["contour_img"], caption="Viền xanh: Vùng quả | Khung đỏ: Vết hỏng", use_container_width=True)

    with col_img3:
        st.markdown("**3. Bản đồ nhiệt (Grad-CAM)**")
        st.image(cur["heatmap"], caption="Phân bố mức độ nghi vấn trên bề mặt quả", use_container_width=True, clamp=True)

    with col_img4:
        st.markdown("**4. Chồng lớp vị trí lỗi (Overlay)**")
        st.image(cur["overlay"], caption="Vùng màu Đỏ/Vàng hiển thị vị trí thối/mốc", use_container_width=True)

    # Bảng thông số kỹ thuật và nhận xét ngắn gọn, thực chất
    st.markdown("---")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("**Thông số đo đạc trên vùng quả:**")
        st.markdown(
            f"- **Loại quả ước lượng:** {telemetry['fruit_type']}\n"
            f"- **Diện tích vùng quả sau tách nền:** `{telemetry['fruit_area_px']:,} px` ({telemetry['fruit_coverage_pct']}% khung hình)\n"
            f"- **Độ sáng trung vị vỏ lành ($V_{{\\text{{median}}}}$):** `{telemetry['healthy_v_median']:.1f} / 255`\n"
            f"- **Tỷ lệ vùng khuyết tật ($R_{{\\text{{defect}}}}$):** `{telemetry['defect_ratio_pct']:.2f}%` (Cụm lớn nhất: `{telemetry['max_lesion_pct']:.2f}%`, số cụm: `{telemetry['lesion_count']}`)"
        )
    with col_d2:
        st.markdown("**Nhận xét & hướng xử lý trên băng chuyền:**")
        if is_rotten:
            st.error(
                f"**Phân loại: Quả hỏng (Loại bỏ).** Phát hiện dấu hiệu: *{telemetry['defect_types']}* "
                f"chiếm {telemetry['defect_ratio_pct']:.2f}% diện tích vùng quả (vượt ngưỡng {threshold*100:.0f}%). "
                f"Kích hoạt van khí nén đẩy sang máng phế phẩm để tránh lây nấm mốc và khí Ethylene."
            )
        elif 0.25 <= pred_prob < threshold:
            st.warning(
                f"**Phân loại: Nghi vấn nhẹ ({pred_prob*100:.1f}%).** Bề mặt có đốm tối nhỏ ({telemetry['defect_ratio_pct']:.2f}%), "
                f"chuyển sang máng kiểm tra thủ công (Human-in-the-Loop) để công nhân KCS xác nhận lại."
            )
        else:
            st.success(
                f"**Phân loại: Quả tươi đạt chuẩn (Grade A).** Bề mặt vỏ đồng đều, không có ổ nấm mốc hay vết thối "
                f"($R_{{\\text{{defect}}}} = {telemetry['defect_ratio_pct']:.2f}\\%$). Cho phép đi thẳng qua công đoạn đóng thùng."
            )


if st.session_state["batch_items"]:
    render_batch_and_inspector(st.session_state["batch_items"], selected_model_key, threshold, cost_fn_vnd, cost_fp_vnd)
else:
    st.info(
        "Chọn ảnh hoặc tệp nén `.zip` ở **Tab 1**, quét thư mục ở **Tab 2**, bật Camera ở **Tab 3**, "
        "hoặc bấm **'Nạp cả bộ 6 ảnh mẫu'** ở **Tab 4** để bắt đầu kiểm tra."
    )

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #64748b; font-size: 13px;'>"
    "Đồ án cuối khóa SIC 2026 — Project 13: Fruit Visual Quality Control | Học viên: Lê Thành Được (MSSV: 25678381) — Khoa Công nghệ Điện tử, IUH"
    "</div>",
    unsafe_allow_html=True
)

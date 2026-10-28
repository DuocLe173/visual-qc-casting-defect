"""
Đồ án cuối khóa SIC 2026 - Project 13: Fruit Visual Quality Control
Module đọc camera đa luồng (ThreadedCamera) và kiểm tra chất lượng quả thời gian thực (OSD HUD)
Học viên thực hiện: Lê Thành Được (MSSV: 25678381) - Khoa Công nghệ Điện tử, ĐH Công nghiệp TP.HCM (IUH)
"""

import os
import time
import threading
from pathlib import Path
import cv2
import numpy as np

PROJECT_DIR = Path(__file__).resolve().parent

STREAM_CONFIG = {
    "source": "http://10.209.6.170:4747/video",
    "frame_width": 1280,
    "frame_height": 720,
    "inference_size": (224, 224),
    "defect_threshold": 0.35,
    "reconnect_timeout_sec": 1.5,
}


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


def discover_keras_models():
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


class ThreadedCamera:
    """Luồng đọc camera chạy ngầm, luôn giữ khung hình mới nhất để tránh trễ bộ đệm FIFO của OpenCV"""
    def __init__(self, src):
        self.src = src
        self.cap = None
        self.frame = None
        self.is_running = False
        self.lock = threading.Lock()
        self.connected = False
        self.last_frame_time = time.time()
        self.fps_inbound = 0.0
        self.consecutive_failures = 0
        self._init_capture()

    def _init_capture(self):
        if self.cap is not None:
            try:
                self.cap.release()
            except Exception:
                pass
            time.sleep(0.3)

        print(f"[CAMERA] Đang kết nối nguồn video: {self.src} ...")
        self.cap = cv2.VideoCapture(self.src)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        if self.cap.isOpened():
            self.connected = True
            self.last_frame_time = time.time()
            self.consecutive_failures = 0
            print("[CAMERA] Kết nối thành công.")
        else:
            self.connected = False
            print(f"[CAMERA] Không thể mở nguồn video {self.src}.")

    def start(self):
        if self.is_running:
            return self
        self.is_running = True
        self.thread = threading.Thread(target=self._capture_worker, daemon=True)
        self.thread.start()
        return self

    def _capture_worker(self):
        frame_count = 0
        fps_timer = time.time()

        while self.is_running:
            if not self.connected or self.cap is None or not self.cap.isOpened():
                time.sleep(STREAM_CONFIG["reconnect_timeout_sec"])
                self._init_capture()
                continue

            grabbed = self.cap.grab()
            if grabbed:
                ret, decoded_frame = self.cap.retrieve()
                if ret and decoded_frame is not None:
                    with self.lock:
                        self.frame = decoded_frame
                        self.last_frame_time = time.time()
                        self.consecutive_failures = 0

                    frame_count += 1
                    if time.time() - fps_timer >= 1.0:
                        self.fps_inbound = frame_count / (time.time() - fps_timer)
                        frame_count = 0
                        fps_timer = time.time()
                else:
                    self.consecutive_failures += 1
                    if self.consecutive_failures > 25:
                        self.connected = False
            else:
                if time.time() - self.last_frame_time > 3.0:
                    self.connected = False

            time.sleep(0.001)

    def read(self):
        with self.lock:
            if self.frame is not None:
                return True, self.frame.copy(), self.fps_inbound
            return False, None, 0.0

    def stop(self):
        self.is_running = False
        if hasattr(self, "thread") and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        if self.cap is not None:
            self.cap.release()
        print("[CAMERA] Đã đóng kết nối camera.")


class RealTimeEdgeQCModel:
    """Bộ suy luận trên luồng video: tích hợp kiểm tra khung ngắm trống và làm mượt xác suất EMA"""
    def __init__(self):
        self.model = None
        self.mode_label = "HSV + CIE Lab Optical QC"
        self.ema_prob = None
        self.last_defect_mask = None
        self._load_production_model()

    def _load_production_model(self):
        found = discover_keras_models()
        for label in ["EfficientNetB0", "ResNet50", "VGG16", "Baseline CNN"]:
            if label in found:
                path = found[label]
                try:
                    import tensorflow as tf
                    self.model = tf.keras.models.load_model(path, compile=False)
                    self.mode_label = f"CNN + ROI: {os.path.basename(path)}"
                    print(f"[MODEL] Đã nạp trọng số: {path}")
                    return
                except Exception as e:
                    print(f"[MODEL] Lỗi nạp {path}: {e}")

        print("[MODEL] Sử dụng chế độ phân tích quang học HSV + CIE Lab.")

    def infer(self, frame_bgr, return_presence=False):
        t0 = time.perf_counter()
        h, w = frame_bgr.shape[:2]

        roi_size = min(h, w) // 2
        cx, cy = w // 2, h // 2
        x1 = max(0, cx - roi_size)
        y1 = max(0, cy - roi_size)
        x2 = min(w, cx + roi_size)
        y2 = min(h, cy + roi_size)
        roi_bgr = frame_bgr[y1:y2, x1:x2]
        if roi_bgr.size == 0 or roi_bgr.shape[0] < 10 or roi_bgr.shape[1] < 10:
            roi_bgr = frame_bgr.copy()
            x1, y1, x2, y2 = 0, 0, w, h

        roi_rgb = cv2.cvtColor(cv2.resize(roi_bgr, (224, 224)), cv2.COLOR_BGR2RGB)
        opt_prob, _, telemetry = segment_and_analyze_fruit(roi_rgb, check_empty_roi=True)
        has_fruit = telemetry.get("has_fruit", True)
        self.last_defect_mask = telemetry.get("clean_defect_mask", None)

        if not has_fruit:
            self.ema_prob = None
            latency_ms = (time.perf_counter() - t0) * 1000.0
            if return_presence:
                return 0.0, (x1, y1, x2, y2), latency_ms, False
            return 0.0, (x1, y1, x2, y2), latency_ms

        if self.model is not None:
            try:
                import tensorflow as tf
                cnn_in = telemetry["bg_neutralized_rgb"] if telemetry.get("is_colored_bg", False) else roi_rgb
                input_tensor = tf.expand_dims(tf.cast(cnn_in, tf.float32), axis=0)
                raw_out = self.model(input_tensor, training=False)
                cnn_prob = float(raw_out.numpy()[0][0])
                if telemetry["defect_ratio_pct"] < 0.8 and opt_prob < 0.15 and telemetry.get("is_colored_bg", False):
                    raw_prob = 0.30 * cnn_prob + 0.70 * opt_prob
                else:
                    raw_prob = 0.65 * cnn_prob + 0.35 * opt_prob
            except Exception:
                raw_prob = opt_prob
        else:
            raw_prob = opt_prob

        if self.ema_prob is None:
            self.ema_prob = raw_prob
        else:
            self.ema_prob = 0.45 * raw_prob + 0.55 * self.ema_prob

        defect_prob = float(np.clip(self.ema_prob, 0.01, 0.99))
        latency_ms = (time.perf_counter() - t0) * 1000.0
        if return_presence:
            return defect_prob, (x1, y1, x2, y2), latency_ms, True
        return defect_prob, (x1, y1, x2, y2), latency_ms


def draw_industrial_hud(frame, defect_prob, bbox, latency_ms, fps_live, engine_name, has_fruit=True):
    h, w = frame.shape[:2]
    x1, y1, x2, y2 = bbox
    is_defective = has_fruit and (defect_prob >= STREAM_CONFIG["defect_threshold"])

    COLOR_BG_DARK = (15, 23, 42)
    COLOR_FRESH_GREEN = (34, 197, 94)
    COLOR_ROTTEN_RED = (59, 43, 239)
    COLOR_STANDBY_AMBER = (11, 158, 245)
    COLOR_CYAN_TECH = (248, 189, 56)
    COLOR_WHITE = (255, 255, 255)
    COLOR_YELLOW = (0, 215, 255)

    if not has_fruit:
        primary_color = COLOR_STANDBY_AMBER
        badge_text = "STANDBY: PLACE FRUIT IN ROI"
    elif is_defective:
        primary_color = COLOR_ROTTEN_RED
        badge_text = "REJECT: ROTTEN / DEFECTIVE"
    else:
        primary_color = COLOR_FRESH_GREEN
        badge_text = "ACCEPT: FRESH (GRADE A)"

    corner_len = 30
    thick = 3
    cv2.line(frame, (x1, y1), (x1 + corner_len, y1), primary_color, thick)
    cv2.line(frame, (x1, y1), (x1, y1 + corner_len), primary_color, thick)
    cv2.line(frame, (x2, y1), (x2 - corner_len, y1), primary_color, thick)
    cv2.line(frame, (x2, y1), (x2, y1 + corner_len), primary_color, thick)
    cv2.line(frame, (x1, y2), (x1 + corner_len, y2), primary_color, thick)
    cv2.line(frame, (x1, y2), (x1, y2 - corner_len), primary_color, thick)
    cv2.line(frame, (x2, y2), (x2 - corner_len, y2), primary_color, thick)
    cv2.line(frame, (x2, y2), (x2 - corner_len, y2), primary_color, thick)
    cv2.rectangle(frame, (x1, y1), (x2, y2), primary_color, 1, cv2.LINE_AA)

    (tw, th), _ = cv2.getTextSize(badge_text, cv2.FONT_HERSHEY_DUPLEX, 0.65, 1)
    badge_y = max(y1 - 10, 30)
    cv2.rectangle(frame, (x1, badge_y - th - 10), (x1 + tw + 20, badge_y + 4), primary_color, -1)
    cv2.putText(frame, badge_text, (x1 + 10, badge_y - 4), cv2.FONT_HERSHEY_DUPLEX, 0.65, COLOR_WHITE, 1, cv2.LINE_AA)

    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, 55), COLOR_BG_DARK, -1)
    cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)

    sys_title = "PROJECT 13: FRUIT VISUAL QC - CAMERA STREAM"
    cv2.putText(frame, sys_title, (20, 34), cv2.FONT_HERSHEY_DUPLEX, 0.72, COLOR_CYAN_TECH, 2, cv2.LINE_AA)

    telemetry_fps = f"FPS: {fps_live:4.1f}"
    telemetry_lat = f"LATENCY: {latency_ms:4.1f} ms"
    cv2.putText(frame, telemetry_fps, (w - 360, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLOR_WHITE, 1, cv2.LINE_AA)
    cv2.putText(frame, telemetry_lat, (w - 200, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLOR_YELLOW, 1, cv2.LINE_AA)

    panel_y = h - 65
    overlay_bottom = frame.copy()
    cv2.rectangle(overlay_bottom, (0, panel_y), (w, h), COLOR_BG_DARK, -1)
    cv2.addWeighted(overlay_bottom, 0.75, frame, 0.25, 0, frame)

    bar_x, bar_y, bar_w, bar_h = 20, panel_y + 20, 280, 24
    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (80, 80, 80), 1)
    fill_w = int(bar_w * (defect_prob if has_fruit else 0.0))
    cv2.rectangle(frame, (bar_x + 1, bar_y + 1), (bar_x + fill_w, bar_y + bar_h - 1), primary_color, -1)

    prob_label = f"Defect Prob: {defect_prob*100:.1f}% (Thresh: {STREAM_CONFIG['defect_threshold']*100:.0f}%)"
    cv2.putText(frame, prob_label, (bar_x, bar_y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.45, COLOR_WHITE, 1, cv2.LINE_AA)

    if not has_fruit:
        actuator_msg = "STATUS: Waiting for fruit in ROI"
    elif is_defective:
        actuator_msg = "ACTION: Push to scrap chute"
    else:
        actuator_msg = "ACTION: Pass to packaging"

    cv2.putText(frame, actuator_msg, (bar_x + bar_w + 30, panel_y + 36), cv2.FONT_HERSHEY_DUPLEX, 0.58, primary_color, 1, cv2.LINE_AA)
    cv2.putText(frame, f"Mode: {engine_name}", (w - 360, panel_y + 36), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (160, 160, 160), 1, cv2.LINE_AA)
    return frame


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fruit Visual QC Camera Stream")
    parser.add_argument("--source", type=str, default=None, help="Camera source: '0' for webcam, or IP URL")
    args = parser.parse_args()

    source = args.source
    if source is None:
        print("\n" + "=" * 65)
        print("PROJECT 13: FRUIT VISUAL QC - KIỂM TRA QUA CAMERA")
        print("=" * 65)
        print("Chọn nguồn camera:")
        print("  [1] DroidCam mặc định (http://10.209.6.170:4747/video) -> Nhấn ENTER")
        print("  [2] Webcam máy tính                                    -> Gõ '0'")
        print("  [3] Nhập địa chỉ IP:Port khác (ví dụ: 192.168.1.15:4747)")
        print("-" * 65)
        user_input = input("Lựa chọn: ").strip()
        if not user_input or user_input == "1":
            source = "http://10.209.6.170:4747/video"
        elif user_input in ["0", "2"]:
            source = 0
        else:
            raw = user_input.replace("http://", "").replace("https://", "").rstrip("/")
            source = f"http://{raw}/video" if "4747" in raw and not raw.endswith("/video") else f"http://{raw}"

    if isinstance(source, str) and source.isdigit():
        source = int(source)

    STREAM_CONFIG["source"] = source
    cam = ThreadedCamera(STREAM_CONFIG["source"]).start()
    qc_engine = RealTimeEdgeQCModel()

    window_name = "Project 13: Fruit Visual QC - Camera Stream"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, STREAM_CONFIG["frame_width"], STREAM_CONFIG["frame_height"])

    fps_display = 0.0
    frame_timer = time.time()
    rendered_frames = 0

    try:
        while True:
            has_frame, frame, _ = cam.read()
            if not has_frame:
                if cv2.waitKey(30) & 0xFF in [ord("q"), 27]:
                    break
                continue

            defect_prob, bbox, latency_ms, has_fruit = qc_engine.infer(frame, return_presence=True)
            rendered_frames += 1
            if time.time() - frame_timer >= 0.5:
                fps_display = rendered_frames / (time.time() - frame_timer)
                rendered_frames = 0
                frame_timer = time.time()

            hud_frame = draw_industrial_hud(
                frame, defect_prob, bbox, latency_ms, fps_display, qc_engine.mode_label, has_fruit=has_fruit
            )
            cv2.imshow(window_name, hud_frame)
            if cv2.waitKey(1) & 0xFF in [ord("q"), 27]:
                break
    finally:
        cam.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

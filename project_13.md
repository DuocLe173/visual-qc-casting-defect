---
title: "20 Đề Tài Project — Môn Trí Tuệ Nhân Tạo"
subtitle: "Yêu cầu chi tiết · Rubric chấm điểm · Dữ liệu & Công cụ gợi ý"
author: "Giảng viên môn học"
date: today
lang: vi
format:
  html:
    toc: true
    toc-depth: 3
    toc-title: "Danh mục đề tài"
    theme: cosmo
    number-sections: false
    code-fold: true
    highlight-style: github
  pdf:
    documentclass: article
    papersize: a4
    toc: true
    number-sections: true
    colorlinks: true
    fontsize: 11pt
---

---

> **Đối tượng:** Sinh viên khối Kinh tế (chủ yếu) · HTTT Quản lý · Khoa học Dữ liệu  
> **Hình thức:** Làm nhóm 3–4 sinh viên · Có thể làm cá nhân đối với project ⭐⭐  
> **Đánh giá:** Báo cáo viết + Demo notebook + Thuyết trình (10 phút/nhóm)  
> **Ngôn ngữ lập trình:** Python (Jupyter Notebook / Google Colab)

---

### Project 13 · Kiểm soát Chất lượng Sản phẩm bằng Ảnh (Visual QC)

**Chương liên quan:** Ch.8 Neural Network · Ch.9 CNN  
**Loại bài toán:** Image Classification · **Độ khó:** ⭐⭐⭐ (Trung bình)  
**Đối tượng phù hợp:** HTTT, Khoa học Dữ liệu, Sản xuất

#### Bối cảnh & Vấn đề kinh doanh

Kiểm soát chất lượng thủ công tốn kém và thiếu nhất quán. Nhà máy sản xuất điện tử muốn **tự động phân loại sản phẩm đạt/lỗi** từ ảnh chụp với độ chính xác ≥ 95% để thay thế kiểm tra thị giác bằng mắt người.

#### Mục tiêu project

- Xây dựng CNN phân loại ảnh sản phẩm đạt/lỗi với **Accuracy ≥ 90%, Recall ≥ 95%** (không bỏ sót sản phẩm lỗi).
- Sử dụng **Transfer Learning** (VGG16, ResNet50, EfficientNet) thay vì train from scratch.
- Visualize **vùng quyết định** bằng Grad-CAM — chứng minh mô hình "nhìn" đúng chỗ.
- Tính toán **tốc độ inference**: xử lý bao nhiêu ảnh/giây? Có khả thi cho real-time không?

#### Các bước thực hiện bắt buộc

1. **Data preparation:** Chia train/val/test (70/15/15). Data augmentation (rotation, flip, brightness) để tăng robustness.
2. **Baseline CNN:** Tự xây dựng CNN 3–5 lớp. Đánh giá overfitting bằng learning curves.
3. **Transfer Learning:** Freeze base layers → fine-tune top layers → unfreeze và train toàn bộ (3-phase).
4. **Grad-CAM:** Visualize attention map trên ảnh test — mô hình tập trung vào vùng nào?
5. **Inference optimization:** So sánh batch inference vs single image. Đo thời gian xử lý.

#### Dữ liệu gợi ý

| Nguồn | Link | Ghi chú |
|-------|------|---------|
| MVTec AD Dataset | [MVTec](https://www.mvtec.com/company/research/datasets/mvtec-ad) | 15 loại sản phẩm |
| Casting Defect | [Kaggle](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product) | 7.348 ảnh |

#### Rubric chấm điểm

| Tiêu chí | Điểm tối đa |
|----------|------------|
| Baseline CNN + learning curves | 15 |
| Transfer Learning đúng 3-phase | 25 |
| Accuracy ≥ 90%, Recall ≥ 95% trên test set | 25 |
| Grad-CAM visualization & giải thích | 20 |
| Inference speed analysis | 15 |

---

*Lưu ý: Tất cả project yêu cầu notebook chạy được, báo cáo PDF và thuyết trình. Bonus điểm (+5 đến +10) cho nhóm dùng dữ liệu thực từ doanh nghiệp hoặc triển khai sản phẩm thực tế có người dùng.*

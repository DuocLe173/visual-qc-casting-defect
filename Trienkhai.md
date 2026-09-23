# 📘 HỒ SƠ TRIỂN KHAI TOÀN DIỆN DỰ ÁN — PROJECT 13
## Hệ Thống Kiểm Soát Chất Lượng Sản Phẩm Bằng Thị Giác Máy Tính (Visual QC)

> **Môn học:** Trí Tuệ Nhân Tạo (AI & Deep Learning)  
> **Chủ đề:** Phát hiện khuyết tật bề mặt phôi đúc kim loại (*Casting Defect Detection*)  
> **Tài liệu hợp nhất:** Tổng hợp toàn bộ hồ sơ kỹ thuật từ ý tưởng, kế hoạch, hướng dẫn thực thi đến phản biện chuyên gia và hệ sinh thái web.

---

## 📑 MỤC LỤC TỔNG QUAN

1. [Phần 1: Đặc Tả Đề Tài — Project 13 (project_13.md)](#phần-1-đặc-tả-đề-tài--project-13-visual-quality-control)
2. [Phần 2: Ý Tưởng & Định Hướng Mở Rộng Dự Án (ytuong.md)](#phần-2-ý-tưởng--định-hướng-mở-rộng-dự-án)
3. [Phần 3: Kế Hoạch Thực Hiện 4 Tuần & Rubric Đánh Giá (kehoach13.md)](#phần-3-kế-hoạch-thực-hiện-4-tuần--rubric-đánh-giá)
4. [Phần 4: Hướng Dẫn Chi Tiết Thực Chiến Từ A Đến Z (huongdan.md)](#phần-4-hướng-dẫn-chi-tiết-thực-chiến-từ-a-đến-z)
5. [Phần 5: Nhận Xét, Phản Biện Chuyên Gia & Tối Ưu Hóa Kiến Trúc (Nhanxet.md)](#phần-5-nhận-xét-phản-biện-chuyên-gia--tối-ưu-hóa-kiến-trúc)
6. [Phần 6: Hệ Sinh Thái Công Nghệ & Danh Mục Nền Tảng Web (webapp.md)](#phần-6-hệ-sinh-thái-công-nghệ--danh-mục-nền-tảng-web-webapp)

---



================================================================================
# PHẦN 1: ĐẶC TẢ ĐỀ TÀI — PROJECT 13 (VISUAL QUALITY CONTROL)
> **Nguồn tài liệu gốc:** `project_13.md`
================================================================================

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

---


================================================================================
# PHẦN 2: Ý TƯỞNG & ĐỊNH HƯỚNG MỞ RỘNG DỰ ÁN
> **Nguồn tài liệu gốc:** `ytuong.md`
================================================================================

# KẾ HOẠCH TRIỂN KHAI KỸ THUẬT: MÔ HÌNH BĂNG CHUYỀN KIỂM ĐỊNH SẢN PHẨM AI (PROJECT 13)
### Phiên bản: Sinh viên DIY — Chi phí Tiết kiệm (~0đ đến 50.000 VNĐ)

> **Cơ quan thẩm định & Hướng dẫn:** Cố vấn Kỹ thuật & Kiến trúc sư Trưởng Hệ thống AI  
> **Dự án mục tiêu:** Project 13 — Kiểm soát Chất lượng Sản phẩm bằng Ảnh (Visual QC)  
> **Đối tượng thực hiện:** Sinh viên năm 2 ngành HTTT / Khoa học Dữ liệu / Kinh tế (Chưa có nền tảng cơ khí phức tạp)  
> **Định vị dự án:** Tối ưu hóa 100% tài nguyên sẵn có (Laptop, Điện thoại, Bìa carton), tập trung tối đa vào **Hàm lượng Trí Tuệ Nhân Tạo (90 điểm)** và nhận trọn vẹn **Điểm thưởng sáng tạo thực tế (+5 đến +10 điểm Bonus)**.

---

## 1. TỔNG QUAN Ý TƯỞNG & SƠ ĐỒ NGUYÊN LÝ HOẠT ĐỘNG

### 1.1. Triết lý thiết kế "Carton DIY — AI First"
Dự án được chuyển hướng từ mô hình cơ khí đắt đỏ sang mô hình **Carton Maker Tái Chế**:
- **Khung & Băng chuyền:** Chế tạo hoàn toàn từ vỏ thùng carton cũ, đũa tre và lõi giấy cuộn.
- **Vận hành:** Dùng tay quay cơ học êm ái (hoặc gắn motor đồ chơi mini 20.000 VNĐ chạy pin).
- **Thu nhận ảnh (Vision):** Tận dụng chiếc **điện thoại thông minh của sinh viên** kết nối với laptop qua cáp USB làm Camera độ phân giải cao ($1080\text{p}$).
- **Bộ não phân tích (Brain):** Laptop sinh viên chạy mô hình Deep Learning (Transfer Learning MobileNetV2 / ResNet50 từ tệp [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd)) để nhận diện thùng hàng đạt chuẩn hay bị móp/rách.
- **Phản hồi kết quả:** Trực quan hóa ngay trên màn hình laptop (Khung viền XANH/ĐỎ + Bản đồ nhiệt Grad-CAM) kết hợp loa laptop phát âm thanh cảnh báo.

```
                  ┌────────────────────────────────────────────────────────┐
                  │          BUỒNG CHỤP QUANG HỌC BẰNG BÌA CARTON          │
                  │   [Đèn học để bàn / Flash]     [Điện thoại Smartphone] │
                  └─────────────────────────┬──────────────────────▲───────┘
                                            │                      │ Luồng video 1080p
                                            ▼                      │ (qua cáp USB / DroidCam)
  [KHU VỰC ĐẶT HỘP]                 [VỊ TRÍ CAMERA SOI]            │              [KHU VỰC PHÂN LOẠI]
    (Bìa Carton)                     (Vỏ hộp trôi qua)             │                 (Hộp Về Đích)
                                                                   │
    ┌─────────────┐                  ┌─────────────┐               │              ┌─────────────┐
    │ Vỏ hộp nhỏ  │ ── Băng chuyền ─>│ Vỏ hộp nhỏ  │ ─ Băng giấy ──┴─ Băng giấy ─>│  Hộp ĐẠT   │ ──> (Thùng Thành Phẩm)
    │ (Cần kiểm)  │    giấy carton   │ (Đang quét) │                              └─────────────┘
    └─────────────┘                  └─────────────┘                                     │
           │                                                                             ▼ (Nếu LỖI: Gạt tay)
     [Quay tay trục]                                                              ┌─────────────┐
     (Hoặc motor 20k)                                                             │  Hộp LỖI    │ ──> (Khay Phế Phẩm)
                                                                                  └─────────────┘
                                                                                         ▲
                                             ┌───────────────────────────────────────────┴─────┐
                                             │             MÁY TÍNH LAPTOP SINH VIÊN           │
                                             │  • OpenCV bắt khung hình phôi                   │
                                             │  • Model AI: MobileNetV2 (Inference ~ 30ms)     │
                                             │  • Màn hình: Bật khung XANH (Pass) / ĐỎ (Fail)  │
                                             │  • Grad-CAM: Khoanh đốm đỏ vị trí bị móp        │
                                             │  • Loa Laptop: Bíp "PASS" hoặc "CẢNH BÁO LỖI"   │
                                             └─────────────────────────────────────────────────┘
```

---

### 1.2. Kịch bản vận hành thực tế khi Demo trước Giảng viên

1. **Khởi động:** Bạn mở laptop, cắm dây cáp sạc điện thoại vào máy tính, bật ứng dụng **DroidCam** và chạy script Python `demo_qc.py`.
2. **Nạp phôi:** Bạn đặt một vỏ hộp nhỏ (như vỏ bao diêm, hộp thuốc hoặc hộp carton mini) lên đầu băng tải giấy.
3. **Di chuyển:** Bạn dùng tay xoay nhẹ núm quay ở con lăn. Băng tải giấy di chuyển êm ái đưa hộp trôi vào bên trong buồng che carton.
4. **Quét & Phân tích AI:**
   - Camera điện thoại truyền hình ảnh góc thẳng đứng xuống laptop.
   - Thuật toán tự động phát hiện hộp xuất hiện trong vùng quan sát (ROI).
   - Mô hình AI quét bề mặt trong vòng **$30\text{ ms}$**:
     - **Nếu hộp nguyên vẹn:** Màn hình laptop hiện viền **XANH LÁ CÂY**, chữ to **"PASS - THÙNG ĐẠT CHUẨN"**, loa kêu *"Tít"*. Hộp trôi thẳng về cuối băng chuyền.
     - **Nếu hộp bị bẹp góc hoặc rách mép:** Màn hình lập tức đổi sang khung viền **ĐỎ RỰC**, nhấp nháy **"FAIL - DEFECT DETECTED"**, loa laptop cảnh báo. Đồng thời, một khung ảnh phụ hiện bản đồ nhiệt **Grad-CAM** làm nổi bật đúng vị trí góc hộp bị móp!
5. **Cơ chế phân loại:** Nhìn tín hiệu đỏ trên màn hình, bạn dùng tay gạt nhẹ tấm lẫy bìa carton bên hông băng chuyền để hộp lỗi trượt sang khay chứa hàng lỗi.

---

## 2. ĐỊNH HƯỚNG KỸ THUẬT & KIẾN TRÚC PHẦN MỀM

Vì không dùng các bo mạch đắt tiền, toàn bộ sức mạnh công nghệ được dồn vào **Mã nguồn Python trên Laptop**, vừa đúng trọng tâm môn học vừa không tốn chi phí.

### 2.1. Cấu hình phần cứng tối giản
- **Thiết bị ghi hình:** Camera sau của điện thoại Android / iPhone qua app **DroidCam Client** (hoặc Iriun Webcam).
  - Tốc độ khung hình: $30\text{ fps}$ mượt mà.
  - Độ phân giải truyền qua USB: $1280 \times 720$ hoặc $1920 \times 1080$.
  - Ưu điểm: Tận dụng cảm biến camera siêu nét của điện thoại, tự động đo sáng và bắt nét macro.
- **Ánh sáng môi trường:** Tận dụng 1 chiếc **đèn học để bàn** chiếu qua một lớp giấy A4 mỏng (đóng vai trò màng tán xạ ánh sáng) để triệt tiêu bóng đổ.

---

### 2.2. Pipeline xử lý thời gian thực trên Laptop (Python + OpenCV + Keras)

Quy trình xử lý hoàn toàn tự động chỉ với 1 webcam điện thoại:

```
[Khung hình từ DroidCam qua OpenCV: cv2.VideoCapture(1)]
                          │
                          ▼
[Vùng quan sát cố định (ROI Box): 400x400 giữa màn hình]
                          │
                          ▼
[Phát hiện phôi tự động (Auto-Trigger bằng độ sai khác nền)]
   - Khi không có hộp: Bỏ qua (Idle)
   - Khi hộp trôi vào giữa khung: Kích hoạt phân loại (Capture Event)
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  MÔ HÌNH HỌC MÁY (TẬN DỤNG CODE TỪ DHL.qmd)                 │
│  • Kiến trúc: Transfer Learning với MobileNetV2 (pre-train) │
│  • Kích thước đầu vào: 224x224 pixel                        │
│  • Thời gian chạy trên CPU Laptop: ~25 - 35 ms/ảnh          │
│  • Ngưỡng phân loại an toàn: tau = 0.35 (Recall >= 95%)     │
└─────────────────────────┬───────────────────────────────────┘
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
   [ĐÁNH GIÁ NHÃN]                  [BẢN ĐỒ NHIỆT GRAD-CAM]
   P(Damaged) >= 0.35               Tính Gradient tầng Conv cuối
   -> Viền ĐỎ + Loa kêu             Tô màu đỏ vào vết móp thực tế
```

---

## 3. DANH MỤC NGUYÊN VẬT LIỆU TỰ LÀM (BOM DIY — ~0Đ ĐẾN 50K)

Bạn có thể chuẩn bị toàn bộ hệ thống này trong vòng **1 buổi tối** bằng các vật dụng quanh nhà hoặc phòng trọ:

| STT | Vật liệu / Thiết bị | Nguồn tìm kiếm | Chi phí ước tính | Vai trò trong hệ thống |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Thùng bìa carton cũ** | Xin tạp hóa / Thùng mì tôm / Hộp bưu phẩm cũ | **0 VNĐ** | Cắt làm khung thành 2 bên, chân đế và hộp che sáng |
| 2 | **2 Lõi cuộn giấy** | Lõi màng bọc thực phẩm / Lõi giấy vệ sinh / Ống nước | **0 VNĐ** | Làm 2 con lăn tròn dẫn động băng chuyền |
| 3 | **2 Đũa gỗ / Que tre** | Đũa ăn cơm dùng 1 lần / Xiên thịt nướng | **0 VNĐ** | Luồn qua tâm lõi giấy làm trục xoay |
| 4 | **Dây đai băng chuyền** | Tờ bìa lịch cũ / Dải vải / Băng dính bản to dán ngược | **0 VNĐ** | Vòng qua 2 con lăn để làm mặt trượt phẳng cho hộp |
| 5 | **Keo dán & Băng dính** | Keo 502 / Súng bắn keo nến / Băng dính 2 mặt | **10.000 – 15.000 VNĐ** | Cố định các mối nối khung carton |
| 6 | **Điện thoại thông minh** | Smartphone cá nhân (Android / iPhone) | **0 VNĐ** *(Sẵn có)* | Biến thành camera quét $1080\text{p}$ qua app DroidCam |
| 7 | **Cáp sạc USB** | Cáp sạc điện thoại có sẵn | **0 VNĐ** *(Sẵn có)* | Cắm từ điện thoại vào laptop để truyền hình ảnh |
| 8 | **Đèn học để bàn** | Đèn bàn học sinh (hoặc bật Flash điện thoại) | **0 VNĐ** *(Sẵn có)* | Cung cấp ánh sáng trắng ổn định phía trên buồng chụp |
| 9 | **Laptop cá nhân** | Máy tính học tập của bạn | **0 VNĐ** *(Sẵn có)* | Chạy chương trình AI, hiển thị kết quả và phát loa |
| 10 | *(Tùy chọn nâng cao)* Động cơ vàng | Động cơ vàng TT motor đồ chơi + Hộp 2 pin tiểu | **~25.000 VNĐ** *(Trên Shopee)* | Dành cho bạn nào lười quay tay, muốn băng tải tự trôi |
| **TỔNG**| **CHI PHÍ ĐẦU TƯ THỰC TẾ** | | **~10.000 – 35.000 VNĐ** | **Rẻ gấp 50 lần bản cơ khí, phù hợp 100% sinh viên!** |

---

## 4. QUY TRÌNH THỰC HIỆN 4 TUẦN (WBS RÚT GỌN)

Lộ trình này thiết kế riêng cho sinh viên năm 2: **Dễ làm, không áp lực phần cứng, chắc chắn đạt điểm A.**

```
Tuần 1: Chuẩn bị dữ liệu + Làm băng chuyền bìa carton (1 buổi tối)
Tuần 2: Train mô hình MobileNetV2 trên Google Colab theo file DHL.qmd
Tuần 3: Viết script Python giao diện Webcam trên Laptop + Tích hợp Grad-CAM
Tuần 4: Chạy thử thực tế trên băng chuyền carton, quay clip demo & làm slide báo cáo
```

### Tuần 1: Cắt dán mô hình bìa carton & Cài đặt phần mềm (Ước tính 3–4 giờ)
- **Buổi 1 (Cơ khí bìa carton):**
  - Cắt 2 miếng bìa carton dài $35\text{ cm}$, rộng $10\text{ cm}$ làm thanh chắn 2 bên.
  - Luồn đũa gỗ qua 2 lõi giấy, đục lỗ trên thành bìa để gắn 2 con lăn vào.
  - Cắt dải bìa lịch phẳng rộng $8\text{ cm}$, dán 2 đầu lại vòng qua 2 con lăn làm mặt băng tải.
  - Gắn một nắp chai nhựa vào đầu đũa làm tay quay. Thử quay tay: Thấy băng giấy di chuyển mượt là hoàn tất!
- **Buổi 2 (Cài DroidCam):**
  - Tải app DroidCam trên CH Play / App Store và cài DroidCam Client trên laptop.
  - Cắm cáp USB, bật USB Debugging: Màn hình laptop hiển thị ngay video camera điện thoại.

### Tuần 2: Huấn luyện mô hình AI trên Google Colab (Theo chuẩn môn học)
- Mở tệp **[DHL.qmd](file:///e:/Project%20SIC/DHL.qmd)** đã chuẩn bị sẵn trong thư mục dự án.
- Tải dataset thùng hàng bưu kiện từ Kaggle (`Damaged and Intact Packages`).
- Chạy huấn luyện mạng **MobileNetV2** (hoặc **ResNet50**) qua 3 phase Transfer Learning trên Colab (mất khoảng 15 phút GPU miễn phí).
- Tải file trọng số mô hình đã lưu: `package_model.h5` (hoặc `model.keras`) về laptop.

### Tuần 3: Lập trình giao diện hiển thị trên Laptop
- Viết 1 file Python đơn giản `app_demo.py`:
  - Dùng thư viện OpenCV mở webcam từ DroidCam.
  - Cắt vùng giữa màn hình đưa vào mô hình dự đoán.
  - Nếu xác suất Lỗi $\ge 0.35 \rightarrow$ Vẽ viền ĐỎ + Ghi text "DEFECT: DAMAGED" + Phát âm thanh `winsound.Beep()`.
  - Tích hợp hàm hiển thị bản đồ nhiệt **Grad-CAM** kế bên ảnh gốc.

### Tuần 4: Chạy thử nghiệm, quay Video và hoàn tất Báo cáo
- Đặt 10 vỏ hộp nhỏ (5 hộp đẹp phẳng phiu, 5 hộp tự lấy tay bóp móp góc hoặc rách mép).
- Vừa quay tay con lăn, vừa quay lại màn hình laptop ghi nhận cả 10 hộp được phân loại chuẩn xác 100%.
- Đưa video clip và hình ảnh mô hình bìa carton vào Slide thuyết trình. Giảng viên chắc chắn sẽ cộng trọn vẹn điểm thưởng sáng tạo thực tế!

---

## 5. TÍNH TOÁN VẬN TỐC & TIÊU CHÍ NGHIỆM THU

### 5.1. Bài toán đồng bộ giữa tay quay và tốc độ máy tính

Một lo ngại phổ biến: *"Liệu mình quay tay quá nhanh thì máy tính có nhận diện kịp không?"*

Hãy xem phép tính toán kỹ thuật dưới đây:
- Thời gian mô hình AI xử lý 1 ảnh trên CPU laptop: $t_{\text{AI}} \approx 30 \text{ ms} = 0.03 \text{ giây}$ (tương đương tốc độ quét $33 \text{ ảnh/giây}$).
- Chiều rộng vùng quét của camera: $W = 15 \text{ cm}$.
- Khi bạn dùng tay quay nhẹ nhàng, vận tốc trượt của vỏ hộp trên băng giấy:
  $$v_{\text{quay\_tay}} \approx 5 \text{ cm/s}$$
- **Thời gian vỏ hộp nằm trong tầm nhìn camera:**
  $$t_{\text{nhìn}} = \frac{W}{v} = \frac{15 \text{ cm}}{5 \text{ cm/s}} = 3.0 \text{ giây}$$
- **Số khung hình máy tính quét được khi hộp trôi qua:**
  $$N_{\text{frames}} = 3.0 \text{ giây} \times 30 \text{ fps} = 90 \text{ khung hình!}$$

> 💡 **KẾT LUẬN TOÁN HỌC:**  
> Trong 3 giây hộp trôi qua tầm mắt, mô hình AI có cơ hội quét và suy luận tới **90 lần**. Do đó, bạn quay tay với tốc độ bình thường thì máy tính **thừa thời gian để nhận diện chính xác 100%**, hoàn toàn không có hiện tượng bị trôi hay bỏ lọt lỗi!

---

### 5.2. Bảng đối chiếu mục tiêu đạt điểm tối đa môn học

| Tiêu chí Rubric môn học | Điểm tối đa | Cách đạt điểm với mô hình DIY |
| :--- | :---: | :--- |
| **1. Baseline CNN + Learning Curves** | 15đ | Có sẵn code CNN 3 lớp trong file [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd), vẽ biểu đồ Loss/Accuracy đầy đủ. |
| **2. Transfer Learning 3-Phase** | 25đ | Áp dụng đúng quy trình: Freeze base $\rightarrow$ Fine-tune tầng cuối $\rightarrow$ Đánh giá. |
| **3. Accuracy $\ge 90\%$, Recall $\ge 95\%$** | 25đ | Tinh chỉnh ngưỡng phân loại $\tau = 0.35$ trên PR-Curve để không bỏ sót thùng lỗi. |
| **4. Grad-CAM Visualization** | 20đ | Hiển thị trực tiếp bản đồ nhiệt vùng móp trên màn hình laptop khi demo. |
| **5. Phân tích tốc độ Inference** | 15đ | Báo cáo chi tiết độ trễ: $30\text{ ms/ảnh}$, FPS thực tế trên webcam điện thoại. |
| **ĐIỂM THƯỞNG SÁNG TẠO (BONUS)** | **+5 đến +10đ** | **Ăn trọn điểm thưởng:** Mô hình băng chuyền carton DIY hoạt động trực quan trước mắt hội đồng! |
| **TỔNG ĐIỂM DỰ KIẾN** | **100/100 (Điểm A+)** | |

---

## 6. LỜI KHUYÊN DÀNH CHO BẠN ĐỂ BẮT ĐẦU NGAY HÔM NAY

1. **Đừng tự ti vì làm bằng bìa carton:** Trong kỹ thuật, việc giải quyết một bài toán phức tạp bằng công cụ đơn giản với chi phí thấp nhất luôn được coi là **đỉnh cao của sự sáng tạo (Jugaad Engineering)**.
2. **Ưu tiên phần mềm trước:** Dành 80% thời gian cho bài tập Colab theo hướng dẫn trong [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd). Khi mô hình đạt Accuracy cao, việc gắn vào mô hình bìa carton chỉ mất đúng 1 buổi tối.
3. **Mọi tài liệu đã sẵn sàng:** Toàn bộ công thức, kịch bản dữ liệu và mã nguồn đã được định hình trọn vẹn trong thư mục dự án của bạn!

---


================================================================================
# PHẦN 3: KẾ HOẠCH THỰC HIỆN 4 TUẦN & RUBRIC ĐÁNH GIÁ
> **Nguồn tài liệu gốc:** `kehoach13.md`
================================================================================

# KẾ HOẠCH THỰC HIỆN — PROJECT 13
## Kiểm soát Chất lượng Sản phẩm bằng Ảnh (Visual QC)

> **Môn học:** Trí Tuệ Nhân Tạo  
> **Loại bài toán:** Image Classification (CNN + Transfer Learning)  
> **Độ khó:** ⭐⭐⭐ Trung bình  
> **Hình thức:** Cá nhân (1 người thực hiện)  
> **Đối tượng phù hợp:** HTTT, Khoa học Dữ liệu, Sản xuất

---

## 1. MỤC TIÊU

| # | Mục tiêu | Chỉ số thành công |
|---|----------|-------------------|
| 1 | Phân loại ảnh sản phẩm **đạt / lỗi** | Accuracy ≥ 90%, Recall ≥ 95% |
| 2 | Áp dụng **Transfer Learning** | So sánh VGG16, ResNet50, EfficientNet |
| 3 | Giải thích mô hình bằng **Grad-CAM** | Visualize vùng mô hình "nhìn" vào |
| 4 | Đánh giá **tốc độ inference** | Số ảnh/giây, khả năng real-time |

---

## 2. TIMELINE CÁ NHÂN (4 tuần)

### Tổng quan

```
Tuần 1  │ Chuẩn bị môi trường + Thu thập & khám phá dữ liệu
Tuần 2  │ Xây Baseline CNN + Transfer Learning Phase 1-2
Tuần 3  │ Fine-tune toàn bộ + Grad-CAM + Inference benchmark + PR Curve
Tuần 4  │ Tổng hợp kết quả · Viết báo cáo · Chuẩn bị thuyết trình
```

### Lịch làm việc chi tiết theo ngày

| Tuần | Ngày | Công việc cụ thể | Thời lượng ước tính | Trạng thái |
|:---:|:---:|---|:---:|:---:|
| **1** | Ngày 1 | Tạo tài khoản Kaggle + Google Colab, cài đặt môi trường | 1–2h | ✅ Hoàn thành |
| | Ngày 2 | Tải dataset Casting Defect từ Kaggle, tổ chức thư mục | 1h | ✅ Hoàn thành |
| | Ngày 3 | EDA: đếm ảnh mỗi lớp, xem phân phối, kích thước ảnh, plot mẫu | 2–3h | ✅ Hoàn thành |
| | Ngày 4 | Chia train/val/test (70/15/15), kiểm tra class imbalance | 2h | ✅ Hoàn thành |
| | Ngày 5 | Viết pipeline Data Augmentation (chỉ trên tập Train!) | 2–3h | ✅ Hoàn thành |
| | Ngày 6–7 | Review lại notebook EDA, chỉnh sửa, commit lên GitHub | 1–2h | ✅ Đã đẩy lên GitHub |
| **2** | Ngày 8 | Xây Baseline CNN (3–5 Conv layers) | 3h | ✅ Hoàn thành |
| | Ngày 9 | Train Baseline 20–30 epochs, vẽ Learning Curves | 2–3h | ✅ Hoàn thành (Learning Curves) |
| | Ngày 10 | Đánh giá overfitting, thêm Dropout/L2, ghi metrics | 2h | ✅ Hoàn thành (Acc: 97.69%, Recall: 95.91%) |
| | Ngày 11 | Transfer Learning Phase 1: Load VGG16, freeze, train head | 3h | ✅ Hoàn thành |
| | Ngày 12 | Transfer Learning Phase 2: Unfreeze top layers, fine-tune | 3h | ✅ Hoàn thành |
| | Ngày 13–14 | Lặp lại Phase 1-2 cho ResNet50 và EfficientNetB0 | 4–5h | ✅ Hoàn thành (Acc > 99.3%, Recall > 98.7%) |
| **3** | Ngày 15 | Transfer Learning Phase 3: Full fine-tune cho model tốt nhất | 3h | ✅ Hoàn thành (Checkpoint Best Model) |
| | Ngày 16 | So sánh kết quả 3 model, lập bảng tổng hợp | 2h | ✅ Hoàn thành (CSV + Biểu đồ đối chuẩn) |
| | Ngày 17 | Implement Grad-CAM, tạo heatmap ≥ 10 ảnh | 3–4h | ✅ Hoàn thành (10 ảnh mẫu Đạt & Lỗi) |
| | Ngày 18 | Viết phân tích Grad-CAM: mô hình nhìn vào đâu? | 2h | ✅ Hoàn thành (Soi trúng vết nứt rỗ kim loại) |
| | Ngày 19 | Đo inference speed (single image + batch), vẽ biểu đồ | 2–3h | ✅ Hoàn thành (Single Latency + Batch FPS) |
| | Ngày 20 | Vẽ Precision-Recall Curve, tìm sweet spot threshold | 2h | ✅ Hoàn thành (AP = 0.9999, Precision 100%) |
| | Ngày 21 | Review toàn bộ notebook, fix bugs, chạy lại Restart & Run All | 2–3h | ✅ Hoàn thành (Tích hợp trọn vẹn trong 1_EDA) |
| **4** | Ngày 22–23 | Viết báo cáo PDF (≤ 15 trang) | 4–5h |
| | Ngày 24–25 | Làm slide thuyết trình (tối đa 12 slides) | 3–4h |
| | Ngày 26 | Tập thuyết trình (10 phút), chỉnh slide | 2h |
| | Ngày 27–28 | Buffer: sửa lỗi cuối, hoàn thiện, nộp bài | 2h |

> ⏱️ **Tổng thời lượng ước tính:** ~55–70 giờ trong 4 tuần (~2h/ngày trung bình)

---

## 3. BẢNG CHUẨN BỊ CHI TIẾT

### 3.1. Tài khoản cần tạo / đăng nhập

| # | Tài khoản | Mục đích | Chi phí | Ghi chú |
|---|-----------|----------|---------|---------|
| 1 | **Google Account** | Dùng Google Colab (GPU miễn phí) | Miễn phí | Đã có sẵn thì bỏ qua |
| 2 | **Kaggle Account** | Tải dataset Casting Defect | Miễn phí | Cần xác minh số điện thoại để tải data |
| 3 | **GitHub Account** | Quản lý code, lưu version | Miễn phí | Tạo repo mới cho project |

### 3.2. Phần mềm & thư viện cần cài đặt

| # | Thứ cần cài | Cách cài | Ghi chú |
|---|-------------|----------|---------|
| 1 | Python 3.8+ | Có sẵn trên Google Colab | Không cần cài nếu dùng Colab |
| 2 | TensorFlow / Keras | `pip install tensorflow` | Colab đã có sẵn |
| 3 | NumPy, Pandas | `pip install numpy pandas` | Colab đã có sẵn |
| 4 | OpenCV | `pip install opencv-python` | Xử lý ảnh |
| 5 | Matplotlib, Seaborn | `pip install matplotlib seaborn` | Vẽ biểu đồ |
| 6 | tf-keras-vis | `pip install tf-keras-vis` | Dùng cho Grad-CAM |
| 7 | scikit-learn | `pip install scikit-learn` | Chia data, metrics, PR Curve |
| 8 | Kaggle API (tuỳ chọn) | `pip install kaggle` | Tải dataset bằng command line |

> 💡 **Mẹo:** Tạo 1 cell đầu notebook chứa tất cả lệnh `pip install` để chạy 1 lần khi mở Colab.

### 3.3. Dataset cần tải

| # | Dataset | Link tải | Dung lượng | Cách tải |
|---|---------|----------|------------|----------|
| 1 | **Casting Defect** (⭐ Khuyên dùng) | [Kaggle](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product) | ~830 MB | Tải file ZIP trực tiếp từ Kaggle hoặc dùng `kaggle datasets download` |
| 2 | MVTec AD (tuỳ chọn nâng cao) | [MVTec](https://www.mvtec.com/company/research/datasets/mvtec-ad) | ~4.9 GB | Đăng ký email để nhận link tải |

### 3.4. Cấu trúc thư mục cần tạo

```
project_13_visual_qc/
├── data/
│   ├── raw/                  ← Ảnh gốc sau khi giải nén
│   ├── train/                ← 70% ảnh (augmentation áp dụng ở đây)
│   │   ├── ok/
│   │   └── defect/
│   ├── val/                  ← 15% ảnh (KHÔNG augment)
│   │   ├── ok/
│   │   └── defect/
│   └── test/                 ← 15% ảnh (KHÔNG augment)
│       ├── ok/
│       └── defect/
├── notebooks/
│   ├── 1_EDA.ipynb
│   ├── 2_Baseline_CNN.ipynb
│   ├── 3_Transfer_Learning.ipynb
│   ├── 4_GradCAM.ipynb
│   └── 5_Inference_Speed.ipynb
├── models/                   ← Lưu model weights (.h5 / .keras)
├── results/                  ← Hình ảnh kết quả, biểu đồ
├── report/
│   ├── bao_cao.pdf
│   └── slides.pptx
└── README.md
```

> 💡 Chia thành nhiều notebook độc lập giúp dễ quản lý, dễ debug, và tránh notebook quá dài.

### 3.5. Tài liệu cần đọc / xem trước

| # | Tài liệu | Link | Khi nào đọc |
|---|-----------|------|-------------|
| 1 | Bài giảng Ch.8 Neural Network | Slide môn học | Trước tuần 1 |
| 2 | Bài giảng Ch.9 CNN | Slide môn học | Trước tuần 1 |
| 3 | Transfer Learning guide (Keras) | [Keras docs](https://keras.io/guides/transfer_learning/) | Đầu tuần 2 |
| 4 | Grad-CAM paper (tóm tắt) | [arXiv](https://arxiv.org/abs/1610.02391) | Đầu tuần 3 |
| 5 | Precision-Recall Curve (scikit-learn) | [sklearn docs](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html) | Tuần 3 |

### 3.6. Chi phí

| Hạng mục | Chi phí | Ghi chú |
|----------|---------|---------|
| Google Colab (GPU T4) | **Miễn phí** | Giới hạn ~12h/session, đủ dùng |
| Colab Pro (tuỳ chọn) | ~$10/tháng | GPU tốt hơn, session lâu hơn, KHÔNG bắt buộc |
| Kaggle dataset | **Miễn phí** | — |
| GitHub | **Miễn phí** | Repo public hoặc private |
| **Tổng chi phí tối thiểu** | **$0** | Hoàn toàn miễn phí nếu dùng Colab free |

---

## 4. CÁC BƯỚC THỰC HIỆN CHI TIẾT

### Bước 1 — Chuẩn bị dữ liệu

- [ ] Tải dataset từ Kaggle (Casting Defect) hoặc MVTec AD
- [ ] Chia tập: **Train 70% / Val 15% / Test 15%**
- [ ] Kiểm tra class imbalance (tỷ lệ lỗi/đạt)
- [ ] Áp dụng **Data Augmentation**:
  - Rotation (±15°)
  - Horizontal/Vertical Flip
  - Brightness & Contrast jitter
  - Zoom / Crop ngẫu nhiên
- [ ] Chuẩn hóa ảnh về kích thước đầu vào mô hình (224×224)

> ⚠️ **Lưu ý cực kỳ quan trọng:** Hãy đảm bảo rằng chỉ Augmentation trên tập Train. Nếu áp dụng Augmentation lên toàn bộ dataset trước khi chia, các ảnh biến thể của tập Test sẽ nằm trong tập Train, dẫn đến kết quả Accuracy/Recall cao "ảo" nhưng chạy thực tế sẽ rất tệ.

### Bước 2 — Baseline CNN

- [ ] Xây dựng CNN từ đầu với 3–5 Conv layers
- [ ] Cấu trúc gợi ý:
  ```
  Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Conv2D(128) → Flatten → Dense → Output
  ```
- [ ] Huấn luyện 20–30 epochs
- [ ] Vẽ **Learning Curves** (loss & accuracy trên train/val)
- [ ] Nhận diện hiện tượng overfitting → thêm Dropout / L2 nếu cần
- [ ] Ghi lại metrics: Accuracy, Precision, Recall, F1, Confusion Matrix

### Bước 3 — Transfer Learning (3 Phase)

#### Phase 1 — Feature Extraction (Freeze toàn bộ base)
- [ ] Load pretrained model (VGG16 / ResNet50 / EfficientNetB0)
- [ ] Freeze tất cả layers của base model
- [ ] Thêm classification head mới
- [ ] Train 10–15 epochs, LR = 1e-3

#### Phase 2 — Fine-tune Top Layers
- [ ] Unfreeze các layer cuối của base model (ví dụ: 2–4 lớp)
- [ ] Train thêm 10 epochs, LR giảm xuống 1e-4
- [ ] Theo dõi Val Recall — ưu tiên không bỏ sót lỗi

#### Phase 3 — Full Fine-tune
- [ ] Unfreeze toàn bộ model
- [ ] Train thêm 5–10 epochs với LR rất nhỏ (1e-5)
- [ ] So sánh kết quả 3 phase — trình bày bảng tổng hợp

### Bước 4 — Grad-CAM Visualization

- [ ] Implement Grad-CAM (có thể dùng thư viện `tf-keras-vis` hoặc viết tay)
- [ ] Áp dụng trên **≥ 10 ảnh test** (cả đạt & lỗi)
- [ ] Overlay heatmap lên ảnh gốc
- [ ] **Viết giải thích**: Mô hình tập trung vào vùng nào? Có hợp lý về nghiệp vụ không?
- [ ] Phát hiện trường hợp mô hình sai → phân tích nguyên nhân

### Bước 5 — Inference Speed Analysis

- [ ] Đo thời gian xử lý **Single Image** (latency per image)
- [ ] Đo thời gian xử lý **Batch** (batch size 16, 32, 64)
- [ ] Tính **throughput** (số ảnh/giây)
- [ ] Đánh giá: Với tốc độ này, có thể triển khai real-time trên dây chuyền sản xuất?
- [ ] (Tuỳ chọn) Thử TensorFlow Lite hoặc ONNX để tăng tốc

### Bước 6 — Precision-Recall Curve & Threshold Tuning

- [ ] Vẽ Precision-Recall Curve cho model tốt nhất
- [ ] Tìm **sweet spot** — điểm cân bằng tối ưu giữa Precision và Recall
- [ ] Thử nhiều threshold (0.3, 0.4, 0.5, 0.6) và so sánh kết quả
- [ ] Đưa ra khuyến nghị threshold phù hợp cho bài toán kinh doanh (ưu tiên Recall vì không được bỏ sót sản phẩm lỗi)

---

## 5. CÔNG CỤ & THƯ VIỆN

| Nhóm | Thư viện |
|------|----------|
| Framework DL | TensorFlow / Keras hoặc PyTorch |
| Data handling | NumPy, Pandas, OpenCV / Pillow |
| Visualization | Matplotlib, Seaborn |
| Grad-CAM | `tf-keras-vis`, `pytorch-grad-cam` |
| Metrics & Curves | scikit-learn (PR Curve, Confusion Matrix) |
| Môi trường | Google Colab (GPU T4 miễn phí) |
| Quản lý code | Git + GitHub |

---

## 6. DATASET GỢI Ý

| Dataset | Link | Đặc điểm |
|---------|------|----------|
| **Casting Defect** (Kaggle) | [Link](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product) | 7.348 ảnh, 2 class (ok/defect), dễ dùng |
| **MVTec AD** | [Link](https://www.mvtec.com/company/research/datasets/mvtec-ad) | 15 loại sản phẩm, phức tạp hơn |

> 💡 **Gợi ý:** Bắt đầu với **Casting Defect** vì dữ liệu gọn, nhãn rõ ràng. Nếu còn thời gian, thử thêm 1–2 category từ MVTec AD.

---

## 7. RUBRIC & PHÂN BỔ ĐIỂM

| Tiêu chí | Điểm tối đa | Ghi chú |
|----------|------------|---------|
| Baseline CNN + Learning Curves | 15 | Phải vẽ được biểu đồ, phân tích overfitting |
| Transfer Learning đúng 3-phase | 25 | Trình bày rõ từng phase, LR schedule |
| Accuracy ≥ 90%, Recall ≥ 95% | 25 | Đo trên **test set**, không phải val |
| Grad-CAM visualization & giải thích | 20 | Có hình ảnh + phân tích bằng lời |
| Inference speed analysis | 15 | Có số liệu cụ thể (ms/ảnh, ảnh/giây) |
| **Tổng** | **100** | |
| **Bonus** | +5 đến +10 | Dữ liệu thực từ doanh nghiệp / Triển khai thực tế |

---

## 8. CẤU TRÚC BÁO CÁO & NOTEBOOK

### Notebook (chia thành nhiều file)

| File | Nội dung |
|------|----------|
| `1_EDA.ipynb` | Import, Load data, Explore, Visualize phân phối |
| `2_Baseline_CNN.ipynb` | Build CNN, Train, Learning Curves, Evaluate |
| `3_Transfer_Learning.ipynb` | VGG16/ResNet50/EfficientNet, 3 Phase, So sánh |
| `4_GradCAM.ipynb` | Implement Grad-CAM, Overlay heatmap, Phân tích |
| `5_Inference_Speed.ipynb` | Benchmark tốc độ, PR Curve, Threshold tuning |

> 💡 Chia notebook độc lập giúp dễ quản lý và debug. Tránh tình trạng 1 notebook quá dài khó theo dõi.

### Báo cáo PDF (≤ 15 trang)
1. Giới thiệu bài toán & mục tiêu
2. Dữ liệu & tiền xử lý
3. Phương pháp (CNN, Transfer Learning, Grad-CAM)
4. Kết quả thực nghiệm
5. Phân tích & Thảo luận
6. Kết luận

### Slide thuyết trình (10 phút)
- Tối đa **12 slides**
- Phải có: demo Grad-CAM, bảng so sánh model, kết luận kinh doanh

---

## 9. CÁC RỦI RO & CÁCH XỬ LÝ

| Rủi ro | Xác suất | Giải pháp |
|--------|----------|-----------|
| Recall < 95% | Cao | Điều chỉnh threshold (từ 0.5 xuống 0.3–0.4), dùng class_weight |
| Overfitting mạnh | Trung bình | Tăng Dropout, dùng EarlyStopping, giảm complexity |
| Grad-CAM nhìn sai vùng | Thấp | Kiểm tra lại data augmentation, thêm dữ liệu |
| Hết RAM/GPU Colab | Trung bình | Giảm batch size, dùng `tf.data` pipeline |
| Dataset mất cân bằng | Trung bình | Dùng `class_weight`, oversampling hoặc Focal Loss |
| Làm 1 mình bị quá tải | Trung bình | Ưu tiên các phần có điểm cao trước (Transfer Learning 25đ, Metrics 25đ) |
| Mất kết quả training | Thấp | Save checkpoint sau mỗi phase, push lên GitHub thường xuyên |

> 💡 Nên bổ sung biểu đồ **Precision-Recall Curve** ở tuần 3 để tìm ra điểm cân bằng (Sweet Spot) tối ưu nhất cho doanh nghiệp, thay vì chỉ tập trung vào mỗi Recall.

---

## 10. CHECKLIST CUỐI DỰ ÁN

- [ ] Notebook chạy được từ đầu đến cuối (Restart & Run All)
- [ ] Accuracy ≥ 90% và Recall ≥ 95% trên **test set**
- [ ] Có Confusion Matrix rõ ràng
- [ ] Grad-CAM có ≥ 10 ảnh minh họa với giải thích
- [ ] Bảng so sánh 3 mô hình Transfer Learning
- [ ] Precision-Recall Curve với phân tích threshold
- [ ] Inference speed được báo cáo (ms/ảnh)
- [ ] Báo cáo PDF hoàn chỉnh
- [ ] Slide chuẩn bị xong trước ngày thuyết trình
- [ ] Tất cả code đã push lên GitHub

---


================================================================================
# PHẦN 4: HƯỚNG DẪN CHI TIẾT THỰC CHIẾN TỪ A ĐẾN Z
> **Nguồn tài liệu gốc:** `huongdan.md`
================================================================================

# HƯỚNG DẪN CHI TIẾT TỪ A ĐẾN Z — PROJECT 13

## Kiểm Soát Chất Lượng Sản Phẩm Bằng Ảnh (Visual QC)

> **Môn học:** Trí Tuệ Nhân Tạo  
> **Đề tài:** Project 13 — Visual Quality Control on Casting Defect Dataset  
> **Mục tiêu chính:** Accuracy ≥ 90%, Recall ≥ 95%, Explainable AI (Grad-CAM), Tối ưu Inference Speed  
> **Thực hiện:** Cá nhân / Nhóm  

---

## MỤC LỤC

1. [Tổng quan & Thiết lập Ban đầu (Giai đoạn 0)](#1-tổng-quan--thiết-lập-ban-đầu-giai-đoạn-0)
2. [Khám phá & Tiền xử lý Dữ liệu - Tuần 1 (Giai đoạn 1)](#2-khám-phá--tiền-xử-lý-dữ-liệu---tuần-1-giai-đoạn-1)
3. [Xây dựng & Huấn luyện Mô hình - Tuần 2 (Giai đoạn 2)](#3-xây-dựng--huấn-luyện-mô-hình---tuần-2-giai-đoạn-2)
4. [Phân tích Chuyên sâu: Grad-CAM & Benchmark - Tuần 3 (Giai đoạn 3)](#4-phân-tích-chuyên-sâu-grad-cam--benchmark---tuần-3-giai-đoạn-3)
5. [Ứng dụng Demo, Báo cáo & Thuyết trình - Tuần 4 (Giai đoạn 4)](#5-ứng-dụng-demo-báo-cáo--thuyết-trình---tuần-4-giai-đoạn-4)
6. [Checklist Đánh giá & Tiêu chí Chấm điểm (Rubric)](#6-checklist-đánh-giá--tiêu-chí-chấm-điểm-rubric)

---

## 1. TỔNG QUAN & THIẾT LẬP BAN ĐẦU (GIAI ĐOẠN 0)

### 1.1. Lấy Kaggle API Token (`kaggle.json`)

Dataset *Casting Defect* có dung lượng ~830 MB. Cách nhanh và tiện nhất là kéo dữ liệu trực tiếp vào Google Colab bằng Kaggle API (chỉ mất khoảng 15-30 giây).

1. Truy cập [Kaggle](https://www.kaggle.com/) và đăng nhập tài khoản.
2. Nhấp vào ảnh đại diện (avatar) góc trên bên phải $\rightarrow$ Chọn **Settings**.
3. Cuộn xuống phần **API** $\rightarrow$ Bấm nút **Create New Token**.
4. Trình duyệt sẽ tự động tải file `kaggle.json` về máy tính (lưu file này lại để dùng ở bước sau).

### 1.2. Tạo Repository trên GitHub

1. Mở [GitHub](https://github.com/) $\rightarrow$ Chọn **New Repository**.
2. Đặt tên Repo: `visual-qc-casting-defect` hoặc `project-13-visual-qc`.
3. Chế độ: **Public** (để giảng viên dễ xem) hoặc **Private**.
4. Tích chọn **Add a README file** và chọn `.gitignore` template **Python**.

### 1.3. Cấu trúc thư mục chuẩn của dự án

```text
Project SIC/
├── data/                      # Chứa dataset sau khi tải về (bỏ qua không push Git)
│   ├── raw/                   # Dữ liệu gốc sau khi giải nén
│   ├── train/                 # 70% dữ liệu (chỉ áp dụng Augmentation ở đây)
│   ├── val/                   # 15% dữ liệu (Validation)
│   └── test/                  # 15% dữ liệu (Đánh giá cuối cùng)
├── notebooks/                 # 5 Notebook độc lập theo tiến độ
│   ├── 1_EDA.ipynb            # Khám phá, trực quan hóa và tiền xử lý
│   ├── 2_Baseline_CNN.ipynb   # Mô hình CNN tự xây từ đầu & Learning curves
│   ├── 3_Transfer_Learning.ipynb # VGG16, ResNet50, EfficientNetB0 (3 Phase)
│   ├── 4_GradCAM.ipynb        # Bản đồ nhiệt giải thích quyết định của mô hình
│   └── 5_Inference_Speed.ipynb # Đo tốc độ trễ (latency), FPS & PR Curve
├── models/                    # Lưu trọng số mô hình (.keras hoặc .h5)
├── results/                   # Chứa biểu đồ, ma trận nhầm lẫn, ảnh Grad-CAM
├── report/                    # Chứa báo cáo PDF (<= 15 trang) và Slides (<= 12 trang)
├── app.py                     # Demo Web App (Streamlit) để lấy điểm Bonus (+5 đến +10)
├── requirements.txt           # Danh sách các thư viện Python
├── .gitignore                 # Bỏ qua data/, models/, .ipynb_checkpoints/
└── README.md                  # Giới thiệu tổng quan dự án
```

### 1.4. Ý Nghĩa & Vai Trò Của Từng File / Thư Mục Vừa Tạo

| Tên File / Thư Mục | Loại | Ý Nghĩa & Cách Sử Dụng |
| --- | :---: | --- |
| [notebooks/1_EDA.ipynb](file:///e:/Project%20SIC/notebooks/1_EDA.ipynb) | Jupyter Notebook | **Khám phá & Tiền xử lý dữ liệu:** Chứa code tải dataset tự động từ Kaggle, phân tích tỷ lệ phôi đúc Đạt/Lỗi, trực quan hóa ảnh khuyết tật, chia tỷ lệ 70/15/15 và viết pipeline Data Augmentation (chỉ áp dụng trên tập Train). |
| [notebooks/2_Baseline_CNN.ipynb](file:///e:/Project%20SIC/notebooks/2_Baseline_CNN.ipynb) | Jupyter Notebook | **Mô hình cơ sở (15 điểm):** Chứa kiến trúc mạng CNN tự xây dựng từ đầu (3-5 Conv layers), vẽ đồ thị Learning Curves (Loss & Accuracy) và phân tích hiện tượng Overfitting. |
| [notebooks/3_Transfer_Learning.ipynb](file:///e:/Project%20SIC/notebooks/3_Transfer_Learning.ipynb) | Jupyter Notebook | **Mô hình học chuyển giao (50 điểm):** Thực hiện quy trình chuẩn 3-Phase (Freeze base $\rightarrow$ Fine-tune tầng đỉnh $\rightarrow$ Full fine-tune) trên 3 kiến trúc: VGG16, ResNet50, EfficientNetB0; xuất ma trận nhầm lẫn và đạt mục tiêu Accuracy $\ge 90\%$, Recall $\ge 95\%$. |
| [notebooks/4_GradCAM.ipynb](file:///e:/Project%20SIC/notebooks/4_GradCAM.ipynb) | Jupyter Notebook | **Explainable AI (20 điểm):** Tạo bản đồ nhiệt (Heatmap) Grad-CAM phủ lên ảnh phôi đúc gốc cho $\ge 10$ ảnh để chứng minh mô hình thực sự soi vào vị trí nứt, rỗ khí chứ không nhìn lan man vào phông nền. |
| [notebooks/5_Inference_Speed.ipynb](file:///e:/Project%20SIC/notebooks/5_Inference_Speed.ipynb) | Jupyter Notebook | **Đo tốc độ & Tối ưu ngưỡng (15 điểm):** Đo độ trễ suy luận 1 ảnh (Latency ms/ảnh) và thông lượng theo batch (FPS); vẽ đồ thị Precision-Recall Curve để chọn ngưỡng phân loại tối ưu (Sweet Spot). |
| [app.py](file:///e:/Project%20SIC/app.py) | Python Script | **Demo Web App (Điểm thưởng +5 đến +10):** Giao diện web viết bằng thư viện Streamlit, cho phép kỹ sư/người dùng tải ảnh sản phẩm từ máy lên để mô hình dự đoán ngay tức thì kèm hiển thị Heatmap Grad-CAM. |
| [requirements.txt](file:///e:/Project%20SIC/requirements.txt) | Cấu hình | **Danh mục thư viện phụ thuộc:** Liệt kê các package Python (TensorFlow, OpenCV, Streamlit, Seaborn,...) để cài đặt nhanh bằng 1 câu lệnh `pip install -r requirements.txt`. |
| [.gitignore](file:///e:/Project%20SIC/.gitignore) | Cấu hình Git | **Chặn file không cần thiết:** Tự động ngăn Git tải lên các file dung lượng lớn (dataset `data/` ~830MB, trọng số mô hình `models/*.keras`), file tạm và token bảo mật `kaggle.json`. |
| [README.md](file:///e:/Project%20SIC/README.md) | Tài liệu Markdown | **Trang chủ giới thiệu dự án:** Hiển thị trực tiếp trên GitHub với huy hiệu (badges), mô tả đề tài, mục tiêu, kết quả thực nghiệm và hướng dẫn khởi chạy. |
| [models/](file:///e:/Project%20SIC/models/) | Thư mục | **Lưu trữ mô hình:** Nơi chứa các file trọng số mô hình đã huấn luyện xong (định dạng `.keras` hoặc `.h5`) để tái sử dụng trong web app hoặc Grad-CAM mà không cần train lại. |
| [results/](file:///e:/Project%20SIC/results/) | Thư mục | **Lưu kết quả & Hình ảnh:** Chứa các biểu đồ Learning curves, Confusion matrix, ảnh Heatmap Grad-CAM đã xuất ra để chèn vào báo cáo và slide thuyết trình. |
| [report/](file:///e:/Project%20SIC/report/) | Thư mục | **Báo cáo & Thuyết trình:** Nơi lưu file báo cáo PDF cuối kỳ ($\le 15$ trang) và file slide thuyết trình PowerPoint/Canva ($\le 12$ slide). |
| [data/](file:///e:/Project%20SIC/data/) | Thư mục | **Chứa dữ liệu ảnh:** Thư mục cục bộ lưu ảnh phôi đúc tải về từ Kaggle sau khi giải nén (chia thành `raw/`, `train/`, `val/`, `test/`). |
| [kehoach13.md](file:///e:/Project%20SIC/kehoach13.md) | Tài liệu Markdown | **Kế hoạch dự án:** Bảng phân bổ timeline 4 tuần theo từng ngày, công việc cụ thể và chi tiết thang điểm rubric của giảng viên. |
| [huongdan.md](file:///e:/Project%20SIC/huongdan.md) | Tài liệu Markdown | **Cẩm nang A - Z:** Tài liệu hướng dẫn thực chiến chi tiết từng bước từ chuẩn bị, code mẫu đến báo cáo và nộp bài. |

---

### 1.5. Thiết lập Google Colab

1. Truy cập [Google Colab](https://colab.research.google.com/).
2. Chọn **Runtime** $\rightarrow$ **Change runtime type** $\rightarrow$ Chọn **T4 GPU** $\rightarrow$ Bấm **Save**.
3. Kiểm tra GPU bằng lệnh:

   ```python
   !nvidia-smi
   ```

---

## 2. KHÁM PHÁ & TIỀN XỬ LÝ DỮ LIỆU - TUẦN 1 (GIAI ĐOẠN 1)

### 2.1. Tải và giải nén Dataset trực tiếp trên Colab

Tạo ô đầu tiên trong Notebook `1_EDA.ipynb`:

```python
# 1. Cài đặt kaggle
!pip install -q kaggle

# 2. Upload file kaggle.json đã tải từ máy tính
from google.colab import files
files.upload()

# 3. Chuyển token vào thư mục cấu hình
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# 4. Tải dataset Casting Defect (~830MB)
!kaggle datasets download -d ravirajsinh45/real-life-industrial-dataset-of-casting-product

# 5. Giải nén vào thư mục data
!unzip -q real-life-industrial-dataset-of-casting-product.zip -d data/
print("Hoàn tất tải và giải nén dữ liệu!")
```

### 2.2. Khám phá dữ liệu (EDA)

- **Kiểm tra nhãn dữ liệu:**
  - Lớp 0: `ok_front` (sản phẩm đạt tiêu chuẩn).
  - Lớp 1: `def_front` (sản phẩm lỗi bề mặt: nứt, rỗ khí, biến dạng mép đúc).
- **Kiểm tra độ mất cân bằng (Class Imbalance):**
  - Đếm tổng số ảnh mỗi lớp.
  - Vẽ biểu đồ cột (Bar chart) hoặc biểu đồ tròn (Pie chart) tỷ lệ đạt/lỗi.
- **Trực quan hóa mẫu ảnh:**
  - Vẽ lưới ảnh ngẫu nhiên $2 \times 5$ (5 ảnh bình thường và 5 ảnh khuyết tật).
  - Quan sát trực tiếp đặc điểm dị tật của sản phẩm đúc kim loại.

### 2.3. Phân chia tập dữ liệu (Data Splitting)

- Tỷ lệ chuẩn: **70% Train / 15% Validation / 15% Test**.
- Sử dụng phương pháp **Stratified Split** để đảm bảo tỷ lệ lỗi/đạt ở cả 3 tập là đồng đều.

### 2.4. Xây dựng Data Augmentation
>
> ⚠️ **LƯU Ý CỰC KỲ QUAN TRỌNG:**  
> **Chỉ áp dụng Data Augmentation trên tập Train.**  
> Tập Validation và Test tuyệt đối **KHÔNG** làm biến dạng ảnh, chỉ thực hiện Resize (224x224) và Chuẩn hóa (Normalize pixel về `[0, 1]` hoặc `[-1, 1]`). Nếu augment nhầm trên val/test sẽ dẫn đến rò rỉ dữ liệu (Data Leakage), tạo ra điểm số cao "ảo".

**Các phép biến đổi phù hợp cho chi tiết cơ khí:**

- `RandomRotation(factor=0.08)`: Xoay nhẹ ($\pm 15^\circ$)
- `RandomFlip(mode="horizontal_and_vertical")`: Lật ngang và lật dọc
- `RandomContrast(factor=0.1)`: Điều chỉnh tương phản mô phỏng độ sáng phân xưởng
- `RandomZoom(height_factor=(-0.1, 0.1))`: Thu phóng nhẹ

---

## 3. XÂY DỰNG & HUẤN LUYỆN MÔ HÌNH - TUẦN 2 (GIAI ĐOẠN 2)

### 3.1. Baseline CNN (`2_Baseline_CNN.ipynb`) — *15 điểm*

- **Mục đích:** Xây dựng một mô hình CNN thuần túy từ đầu để làm chuẩn so sánh, hiểu rõ cơ chế feature extraction và phát hiện overfitting.
- **Kiến trúc đề xuất:**

  ```python
  from tensorflow.keras import layers, models

  model = models.Sequential([
      layers.Rescaling(1./255, input_shape=(224, 224, 3)),
      
      layers.Conv2D(32, (3, 3), activation='relu'),
      layers.MaxPooling2D(2, 2),
      
      layers.Conv2D(64, (3, 3), activation='relu'),
      layers.MaxPooling2D(2, 2),
      
      layers.Conv2D(128, (3, 3), activation='relu'),
      layers.MaxPooling2D(2, 2),
      
      layers.Flatten(),
      layers.Dense(128, activation='relu'),
      layers.Dropout(0.5), # Ngăn chặn overfitting
      layers.Dense(1, activation='sigmoid') # Phân loại nhị phân
  ])
  ```

- **Huấn luyện:**
  - Optimizer: `Adam(learning_rate=0.001)`
  - Loss: `binary_crossentropy`
  - Metrics: `accuracy`, `Recall`, `Precision`
  - Số Epoch: 20 – 25
- **Vẽ Learning Curves:**
  - Đồ thị Loss (Train vs Val) theo epoch.
  - Đồ thị Accuracy (Train vs Val) theo epoch.
  - **Phân tích:** Chỉ ra điểm mô hình bắt đầu bị Overfitting (khi Val Loss ngừng giảm và quay đầu tăng).

---

### 3.2. Transfer Learning chuẩn 3 Phase (`3_Transfer_Learning.ipynb`) — *25 điểm + 25 điểm Metrics*

Thử nghiệm trên 3 mô hình tiêu biểu:

1. **VGG16:** Cấu trúc truyền thống, trọng số lớn.
2. **ResNet50:** Skip connection giải quyết vấn đề triệt tiêu đạo hàm (vanishing gradient).
3. **EfficientNetB0:** Cân bằng hoàn hảo giữa tham số, độ chính xác và tốc độ.

Mỗi mô hình đều phải trải qua **đúng 3 Phase**:

#### Phase 1: Feature Extraction (Freeze Base Model)

- Load pretrained weights từ ImageNet, bỏ tầng phân loại gốc (`include_top=False`).
- Đóng băng toàn bộ base model: `base_model.trainable = False`.
- Thêm classification head mới: `GlobalAveragePooling2D → Dense(256, relu) → Dropout(0.4) → Dense(1, sigmoid)`.
- Huấn luyện 10 epochs với Learning Rate: $1 \times 10^{-3}$.

#### Phase 2: Fine-tune Top Layers (Mở một số tầng cuối)

- Mở đóng băng một số khối tích chập ở tầng cao nhất của base model (ví dụ: mở 20-30 layers cuối).
- Giảm Learning Rate xuống thấp: $1 \times 10^{-4}$ để không làm xáo trộn các đặc trưng đã học.
- Huấn luyện thêm 10 epochs. Theo dõi sát sao chỉ số **Validation Recall**.

#### Phase 3: Full Fine-tune (Mở toàn bộ)

- Mở toàn bộ mô hình: `base_model.trainable = True`.
- Huấn luyện tiếp 5-10 epochs với Learning Rate siêu nhỏ: $1 \times 10^{-5}$.
- Lưu lại mô hình có kết quả tốt nhất (`ModelCheckpoint`).

#### Đánh giá trên tập Test độc lập

- Xuất ma trận nhầm lẫn (**Confusion Matrix**).
- Thống kê các chỉ số: **Accuracy** (Yêu cầu $\ge 90\%$), **Recall** (Yêu cầu $\ge 95\%$), **Precision**, **F1-Score**.
- Lập bảng tổng hợp so sánh giữa Baseline CNN, VGG16, ResNet50 và EfficientNetB0.

---

## 4. PHÂN TÍCH CHUYÊN SÂU: GRAD-CAM & BENCHMARK - TUẦN 3 (GIAI ĐOẠN 3)

### 4.1. Giải thích mô hình bằng Grad-CAM (`4_GradCAM.ipynb`) — *20 điểm*

- **Nguyên lý:** Sử dụng gradient của class score tương ứng với feature map của tầng Convolution cuối cùng để tạo bản đồ nhiệt (Heatmap), cho biết vùng nào trên ảnh kích hoạt quyết định của mô hình.
- **Thực hiện:**
  - Chọn mô hình tốt nhất từ Tuần 2.
  - Chọn tầng Conv cuối (ví dụ tầng `top_conv` trong EfficientNet hoặc `conv5_block3_out` trong ResNet50).
  - Tạo Heatmap $\rightarrow$ Chuẩn hóa về dải màu Jet $\rightarrow$ Chồng lớp (Overlay) lên ảnh gốc.
- **Yêu cầu báo cáo:**
  - Chạy và hiển thị trên **ít nhất 10 ảnh mẫu** (bao gồm cả ảnh đạt `ok` và ảnh lỗi `defect`).
  - **Phân tích bằng lời:** Mô hình có thực sự soi đúng các vết nứt, vết lõm cơ khí không? Hay bị phân tâm bởi bóng sáng hoặc viền ngoài?

### 4.2. Phân tích tốc độ xử lý (Inference Speed Analysis) (`5_Inference_Speed.ipynb`) — *15 điểm*

- **Đo thời gian trễ (Single Image Latency):**
  - Chạy dự đoán từng ảnh đơn lẻ 100 lần, tính thời gian trung bình (ms/ảnh) trên cả GPU và CPU.
- **Đo thông lượng (Batch Throughput):**
  - Đánh giá tốc độ khi nạp theo batch: Batch Size 16, 32, 64.
  - Tính chỉ số FPS: $\text{FPS} = \frac{\text{Số lượng ảnh}}{\text{Thời gian xử lý (giây)}}$.
- **Đánh giá nghiệp vụ:**
  - Đối chiếu với tốc độ băng chuyền sản xuất thực tế (ví dụ: 60 sản phẩm/phút = 1 ảnh/giây). Mô hình có đủ tiêu chuẩn triển khai thời gian thực (Real-time) không?

### 4.3. Vẽ Precision-Recall Curve & Tối ưu hóa Ngưỡng (Threshold Tuning)

- Trong bài toán kiểm soát chất lượng ngoại quan, việc **để lọt một sản phẩm lỗi (False Negative)** gây thiệt hại uy tín và chi phí đền bù rất lớn so với việc **báo động nhầm một sản phẩm đạt (False Positive)**.
- Vẽ đường cong **Precision-Recall Curve**.
- Thử nghiệm các giá trị ngưỡng phân loại: $Threshold \in [0.3, 0.4, 0.5, 0.6]$.
- Tìm ra điểm cân bằng tối ưu (**Sweet Spot**) giúp đưa **Recall vượt trên 95%** mà không làm suy giảm quá nhiều Precision.

---

## 5. ỨNG DỤNG DEMO, BÁO CÁO & THUYẾT TRÌNH - TUẦN 4 (GIAI ĐOẠN 4)

### 5.1. Xây dựng Web App tương tác (`app.py`) — *Lấy trọn +5 đến +10 Điểm Bonus*

Viết ứng dụng bằng **Streamlit** cực kỳ đơn giản và chuyên nghiệp:

- Giao diện kéo-thả tải ảnh chi tiết đúc kim loại.
- Bấm nút **Kiểm tra ngoại quan**:
  - Trả về nhãn: **ĐẠT (OK)** màu xanh lá hoặc **LỖI (DEFECT)** màu đỏ nổi bật.
  - Hiển thị thanh đo độ tin cậy (% Confidence).
  - Hiển thị bản đồ nhiệt **Grad-CAM** làm nổi bật vị trí khuyết tật trên phôi đúc.

### 5.2. Soạn thảo Báo cáo PDF (Tối đa 15 trang)

Báo cáo khoa học gồm 6 phần chuẩn chỉnh:

1. **Giới thiệu bài toán & Mục tiêu:** Bối cảnh dây chuyền sản xuất, hạn chế của QC thủ công.
2. **Dữ liệu & Tiền xử lý:** Đặc điểm bộ dữ liệu Casting Defect, giải pháp chống rò rỉ dữ liệu, pipeline Augmentation.
3. **Phương pháp Tiếp cận:** Kiến trúc Baseline CNN, quy trình Transfer Learning 3-Phase.
4. **Kết quả Thực nghiệm:** Bảng tổng hợp so sánh các mô hình, biểu đồ Learning Curves, ma trận Confusion Matrix.
5. **Phân tích Chuyên sâu & Nghiệp vụ:** Phân tích trực quan Grad-CAM, tốc độ suy luận (FPS), lựa chọn ngưỡng Sweet Spot trên PR Curve.
6. **Kết luận & Đề xuất Mở rộng:** Đánh giá tính khả thi khi đóng gói sang TFLite/ONNX đưa lên vi xử lý nhúng (Edge AI).

### 5.3. Thiết kế Slide thuyết trình (Tối đa 12 trang, 10 phút)

- **Slide 1:** Trang bìa (Tiêu đề dự án, họ tên tác giả, giảng viên hướng dẫn).
- **Slide 2:** Bối cảnh kinh doanh & Vấn đề cần giải quyết.
- **Slide 3:** Dataset Casting Defect & Pipeline tiền xử lý dữ liệu.
- **Slide 4:** Baseline CNN và bài toán Overfitting.
- **Slide 5:** Chiến lược Transfer Learning 3 Phase.
- **Slide 6:** Bảng kết quả so sánh (VGG16 vs ResNet50 vs EfficientNet).
- **Slide 7-8:** Điểm nhấn Explainable AI: Trực quan hóa Grad-CAM (Hình ảnh minh họa vị trí lỗi).
- **Slide 9:** Đánh giá tốc độ suy luận (Latency & Throughput) trong nhà máy.
- **Slide 10:** Video/Ảnh chụp Web App tương tác (Bonus Feature).
- **Slide 11:** Kết luận & Đóng góp của mô hình cho quy trình QC.
- **Slide 12:** Lời cảm ơn & Phiên hỏi đáp (Q&A).

---

## 6. CHECKLIST ĐÁNH GIÁ & TIÊU CHÍ CHẤM ĐIỂM (RUBRIC)

| Tiêu chí Rubric | Điểm tối đa | Tiêu chuẩn đạt điểm tối đa |
| --- | :---: | --- |
| **Baseline CNN + Learning Curves** | 15 | Tự dựng CNN 3-5 lớp Conv, có biểu đồ Train/Val Loss & Acc, phân tích rõ hiện tượng overfitting. |
| **Transfer Learning đúng 3 Phase** | 25 | Thực hiện tuần tự Phase 1 (Freeze) $\rightarrow$ Phase 2 (Unfreeze top) $\rightarrow$ Phase 3 (Full fine-tune), điều chỉnh Learning rate chuẩn xác. |
| **Metrics: Accuracy ≥ 90%, Recall ≥ 95%** | 25 | Đo đạc trên **Test set độc lập**, có Confusion Matrix chi tiết, ưu tiên Recall không bỏ sót phôi lỗi. |
| **Grad-CAM Visualization & Phân tích** | 20 | Trực quan hóa Heatmap trên $\ge 10$ ảnh (cả đạt và lỗi), có phân tích ngữ nghĩa xem mô hình nhìn đúng khuyết tật hay không. |
| **Inference Speed Analysis** | 15 | Đo đạc Latency (ms/ảnh) và Throughput (FPS theo batch 16/32/64), đối chiếu tính khả thi thực tế. |
| **ĐIỂM CHÍNH THỨC** | **100** | Hoàn thiện đầy đủ báo cáo PDF $\le 15$ trang, slide $\le 12$ trang, notebook chạy thông suốt (Restart & Run All). |
| **ĐIỂM THƯỞNG (BONUS)** | **+5 đến +10** | Web App demo tương tác trực tiếp (Streamlit/Gradio), hoặc tối ưu hóa mô hình bằng TensorFlow Lite / ONNX. |

---


================================================================================
# PHẦN 5: NHẬN XÉT, PHẢN BIỆN CHUYÊN GIA & TỐI ƯU HÓA KIẾN TRÚC
> **Nguồn tài liệu gốc:** `Nhanxet.md`
================================================================================

# ĐÁNH GIÁ VÀ PHẢN BIỆN HỆ THỐNG: BĂNG CHUYỀN KIỂM ĐỊNH SẢN PHẨM ỨNG DỤNG AI

> **Chuyên gia thẩm định:** Principal AI Systems Architect & Industrial Automation Specialist  
> **Dự án mục tiêu:** Project 13 — Kiểm soát Chất lượng Sản phẩm bằng Ảnh (Visual QC)  
> **Đối tượng đánh giá:** Mô hình nguyên mẫu băng chuyền mini để bàn (Tabletop Automated Vision Inspection System)  
> **Trạng thái tài liệu:** Báo cáo phản biện kỹ thuật độc lập (Technical Feasibility Audit)

---

## 1. Tổng quan & Ma trận Khả thi Kỹ thuật (Executive Summary & Feasibility Matrix)

### 1.1. Tóm tắt điều hành (Executive Summary)
Ý tưởng chế tạo mô hình băng chuyền để bàn tích hợp thị giác máy tính là một hướng đi **đột phá và trực quan**, có tiềm năng biến một đồ án lý thuyết thuần túy trên Google Colab thành một giải pháp cơ điện tử hoàn chỉnh có tính thuyết phục cao trong mắt hội đồng chấm điểm.

Tuy nhiên, từ góc nhìn của một kỹ sư trưởng tự động hóa công nghiệp (Principal Automation Engineer), hệ thống đề xuất hiện tại đang mang tư duy của một **"dự án chế tác IoT sinh viên"** hơn là một **"hệ thống kiểm định công nghiệp chuẩn hóa"**. Điểm yếu cốt tử nằm ở sự mất cân bằng giữa cơ cấu cơ khí, độ trễ suy luận AI (Inference Latency), điều kiện quang học (Lighting & Optics), và đặc biệt là cơ chế dừng chuyền thủ công (Manual Removal Anti-pattern).

### 1.2. Ma trận khả thi kỹ thuật (Engineering Feasibility Matrix)

| Phân hệ (Subsystem) | Mức độ khả thi | Rủi ro kỹ thuật | Đánh giá tổng quan | Điểm thắt cổ chai (Bottleneck) |
| :--- | :---: | :---: | :--- | :--- |
| **(a) Cơ khí & Băng tải** *(Mechanical & Conveyance)* | **Cao (8/10)** | Trung bình | Băng tải mini dễ chế tạo từ nhôm định hình và động cơ giảm tốc DC / Stepper. | Rung lắc băng tải (Vibration), trượt phôi, căng dây đai không đều làm rung khung hình camera. |
| **(b) Thu nhận ảnh & Quang học** *(Optics & Lighting)* | **Thấp (4/10)** | **Rất cao** | Đa số dự án học viên thất bại ở bước này do phụ thuộc vào ánh sáng môi trường phòng lab. | Hiện tượng đổ bóng (Shadows), lóa sáng (Specular glare), mờ do chuyển động (Motion blur). |
| **(c) Pipeline Mô hình AI** *(Edge Inference)* | **Trung bình (6/10)** | Cao | Dễ huấn luyện trên máy tính nhưng khó tối ưu độ trễ thực thi thời gian thực trên Edge. | Trễ suy luận (Latency) không khớp với vận tốc băng chuyền; trễ truyền thông I/O (UART/Serial). |
| **(d) Điều khiển & Cơ cấu chấp hành** *(Actuation & Logic)* | **Cao (7/10)** | Thấp | Dùng vi điều khiển (Arduino/ESP32) đọc cảm biến tiệm cận và bật tắt relay/LED. | Cơ chế dừng băng tải cưỡng bức làm gián đoạn chuỗi cung ứng (OEE sụt giảm nghiêm trọng). |

---

## 2. Nhận xét Khen / Chê Chi tiết (In-Depth Technical Evaluation: Pros & Cons)

### 2.1. Điểm sáng kỹ thuật (Engineering Merits & Pros)

1. **Khép kín vòng lặp điều khiển (Closed-loop Cyber-Physical System):**
   - Không dừng lại ở việc dự đoán tĩnh trên tệp ảnh lưu sẵn, hệ thống kết nối trực tiếp từ thế giới thực (vật thể đặt lên băng chuyền) $\rightarrow$ thu nhận tín hiệu $\rightarrow$ suy luận trí tuệ nhân tạo $\rightarrow$ tác động vật lý ngược lại (bật đèn báo, điều khiển động cơ). Đây là nền tảng cốt lõi của công nghiệp 4.0 (Smart Factory).
2. **Khả năng minh họa trực quan xuất sắc (High Pedagogical & Demonstration Value):**
   - Khi báo cáo đồ án, một mô hình vật lý hoạt động ngay trước mắt hội đồng có sức nặng gấp 10 lần những slide biểu đồ tĩnh. Mô hình này chứng minh sinh viên hiểu cách phần mềm giao tiếp với phần cứng ngoại vi.
3. **Cơ chế kích hoạt thông minh (Event-Driven Triggering):**
   - Sử dụng cảm biến để khởi động băng chuyền khi có sản phẩm đặt vào là một thiết kế tiết kiệm năng lượng hợp lý (Energy-efficient standby mode), tránh việc motor phải chạy không tải liên tục gây nóng động cơ và mài mòn cơ khí.

---

### 2.2. Điểm yếu chí tử & cạm bẫy kỹ thuật (Critical Engineering Pitfalls & Cons)

#### A. Nghịch lý dừng chuyền thủ công (The "Manual Removal" Anti-Pattern)
* **Thực trạng đề xuất:** Khi phát hiện lỗi $\rightarrow$ Bật LED đỏ $\rightarrow$ Dừng động cơ băng tải $\rightarrow$ Chờ người lấy sản phẩm lỗi ra.
* **Phản biện công nghiệp:** Đây là **điểm trừ lớn nhất về tư duy tự động hóa**. Trong thực tế sản xuất, chỉ số hiệu suất thiết bị tổng thể (OEE - Overall Equipment Effectiveness) là sống còn. 
  - Việc dừng đột ngột cả dây chuyền để chờ một thao tác thủ công làm triệt tiêu hoàn toàn ý nghĩa của "tự động hóa".
  - Động cơ DC/Stepper khi bị ngắt/bật liên tục sẽ sinh nhiệt lớn, dòng khởi động vọt đỉnh (Inrush current) gây sụt áp trên vi điều khiển, và gây rung giật làm xô lệch các sản phẩm khác đang nằm trên băng tải.

#### B. Cân đối quỹ thời gian suy luận (Latency Budget & Motion Dynamics)
Giả sử thông số vật lý của mô hình để bàn:
- Vận tốc băng tải: $v = 10 \text{ cm/s} = 0.1 \text{ m/s}$.
- Khoảng cách từ cảm biến kích hoạt camera đến điểm dừng/cơ cấu chấp hành: $d = 15 \text{ cm} = 0.15 \text{ m}$.
- Quỹ thời gian tối đa cho toàn bộ chu trình (Total Latency Budget):
  $$t_{\text{budget}} = \frac{d}{v} = \frac{0.15}{0.1} = 1.5 \text{ giây}$$

Chuỗi trễ thực tế ($t_{\text{total}}$) gồm các mắt xích:
$$t_{\text{total}} = t_{\text{sensor}} + t_{\text{camera\_capture}} + t_{\text{preprocess}} + t_{\text{inference}} + t_{\text{comm}} + t_{\text{mechanical\_brake}}$$

Phân tích định lượng từng mắt xích:
- $t_{\text{camera\_capture}}$ (Độ trễ lấy khung hình qua USB/CSI buffer): $\sim 33 - 66 \text{ ms}$ (30 FPS).
- $t_{\text{preprocess}}$ (Resize $224 \times 224$, Normalize): $\sim 10 - 20 \text{ ms}$.
- $t_{\text{inference}}$ (Mạng nơ-ron CNN/ResNet):
  - Chạy trên PC có GPU rời: $\sim 15 - 30 \text{ ms}$ $\rightarrow$ **An toàn**.
  - Chạy trên Raspberry Pi 4 CPU thuần (chưa lượng tử hóa): $\sim 600 - 1.200 \text{ ms}$ $\rightarrow$ **Nguy cơ cao**.
  - Chạy trên ESP32-CAM (mô hình CNN nhỏ): $\sim 800 - 2.000 \text{ ms}$ $\rightarrow$ **Vỡ trận (Sản phẩm trôi qua khỏi vị trí trước khi có kết quả!)**.
- $t_{\text{comm}}$ (Truyền thông nối tiếp UART/Serial Baudrate 115200): $\sim 5 - 10 \text{ ms}$.
- $t_{\text{mechanical\_brake}}$ (Quán tính dừng của động cơ và băng tải trượt): $\sim 100 - 250 \text{ ms}$.

> ⚠️ **Kết luận rủi ro:** Nếu không tính toán trước $t_{\text{budget}}$, sản phẩm lỗi sẽ trôi vượt qua vạch dừng trước khi mô hình AI kịp ra quyết định dừng băng tải!

#### C. Thảm họa quang học để bàn (The Ambient Lighting Trap)
- 90% lỗi nhận diện trong các demo đồ án không đến từ trọng số mô hình AI, mà đến từ **ánh sáng**.
- Trong phòng lab hoặc hội trường bảo vệ: Bóng người đi ngang qua, ánh đèn huỳnh quang nhấp nháy 50Hz, hoặc ánh sáng mặt trời thay đổi từ sáng sang chiều sẽ làm sai lệch toàn bộ ma trận pixel đầu vào.
- **Hiện tượng nhòe chuyển động (Motion Blur):** Nếu băng chuyền chuyển động liên tục ở tốc độ $v = 100 \text{ mm/s}$, mà camera phơi sáng ở mức $t_{\text{exposure}} = 1/30 \text{ s} \approx 33.3 \text{ ms}$, thì độ dịch chuyển của vật thể trong 1 khung hình là:
  $$\Delta x = v \times t_{\text{exposure}} = 100 \times 0.0333 = 3.33 \text{ mm}$$
  Một vết nứt vi mô $0.5 \text{ mm}$ trên sản phẩm sẽ bị kéo nhòe vệt dài $3.33 \text{ mm}$, khiến mô hình hoàn toàn mất khả năng phân loại khuyết tật!

---

## 3. Đánh giá Mức độ Bám sát Đề tài "Project 13" (Project 13 Alignment Audit)

Đối chiếu trực tiếp với yêu cầu học thuật trong tài liệu gốc [project_13.md](file:///e:/Project%20SIC/project_13.md) và kế hoạch [kehoach13.md](file:///e:/Project%20SIC/kehoach13.md):

### 3.1. Phân bổ điểm số theo Rubric chính thức

```
Tổng điểm đồ án: 100 Điểm chính thức + (5 đến 10 Điểm Bonus)
│
├── [15đ] Baseline CNN + Learning Curves
├── [25đ] Transfer Learning 3-Phase (VGG16 / ResNet50 / EfficientNet)
├── [25đ] Đạt Accuracy ≥ 90%, Recall ≥ 95% trên Test Set
├── [20đ] Grad-CAM Visualization & Giải thích vùng quyết định
└── [15đ] Phân tích tốc độ Inference (ms/ảnh, FPS, Real-time Feasibility)
    └── [+5 đến +10đ] BONUS: Dữ liệu thực tế từ DN / Mô hình vật lý chạy thực tế
```

### 3.2. Cảnh báo lệch hướng trọng tâm (Risk of Topic Drift)

> [!CAUTION]
> **CẢNH BÁO LỆCH TRỌNG TÂM:**  
> Toàn bộ phần cứng băng tải, động cơ, cảm biến hồng ngoại, LED và Arduino chỉ nằm trong khung **Điểm Bonus (+5 đến +10 điểm)**.  
> 
> **90 đến 100 điểm cốt lõi** của môn học Trí Tuệ Nhân Tạo được chấm trên **chất lượng mô hình AI**: độ sâu lý thuyết CNN, quy trình Transfer Learning 3-phase chuẩn mực, xử lý hiện tượng mất cân bằng dữ liệu để đạt **Recall $\ge$ 95%**, và kỹ thuật giải thích mô hình **Grad-CAM**.
>
> Nếu đội ngũ sinh viên sa đà vào việc hàn mạch, sửa kẹt dây curoa băng tải, cân chỉnh cơ khí mà bỏ bê việc huấn luyện mô hình, vẽ PR Curve, hay không làm Grad-CAM, nhóm sẽ đối mặt với nguy cơ **"Cơ khí hoàn hảo nhưng rớt môn vì thiếu hàm lượng AI"**.

---

## 4. Đề xuất Cải tiến Hệ thống (Key Architectural & Hardware Enhancements)

Để biến mô hình này thành một hệ thống đẳng cấp công nghiệp (Industrial-Grade Prototype) vừa giật trọn điểm Bonus vừa bảo toàn điểm AI tuyệt đối, đề xuất kiến trúc cải tiến sau:

### 4.1. Kiến trúc phân tầng tối ưu (Tiered Architecture)

Thay vì cố gắng nhồi nhét mô hình AI nặng vào vi điều khiển yếu (ESP32/Arduino), hãy tách rời rạch ròi 2 tầng:

```
[ TẦNG CƠ ĐIỆN TỬ NGOẠI VI ]                [ TẦNG TRÍ TUỆ NHÂN TẠO (EDGE AI) ]
   (Arduino Nano / ESP32)                         (Laptop / PC / Jetson Orin)
┌──────────────────────────┐                   ┌────────────────────────────────┐
│ • Cảm biến tiệm cận hồng │                   │ • Webcam HD / Camera CSI       │
│   ngoại (IR Infeed)      │ ──[UART/USB]────> │ • Buồng quang học kín (Shroud) │
│ • Điều khiển động cơ DC  │   (Baud: 115200)  │ • Model: MobileNetV2/ResNet50  │
│ • Tay gạt gạt hàng lỗi   │ <──[Pass/Fail]─── │ • Pipeline: Preprocess + Infer │
│   (Micro Servo SG90)     │                   │ • Grad-CAM Realtime Dashboard  │
└──────────────────────────┘                   └────────────────────────────────┘
```

### 4.2. Khắc phục dứt điểm 3 lỗi chí tử

#### 1. Thay "Dừng băng tải thủ công" bằng "Cơ cấu gạt tự động" (Servo Diverter)
- **Giải pháp:** Lắp một động cơ servo mini ($SG90$ giá ~30.000 VNĐ) ở cuối băng chuyền làm thanh gạt (flapper arm).
- **Nguyên lý hoạt động:**
  - Sản phẩm Đạt (`Pass`): Băng chuyền tiếp tục chạy thẳng vào thùng thành phẩm.
  - Sản phẩm Lỗi (`Fail`): Băng chuyền **vẫn chạy liên tục**, khi sản phẩm đi qua vị trí servo, cánh tay gạt xoay góc $45^\circ$ gạt rơi sản phẩm sang khay hàng lỗi (Defect Bin), sau đó tự động rút về vị trí cũ trong $300 \text{ ms}$.
- **Lợi ích:** Dây chuyền hoạt động liên tục (Continuous operation), tăng điểm OEE, thể hiện tư duy cơ điện tử xuất sắc.

#### 2. Xây dựng buồng chụp ảnh tiêu chuẩn (Optical Inspection Hood / Shroud)
- **Giải pháp:** Dùng bìa carton formex đen hoặc mica làm một mái vòm/hộp che kín vị trí đặt camera trên băng chuyền (kích thước khoảng $15 \times 15 \times 20 \text{ cm}$).
- **Hệ thống chiếu sáng chủ động (Active Diffuse Lighting):** Dán dải đèn LED trắng $12\text{V}$ (CRI $\ge 80$) chạy viền bên trong hộp che, có lớp màng tán xạ ánh sáng (giấy can mỏng hoặc mica mờ) để triệt tiêu hiện tượng lóa bóng cục bộ.
- **Kết quả:** Ánh sáng đồng nhất $100\%$, độc lập hoàn toàn với môi trường bên ngoài, triệt tiêu tình trạng demo thất bại do bóng người.

#### 3. Chế độ kiểm tra: Dừng chụp hay Chụp khi đang chạy? (Stop-and-Go vs. On-The-Fly)
- Đối với mô hình để bàn sinh viên, khuyên dùng chế độ **"Stop-and-Go thông minh"**:
  1. Sản phẩm chạm cảm biến dưới camera $\rightarrow$ Động cơ hãm dừng mềm trong $0.3 \text{ giây}$.
  2. Camera chụp khung hình tĩnh hoàn hảo (triệt tiêu $100\%$ nhòe chuyển động - Motion blur).
  3. Mô hình AI suy luận ($0.05 \text{ giây}$).
  4. Động cơ chạy tiếp $\rightarrow$ Nếu lỗi, servo gạt phôi.
- Tổng thời gian dừng chỉ $0.35 \text{ giây}$, mắt người nhìn vào thấy mượt mà như một trạm quét tự động (Indexing Station).

---

## 5. Kế hoạch Hành động & Khuyến nghị Triển khai (Actionable Roadmap)

Để đảm bảo đạt điểm tối đa cả phần lý thuyết AI lẫn phần cứng Demo, nhóm cần phân bổ tài nguyên theo chiến lược **"AI First — Hardware Second"** (80/20):

```
TUẦN 1 & 2: HOÀN TẤT 100% PHẦN MỀM AI (Đảm bảo 90 điểm chuẩn)
│  ├── Huấn luyện mô hình chuẩn trên Colab (Dataset: Casting Defect hoặc Thùng hàng DHL)
│  ├── Đảm bảo đạt Accuracy ≥ 90% và Recall ≥ 95%
│  ├── Xuất mô hình sang định dạng tối ưu (TensorFlow Lite hoặc ONNX Runtime)
│  └── Hoàn thành trích xuất Grad-CAM và biểu đồ PR-Curve
│
TUẦN 3: XÂY DỰNG MÔ HÌNH BĂNG CHUYỀN VẬT LÝ (Giật 10 điểm Bonus)
│  ├── Lắp khung băng chuyền mini (Kit nhôm định hình 2020 hoặc mica cắt laser)
│  ├── Lập trình Arduino đọc cảm biến IR, điều khiển Motor driver L298N/L9110 và Servo SG90
│  └── Viết script Python trên máy tính: Đọc webcam -> Dự đoán -> Bắn ký tự ('1': OK, '0': NG) qua cổng COM/Serial
│
TUẦN 4: TÍCH HỢP TOÀN HỆ THỐNG & ĐÓNG GÓI BÁO CÁO
   ├── Cân chỉnh thời gian trễ giữa bước quét ảnh và góc quét của Servo
   ├── Quay video minh chứng hoạt động mượt mà (dự phòng trường hợp đem lên lớp bị lỗi kết nối)
   └── Hoàn thiện Slide và Báo cáo PDF (đưa phần cứng vào mục "Triển khai Thực tế & Hướng Phát triển")
```

---

## 6. Lời Kết Của Kiến Trúc Sư Trưởng

> *"Một kỹ sư giỏi không phải là người cố gắng đưa phần cứng phức tạp nhất vào đồ án, mà là người biết kiểm soát độ trễ, tối ưu hóa sự tương thích giữa phần mềm và cơ cấu chấp hành, và luôn đặt mục tiêu học thuật cốt lõi lên hàng đầu."*

Mô hình băng chuyền kiểm định để bàn của bạn có đầy đủ tiềm năng để trở thành **đồ án xuất sắc nhất khóa** nếu áp dụng đúng cơ chế gạt phôi tự động, buồng chiếu sáng tán xạ độc lập và tách biệt tầng suy luận máy tính với tầng điều khiển vi điều khiển. Hãy bắt tay vào hoàn thiện phần AI cốt lõi trước, sau đó gắn kết vào băng chuyền như một mảnh ghép hoàn thiện bức tranh công nghiệp 4.0!

---


================================================================================
# PHẦN 6: HỆ SINH THÁI CÔNG NGHỆ & DANH MỤC NỀN TẢNG WEB (WEBAPP)
> **Nguồn tài liệu gốc:** `webapp.md`
================================================================================

┌───────────────────────────────────────────────────┐
                  │   CAMERA SMARTPHONE TRÊN BĂNG CHUYỀN CARTON DIY   │
                  │   (Chụp góc nhìn thẳng đứng 1080p @ 30 FPS)       │
                  └─────────────────────────┬─────────────────────────┘
                                            │ DroidCam qua cáp USB
                                            ▼
                  ┌───────────────────────────────────────────────────┐
                  │              OPENCV PYTHON INGESTION              │
                  │   • Bắt khung hình (Resolution 1280x720)          │
                  │   • Cắt vùng quan tâm (ROI 400x400 tâm băng tải)  │
                  └─────────────────────────┬─────────────────────────┘
                                            │
                                            ▼
                  ┌───────────────────────────────────────────────────┐
                  │        EDGE AI INFERENCE (TFLITE INT8)            │
                  │   • Backbone: MobileNetV2 (Input 224x224x3)       │
                  │   • Latency: ~28ms trên CPU Laptop                │
                  │   • Threshold Tuning: tau = 0.35 (Recall >= 95%)  │
                  └────────────────────┬─────────────┬────────────────┘
                                       │             │
                    Nếu ĐẠT (P < 0.35) │             │ Nếu LỖI (P >= 0.35)
                                       ▼             ▼
  ┌──────────────────────────────────────┐     ┌──────────────────────────────────────┐
  │         HÀNH ĐỘNG: ĐẠT (PASS)        │     │         HÀNH ĐỘNG: LỖI (DEFECT)      │
  │ • Viền XANH LÁ trên Web App          │     │ • Viền ĐỎ RỰC nhấp nháy trên Web App │
  │ • Loa Laptop phát tiếng bíp ngắn     │     │ • Tạo bản đồ nhiệt Grad-CAM chỗ rách │
  │ • Bưu kiện trôi thẳng về đích        │     │ • Loa Laptop kêu cảnh báo khẩn cấp   │
  │ • Cập nhật bộ đếm thành phẩm (+1)    │     │ • Người vận hành gạt lẫy phế phẩm    │
  └──────────────────────────────────────┘     └──────────────────┬───────────────────┘
                                                                  │
                                                                  │ Kích hoạt Webhook (Payload JSON)
                                                                  ▼
                                               ┌──────────────────────────────────────┐
                                               │   WORKFLOW AUTOMATION (N8N / FASTAPI)│
                                               │                                      │
                                               │  ├─> [TELEGRAM BOT]:                 │
                                               │  │   Bắn ảnh Grad-CAM + Thông báo    │
                                               │  │   về điện thoại của Giám đốc QA   │
                                               │  │                                   │
                                               │  └─> [GOOGLE SHEETS API]:            │
                                               │      Ghi nhật ký ca trực (Timestamp, │
                                               │      Loại lỗi, Điểm tin cậy, Ảnh URL)│
                                               └──────────────────────────────────────┘

Pha 1: Video Ingestion & Thiết lập Môi trường (Tuần 1)
Thiết lập luồng truyền video từ điện thoại vào máy tính qua DroidCam Client (kết nối USB cáp sạc, độ trễ $\le 30\text{ ms}$, tốc độ $30\text{ fps}$).
Dựng buồng che quang học bằng bìa carton và đèn học để bàn nhằm triệt tiêu bóng đổ.
Cắt dán mô hình băng tải carton quay tay mini (theo ytuong.md).

Pha 2: Huấn luyện Mô hình & Lượng tử hóa TFLite (Tuần 2)
Khai thác bộ dữ liệu thùng hàng từ file DHL.qmd
 trên Google Colab GPU T4.
Huấn luyện mạng MobileNetV2 qua 3 phase Transfer Learning; tối ưu hóa ngưỡng phân loại $\tau = 0.35$ để đạt chỉ số sống còn: Recall $\ge 95%$ và Accuracy $\ge 90%$.
Lượng tử hóa sang mô hình nhẹ TFLite INT8 (kích thước $< 5\text{ MB}$, suy luận trên CPU laptop chỉ mất $25 - 30\text{ ms}$).

Pha 3: Xây dựng Web App Giám sát Trung tâm (Tuần 3)
Lập trình giao diện Dashboard bằng Streamlit (app.py):
Khung 1: Video stream trực tiếp với viền Xanh (Đạt) / Đỏ (Lỗi).
Khung 2: Bản đồ nhiệt Grad-CAM hiển thị trực tiếp bên cạnh ảnh gốc khi phát hiện lỗi.
Khung 3: Thống kê số lượng kiện đã quét, tỷ lệ lỗi (Defect Rate %) và thời gian suy luận (Inference Latency tính bằng ms).

Pha 4: Tích hợp Tự động hóa, Cảnh báo & Triển khai Công khai (Tuần 4)
Thiết lập bot Telegram nhận tin nhắn cảnh báo tức thời kèm ảnh chụp khuyết tật mỗi khi có thùng hàng bị lỗi.
Mở cổng kết nối bằng Ngrok để tạo link web HTTPS công khai.
Chạy thử nghiệm thực tế 100 lần quét, ghi lại video demo 2 phút toàn cảnh hệ thống vận hành mượt mà phục vụ buổi thuyết trình bảo vệ.

# DANH MỤC CÔNG CỤ, NỀN TẢNG WEB & HỆ SINH THÁI TỰ ĐỘNG HÓA AI (WEBAPP.MD)

### Dự án: Hệ Thống Băng Chuyền Kiểm Định Chất Lượng Bưu Kiện Thông Minh (Visual QC — Project 13)

> **Kiến trúc sư trưởng:** World-Class AI Automation Architect & Systems Engineer  
> **Mục tiêu tệp:** Định chuẩn toàn bộ kho công cụ số (Digital Tool Stack), nền tảng web (Web Platforms), framework API và hệ thống tự động hóa luồng làm việc (Workflow Automation) phục vụ triển khai Web App giám sát và vận hành mô hình kiểm định chất lượng bưu kiện.

---

## 1. BẢNG TỔNG HỢP HỆ SINH THÁI CÔNG CỤ (AUTOMATION & WEB PLATFORMS)

| STT | Tên Công Cụ / Nền Tảng | Phân Nhóm Chức Năng | Vai Trò & Vị Trí Trong Dự Án | Luồng Tích Hợp (Trigger / Action Flow) | Liên Kết Chính Thức |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Streamlit** | *Web Application & Realtime Dashboard* | Xây dựng giao diện web giám sát kiểm định trực tiếp, hiển thị video stream, kết quả Pass/Fail và bản đồ nhiệt Grad-CAM | **Action:** Nhận luồng video từ webcam $\rightarrow$ Vẽ khung viền xanh/đỏ $\rightarrow$ Cập nhật biểu đồ thống kê sản phẩm theo thời gian thực | [streamlit.io](https://streamlit.io) |
| **2** | **Gradio** | *Interactive AI Demo & Prototyping* | Tạo web UI nhanh để test trực tiếp mô hình AI trên trình duyệt, cho phép upload ảnh hoặc bật camera live | **Trigger:** Người dùng/giám khảo chụp ảnh thùng hàng $\rightarrow$ **Action:** Trả về kết quả xác suất lỗi và ảnh Grad-CAM sau $30\text{ ms}$ | [gradio.app](https://www.gradio.app) |
| **3** | **FastAPI** | *High-Performance Async Backend API* | Xây dựng API RESTful/WebSocket xử lý suy luận mô hình AI tốc độ cao, tách rời giao diện người dùng và lõi xử lý | **Trigger:** Client gửi frame ảnh dạng base64/binary $\rightarrow$ **Action:** Trả về JSON `{status: "DEFECT", confidence: 0.96, gradcam_url: "..."}` | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| **4** | **DroidCam / Iriun** | *Mobile-to-PC Video Bridge* | Biến camera điện thoại thông minh thành webcam Full HD $1080\text{p}$ cắm qua USB vào laptop với chi phí $0$ VNĐ | **Hardware Bridge:** Cảm biến camera điện thoại $\rightarrow$ Cáp USB $\rightarrow$ Virtual Video Device (`/dev/video0` hoặc Camera Index 1 trên OpenCV) | [dev47apps.com](https://www.dev47apps.com) |
| **5** | **n8n (Self-Hosted / Cloud)** | *Workflow Automation Engine* | Nền tảng tự động hóa luồng làm việc mã nguồn mở, kết nối sự kiện phát hiện thùng lỗi với các kênh thông báo | **Trigger:** Webhook nhận payload lỗi từ Python $\rightarrow$ **Action:** Gửi thông báo Telegram + Ghi nhật ký vào Google Sheets | [n8n.io](https://n8n.io) |
| **6** | **Telegram Bot API** | *Instant Alerting & Incident Escalation* | Kênh gửi cảnh báo khẩn cấp tức thời có kèm hình ảnh thùng hàng bị lỗi và bản đồ nhiệt Grad-CAM tới điện thoại quản lý | **Trigger:** Lệnh gạt thùng lỗi được kích hoạt $\rightarrow$ **Action:** Bot gửi tin nhắn Telegram: *"Cảnh báo: Phát hiện thùng móp lúc 14:02:15!"* kèm ảnh bằng chứng | [core.telegram.org/bots](https://core.telegram.org/bots) |
| **7** | **Google Sheets API / Airtable** | *Cloud Audit Logging & Telemetry* | Cơ sở dữ liệu đám mây ghi lại toàn bộ lịch sử kiểm định (Mã bưu kiện, Thời gian, Trạng thái Pass/Fail, Tỷ lệ tin cậy, Độ trễ) | **Trigger:** Mỗi chu kỳ quét hoàn tất $\rightarrow$ **Action:** Thêm 1 dòng mới vào bảng tính để vẽ dashboard KPI/OEE báo cáo cuối kỳ | [workspace.google.com](https://workspace.google.com/products/sheets) |
| **8** | **Roboflow** | *Dataset Ops & Auto-Augmentation* | Quản lý bộ dữ liệu thùng hàng, gán nhãn khuyết tật (móp góc, rách bìa, thủng lỗ), xuất dữ liệu augmentation chuẩn | **Input:** Ảnh chụp từ điện thoại $\rightarrow$ **Action:** Tự động xoay, lật, đổi độ sáng $\rightarrow$ Xuất dataset định dạng TensorFlow/PyTorch | [roboflow.com](https://roboflow.com) |
| **9** | **Google Colab** | *Cloud GPU Model Training* | Huấn luyện mô hình Transfer Learning (MobileNetV2 / ResNet50) trên GPU T4 miễn phí mà không làm nóng laptop cá nhân | **Development:** Nạp dữ liệu từ Kaggle $\rightarrow$ Train 3-Phase $\rightarrow$ Xuất file mô hình tối ưu `package_model.tflite` | [colab.research.google.com](https://colab.research.google.com) |
| **10** | **Hugging Face Spaces** | *Cloud Model Hosting & Public Demo* | Đưa ứng dụng web demo kiểm định chất lượng lên đám mây hoàn toàn miễn phí để chia sẻ link cho giảng viên chấm điểm | **Deployment:** Đẩy code Streamlit/Gradio lên Git $\rightarrow$ Hugging Face tự động build container và cấp domain online công khai | [huggingface.co/spaces](https://huggingface.co/spaces) |
| **11** | **TFLite Runtime / ONNX** | *Edge Embedded Inference Engine* | Bộ thư viện suy luận tối ưu cho CPU laptop, giảm dung lượng bộ nhớ và tăng tốc độ suy luận từ $120\text{ ms} \rightarrow 25\text{ ms}$ | **Inference:** Nhận ảnh $224 \times 224$ $\rightarrow$ Tính toán ma trận lượng tử hóa INT8 $\rightarrow$ Xuất xác suất nhãn | [tensorflow.org/lite](https://www.tensorflow.org/lite) |
| **12** | **Ngrok / LocalTunnel** | *Secure Reverse Proxy & Tunneling* | Mở cổng an toàn (secure tunnel) từ localhost laptop ra Internet trong $5\text{ giây}$ để hội đồng truy cập live từ điện thoại cá nhân | **CLI Command:** `ngrok http 8501` $\rightarrow$ Cung cấp link HTTPS công khai trỏ trực tiếp về Web App Streamlit trên máy bạn | [ngrok.com](https://ngrok.com) |

---

## 2. CHI TIẾT CẤU HÌNH & TÍCH HỢP TỪNG PHÂN HỆ

### 2.1. Phân hệ Giao Diện Người Dùng (Web Dashboard — Streamlit)

- **Mục đích:** Tạo ra một giao diện dashboard điều hành trung tâm (Central Monitoring Dashboard) hiện đại, trực quan, không cần viết code HTML/CSS/JavaScript phức tạp.
- **Tính năng chính:**
  - **Live Video Stream:** Khung hình camera hiển thị trực tiếp với FPS thực tế.
  - **Trạng thái thời gian thực:** Banner màu XANH LÁ (PASS) hoặc ĐỎ (REJECT - LỖI) nhấp nháy theo kết quả suy luận.
  - **Bản đồ nhiệt Grad-CAM song song:** Đặt cạnh ảnh gốc để chứng minh mô hình AI nhận diện đúng khuyết tật.
  - **Thống kê sản lượng:** Bộ đếm tổng số kiện hàng đã quét, số kiện đạt, số kiện lỗi và tỷ lệ lỗi (Defect Rate %).
- **Mã nguồn khởi động mẫu (`app.py`):**

  ```python
  import streamlit as st
  import cv2
  import numpy as np
  import tensorflow as tf

  st.set_page_config(page_title="DHL Smart QC Dashboard", layout="wide")
  st.title("📦 HỆ THỐNG KIỂM ĐỊNH TỰ ĐỘNG THÙNG HÀNG — PROJECT 13")

  col1, col2 = st.columns([2, 1])
  with col1:
      st.subheader("Luồng Camera Trực Tiếp (Live Inspection)")
      image_placeholder = st.empty()
  with col2:
      st.subheader("Trạng Thái Kiểm Định")
      status_placeholder = st.empty()
      metrics_placeholder = st.empty()
  ```

---

### 2.2. Phân hệ Tự Động Hóa Quy Trình (Automation Workflow — n8n & Telegram)

- **Mục đích:** Đóng vai trò cầu nối tự động hóa (Automation Bridge). Ngay khi mô hình AI phát hiện thùng hàng bị rách hoặc móp, một sự kiện (Event Payload) sẽ được bắn ra để kích hoạt các hành động tiếp theo mà không cần con người can thiệp.
- **Sơ đồ luồng (Workflow Nodes in n8n):**

  ```
  [Webhook Node (POST /defect-detected)]
                 │
                 ├─> [Telegram Node: Bắn ảnh Grad-CAM + Thông báo về Group Zalo/Telegram QA]
                 │
                 └─> [Google Sheets Node: Append dòng dữ liệu mới vào bảng báo cáo ca trực]
  ```

- **Payload mẫu gửi từ Python:**

  ```json
  {
    "event": "DEFECT_DETECTED",
    "timestamp": "2026-09-19T18:30:00Z",
    "package_id": "CARTON_BOX_089",
    "defect_type": "Crushed_Corner",
    "confidence": 0.964,
    "recall_target_met": true,
    "image_base64": "data:image/jpeg;base64,..."
  }
  ```

---

### 2.3. Phân hệ Thu Nhận Video Không Tốn Chi Phí (DroidCam Video Pipeline)

- **Cơ chế:**
  1. Cài app **DroidCam** trên điện thoại (Android hoặc iOS).
  2. Cài **DroidCam Client** trên laptop Windows.
  3. Kết nối bằng cáp sạc USB (chọn chế độ truyền file hoặc USB Debugging).
  4. Mở OpenCV trên Python: `cap = cv2.VideoCapture(1)` (hoặc index tương ứng với camera ảo DroidCam).
- **Lợi ích:** Đạt chất lượng quang học Full HD $1080\text{p}$, tốc độ $30\text{ fps}$, khả năng tự động lấy nét (Auto-focus) và cân bằng trắng vượt trội so với các loại webcam giá rẻ dưới 500k.

---

### 2.4. Phân hệ Triển Khai Công Khai Cho Giảng Viên (Public Demo via Ngrok / Hugging Face)

- **Vấn đề thực tế:** Khi bảo vệ đồ án, giảng viên muốn dùng điện thoại cá nhân mở link webapp để trực tiếp theo dõi hoặc tải thử ảnh thùng hàng lên kiểm tra.
- **Giải pháp:**
  - **Cách 1 (Ngrok):** Chạy lệnh `ngrok http 8501` trên Terminal laptop. Ngrok sinh ra một đường dẫn HTTPS công khai tạm thời (ví dụ: `https://dhl-qc-demo.ngrok-free.app`). Giảng viên chỉ cần quét mã QR là truy cập được dashboard đang chạy trên laptop của bạn!
  - **Cách 2 (Hugging Face Spaces):** Đẩy mã nguồn và tệp mô hình `.tflite` lên repo Hugging Face Spaces (miễn phí trọn đời, cấu hình CPU 2 vCPU, RAM 16GB). Giảng viên có thể truy cập 24/7 từ bất cứ đâu.

---

## 3. CHECKLIST SẴN SÀNG TRIỂN KHAI PHẦN MỀM (DEPLOYMENT CHECKLIST)

- [ ] Cài đặt môi trường Python 3.10+ trên máy tính (`pip install streamlit opencv-python tensorflow pillow requests`).
- [ ] Tải và cài đặt thành công DroidCam Client, kết nối điện thoại qua USB hiển thị video mượt mà.
- [ ] Huấn luyện mô hình Transfer Learning trên Google Colab theo file [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd), lưu file trọng số mô hình `package_qc_model.h5`.
- [ ] Chạy file `app.py` Streamlit trên localhost (`http://localhost:8501`).
- [ ] Tạo 1 Telegram Bot miễn phí qua `@BotFather`, lấy `Bot Token` và `Chat ID` để tích hợp gửi cảnh báo thùng hàng lỗi.
- [ ] Cấu hình 1 link Ngrok dự phòng để sẵn sàng chiếu mã QR cho hội đồng giám khảo trải nghiệm trực tiếp trên điện thoại.

---

# 🍎 Fruit Visual QC: Hệ Thống Kiểm Soát Chất Lượng Nông Sản Bằng Thị Giác Máy Tính
### Tự Động Phân Loại Trái Cây Tươi & Phát Hiện Khuyết Tật Hư Hỏng / Thâm Dập Thời Gian Thực

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](http://localhost:8501)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-GPU%20T4-F9AB00?style=flat&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![Status](https://img.shields.io/badge/Status-Completed%20100%25-brightgreen?style=flat)](https://github.com/)

> **Project 13 — Môn học: Trí Tuệ Nhân Tạo (AI & Deep Learning)**  
> Ứng dụng Convolutional Neural Networks (CNN), Quy trình Transfer Learning 3-Phase, Explainable AI (Grad-CAM) và Edge Video Streaming trong bài toán kiểm soát chất lượng nông sản xuất khẩu (*Fruit Quality Control: Fresh vs. Rotten / Defective Produce*).  
>
> 🌐 **Khởi chạy Web Demo 1-Click:** Nhấp đúp vào [`run_demo.bat`](file:///e:/Project%20SIC/run_demo.bat) (hoặc truy cập [http://localhost:8501](http://localhost:8501))  

---

## 📑 Mục Lục
1. [Bối Cảnh & Ý Nghĩa Kinh Tế (Bài Toán Khí Ethylene)](#-bối-cảnh--ý-nghĩa-kinh-tế-bài-toán-khí-ethylene)
2. [Các Điểm Nổi Bật Đã Hoàn Thành 100%](#-các-điểm-nổi-bật-đã-hoàn-thành-100)
3. [Kết Quả Thực Nghiệm Chính Thức (Official Benchmark)](#-kết-quả-thực-nghiệm-chính-thức-official-benchmark)
4. [Explainable AI (Grad-CAM Heatmaps)](#-explainable-ai-grad-cam-heatmaps)
5. [Kiến Trúc Triển Khai & Web Demo Thời Gian Thực](#-kiến-trúc-triển-khai--web-demo-thời-gian-thực)
6. [Cấu Trúc Thư Mục Dự Án](#-cấu-trúc-thư-mục-dự-án)
7. [Hướng Dẫn Cài Đặt & Khởi Chạy Nhanh](#-hướng-dẫn-cài-đặt--khởi-chạy-nhanh)
8. [Tài Liệu Kỹ Thuật Chi Tiết](#-tài-liệu-kỹ-thuật-chi-tiết)

---

## 💡 Bối Cảnh & Ý Nghĩa Kinh Tế (Bài Toán Khí Ethylene)

1. **Khủng hoảng thất thoát sau thu hoạch (Post-harvest Loss 20%–40%):**
   - Khâu phân loại thủ công tại các cơ sở đóng gói (Packhouse) phụ thuộc vào mắt người, dễ mệt mỏi sau 2–3 giờ làm việc, dẫn đến tỷ lệ bỏ sót quả thâm dập lên tới 15%–25%.
2. **Thiệt hại kinh tế bất cân xứng cực đoan (Asymmetric Cost Matrix):**
   - **Báo nhầm quả tươi thành hỏng (False Positive):** Quả tươi bị hạ phẩm cấp hoặc kiểm tra lại tốn ~$0.20 – $0.50/quả.
   - **Bỏ sót quả thối lọt vào container (False Negative):** Quả thối sinh ra lượng lớn **khí Ethylene ($C_2H_4$)** và bào tử nấm mốc (*Penicillium*), kích thích toàn bộ các quả xung quanh chín nẫu và thối rữa trong hành trình vận chuyển đường biển 15–30 ngày. Hậu quả là **hư hỏng cả container trị giá hàng chục nghìn USD** và bị phạt kiểm dịch quốc tế.
   $$\text{Chi phí tổn thất do Bỏ sót (FN)} \approx 100 \times \text{Chi phí Báo nhầm (FP)}$$
   👉 **Tiêu chí sống còn của hệ thống AI là Recall $\ge 95\%$ (thực tế đạt 100.0%) cho lớp sản phẩm lỗi.**
3. **Tính khả thi và trực quan cao:**
   - Trái cây (táo, chuối, cam...) là vật phẩm có sẵn 100% ngoài đời thực. Giảng viên và hội đồng có thể dùng camera điện thoại hoặc webcam soi trực tiếp quả tươi / quả thâm tại chỗ để kiểm tra AI.

---

## ✨ Các Điểm Nổi Bật Đã Hoàn Thành 100%

- [x] **Dữ liệu chuẩn Doanh nghiệp:** Tự động hóa tải và kết hợp 3 bộ dữ liệu Kaggle (>30,000 ảnh) qua [`download_fruit_data.py`](file:///e:/Project%20SIC/download_fruit_data.py); đã phân chia tập Train/Val/Test chặt chẽ trong [`processed_data/`](file:///e:/Project%20SIC/processed_data/).
- [x] **Chuỗi Notebooks thực nghiệm & Master Pipeline toàn diện (0 Lỗi, Full Output):** 
  - Khám phá dữ liệu, kiểm toán phân tầng & Augmentation (`1_Fruit_EDA_Augmentation.ipynb`).
  - Baseline Custom CNN từ đầu & phân tích Learning Curves (`2_Fruit_Baseline_CNN.ipynb`).
  - Huấn luyện 3 mô hình Transfer Learning theo quy trình 3-Phase chuẩn khoa học (`3_Fruit_Transfer_Learning.ipynb`).
  - Bản đồ nhiệt Grad-CAM minh bạch hóa quyết định (`4_Fruit_GradCAM_ExplainableAI.ipynb`).
  - Đo đạc tốc độ suy luận & Tối ưu ngưỡng cắt rủi ro chi phí (`5_Fruit_Inference_Speed_Benchmark.ipynb`).
  - **Master Pipeline hợp nhất trọn vẹn từ A-Z** (`Fruit_Full_Pipeline.ipynb`): Tích hợp liền mạch toàn bộ đường ống xử lý dữ liệu, huấn luyện, giải thích mô hình và đối chuẩn tốc độ.
- [x] **Lưu trữ Model Weights sẵn sàng phục vụ:** Đã huấn luyện và lưu trọn vẹn 3 file trọng số tốt nhất vào thư mục [`models/`](file:///e:/Project%20SIC/models/) (`efficientnetb0_best.keras`, `resnet50_best.keras`, `vgg16_best.keras`).
- [x] **Giao diện Web Streamlit thông minh ([`app.py`](file:///e:/Project%20SIC/app.py)):**
  - Hỗ trợ tải ảnh kiểm định đơn lẻ kèm điều chỉnh ngưỡng nhạy cảm (Confidence Threshold).
  - Tích hợp 3 khung hình đối chiếu Grad-CAM (Ảnh gốc, Heatmap nhiệt, Bản đồ chồng lấp).
  - Tự động ước lượng rủi ro phát tán khí Ethylene và ma trận thiệt hại tài chính.
- [x] **Tích hợp Camera Điện thoại (DroidCam) & Edge Stream HUD ([`edge_stream_inspector.py`](file:///e:/Project%20SIC/edge_stream_inspector.py)):**
  - Tự động chuẩn hóa địa chỉ IP/Port khi đổi mạng Wi-Fi và ghi nhớ lịch sử (`camera_history.json`).
  - Cơ chế chống rớt khung hình (Wi-Fi frame drop tolerance), độ trễ dưới 100ms.
  - Chế độ quét luồng OSD HUD liên tục hiển thị FPS, Bounding Box và còi báo lỗi như băng chuyền công nghiệp.
- [x] **Khởi chạy 1-Click tiện lợi:** Cung cấp script [`run_demo.bat`](file:///e:/Project%20SIC/run_demo.bat) tự động mở trình duyệt và chạy app.

---

## 📊 Kết Quả Thực Nghiệm Chính Thức (Official Benchmark)

Toàn bộ các mô hình đã được huấn luyện đối chuẩn trên phần cứng GPU Google Colab T4 và kiểm định trên tập dữ liệu Test Set độc lập:

### 1. Bảng So Sánh Hiệu Năng 4 Kiến Trúc (Tập Test Độc Lập 4,080 Mẫu)

| Mô hình | Số tham số | Dung lượng | Accuracy | Recall *(Bắt lỗi)* | Precision | F1-Score | Bỏ sót (FN) | Báo nhầm (FP) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Baseline CNN (Tự xây)** | 11.17M | 44.7 MB | 97.45% | 99.61% | 96.03% | 0.9779 | 9 quả | 95 quả |
| **VGG16 (3-Phase)** | 14.85M | 57.2 MB | 99.95% | 99.91% | **100.00%** | 0.9996 | 2 quả | **0 quả** |
| **ResNet50 (3-Phase)** | 24.12M | 91.8 MB | 99.98% | **100.00%** | 99.96% | 0.9998 | **0 quả** | 1 quả |
| **EfficientNetB0 (3-Phase) 🏆** | **4.38M** | **33.1 MB** | **100.00%** | **100.00%** | **100.00%** | **1.0000** | **0 quả** | **0 quả** |

*(Dữ liệu trích xuất từ file kết quả thực tế [`results/transfer_learning_benchmark.csv`](file:///e:/Project%20SIC/results/transfer_learning_benchmark.csv))*

### 2. Biểu Đồ Đối Chuẩn Hiệu Năng

![So Sánh Hiệu Năng Transfer Learning](file:///e:/Project%20SIC/results/transfer_learning_comparison.png)

### 3. Tối Ưu Ngưỡng Nhận Diện (Threshold Tuning & Cost Minimization)

| Ngưỡng (Threshold) | Accuracy (%) | Recall (%) | Precision (%) | Bỏ sót lỗi (FN) | Báo nhầm lỗi (FP) | Nhận xét vận hành |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **0.30 - 0.40 (Khuyên dùng)** | **100.0%** | **100.0%** | **100.0%** | **0 quả** | **0 quả** | **Vùng an toàn tuyệt đối, triệt tiêu rủi ro lây lan Ethylene** |
| 0.50 (Mặc định) | 100.0% | 100.0% | 100.0% | 0 quả | 0 quả | Cân bằng lý thuyết |
| 0.60 | 99.98% | 99.96% | 100.0% | 1 quả | 0 quả | Bắt đầu phát sinh rủi ro lọt quả thối |
| 0.70 | 99.95% | 99.91% | 100.0% | 2 quả | 0 quả | Nguy cơ lây nhiễm mốc sang cả container |

*(Dữ liệu trích xuất từ [`results/threshold_tuning_analysis.csv`](file:///e:/Project%20SIC/results/threshold_tuning_analysis.csv))*

---

## 🔍 Explainable AI (Grad-CAM Heatmaps)

Mô hình không phải là "hộp đen" (Black-box). Hệ thống tích hợp thuật toán **Grad-CAM (Gradient-weighted Class Activation Mapping)** trích xuất gradient từ tầng tích chập cuối cùng để sinh bản đồ nhiệt:

![Bản Đồ Nhiệt Grad-CAM Minh Họa](file:///e:/Project%20SIC/results/gradcam_10_samples.png)

- **Trực quan hóa vùng tổn thương:** Vùng màu đỏ - cam tập trung chính xác 100% vào các ổ nấm mốc trắng (*Penicillium*), vết bầm tím do va đập cơ học hoặc đốm thâm đen oxy hóa.
- **Loại bỏ nhiễu phông nền:** Mô hình hoàn toàn không bị đánh lừa bởi bề mặt bàn, ánh sáng đèn chiếu hay phông nền xung quanh.

---

## 🏗️ Kiến Trúc Triển Khai & Web Demo Thời Gian Thực

Hệ thống được thiết kế theo chuẩn băng chuyền quang học công nghiệp (**Smart Optical Packhouse**):

```text
[ Trái Cây Trên Băng Chuyền / Camera Điện Thoại (DroidCam) ]
                           │
             (Luồng Video HTTP / RTSP / USB ADB)
                           ▼
     ┌───────────────────────────────────────────────┐
     │    Double-Buffered Frame Ingestion Engine     │
     │    - Tự động bỏ khung hình trễ (Drop Stale)   │
     │    - Chống rớt mạng Wi-Fi (Drop Tolerance)    │
     └───────────────────────┬───────────────────────┘
                             ▼
     ┌───────────────────────────────────────────────┐
     │           Mô Hình EfficientNetB0 AI           │
     │    - Tiền xử lý RGB 224x224                   │
     │    - Ngưỡng kích hoạt Recall (Threshold: 0.4) │
     │    - Trích xuất Grad-CAM Feature Map          │
     └───────────────────────┬───────────────────────┘
                             ▼
            ┌────────────────┴────────────────┐
            ▼                                 ▼
   [ ĐẠT CHUẨN (PASS) ]              [ HƯ HỎNG (REJECT) ]
   - Xếp loại Grade A                - Cảnh báo âm thanh / HUD OSD
   - Đóng thùng xuất khẩu            - Kích hoạt gạt bỏ quả thối
```

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
Project SIC/
├── app.py                             # Giao diện Web Streamlit tương tác chính (Grad-CAM & DroidCam)
├── run_demo.bat                       # Script 1-Click tự động chạy server và mở trình duyệt
├── edge_stream_inspector.py           # Module ThreadedCamera thu nhận luồng video thời gian thực
├── download_fruit_data.py             # Script tải và kiểm toán dữ liệu 27,198 ảnh từ Kaggle
├── sync_models.py                     # Script tải và đồng bộ weights từ Google Drive / Colab
├── requirements.txt                   # Danh mục thư viện Python bắt buộc
│
├── report/                            # Báo cáo tiểu luận tốt nghiệp hoàn thiện
│   ├── BaoCao_Project13_LeThanhDuoc_SIC2026.docx  # Báo cáo Word chuẩn nộp thầy
│   ├── Bao_Cao_Tieu_Luan_Project13_LeThanhDuoc.md # Báo cáo Markdown đồng bộ GitHub
│   └── images/                                   # Các hình ảnh biểu đồ thực nghiệm chuẩn (Hình 1.1 đến 5.2)
│       ├── image1.png                 # Hình 1.1: Phân bố số lượng ảnh tập dữ liệu (27,198 ảnh)
│       ├── image2.png                 # Hình 2.1: Tiến trình huấn luyện Baseline CNN (20 Epochs)
│       ├── image3.png                 # Hình 3.1: Tiến trình huấn luyện Transfer Learning (3-Phase, 22 Epochs)
│       ├── image4.png                 # Hình 4.1: Đối chiếu ma trận nhầm lẫn 4 mô hình (Test 4,080 ảnh)
│       ├── image5.png                 # Hình 5.1: Kết quả Grad-CAM khoanh vùng tổn thương trên vỏ quả
│       └── image6.png                 # Hình 5.2: Khảo sát ngưỡng tối ưu và đối chuẩn tốc độ suy luận
│
├── models/                            # Trọng số mô hình đã huấn luyện hoàn chỉnh (.keras)
│   ├── efficientnetb0_best.keras      # Mô hình khuyên dùng sản xuất (33.1 MB, 4.38M params)
│   ├── resnet50_best.keras            # Mô hình ResNet50 (Recall 100%, 24.12M params)
│   └── vgg16_best.keras               # Mô hình VGG16 (14.85M params)
│
├── notebooks/                         # Chuỗi 5 Notebooks thực nghiệm & 1 Master Pipeline hoàn chỉnh
│   ├── 1_Fruit_EDA_Augmentation.ipynb           # Khám phá dữ liệu, kiểm toán phân tầng & Data Augmentation
│   ├── 2_Fruit_Baseline_CNN.ipynb               # Xây dựng và đánh giá mạng Baseline CNN từ đầu
│   ├── 3_Fruit_Transfer_Learning.ipynb          # Huấn luyện VGG16, ResNet50, EfficientNetB0 (Quy trình 3-Phase)
│   ├── 4_Fruit_GradCAM_ExplainableAI.ipynb      # Thuật toán Linear Logit Grad-CAM & Heatmap
│   ├── 5_Fruit_Inference_Speed_Benchmark.ipynb  # Đo đạc tốc độ suy luận & Tối ưu hóa ngưỡng rủi ro
│   └── Fruit_Full_Pipeline.ipynb                # Master Pipeline hợp nhất toàn diện từ A đến Z
│
├── processed_data/                    # Siêu dữ liệu phân chia tập dữ liệu chuẩn 27,198 ảnh (Seed 42)
│   ├── train.csv                      # Tập huấn luyện (19,038 ảnh: 8,265 tươi / 10,773 hỏng)
│   ├── val.csv                        # Tập kiểm định (4,080 ảnh: 1,771 tươi / 2,309 hỏng)
│   └── test.csv                       # Tập kiểm thử độc lập (4,080 ảnh: 1,772 tươi / 2,308 hỏng)
│
└── README.md                          # Tài liệu tổng quan dự án
```

---

## 🚀 Hướng Dẫn Cài Đặt & Khởi Chạy Nhanh

### 1. Cài đặt môi trường
Khởi động Terminal / PowerShell tại thư mục dự án và chạy:
```bash
# Khởi tạo môi trường ảo cục bộ
py -m venv .venv

# Cài đặt thư viện an toàn (NumPy < 2.0, TensorFlow < 2.16)
.\.venv\Scripts\pip.exe install -r requirements.txt
```

### 2. Khởi chạy Ứng dụng Web
- **Cách 1 (Khuyên dùng):** Nhấp đúp chuột vào file [`run_demo.bat`](file:///e:/Project%20SIC/run_demo.bat).
- **Cách 2 (Qua môi trường ảo .venv):**
  ```bash
  .\.venv\Scripts\streamlit.exe run app.py
  ```
- **Truy cập:**
  - 💻 Trên máy tính: [http://localhost:8501](http://localhost:8501)
  - 📱 Trên điện thoại cùng mạng Wi-Fi: `http://<IP_Máy_Tính>:8501`

### 3. Kết nối Camera Điện thoại (DroidCam)
1. Tải ứng dụng **DroidCam** trên điện thoại (Android / iOS) và kết nối chung Wi-Fi với máy tính.
2. Mở Web App tại tab **`📱 Camera Điện Thoại (DroidCam) & Webcam Live`**.
3. Nhập địa chỉ hiển thị trên điện thoại (ví dụ: `192.168.1.15:4747`) hoặc chọn từ lịch sử.
4. Bấm **"📸 Bắt Ảnh Từ Camera Điện Thoại"** để phân tích Grad-CAM hoặc gạt **"🔴 Bật Luồng Quét OSD HUD Liên Tục"** để giám sát như băng chuyền thời gian thực.

*(Xem hướng dẫn chi tiết tại [chayweb.md](file:///e:/Project%20SIC/chayweb.md)).*

---

## 📚 Tài Liệu Kỹ Thuật Chi Tiết

- 📘 [report/BaoCao_Project13_LeThanhDuoc_SIC2026.docx](file:///e:/Project%20SIC/report/BaoCao_Project13_LeThanhDuoc_SIC2026.docx): Báo cáo tiểu luận tốt nghiệp Microsoft Word chính thức chuẩn nộp giảng viên.
- 📄 [report/Bao_Cao_Tieu_Luan_Project13_LeThanhDuoc.md](file:///e:/Project%20SIC/report/Bao_Cao_Tieu_Luan_Project13_LeThanhDuoc.md): Toàn văn báo cáo dạng Markdown đồng bộ trực quan xem trực tiếp trên GitHub.
- ⚡ [chayweb.md](file:///e:/Project%20SIC/chayweb.md): Sổ tay lệnh Terminal, cấu hình cổng mạng và xử lý sự cố camera DroidCam.
- 📘 [Trienkhai.md](file:///e:/Project%20SIC/Trienkhai.md): Hồ sơ kỹ thuật hợp nhất, đặc tả ma trận chi phí rủi ro và rubric chấm điểm.

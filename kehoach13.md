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

| Tuần | Ngày | Công việc cụ thể | Thời lượng ước tính |
|------|------|-------------------|---------------------|
| **1** | Ngày 1 | Tạo tài khoản Kaggle + Google Colab, cài đặt môi trường | 1–2h |
| | Ngày 2 | Tải dataset Casting Defect từ Kaggle, tổ chức thư mục | 1h |
| | Ngày 3 | EDA: đếm ảnh mỗi lớp, xem phân phối, kích thước ảnh, plot mẫu | 2–3h |
| | Ngày 4 | Chia train/val/test (70/15/15), kiểm tra class imbalance | 2h |
| | Ngày 5 | Viết pipeline Data Augmentation (chỉ trên tập Train!) | 2–3h |
| | Ngày 6–7 | Review lại notebook EDA, chỉnh sửa, commit lên GitHub | 1–2h |
| **2** | Ngày 8 | Xây Baseline CNN (3–5 Conv layers) | 3h |
| | Ngày 9 | Train Baseline 20–30 epochs, vẽ Learning Curves | 2–3h |
| | Ngày 10 | Đánh giá overfitting, thêm Dropout/L2, ghi metrics | 2h |
| | Ngày 11 | Transfer Learning Phase 1: Load VGG16, freeze, train head | 3h |
| | Ngày 12 | Transfer Learning Phase 2: Unfreeze top layers, fine-tune | 3h |
| | Ngày 13–14 | Lặp lại Phase 1-2 cho ResNet50 và EfficientNetB0 | 4–5h |
| **3** | Ngày 15 | Transfer Learning Phase 3: Full fine-tune cho model tốt nhất | 3h |
| | Ngày 16 | So sánh kết quả 3 model, lập bảng tổng hợp | 2h |
| | Ngày 17 | Implement Grad-CAM, tạo heatmap ≥ 10 ảnh | 3–4h |
| | Ngày 18 | Viết phân tích Grad-CAM: mô hình nhìn vào đâu? | 2h |
| | Ngày 19 | Đo inference speed (single image + batch), vẽ biểu đồ | 2–3h |
| | Ngày 20 | Vẽ Precision-Recall Curve, tìm sweet spot threshold | 2h |
| | Ngày 21 | Review toàn bộ notebook, fix bugs, chạy lại Restart & Run All | 2–3h |
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

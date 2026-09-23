# 🍎 Fruit Visual QC: Hệ Thống Kiểm Soát Chất Lượng Nông Sản Bằng Thị Giác Máy Tính
### Tự Động Phân Loại Trái Cây Tươi & Phát Hiện Khuyết Tật Hư Hỏng / Thâm Dập

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Colab](https://img.shields.io/badge/Google%20Colab-GPU%20T4-F9AB00?style=flat&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)

> **Project 13 — Môn học: Trí Tuệ Nhân Tạo (AI & Deep Learning)**  
> Ứng dụng Convolutional Neural Networks (CNN), Transfer Learning và Explainable AI (Grad-CAM) trong bài toán phân loại và kiểm soát chất lượng nông sản xuất khẩu (*Fruit Quality Control: Fresh vs. Rotten / Defective*).

---

## 💡 Lý Do Chọn Đề Tài

1. **Ý nghĩa kinh tế & chuỗi cung ứng nông sản xuất khẩu:**
   - Việt Nam và các nước nông nghiệp hàng năm xuất khẩu hàng triệu tấn trái cây (táo, cam, chuối, xoài, thanh long...). Tuy nhiên, **tỷ lệ tổn thất sau thu hoạch (Post-harvest Loss) lên tới 20%–40%** do khâu phân loại thủ công chưa triệt để, khiến trái cây dập nát, thối rữa bị ủ kín trong container.

2. **Hạn chế nghiêm trọng của kiểm tra thủ công (Manual QC):**
   - Đa số các cơ sở đóng gói (Packhouse) hiện vẫn dựa vào công nhân đứng bên băng chuyền quan sát bằng mắt thường.
   - Sau vài giờ làm việc, mắt người bị mỏi mệt cực độ, dẫn đến tỷ lệ bỏ sót quả thâm dập lên tới 15%–25%. Tốc độ phân loại thủ công tạo ra "nút thắt cổ chai", kìm hãm năng suất xuất khẩu.

3. **Thiệt hại kinh tế bất cân xứng cực đoan (Asymmetric Risk):**
   - **Báo nhầm quả tươi thành hỏng (False Positive):** Chỉ tốn vài giây để công nhân kiểm tra lại hoặc hạ cấp bán nội địa (thiệt hại nhẹ ~$0.20/quả).
   - **Bỏ sót quả thối lọt vào thùng hàng (False Negative):** Quả thối phát sinh lượng lớn **khí Ethylene ($C_2H_4$)** và bào tử nấm mốc (*Penicillium*), kích thích toàn bộ các quả xung quanh chín nẫu và thối rữa trong quá trình vận chuyển đường biển 15–30 ngày. Hậu quả là **hư hỏng cả container hàng trị giá hàng chục nghìn USD**, bị phạt kiểm dịch quốc tế và tổn hại uy tín thương hiệu.
   - Do đó, tiêu chí sống còn của hệ thống AI là **Recall $\ge 95\%$** cho lớp sản phẩm lỗi.

4. **Tính khả thi và trực quan cao khi kiểm thử thực tế:**
   - Trái cây (táo, chuối, cam...) là vật phẩm quen thuộc, sẵn có 100% trong đời sống hàng ngày.
   - Người thuyết trình và hội đồng chấm thi có thể **dùng camera điện thoại hoặc webcam chụp trực tiếp một quả táo tươi hoặc quả chuối thâm dập thật tại chỗ** để xác thực độ chính xác của hệ thống AI trong tích tắc!

---

## 🎯 Mục Tiêu Dự Án
- **Độ chính xác phân loại:** Đạt **Accuracy $\ge 90\%$** và **Recall $\ge 95\%$** trên Test Set (đảm bảo hạn chế tối đa việc bỏ sót quả hư hỏng).
- **Transfer Learning chuẩn mực:** Huấn luyện so sánh 3 kiến trúc: **VGG16**, **ResNet50**, và **EfficientNetB0** theo quy trình 3-Phase khoa học.
- **Explainable AI (Grad-CAM):** Trực quan hóa bản đồ nhiệt (Heatmap) chứng minh mô hình định vị chính xác vết nấm mốc, đốm thâm dập trên vỏ trái cây.
- **Inference Benchmark:** Đo lường độ trễ suy luận ($ms/image$), thông lượng xử lý ($FPS$), và tìm ngưỡng phân loại tối ưu (Threshold Tuning).
- **Demo Thực Tế:** Giao diện Web tương tác Streamlit (`app.py`) hỗ trợ tải ảnh, chụp camera live và phân tích chi phí kinh tế.

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
Project SIC/
├── data/                      # Thư mục chứa dữ liệu ảnh nông sản (Train / Test)
├── notebooks/                 # Chuỗi 5 Jupyter Notebook theo quy trình chuẩn
│   ├── 1_EDA.ipynb            # Khám phá dữ liệu, phân tích RGB & Data Augmentation
│   ├── 2_Baseline_CNN.ipynb   # Baseline CNN từ đầu & phân tích Learning Curves
│   ├── 3_Transfer_Learning.ipynb # VGG16, ResNet50, EfficientNet (Quy trình 3-Phase)
│   ├── 4_GradCAM.ipynb        # Bản đồ nhiệt giải thích vị trí vết thâm dập/mốc
│   ├── 5_Inference_Speed.ipynb # Benchmark tốc độ suy luận & Tối ưu PR Threshold
│   └── Full_Pipeline.ipynb    # Master Pipeline chạy trọn vẹn từ A - Z
├── models/                    # Lưu trọng số mô hình đã huấn luyện (.keras)
├── results/                   # Biểu đồ đánh giá, Confusion Matrix, Heatmaps
├── report/                    # Báo cáo kỹ thuật tổng kết (PDF) & Slide
├── app.py                     # Demo Web App (Streamlit) với Grad-CAM & Camera Live
├── Trienkhai.md               # Hồ sơ triển khai toàn diện (Kế hoạch, hướng dẫn, phản biện)
├── requirements.txt           # Danh mục thư viện phụ thuộc
└── README.md
```

---

## 🚀 Hướng Dẫn Bắt Đầu Nhanh

### 1. Cài đặt môi trường
```bash
pip install -r requirements.txt
```

### 2. Tải Dataset Nông Sản từ Kaggle
Sử dụng bộ dữ liệu chuẩn doanh nghiệp **Fruits fresh and rotten for classification** (~13,600 ảnh RGB):
```bash
kaggle datasets download -d sriramr/fruits-fresh-and-rotten-for-classification --unzip -p data/
```

*Các nguồn dự phòng bổ sung:*
- `kaggle datasets download -d raghavrbi/fruit-freshness-dataset --unzip -p data_backup1/`
- `kaggle datasets download -d khandakerdipro/fruit-quality-classification --unzip -p data_backup2/`

### 3. Thứ tự thực thi Notebooks
1. Chạy `notebooks/1_EDA.ipynb` để khám phá, trích xuất metadata và tạo data pipeline.
2. Chạy `notebooks/2_Baseline_CNN.ipynb` để huấn luyện mô hình cơ sở Custom CNN.
3. Chạy `notebooks/3_Transfer_Learning.ipynb` để huấn luyện 3 mô hình Transfer Learning (Phase 1 -> Phase 2 -> Phase 3).
4. Chạy `notebooks/4_GradCAM.ipynb` để xuất heatmap giải thích trực quan vết khuyết tật.
5. Chạy `notebooks/5_Inference_Speed.ipynb` để benchmark tốc độ suy luận ($ms$) và tìm ngưỡng Sweet Spot.

### 4. Khởi chạy Ứng dụng Web Demo
```bash
streamlit run app.py
```

---

## 📊 Kết Quả Thực Nghiệm Dự Kiến

| Mô hình | Accuracy (Test) | Precision | Recall (Ưu tiên Lỗi) | F1-Score | Latency (ms/ảnh) |
|---|:---:|:---:|:---:|:---:|:---:|
| Baseline CNN | ~86.5% | ~84.2% | ~88.1% | ~86.1% | ~18 ms |
| VGG16 | ~92.4% | ~91.0% | ~94.2% | ~92.6% | ~45 ms |
| ResNet50 | ~95.8% | ~94.5% | ~97.3% | ~95.9% | ~28 ms |
| **EfficientNetB0 (Khuyên dùng)** | **~96.7%** | **~95.8%** | **~98.1%** | **~96.9%** | **~15 ms** |

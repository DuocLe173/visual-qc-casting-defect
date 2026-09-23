# 🏭 Visual QC: Kiểm Soát Chất Lượng Sản Phẩm Bằng Ảnh

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io/)
[![Colab](https://img.shields.io/badge/Google%20Colab-GPU%20T4-F9AB00?style=flat&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)

> **Project 13 — Môn học: Trí Tuệ Nhân Tạo**  
> Ứng dụng Convolutional Neural Networks (CNN), Transfer Learning và Grad-CAM trong bài toán phát hiện khuyết tật bề mặt sản phẩm đúc kim loại (*Casting Defect*).

---

## 💡 Lý Do Chọn Đề Tài

1. **Ý nghĩa sống còn trong sản xuất cơ khí & công nghiệp nặng:**
   - **Đúc kim loại (Metal Casting)** là nguyên công nền tảng tạo phôi cho hầu hết các ngành công nghiệp mũi nhọn: ô tô, hàng không, đóng tàu và máy móc cơ khí. Trong quá trình kết tinh và làm nguội, các khuyết tật bề mặt như **rỗ khí (blowholes), vết nứt tế vi (pinholes), co ngót không đều và lẫn xỉ** luôn tiềm ẩn và không thể loại trừ triệt để.

2. **Hạn chế nghiêm trọng của kiểm tra thủ công (Manual QC):**
   - Đa số các nhà máy đúc hiện nay vẫn phụ thuộc vào công nhân kiểm tra bằng mắt thường. Phương pháp thủ công này bộc lộ 3 nhược điểm lớn:
     - **Tính chủ quan và sai sót cao:** Tỷ lệ bỏ sót lỗi tăng vọt khi công nhân mỏi mắt sau ca làm việc dài.
     - **Năng suất giới hạn:** Kiểm định thủ công trở thành "nút thắt cổ chai" (bottleneck), kìm hãm tốc độ của toàn bộ dây chuyền tự động.
     - **Thiếu tính định lượng & truy vết:** Không có dữ liệu số hóa tức thời để phân tích nguyên nhân gốc rễ (Root Cause Analysis).

3. **Thiệt hại kinh tế bất cân xứng (Asymmetric Risk):**
   - Trong dây chuyền sản xuất:
     - Báo nhầm 1 sản phẩm đạt thành lỗi (**False Positive**): Chỉ tốn vài giây để công nhân soi lại.
     - Nhưng **bỏ sót 1 phôi khuyết tật lọt ra ngoài (False Negative)**: Phôi nứt lọt vào công đoạn gia công CNC tinh xảo sẽ gây gãy dao cụ đắt tiền, hoặc nguy hiểm hơn là vỡ khối động cơ khi xe lăn bánh, dẫn đến khiếu nại, đền bù bảo hiểm và tổn hại nghiêm trọng đến uy tín thương hiệu.

4. **Sự kết hợp hoàn hảo giữa Deep Learning & Tự động hóa:**
   - Đề tài ứng dụng mạng tích chập sâu (**CNN**) kết hợp các kiến trúc hàng đầu (**VGG16, ResNet50, EfficientNetB0**) và công nghệ giải thích quyết định **Grad-CAM (Explainable AI)** nhằm tạo ra một hệ thống Visual QC thời gian thực: phân loại chính xác, minh bạch vùng lỗi và sẵn sàng tích hợp trực tiếp vào băng chuyền công nghiệp.

---

## 🎯 Mục Tiêu Dự Án
- **Phân loại ảnh đạt / lỗi:** Đạt **Accuracy $\ge 90\%$** và **Recall $\ge 95\%$** trên Test Set (đảm bảo không bỏ sót sản phẩm khuyết tật).
- **Transfer Learning:** Áp dụng quy trình 3 Phase chuẩn trên 3 kiến trúc: **VGG16**, **ResNet50**, và **EfficientNetB0**.
- **Explainable AI (Grad-CAM):** Trực quan hóa bản đồ nhiệt (Heatmap) giải thích các đặc trưng dị tật mà mô hình tập trung nhận diện.
- **Inference Benchmark:** Phân tích độ trễ (latency), thông lượng (throughput FPS) theo batch và tối ưu hóa ngưỡng trên đường cong Precision-Recall.
- **Demo Thực Tế:** Giao diện Web tương tác (Streamlit) hỗ trợ kỹ sư QC kiểm định tức thì.

---

## 📂 Cấu Trúc Dự Án

```text
Project SIC/
├── data/                      # Dữ liệu ảnh phôi đúc (Train/Val/Test)
├── notebooks/                 # Chuỗi 5 Jupyter Notebook theo quy trình chuẩn
│   ├── 1_EDA.ipynb            # Khám phá dữ liệu, phân tích phân phối & Augmentation
│   ├── 2_Baseline_CNN.ipynb   # Baseline CNN từ đầu & phân tích Learning Curves
│   ├── 3_Transfer_Learning.ipynb # VGG16, ResNet50, EfficientNet (3-Phase)
│   ├── 4_GradCAM.ipynb        # Bản đồ nhiệt giải thích quyết định
│   ├── 5_Inference_Speed.ipynb # Đo tốc độ suy luận & Tối ưu PR Threshold
│   └── Full_Pipeline.ipynb    # Master Pipeline chạy trọn vẹn từ A - Z
├── models/                    # Lưu trọng số mô hình (.keras)
├── results/                   # Biểu đồ, ma trận nhầm lẫn và ảnh Heatmap
├── report/                    # Báo cáo học thuật (PDF) & Slide thuyết trình
├── app.py                     # Demo Web App (Streamlit)
├── huongdan.md                # Cẩm nang hướng dẫn A - Z chi tiết
├── kehoach13.md               # Kế hoạch thực hiện theo ngày & rubric
├── requirements.txt           # Danh mục thư viện phụ thuộc
└── README.md
```

---

## 🚀 Hướng Dẫn Bắt Đầu Nhanh

### 1. Cài đặt môi trường
```bash
pip install -r requirements.txt
```

### 2. Tải Dataset từ Kaggle
Cung cấp file token `kaggle.json` vào máy hoặc Google Colab:
```bash
kaggle datasets download -d ravirajsinh45/real-life-industrial-dataset-of-casting-product
unzip real-life-industrial-dataset-of-casting-product.zip -d data/
```

### 3. Thứ tự thực thi Notebooks
1. Chạy `notebooks/1_EDA.ipynb` để khám phá và tạo pipeline dữ liệu.
2. Chạy `notebooks/2_Baseline_CNN.ipynb` để huấn luyện mô hình cơ sở.
3. Chạy `notebooks/3_Transfer_Learning.ipynb` để huấn luyện 3 mô hình Transfer Learning (Phase 1 -> 2 -> 3).
4. Chạy `notebooks/4_GradCAM.ipynb` để xuất heatmap giải thích trực quan.
5. Chạy `notebooks/5_Inference_Speed.ipynb` để benchmark tốc độ và tìm ngưỡng Sweet Spot.

---

## 📊 Kết Quả Thực Nghiệm (Tóm tắt)
*Sẽ cập nhật sau khi hoàn tất training trên Google Colab.*

| Mô hình | Accuracy (Test) | Precision | Recall (Ưu tiên) | F1-Score | Latency (ms/ảnh) |
|---|:---:|:---:|:---:|:---:|:---:|
| Baseline CNN | ... | ... | ... | ... | ... |
| VGG16 | ... | ... | ... | ... | ... |
| ResNet50 | ... | ... | ... | ... | ... |
| **EfficientNetB0 (Tối ưu)** | ... | ... | ... | ... | ... |

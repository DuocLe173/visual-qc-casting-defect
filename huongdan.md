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
|---|:---:|---|
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

#### Đánh giá trên tập Test độc lập:
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
|---|:---:|---|
| **Baseline CNN + Learning Curves** | 15 | Tự dựng CNN 3-5 lớp Conv, có biểu đồ Train/Val Loss & Acc, phân tích rõ hiện tượng overfitting. |
| **Transfer Learning đúng 3 Phase** | 25 | Thực hiện tuần tự Phase 1 (Freeze) $\rightarrow$ Phase 2 (Unfreeze top) $\rightarrow$ Phase 3 (Full fine-tune), điều chỉnh Learning rate chuẩn xác. |
| **Metrics: Accuracy ≥ 90%, Recall ≥ 95%** | 25 | Đo đạc trên **Test set độc lập**, có Confusion Matrix chi tiết, ưu tiên Recall không bỏ sót phôi lỗi. |
| **Grad-CAM Visualization & Phân tích** | 20 | Trực quan hóa Heatmap trên $\ge 10$ ảnh (cả đạt và lỗi), có phân tích ngữ nghĩa xem mô hình nhìn đúng khuyết tật hay không. |
| **Inference Speed Analysis** | 15 | Đo đạc Latency (ms/ảnh) và Throughput (FPS theo batch 16/32/64), đối chiếu tính khả thi thực tế. |
| **ĐIỂM CHÍNH THỨC** | **100** | Hoàn thiện đầy đủ báo cáo PDF $\le 15$ trang, slide $\le 12$ trang, notebook chạy thông suốt (Restart & Run All). |
| **ĐIỂM THƯỞNG (BONUS)** | **+5 đến +10** | Web App demo tương tác trực tiếp (Streamlit/Gradio), hoặc tối ưu hóa mô hình bằng TensorFlow Lite / ONNX. |

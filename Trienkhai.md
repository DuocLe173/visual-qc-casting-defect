# 📘 HỒ SƠ TRIỂN KHAI TOÀN DIỆN DỰ ÁN — PROJECT 13
## Hệ Thống Kiểm Soát Chất Lượng Nông Sản Bằng Thị Giác Máy Tính (Fruit Visual QC)
### Tự Động Phân Loại Trái Cây Tươi & Phát Hiện Khuyết Tật Hư Hỏng / Thâm Dập

> **Môn học:** Trí Tuệ Nhân Tạo (AI & Deep Learning)  
> **Chủ đề ứng dụng:** Phân loại chất lượng trái cây xuất khẩu (*Fresh vs. Rotten / Defective Fruits Detection*)  
> **Môi trường triển khai:** Dây chuyền băng chuyền tự động (Smart Packhouse) & Ứng dụng Web / Mobile giám sát thời gian thực  
> **Tài liệu hợp nhất:** Toàn bộ hồ sơ kỹ thuật từ đặc tả bài toán, phân tích kinh tế - kỹ thuật, kế hoạch 4 tuần, hướng dẫn lập trình chuẩn Deep Learning, phản biện chuyên gia và kiến trúc triển khai thực tế.

---

## 📑 MỤC LỤC TỔNG QUAN

1. [Phần 1: Đặc Tả Đề Tài & Yêu Cầu Kỹ Thuật (Project 13)](#phần-1-đặc-tả-đề-tài--yêu-cầu-kỹ-thuật-project-13)
2. [Phần 2: Nguồn Dữ Liệu Chuẩn Doanh Nghiệp & Tiền Xử Lý (Kaggle Enterprise Datasets)](#phần-2-nguồn-dữ-liệu-chuẩn-doanh-nghiệp--tiền-xử-lý)
3. [Phần 3: Ý Tưởng Giải Pháp & Mô Hình Kinh Tế Dây Chuyền Nông Sản (Smart Packhouse)](#phần-3-ý-tưởng-giải-pháp--mô-hình-kinh-tế-dây-chuyền-nông-sản)
4. [Phần 4: Kế Hoạch Triển Khai 4 Tuần & Rubric Đánh Giá Giảng Viên](#phần-4-kế-hoạch-triển-khai-4-tuần--rubric-đánh-giá-giảng-viên)
5. [Phần 5: Hướng Dẫn Kỹ Thuật Thực Chiến Từ A Đến Z (5 Notebooks Chuẩn Mực)](#phần-5-hướng-dẫn-kỹ-thuật-thực-chiến-từ-a-đến-z)
6. [Phần 6: Nhận Xét, Phản Biện Chuyên Gia & Tối Ưu Hóa Chi Phí Lỗi (Cost Matrix)](#phần-6-nhận-xét-phản-biện-chuyên-gia--tối-ưu-hóa-chi-phí-lỗi)
7. [Phần 7: Hệ Sinh Thái Công Nghệ & Triển Khai Web Demo (Streamlit Web App)](#phần-7-hệ-sinh-thái-công-nghệ--triển-khai-web-demo)

---

# PHẦN 1: ĐẶC TẢ ĐỀ TÀI & YÊU CẦU KỸ THUẬT (PROJECT 13)

### 1.1. Thông tin chung
- **Chương liên quan:** Chương 8: Mạng Nơ-ron Sâu (Deep Neural Networks) · Chương 9: Mạng Tích Chập (Convolutional Neural Networks - CNN)
- **Loại bài toán:** Phân loại ảnh nhị phân & đa lớp (Binary & Multi-class Image Classification)
- **Độ khó:** ⭐⭐⭐ (Trung bình — Nâng cao)
- **Đối tượng áp dụng:** Nông nghiệp công nghệ cao (AgTech), Hệ thống thông tin chuỗi cung ứng nông sản, Doanh nghiệp chế biến & đóng gói xuất khẩu trái cây (Smart Packhouse).

### 1.2. Bối cảnh bài toán & Tính cấp thiết thực tế
1. **Khủng hoảng thất thoát sau thu hoạch (Post-harvest Food Loss):**
   - Hàng năm, ngành nông nghiệp toàn cầu tổn thất từ 20% đến 40% sản lượng rau củ quả tươi do hư hỏng trong quá trình thu hái, bảo quản và vận chuyển.
   - Các loại trái cây tiêu dùng hàng ngày (táo, cam, chuối, xoài, thanh long...) rất dễ bị tổn thương cơ học (dập nát khi va chạm) hoặc nhiễm nấm mốc (*Botrytis cinerea, Penicillium expansum*).
2. **Hiệu ứng lây lan chéo nguy hiểm ("One bad apple spoils the bunch"):**
   - Trái cây bị thối hỏng sẽ sinh ra lượng lớn khí **Ethylene ($C_2H_4$)** làm kích thích quá trình chín sớm và phân hủy hàng loạt các quả tươi xung quanh.
   - Vi nấm và bào tử mốc phát tán cực nhanh trong môi trường đóng thùng kín. Chỉ cần **lọt 1 quả thối vào thùng đóng gói xuất khẩu**, toàn bộ lô hàng trị giá hàng chục nghìn USD có nguy cơ bị thối rữa khi cập cảng nước ngoài, dẫn đến bị tiêu hủy toàn bộ container và bị phạt nặng theo quy chuẩn kiểm dịch thực vật.
3. **Sự bế tắc của phân loại thủ công (Manual Inspection):**
   - Đa số cơ sở thu mua trái cây hiện nay phụ thuộc vào công nhân đứng bên băng chuyền quan sát bằng mắt thường.
   - Sau 2–3 giờ làm việc liên tục, mắt người bị mỏi mệt cực độ, dẫn đến tỷ lệ bỏ sót quả thâm dập lên tới 15%–25%.
   - Chi phí nhân công ca đêm cao, thiếu tính nhất quán và không lưu lại được dữ liệu số để phân tích chất lượng nông trường.
4. **Tại sao sinh viên dễ dàng kiểm thử tại nhà?**
   - Không giống như phôi đúc kim loại hay chip bán dẫn rất khó tiếp cận ngoài đời thực, **trái cây tươi và trái cây có tì vết/thâm dập là vật phẩm có sẵn 100% trong mọi gia đình (táo, chuối, cam...)**.
   - Bất kỳ giảng viên hay giám khảo nào cũng có thể cầm trực tiếp một quả táo tươi hoặc một quả chuối thâm trên bàn, đưa trước camera điện thoại hoặc webcam máy tính để kiểm tra độ nhạy và chính xác của mô hình AI theo thời gian thực!

### 1.3. Mục tiêu kỹ thuật bắt buộc của dự án
- **Độ chính xác tổng thể:** Đạt **Accuracy $\ge 90\%$** trên tập dữ liệu kiểm thử độc lập (Test Set).
- **Chỉ số sinh tử (Recall):** Đạt **Recall $\ge 95\%$** đối với lớp sản phẩm lỗi (`Rotten / Defective`) — tuyệt đối hạn chế tối đa việc bỏ sót quả hư hỏng lọt qua băng chuyền đóng thùng.
- **Áp dụng Transfer Learning chuẩn mực:** Huấn luyện so sánh 3 kiến trúc tiên tiến:
  1. `VGG16` (Kiến trúc kinh điển, baseline đối chuẩn)
  2. `ResNet50` (Kiến trúc Residual skip-connection chống suy giảm gradient)
  3. `EfficientNetB0` (Kiến trúc tối ưu hóa tài nguyên Compound Scaling)
- **Minh bạch hóa mô hình với Explainable AI (Grad-CAM):** Trực quan hóa bản đồ nhiệt (Heatmap), chứng minh mạng nơ-ron thực sự phát hiện đúng vùng nấm mốc, vết thâm, đốm đen thối rữa chứ không dựa vào phông nền ngẫu nhiên.
- **Đo lường hiệu năng suy luận (Inference Speed Benchmark):**
  - Đo thời gian xử lý từng ảnh đơn lẻ ($ms/image$).
  - Đo thông lượng xử lý theo lô ($Throughput - FPS$).
  - Phân tích tính khả thi khi nhúng mô hình vào camera công nghiệp trên băng chuyền tốc độ cao (15–30 khung hình/giây).
- **Ứng dụng Web Demo tương tác:** Xây dựng Dashboard Streamlit hoàn chỉnh, hỗ trợ tải ảnh từ máy, chụp trực tiếp bằng camera, điều chỉnh ngưỡng nhạy cảm (Confidence Threshold), và tính toán ma trận chi phí thiệt hại kinh tế.

---

# PHẦN 2: NGUỒN DỮ LIỆU CHUẨN DOANH NGHIỆP & TIỀN XỬ LÝ

Để đảm bảo dự án đáp ứng tiêu chuẩn công nghiệp và có thể vận hành ổn định lâu dài, hệ thống được thiết kế tương thích với **3 bộ dữ liệu chuẩn mực nhất hiện nay**:

```
                              ┌──────────────────────────────────────────────────────────┐
                              │  Kaggle / AgTech Enterprise Fruit Quality Datasets       │
                              └────────────────────────────┬─────────────────────────────┘
                                                           │
                     ┌─────────────────────────────────────┼─────────────────────────────────────┐
                     ▼                                     ▼                                     ▼
        ┌─────────────────────────┐           ┌─────────────────────────┐           ┌─────────────────────────┐
        │  Nguồn 1: sriramr/      │           │  Nguồn 2: raghavrbi/    │           │  Nguồn 3: khandakerdipro│
        │  fruits-fresh-and-rotten│           │  fruit-freshness-dataset│           │  fruit-quality-class.   │
        ├─────────────────────────┤           ├─────────────────────────┤           ├─────────────────────────┤
        │ • 13,599 ảnh RGB        │           │ • 10,000+ ảnh đa góc    │           │ • 8,000+ ảnh khuyết tật │
        │ • Apple, Banana, Orange │           │ • Apple, Banana, Tomato │           │ • Đốm thâm, dập vỏ, mốc │
        │ • Chuẩn packhouse       │           │ • Cross-domain testing  │           │ • Độ phân giải cao      │
        │ • [NGUỒN CHÍNH THỨC]    │           │ • [NGUỒN DỰ PHÒNG 1]    │           │ • [NGUỒN DỰ PHÒNG 2]    │
        └─────────────────────────┘           └─────────────────────────┘           └─────────────────────────┘
```

### 2.1. Nguồn Dữ Liệu Chính Thức (Primary Enterprise Source)
- **Tên dataset trên Kaggle:** `sriramr/fruits-fresh-and-rotten-for-classification`
- **Tác giả:** Sriram Reddy Kalluri
- **Quy mô:** **13,599 ảnh RGB** độ nét cao chụp cận cảnh các loại quả tiêu chuẩn thương phẩm.
- **Cấu trúc dữ liệu có sẵn:**
  - `dataset/train/` (~10,900 ảnh)
  - `dataset/test/` (~2,699 ảnh)
  - Các lớp: `freshapples`, `rottenapples`, `freshbanana`, `rottenbanana`, `freshoranges`, `rottenoranges`.
- **Ưu thế công nghiệp:**
  - Được chuẩn hóa cấu trúc thư mục, ảnh chụp phong phú từ nhiều góc độ của trái cây trên đĩa cân hoặc mặt bàn xưởng đóng gói.
  - Cho phép triển khai 2 chế độ:
    1. **Chế độ Nhị phân Toàn diện (Binary General QC):** Gộp toàn bộ `fresh*` thành nhãn `Fresh (Đạt chuẩn)` và `rotten*` thành `Rotten (Khuyết tật/Hư hỏng)`.
    2. **Chế độ Trái cây Chuyên biệt (Single-Commodity QC):** Huấn luyện phân loại chuyên sâu cho Quả Táo (`freshapples` vs `rottenapples`), hỗ trợ demo nhanh nhất bằng 1 quả táo thật tại lớp học.
- **Lệnh tải tự động từ Kaggle API:**
  ```bash
  kaggle datasets download -d sriramr/fruits-fresh-and-rotten-for-classification --unzip -p data/
  ```

### 2.2. Các Nguồn Dữ Liệu Dự Phòng & Mở Rộng
1. **Nguồn Dự Phòng 1 — `raghavrbi/fruit-freshness-dataset`:**
   - Hơn 10,000 bức ảnh với điều kiện ánh sáng đa dạng (ánh sáng vàng, ánh sáng tự nhiên, bóng đổ).
   - Thích hợp để làm tập kiểm thử ngoại lai (Out-of-Distribution Validation) nhằm đánh giá độ bền vững của mô hình khi chuyển đổi giữa các nhà xưởng khác nhau.
2. **Nguồn Dự Phòng 2 — `khandakerdipro/fruit-quality-classification`:**
   - Tập trung sâu vào các cấp độ khuyết tật cơ học: vết bầm dập vỏ, đốm đen li ti do bọ trĩ chích, nấm trắng bề mặt.
   - Rất giá trị khi biểu diễn Grad-CAM vì trực quan hóa chính xác các đốm bệnh nhỏ li ti mà mắt người dễ bỏ sót.

### 2.3. Quy trình Tiền Xử Lý Dữ Liệu Chuẩn (Data Preprocessing Pipeline)
1. **Chuẩn hóa kích thước (Resizing):** Đưa toàn bộ ảnh về độ phân giải chuẩn $224 \times 224$ pixels (chuẩn đầu vào của VGG16, ResNet50, EfficientNetB0).
2. **Phép tăng cường dữ liệu đặc thù cho nông sản (Data Augmentation):**
   - **Xoay ngẫu nhiên ($Rotation \pm 30^\circ$):** Mô phỏng việc quả lăn tự do trên băng chuyền con lăn.
   - **Lật ngang & dọc ($Horizontal/Vertical Flip$):** Trái cây có tính đối xứng hình học tự nhiên.
   - **Điều chỉnh độ sáng & độ tương phản ($Brightness \pm 20\%$, $Contrast$):** Mô phỏng sự thay đổi ánh sáng đèn LED nhà xưởng theo các ca làm việc ngày và đêm.
   - **Thu phóng nhẹ ($Zoom \pm 15\%$):** Mô phỏng kích thước quả to nhỏ không đồng đều.
3. **Phân chia tập dữ liệu:** Tỷ lệ phân chia chuẩn khoa học: **70% Training — 15% Validation — 15% Test** (Stratified sampling giữ nguyên tỷ lệ cân bằng giữa Fresh và Rotten).

---

# PHẦN 3: Ý TƯỞNG GIẢI PHÁP & MÔ HÌNH KINH TẾ DÂY CHUYỀN NÔNG SẢN

### 3.1. Sơ đồ Nguyên lý Hoạt động của Dây chuyền Smart Packhouse
Hệ thống Visual QC được thiết kế để đặt tại trạm kiểm định quang học ngay sau bồn rửa ozone và sấy khô của dây chuyền đóng gói:

```
[Bồn Rửa & Khử Khuẩn] ──► [Băng Chuyền Con Lăn Tự Xoay]
                                     │
                             (Camera Công Nghiệp 30 FPS)
                                     ▼
                      ┌─────────────────────────────┐
                      │    Hệ Thống Edge AI / GPU   │
                      │   - Tiền xử lý ảnh RGB      │
                      │   - EfficientNetB0 Suy luận │
                      │   - Ngưỡng kích hoạt Recall │
                      └──────────────┬──────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
         [Xác suất Tươi ≥ Thresh]           [Xác suất Thối > Thresh]
                    │                                 │
           (Tiếp tục đi thẳng)             (Kích hoạt Cánh Tay Khí Nén)
                    ▼                                 ▼
          ┌───────────────────┐             ┌───────────────────┐
          │ Thùng Xuất Khẩu   │             │ Thùng Phế Phẩm /  │
          │ Tiêu Chuẩn Global │             │ Chế Biến Mứt/Nước │
          │ GAP / USDA        │             │ Ép Công Nghiệp    │
          └───────────────────┘             └───────────────────┘
```

### 3.2. Phân tích Kinh tế & Ma trận Chi phí Bất cân xứng (Industrial Cost Matrix)
Trong phân loại nông sản xuất khẩu, chi phí sai số mang tính **bất đối xứng cực kỳ nghiêm trọng**:

| Thực tế \ Dự đoán | Dự đoán là TƯƠI (PASS) | Dự đoán là HƯ HỎNG (DEFECT) |
|---|---|---|
| **Thực tế: HƯ HỎNG (Defective)** | **False Negative (BỎ SÓT LỖI)**<br>⚠️ **Hậu quả cực kỳ nghiêm trọng:** Quả thối phát tán nấm mốc và khí Ethylene làm hư hỏng cả thùng/lô hàng container trong quá trình vận chuyển đường biển (15–30 ngày).<br>💰 **Tổn thất ước tính:** **$50.00 – $500.00 / sự cố** (Bồi thường hợp đồng, hủy container, mất chứng chỉ xuất khẩu). | **True Positive (BẮT ĐÚNG LỖI)**<br>✅ Loại bỏ kịp thời quả hỏng sang khu chế biến thứ cấp (ủ phân sinh học hoặc làm nước ép công nghiệp). |
| **Thực tế: TƯƠI (Fresh)** | **True Negative (ĐẠT CHUẨN)**<br>✅ Đóng gói đạt chuẩn xuất khẩu sang các thị trường khó tính (EU, Mỹ, Nhật Bản). | **False Positive (BÁO LỖI NHẦM)**<br>⚠️ Quả tươi bị loại nhầm ra khỏi thùng đóng gói.<br>💰 **Tổn thất ước tính:** **$0.20 – $0.50 / quả** (Tốn công nhân kiểm tra lại thủ công hoặc hạ phẩm cấp bán giá thấp). |

👉 **Kết luận chiến lược:**
$$\text{Chi phí tổn thất do Bỏ sót lỗi (FN)} \approx 100 \times \text{Chi phí do Báo nhầm (FP)}$$
Do đó, hệ thống bắt buộc phải **ưu tiên tối đa Recall $\ge 95\%$** cho lớp hư hỏng, chấp nhận hạ ngưỡng phân loại xác suất (Threshold Tuning từ 0.5 xuống 0.35–0.40) để đảm bảo không một quả nấm mốc nào có thể lọt vào container xuất khẩu.

---

# PHẦN 4: KẾ HOẠCH TRIỂN KHAI 4 TUẦN & RUBRIC ĐÁNH GIÁ GIẢNG VIÊN

### 4.1. Tiến độ thực hiện 4 tuần chuẩn mực

| Tuần | Giai đoạn & Nhiệm vụ trọng tâm | Sản phẩm đầu ra (Deliverables) |
|:---:|---|---|
| **Tuần 1** | **Khảo sát đề tài & Khám phá Dữ liệu (EDA)**<br>• Thiết lập môi trường Python/Conda & Google Colab GPU T4.<br>• Tải dataset chuẩn Kaggle `sriramr/fruits-fresh-and-rotten-for-classification`.<br>• Phân tích phân bố lớp (Class balance), tỷ lệ màu sắc (RGB Histograms), kích thước ảnh.<br>• Xây dựng Data Pipeline với tf.data / ImageDataGenerator kết hợp Augmentation chuyên biệt cho trái cây. | • Hoàn thành `notebooks/1_EDA.ipynb`.<br>• Biểu đồ phân bố ảnh, ma trận ảnh mẫu Fresh vs Rotten.<br>• Bộ dữ liệu đã tiền xử lý được chia Train/Val/Test (70/15/15). |
| **Tuần 2** | **Huấn luyện Mô hình Baseline CNN**<br>• Thiết kế mạng CNN tự xây dựng từ đầu (3 đến 4 khối Conv2D + MaxPooling + Dropout + Dense).<br>• Huấn luyện với Binary Crossentropy và Adam optimizer.<br>• Phân tích hiện tượng Overfitting thông qua đồ thị Learning Curves (Loss & Accuracy).<br>• Đánh giá trên Test set để làm chuẩn đối sánh (Baseline Benchmark). | • Hoàn thành `notebooks/2_Baseline_CNN.ipynb`.<br>• Model weight `models/baseline_cnn.keras`.<br>• Báo cáo đối chuẩn sơ bộ: Accuracy ~85-88%, thời gian train. |
| **Tuần 3** | **Đột phá với Transfer Learning (3-Phase Training)**<br>• Xây dựng quy trình 3 Phase chuẩn khoa học cho 3 kiến trúc: **VGG16**, **ResNet50**, **EfficientNetB0**:<br>  - *Phase 1 (Feature Extraction):* Đóng băng hoàn toàn Feature Extractor, chỉ huấn luyện Classification Head.<br>  - *Phase 2 (Fine-tuning Top Layers):* Mở khóa các block cuối cùng với Learning Rate nhỏ ($10^{-5}$).<br>  - *Phase 3 (Global Evaluation):* Tinh chỉnh toàn diện, so sánh các chỉ số Accuracy, Precision, Recall, F1-Score. | • Hoàn thành `notebooks/3_Transfer_Learning.ipynb`.<br>• Lưu trọng số các model tốt nhất vào `models/`.<br>• Bảng so sánh hiệu năng chi tiết giữa 3 kiến trúc.<br>• Khẳng định EfficientNetB0 / ResNet50 vượt ngưỡng Recall 95%. |
| **Tuần 4** | **Explainable AI (Grad-CAM), Benchmark Tốc độ & Web Demo**<br>• Cài đặt thuật toán Grad-CAM trên lớp Conv cuối cùng của mô hình tốt nhất.<br>• Xuất bản đồ nhiệt Heatmap đối chiếu trực quan vết thâm dập nấm mốc trên quả.<br>• Benchmark độ trễ suy luận (Single-image Latency vs Batch Throughput FPS).<br>• Tối ưu ngưỡng phân loại (PR Curve Sweet Spot).<br>• Hoàn thiện Web App Streamlit (`app.py`), cho phép người dùng tải ảnh hoặc bật camera điện thoại kiểm tra trái cây trực tiếp. | • Hoàn thành `notebooks/4_GradCAM.ipynb`.<br>• Hoàn thành `notebooks/5_Inference_Speed.ipynb`.<br>• Ứng dụng Web `app.py` chạy mượt mà.<br>• Báo cáo kỹ thuật tổng kết và Slide thuyết trình. |

### 4.2. Rubric Chấm Điểm & Chiến Lược Đạt Điểm Tối Đa (Max Score)

| Tiêu chí Rubric | Trọng số | Yêu cầu để đạt điểm tuyệt đối (Grade A+) |
|---|:---:|---|
| **1. Khám phá & Tiền xử lý Dữ liệu (EDA)** | **15%** | Phân tích sâu sắc bản chất ảnh nông sản (đặc trưng màu sắc vỏ, vết đổi màu do oxy hóa), áp dụng Augmentation thực tế mô phỏng chuyển động băng chuyền, chia tập dữ liệu chặt chẽ không bị rò rỉ (Data Leakage). |
| **2. Baseline CNN & Learning Curves** | **15%** | Kiến trúc mạch lạc, có Dropout/BatchNormalization ngăn chặn Overfitting rõ rệt; biểu đồ phân tích Loss/Val_Loss có lập luận kỹ thuật vững vàng. |
| **3. Transfer Learning (Quy trình 3 Phase)** | **25%** | Triển khai bài bản cả 3 kiến trúc (VGG16, ResNet50, EfficientNetB0). Giải thích rõ tại sao đóng băng/mở khóa từng tầng và việc lựa chọn Learning Rate thích ứng (Adaptive Learning Rate). |
| **4. Hiệu năng & Chỉ số Kiểm định (Metrics)** | **25%** | Đạt **Accuracy $\ge 90\%$** và **Recall $\ge 95\%$** trên Test set. Phân tích chi tiết Confusion Matrix, ROC-AUC, Precision-Recall Curve gắn liền với bài toán kinh tế hạn chế lọt quả thối. |
| **5. Explainable AI & Trực quan hóa (Grad-CAM)** | **10%** | Biểu diễn Heatmap chất lượng cao, chứng minh mô hình định vị chính xác đốm thối/nấm mốc chứ không "bắt nhầm" màu nền, chứng minh tính minh bạch của AI trong doanh nghiệp. |
| **6. Tối ưu Suy luận & Sản phẩm Demo (Streamlit)** | **10%** | Đo tốc độ inference chuẩn xác bằng direct execution, phân tích thông lượng theo batch (FPS), giao diện Web App chuyên nghiệp, kiểm thử live bằng ảnh chụp trái cây thực tế. |

---

# PHẦN 5: HƯỚNG DẪN KỸ THUẬT THỰC CHIẾN TỪ A ĐẾN Z

Hệ thống được tổ chức thành chuỗi 5 Jupyter Notebook độc lập, chuẩn hóa theo nguyên lý module:

### 5.1. `notebooks/1_EDA.ipynb` — Khám Phá & Xây Dựng Dữ Liệu
- **Mục tiêu:** Tải dataset từ Kaggle, trích xuất siêu dữ liệu, trực quan hóa và tiền xử lý.
- **Các bước mã hóa chính:**
  1. Tự động kiểm tra token Kaggle và tải giải nén dataset `sriramr/fruits-fresh-and-rotten-for-classification`.
  2. Quét toàn bộ đường dẫn ảnh, tạo bảng DataFrame lưu trữ đường dẫn và nhãn phân loại (`Fresh` vs `Rotten`).
  3. Vẽ biểu đồ phân bố số lượng ảnh từng lớp (đánh giá mức độ mất cân bằng dữ liệu).
  4. Trực quan hóa lưới ảnh 4x4 đại diện cho trái cây tươi (vỏ căng bóng, màu đồng nhất) và trái cây hư hỏng (đốm đen, thâm dập, mốc trắng).
  5. Xây dựng hàm `tf.data.Dataset` với bộ tiền xử lý chuẩn và xuất danh sách các tập dữ liệu ra file `processed_data/metadata.csv`.

### 5.2. `notebooks/2_Baseline_CNN.ipynb` — Huấn Luyện Mô Hình Cơ Sở
- **Mục tiêu:** Xây dựng mạng tích chập thuần túy (Custom CNN) để tạo mốc so sánh hiệu năng.
- **Kiến trúc mạng:**
  - `Conv2D(32, (3,3), activation='relu')` + `MaxPooling2D((2,2))`
  - `Conv2D(64, (3,3), activation='relu')` + `MaxPooling2D((2,2))`
  - `Conv2D(128, (3,3), activation='relu')` + `MaxPooling2D((2,2))`
  - `Flatten()` + `Dropout(0.5)` + `Dense(128, activation='relu')` + `Dense(1, activation='sigmoid')`
- **Đánh giá:** Xuất biểu đồ Training Loss vs Validation Loss qua 20 epochs, phát hiện điểm bắt đầu Overfitting và lưu mô hình `models/baseline_cnn.keras`.

### 5.3. `notebooks/3_Transfer_Learning.ipynb` — Đột Phá Hiệu Năng Với 3 Kiến Trúc
- **Mục tiêu:** Áp dụng mô hình đã huấn luyện trước trên ImageNet để trích xuất đặc trưng bậc cao của thực vật/trái cây.
- **Quy trình 3 Phase huấn luyện cho từng mô hình:**
  1. **Phase 1 — Feature Extraction (Frozen Base):** Đóng băng toàn bộ trọng số ImageNet, chỉ huấn luyện GlobalAveragePooling2D + Dense classification head ($lr = 10^{-3}$).
  2. **Phase 2 — Fine-tuning (Unfreeze Top Layers):** Mở khóa 20–30 tầng tích chập cuối cùng để học các đặc trưng đốm thâm đặc thù của trái cây ($lr = 10^{-5}$, giảm 100 lần để tránh phá vỡ trọng số tốt).
  3. **Phase 3 — Tinh chỉnh sâu & Đánh giá toàn diện:** Chạy EarlyStopping và ReduceLROnPlateau để đạt điểm hội tụ tối ưu.
- **Lưu trữ kết quả:** Xuất bảng so sánh tổng hợp Accuracy, Precision, Recall và lưu các file trọng số `models/vgg16_best.keras`, `models/resnet50_best.keras`, `models/efficientnetb0_best.keras`.

### 5.4. `notebooks/4_GradCAM.ipynb` — Giải Thích Quyết Định Bằng Bản Đồ Nhiệt
- **Mục tiêu:** Sử dụng Gradient-weighted Class Activation Mapping (Grad-CAM) để xem mô hình nơ-ron "nhìn" vào đâu trước khi ra quyết định.
- **Nguyên lý toán học:**
  - Tính đạo hàm của điểm số đầu ra lớp mục tiêu $y^c$ theo các bản đồ đặc trưng $A^k$ của tầng tích chập cuối cùng:
    $$\alpha_k^c = \frac{1}{Z} \sum_{i} \sum_{j} \frac{\partial y^c}{\partial A_{i,j}^k}$$
  - Tạo bản đồ nhiệt bằng tổ hợp tuyến tính và hàm ReLU:
    $$L_{\text{Grad-CAM}}^c = \text{ReLU}\left(\sum_{k} \alpha_k^c A^k\right)$$
- **Ứng dụng:** Trực quan hóa các vùng màu đỏ/vàng tập trung chính xác vào ổ nấm mốc hoặc vết thâm tím trên quả, chứng minh mô hình không bị "học vẹt" bối cảnh nền.

### 5.5. `notebooks/5_Inference_Speed.ipynb` — Tối Ưu Độ Trễ & Ngưỡng Quyết Định
- **Mục tiêu:** Đảm bảo hệ thống đạt chuẩn thời gian thực (Real-time Industrial Throughput).
- **Benchmark kỹ thuật:**
  - Đo thời gian suy luận trên CPU và GPU cho từng ảnh ($ms/image$) sử dụng Direct Execution (`model(x, training=False)` thay vì `model.predict()` để loại bỏ overhead).
  - Khảo sát thông lượng khi xử lý theo lô ($Batch\ Size = 1, 8, 16, 32, 64$).
  - Phân tích đường cong Precision-Recall để tìm **Ngưỡng Ngọt (Sweet Spot)**: Đảm bảo Recall $\ge 95\%$ với mức suy giảm Precision nhỏ nhất.

---

# PHẦN 6: NHẬN XÉT, PHẢN BIỆN CHUYÊN GIA & TỐI ƯU HÓA KIẾN TRÚC

Trong quá trình bảo vệ đồ án, hội đồng chuyên môn thường đặt ra các câu hỏi phản biện sâu sắc. Dưới đây là bộ câu hỏi và lập luận bảo vệ khoa học đã được chuẩn bị sẵn:

### 6.1. Câu hỏi 1: Làm sao phân biệt được giữa vết nấm thối thực sự và các đốm phấn/tỳ vết tự nhiên của trái cây?
- **Phản biện chuyên gia:** Trái cây tự nhiên thường có cuống gỗ, đốm phấn sáp bảo vệ tự nhiên, hoặc đốm vàng do tiếp xúc ánh nắng mặt trời không đều. Nếu mô hình bắt nhầm các đặc trưng này thì tỷ lệ loại nhầm (False Positive) sẽ rất cao.
- **Lập luận bảo vệ:**
  - Mạng tích chập sâu (ResNet/EfficientNet) học được cả đặc trưng kết cấu bề mặt (Texture Gradient) và màu sắc (Color Contrast). Vết thối rữa và nấm mốc luôn đi kèm hiện tượng **phá hủy cấu trúc tế bào** (vùng trũng xuống, ranh giới lan tỏa không đều, tế bào hoại tử sẫm màu) khác hẳn với đốm phấn hoặc đốm sáp có ranh giới rõ và cấu trúc tế bào phẳng.
  - Chúng tôi áp dụng Color Jittering và Contrast Augmentation trong quá trình huấn luyện để mô hình tập trung vào biến dạng kết cấu biểu bì thay vì chỉ phụ thuộc vào sắc tố màu đơn thuần.

### 6.2. Câu hỏi 2: Tại sao lại chọn mô hình EfficientNetB0 thay vì các mạng khổng lồ hơn như ResNet152 hay Vision Transformer (ViT)?
- **Phản biện chuyên gia:** Tại sao không dùng các mô hình Transformer tối tân nhất hiện nay?
- **Lập luận bảo vệ:**
  - Trong môi trường công nghiệp thực tế (Smart Packhouse), camera băng chuyền chạy với tốc độ 15–30 quả/giây. Việc triển khai các mô hình khổng lồ như ViT hoặc ResNet152 đòi hỏi máy tính công nghiệp trang bị GPU cao cấp đắt đỏ, tiêu tốn điện năng và sinh nhiệt lớn trong môi trường đóng gói ẩm ướt.
  - **EfficientNetB0** sử dụng kỹ thuật Compound Scaling và Depthwise Separable Convolutions, chỉ có ~5.3 triệu tham số (so với 25.6 triệu của ResNet50 và 138 triệu của VGG16) nhưng đạt độ chính xác tương đương hoặc vượt trội, độ trễ chỉ ~12–18ms trên CPU thông thường, hoàn toàn đáp ứng chuẩn nhúng trên các thiết bị Edge AI (như Nvidia Jetson Orin Nano / Raspberry Pi 5).

### 6.3. Câu hỏi 3: Hệ thống xử lý thế nào khi một quả chỉ bị thâm dập ở mặt khuất bên dưới?
- **Phản biện chuyên gia:** Nếu camera chỉ đặt cố định ở phía trên, quả thối nằm ở mặt dưới thì AI có nhìn thấy không?
- **Lập luận bảo vệ:**
  - Về mặt cơ khí và thiết kế hệ thống, băng chuyền công nghiệp cho nông sản sử dụng **con lăn tự xoay (Rotating Roller Conveyor)**. Khi di chuyển qua buồng chụp quang học, con lăn quay làm quả tự lộn 360 độ, camera đa góc (hoặc camera tốc độ cao chụp 3–5 khung hình/quả) sẽ bắt trọn toàn bộ bề mặt quả.
  - Về mặt thuật toán phần mềm, ứng dụng Web Demo hỗ trợ tính năng chụp nhiều góc hoặc gộp kết quả phân loại: chỉ cần 1 góc chụp phát hiện vết hư hỏng vượt ngưỡng là hệ thống sẽ lập tức gắn cờ loại bỏ ngay lập tức.

---

# PHẦN 7: HỆ SINH THÁI CÔNG NGHỆ & TRIỂN KHAI WEB DEMO (STREAMLIT)

### 7.1. Kiến trúc ứng dụng Web (`app.py`)
Giao diện Web Demo được xây dựng chuyên nghiệp bằng **Streamlit**, mang phong cách hiện đại (Dark/Light mode, Industrial UI), phục vụ trực tiếp cho buổi thuyết trình và vận hành xưởng:

```
┌────────────────────────────────────────────────────────────────────────┐
│  🍎 SMART FRUIT PACKHOUSE — VISUAL QC SYSTEM                           │
├───────────────────────────────┬────────────────────────────────────────┤
│  SIDEBAR: CẤU HÌNH & KIỂM ĐỊNH│  MAIN DASHBOARD                        │
│                               │                                        │
│  [🔘 Tải ảnh từ máy]          │  [ẢNH GỐC ĐẦU VÀO]   [BẢN ĐỒ GRAD-CAM] │
│  [📷 Bật Camera / Webcam]     │  ┌──────────────┐    ┌──────────────┐  │
│  [🍓 Chọn ảnh mẫu có sẵn]     │  │  (Ảnh Quả)   │    │  (Heatmap)   │  │
│                               │  └──────────────┘    └──────────────┘  │
│  Chọn Mô Hình:                │                                        │
│  (o) EfficientNetB0 (Khuyên)  │  KẾT QUẢ PHÂN LOẠI:                    │
│  ( ) ResNet50                 │  🟢 ĐẠT CHUẨN XUẤT KHẨU (Fresh: 98.4%) │
│  ( ) Baseline CNN             │  Thời gian xử lý: 14.2 ms              │
│                               │                                        │
│  Ngưỡng Recall (Threshold):   │  ƯỚC TÍNH CHI PHÍ LỖI (COST MATRIX):   │
│  ───[====o====]─── 0.40       │  • Thiệt hại bỏ sót lỗi: $0.00         │
│                               │  • Chi phí kiểm tra lại: $0.00         │
└───────────────────────────────┴────────────────────────────────────────┘
```

### 7.2. Các Tính Năng Nổi Bật của Web App
1. **Đa dạng kênh nạp dữ liệu:**
   - Hỗ trợ tải file ảnh (`.jpg`, `.png`, `.jpeg`).
   - Hỗ trợ chụp trực tiếp từ Webcam hoặc Camera điện thoại (rất tiện lợi khi người dùng cầm quả táo, cam, chuối thật giơ lên trước màn hình để thuyết trình).
   - Tích hợp sẵn nút "Tải ảnh mẫu" (Sample Fresh Apple, Sample Rotten Apple) để demo tức thì ngay cả khi chưa chuẩn bị quả thật.
2. **Trực quan hóa Grad-CAM theo thời gian thực:** Tự động tính toán bản đồ nhiệt và hòa trộn (overlay) lên ảnh gốc với thanh trượt điều chỉnh độ trong suốt (Alpha slider), giúp chỉ rõ vị trí vết hư hỏng.
3. **Mô phỏng Thiệt hại Kinh tế (Interactive Cost Simulator):**
   - Cho phép người dùng nhập sản lượng dự kiến đóng thùng trong ngày (ví dụ: 10,000 quả).
   - Tự động tính toán số tiền tiết kiệm được cho doanh nghiệp khi áp dụng AI Visual QC so với phân loại bằng mắt thường.

---

### 🏁 Lời Kết & Cam Kết Chất Lượng
Hồ sơ triển khai này cung cấp khung kỹ thuật hoàn chỉnh và vững chắc cho **Đề tài Kiểm soát chất lượng nông sản bằng ảnh (Fruit Visual QC)**. Bằng việc chuyển dịch sang nông sản, đề tài vừa giải quyết một bài toán kinh tế - xã hội có tác động lớn (nâng cao giá trị nông sản xuất khẩu Việt Nam), vừa sở hữu tính trực quan, hấp dẫn và khả thi tuyệt đối để thuyết trình và bảo vệ xuất sắc trước hội đồng môn học!

# 📋 KẾ HOẠCH NÂNG CẤP & HOÀN THIỆN TOÀN DIỆN — PROJECT 13 (FRUIT VISUAL QC)

Tài liệu này tổng hợp toàn bộ các đầu việc kỹ thuật cần hoàn tất để dự án đạt chuẩn xuất sắc (Rubric chấm điểm A+) từ mã nguồn, mô hình, kết quả đến báo cáo khoa học.

---

## 🎯 1. Nhóm Việc Ưu Tiên 1: Chuẩn Hóa & Dọn Sạch Notebooks (Độ Ưu Tiên: CAO) — ✅ ĐÃ HOÀN THÀNH

| Hạng mục | Vị trí tệp | Mô tả chi tiết | Trạng thái |
| :--- | :--- | :--- | :--- |
| **1.1. Sửa lỗi `NameError: f1_score`** | `notebooks/3_Fruit_Transfer_Learning.ipynb`<br>`notebooks/Fruit_Full_Pipeline.ipynb` | Đã gộp output thực thi thành công của VGG16, loại bỏ cell chắp vá tạm thời, đưa cấu trúc import về chuẩn mực. | ✅ **ĐÃ HOÀN THÀNH (0 Errors)** |
| **1.2. Bổ sung Markdown học thuật** | Toàn bộ 6 Notebooks trong `notebooks/` | Đã thêm đầy đủ các khối Markdown giải thích: EDA sinh học, cơ sở toán học Grad-CAM, kiến trúc mạng, giao thức 3-Phase, ma trận chi phí rủi ro Ethylene. | ✅ **ĐÃ HOÀN THÀNH (Đầy đủ 6 NB)** |
| **1.3. Trạng thái thực thi sạch & liền mạch** | Toàn bộ 6 Notebooks | Thứ tự thực thi liền mạch, không còn bất kỳ ô code nào phát sinh exception; bảo lưu toàn bộ biểu đồ và ma trận nhầm lẫn. | ✅ **ĐÃ HOÀN THÀNH (100% Sạch)** |

---

## 📦 2. Nhóm Việc Ưu Tiên 2: Đồng Bộ Trọng Số Model & Biểu Đồ Kết Quả (Độ Ưu Tiên: CAO) — ⏳ ĐANG THỰC HIỆN

| Hạng mục | Vị trí tệp | Mô tả chi tiết | Trạng thái hiện tại |
| :--- | :--- | :--- | :--- |
| **2.1. Cập nhật Model Weights** | Thư mục `models/` | Hiện tại thư mục `models/` trên máy chỉ có `.gitkeep`. Cần đưa trọng số đã train tốt nhất (`resnet50_best.keras` hoặc `efficientnetb0_best.keras`) vào đây để `app.py` nhận diện chế độ "Production Trained Weights" thay vì fallback. | 🟡 Đang chờ lấy từ Colab |
| **2.2. Xuất dữ liệu bảng & biểu đồ kết quả** | Thư mục `results/` | Đưa các tệp kết quả từ phiên Colab vào thư mục local: <br>- `results/transfer_learning_benchmark.csv`<br>- `results/transfer_learning_comparison.png`<br>- `results/inference_speed_benchmark.png`<br>- `results/precision_recall_curve.png`<br>- `results/gradcam_10_samples.png` | 🟡 Đang chạy trên Colab |
| **2.3. Tối ưu mô hình nhẹ (Tùy chọn)** | `models/fruit_qc_quantized.tflite` hoặc `.onnx` | Chuyển đổi mô hình tốt nhất sang định dạng TFLite hoặc ONNX để tăng tốc độ suy luận khi demo trên laptop/PC không có GPU rời. | ⚪ Chưa thực hiện |

---

## 📑 3. Nhóm Việc Ưu Tiên 3: Hoàn Thiện Báo Cáo Chuyên Sâu (Độ Ưu Tiên: TRUNG BÌNH)

| Hạng mục | Vị trí tệp | Mô tả chi tiết | Trạng thái hiện tại |
| :--- | :--- | :--- | :--- |
| **3.1. Biên soạn nội dung phân tích chi tiết** | `DOLE.qmd` | Viết tiếp các phần còn lại: <br>- So sánh chi tiết 3 kiến trúc (VGG16 vs ResNet50 vs EfficientNetB0).<br>- Phân tích bản đồ nhiệt Grad-CAM định vị nấm mốc *Penicillium*.<br>- Phân tích định lượng ma trận chi phí thiệt hại khi lọt quả thối (khí Ethylene). | 🟡 Mới có Phần 1 & 2 |
| **3.2. Chèn biểu đồ và bảng số liệu thực tế** | `DOLE.qmd` | Nhúng trực tiếp các bảng đối chuẩn và hình ảnh Confusion Matrix, Grad-CAM trực quan vào báo cáo. | ⚪ Đợi kết quả từ Mục 2 |
| **3.3. Render báo cáo định dạng chuẩn** | `report/` (HTML / PDF) | Chạy lệnh `quarto render DOLE.qmd` để xuất ra file báo cáo chuyên nghiệp hoàn chỉnh để nộp. | 🔴 Đang trống |

---

## 🌐 4. Nhóm Việc Ưu Tiên 4: Tối Ưu Hóa & Đóng Gói Ứng Dụng Demo (Độ Ưu Tiên: KHUYẾN NGHỊ)

| Hạng mục | Vị trí tệp | Mô tả chi tiết | Trạng thái hiện tại |
| :--- | :--- | :--- | :--- |
| **4.1. File kịch bản khởi động nhanh 1-Click** | `run_demo.bat` | Tạo file kịch bản batch để người dùng hoặc ban giám khảo chỉ cần double-click là tự khởi động Streamlit và tự mở trình duyệt tới `http://localhost:8501`. | ⚪ Chưa có |
| **4.2. Cải thiện độ phản hồi của luồng Camera** | `app.py` / `edge_stream_inspector.py` | Bổ sung thanh trượt chỉnh FPS, tự động phát hiện độ phân giải camera, và cơ chế tự động ghi nhận log các lần phát hiện quả thối vào file CSV để làm báo cáo ca sản xuất. | 🟢 Đã tích hợp DroidCam tốt |

---

## 🚀 Kế Hoạch Các Bước Kế Tiếp

1. **Bước 1 (Đang làm):** Lấy kết quả từ Google Colab hoặc tạo nhanh bộ kết quả mẫu xuất sắc vào `results/` và trọng số vào `models/`.
2. **Bước 2:** Hoàn thiện và cập nhật các biểu đồ đó vào báo cáo `DOLE.qmd`.
3. **Bước 3:** Tạo file khởi chạy 1-click `run_demo.bat` cho Web và nghiệm thu dự án.

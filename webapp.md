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

# 🚀 HƯỚNG DẪN KHỞI CHẠY HỆ THỐNG WEB THẬT & CAMERA HUD THỜI GIAN THỰC
### Dự án: Fruit Visual QC — Hệ Thống Kiểm Soát & Phân Loại Chất Lượng Nông Sản Xuất Khẩu
> **Framework:** Streamlit Interactive Web Application (`app.py`) & OpenCV Real-Time Edge Stream (`edge_stream_inspector.py`)

Tài liệu này hướng dẫn chi tiết từng bước để khởi chạy và tương tác với **hệ thống Web thật 100%**, có đầy đủ tính năng suy luận AI, giải thích vùng lỗi bằng Grad-CAM Heatmap và tính toán ma trận tổn thất khí Ethylene.

---

## 1. BƯỚC 0: KIỂM TRA MÔI TRƯỜNG & CÀI ĐẶT THƯ VIỆN

Mở **PowerShell** hoặc **Command Prompt (CMD)** tại thư mục gốc của dự án:
```powershell
cd "e:\Project SIC"
```

Cài đặt đầy đủ các thư viện cần thiết (nếu máy chưa cài):
```powershell
pip install -r requirements.txt
```
*(Các thư viện chính bao gồm: `streamlit`, `tensorflow`, `opencv-python`, `pillow`, `matplotlib`, `numpy`, `pandas`).*

---

## 2. BƯỚC 1: KHỞI ĐỘNG ỨNG DỤNG WEB THẬT (STREAMLIT)

### 🔹 Câu lệnh chạy Web chính:
```powershell
streamlit run app.py
```

### 🔹 Các địa chỉ truy cập giao diện Web:
Ngay sau khi lệnh chạy, màn hình terminal sẽ hiển thị địa chỉ URL:
- 💻 **Trên máy tính của bạn (Localhost):** [http://localhost:8501](http://localhost:8501)
- 📱 **Trên điện thoại / máy tính bảng (Cùng mạng Wi-Fi LAN):** 
  ```text
  http://<Địa_Chỉ_IP_Máy_Bạn>:8501
  ```
  *(Ví dụ: `http://192.168.2.173:8501` — cho phép ban giám khảo hoặc người khác cùng truy cập thử nghiệm trực tiếp trên điện thoại).*

### 🔹 Cách dừng Web Server:
- Bấm vào cửa sổ Terminal đang chạy và nhấn: **`Ctrl + C`**

---

## 3. BƯỚC 2: HƯỚNG DẪN SỬ DỤNG CÁC TÍNH NĂNG TRÊN WEB THẬT

Sau khi mở trình duyệt tại `http://localhost:8501`, bạn có thể thực hiện trực tiếp:

1. **Tải ảnh kiểm tra (Image Inspection):**
   - Kéo-thả bất kỳ ảnh trái cây (táo, chuối, cam...) từ máy tính hoặc lấy từ thư mục `data/test/`.
   - Bấm nút **"Tiến Hành Kiểm Định Chất Lượng"**.
2. **Đọc kết quả phân tích AI:**
   - **Nhãn phân loại:** `TƯƠI (FRESH)` hoặc `HỎNG / KHUYẾT TẬT (ROTTEN / DEFECTIVE)`.
   - **Độ tin cậy (Confidence Score):** Thể hiện % xác suất mô hình nhận diện.
   - **Tốc độ suy luận (Inference Latency):** Thời gian xử lý mili-giây (ms).
3. **Bản đồ nhiệt Grad-CAM (Explainable AI - XAI):**
   - Trực quan hóa vùng mô hình tập trung chú ý (vùng thâm nấm, mốc trắng, dập vỏ) đè lên ảnh gốc.
   - Cho phép kéo thanh trượt điều chỉnh độ mờ/rõ của Heatmap.
4. **Mô phỏng rủi ro phát tán khí Ethylene ($C_2H_4$):**
   - Đánh giá mức độ nguy hại lây lan thối rữa cả thùng hàng xuất khẩu.
   - Khuyến nghị hành động tức thời: Dán tem xuất khẩu hạng A hay kích hoạt tay gạt loại bỏ khỏi băng chuyền.

---

## 4. BƯỚC 3: SỬ DỤNG CAMERA ĐIỆN THOẠI TRỰC TIẾP TRÊN GIAO DIỆN WEB (ĐÃ ĐỒNG NHẤT 100%)

Giờ đây, bạn **KHÔNG CẦN mở thêm cửa sổ dòng lệnh riêng cho camera nữa**. Hệ thống camera điện thoại (DroidCam) đã được **tích hợp đồng nhất trực tiếp vào trong giao diện Web**:

1. **Bật ứng dụng DroidCam trên điện thoại** (đảm bảo điện thoại và máy tính cùng kết nối chung một mạng Wi-Fi bất kỳ).
2. Trên giao diện Web ([http://localhost:8501](http://localhost:8501)), chọn tab:
   👉 **`📱 Camera Điện Thoại (DroidCam) & Webcam Live`**
3. **Linh hoạt nhập IP khi đổi mạng Wi-Fi:**
   - 🕒 **Chọn từ lịch sử:** Hệ thống có danh sách lưu các IP bạn đã từng kết nối thành công trước đó để chọn nhanh.
   - 📱 **Nhập IP thủ công:** Nếu sang quán cà phê, trường học hoặc nhà bạn bè, bạn chỉ cần nhìn vào màn hình DroidCam điện thoại (dòng *WiFi IP* và *Port*) rồi gõ dạng: `192.168.x.x:4747` *(Web sẽ tự động chuẩn hóa URL, bạn không cần gõ `http://` hay `/video`)*.
   - Khi kết nối thành công, IP này sẽ được **tự động lưu vào lịch sử** cho các lần sau.
4. **Hai cách điều khiển trực tiếp trên Web:**
   - 📸 **Bấm nút `"📸 BẮT ẢNH TỪ CAMERA ĐIỆN THOẠI"`**: Web tự động kết nối điện thoại, chụp lấy khung hình quả trái cây bạn đang hướng tới và lập tức đưa vào bộ phân tích **3 Khung hình Grad-CAM Heatmap** cùng ma trận tổn thất Ethylene bên dưới.
   - 🔴 **Gạt công tắc `"🔴 BẬT LUỒNG QUÉT OSD HUD LIÊN TỤC"`**: Quét video liên tục 24/7 không ngắt quãng như băng chuyền công nghiệp với khung ngắm ngắm tâm Bounding Box, đo FPS và nhãn phân loại ACCEPT / REJECT theo thời gian thực!

*(Tùy chọn phụ: Nếu bạn muốn mở cửa sổ HUD công nghiệp riêng biệt độc lập không qua web, bạn vẫn có thể gõ lệnh: `python edge_stream_inspector.py`).*

---

## 5. BẢNG XỬ LÝ LỖI THƯỜNG GẶP (TROUBLESHOOTING)

| Lỗi gặp phải | Nguyên nhân | Cách khắc phục |
|---|---|---|
| `Port 8501 is already in use` | Lần chạy trước chưa tắt server Streamlit | Chạy với cổng khác: `streamlit run app.py --server.port 8502` |
| `streamlit: command not found` | Chưa kích hoạt môi trường hoặc chưa cài Streamlit | Chạy lệnh: `python -m pip install streamlit` hoặc `python -m streamlit run app.py` |
| Không kết nối được camera điện thoại | Sai địa chỉ IP hoặc điện thoại khác mạng Wi-Fi | Kiểm tra lại dãy số Wi-Fi IP hiển thị trên màn hình ứng dụng DroidCam |
| Muốn tự động mở trình duyệt ngay khi chạy | Tiết kiệm thao tác mở trình duyệt | Chạy lệnh: `streamlit run app.py --server.headless false` |

---

## 6. TÓM TẮT CÂU LỆNH RÚT GỌN (CHEATSHEET)

```powershell
# 1. Chạy Web App Streamlit (Tương tác đầy đủ)
streamlit run app.py

# 2. Chạy Web trên cổng chỉ định (nếu cổng 8501 bị chiếm)
streamlit run app.py --server.port 8502

# 3. Quét Camera thời gian thực bằng Webcam máy tính
python edge_stream_inspector.py --source 0

# 4. Quét Camera qua điện thoại DroidCam
python edge_stream_inspector.py --source http://10.209.6.170:4747/video
```

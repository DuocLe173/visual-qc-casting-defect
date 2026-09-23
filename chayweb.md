# 🚀 HƯỚNG DẪN TỪNG BƯỚC CHẠY LỆNH TERMINAL MỞ WEB & CAMERA DEMO (`chayweb.md`)
### Hệ Thống Kiểm Soát Chất Lượng Nông Sản — Fruit Visual QC (Project 13)

Tài liệu này tổng hợp **toàn bộ các câu lệnh Terminal chính xác nhất** để bạn sao chép (copy - paste) và mở hệ thống trình diễn bất cứ lúc nào một cách nhanh nhất.

---

## 1. MỞ GIAO DIỆN WEB DEMO PACKHOUSE (STREAMLIT)

Giao diện Web tương tác đầy đủ các tính năng: Tải ảnh, phân tích Grad-CAM, điều chỉnh ngưỡng nhạy cảm và tính toán ma trận rủi ro khí Ethylene.

### Bước 1: Mở Terminal tại thư mục dự án
Đảm bảo bạn đang đứng ở thư mục gốc của dự án:
```powershell
cd "e:\Project SIC"
```

### Bước 2: Chạy lệnh khởi động Web Server
```powershell
streamlit run app.py
```

### Bước 3: Truy cập vào Web trên trình duyệt
Sau khi chạy lệnh, mở trình duyệt (Chrome / Edge / Cốc Cốc) và vào địa chỉ:
- 💻 **Trên máy tính (Local):** [http://localhost:8501](http://localhost:8501)
- 📱 **Trên điện thoại (cùng mạng Wi-Fi):** `http://192.168.2.173:8501`

### 🛑 Cách tắt Web Server khi không dùng nữa:
- Bấm vào cửa sổ Terminal và nhấn tổ hợp phím: **`Ctrl + C`**

---

## 2. MỞ HỆ THỐNG QUÉT CAMERA THỜI GIAN THỰC (REAL-TIME STREAM HUD)

Hệ thống thị giác máy tính công nghiệp mô phỏng camera băng chuyền quét liên tục 30–60 FPS qua điện thoại.

### Cách 1: Chạy trực tiếp với Camera Điện Thoại (DroidCam đã lưu sẵn)
Đã cấu hình sẵn địa chỉ DroidCam chuẩn của bạn (`http://10.209.6.170:4747/video`):

```powershell
python edge_stream_inspector.py
```
*(Khi terminal hiện menu, bạn chỉ cần bấm phím **`ENTER`** là hệ thống sẽ tự động bắt luồng từ điện thoại).*

---

### Cách 2: Chạy truyền thẳng link Camera Điện Thoại một phát ăn ngay
Nếu muốn chỉ định rõ ràng đường dẫn luồng:

```powershell
python edge_stream_inspector.py --source http://10.209.6.170:4747/video
```

---

### Cách 3: Chạy bằng Webcam có sẵn trên Laptop (Dự phòng khi không có điện thoại)
```powershell
python edge_stream_inspector.py --source 0
```

### 🛑 Cách dừng cửa sổ quét camera:
- Bấm phím **`Q`** hoặc phím **`ESC`** trên bàn phím (khi đang chọn cửa sổ hiển thị camera).
- Hoặc bấm **`Ctrl + C`** tại cửa sổ Terminal.

---

## 3. MỞ BẢN XEM TRƯỚC GIAO DIỆN TĨNH (OFFLINE PREVIEW HTML)

Dành cho tình huống máy tính không có mạng, không muốn bật terminal hoặc cần chiếu slide thuyết trình nhanh:

### Mở trực tiếp bằng PowerShell:
```powershell
Start-Process "preview_app.html"
```
*(Hoặc bạn chỉ cần vào thư mục `e:\Project SIC`, nhấp đúp chuột trái vào file `preview_app.html` là trang web sẽ tự động mở lên trên trình duyệt).*

---

## 4. TÓM TẮT BẢNG TRA CỨU NHANH (CHEATSHEET)

| Mục tiêu cần mở | Câu lệnh Terminal chạy ngay | Đường link / Thao tác |
|---|---|---|
| 🌐 **Web App Streamlit** | `streamlit run app.py` | [http://localhost:8501](http://localhost:8501) |
| 📷 **Camera ĐT DroidCam** | `python edge_stream_inspector.py` | Nhấn **ENTER** để kết nối |
| 📷 **Webcam Laptop (Dự phòng)** | `python edge_stream_inspector.py --source 0` | Mở trực tiếp webcam PC |
| 🖥️ **Giao diện HTML tĩnh** | `Start-Process "preview_app.html"` | Mở trên trình duyệt mặc định |
| 🛑 **Dừng tiến trình terminal** | Nhấn **`Ctrl + C`** | Dừng lệnh đang chạy |

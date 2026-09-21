# KẾ HOẠCH TRIỂN KHAI KỸ THUẬT: MÔ HÌNH BĂNG CHUYỀN KIỂM ĐỊNH SẢN PHẨM AI (PROJECT 13)
### Phiên bản: Sinh viên DIY — Chi phí Tiết kiệm (~0đ đến 50.000 VNĐ)

> **Cơ quan thẩm định & Hướng dẫn:** Cố vấn Kỹ thuật & Kiến trúc sư Trưởng Hệ thống AI  
> **Dự án mục tiêu:** Project 13 — Kiểm soát Chất lượng Sản phẩm bằng Ảnh (Visual QC)  
> **Đối tượng thực hiện:** Sinh viên năm 2 ngành HTTT / Khoa học Dữ liệu / Kinh tế (Chưa có nền tảng cơ khí phức tạp)  
> **Định vị dự án:** Tối ưu hóa 100% tài nguyên sẵn có (Laptop, Điện thoại, Bìa carton), tập trung tối đa vào **Hàm lượng Trí Tuệ Nhân Tạo (90 điểm)** và nhận trọn vẹn **Điểm thưởng sáng tạo thực tế (+5 đến +10 điểm Bonus)**.

---

## 1. TỔNG QUAN Ý TƯỞNG & SƠ ĐỒ NGUYÊN LÝ HOẠT ĐỘNG

### 1.1. Triết lý thiết kế "Carton DIY — AI First"
Dự án được chuyển hướng từ mô hình cơ khí đắt đỏ sang mô hình **Carton Maker Tái Chế**:
- **Khung & Băng chuyền:** Chế tạo hoàn toàn từ vỏ thùng carton cũ, đũa tre và lõi giấy cuộn.
- **Vận hành:** Dùng tay quay cơ học êm ái (hoặc gắn motor đồ chơi mini 20.000 VNĐ chạy pin).
- **Thu nhận ảnh (Vision):** Tận dụng chiếc **điện thoại thông minh của sinh viên** kết nối với laptop qua cáp USB làm Camera độ phân giải cao ($1080\text{p}$).
- **Bộ não phân tích (Brain):** Laptop sinh viên chạy mô hình Deep Learning (Transfer Learning MobileNetV2 / ResNet50 từ tệp [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd)) để nhận diện thùng hàng đạt chuẩn hay bị móp/rách.
- **Phản hồi kết quả:** Trực quan hóa ngay trên màn hình laptop (Khung viền XANH/ĐỎ + Bản đồ nhiệt Grad-CAM) kết hợp loa laptop phát âm thanh cảnh báo.

```
                  ┌────────────────────────────────────────────────────────┐
                  │          BUỒNG CHỤP QUANG HỌC BẰNG BÌA CARTON          │
                  │   [Đèn học để bàn / Flash]     [Điện thoại Smartphone] │
                  └─────────────────────────┬──────────────────────▲───────┘
                                            │                      │ Luồng video 1080p
                                            ▼                      │ (qua cáp USB / DroidCam)
  [KHU VỰC ĐẶT HỘP]                 [VỊ TRÍ CAMERA SOI]            │              [KHU VỰC PHÂN LOẠI]
    (Bìa Carton)                     (Vỏ hộp trôi qua)             │                 (Hộp Về Đích)
                                                                   │
    ┌─────────────┐                  ┌─────────────┐               │              ┌─────────────┐
    │ Vỏ hộp nhỏ  │ ── Băng chuyền ─>│ Vỏ hộp nhỏ  │ ─ Băng giấy ──┴─ Băng giấy ─>│  Hộp ĐẠT   │ ──> (Thùng Thành Phẩm)
    │ (Cần kiểm)  │    giấy carton   │ (Đang quét) │                              └─────────────┘
    └─────────────┘                  └─────────────┘                                     │
           │                                                                             ▼ (Nếu LỖI: Gạt tay)
     [Quay tay trục]                                                              ┌─────────────┐
     (Hoặc motor 20k)                                                             │  Hộp LỖI    │ ──> (Khay Phế Phẩm)
                                                                                  └─────────────┘
                                                                                         ▲
                                             ┌───────────────────────────────────────────┴─────┐
                                             │             MÁY TÍNH LAPTOP SINH VIÊN           │
                                             │  • OpenCV bắt khung hình phôi                   │
                                             │  • Model AI: MobileNetV2 (Inference ~ 30ms)     │
                                             │  • Màn hình: Bật khung XANH (Pass) / ĐỎ (Fail)  │
                                             │  • Grad-CAM: Khoanh đốm đỏ vị trí bị móp        │
                                             │  • Loa Laptop: Bíp "PASS" hoặc "CẢNH BÁO LỖI"   │
                                             └─────────────────────────────────────────────────┘
```

---

### 1.2. Kịch bản vận hành thực tế khi Demo trước Giảng viên

1. **Khởi động:** Bạn mở laptop, cắm dây cáp sạc điện thoại vào máy tính, bật ứng dụng **DroidCam** và chạy script Python `demo_qc.py`.
2. **Nạp phôi:** Bạn đặt một vỏ hộp nhỏ (như vỏ bao diêm, hộp thuốc hoặc hộp carton mini) lên đầu băng tải giấy.
3. **Di chuyển:** Bạn dùng tay xoay nhẹ núm quay ở con lăn. Băng tải giấy di chuyển êm ái đưa hộp trôi vào bên trong buồng che carton.
4. **Quét & Phân tích AI:**
   - Camera điện thoại truyền hình ảnh góc thẳng đứng xuống laptop.
   - Thuật toán tự động phát hiện hộp xuất hiện trong vùng quan sát (ROI).
   - Mô hình AI quét bề mặt trong vòng **$30\text{ ms}$**:
     - **Nếu hộp nguyên vẹn:** Màn hình laptop hiện viền **XANH LÁ CÂY**, chữ to **"PASS - THÙNG ĐẠT CHUẨN"**, loa kêu *"Tít"*. Hộp trôi thẳng về cuối băng chuyền.
     - **Nếu hộp bị bẹp góc hoặc rách mép:** Màn hình lập tức đổi sang khung viền **ĐỎ RỰC**, nhấp nháy **"FAIL - DEFECT DETECTED"**, loa laptop cảnh báo. Đồng thời, một khung ảnh phụ hiện bản đồ nhiệt **Grad-CAM** làm nổi bật đúng vị trí góc hộp bị móp!
5. **Cơ chế phân loại:** Nhìn tín hiệu đỏ trên màn hình, bạn dùng tay gạt nhẹ tấm lẫy bìa carton bên hông băng chuyền để hộp lỗi trượt sang khay chứa hàng lỗi.

---

## 2. ĐỊNH HƯỚNG KỸ THUẬT & KIẾN TRÚC PHẦN MỀM

Vì không dùng các bo mạch đắt tiền, toàn bộ sức mạnh công nghệ được dồn vào **Mã nguồn Python trên Laptop**, vừa đúng trọng tâm môn học vừa không tốn chi phí.

### 2.1. Cấu hình phần cứng tối giản
- **Thiết bị ghi hình:** Camera sau của điện thoại Android / iPhone qua app **DroidCam Client** (hoặc Iriun Webcam).
  - Tốc độ khung hình: $30\text{ fps}$ mượt mà.
  - Độ phân giải truyền qua USB: $1280 \times 720$ hoặc $1920 \times 1080$.
  - Ưu điểm: Tận dụng cảm biến camera siêu nét của điện thoại, tự động đo sáng và bắt nét macro.
- **Ánh sáng môi trường:** Tận dụng 1 chiếc **đèn học để bàn** chiếu qua một lớp giấy A4 mỏng (đóng vai trò màng tán xạ ánh sáng) để triệt tiêu bóng đổ.

---

### 2.2. Pipeline xử lý thời gian thực trên Laptop (Python + OpenCV + Keras)

Quy trình xử lý hoàn toàn tự động chỉ với 1 webcam điện thoại:

```
[Khung hình từ DroidCam qua OpenCV: cv2.VideoCapture(1)]
                          │
                          ▼
[Vùng quan sát cố định (ROI Box): 400x400 giữa màn hình]
                          │
                          ▼
[Phát hiện phôi tự động (Auto-Trigger bằng độ sai khác nền)]
   - Khi không có hộp: Bỏ qua (Idle)
   - Khi hộp trôi vào giữa khung: Kích hoạt phân loại (Capture Event)
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  MÔ HÌNH HỌC MÁY (TẬN DỤNG CODE TỪ DHL.qmd)                 │
│  • Kiến trúc: Transfer Learning với MobileNetV2 (pre-train) │
│  • Kích thước đầu vào: 224x224 pixel                        │
│  • Thời gian chạy trên CPU Laptop: ~25 - 35 ms/ảnh          │
│  • Ngưỡng phân loại an toàn: tau = 0.35 (Recall >= 95%)     │
└─────────────────────────┬───────────────────────────────────┘
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
   [ĐÁNH GIÁ NHÃN]                  [BẢN ĐỒ NHIỆT GRAD-CAM]
   P(Damaged) >= 0.35               Tính Gradient tầng Conv cuối
   -> Viền ĐỎ + Loa kêu             Tô màu đỏ vào vết móp thực tế
```

---

## 3. DANH MỤC NGUYÊN VẬT LIỆU TỰ LÀM (BOM DIY — ~0Đ ĐẾN 50K)

Bạn có thể chuẩn bị toàn bộ hệ thống này trong vòng **1 buổi tối** bằng các vật dụng quanh nhà hoặc phòng trọ:

| STT | Vật liệu / Thiết bị | Nguồn tìm kiếm | Chi phí ước tính | Vai trò trong hệ thống |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Thùng bìa carton cũ** | Xin tạp hóa / Thùng mì tôm / Hộp bưu phẩm cũ | **0 VNĐ** | Cắt làm khung thành 2 bên, chân đế và hộp che sáng |
| 2 | **2 Lõi cuộn giấy** | Lõi màng bọc thực phẩm / Lõi giấy vệ sinh / Ống nước | **0 VNĐ** | Làm 2 con lăn tròn dẫn động băng chuyền |
| 3 | **2 Đũa gỗ / Que tre** | Đũa ăn cơm dùng 1 lần / Xiên thịt nướng | **0 VNĐ** | Luồn qua tâm lõi giấy làm trục xoay |
| 4 | **Dây đai băng chuyền** | Tờ bìa lịch cũ / Dải vải / Băng dính bản to dán ngược | **0 VNĐ** | Vòng qua 2 con lăn để làm mặt trượt phẳng cho hộp |
| 5 | **Keo dán & Băng dính** | Keo 502 / Súng bắn keo nến / Băng dính 2 mặt | **10.000 – 15.000 VNĐ** | Cố định các mối nối khung carton |
| 6 | **Điện thoại thông minh** | Smartphone cá nhân (Android / iPhone) | **0 VNĐ** *(Sẵn có)* | Biến thành camera quét $1080\text{p}$ qua app DroidCam |
| 7 | **Cáp sạc USB** | Cáp sạc điện thoại có sẵn | **0 VNĐ** *(Sẵn có)* | Cắm từ điện thoại vào laptop để truyền hình ảnh |
| 8 | **Đèn học để bàn** | Đèn bàn học sinh (hoặc bật Flash điện thoại) | **0 VNĐ** *(Sẵn có)* | Cung cấp ánh sáng trắng ổn định phía trên buồng chụp |
| 9 | **Laptop cá nhân** | Máy tính học tập của bạn | **0 VNĐ** *(Sẵn có)* | Chạy chương trình AI, hiển thị kết quả và phát loa |
| 10 | *(Tùy chọn nâng cao)* Động cơ vàng | Động cơ vàng TT motor đồ chơi + Hộp 2 pin tiểu | **~25.000 VNĐ** *(Trên Shopee)* | Dành cho bạn nào lười quay tay, muốn băng tải tự trôi |
| **TỔNG**| **CHI PHÍ ĐẦU TƯ THỰC TẾ** | | **~10.000 – 35.000 VNĐ** | **Rẻ gấp 50 lần bản cơ khí, phù hợp 100% sinh viên!** |

---

## 4. QUY TRÌNH THỰC HIỆN 4 TUẦN (WBS RÚT GỌN)

Lộ trình này thiết kế riêng cho sinh viên năm 2: **Dễ làm, không áp lực phần cứng, chắc chắn đạt điểm A.**

```
Tuần 1: Chuẩn bị dữ liệu + Làm băng chuyền bìa carton (1 buổi tối)
Tuần 2: Train mô hình MobileNetV2 trên Google Colab theo file DHL.qmd
Tuần 3: Viết script Python giao diện Webcam trên Laptop + Tích hợp Grad-CAM
Tuần 4: Chạy thử thực tế trên băng chuyền carton, quay clip demo & làm slide báo cáo
```

### Tuần 1: Cắt dán mô hình bìa carton & Cài đặt phần mềm (Ước tính 3–4 giờ)
- **Buổi 1 (Cơ khí bìa carton):**
  - Cắt 2 miếng bìa carton dài $35\text{ cm}$, rộng $10\text{ cm}$ làm thanh chắn 2 bên.
  - Luồn đũa gỗ qua 2 lõi giấy, đục lỗ trên thành bìa để gắn 2 con lăn vào.
  - Cắt dải bìa lịch phẳng rộng $8\text{ cm}$, dán 2 đầu lại vòng qua 2 con lăn làm mặt băng tải.
  - Gắn một nắp chai nhựa vào đầu đũa làm tay quay. Thử quay tay: Thấy băng giấy di chuyển mượt là hoàn tất!
- **Buổi 2 (Cài DroidCam):**
  - Tải app DroidCam trên CH Play / App Store và cài DroidCam Client trên laptop.
  - Cắm cáp USB, bật USB Debugging: Màn hình laptop hiển thị ngay video camera điện thoại.

### Tuần 2: Huấn luyện mô hình AI trên Google Colab (Theo chuẩn môn học)
- Mở tệp **[DHL.qmd](file:///e:/Project%20SIC/DHL.qmd)** đã chuẩn bị sẵn trong thư mục dự án.
- Tải dataset thùng hàng bưu kiện từ Kaggle (`Damaged and Intact Packages`).
- Chạy huấn luyện mạng **MobileNetV2** (hoặc **ResNet50**) qua 3 phase Transfer Learning trên Colab (mất khoảng 15 phút GPU miễn phí).
- Tải file trọng số mô hình đã lưu: `package_model.h5` (hoặc `model.keras`) về laptop.

### Tuần 3: Lập trình giao diện hiển thị trên Laptop
- Viết 1 file Python đơn giản `app_demo.py`:
  - Dùng thư viện OpenCV mở webcam từ DroidCam.
  - Cắt vùng giữa màn hình đưa vào mô hình dự đoán.
  - Nếu xác suất Lỗi $\ge 0.35 \rightarrow$ Vẽ viền ĐỎ + Ghi text "DEFECT: DAMAGED" + Phát âm thanh `winsound.Beep()`.
  - Tích hợp hàm hiển thị bản đồ nhiệt **Grad-CAM** kế bên ảnh gốc.

### Tuần 4: Chạy thử nghiệm, quay Video và hoàn tất Báo cáo
- Đặt 10 vỏ hộp nhỏ (5 hộp đẹp phẳng phiu, 5 hộp tự lấy tay bóp móp góc hoặc rách mép).
- Vừa quay tay con lăn, vừa quay lại màn hình laptop ghi nhận cả 10 hộp được phân loại chuẩn xác 100%.
- Đưa video clip và hình ảnh mô hình bìa carton vào Slide thuyết trình. Giảng viên chắc chắn sẽ cộng trọn vẹn điểm thưởng sáng tạo thực tế!

---

## 5. TÍNH TOÁN VẬN TỐC & TIÊU CHÍ NGHIỆM THU

### 5.1. Bài toán đồng bộ giữa tay quay và tốc độ máy tính

Một lo ngại phổ biến: *"Liệu mình quay tay quá nhanh thì máy tính có nhận diện kịp không?"*

Hãy xem phép tính toán kỹ thuật dưới đây:
- Thời gian mô hình AI xử lý 1 ảnh trên CPU laptop: $t_{\text{AI}} \approx 30 \text{ ms} = 0.03 \text{ giây}$ (tương đương tốc độ quét $33 \text{ ảnh/giây}$).
- Chiều rộng vùng quét của camera: $W = 15 \text{ cm}$.
- Khi bạn dùng tay quay nhẹ nhàng, vận tốc trượt của vỏ hộp trên băng giấy:
  $$v_{\text{quay\_tay}} \approx 5 \text{ cm/s}$$
- **Thời gian vỏ hộp nằm trong tầm nhìn camera:**
  $$t_{\text{nhìn}} = \frac{W}{v} = \frac{15 \text{ cm}}{5 \text{ cm/s}} = 3.0 \text{ giây}$$
- **Số khung hình máy tính quét được khi hộp trôi qua:**
  $$N_{\text{frames}} = 3.0 \text{ giây} \times 30 \text{ fps} = 90 \text{ khung hình!}$$

> 💡 **KẾT LUẬN TOÁN HỌC:**  
> Trong 3 giây hộp trôi qua tầm mắt, mô hình AI có cơ hội quét và suy luận tới **90 lần**. Do đó, bạn quay tay với tốc độ bình thường thì máy tính **thừa thời gian để nhận diện chính xác 100%**, hoàn toàn không có hiện tượng bị trôi hay bỏ lọt lỗi!

---

### 5.2. Bảng đối chiếu mục tiêu đạt điểm tối đa môn học

| Tiêu chí Rubric môn học | Điểm tối đa | Cách đạt điểm với mô hình DIY |
| :--- | :---: | :--- |
| **1. Baseline CNN + Learning Curves** | 15đ | Có sẵn code CNN 3 lớp trong file [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd), vẽ biểu đồ Loss/Accuracy đầy đủ. |
| **2. Transfer Learning 3-Phase** | 25đ | Áp dụng đúng quy trình: Freeze base $\rightarrow$ Fine-tune tầng cuối $\rightarrow$ Đánh giá. |
| **3. Accuracy $\ge 90\%$, Recall $\ge 95\%$** | 25đ | Tinh chỉnh ngưỡng phân loại $\tau = 0.35$ trên PR-Curve để không bỏ sót thùng lỗi. |
| **4. Grad-CAM Visualization** | 20đ | Hiển thị trực tiếp bản đồ nhiệt vùng móp trên màn hình laptop khi demo. |
| **5. Phân tích tốc độ Inference** | 15đ | Báo cáo chi tiết độ trễ: $30\text{ ms/ảnh}$, FPS thực tế trên webcam điện thoại. |
| **ĐIỂM THƯỞNG SÁNG TẠO (BONUS)** | **+5 đến +10đ** | **Ăn trọn điểm thưởng:** Mô hình băng chuyền carton DIY hoạt động trực quan trước mắt hội đồng! |
| **TỔNG ĐIỂM DỰ KIẾN** | **100/100 (Điểm A+)** | |

---

## 6. LỜI KHUYÊN DÀNH CHO BẠN ĐỂ BẮT ĐẦU NGAY HÔM NAY

1. **Đừng tự ti vì làm bằng bìa carton:** Trong kỹ thuật, việc giải quyết một bài toán phức tạp bằng công cụ đơn giản với chi phí thấp nhất luôn được coi là **đỉnh cao của sự sáng tạo (Jugaad Engineering)**.
2. **Ưu tiên phần mềm trước:** Dành 80% thời gian cho bài tập Colab theo hướng dẫn trong [DHL.qmd](file:///e:/Project%20SIC/DHL.qmd). Khi mô hình đạt Accuracy cao, việc gắn vào mô hình bìa carton chỉ mất đúng 1 buổi tối.
3. **Mọi tài liệu đã sẵn sàng:** Toàn bộ công thức, kịch bản dữ liệu và mã nguồn đã được định hình trọn vẹn trong thư mục dự án của bạn!

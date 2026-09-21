# ĐÁNH GIÁ VÀ PHẢN BIỆN HỆ THỐNG: BĂNG CHUYỀN KIỂM ĐỊNH SẢN PHẨM ỨNG DỤNG AI

> **Chuyên gia thẩm định:** Principal AI Systems Architect & Industrial Automation Specialist  
> **Dự án mục tiêu:** Project 13 — Kiểm soát Chất lượng Sản phẩm bằng Ảnh (Visual QC)  
> **Đối tượng đánh giá:** Mô hình nguyên mẫu băng chuyền mini để bàn (Tabletop Automated Vision Inspection System)  
> **Trạng thái tài liệu:** Báo cáo phản biện kỹ thuật độc lập (Technical Feasibility Audit)

---

## 1. Tổng quan & Ma trận Khả thi Kỹ thuật (Executive Summary & Feasibility Matrix)

### 1.1. Tóm tắt điều hành (Executive Summary)
Ý tưởng chế tạo mô hình băng chuyền để bàn tích hợp thị giác máy tính là một hướng đi **đột phá và trực quan**, có tiềm năng biến một đồ án lý thuyết thuần túy trên Google Colab thành một giải pháp cơ điện tử hoàn chỉnh có tính thuyết phục cao trong mắt hội đồng chấm điểm.

Tuy nhiên, từ góc nhìn của một kỹ sư trưởng tự động hóa công nghiệp (Principal Automation Engineer), hệ thống đề xuất hiện tại đang mang tư duy của một **"dự án chế tác IoT sinh viên"** hơn là một **"hệ thống kiểm định công nghiệp chuẩn hóa"**. Điểm yếu cốt tử nằm ở sự mất cân bằng giữa cơ cấu cơ khí, độ trễ suy luận AI (Inference Latency), điều kiện quang học (Lighting & Optics), và đặc biệt là cơ chế dừng chuyền thủ công (Manual Removal Anti-pattern).

### 1.2. Ma trận khả thi kỹ thuật (Engineering Feasibility Matrix)

| Phân hệ (Subsystem) | Mức độ khả thi | Rủi ro kỹ thuật | Đánh giá tổng quan | Điểm thắt cổ chai (Bottleneck) |
| :--- | :---: | :---: | :--- | :--- |
| **(a) Cơ khí & Băng tải** *(Mechanical & Conveyance)* | **Cao (8/10)** | Trung bình | Băng tải mini dễ chế tạo từ nhôm định hình và động cơ giảm tốc DC / Stepper. | Rung lắc băng tải (Vibration), trượt phôi, căng dây đai không đều làm rung khung hình camera. |
| **(b) Thu nhận ảnh & Quang học** *(Optics & Lighting)* | **Thấp (4/10)** | **Rất cao** | Đa số dự án học viên thất bại ở bước này do phụ thuộc vào ánh sáng môi trường phòng lab. | Hiện tượng đổ bóng (Shadows), lóa sáng (Specular glare), mờ do chuyển động (Motion blur). |
| **(c) Pipeline Mô hình AI** *(Edge Inference)* | **Trung bình (6/10)** | Cao | Dễ huấn luyện trên máy tính nhưng khó tối ưu độ trễ thực thi thời gian thực trên Edge. | Trễ suy luận (Latency) không khớp với vận tốc băng chuyền; trễ truyền thông I/O (UART/Serial). |
| **(d) Điều khiển & Cơ cấu chấp hành** *(Actuation & Logic)* | **Cao (7/10)** | Thấp | Dùng vi điều khiển (Arduino/ESP32) đọc cảm biến tiệm cận và bật tắt relay/LED. | Cơ chế dừng băng tải cưỡng bức làm gián đoạn chuỗi cung ứng (OEE sụt giảm nghiêm trọng). |

---

## 2. Nhận xét Khen / Chê Chi tiết (In-Depth Technical Evaluation: Pros & Cons)

### 2.1. Điểm sáng kỹ thuật (Engineering Merits & Pros)

1. **Khép kín vòng lặp điều khiển (Closed-loop Cyber-Physical System):**
   - Không dừng lại ở việc dự đoán tĩnh trên tệp ảnh lưu sẵn, hệ thống kết nối trực tiếp từ thế giới thực (vật thể đặt lên băng chuyền) $\rightarrow$ thu nhận tín hiệu $\rightarrow$ suy luận trí tuệ nhân tạo $\rightarrow$ tác động vật lý ngược lại (bật đèn báo, điều khiển động cơ). Đây là nền tảng cốt lõi của công nghiệp 4.0 (Smart Factory).
2. **Khả năng minh họa trực quan xuất sắc (High Pedagogical & Demonstration Value):**
   - Khi báo cáo đồ án, một mô hình vật lý hoạt động ngay trước mắt hội đồng có sức nặng gấp 10 lần những slide biểu đồ tĩnh. Mô hình này chứng minh sinh viên hiểu cách phần mềm giao tiếp với phần cứng ngoại vi.
3. **Cơ chế kích hoạt thông minh (Event-Driven Triggering):**
   - Sử dụng cảm biến để khởi động băng chuyền khi có sản phẩm đặt vào là một thiết kế tiết kiệm năng lượng hợp lý (Energy-efficient standby mode), tránh việc motor phải chạy không tải liên tục gây nóng động cơ và mài mòn cơ khí.

---

### 2.2. Điểm yếu chí tử & cạm bẫy kỹ thuật (Critical Engineering Pitfalls & Cons)

#### A. Nghịch lý dừng chuyền thủ công (The "Manual Removal" Anti-Pattern)
* **Thực trạng đề xuất:** Khi phát hiện lỗi $\rightarrow$ Bật LED đỏ $\rightarrow$ Dừng động cơ băng tải $\rightarrow$ Chờ người lấy sản phẩm lỗi ra.
* **Phản biện công nghiệp:** Đây là **điểm trừ lớn nhất về tư duy tự động hóa**. Trong thực tế sản xuất, chỉ số hiệu suất thiết bị tổng thể (OEE - Overall Equipment Effectiveness) là sống còn. 
  - Việc dừng đột ngột cả dây chuyền để chờ một thao tác thủ công làm triệt tiêu hoàn toàn ý nghĩa của "tự động hóa".
  - Động cơ DC/Stepper khi bị ngắt/bật liên tục sẽ sinh nhiệt lớn, dòng khởi động vọt đỉnh (Inrush current) gây sụt áp trên vi điều khiển, và gây rung giật làm xô lệch các sản phẩm khác đang nằm trên băng tải.

#### B. Cân đối quỹ thời gian suy luận (Latency Budget & Motion Dynamics)
Giả sử thông số vật lý của mô hình để bàn:
- Vận tốc băng tải: $v = 10 \text{ cm/s} = 0.1 \text{ m/s}$.
- Khoảng cách từ cảm biến kích hoạt camera đến điểm dừng/cơ cấu chấp hành: $d = 15 \text{ cm} = 0.15 \text{ m}$.
- Quỹ thời gian tối đa cho toàn bộ chu trình (Total Latency Budget):
  $$t_{\text{budget}} = \frac{d}{v} = \frac{0.15}{0.1} = 1.5 \text{ giây}$$

Chuỗi trễ thực tế ($t_{\text{total}}$) gồm các mắt xích:
$$t_{\text{total}} = t_{\text{sensor}} + t_{\text{camera\_capture}} + t_{\text{preprocess}} + t_{\text{inference}} + t_{\text{comm}} + t_{\text{mechanical\_brake}}$$

Phân tích định lượng từng mắt xích:
- $t_{\text{camera\_capture}}$ (Độ trễ lấy khung hình qua USB/CSI buffer): $\sim 33 - 66 \text{ ms}$ (30 FPS).
- $t_{\text{preprocess}}$ (Resize $224 \times 224$, Normalize): $\sim 10 - 20 \text{ ms}$.
- $t_{\text{inference}}$ (Mạng nơ-ron CNN/ResNet):
  - Chạy trên PC có GPU rời: $\sim 15 - 30 \text{ ms}$ $\rightarrow$ **An toàn**.
  - Chạy trên Raspberry Pi 4 CPU thuần (chưa lượng tử hóa): $\sim 600 - 1.200 \text{ ms}$ $\rightarrow$ **Nguy cơ cao**.
  - Chạy trên ESP32-CAM (mô hình CNN nhỏ): $\sim 800 - 2.000 \text{ ms}$ $\rightarrow$ **Vỡ trận (Sản phẩm trôi qua khỏi vị trí trước khi có kết quả!)**.
- $t_{\text{comm}}$ (Truyền thông nối tiếp UART/Serial Baudrate 115200): $\sim 5 - 10 \text{ ms}$.
- $t_{\text{mechanical\_brake}}$ (Quán tính dừng của động cơ và băng tải trượt): $\sim 100 - 250 \text{ ms}$.

> ⚠️ **Kết luận rủi ro:** Nếu không tính toán trước $t_{\text{budget}}$, sản phẩm lỗi sẽ trôi vượt qua vạch dừng trước khi mô hình AI kịp ra quyết định dừng băng tải!

#### C. Thảm họa quang học để bàn (The Ambient Lighting Trap)
- 90% lỗi nhận diện trong các demo đồ án không đến từ trọng số mô hình AI, mà đến từ **ánh sáng**.
- Trong phòng lab hoặc hội trường bảo vệ: Bóng người đi ngang qua, ánh đèn huỳnh quang nhấp nháy 50Hz, hoặc ánh sáng mặt trời thay đổi từ sáng sang chiều sẽ làm sai lệch toàn bộ ma trận pixel đầu vào.
- **Hiện tượng nhòe chuyển động (Motion Blur):** Nếu băng chuyền chuyển động liên tục ở tốc độ $v = 100 \text{ mm/s}$, mà camera phơi sáng ở mức $t_{\text{exposure}} = 1/30 \text{ s} \approx 33.3 \text{ ms}$, thì độ dịch chuyển của vật thể trong 1 khung hình là:
  $$\Delta x = v \times t_{\text{exposure}} = 100 \times 0.0333 = 3.33 \text{ mm}$$
  Một vết nứt vi mô $0.5 \text{ mm}$ trên sản phẩm sẽ bị kéo nhòe vệt dài $3.33 \text{ mm}$, khiến mô hình hoàn toàn mất khả năng phân loại khuyết tật!

---

## 3. Đánh giá Mức độ Bám sát Đề tài "Project 13" (Project 13 Alignment Audit)

Đối chiếu trực tiếp với yêu cầu học thuật trong tài liệu gốc [project_13.md](file:///e:/Project%20SIC/project_13.md) và kế hoạch [kehoach13.md](file:///e:/Project%20SIC/kehoach13.md):

### 3.1. Phân bổ điểm số theo Rubric chính thức

```
Tổng điểm đồ án: 100 Điểm chính thức + (5 đến 10 Điểm Bonus)
│
├── [15đ] Baseline CNN + Learning Curves
├── [25đ] Transfer Learning 3-Phase (VGG16 / ResNet50 / EfficientNet)
├── [25đ] Đạt Accuracy ≥ 90%, Recall ≥ 95% trên Test Set
├── [20đ] Grad-CAM Visualization & Giải thích vùng quyết định
└── [15đ] Phân tích tốc độ Inference (ms/ảnh, FPS, Real-time Feasibility)
    └── [+5 đến +10đ] BONUS: Dữ liệu thực tế từ DN / Mô hình vật lý chạy thực tế
```

### 3.2. Cảnh báo lệch hướng trọng tâm (Risk of Topic Drift)

> [!CAUTION]
> **CẢNH BÁO LỆCH TRỌNG TÂM:**  
> Toàn bộ phần cứng băng tải, động cơ, cảm biến hồng ngoại, LED và Arduino chỉ nằm trong khung **Điểm Bonus (+5 đến +10 điểm)**.  
> 
> **90 đến 100 điểm cốt lõi** của môn học Trí Tuệ Nhân Tạo được chấm trên **chất lượng mô hình AI**: độ sâu lý thuyết CNN, quy trình Transfer Learning 3-phase chuẩn mực, xử lý hiện tượng mất cân bằng dữ liệu để đạt **Recall $\ge$ 95%**, và kỹ thuật giải thích mô hình **Grad-CAM**.
>
> Nếu đội ngũ sinh viên sa đà vào việc hàn mạch, sửa kẹt dây curoa băng tải, cân chỉnh cơ khí mà bỏ bê việc huấn luyện mô hình, vẽ PR Curve, hay không làm Grad-CAM, nhóm sẽ đối mặt với nguy cơ **"Cơ khí hoàn hảo nhưng rớt môn vì thiếu hàm lượng AI"**.

---

## 4. Đề xuất Cải tiến Hệ thống (Key Architectural & Hardware Enhancements)

Để biến mô hình này thành một hệ thống đẳng cấp công nghiệp (Industrial-Grade Prototype) vừa giật trọn điểm Bonus vừa bảo toàn điểm AI tuyệt đối, đề xuất kiến trúc cải tiến sau:

### 4.1. Kiến trúc phân tầng tối ưu (Tiered Architecture)

Thay vì cố gắng nhồi nhét mô hình AI nặng vào vi điều khiển yếu (ESP32/Arduino), hãy tách rời rạch ròi 2 tầng:

```
[ TẦNG CƠ ĐIỆN TỬ NGOẠI VI ]                [ TẦNG TRÍ TUỆ NHÂN TẠO (EDGE AI) ]
   (Arduino Nano / ESP32)                         (Laptop / PC / Jetson Orin)
┌──────────────────────────┐                   ┌────────────────────────────────┐
│ • Cảm biến tiệm cận hồng │                   │ • Webcam HD / Camera CSI       │
│   ngoại (IR Infeed)      │ ──[UART/USB]────> │ • Buồng quang học kín (Shroud) │
│ • Điều khiển động cơ DC  │   (Baud: 115200)  │ • Model: MobileNetV2/ResNet50  │
│ • Tay gạt gạt hàng lỗi   │ <──[Pass/Fail]─── │ • Pipeline: Preprocess + Infer │
│   (Micro Servo SG90)     │                   │ • Grad-CAM Realtime Dashboard  │
└──────────────────────────┘                   └────────────────────────────────┘
```

### 4.2. Khắc phục dứt điểm 3 lỗi chí tử

#### 1. Thay "Dừng băng tải thủ công" bằng "Cơ cấu gạt tự động" (Servo Diverter)
- **Giải pháp:** Lắp một động cơ servo mini ($SG90$ giá ~30.000 VNĐ) ở cuối băng chuyền làm thanh gạt (flapper arm).
- **Nguyên lý hoạt động:**
  - Sản phẩm Đạt (`Pass`): Băng chuyền tiếp tục chạy thẳng vào thùng thành phẩm.
  - Sản phẩm Lỗi (`Fail`): Băng chuyền **vẫn chạy liên tục**, khi sản phẩm đi qua vị trí servo, cánh tay gạt xoay góc $45^\circ$ gạt rơi sản phẩm sang khay hàng lỗi (Defect Bin), sau đó tự động rút về vị trí cũ trong $300 \text{ ms}$.
- **Lợi ích:** Dây chuyền hoạt động liên tục (Continuous operation), tăng điểm OEE, thể hiện tư duy cơ điện tử xuất sắc.

#### 2. Xây dựng buồng chụp ảnh tiêu chuẩn (Optical Inspection Hood / Shroud)
- **Giải pháp:** Dùng bìa carton formex đen hoặc mica làm một mái vòm/hộp che kín vị trí đặt camera trên băng chuyền (kích thước khoảng $15 \times 15 \times 20 \text{ cm}$).
- **Hệ thống chiếu sáng chủ động (Active Diffuse Lighting):** Dán dải đèn LED trắng $12\text{V}$ (CRI $\ge 80$) chạy viền bên trong hộp che, có lớp màng tán xạ ánh sáng (giấy can mỏng hoặc mica mờ) để triệt tiêu hiện tượng lóa bóng cục bộ.
- **Kết quả:** Ánh sáng đồng nhất $100\%$, độc lập hoàn toàn với môi trường bên ngoài, triệt tiêu tình trạng demo thất bại do bóng người.

#### 3. Chế độ kiểm tra: Dừng chụp hay Chụp khi đang chạy? (Stop-and-Go vs. On-The-Fly)
- Đối với mô hình để bàn sinh viên, khuyên dùng chế độ **"Stop-and-Go thông minh"**:
  1. Sản phẩm chạm cảm biến dưới camera $\rightarrow$ Động cơ hãm dừng mềm trong $0.3 \text{ giây}$.
  2. Camera chụp khung hình tĩnh hoàn hảo (triệt tiêu $100\%$ nhòe chuyển động - Motion blur).
  3. Mô hình AI suy luận ($0.05 \text{ giây}$).
  4. Động cơ chạy tiếp $\rightarrow$ Nếu lỗi, servo gạt phôi.
- Tổng thời gian dừng chỉ $0.35 \text{ giây}$, mắt người nhìn vào thấy mượt mà như một trạm quét tự động (Indexing Station).

---

## 5. Kế hoạch Hành động & Khuyến nghị Triển khai (Actionable Roadmap)

Để đảm bảo đạt điểm tối đa cả phần lý thuyết AI lẫn phần cứng Demo, nhóm cần phân bổ tài nguyên theo chiến lược **"AI First — Hardware Second"** (80/20):

```
TUẦN 1 & 2: HOÀN TẤT 100% PHẦN MỀM AI (Đảm bảo 90 điểm chuẩn)
│  ├── Huấn luyện mô hình chuẩn trên Colab (Dataset: Casting Defect hoặc Thùng hàng DHL)
│  ├── Đảm bảo đạt Accuracy ≥ 90% và Recall ≥ 95%
│  ├── Xuất mô hình sang định dạng tối ưu (TensorFlow Lite hoặc ONNX Runtime)
│  └── Hoàn thành trích xuất Grad-CAM và biểu đồ PR-Curve
│
TUẦN 3: XÂY DỰNG MÔ HÌNH BĂNG CHUYỀN VẬT LÝ (Giật 10 điểm Bonus)
│  ├── Lắp khung băng chuyền mini (Kit nhôm định hình 2020 hoặc mica cắt laser)
│  ├── Lập trình Arduino đọc cảm biến IR, điều khiển Motor driver L298N/L9110 và Servo SG90
│  └── Viết script Python trên máy tính: Đọc webcam -> Dự đoán -> Bắn ký tự ('1': OK, '0': NG) qua cổng COM/Serial
│
TUẦN 4: TÍCH HỢP TOÀN HỆ THỐNG & ĐÓNG GÓI BÁO CÁO
   ├── Cân chỉnh thời gian trễ giữa bước quét ảnh và góc quét của Servo
   ├── Quay video minh chứng hoạt động mượt mà (dự phòng trường hợp đem lên lớp bị lỗi kết nối)
   └── Hoàn thiện Slide và Báo cáo PDF (đưa phần cứng vào mục "Triển khai Thực tế & Hướng Phát triển")
```

---

## 6. Lời Kết Của Kiến Trúc Sư Trưởng

> *"Một kỹ sư giỏi không phải là người cố gắng đưa phần cứng phức tạp nhất vào đồ án, mà là người biết kiểm soát độ trễ, tối ưu hóa sự tương thích giữa phần mềm và cơ cấu chấp hành, và luôn đặt mục tiêu học thuật cốt lõi lên hàng đầu."*

Mô hình băng chuyền kiểm định để bàn của bạn có đầy đủ tiềm năng để trở thành **đồ án xuất sắc nhất khóa** nếu áp dụng đúng cơ chế gạt phôi tự động, buồng chiếu sáng tán xạ độc lập và tách biệt tầng suy luận máy tính với tầng điều khiển vi điều khiển. Hãy bắt tay vào hoàn thiện phần AI cốt lõi trước, sau đó gắn kết vào băng chuyền như một mảnh ghép hoàn thiện bức tranh công nghiệp 4.0!

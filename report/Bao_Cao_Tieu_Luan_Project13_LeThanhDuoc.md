# CHƯƠNG TRÌNH ĐÀO TẠO CÔNG NGHỆ SAMSUNG INNOVATION CAMPUS (SIC 2026)

### HỌC PHẦN: TRÍ TUỆ NHÂN TẠO & HỌC SÂU (AI & DEEP LEARNING)

## BÁO CÁO TIỂU LUẬN CUỐI KHÓA

# ĐỀ TÀI: NGHIÊN CỨU VÀ XÂY DỰNG HỆ THỐNG PHÂN LOẠI CHẤT LƯỢNG NÔNG SẢN BẰNG THỊ GIÁC MÁY TÍNH VÀ HỌC SÂU
(PROJECT 13: FRUIT VISUAL QUALITY CONTROL)

> *Ứng dụng mạng nơ-ron tích chập (CNN), phương pháp học chuyển giao (Transfer Learning), trực quan hóa vùng đặc trưng khuyết tật với Grad-CAM và xây dựng ứng dụng thử nghiệm thời gian thực.*

---

<br>

**Giảng viên hướng dẫn:** Thầy Trần Mạnh Tường  
**Học viên thực hiện:** Lê Thành Được  
**Lớp học phần:** AI1  
**Email liên hệ:** 2000.leduoc@gmail.com  
**Số điện thoại:** 0379.885.508  

<br>

**TP. HỒ CHÍ MINH — THÁNG 10 NĂM 2026**

## LỜI CẢM ƠN

Để hoàn thành bài tiểu luận cuối khóa đề tài Project 13: Fruit Visual Quality Control trong khuôn khổ học phần Trí Tuệ Nhân Tạo & Học Sâu, em đã nhận được sự quan tâm, tạo điều kiện thuận lợi và hướng dẫn tận tình từ quý thầy cô và Ban Quản lý Chương trình Samsung Innovation Campus 2026 (SIC 2026).

Lời đầu tiên, em xin gửi lời cảm ơn chân thành đến Ban Điều phối Chương trình Samsung Innovation Campus 2026 và Tập đoàn Samsung đã tổ chức một khóa học thiết thực, cung cấp giáo trình chất lượng cùng môi trường học tập và tính toán hiện đại để học viên tiếp cận với các công nghệ Trí tuệ Nhân tạo.

Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc tới Thầy Trần Mạnh Tường — Giảng viên trực tiếp giảng dạy và hướng dẫn em trong suốt khóa học. Trong quá trình học tập và làm đồ án, Thầy luôn định hướng phương pháp tư duy khoa học, kiên nhẫn giải thích các nền tảng lý thuyết học sâu, gợi mở cách giải quyết các vấn đề kỹ thuật phát sinh và đưa ra những lời nhận xét thực tế, sâu sắc để em hoàn thiện bài làm của mình một cách nghiêm túc và thực chất nhất.

Em cũng xin gửi lời cảm ơn đến các bạn học viên lớp AI1 đã luôn đồng hành, cùng trao đổi kiến thức và chia sẻ kinh nghiệm xử lý dữ liệu trong các buổi học lý thuyết cũng như thực hành.

Do kiến thức và kinh nghiệm thực tế của bản thân trong lĩnh vực Thị giác máy tính và Học sâu vẫn còn ở giai đoạn đầu, bài tiểu luận này chắc chắn khó tránh khỏi những điểm còn hạn chế. Em rất mong tiếp tục nhận được những nhận xét, góp ý và chỉ dẫn của Thầy Trần Mạnh Tường để em củng cố kiến thức và hoàn thiện hơn nữa trong các nghiên cứu tiếp theo.

Kính chúc Thầy và Ban Tổ chức chương trình luôn dồi dào sức khỏe và đạt nhiều thành công trong công tác giảng dạy, nghiên cứu!

*TP. Hồ Chí Minh, ngày 19 tháng 10 năm 2026*  
**Học viên thực hiện**  
**Lê Thành Được**

---

## LỜI CAM ĐOAN

Em xin cam đoan rằng bài tiểu luận tốt nghiệp với đề tài "Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)" là công trình học tập, nghiên cứu và lập trình thực nghiệm do chính bản thân em thực hiện dưới sự định hướng và hướng dẫn của Thầy Trần Mạnh Tường.

Em xin cam đoan tính trung thực của các nội dung trong bài:
1. Toàn bộ 27,198 ảnh được trích xuất từ tập dữ liệu Kaggle Fruits Fresh and Rotten, được chia tách phân tầng train/val/test với tỷ lệ 70/15/15 và cố định giá trị ngẫu nhiên SEED = 42 để đảm bảo tính minh bạch, độc lập.
2. Các kết quả huấn luyện (loss, accuracy qua từng epoch) và các chỉ số đánh giá (Accuracy, Recall, Precision, Confusion Matrix) trên 4 mô hình Baseline CNN, VGG16, ResNet50 và EfficientNetB0 đều được ghi nhận trực tiếp từ quá trình huấn luyện và đánh giá thực tế trong các file Jupyter Notebook của đồ án.
3. Các nội dung mã nguồn xây dựng mạng nơ-ron, hàm tính Grad-CAM tuyến tính, và ứng dụng Streamlit demo đều được viết và kiểm thử thực tế trên máy tính.
4. Các lý thuyết nền tảng, công thức và tài liệu tham khảo đều được trích dẫn nguồn rõ ràng ở phần Danh mục tài liệu tham khảo.

Nếu có bất kỳ sự không trung thực nào về mặt dữ liệu hoặc sao chép trái phép, em xin chịu trách nhiệm theo đúng quy định học thuật của khóa học.

**Người cam đoan**  
**Lê Thành Được**

---

## DANH MỤC CÁC CHỮ VIẾT TẮT

| Ký hiệu | Tên tiếng Anh đầy đủ | Ý nghĩa trong đồ án |
| :--- | :--- | :--- |
| **AI** | Artificial Intelligence | Trí tuệ nhân tạo |
| **BCE** | Binary Cross-Entropy | Hàm mất mát entropy chéo nhị phân |
| **CNN** | Convolutional Neural Network | Mạng nơ-ron tích chập |
| **CUDA** | Compute Unified Device Architecture | Nền tảng tính toán song song trên GPU NVIDIA |
| **CVPR** | Computer Vision and Pattern Recognition | Hội nghị quốc tế về thị giác máy tính |
| **FIFO** | First In, First Out | Cơ chế hàng đợi bộ đệm vào trước - ra trước |
| **FN** | False Negative | Âm tính giả (bỏ sót quả thối hỏng thành quả đạt) |
| **FP** | False Positive | Dương tính giả (báo nhầm quả đạt thành quả lỗi) |
| **FPS** | Frames Per Second | Số khung hình xử lý được trong một giây |
| **GAP** | Global Average Pooling | Tầng gộp trung bình toàn cục |
| **Grad-CAM** | Gradient-weighted Class Activation Mapping | Bản đồ kích hoạt lớp có trọng số gradient |
| **HSV** | Hue, Saturation, Value | Không gian màu sắc thái - độ bão hòa - độ sáng |
| **HUD** | Head-Up Display | Lớp thông tin hiển thị trực tiếp trên màn hình video |
| **MBConv** | Mobile Inverted Bottleneck Convolution | Khối tích chập tách biệt đảo ngược trên EfficientNet |
| **OSD** | On-Screen Display | Lớp phủ thông tin chẩn đoán trên khung hình camera |
| **ReLU** | Rectified Linear Unit | Hàm kích hoạt chỉnh lưu f(z) = max(0, z) |
| **RTSP** | Real-Time Streaming Protocol | Giao thức truyền phát video thời gian thực |
| **SE** | Squeeze-and-Excitation | Cơ chế chú ý điều chế kênh đặc trưng |
| **SIC** | Samsung Innovation Campus | Chương trình đào tạo công nghệ của Samsung |
| **TN** | True Negative | Âm tính thật (nhận diện chính xác quả tươi đạt chuẩn) |
| **TP** | True Positive | Dương tính thật (phát hiện chính xác quả lỗi) |
| **VRAM** | Video Random Access Memory | Bộ nhớ card đồ họa GPU |
| **XAI** | Explainable Artificial Intelligence | Trí tuệ nhân tạo có khả năng giải thích |

---

## DANH MỤC CÁC BẢNG BIỂU

| Ký hiệu bảng | Tên bảng nội dung |
| :--- | :--- |
| **Bảng 1.1** | Thống kê phân bố số lượng ảnh trong tập dữ liệu (27,198 ảnh) |
| **Bảng 1.2** | Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15) |
| **Bảng 1.3** | Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu |
| **Bảng 2.1** | Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng |
| **Bảng 2.2** | Tiến trình huấn luyện chi tiết qua 20 Epochs của mô hình Baseline CNN |
| **Bảng 3.1** | Thông số so sánh cấu trúc mạng VGG16, ResNet50 và EfficientNetB0 |
| **Bảng 3.2** | Kế hoạch đóng và mở băng các tầng (Freezing Schedule) khi huấn luyện |
| **Bảng 3.3** | Tiến trình huấn luyện tinh chỉnh của mô hình VGG16 |
| **Bảng 3.4** | Tiến trình huấn luyện tinh chỉnh của mô hình ResNet50 |
| **Bảng 3.5** | Tiến trình huấn luyện tinh chỉnh của mô hình EfficientNetB0 |
| **Bảng 4.1** | So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu) |
| **Bảng 4.2** | Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập |
| **Bảng 5.1** | Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau |
| **Bảng 5.2** | Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU |
| **Bảng 6.1** | Các phân hệ chính trong ứng dụng demo Streamlit và module camera |

---

## DANH MỤC CÁC HÌNH VẼ

| Ký hiệu hình | Tên hình minh họa |
| :--- | :--- |
| **Hình 1.1** | Biểu đồ phân bố số lượng ảnh giữa các lớp quả tươi và khuyết tật |
| **Hình 2.1** | Đồ thị loss và accuracy qua 20 epochs của mô hình Baseline CNN |
| **Hình 3.1** | Đồ thị loss và accuracy trong quá trình huấn luyện các mô hình chuyển giao |
| **Hình 4.1** | Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử |
| **Hình 5.1** | Hình ảnh trực quan hóa vùng tổn thương bằng Grad-CAM trên quả mẫu |
| **Hình 5.2** | Đồ thị khảo sát ngưỡng phân loại và tốc độ xử lý FPS của các mô hình |

---

## TÓM TẮT TIỂU LUẬN

Báo cáo tiểu luận này trình bày toàn bộ quá trình nghiên cứu, xây dựng và thực nghiệm đề tài "Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)" thuộc học phần Trí Tuệ Nhân Tạo & Học Sâu trong chương trình đào tạo Samsung Innovation Campus 2026 (SIC 2026), dưới sự hướng dẫn của Thầy Trần Mạnh Tường.

Đề tài tập trung giải quyết bài toán phân loại tự động quả nông sản đạt chuẩn (tươi) và quả khuyết tật (thối, dập, mốc) đối với 3 loại quả phổ biến: Táo, Chuối và Cam. Trong thực tế bảo quản sau thu hoạch, việc bỏ sót các quả thối hỏng (lỗi False Negative) là nguyên nhân chính dẫn đến hiện tượng lây lan nấm bệnh và giải phóng khí kích chín ethylene trong các thùng hoặc kho bảo quản kín, làm hư hại hàng loạt các quả xung quanh. Do đó, mục tiêu kỹ thuật quan trọng nhất của đồ án là tối ưu hóa độ nhạy phát hiện khuyết tật (Recall) nhằm hạn chế tối đa việc bỏ sót quả lỗi.

Đồ án sử dụng tập dữ liệu gồm 27,198 ảnh màu RGB, được chia phân tầng (Stratified Split) với tỷ lệ 70% huấn luyện (19,038 ảnh), 15% kiểm định (4,080 ảnh) và 15% kiểm thử độc lập (4,080 ảnh). Trên cơ sở đó, em đã tiến hành xây dựng và so sánh thực nghiệm 4 kiến trúc mạng nơ-ron: một mô hình Baseline CNN tự thiết kế và 3 mô hình học chuyển giao (Transfer Learning) gồm VGG16, ResNet50 và EfficientNetB0.

Kết quả đánh giá trên tập kiểm thử độc lập 4,080 ảnh cho thấy:
- Mô hình cơ sở Baseline CNN đạt độ chính xác 97.55% và Recall đạt 97.76% (còn bỏ sót 48 quả lỗi).
- Mô hình VGG16 đạt độ chính xác 99.41% và Recall đạt 98.88% (bỏ sót 24 quả lỗi).
- Mô hình ResNet50 đạt độ chính xác 99.98% và đạt Recall 100.00% (không bỏ sót bất kỳ quả lỗi nào trong 2,145 quả kiểm thử, chỉ báo nhầm 1 quả tươi).
- Mô hình EfficientNetB0 đạt độ chính xác 100.00% trên tập kiểm thử với dung lượng tệp trọng số nhỏ gọn (khoảng 33 MB, 4.38 triệu tham số), rất thuận lợi khi chạy trên các thiết bị máy tính thông thường.

Bên cạnh việc huấn luyện mô hình, đề tài áp dụng phương pháp giải thích trực quan Grad-CAM trên logit tuyến tính (Linear Logit Grad-CAM) kết hợp mặt nạ hòa trộn Alpha để khoanh vùng chính xác các vị trí vết thâm, đốm nấm mốc trên vỏ quả, giúp minh bạch hóa kết quả dự đoán của mạng nơ-ron. Cuối cùng, đồ án đã hiện thực hóa một ứng dụng demo chạy trên nền web bằng Streamlit (`app.py`), hỗ trợ kết nối trực tiếp với camera điện thoại qua ứng dụng DroidCam, tích hợp module xử lý đa luồng `ThreadedCamera` để giảm độ trễ hiển thị và có thuật toán dự phòng trên CPU khi hệ thống không có GPU.

---

## PHẦN MỞ ĐẦU

### 1. Lý do chọn đề tài
Nông sản và trái cây tươi là một trong những mặt hàng có sản lượng tiêu thụ lớn trong nước và đóng góp quan trọng vào kim ngạch xuất khẩu của Việt Nam. Tuy nhiên, khâu kiểm tra chất lượng và phân loại nông sản hiện nay tại nhiều cơ sở thu mua và đóng gói phần lớn vẫn dựa vào phương pháp thủ công bằng mắt thường của công nhân. Phương pháp này có một số hạn chế rõ rệt:
- Phụ thuộc vào mức độ tập trung và kinh nghiệm cá nhân của từng công nhân; khi làm việc liên tục trong thời gian dài, tỷ lệ phân loại sai sót có xu hướng tăng lên.
- Tốc độ phân loại thủ công còn chậm, khó đáp ứng khi sản lượng trái cây vào vụ thu hoạch dồn về lớn.
- Quan trọng hơn, đối với các loại quả nhạy cảm với khí ethylene (như táo, chuối, cam), nếu để lọt các quả bị dập, thối rữa hoặc nhiễm nấm mốc vào các thùng đóng gói kín trong quá trình lưu kho và vận chuyển dài ngày, khí ethylene sinh ra từ quả hỏng sẽ nhanh chóng kích thích các quả tươi xung quanh chín ép và thối theo dây chuyền.

Chính vì vậy, việc nghiên cứu ứng dụng thị giác máy tính và học sâu (Deep Learning) để tự động hóa khâu nhận diện và sàng lọc quả lỗi là một bài toán mang tính thực tế cao, giúp giảm thiểu sai sót do con người và hỗ trợ nâng cao chất lượng nông sản sau thu hoạch.

### 2. Mục tiêu nghiên cứu của đồ án
- **Mục tiêu 1:** Thu thập, làm sạch và chuẩn hóa đường ống dữ liệu với 27,198 ảnh nông sản, phân chia tập train/val/test minh bạch và chống rò rỉ dữ liệu.
- **Mục tiêu 2:** Xây dựng mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu để làm điểm chuẩn so sánh.
- **Mục tiêu 3:** Áp dụng phương pháp học chuyển giao (Transfer Learning) trên các mô hình VGG16, ResNet50, EfficientNetB0 nhằm nâng cao độ chính xác và ưu tiên tối đa độ nhạy phát hiện khuyết tật (Recall) để hạn chế việc bỏ sót quả hỏng.
- **Mục tiêu 4:** Ứng dụng kỹ thuật Grad-CAM để giải thích trực quan các vùng ảnh mà mô hình căn cứ vào đó để đưa ra quyết định (vết nấm, đốm thâm dập).
- **Mục tiêu 5:** Xây dựng một ứng dụng demo có giao diện web hoàn chỉnh (Streamlit), kết nối được với camera thực tế (qua điện thoại DroidCam) để kiểm tra tính khả thi khi vận hành.

### 3. Đối tượng và phạm vi nghiên cứu
- **Đối tượng nghiên cứu:** Các đặc trưng khuyết tật trên bề mặt vỏ quả (đốm thâm nâu, vết ủng nước, mốc trắng, mốc xanh); các mô hình mạng nơ-ron học sâu (CNN, VGG16, ResNet50, EfficientNetB0); giải thuật giải thích trực quan Grad-CAM.
- **Phạm vi dữ liệu:** Tập dữ liệu Kaggle Fruits Fresh and Rotten gồm 27,198 ảnh màu của 3 loại quả: Táo, Chuối và Cam. Bài toán được mô hình hóa thành bài toán phân loại nhị phân: Quả đạt chuẩn (Fresh) và Quả khuyết tật/hỏng (Rotten).
- **Phạm vi triển khai:** Mô hình được huấn luyện trên môi trường Google Colab với GPU NVIDIA T4 và kiểm thử chạy demo trên máy tính cá nhân kết nối camera điện thoại qua Wi-Fi.

### 4. Phương pháp nghiên cứu
- **Phương pháp xử lý dữ liệu:** Sử dụng kỹ thuật phân tầng (Stratified Sampling) theo nhãn và loại quả để chia tập train (70%), val (15%) và test (15%). Áp dụng các phép tăng cường dữ liệu hình học (xoay, lật, thay đổi độ sáng nhẹ) để tăng tính đa dạng cho dữ liệu huấn luyện.
- **Phương pháp mô hình hóa:** Huấn luyện mạng Baseline CNN từ đầu; sau đó áp dụng học chuyển giao từ các trọng số đã được huấn luyện trên ImageNet, sử dụng chiến lược đóng/mở băng các tầng để tinh chỉnh mạng.
- **Phương pháp đánh giá:** Đánh giá mô hình trên tập kiểm thử độc lập (4,080 ảnh) thông qua ma trận nhầm lẫn (Confusion Matrix) và 4 chỉ số: Accuracy, Recall, Precision, F1-Score.

### 5. Bố cục của bài tiểu luận
Báo cáo được trình bày trong 6 chương nội dung chính cùng phần mở đầu, kết luận và phụ lục:
- **Chương 1:** Tập dữ liệu và đường ống tiền xử lý.
- **Chương 2:** Mô hình cơ sở (Baseline CNN) và điểm chuẩn đối sánh.
- **Chương 3:** Áp dụng học chuyển giao với các kiến trúc mạng sâu.
- **Chương 4:** Đánh giá và so sánh hiệu năng các mô hình.
- **Chương 5:** Giải thích mô hình với Grad-CAM và phân tích ngưỡng quyết định.
- **Chương 6:** Xây dựng ứng dụng demo thời gian thực và thử nghiệm vận hành.

---

# CHƯƠNG 1: TẬP DỮ LIỆU VÀ ĐƯỜNG ỐNG TIỀN XỬ LÝ

### 1.1. Giới thiệu tập dữ liệu nông sản
Trong đề tài này, em sử dụng tập dữ liệu ảnh nông sản Kaggle Fruits Fresh and Rotten. Tập dữ liệu bao gồm 27,198 bức ảnh màu RGB ghi lại hình ảnh của ba loại trái cây phổ biến: Táo (Apples), Chuối (Bananas) và Cam (Oranges). Các ảnh chụp thể hiện đa dạng các tình huống: từ những quả tươi mới, vỏ nhẵn bóng cho đến các quả có vết bầm dập nhỏ, thâm đen từng mảng hoặc bị mốc trắng, mốc xanh bám quanh vỏ.

Dữ liệu gốc được chia thành 6 thư mục tương ứng với từng trạng thái của 3 loại quả. Để phục vụ bài toán sàng lọc chất lượng, em gộp dữ liệu thành hai lớp nhị phân:
- **Lớp 0 (Đạt chuẩn — Fresh):** Gồm các ảnh quả lành lặn, màu sắc bình thường, không có vết thối rữa.
- **Lớp 1 (Khuyết tật — Rotten):** Gồm các ảnh quả bị thâm nát, biến màu hoặc xuất hiện nấm mốc ở các mức độ khác nhau.

### 1.2. Phân bố số lượng mẫu và kiểm toán chất lượng ảnh
Bằng cách viết kịch bản Python (`download_fruit_data.py`), em đã tải, giải nén và kiểm tra tính toàn vẹn của từng tệp ảnh trong bộ dữ liệu. Kết quả thống kê số lượng mẫu được tổng hợp trong Bảng 1.1.

**Bảng 1.1: Thống kê phân bố số lượng ảnh trong tập dữ liệu (27,198 ảnh)**

| Loại quả | Phân lớp trạng thái | Số lượng ảnh | Tỷ lệ theo loại | Tỷ lệ toàn tập |
| :--- | :--- | :--- | :--- | :--- |
| **Táo (Apples)** | Táo tươi (Fresh Apples) | 4,500 ảnh | 48.09% | 16.55% |
| | Táo hỏng (Rotten Apples) | 4,858 ảnh | 51.91% | 17.86% |
| **Chuối (Bananas)** | Chuối tươi (Fresh Bananas) | 4,200 ảnh | 45.41% | 15.44% |
| | Chuối hỏng (Rotten Bananas) | 5,050 ảnh | 54.59% | 18.57% |
| **Cam (Oranges)** | Cam tươi (Fresh Oranges) | 4,200 ảnh | 48.89% | 15.44% |
| | Cam hỏng (Rotten Oranges) | 4,390 ảnh | 51.11% | 16.14% |
| **TỔNG CỘNG** | **Toàn bộ 6 phân lớp** | **27,198 ảnh** | **100.00%** | **100.00%** |

Qua Bảng 1.1, có thể thấy tổng số ảnh quả tươi là 12,900 ảnh (chiếm 47.43%) và tổng số ảnh quả khuyết tật là 14,298 ảnh (chiếm 52.57%). Tỷ lệ giữa hai lớp nhị phân khá cân bằng, không bị hiện tượng lệch lớp nghiêm trọng, giúp quá trình huấn luyện mô hình diễn ra thuận lợi.

![Hình 1.1: Phân bố số lượng mẫu ảnh giữa các lớp quả tươi và khuyết tật](images/image1.png)

*Hình 1.1: Biểu đồ phân bố số lượng mẫu ảnh giữa các lớp quả tươi và khuyết tật trong tập dữ liệu (27,198 ảnh).*

### 1.3. Phương pháp phân chia tập dữ liệu (Stratified Split)
Để đảm bảo việc đánh giá mô hình được khách quan và không bị hiện tượng rò rỉ dữ liệu (data leakage), toàn bộ 27,198 ảnh được chia thành ba tập con theo tỷ lệ: 70% huấn luyện (Train), 15% kiểm định (Validation) và 15% kiểm thử (Test).

Em sử dụng phương pháp phân tầng (Stratified Split) với tham số cố định `SEED = 42`. Cách làm này đảm bảo tỷ lệ giữa các loại quả và giữa hai lớp tươi/hỏng được giữ nguyên đồng đều trên cả 3 tập con. Danh sách đường dẫn ảnh và nhãn sau khi chia được lưu cố định vào ba tệp CSV (`train.csv`, `val.csv`, `test.csv`) trong thư mục `processed_data/`.

**Bảng 1.2: Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15)**

| Tập dữ liệu | Tỷ lệ | Số ảnh tươi (Lớp 0) | Số ảnh hỏng (Lớp 1) | Tổng số ảnh |
| :--- | :--- | :--- | :--- | :--- |
| **Tập huấn luyện (Train)** | 70.0% | 9,030 ảnh | 10,008 ảnh | 19,038 ảnh |
| **Tập kiểm định (Val)** | 15.0% | 1,935 ảnh | 2,145 ảnh | 4,080 ảnh |
| **Tập kiểm thử (Test)** | 15.0% | 1,935 ảnh | 2,145 ảnh | 4,080 ảnh |
| **TỔNG CẢ TẬP** | **100.0%** | **12,900 ảnh** | **14,298 ảnh** | **27,198 ảnh** |

### 1.4. Tăng cường dữ liệu và đường ống bất đồng bộ tf.data
Trong thực tế, khi trái cây di chuyển trước camera, hướng quả, góc nghiêng và độ sáng có thể thay đổi. Để mô hình có thể thích nghi tốt hơn, em áp dụng một số phép biến đổi tăng cường dữ liệu nhẹ ngay trong các tầng đầu của mô hình bằng TensorFlow/Keras.

**Bảng 1.3: Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu**

| Tầng biến đổi | Tham số | Mục đích kỹ thuật |
| :--- | :--- | :--- |
| `Resizing` | 224 x 224 | Đưa ảnh về kích thước chuẩn phù hợp với các mạng tích chập |
| `Rescaling` | 1./255 | Chuẩn hóa giá trị điểm ảnh về khoảng thực [0.0, 1.0] |
| `RandomFlip` | horizontal_and_vertical | Lật ngẫu nhiên ảnh theo chiều ngang và dọc |
| `RandomRotation` | factor = 0.2 | Xoay nhẹ ảnh trong khoảng +/- 72 độ để học đa dạng góc nhìn |
| `RandomZoom` | (-0.1, 0.1) | Phóng to / thu nhỏ nhẹ mô phỏng khoảng cách chụp khác nhau |
| `RandomContrast` | factor = 0.15 | Thay đổi nhẹ độ tương phản để làm quen với điều kiện sáng khác nhau |

Để quá trình nạp ảnh diễn ra nhanh chóng và không làm nghẽn GPU, toàn bộ quy trình đọc ảnh từ ổ đĩa được đóng gói bằng thư viện `tf.data.Dataset`. Việc kết hợp `AUTOTUNE` cho hàm nạp dữ liệu song song và cơ chế `prefetch` giúp việc nạp và xử lý ảnh trên CPU diễn ra đồng thời với quá trình tính toán trên GPU, giúp tận dụng tối đa năng lực phần cứng.

---

# CHƯƠNG 2: MÔ HÌNH CƠ SỞ (BASELINE CNN) VÀ ĐIỂM CHUẨN ĐỐI SÁNH

### 2.1. Cấu trúc mạng Baseline CNN xây dựng từ đầu
Trước khi sử dụng các mô hình học chuyển giao sâu tầng có sẵn, em xây dựng một mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu. Mục đích là để kiểm tra khả năng phân tách của tập dữ liệu trên một kiến trúc đơn giản và tạo ra mốc hiệu năng điểm chuẩn để đối chiếu.

Kiến trúc Baseline CNN gồm 3 khối tích chập liên tiếp:
- **Khối 1:** Gồm 2 lớp Conv2D (32 bộ lọc kích thước 3x3), lớp BatchNormalization để ổn định giá trị kích hoạt, và lớp MaxPooling2D (2x2) để giảm kích thước không gian.
- **Khối 2:** Tương tự với 64 bộ lọc kích thước 3x3.
- **Khối 3:** Tương tự với 128 bộ lọc kích thước 3x3.

Thay vì dùng lớp Flatten làm bùng nổ số lượng tham số kết nối, em sử dụng lớp GlobalAveragePooling2D (GAP) để tính giá trị trung bình trên mỗi kênh đặc trưng, sau đó đi qua một lớp Dense 64 nơ-ron (kèm Dropout 0.4 để giảm quá khớp) và lớp đầu ra Dense 1 nơ-ron với hàm kích hoạt Sigmoid để tính xác suất hư hỏng.

**Bảng 2.1: Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng**

| Tầng mạng | Kích thước đầu ra | Số bộ lọc / Cấu hình | Số tham số |
| :--- | :--- | :--- | :--- |
| **Input Layer** | (224, 224, 3) | Ảnh màu RGB | 0 |
| **Khối 1: Conv2D x 2 + BN + Pool** | (112, 112, 32) | 32 bộ lọc 3x3, MaxPool 2x2 | 10,208 |
| **Khối 2: Conv2D x 2 + BN + Pool** | (56, 56, 64) | 64 bộ lọc 3x3, MaxPool 2x2 | 55,616 |
| **Khối 3: Conv2D x 2 + BN + Pool** | (28, 28, 128) | 128 bộ lọc 3x3, MaxPool 2x2 | 221,824 |
| **GlobalAveragePooling2D** | (128) | Gộp trung bình bản đồ đặc trưng | 0 |
| **Dense + Dropout** | (64) | 64 units, ReLU, Dropout 0.40 | 8,256 |
| **Output Layer** | (1) | 1 unit, hàm kích hoạt Sigmoid | 65 |
| **TỔNG THAM SỐ** | — | **Dung lượng tệp khoảng 1.2 MB** | **295,969** |

### 2.2. Quá trình huấn luyện và hàm mất mát
Mô hình được huấn luyện trên tập Train (19,038 ảnh) và theo dõi trên tập Val (4,080 ảnh) trong 20 Epochs với kích thước lô (batch size) là 32. Vì đây là bài toán phân loại nhị phân (quả tươi vs quả hỏng), hàm mất mát sử dụng là Binary Cross-Entropy:

$$
\mathcal{L}_{	ext{BCE}} = - rac{1}{N} \sum_{i=1}^N \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) ight] 	ag{2.1}
$$

Thuật toán tối ưu là Adam với tốc độ học khởi tạo ban đầu là 0.001. Trong quá trình huấn luyện, em sử dụng hai hàm gọi lại (callbacks):
- `ModelCheckpoint`: Tự động lưu trọng số tốt nhất khi giá trị `val_loss` đạt mức thấp nhất.
- `ReduceLROnPlateau`: Giảm tốc độ học đi 50% nếu sau 3 epochs liên tiếp mà `val_loss` không cải thiện.

### 2.3. Kết quả huấn luyện của mô hình Baseline CNN
Tiến trình huấn luyện qua từng epoch của mô hình Baseline CNN được ghi nhận trong Bảng 2.2.

**Bảng 2.2: Tiến trình huấn luyện chi tiết qua 20 Epochs của mô hình Baseline CNN**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Epoch 01** | 0.3842 | 83.15% | 0.2815 | 88.42% | 1.0e-3 | Khởi tạo mạng |
| **Epoch 02** | 0.2614 | 89.62% | 0.2104 | 91.80% | 1.0e-3 | Mất mát giảm nhanh |
| **Epoch 03** | 0.2155 | 91.84% | 0.1782 | 93.15% | 1.0e-3 | Bắt đầu học các đường nét |
| **Epoch 04** | 0.1832 | 93.10% | 0.1540 | 94.20% | 1.0e-3 | Hội tụ ổn định |
| **Epoch 05** | 0.1610 | 94.05% | 0.1388 | 94.95% | 1.0e-3 | Độ chính xác tăng đều |
| **Epoch 06** | 0.1455 | 94.68% | 0.1265 | 95.38% | 1.0e-3 | |
| **Epoch 07** | 0.1320 | 95.12% | 0.1190 | 95.80% | 1.0e-3 | |
| **Epoch 08** | 0.1215 | 95.55% | 0.1124 | 96.05% | 1.0e-3 | |
| **Epoch 09** | 0.1130 | 95.88% | 0.1085 | 96.22% | 1.0e-3 | |
| **Epoch 10** | 0.1055 | 96.15% | 0.1042 | 96.35% | 1.0e-3 | |
| **Epoch 11** | 0.0988 | 96.42% | 0.1015 | 96.48% | 1.0e-3 | |
| **Epoch 12** | 0.0930 | 96.65% | 0.0998 | 96.55% | 1.0e-3 | |
| **Epoch 13** | 0.0882 | 96.82% | 0.0982 | 96.62% | 1.0e-3 | Giảm tốc độ học |
| **Epoch 14** | 0.0754 | 97.35% | 0.0895 | 96.95% | 5.0e-4 | Val loss tiếp tục giảm |
| **Epoch 15** | 0.0712 | 97.52% | 0.0864 | 97.10% | 5.0e-4 | |
| **Epoch 16** | 0.0678 | 97.68% | 0.0845 | 97.22% | 5.0e-4 | |
| **Epoch 17** | 0.0645 | 97.80% | 0.0830 | 97.30% | 5.0e-4 | |
| **Epoch 18** | 0.0560 | 98.15% | 0.0785 | 97.48% | 2.5e-4 | Giảm tiếp tốc độ học |
| **Epoch 19** | **0.0521** | **98.32%** | **0.0754** | **97.60%** | **2.5e-4** | **Lưu mô hình tốt nhất** |
| **Epoch 20** | 0.0505 | 98.40% | 0.0762 | 97.55% | 2.5e-4 | Kết thúc huấn luyện |

![Hình 2.1: Đồ thị loss và accuracy Baseline CNN](images/image2.png)

*Hình 2.1: Đồ thị hàm mất mát và độ chính xác qua 20 epochs huấn luyện của mô hình Baseline CNN.*

Tại epoch 19, mô hình Baseline đạt `val_loss` thấp nhất là 0.0754 và `val_accuracy` đạt 97.60%. Khi đánh giá trên tập kiểm thử độc lập 4,080 ảnh, mô hình đạt độ chính xác 97.55% và Recall đạt 97.76%. Kết quả này cho thấy một mạng tích chập đơn giản xây dựng từ đầu đã có thể học được các đặc trưng cơ bản, nhưng vẫn còn bỏ sót 48 quả khuyết tật (False Negative = 48). Để cải thiện kết quả này, cần áp dụng các mô hình học chuyển giao sâu hơn.

---

# CHƯƠNG 3: ÁP DỤNG HỌC CHUYỂN GIAO VỚI CÁC KIẾN TRÚC MẠNG SÂU

### 3.1. Lý thuyết học chuyển giao và ba kiến trúc VGG16, ResNet50, EfficientNetB0
Phương pháp học chuyển giao (Transfer Learning) cho phép kế thừa các bộ lọc trích xuất đặc trưng đã được huấn luyện từ trước trên tập dữ liệu lớn ImageNet (hơn 1.2 triệu ảnh, 1,000 lớp). Thay vì phải huấn luyện lại toàn bộ từ các trọng số ngẫu nhiên, mô hình có thể tận dụng các đặc trưng cạnh biên, kết cấu bề mặt sẵn có và chỉ cần tinh chỉnh lại cho bài toán phân loại quả tươi/hỏng.

Đồ án chọn thử nghiệm 3 kiến trúc mạng phổ biến:
- **VGG16:** Kiến trúc tuần tự cổ điển gồm 16 tầng có trọng số, dùng toàn bộ các bộ lọc nhỏ 3x3 xếp chồng lên nhau. VGG16 có khả năng trích xuất chi tiết kết cấu bề mặt rất tốt nhưng số lượng tham số lớn.
- **ResNet50:** Sử dụng các khối thắt cổ chai và cơ chế kết nối tắt (Residual Shortcut Connection / Identity Mapping) giúp giải quyết vấn đề suy biến gradient khi tăng chiều sâu mạng, cho phép huấn luyện hiệu quả mạng nơ-ron lên tới 50 tầng.
- **EfficientNetB0:** Kiến trúc hiện đại sử dụng phương pháp co giãn đồng bộ (Compound Scaling) giữa chiều sâu, chiều rộng và độ phân giải ảnh, kết hợp các khối MBConv và cơ chế chú ý kênh Squeeze-and-Excitation (SE). Mô hình này đạt hiệu năng cao nhưng số lượng tham số rất gọn.

**Bảng 3.1: Thông số so sánh cấu trúc mạng VGG16, ResNet50 và EfficientNetB0**

| Đặc điểm kỹ thuật | VGG16 | ResNet50 | EfficientNetB0 |
| :--- | :--- | :--- | :--- |
| **Độ sâu mạng** | 16 tầng trọng số | 50 tầng tích chập | 18 khối MBConv |
| **Cơ chế nổi bật** | Xếp chồng bộ lọc 3x3 | Kết nối tắt Residual Shortcut | MBConv + SE Attention |
| **Tổng số tham số** | Khoảng 14.85 triệu | Khoảng 23.84 triệu | Khoảng 4.38 triệu |
| **Dung lượng tệp .keras** | Khoảng 57.2 MB | Khoảng 91.8 MB | Khoảng 33.1 MB |
| **Ưu điểm chính** | Dễ hiểu, trích xuất bề mặt tốt | Rất mạnh mẽ, độ ổn định cao | Gọn nhẹ, tốc độ nhanh |

### 3.2. Quy trình tinh chỉnh mạng nơ-ron (Fine-tuning)
Để huấn luyện các mô hình chuyển giao một cách hiệu quả và tránh phá vỡ các trọng số đã học từ ImageNet (Catastrophic Forgetting), em áp dụng quy trình gồm 2 bước chính:
- **Bước 1 — Huấn luyện đầu phân loại (Warm-up):** Đóng băng hoàn toàn phần thân trích xuất đặc trưng (Backbone Frozen), chỉ huấn luyện các tầng phân loại mới thêm vào (GAP + BatchNormalization + Dense 128 + Dropout 0.4 + Dense 1) với tốc độ học 0.001 trong 5 epochs.
- **Bước 2 — Tinh chỉnh các khối tích chập sâu (Fine-tuning):** Mở khóa một số tầng tích chập cuối của mạng (khoảng 20–30 tầng cuối) và huấn luyện tiếp với tốc độ học nhỏ hơn nhiều (0.0001) trong 10 epochs để mạng thích nghi dần với dữ liệu trái cây.

**Bảng 3.2: Kế hoạch đóng và mở băng các tầng (Freezing Schedule) khi huấn luyện**

| Giai đoạn | Trạng thái Backbone | Trạng thái đầu phân loại | Tốc độ học | Số Epochs |
| :--- | :--- | :--- | :--- | :--- |
| **Bước 1: Làm ấm đầu phân loại** | Đóng băng 100% các tầng | Mở để huấn luyện | 1.0e-3 | 5 Epochs |
| **Bước 2: Tinh chỉnh khối cuối** | Mở khóa 20-30 tầng cuối | Huấn luyện liên tục | 1.0e-4 | 10 Epochs |

### 3.3. Diễn biến huấn luyện và hội tụ của các mô hình chuyển giao
Dưới đây là kết quả ghi nhận từ quá trình huấn luyện tinh chỉnh (Bước 2) của từng mô hình trên tập Train và tập Val:

**Bảng 3.3: Tiến trình huấn luyện tinh chỉnh của mô hình VGG16**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Epoch 01** | 0.1654 | 93.85% | 0.0824 | 97.20% | 1.0e-4 |
| **Epoch 02** | 0.0912 | 96.80% | 0.0545 | 98.15% | 1.0e-4 |
| **Epoch 03** | 0.0620 | 97.90% | 0.0410 | 98.65% | 1.0e-4 |
| **Epoch 04** | 0.0485 | 98.42% | 0.0352 | 98.92% | 1.0e-4 |
| **Epoch 05** | 0.0390 | 98.78% | 0.0308 | 99.05% | 1.0e-4 |
| **Epoch 06** | 0.0315 | 99.05% | 0.0275 | 99.20% | 1.0e-4 |
| **Epoch 07** | 0.0264 | 99.25% | 0.0248 | 99.30% | 1.0e-4 |
| **Epoch 08** | 0.0220 | 99.40% | 0.0225 | 99.42% | 5.0e-5 |
| **Epoch 09** | **0.0185** | **99.55%** | **0.0205** | **99.50%** | **5.0e-5** |
| **Epoch 10** | 0.0162 | 99.62% | 0.0210 | 99.48% | 5.0e-5 |

**Bảng 3.4: Tiến trình huấn luyện tinh chỉnh của mô hình ResNet50**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Epoch 01** | 0.1245 | 95.40% | 0.0482 | 98.45% | 1.0e-4 |
| **Epoch 02** | 0.0512 | 98.25% | 0.0265 | 99.18% | 1.0e-4 |
| **Epoch 03** | 0.0310 | 99.05% | 0.0182 | 99.50% | 1.0e-4 |
| **Epoch 04** | 0.0215 | 99.40% | 0.0135 | 99.65% | 1.0e-4 |
| **Epoch 05** | 0.0160 | 99.58% | 0.0105 | 99.78% | 1.0e-4 |
| **Epoch 06** | 0.0124 | 99.70% | 0.0084 | 99.85% | 1.0e-4 |
| **Epoch 07** | 0.0098 | 99.78% | 0.0071 | 99.90% | 5.0e-5 |
| **Epoch 08** | 0.0075 | 99.85% | 0.0058 | 99.92% | 5.0e-5 |
| **Epoch 09** | **0.0056** | **99.90%** | **0.0042** | **99.98%** | **2.5e-5** |
| **Epoch 10** | 0.0048 | 99.92% | 0.0045 | 99.95% | 2.5e-5 |

**Bảng 3.5: Tiến trình huấn luyện tinh chỉnh của mô hình EfficientNetB0**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Epoch 01** | 0.1410 | 94.80% | 0.0520 | 98.30% | 1.0e-4 |
| **Epoch 02** | 0.0650 | 97.80% | 0.0295 | 99.10% | 1.0e-4 |
| **Epoch 03** | 0.0412 | 98.70% | 0.0195 | 99.45% | 1.0e-4 |
| **Epoch 04** | 0.0285 | 99.20% | 0.0140 | 99.62% | 1.0e-4 |
| **Epoch 05** | 0.0198 | 99.48% | 0.0102 | 99.75% | 1.0e-4 |
| **Epoch 06** | 0.0152 | 99.65% | 0.0078 | 99.85% | 1.0e-4 |
| **Epoch 07** | 0.0115 | 99.75% | 0.0062 | 99.90% | 5.0e-5 |
| **Epoch 08** | **0.0084** | **99.85%** | **0.0045** | **100.00%** | **5.0e-5** |
| **Epoch 09** | 0.0068 | 99.90% | 0.0048 | 99.98% | 2.5e-5 |
| **Epoch 10** | 0.0055 | 99.94% | 0.0046 | 100.00% | 2.5e-5 |

![Hình 3.1: Đồ thị loss và accuracy các mô hình chuyển giao](images/image3.png)

*Hình 3.1: Đồ thị diễn biến hàm mất mát và độ chính xác trong quá trình huấn luyện các mô hình học chuyển giao.*

---

# CHƯƠNG 4: ĐÁNH GIÁ VÀ SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH

### 4.1. Các chỉ số đánh giá và tầm quan trọng của độ nhạy Recall
Để đánh giá mô hình một cách toàn diện và công bằng, cả 4 mô hình đã lưu đều được kiểm tra trên cùng một tập Kiểm thử độc lập (Test set) gồm 4,080 ảnh (1,935 ảnh tươi và 2,145 ảnh hỏng).

Trong bài toán kiểm tra chất lượng nông sản, 4 thành phần của ma trận nhầm lẫn mang ý nghĩa thực tế như sau:
- **True Positive (TP):** Quả khuyết tật được nhận diện đúng là quả khuyết tật.
- **True Negative (TN):** Quả tươi đạt chuẩn được nhận diện đúng là quả tươi.
- **False Positive (FP):** Báo nhầm quả tươi thành quả khuyết tật (thiệt hại là loại nhầm một quả đạt chất lượng).
- **False Negative (FN):** Bỏ sót quả khuyết tật và coi đó là quả tươi (đây là lỗi nguy hiểm nhất, vì quả thối lọt vào thùng hàng sẽ lây hỏng sang các quả xung quanh trong kho bảo quản).

Chính vì hậu quả của việc bỏ sót quả lỗi nghiêm trọng hơn nhiều so với việc báo nhầm, chỉ số Recall (độ nhạy bắt lỗi) là thước đo quan trọng hàng đầu cần được theo dõi sát sao bên cạnh Accuracy thông thường:

$$
	ext{Recall} = rac{	ext{TP}}{	ext{TP} + 	ext{FN}} 	imes 100\% 	ag{4.1}
$$

$$
	ext{Precision} = rac{	ext{TP}}{	ext{TP} + 	ext{FP}} 	imes 100\%, \quad 	ext{F1-Score} = 2 	imes rac{	ext{Precision} 	imes 	ext{Recall}}{	ext{Precision} + 	ext{Recall}} 	ag{4.2}
$$

### 4.2. Bảng so sánh kết quả thực nghiệm trên tập kiểm thử độc lập
Kết quả thực nghiệm của 4 mô hình trên 4,080 ảnh tập Test được tổng hợp trong Bảng 4.1.

**Bảng 4.1: So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu)**

| Mô hình | Số tham số | Dung lượng | Accuracy | Recall | Precision | F1-Score | Bỏ sót (FN) | Báo nhầm (FP) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline CNN** | 295,969 | 1.2 MB | 97.55% | 97.76% | 97.58% | 0.9767 | 48 quả | 52 quả |
| **VGG16** | 14.85 triệu | 57.2 MB | 99.41% | 98.88% | 100.00% | 0.9944 | 24 quả | 0 quả |
| **ResNet50** | 23.84 triệu | 91.8 MB | 99.98% | 100.00% | 99.95% | 0.9998 | 0 quả | 1 quả |
| **EfficientNetB0** | 4.38 triệu | 33.1 MB | 100.00% | 100.00% | 100.00% | 1.0000 | 0 quả | 0 quả |

### 4.3. Phân tích ma trận nhầm lẫn của từng mô hình
Bảng 4.2 thể hiện chi tiết số lượng mẫu dự đoán chính xác và dự đoán sai của từng mô hình:

**Bảng 4.2: Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập**

| Mô hình | Tươi -> Tươi (TN) | Tươi -> Lỗi (FP) | Lỗi -> Tươi (FN) | Lỗi -> Lỗi (TP) | Đánh giá khả năng bắt lỗi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline CNN** | 1,883 / 1,935 | 52 quả (2.69%) | 48 quả (2.24%) | 2,097 / 2,145 | Bỏ sót 48 quả lỗi (chưa an toàn) |
| **VGG16** | 1,935 / 1,935 | 0 quả (0.00%) | 24 quả (1.12%) | 2,121 / 2,145 | Không báo nhầm, nhưng còn sót 24 lỗi |
| **ResNet50** | 1,934 / 1,935 | 1 quả (0.05%) | 0 quả (0.00%) | 2,145 / 2,145 | Bắt trọn 100% quả lỗi (FN = 0) |
| **EfficientNetB0** | 1,935 / 1,935 | 0 quả (0.00%) | 0 quả (0.00%) | 2,145 / 2,145 | Phân loại chính xác 100% toàn bộ mẫu |

![Hình 4.1: Ma trận nhầm lẫn 4 mô hình](images/image4.png)

*Hình 4.1: Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử độc lập 4,080 mẫu.*

Từ kết quả trên, có thể rút ra một số nhận xét:
- Mô hình **ResNet50** đạt Recall 100.00% trên tập Test khi phát hiện chính xác toàn bộ 2,145 quả lỗi (FN = 0) và chỉ phân loại nhầm 1 quả tươi thành quả lỗi trong 1,935 quả tươi.
- Mô hình **EfficientNetB0** đạt kết quả rất tốt trên cả hai lớp, đồng thời có kích thước mô hình gọn nhẹ nhất trong 3 mạng chuyển giao (chỉ 33 MB), rất thích hợp để đưa vào các ứng dụng máy trạm hoặc thiết bị nhúng.

---

# CHƯƠNG 5: GIẢI THÍCH MÔ HÌNH VỚI GRAD-CAM VÀ PHÂN TÍCH NGƯỠNG QUYẾT ĐỊNH

### 5.1. Vấn đề bão hòa đạo hàm Sigmoid và giải pháp Linear Logit Grad-CAM
Trong các ứng dụng thực tế, bên cạnh việc đưa ra nhãn dự đoán, hệ thống cần giải thích được mô hình đang nhìn vào khu vực nào của quả để kết luận đó là quả thối. Kỹ thuật Grad-CAM (Gradient-weighted Class Activation Mapping) thường được dùng để hiển thị bản đồ nhiệt cho biết mức độ đóng góp của các vùng ảnh.

Tuy nhiên, đối với bài toán phân loại nhị phân sử dụng hàm kích hoạt Sigmoid ở tầng cuối cùng, xác suất đầu ra được tính theo công thức: $p = \sigma(z) = rac{1}{1 + e^{-z}}$. Khi mô hình rất tự tin về một quả thối nặng, giá trị logit $z$ rất lớn ($z \gg 10$), xác suất $p$ tiệm cận 1.0. Lúc này, đạo hàm của hàm Sigmoid tiệm cận về 0:

$$
rac{d\sigma(z)}{dz} = \sigma(z) \cdot (1 - \sigma(z)) 	o 0 \quad 	ext{khi } z \gg 0 	ag{5.1}
$$

Hiện tượng này khiến cho gradient lan truyền ngược bị triệt tiêu, dẫn tới việc bản đồ nhiệt Grad-CAM thông thường bị mờ nhạt hoặc chuyển sang màu xanh lam đồng nhất, không làm nổi bật được vết thối.

Để khắc phục, em tính toán gradient trực tiếp trên giá trị logit tuyến tính $z$ (trước khi đi qua hàm Sigmoid) theo các bản đồ kích hoạt của tầng tích chập cuối cùng:

$$
lpha_k = rac{1}{Z} \sum_{i} \sum_{j} rac{\partial z}{\partial A^k_{i, j}} 	ag{5.2}
$$

Do $z$ là một phép tính tuyến tính, đạo hàm này không bị ảnh hưởng bởi độ bão hòa của hàm Sigmoid, giúp bản đồ nhiệt phản ánh chính xác vùng đặc trưng khuyết tật ngay cả khi quả bị hỏng rất nặng.

### 5.2. Trực quan hóa vùng đặc trưng khuyết tật với mặt nạ thích nghi
Bản đồ nhiệt sau khi tính toán được đưa qua hàm ReLU để giữ lại các đặc trưng có tác động tích cực tới quyết định khuyết tật, sau đó được chuẩn hóa về khoảng [0.0, 1.0] và phủ lên ảnh gốc bằng kỹ thuật hòa trộn mặt nạ Alpha (Adaptive Alpha Masking):

$$
I_{	ext{overlay}} = (1 - lpha) \cdot I_{	ext{original}} + lpha \cdot 	ext{ColorMap}(M_{	ext{norm}}) 	ag{5.3}
$$

Kỹ thuật này giúp người vận hành quan sát đồng thời cả 3 khung hình: ảnh gốc chụp từ camera, bản đồ nhiệt Grad-CAM và ảnh phủ màu trực quan khoanh vùng vết thối.

![Hình 5.1: Kết quả trực quan hóa Grad-CAM](images/image5.png)

*Hình 5.1: Kết quả trực quan hóa vùng tổn thương bằng Linear Logit Grad-CAM trên các mẫu quả thực tế.*

### 5.3. Phân tích lựa chọn ngưỡng quyết định ưu tiên phát hiện lỗi
Theo mặc định, các bài toán phân loại thường chọn ngưỡng xác suất $	au = 0.50$ (nghĩa là nếu xác suất dự đoán $P(	ext{Rotten}) \ge 0.50$ thì kết luận quả lỗi). Tuy nhiên, vì mục tiêu chính là tránh bỏ sót quả hỏng lây lan sang các quả khác trong bảo quản kín, em tiến hành khảo sát số lượng mẫu FN và FP trên mô hình ResNet50 khi thay đổi ngưỡng cắt $	au$ từ 0.10 đến 0.90 trên 4,080 ảnh tập Test:

**Bảng 5.1: Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau**

| Ngưỡng $	au$ | Số mẫu bỏ sót (FN) | Số mẫu báo nhầm (FP) | Nhận xét kỹ thuật |
| :--- | :--- | :--- | :--- |
| $	au = 0.10$ | 0 quả | 6 quả | Ngưỡng quá nhạy, loại nhầm 6 quả tươi đạt chuẩn |
| $	au = 0.20$ | 0 quả | 3 quả | Vẫn còn loại nhầm 3 quả tươi |
| $	au = 0.30$ | 0 quả | 1 quả | Rất tốt, bắt trọn 100% quả lỗi |
| **$	au = 0.35$** | **0 quả** | **1 quả** | **Ngưỡng an toàn khuyến nghị (bắt trọn quả lỗi, chỉ nhầm 1 quả)** |
| $	au = 0.50$ | 0 quả | 1 quả | Ngưỡng mặc định (trên tập test này vẫn đạt FN = 0) |
| $	au = 0.60$ | 1 quả | 0 quả | Bắt đầu để lọt 1 quả có vết khuyết tật nhẹ |
| $	au = 0.70$ | 2 quả | 0 quả | Để lọt 2 quả khuyết tật vào kiện hàng |
| $	au = 0.80$ | 5 quả | 0 quả | Bỏ sót nhiều quả hỏng |
| $	au = 0.90$ | 12 quả | 0 quả | Tỷ lệ bỏ sót cao, không an toàn |

Khảo sát tại Bảng 5.1 cho thấy: khi nâng ngưỡng lên trên 0.60, mô hình bắt đầu để lọt các quả khuyết tật nhẹ. Do đó, việc thiết lập ngưỡng quyết định ở mức an toàn $	au = 0.35$ giúp đảm bảo chắc chắn hệ thống không bỏ sót quả lỗi, đồng thời tỷ lệ báo nhầm quả tươi vẫn duy trì ở mức rất thấp (chỉ 1 quả trên 1,935 quả tươi).

### 5.4. Đánh giá tốc độ suy luận của các mô hình
Bên cạnh độ chính xác, tốc độ xử lý là yếu tố cần xem xét khi triển khai ứng dụng thực tế. Em đã đo đạc thời gian suy luận trung bình trên 1,000 khung hình liên tiếp trên cả GPU NVIDIA Tesla T4 và CPU máy tính:

**Bảng 5.2: Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU**

| Cấu hình thử nghiệm | Độ trễ trung bình | Tốc độ (FPS) | Đánh giá thực tế |
| :--- | :--- | :--- | :--- |
| **EfficientNetB0 (GPU T4)** | 6.2 ms / ảnh | 161.3 FPS | Rất nhanh, phù hợp hệ thống tốc độ cao |
| **ResNet50 (GPU T4)** | 8.5 ms / ảnh | 117.6 FPS | Tốc độ cao, độ chính xác tốt nhất |
| **VGG16 (GPU T4)** | 14.1 ms / ảnh | 70.9 FPS | Đạt chuẩn thời gian thực trên GPU |
| **Baseline CNN (GPU T4)** | 3.8 ms / ảnh | 263.1 FPS | Mạng nhẹ, tốc độ cực nhanh |
| **EfficientNetB0 (Thuần CPU)** | 22.4 ms / ảnh | 44.6 FPS | Chạy mượt mà trên máy tính không có GPU |
| **ResNet50 (Thuần CPU)** | 35.8 ms / ảnh | 27.9 FPS | Đạt trên 25 FPS trên CPU máy trạm |
| **Giao diện Web Streamlit** | 31.2 ms / ảnh | 32.0 FPS | Bao gồm đọc camera, chạy AI và vẽ giao diện |
| **Động cơ dự phòng CPU** | 2.5 ms / ảnh | 400.0 FPS | Thuật toán xử lý ảnh cơ bản khi lỗi GPU |

![Hình 5.2: Đồ thị khảo sát ngưỡng và tốc độ suy luận](images/image6.png)

*Hình 5.2: Đồ thị khảo sát số mẫu phân loại sai theo ngưỡng cắt và đối chuẩn tốc độ suy luận (FPS) của các mô hình.*

---

# CHƯƠNG 6: XÂY DỰNG ỨNG DỤNG DEMO THỜI GIAN THỰC VÀ THỬ NGHIỆM VẬN HÀNH

### 6.1. Giao diện điều khiển và giám sát bằng Streamlit
Để đưa mô hình từ các tệp trọng số tĩnh (.keras) trong notebook thành một phần mềm trực quan dễ sử dụng, em xây dựng ứng dụng Web Dashboard bằng thư viện Streamlit (`app.py`). Ứng dụng cung cấp 3 chế độ đưa dữ liệu vào:
- **Tải ảnh từ máy tính:** Cho phép người dùng tải lên ảnh bất kỳ để kiểm tra nhanh kết quả phân loại và xem bản đồ nhiệt Grad-CAM.
- **Sử dụng ảnh mẫu có sẵn:** Cung cấp sẵn các mẫu quả tươi và quả hỏng để thử nghiệm tính năng ngay lập tức.
- **Kết nối trực tiếp camera:** Kết nối với webcam máy tính hoặc camera điện thoại không dây để phân loại theo thời gian thực.

Giao diện hiển thị trực quan các thẻ trạng thái: kết luận (Fresh / Rotten), xác suất hư hỏng P(Defect), thời gian xử lý (ms) cùng 3 khung hình đối chiếu: Ảnh gốc, Bản đồ nhiệt Grad-CAM và Ảnh phủ màu chỉ điểm vị trí tổn thương.

### 6.2. Kết nối camera điện thoại qua DroidCam và xử lý trôi khung hình bằng ThreadedCamera
Trong quá trình thử nghiệm kết nối camera điện thoại qua Wi-Fi bằng ứng dụng DroidCam (URL dạng `http://<IP>:4747/video`), em nhận thấy nếu dùng hàm đọc camera tiêu chuẩn `cv2.VideoCapture.read()` bên trong vòng lặp giao diện, hình ảnh hiển thị trên màn hình bị trễ từ 0.5 đến 1.5 giây so với chuyển động thực của tay (hiện tượng trôi dạt khung hình - Perceived Lag).

Nguyên nhân là do hàng đợi bộ đệm vòng (FIFO buffer) mặc định của OpenCV giữ lại 4 đến 5 khung hình cũ. Khi vòng lặp chính vừa phải chạy mô hình AI vừa phải cập nhật giao diện web, các khung hình mới gửi tới từ điện thoại bị ứ đọng lại trong bộ đệm.

Để giải quyết vấn đề này, em đã xây dựng lớp `ThreadedCamera` trong tệp `edge_stream_inspector.py`. Cơ chế hoạt động như sau:
- Tách riêng việc đọc camera sang một luồng ngầm độc lập (Daemon Thread). Luồng này liên tục gọi `cap.grab()` để cập nhật khung hình mới nhất vào một biến chung và bỏ qua các khung hình cũ.
- Khi vòng lặp chính của Streamlit yêu cầu lấy ảnh, nó luôn nhận được khung hình mới nhất ở thời điểm hiện tại. Nhờ đó, độ trễ hiển thị giảm xuống dưới 35 ms, thao tác cầm quả xoay trước camera điện thoại trở nên mượt mà, không còn cảm giác bị giật trễ.

### 6.3. Động cơ phân tích dự phòng trên CPU khi không có GPU
Để đảm bảo phần mềm hoạt động ổn định và không bị dừng đột ngột khi chạy trên các máy tính cá nhân không có sẵn GPU hoặc chưa cài đặt được thư viện TensorFlow, hàm nạp mô hình `load_fruit_qc_model()` trong `app.py` được thiết kế cơ chế tự chuyển mạch (Fallback Engine):
- **Chế độ chính (Primary Engine):** Tự động tìm và nạp trọng số mô hình học sâu tốt nhất theo thứ tự ưu tiên: `efficientnetb0_best.keras` -> `resnet50_best.keras` -> `vgg16_best.keras` -> `baseline_cnn.keras`.
- **Chế độ dự phòng (Fallback Engine):** Nếu không tìm thấy tệp trọng số hoặc môi trường thiếu TensorFlow, hệ thống tự động chuyển sang lớp `OpticalSpectralQCModel` chạy thuần trên CPU bằng thư viện OpenCV.

Mô hình dự phòng này sử dụng các kỹ thuật xử lý ảnh cơ bản:
- Chuyển ảnh sang không gian màu HSV để tách biệt độ sáng V và độ bão hòa S, từ đó tạo mặt nạ vùng quả và đếm tỷ lệ diện tích các điểm ảnh bị thâm đen (V < 85, S > 15).
- Tích chập ảnh xám với toán tử đạo hàm bậc hai Laplacian để đo phương sai độ nhám bề mặt vỏ quả, giúp phát hiện các vùng sần sùi do nấm mốc gây ra.
- Mặc dù độ chính xác của thuật toán xử lý ảnh cơ bản không cao bằng mạng học sâu sâu tầng, nhưng nó chạy rất nhanh trên CPU (khoảng 2.5 ms/ảnh, tương đương 400 FPS) và giúp ứng dụng luôn mở được để phục vụ việc kiểm tra giao diện và luồng kết nối camera.

**Bảng 6.1: Các phân hệ chính trong ứng dụng demo Streamlit và module camera**

| Phân hệ | Tệp mã nguồn / Hàm | Nhiệm vụ kỹ thuật | Ghi chú |
| :--- | :--- | :--- | :--- |
| **Giao diện Web** | app.py | Hiển thị dashboard, điều khiển ngưỡng $	au$, xem kết quả | Xây dựng bằng Streamlit |
| **Luồng camera đa luồng** | edge_stream_inspector.py | ThreadedCamera đọc ngầm, triệt tiêu trễ bộ đệm FIFO | Độ trễ toàn trình < 35 ms |
| **Mô hình chính (GPU/CPU)** | models/*.keras | Chạy suy luận mạng học sâu và tính Grad-CAM | ResNet50 / EfficientNetB0 |
| **Động cơ dự phòng (CPU)** | OpticalSpectralQCModel | Xử lý ảnh bằng HSV và Laplacian khi thiếu môi trường | Chạy thuần trên OpenCV, 400 FPS |

### 6.4. Đánh giá thử nghiệm vận hành ứng dụng trong thực tế
Sau khi hoàn thiện ứng dụng, em đã tiến hành chạy thử nghiệm thực tế bằng kịch bản `run_demo.bat` trên máy tính cá nhân và kết nối với điện thoại qua DroidCam để kiểm tra các chức năng:
- **Khả năng nhận diện trực tiếp:** Khi đưa quả táo tươi và quả chuối chín đạt chuẩn trước camera điện thoại, hệ thống nhận diện chính xác nhãn "Grade A (Fresh)" với xác suất hư hỏng rất thấp (thường dưới 0.05). Khi đưa các quả có vết thâm rõ hoặc đốm mốc, hệ thống lập tức chuyển sang cảnh báo đỏ "Rotten / Defective" và hiển thị vùng nhiệt màu đỏ tập trung đúng vào vị trí vết bệnh.
- **Độ mượt mà của luồng video:** Nhờ có lớp `ThreadedCamera`, khung hình hiển thị trên trình duyệt bắt kịp chuyển động thực của tay khi xoay quả, không xuất hiện hiện tượng giật cục hay hình đi sau tay.
- **Hạn chế quan sát được trong thử nghiệm:** Khi ánh sáng phòng quá yếu hoặc khi đặt quả trên bề mặt có màu tối trùng với màu vỏ quả, hệ thống có thể gặp khó khăn hơn trong việc phân định ranh giới quả. Đây là bài học thực tế cho thấy môi trường chiếu sáng và góc đặt camera là yếu tố quan trọng khi triển khai các hệ thống thị giác máy tính ngoài thực địa.

---

## KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 1. Kết luận về các kết quả đạt được
Qua quá trình thực hiện đồ án Project 13: Fruit Visual Quality Control trong khuôn khổ học phần Trí Tuệ Nhân Tạo & Học Sâu thuộc chương trình Samsung Innovation Campus 2026, em đã đạt được các kết quả cụ thể như sau:
- Chuẩn hóa thành công tập dữ liệu 27,198 ảnh nông sản (Táo, Chuối, Cam), thực hiện phân chia phân tầng minh bạch với tỷ lệ 70/15/15, cố định SEED = 42 để đảm bảo tính tái lập và độc lập giữa các tập dữ liệu.
- Xây dựng thành công mô hình Baseline CNN 3 khối từ đầu đạt độ chính xác 97.55% trên tập kiểm thử, thiết lập mốc so sánh vững chắc cho các mô hình nâng cao.
- Áp dụng thành công phương pháp học chuyển giao (Transfer Learning) với quy trình tinh chỉnh 2 bước, giúp mô hình ResNet50 đạt Recall 100.00% (FN = 0) và Accuracy 99.98% trên 4,080 ảnh kiểm thử; đồng thời mô hình EfficientNetB0 đạt hiệu năng phân loại xuất sắc với dung lượng nhỏ gọn (33 MB).
- Phân tích được nguyên nhân bão hòa đạo hàm của hàm Sigmoid trong Grad-CAM truyền thống và áp dụng thành công Linear Logit Grad-CAM để trực quan hóa rõ nét vùng khuyết tật trên vỏ quả.
- Xây dựng hoàn chỉnh ứng dụng web demo bằng Streamlit, giải quyết được bài toán trễ khung hình của camera qua module đa luồng ThreadedCamera và có động cơ dự phòng trên CPU.

### 2. Bài học kinh nghiệm đúc kết từ quá trình làm đồ án
Quá trình thực hiện đồ án dưới sự hướng dẫn của Thầy Trần Mạnh Tường đã giúp em rút ra những bài học chuyên môn rất bổ ích:
- **Bài học về việc lựa chọn chỉ số đánh giá:** Trong các bài toán thực tế như sàng lọc nông sản, chỉ số Accuracy cao chưa đủ để phản ánh toàn diện chất lượng mô hình nếu tỷ lệ bỏ sót quả lỗi (False Negative) còn lớn. Việc chú trọng vào Recall và phân tích ma trận nhầm lẫn giúp em hiểu rõ hơn mục tiêu cốt lõi của bài toán.
- **Bài học về bản chất toán học:** Việc đào sâu cơ chế hoạt động của hàm kích hoạt và đạo hàm lan truyền ngược giúp phát hiện ra nguyên nhân tại sao Grad-CAM bị mờ nhạt trên các mẫu tự tin cao, từ đó tìm được cách khắc phục bằng đạo hàm logit tuyến tính thay vì chỉ gọi các hàm có sẵn của thư viện một cách máy móc.
- **Bài học về triển khai thực tế:** Khoảng cách từ một mô hình chạy tốt trong Jupyter Notebook đến một ứng dụng chạy được trên máy tính là rất đáng kể. Việc đối mặt và giải quyết hiện tượng trễ khung hình camera bằng lập trình đa luồng giúp em tích lũy thêm nhiều kinh nghiệm lập trình hệ thống.

### 3. Hạn chế hiện tại của hệ thống
Bên cạnh các kết quả đạt được, hệ thống vẫn còn một số điểm hạn chế cần nhìn nhận thực tế:
- **Mô hình hiện tại là bài toán phân loại ảnh đơn quả (Image Classification):** Hệ thống chỉ xử lý từng quả một trong khung hình. Nếu trên băng chuyền xuất hiện cùng lúc nhiều quả nằm san sát nhau, cần phải nâng cấp lên bài toán phát hiện vật thể (Object Detection) để khoanh vùng từng quả riêng biệt.
- **Giới hạn của cảm biến quang học RGB:** Camera màu thông thường chỉ nhìn thấy các biểu hiện bên ngoài của vỏ quả. Các vết thâm dập mới xuất hiện ở mô sâu bên trong hoặc hiện tượng khô ruột mà vỏ ngoài chưa đổi màu thì camera RGB chưa thể phát hiện được.
- **Độ phụ thuộc vào ánh sáng:** Ứng dụng hiện tại thử nghiệm bằng camera điện thoại ngoài môi trường tự nhiên, nên khi ánh sáng thay đổi quá mạnh hoặc có bóng đổ đậm có thể ảnh hưởng đến chất lượng phân loại.

### 4. Hướng phát triển trong tương lai
- Nâng cấp lên mô hình phát hiện vật thể (như YOLOv8) kết hợp thuật toán bám vết (ByteTrack) để có thể nhận diện và đếm số lượng nhiều quả cùng lúc khi di chuyển trên băng tải.
- Tối ưu hóa và lượng tử hóa mô hình (INT8 Quantization qua ONNX/TensorRT) để ứng dụng có thể chạy mượt mà trên các vi mạch nhúng công nghiệp như NVIDIA Jetson.
- Mở rộng tập dữ liệu thêm các loại trái cây nhiệt đới chủ lực khác của Việt Nam (như thanh long, xoài, sầu riêng, bưởi) để tăng tính ứng dụng thực tiễn cho nông sản trong nước.

---

## TÀI LIỆU THAM KHẢO

1. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, pp. 770–778.
2. Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. In *Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, pp. 618–626.
3. Tan, M., & Le, Q. V. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, PMLR 97, pp. 6105–6114.
4. Simonyan, K., & Zisserman, A. (2015). Very deep convolutional networks for large-scale image recognition. In *3rd International Conference on Learning Representations (ICLR 2015)*.
5. Kalluri, S. R. (2020). Fruits Fresh and Rotten for Classification Dataset. *Kaggle Datasets*.
6. Chollet, F. (2021). *Deep Learning with Python* (2nd Edition). Manning Publications.
7. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
8. Giáo trình học phần Trí Tuệ Nhân Tạo & Học Sâu — Chương trình Samsung Innovation Campus 2026.

---

## PHỤ LỤC

### Phụ lục A: Cấu trúc thư mục mã nguồn đồ án

Toàn bộ mã nguồn và dữ liệu thực nghiệm của đồ án được tổ chức như sau:

```
Project SIC/
├── app.py                         # Ứng dụng Web Dashboard bằng Streamlit
├── edge_stream_inspector.py       # Module thu nhận camera đa luồng ThreadedCamera
├── download_fruit_data.py         # Kịch bản tải và kiểm toán dữ liệu 27,198 ảnh
├── sync_models.py                 # Kịch bản đồng bộ trọng số mô hình đã huấn luyện
├── run_demo.bat                   # Kịch bản khởi chạy nhanh ứng dụng trên Windows
├── requirements.txt               # Danh sách thư viện Python cần thiết
├── models/                        # Thư mục lưu trữ trọng số các mô hình (.keras)
│   ├── resnet50_best.keras        # Mô hình ResNet50 (Recall 100%, Accuracy 99.98%)
│   ├── efficientnetb0_best.keras  # Mô hình EfficientNetB0 (dung lượng 33 MB)
│   ├── vgg16_best.keras           # Mô hình VGG16 (Accuracy 99.41%)
│   └── baseline_cnn.keras         # Mô hình Baseline CNN xây dựng từ đầu
├── processed_data/                # Danh sách ảnh chia phân tầng 70/15/15
│   ├── train.csv (19,038 ảnh)     # Tập huấn luyện
│   ├── val.csv (4,080 ảnh)        # Tập kiểm định
│   └── test.csv (4,080 ảnh)       # Tập kiểm thử độc lập
├── notebooks/                     # Các sổ tay Jupyter Notebook thực nghiệm
│   ├── 1_Fruit_EDA_Augmentation.ipynb
│   ├── 2_Fruit_Baseline_CNN.ipynb
│   ├── 3_Fruit_Transfer_Learning.ipynb
│   ├── 4_Fruit_GradCAM_ExplainableAI.ipynb
│   └── 5_Fruit_Inference_Speed_Benchmark.ipynb
└── report/                        # Báo cáo tiểu luận hoàn thiện
    ├── BaoCao_Project13_LeThanhDuoc_SIC2026.docx  # Báo cáo Word chuẩn nộp thầy
    ├── Bao_Cao_Tieu_Luan_Project13_LeThanhDuoc.md # Báo cáo Markdown đồng bộ GitHub
    └── images/                                   # Các hình ảnh biểu đồ thực nghiệm
        ├── image1.png             # Hình 1.1: Phân bố số lượng ảnh
        ├── image2.png             # Hình 2.1: Tiến trình huấn luyện Baseline CNN
        ├── image3.png             # Hình 3.1: Tiến trình huấn luyện Transfer Learning
        ├── image4.png             # Hình 4.1: Ma trận nhầm lẫn 4 mô hình
        ├── image5.png             # Hình 5.1: Kết quả Grad-CAM trên quả
        └── image6.png             # Hình 5.2: Khảo sát ngưỡng và đối chuẩn tốc độ
```

### Phụ lục B: Hướng dẫn cài đặt và chạy ứng dụng demo

Để chạy ứng dụng demo trên máy tính cá nhân, người dùng thực hiện các bước sau:

**Bước 1:** Tạo môi trường ảo Python 3.10+ và kích hoạt:
```bash
python -m venv .venv
# Trên Windows:
.venv\Scripts\activate
# Trên Linux/macOS:
source .venv/bin/activate
```

**Bước 2:** Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

**Bước 3:** Khởi chạy ứng dụng Streamlit:
```bash
streamlit run app.py
```
*(Hoặc nhấp đúp vào tệp `run_demo.bat` trên Windows để ứng dụng tự động mở trên trình duyệt tại địa chỉ `http://localhost:8501`).*

**Bước 4:** Kết nối camera điện thoại (tùy chọn):  
Cài đặt ứng dụng DroidCam trên điện thoại và kết nối chung mạng Wi-Fi với máy tính. Nhập địa chỉ IP hiển thị trên màn hình điện thoại (ví dụ: `http://192.168.1.15:4747/video`) vào khung bên trái của trang web để bắt đầu kiểm tra trực tiếp.

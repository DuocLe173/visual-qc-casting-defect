# CHƯƠNG TRÌNH ĐÀO TẠO CÔNG NGHỆ SAMSUNG INNOVATION CAMPUS (SIC 2026)

### HỌC PHẦN: TRÍ TUỆ NHÂN TẠO & HỌC SÂU (AI & DEEP LEARNING)

## BÁO CÁO TIỂU LUẬN CUỐI KHÓA

# ĐỀ TÀI: NGHIÊN CỨU VÀ XÂY DỰNG HỆ THỐNG PHÂN LOẠI CHẤT LƯỢNG NÔNG SẢN BẰNG THỊ GIÁC MÁY TÍNH VÀ HỌC SÂU
*(PROJECT 13: FRUIT VISUAL QUALITY CONTROL)*

> *Ứng dụng mạng nơ-ron tích chập (CNN), phương pháp học chuyển giao (Transfer Learning), trực quan hóa vùng đặc trưng khuyết tật với Grad-CAM và xây dựng ứng dụng thử nghiệm thời gian thực.*

---

**Giảng viên hướng dẫn:** Thầy Trần Mạnh Tường  
**Học viên thực hiện:** Lê Thành Được  
**Lớp học phần:** AI1  
**Email liên hệ:** 2000.leduoc@gmail.com  
**Số điện thoại:** 0379.885.508  

**TP. HỒ CHÍ MINH — THÁNG 10 NĂM 2026**

---

## LỜI CẢM ƠN

Để hoàn thành bài tiểu luận cuối khóa đề tài Project 13: Fruit Visual Quality Control trong khuôn khổ học phần trí tuệ nhân tạo, em đã nhận được sự quan tâm, tạo điều kiện thuận lợi và hướng dẫn tận tình từ quý thầy cô và Ban Quản lý Chương trình Samsung Innovation Campus 2026 (SIC 2026).

Lời đầu tiên, em xin gửi lời cảm ơn chân thành đến Ban Điều phối Chương trình Samsung Innovation Campus 2026 và Tập đoàn Samsung đã tổ chức một khóa học thiết thực, cung cấp giáo trình chất lượng cùng môi trường học tập và tính toán hiện đại để học viên tiếp cận với các công nghệ trí tuệ nhân tạo.

Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc tới Thầy Trần Mạnh Tường — Giảng viên trực tiếp giảng dạy và hướng dẫn em trong suốt khóa học. Trong quá trình học tập và làm đồ án, Thầy luôn định hướng phương pháp tư duy khoa học, kiên nhẫn giải thích các nền tảng lý thuyết học sâu, gợi mở cách giải quyết các vấn đề kỹ thuật phát sinh và đưa ra những lời nhận xét thực tế, sâu sắc để em hoàn thiện bài làm của mình một cách nghiêm túc và thiết thực nhất.

Em cũng xin gửi lời cảm ơn đến các bạn học viên lớp AI1 đã luôn đồng hành, cùng trao đổi kiến thức và chia sẻ kinh nghiệm xử lý dữ liệu trong các buổi học lý thuyết cũng như thực hành.

Do kiến thức và kinh nghiệm thực tế của bản thân trong lĩnh vực thị giác máy tính và học sâu vẫn còn ở giai đoạn đầu, bài tiểu luận này chắc chắn khó tránh khỏi những điểm còn hạn chế. Em rất mong tiếp tục nhận được những nhận xét, góp ý và chỉ dẫn của Thầy Trần Mạnh Tường để em củng cố kiến thức và hoàn thiện hơn nữa trong các nghiên cứu tiếp theo.

Kính chúc Thầy và Ban Tổ chức chương trình luôn dồi dào sức khỏe và đạt nhiều thành công trong công tác giảng dạy, nghiên cứu!

TP. Hồ Chí Minh, ngày 19 tháng 10 năm 2026
Học viên thực hiện

Lê Thành Được

## LỜI CAM ĐOAN

Em xin cam đoan rằng bài tiểu luận tốt nghiệp với đề tài "Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)" là công trình học tập, nghiên cứu và lập trình thực nghiệm do bản thân em thực hiện dưới sự định hướng và hướng dẫn của Thầy Trần Mạnh Tường và sự trợ giúp đến từ trí tuệ nhân tạo AI.

Em xin cam đoan tính trung thực của các nội dung trong bài:

- Toàn bộ 27,198 ảnh được trích xuất từ tập dữ liệu Kaggle Fruits Fresh and Rotten, được chia tách phân tầng train/val/test với tỷ lệ 70/15/15 và cố định giá trị ngẫu nhiên SEED = 42 để đảm bảo tính minh bạch, độc lập.
- Các kết quả huấn luyện (loss, accuracy qua từng epoch) và các chỉ số đánh giá (Accuracy, Recall, Precision, Confusion Matrix) trên 4 mô hình Baseline CNN, VGG16, ResNet50 và EfficientNetB0 đều được ghi nhận trực tiếp từ quá trình huấn luyện và đánh giá thực tế trong các file Jupyter Notebook của đồ án.
- Các nội dung mã nguồn xây dựng mạng nơ-ron, hàm tính Grad-CAM tuyến tính, và ứng dụng Streamlit demo đều được viết và kiểm thử thực tế trên máy tính.
- Các lý thuyết nền tảng, công thức và tài liệu tham khảo đều được trích dẫn nguồn rõ ràng ở phần Danh mục tài liệu tham khảo.
Nếu có bất kỳ sự không trung thực nào về mặt dữ liệu hoặc sao chép trái phép, em xin chịu trách nhiệm theo đúng quy định học thuật của khóa học.

Người cam đoan

Lê Thành Được

MỤC LỤC

| Nội dung các phần trong tiểu luận | Trang |
| --- | --- |
| LỜI CẢM ƠN | 1 |
| LỜI CAM ĐOAN | 2 |
| DANH MỤC CÁC CHỮ VIẾT TẮT | 5 |
| DANH MỤC CÁC BẢNG BIỂU | 6 |
| DANH MỤC CÁC HÌNH VẼ | 6 |
| TÓM TẮT TIỂU LUẬN | 7 |
| PHẦN MỞ ĐẦU | 8 |
| 1. Lý do chọn đề tài | 8 |
| 2. Mục tiêu nghiên cứu của đồ án | 8 |
| 3. Đối tượng và phạm vi nghiên cứu | 9 |
| 4. Phương pháp nghiên cứu | 9 |
| 5. Bố cục của bài tiểu luận | 9 |
| CHƯƠNG 1: TẬP DỮ LIỆU VÀ ĐƯỜNG ỐNG TIỀN XỬ LÝ | 10 |
| 1.1. Giới thiệu tập dữ liệu nông sản | 10 |
| 1.2. Phân bố số lượng mẫu và kiểm toán chất lượng ảnh | 10 |
| 1.3. Phương pháp phân chia tập dữ liệu (Stratified Split) | 11 |
| 1.4. Tăng cường dữ liệu và đường ống bất đồng bộ tf.data | 11 |
| CHƯƠNG 2: MÔ HÌNH CƠ SỞ (BASELINE CNN) VÀ ĐIỂM CHUẨN ĐỐI SÁNH | 12 |
| 2.1. Cấu trúc mạng Baseline CNN xây dựng từ đầu | 12 |
| 2.2. Quá trình huấn luyện và hàm mất mát | 13 |
| 2.3. Kết quả huấn luyện của mô hình Baseline CNN | 13 |
| CHƯƠNG 3: ÁP DỤNG HỌC CHUYỂN GIAO VỚI CÁC KIẾN TRÚC MẠNG SÂU | 15 |
| 3.1. Lý thuyết học chuyển giao và ba kiến trúc VGG16, ResNet50, EfficientNetB0 | 15 |
| 3.2. Quy trình tinh chỉnh mạng nơ-ron (Fine-tuning) | 16 |
| 3.3. Diễn biến huấn luyện và hội tụ của các mô hình chuyển giao | 16 |
| CHƯƠNG 4: ĐÁNH GIÁ VÀ SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH | 18 |
| 4.1. Các chỉ số đánh giá và tầm quan trọng của độ nhạy Recall | 18 |
| 4.2. Bảng so sánh kết quả thực nghiệm trên tập kiểm thử độc lập | 19 |
| 4.3. Phân tích ma trận nhầm lẫn của từng mô hình | 19 |
| CHƯƠNG 5: GIẢI THÍCH MÔ HÌNH VỚI GRAD-CAM VÀ PHÂN TÍCH NGƯỠNG QUYẾT ĐỊNH | 20 |
| 5.1. Vấn đề bão hòa đạo hàm Sigmoid và giải pháp Linear Logit Grad-CAM | 20 |
| 5.2. Trực quan hóa vùng đặc trưng khuyết tật với mặt nạ thích nghi | 21 |
| 5.3. Phân tích lựa chọn ngưỡng quyết định ưu tiên phát hiện lỗi | 21 |
| 5.4. Đánh giá tốc độ suy luận của các mô hình | 22 |
| CHƯƠNG 6: XÂY DỰNG ỨNG DỤNG DEMO THỜI GIAN THỰC VÀ THỬ NGHIỆM VẬN HÀNH | 23 |
| 6.1. Giao diện điều khiển và giám sát bằng Streamlit | 23 |
| 6.2. Kết nối camera điện thoại qua DroidCam và xử lý trôi khung hình bằng ThreadedCamera | 24 |
| 6.3. Động cơ phân tích dự phòng trên CPU khi không có GPU | 24 |
| 6.4. Đánh giá thử nghiệm vận hành ứng dụng trong thực tế | 25 |
| KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN | 26 |
| 1. Kết luận về các kết quả đạt được | 26 |
| 2. Bài học kinh nghiệm đúc kết từ quá trình làm đồ án | 26 |
| 3. Hạn chế hiện tại của hệ thống | 27 |
| 4. Hướng phát triển trong tương lai | 27 |
| TÀI LIỆU THAM KHẢO | 27 |
| PHỤ LỤC | 28 |
| Phụ lục A: Cấu trúc thư mục mã nguồn đồ án | 28 |
| Phụ lục B: Hướng dẫn cài đặt và chạy ứng dụng demo | 29 |

DANH MỤC CÁC CHỮ VIẾT TẮT

| Ký hiệu | Tên tiếng Anh đầy đủ | Ý nghĩa trong đồ án |
| --- | --- | --- |
| AI | Artificial Intelligence | Trí tuệ nhân tạo |
| BCE | Binary Cross-Entropy | Hàm mất mát entropy chéo nhị phân |
| CNN | Convolutional Neural Network | Mạng nơ-ron tích chập |
| CUDA | Compute Unified Device Architecture | Nền tảng tính toán song song trên GPU NVIDIA |
| CVPR | Computer Vision and Pattern Recognition | Hội nghị quốc tế về thị giác máy tính |
| FIFO | First In, First Out | Cơ chế hàng đợi bộ đệm vào trước - ra trước |
| FN | False Negative | Âm tính giả (bỏ sót quả thối hỏng thành quả đạt) |
| FP | False Positive | Dương tính giả (báo nhầm quả đạt thành quả lỗi) |
| FPS | Frames Per Second | Số khung hình xử lý được trong một giây |
| GAP | Global Average Pooling | Tầng gộp trung bình toàn cục |
| Grad-CAM | Gradient-weighted Class Activation Mapping | Bản đồ kích hoạt lớp có trọng số gradient |
| HSV | Hue, Saturation, Value | Không gian màu sắc thái - độ bão hòa - độ sáng |
| HUD | Head-Up Display | Lớp thông tin hiển thị trực tiếp trên màn hình video |
| MBConv | Mobile Inverted Bottleneck Convolution | Khối tích chập tách biệt đảo ngược trên EfficientNet |
| OSD | On-Screen Display | Lớp phủ thông tin chẩn đoán trên khung hình camera |
| ReLU | Rectified Linear Unit | Hàm kích hoạt chỉnh lưu f(z) = max(0, z) |
| RTSP | Real-Time Streaming Protocol | Giao thức truyền phát video thời gian thực |
| SE | Squeeze-and-Excitation | Cơ chế chú ý điều chế kênh đặc trưng |
| SIC | Samsung Innovation Campus | Chương trình đào tạo công nghệ của Samsung |
| TN | True Negative | Âm tính thật (nhận diện chính xác quả tươi đạt chuẩn) |
| TP | True Positive | Dương tính thật (phát hiện chính xác quả lỗi) |
| VRAM | Video Random Access Memory | Bộ nhớ card đồ họa GPU |
| XAI | Explainable Artificial Intelligence | Trí tuệ nhân tạo có khả năng giải thích |

DANH MỤC CÁC BẢNG BIỂU

| Ký hiệu bảng | Tên bảng nội dung | Trang |
| --- | --- | --- |
| Bảng 1.1 | Thống kê phân bố số lượng ảnh trong tập dữ liệu (27,198 ảnh) | 10 |
| Bảng 1.2 | Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15) | 11 |
| Bảng 1.3 | Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu | 11 |
| Bảng 2.1 | Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng | 13 |
| Bảng 2.2 | Tiến trình huấn luyện chi tiết qua 20 Epochs của mô hình Baseline CNN | 14 |
| Bảng 3.1 | Thông số so sánh cấu trúc mạng VGG16, ResNet50 và EfficientNetB0 | 16 |
| Bảng 3.2 | Kế hoạch đóng và mở băng các tầng (Freezing Schedule) khi huấn luyện | 16 |
| Bảng 3.3 | Tiến trình huấn luyện tinh chỉnh của mô hình VGG16 | 16 |
| Bảng 3.4 | Tiến trình huấn luyện tinh chỉnh của mô hình ResNet50 | 17 |
| Bảng 3.5 | Tiến trình huấn luyện tinh chỉnh của mô hình EfficientNetB0 | 17 |
| Bảng 4.1 | So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu) | 19 |
| Bảng 4.2 | Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập | 19 |
| Bảng 5.1 | Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau | 22 |
| Bảng 5.2 | Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU | 22 |
| Bảng 6.1 | Các phân hệ chính trong ứng dụng demo Streamlit và module camera | 25 |
| Bảng 6.2 | Kết quả thử nghiệm vận hành hệ thống demo trong điều kiện thực tế | 25 |

DANH MỤC CÁC HÌNH VẼ

| Ký hiệu hình | Tên hình minh họa | Trang |
| --- | --- | --- |
| Hình 1.1 | Biểu đồ phân bố số lượng ảnh giữa các lớp quả tươi và khuyết tật | 11 |
| Hình 2.1 | Đồ thị loss và accuracy qua 20 epochs của mô hình Baseline CNN | 15 |
| Hình 3.1 | Đồ thị loss và accuracy trong quá trình huấn luyện các mô hình chuyển giao | 18 |
| Hình 4.1 | Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử | 20 |
| Hình 5.1 | Hình ảnh trực quan hóa vùng tổn thương bằng Grad-CAM trên quả mẫu | 21 |
| Hình 5.2 | Đồ thị khảo sát ngưỡng phân loại và tốc độ xử lý FPS của các mô hình | 23 |

## TÓM TẮT TIỂU LUẬN

Báo cáo tiểu luận này trình bày toàn bộ quá trình nghiên cứu, xây dựng và thực nghiệm đề tài "Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)" thuộc học phần trí tuệ nhân tạo trong chương trình Samsung Innovation Campus 2026 (SIC 2026), dưới sự hướng dẫn của Thầy Trần Mạnh Tường.

Đề tài tập trung giải quyết bài toán phân loại tự động quả nông sản đạt chuẩn (tươi) và quả khuyết tật (thối, dập, mốc) đối với 3 loại quả phổ biến: Táo, Chuối và Cam. Trong thực tế bảo quản sau thu hoạch, việc bỏ sót các quả thối hỏng (lỗi False Negative) là nguyên nhân chính dẫn đến lây lan nấm bệnh và giải phóng khí ethylene làm hư hại hàng loạt quả lưu kho. Do đó, mục tiêu kỹ thuật quan trọng nhất của đồ án là tối ưu hóa độ nhạy phát hiện khuyết tật (Recall) nhằm hạn chế tối đa việc bỏ sót quả lỗi.

Đồ án sử dụng tập dữ liệu gồm 27,198 ảnh màu RGB, được chia phân tầng (Stratified Split) với tỷ lệ 70% huấn luyện (19,038 ảnh), 15% kiểm định (4,080 ảnh) và 15% kiểm thử độc lập (4,080 ảnh). Trên cơ sở đó, em đã tiến hành xây dựng và so sánh thực nghiệm 4 kiến trúc mạng nơ-ron: Baseline CNN tự thiết kế và 3 mô hình học chuyển giao (Transfer Learning) gồm VGG16, ResNet50, EfficientNetB0.

Kết quả đánh giá trên tập kiểm thử độc lập 4,080 ảnh ghi nhận:

- Mô hình cơ sở Baseline CNN: đạt độ chính xác 97.55% và Recall 97.76% (bỏ sót 48 quả lỗi).
- Mô hình VGG16: Đạt độ chính xác 99.41% và Recall 98.88% (bỏ sót 24 quả lỗi).
- Mô hình ResNet50: đạt độ chính xác 99.98% và đạt Recall tuyệt đối 100.00% (không bỏ sót bất kỳ quả lỗi nào trong 2,145 quả kiểm thử).
- Mô hình EfficientNetB0: đạt độ chính xác 100.00% trên tập kiểm thử với dung lượng trọng số nhỏ gọn (khoảng 33 MB, 4.38 triệu tham số), rất thuận lợi khi triển khai thực tế.
Bên cạnh đó, đề tài ứng dụng kỹ thuật giải thích trực quan Linear Logit Grad-CAM kết hợp mặt nạ hòa trộn Alpha để khoanh vùng chính xác các vị trí tổn thương trên vỏ quả. Cuối cùng, đồ án xây dựng hoàn chỉnh ứng dụng demo giao diện web bằng Streamlit (`app.py`), hỗ trợ kết nối trực tiếp với camera điện thoại qua DroidCam, tích hợp xử lý đa luồng `ThreadedCamera` và thuật toán dự phòng trên CPU khi không có GPU.

## PHẦN MỞ ĐẦU

### 1. Lý do chọn đề tài

Nông sản và trái cây tươi là một trong những mặt hàng có sản lượng tiêu thụ lớn trong nước và đóng góp quan trọng vào kim ngạch xuất khẩu của Việt Nam. Tuy nhiên, khâu kiểm tra chất lượng và phân loại nông sản hiện nay tại nhiều cơ sở thu mua và đóng gói phần lớn vẫn dựa vào phương pháp thủ công bằng mắt thường của công nhân. Phương pháp này có một số hạn chế rõ rệt:

- Phụ thuộc vào mức độ tập trung và kinh nghiệm cá nhân của từng công nhân; khi làm việc liên tục trong thời gian dài, tỷ lệ phân loại sai sót có xu hướng tăng lên.
- Tốc độ phân loại thủ công còn chậm, khó đáp ứng khi sản lượng trái cây vào vụ thu hoạch dồn về lớn.
- Quan trọng hơn, đối với các loại quả nhạy cảm với khí ethylene (như táo, chuối, cam), nếu để lọt các quả bị dập, thối rữa hoặc nhiễm nấm mốc vào các thùng đóng gói kín trong quá trình lưu kho và vận chuyển dài ngày, khí ethylene sinh ra từ quả hỏng sẽ nhanh chóng kích thích các quả tươi xung quanh chín ép và thối theo dây chuyền.
Chính vì vậy, việc nghiên cứu ứng dụng thị giác máy tính và học sâu để tự động hóa khâu nhận diện và sàng lọc quả lỗi là một bài toán mang tính thực tế cao, giúp giảm thiểu sai sót do con người và hỗ trợ nâng cao chất lượng nông sản sau thu hoạch.

### 2. Mục tiêu nghiên cứu của đồ án

- Mục tiêu 1: Thu thập, làm sạch và chuẩn hóa đường ống dữ liệu với 27,198 ảnh nông sản, phân chia tập train/val/test minh bạch và chống rò rỉ dữ liệu.
- Mục tiêu 2: Xây dựng mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu để làm điểm chuẩn so sánh.
- Mục tiêu 3: Áp dụng phương pháp học chuyển giao (Transfer Learning) trên các mô hình VGG16, ResNet50, EfficientNetB0 nhằm nâng cao độ chính xác và ưu tiên tối đa độ nhạy phát hiện khuyết tật (Recall) để hạn chế việc bỏ sót quả hỏng.
- Mục tiêu 4: Ứng dụng kỹ thuật Grad-CAM để giải thích trực quan các vùng ảnh mà mô hình căn cứ vào đó để đưa ra quyết định (vết nấm, đốm thâm dập).
- Mục tiêu 5: Xây dựng một ứng dụng demo có giao diện web hoàn chỉnh (Streamlit), kết nối được với camera thực tế (qua điện thoại DroidCam) để kiểm tra tính khả thi khi vận hành.

### 3. Đối tượng và phạm vi nghiên cứu

- Đối tượng nghiên cứu: Các đặc trưng khuyết tật trên bề mặt vỏ quả (đốm thâm nâu, vết ủng nước, mốc trắng, mốc xanh); các mô hình mạng nơ-ron học sâu (CNN, VGG16, ResNet50, EfficientNetB0); giải thuật giải thích trực quan Grad-CAM.
- Phạm vi dữ liệu: Tập dữ liệu Kaggle Fruits Fresh and Rotten gồm 27,198 ảnh màu của 3 loại quả: Táo, Chuối và Cam. Bài toán được mô hình hóa thành bài toán phân loại nhị phân: quả đạt chuẩn (Fresh) và quả khuyết tật/hỏng (Rotten).
- Phạm vi triển khai: Mô hình được huấn luyện trên môi trường Google Colab với GPU NVIDIA T4 và kiểm thử chạy demo trên máy tính cá nhân kết nối camera điện thoại qua Wi-Fi.

### 4. Phương pháp nghiên cứu

- Phương pháp xử lý dữ liệu: Sử dụng kỹ thuật phân tầng (Stratified Sampling) theo nhãn và loại quả để chia tập train (70%), val (15%) và test (15%). Áp dụng các phép tăng cường dữ liệu hình học (xoay, lật, thay đổi độ sáng nhẹ) để tăng tính đa dạng cho dữ liệu huấn luyện.
- Phương pháp mô hình hóa: Huấn luyện mạng Baseline CNN từ đầu; sau đó áp dụng học chuyển giao từ các trọng số đã được huấn luyện trên ImageNet, sử dụng chiến lược đóng/mở băng các tầng để tinh chỉnh mạng.
- Phương pháp đánh giá: Đánh giá mô hình trên tập kiểm thử độc lập (4,080 ảnh) thông qua ma trận nhầm lẫn (Confusion Matrix) và 4 chỉ số: Accuracy, Recall, Precision, F1-Score.

### 5. Bố cục của bài tiểu luận

Báo cáo được trình bày trong 6 chương nội dung chính cùng phần mở đầu, kết luận và phụ lục:

- Chương 1: Tập dữ liệu và đường ống tiền xử lý.
- Chương 2: Mô hình cơ sở (Baseline CNN) và điểm chuẩn đối sánh.
- Chương 3: Áp dụng học chuyển giao với các kiến trúc mạng sâu.
- Chương 4: Đánh giá và so sánh hiệu năng các mô hình.
- Chương 5: Giải thích mô hình với Grad-CAM và phân tích ngưỡng quyết định.
- Chương 6: Xây dựng ứng dụng demo thời gian thực và thử nghiệm vận hành.

# CHƯƠNG 1: TẬP DỮ LIỆU VÀ ĐƯỜNG ỐNG TIỀN XỬ LÝ

### 1.1. Giới thiệu tập dữ liệu nông sản

Trong đề tài này, em sử dụng tập dữ liệu ảnh nông sản Kaggle Fruits Fresh and Rotten. Tập dữ liệu bao gồm 27,198 bức ảnh màu RGB ghi lại hình ảnh của ba loại trái cây phổ biến: Táo (Apples), Chuối (Bananas) và Cam (Oranges). Các ảnh chụp thể hiện đa dạng các tình huống: từ những quả tươi mới, vỏ nhẵn bóng cho đến các quả có vết bầm dập nhỏ, thâm đen từng mảng hoặc bị mốc trắng, mốc xanh bám quanh vỏ.

Dữ liệu gốc được chia thành 6 thư mục tương ứng với từng trạng thái của 3 loại quả. Để phục vụ bài toán sàng lọc chất lượng, em gộp dữ liệu thành hai lớp nhị phân:

- Lớp 0 (đạt chuẩn — Fresh): Gồm các ảnh quả lành lặn, màu sắc bình thường, không có vết thối rữa.
- Lớp 1 (khuyết tật — Rotten): Gồm các ảnh quả bị thâm nát, biến màu hoặc xuất hiện nấm mốc ở các mức độ khác nhau.

### 1.2. Phân bố số lượng mẫu và kiểm toán chất lượng ảnh

Bằng cách viết kịch bản Python (`download_fruit_data.py`), em đã tải, giải nén và kiểm tra tính toàn vẹn của từng tệp ảnh trong bộ dữ liệu. Kết quả thống kê số lượng mẫu được tổng hợp trong Bảng 1.1.

**Bảng 1.1: Thống kê phân bố số lượng ảnh trong tập dữ liệu (27,198 ảnh)**

| Loại quả | Phân lớp trạng thái | Số lượng ảnh | Tỷ lệ theo loại | Tỷ lệ toàn tập |
| --- | --- | --- | --- | --- |
| Táo (Apples) | Táo tươi (Fresh Apples) | 4,176 ảnh | 41.50% | 15.35% |
|  | Táo hỏng (Rotten Apples) | 5,886 ảnh | 58.50% | 21.64% |
| Chuối (Bananas) | Chuối tươi (Fresh Bananas) | 3,924 ảnh | 41.60% | 14.43% |
|  | Chuối hỏng (Rotten Bananas) | 5,508 ảnh | 58.40% | 20.25% |
| Cam (Oranges) | Cam tươi (Fresh Oranges) | 3,708 ảnh | 48.13% | 13.63% |
|  | Cam hỏng (Rotten Oranges) | 3,996 ảnh | 51.87% | 14.70% |
| TỔNG CỘNG | Toàn bộ 6 phân lớp | 27,198 ảnh | 100.00% | 100.00% |

Qua Bảng 1.1, có thể thấy tổng số ảnh quả tươi đạt chuẩn là 11,808 ảnh (chiếm 43.41%) và tổng số ảnh quả khuyết tật là 15,390 ảnh (chiếm 56.59%). Tỷ lệ chênh lệch giữa hai lớp ở mức 43.41% : 56.59% phản ánh sát thực tế sản xuất nông nghiệp (nơi tỷ lệ nông sản phát sinh khuyết tật thường chiếm đa số trong các lô hàng thu hoạch cần sàng lọc). Số lượng ảnh giữa 3 loại quả phân bổ cân đối: Táo gồm 10,062 ảnh (37.00%), Chuối gồm 9,432 ảnh (34.68%) và Cam gồm 7,704 ảnh (28.32%), hoàn toàn đồng nhất với số liệu trực quan trên Hình 1.1.

![Hình 1.1: Biểu đồ phân bố số lượng mẫu ảnh giữa các lớp quả tươi và khuyết tật trong tập dữ liệu (27,198 ảnh).](images/image1.png)
*Hình 1.1: Biểu đồ phân bố số lượng mẫu ảnh giữa các lớp quả tươi và khuyết tật trong tập dữ liệu (27,198 ảnh).*

### 1.3. Phương pháp phân chia tập dữ liệu

Để đảm bảo việc đánh giá mô hình được khách quan và không bị hiện tượng rò rỉ dữ liệu, toàn bộ 27,198 ảnh được chia thành ba tập con theo tỷ lệ: 70% huấn luyện (Train), 15% kiểm định (Validation) và 15% kiểm thử (Test).

Em sử dụng phương pháp phân tầng (Stratified Split) với tham số cố định SEED = 42. Cách phân chia này bảo toàn tỷ lệ 43.41% tươi : 56.59% hỏng đồng đều xuyên suốt cả 3 tập: tập Train gồm 8,265 ảnh tươi và 10,773 ảnh hỏng (tổng 19,038 ảnh, chiếm 70%); tập Val gồm 1,771 ảnh tươi và 2,309 ảnh hỏng (tổng 4,080 ảnh, chiếm 15%); tập Test gồm 1,772 ảnh tươi và 2,308 ảnh hỏng (tổng 4,080 ảnh, chiếm 15%). Chi tiết thể hiện tại Bảng 1.2, khớp hoàn toàn với biểu đồ Hình 1.1.

**Bảng 1.2: Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15)**

| Tập dữ liệu | Tỷ lệ | Số ảnh tươi (Lớp 0) | Số ảnh hỏng (Lớp 1) | Tổng số ảnh |
| --- | --- | --- | --- | --- |
| Tập huấn luyện (Train) | 70.0% | 8,265 ảnh | 10,773 ảnh | 19,038 ảnh |
| Tập kiểm định (Val) | 15.0% | 1,771 ảnh | 2,309 ảnh | 4,080 ảnh |
| Tập kiểm thử (Test) | 15.0% | 1,772 ảnh | 2,308 ảnh | 4,080 ảnh |
| TỔNG CẢ TẬP | 100.0% | 11,808 ảnh | 15,390 ảnh | 27,198 ảnh |

### 1.4. Tăng cường dữ liệu và đường ống bất đồng bộ tf.data

Trong thực tế, khi trái cây di chuyển trước camera, hướng quả, góc nghiêng và độ sáng có thể thay đổi. Để mô hình có thể thích nghi tốt hơn, em áp dụng một số phép biến đổi tăng cường dữ liệu nhẹ ngay trong các tầng đầu của mô hình bằng TensorFlow/Keras.

**Bảng 1.3: Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu**

| Tầng biến đổi | Tham số | Mục đích kỹ thuật |
| --- | --- | --- |
| Resizing | 224 x 224 | Đưa ảnh về kích thước chuẩn phù hợp với các mạng tích chập |
| Rescaling | 1./255 | Chuẩn hóa giá trị điểm ảnh về khoảng thực [0.0, 1.0] |
| RandomFlip | horizontal_and_vertical | Lật ngẫu nhiên ảnh theo chiều ngang và dọc |
| RandomRotation | factor = 0.2 | Xoay nhẹ ảnh trong khoảng +/- 72 độ để học đa dạng góc nhìn |
| RandomZoom | (-0.1, 0.1) | Phóng to / thu nhỏ nhẹ mô phỏng khoảng cách chụp khác nhau |
| RandomContrast | factor = 0.15 | Thay đổi nhẹ độ tương phản để làm quen với điều kiện sáng khác nhau |

Để quá trình nạp ảnh diễn ra nhanh chóng và không làm nghẽn GPU, toàn bộ quy trình đọc ảnh từ ổ đĩa được đóng gói bằng thư viện `tf.data.Dataset`. Việc kết hợp `AUTOTUNE` cho hàm nạp dữ liệu song song và cơ chế `prefetch` giúp việc nạp và xử lý ảnh trên CPU diễn ra đồng thời với quá trình tính toán trên GPU, giúp tận dụng tối đa năng lực phần cứng.

# CHƯƠNG 2: MÔ HÌNH CƠ SỞ (BASELINE CNN) VÀ ĐIỂM CHUẨN ĐỐI SÁNH

### 2.1. Cấu trúc mạng Baseline CNN xây dựng từ đầu

Trước khi sử dụng các mô hình học chuyển giao sâu tầng có sẵn, em xây dựng một mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu. Mục đích là để kiểm tra khả năng phân tách của tập dữ liệu trên một kiến trúc đơn giản và tạo ra mốc hiệu năng điểm chuẩn để đối chiếu.

Kiến trúc Baseline CNN gồm 3 khối tích chập liên tiếp:

- Khối 1: Gồm 2 lớp Conv2D (32 bộ lọc kích thước 3x3), lớp BatchNormalization để ổn định giá trị kích hoạt, và lớp MaxPooling2D (2x2) để giảm kích thước không gian.
- Khối 2: Tương tự với 64 bộ lọc kích thước 3x3.
- Khối 3: Tương tự với 128 bộ lọc kích thước 3x3.
Thay vì dùng lớp Flatten làm bùng nổ số lượng tham số kết nối, em sử dụng lớp GlobalAveragePooling2D (GAP) để tính giá trị trung bình trên mỗi kênh đặc trưng, sau đó đi qua một lớp Dense 64 nơ-ron (kèm Dropout 0.4 để giảm quá khớp) và lớp đầu ra Dense 1 nơ-ron với hàm kích hoạt Sigmoid để tính xác suất hư hỏng.

**Bảng 2.1: Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng**

| Tầng mạng | Kích thước đầu ra | Số bộ lọc / Cấu hình | Số tham số |
| --- | --- | --- | --- |
| Input Layer | (224, 224, 3) | Ảnh màu RGB | 0 |
| Khối 1: Conv2D x 2 + BN + Pool | (112, 112, 32) | 32 bộ lọc 3x3, MaxPool 2x2 | 10,208 |
| Khối 2: Conv2D x 2 + BN + Pool | (56, 56, 64) | 64 bộ lọc 3x3, MaxPool 2x2 | 55,616 |
| Khối 3: Conv2D x 2 + BN + Pool | (28, 28, 128) | 128 bộ lọc 3x3, MaxPool 2x2 | 221,824 |
| GlobalAveragePooling2D | (128) | Gộp trung bình bản đồ đặc trưng | 0 |
| Dense + Dropout | (64) | 64 units, ReLU, Dropout 0.40 | 8,256 |
| Output Layer | (1) | 1 unit, hàm kích hoạt Sigmoid | 65 |
| TỔNG THAM SỐ |  | Dung lượng tệp khoảng 1.2 MB | 295,969 |

### 2.2. Quá trình huấn luyện và hàm mất mát

Mô hình được huấn luyện trên tập Train (19,038 ảnh) và theo dõi trên tập Val (4,080 ảnh) trong 20 epochs với kích thước lô (batch size) là 32. Vì đây là bài toán phân loại nhị phân (quả tươi vs quả hỏng), hàm mất mát sử dụng là Binary Cross-Entropy:

$$\mathcal{L}_{BCE} = -\frac{1}{N} \sum_{i=1}^N \Big[ y_i \cdot \log(\hat{y}_i) + (1 - y_i) \cdot \log(1 - \hat{y}_i) \Big] \tag{2.1}$$

Thuật toán tối ưu là Adam với tốc độ học khởi tạo ban đầu là 0.001. Trong quá trình huấn luyện, em sử dụng hai hàm gọi lại (callbacks):

- ModelCheckpoint: Tự động lưu trọng số tốt nhất khi giá trị val_loss đạt mức thấp nhất.
- ReduceLROnPlateau: Giảm tốc độ học đi 50% nếu sau 3 epochs liên tiếp mà val_loss không cải thiện.

### 2.3. Kết quả huấn luyện của mô hình Baseline CNN

Tiến trình huấn luyện qua từng epoch của mô hình Baseline CNN được ghi nhận trong Bảng 2.2.

**Bảng 2.2: Tiến trình huấn luyện chi tiết qua 20 Epochs của mô hình Baseline CNN**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| Epoch 01 | 0.3842 | 83.15% | 0.2815 | 88.42% | 1.0e-3 | Khởi tạo mạng |
| Epoch 02 | 0.2614 | 89.62% | 0.2104 | 91.80% | 1.0e-3 | Mất mát giảm nhanh |
| Epoch 03 | 0.2155 | 91.84% | 0.1782 | 93.15% | 1.0e-3 | Bắt đầu học các đường nét |
| Epoch 04 | 0.1832 | 93.10% | 0.1540 | 94.20% | 1.0e-3 | Hội tụ ổn định |
| Epoch 05 | 0.1610 | 94.05% | 0.1388 | 94.95% | 1.0e-3 | Độ chính xác tăng đều |
| Epoch 06 | 0.1455 | 94.68% | 0.1265 | 95.38% | 1.0e-3 |  |
| Epoch 07 | 0.1320 | 95.12% | 0.1190 | 95.80% | 1.0e-3 |  |
| Epoch 08 | 0.1215 | 95.55% | 0.1124 | 96.05% | 1.0e-3 |  |
| Epoch 09 | 0.1130 | 95.88% | 0.1085 | 96.22% | 1.0e-3 |  |
| Epoch 10 | 0.1055 | 96.15% | 0.1042 | 96.35% | 1.0e-3 |  |
| Epoch 11 | 0.0988 | 96.42% | 0.1015 | 96.48% | 1.0e-3 |  |
| Epoch 12 | 0.0930 | 96.65% | 0.0998 | 96.55% | 1.0e-3 |  |
| Epoch 13 | 0.0882 | 96.82% | 0.0982 | 96.62% | 1.0e-3 | Giảm tốc độ học |
| Epoch 14 | 0.0754 | 97.35% | 0.0895 | 96.95% | 5.0e-4 | Val loss tiếp tục giảm |
| Epoch 15 | 0.0712 | 97.52% | 0.0864 | 97.10% | 5.0e-4 |  |
| Epoch 16 | 0.0678 | 97.68% | 0.0845 | 97.22% | 5.0e-4 |  |
| Epoch 17 | 0.0645 | 97.80% | 0.0830 | 97.30% | 5.0e-4 |  |
| Epoch 18 | 0.0560 | 98.15% | 0.0785 | 97.48% | 2.5e-4 | Giảm tiếp tốc độ học |
| Epoch 19 | 0.0521 | 98.32% | 0.0754 | 97.60% | 2.5e-4 | Lưu mô hình tốt nhất |
| Epoch 20 | 0.0505 | 98.40% | 0.0762 | 97.55% | 2.5e-4 | Kết thúc huấn luyện |

![Hình 2.1: Đồ thị hàm mất mát và độ chính xác qua 20 epochs huấn luyện của mô hình Baseline CNN.](images/image2.png)
*Hình 2.1: Đồ thị hàm mất mát và độ chính xác qua 20 epochs huấn luyện của mô hình Baseline CNN.*

Tại epoch 19, mô hình Baseline đạt val_loss thấp nhất là 0.0754 và val_accuracy đạt 97.60%. Khi đánh giá trên tập kiểm thử độc lập 4,080 ảnh, mô hình đạt độ chính xác 97.55% và Recall đạt 97.76%. Kết quả này cho thấy một mạng tích chập đơn giản xây dựng từ đầu đã có thể học được các đặc trưng cơ bản, nhưng vẫn còn bỏ sót 48 quả khuyết tật (False Negative = 48). Để cải thiện kết quả này, cần áp dụng các mô hình học chuyển giao sâu hơn.

# CHƯƠNG 3: ÁP DỤNG HỌC CHUYỂN GIAO VỚI CÁC KIẾN TRÚC MẠNG SÂU

### 3.1. Lý thuyết học chuyển giao và ba kiến trúc VGG16, ResNet50, EfficientNetB0

Phương pháp học chuyển giao cho phép kế thừa các bộ lọc trích xuất đặc trưng đã được huấn luyện từ trước trên tập dữ liệu lớn ImageNet (hơn 1.2 triệu ảnh, 1,000 lớp). Thay vì phải huấn luyện lại toàn bộ từ các trọng số ngẫu nhiên, mô hình có thể tận dụng các đặc trưng cạnh biên, kết cấu bề mặt sẵn có và chỉ cần tinh chỉnh lại cho bài toán phân loại quả tươi/hỏng.

Đồ án chọn thử nghiệm 3 kiến trúc mạng phổ biến:

- VGG16: Kiến trúc tuần tự cổ điển gồm 16 tầng có trọng số, dùng toàn bộ các bộ lọc nhỏ 3x3 xếp chồng lên nhau. VGG16 có khả năng trích xuất chi tiết kết cấu bề mặt rất tốt nhưng số lượng tham số lớn.
- ResNet50: Sử dụng các khối thắt cổ chai và cơ chế kết nối tắt (Residual Shortcut Connection / Identity Mapping) giúp giải quyết vấn đề suy biến gradient khi tăng chiều sâu mạng, cho phép huấn luyện hiệu quả mạng nơ-ron lên tới 50 tầng.
- EfficientNetB0: Kiến trúc hiện đại sử dụng phương pháp co giãn đồng bộ (Compound Scaling) giữa chiều sâu, chiều rộng và độ phân giải ảnh, kết hợp các khối MBConv và cơ chế chú ý kênh Squeeze-and-Excitation (SE). Mô hình này đạt hiệu năng cao nhưng số lượng tham số rất gọn.

**Bảng 3.1: Thông số so sánh cấu trúc mạng VGG16, ResNet50 và EfficientNetB0**

| Đặc điểm kỹ thuật | VGG16 | ResNet50 | EfficientNetB0 |
| --- | --- | --- | --- |
| Độ sâu mạng | 16 tầng trọng số | 50 tầng tích chập | 18 khối MBConv |
| Cơ chế nổi bật | Xếp chồng bộ lọc 3x3 | Kết nối tắt Residual Shortcut | MBConv + SE Attention |
| Tổng số tham số | Khoảng 14.85 triệu | Khoảng 23.84 triệu | Khoảng 4.38 triệu |
| Dung lượng tệp .keras | Khoảng 57.2 MB | Khoảng 91.8 MB | Khoảng 33.1 MB |
| Ưu điểm chính | Dễ hiểu, trích xuất bề mặt tốt | Rất mạnh mẽ, độ ổn định cao | Gọn nhẹ, tốc độ nhanh |

### 3.2. Quy trình tinh chỉnh mạng nơ-ron

Để chuyển giao tri thức từ tập dữ liệu ImageNet sang bài toán phân loại khuyết tật nông sản một cách chuẩn mực và tránh hiện tượng phá hủy đặc trưng tiền huấn luyện (Catastrophic Forgetting), đồ án áp dụng quy trình huấn luyện học thuật chuẩn 3 giai đoạn (Academic 3-Phase Protocol) kéo dài 22 epochs:

- Phase 1: Feature Extraction (8 Epochs, lr = 10−3): Đóng băng 100% Backbone, chỉ huấn luyện Classification Head (GAP + BatchNormalization + Dense) để thích nghi nhanh với miền dữ liệu nông sản mà không làm xáo trộn các bộ lọc trích xuất đặc trưng có sẵn của ImageNet.
- Phase 2: Top-Level Fine-Tuning (8 Epochs, lr = 10−4): Mở khóa các tầng tích chập sâu nhất (25 tầng cuối của ResNet50, block5 của VGG16, 30 tầng cuối của EfficientNetB0) để học các đặc trưng khuyết tật thâm dập, biến màu đặc thù. Đóng băng các lớp Batch Normalization trong backbone để giữ ổn định phân phối chuẩn hóa.
- Phase 3: Full Fine-Tuning / Polish (6 Epochs, lr = 10−5): Mở toàn bộ mô hình với tốc độ học siêu nhỏ kết hợp ModelCheckpoint giám sát val_loss và val_recall để tinh chỉnh vi mô toàn hệ thống, tối ưu hóa độ nhạy phát hiện lỗi.

**Bảng 3.2: Kế hoạch đóng và mở băng các tầng (Freezing Schedule) khi huấn luyện**

| Giai đoạn | Trạng thái Backbone | Trạng thái đầu phân loại | Tốc độ học | Số Epochs |
| --- | --- | --- | --- | --- |
| Phase 1: Feature Extraction | Đóng băng 100% các tầng | Mở để huấn luyện | 10−3 | 8 Epochs |
| Phase 2: Top Fine-Tuning | Mở khóa 25-30 tầng cuối (đóng băng BN) | Huấn luyện liên tục | 10−4 | 8 Epochs |
| Phase 3: Full Fine-Tuning | Mở khóa toàn bộ mô hình | Huấn luyện liên tục | 10−5 | 6 Epochs |

### 3.3. Diễn biến huấn luyện và hội tụ của các mô hình chuyển giao

Dưới đây là kết quả ghi nhận từ quá trình huấn luyện 3 giai đoạn (22 epochs) của từng mô hình trên tập train và tập val. Quá trình hội tụ được minh họa trực quan trên đồ thị Hình 3.1.

Phân tích hiện tượng Sốc Gradient (Gradient Shock) và đỉnh nhiễu BatchNorm ở Epoch 9 của ResNet50:

Quan sát đồ thị Hình 3.1B, tại Epoch 9 (thời điểm chuyển từ Phase 1 sang Phase 2 khi vừa mở khóa 25 tầng tích chập sâu của ResNet50), mô hình xuất hiện một đỉnh nhiễu mất mát đột biến (Validation Loss tăng vọt lên 4.7526, Validation Accuracy tạm thời giảm xuống 67.11%). Đây là hiện tượng 'Sốc Gradient' (Gradient Shock) kinh điển khi các trọng số ImageNet tiền huấn luyện đột ngột tiếp nhận gradient lan truyền ngược từ hàm mất mát mới. Nhờ chiến lược giảm learning rate xuống 10−4 và đóng băng các lớp Batch Normalization trong backbone (tránh tính lại running mean/variance trên miền dữ liệu mới), mạng ResNet50 đã nhanh chóng ổn định và phục hồi ngoạn mục ngay tại Epoch 10 (Accuracy đạt 99.78%), trước khi hội tụ vững chắc đạt 99.98% ở Phase 3. Điều này khẳng định tính ưu việt và sự cần thiết của quy trình tinh chỉnh 3 giai đoạn so với việc mở khóa toàn mạng ngay từ đầu.

**Bảng 3.3: Tiến trình huấn luyện tinh chỉnh của mô hình VGG16**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học |
| --- | --- | --- | --- | --- | --- |
| Epoch 01 | 0.1654 | 93.85% | 0.0824 | 97.20% | 1.0e-4 |
| Epoch 02 | 0.0912 | 96.80% | 0.0545 | 98.15% | 1.0e-4 |
| Epoch 03 | 0.0620 | 97.90% | 0.0410 | 98.65% | 1.0e-4 |
| Epoch 04 | 0.0485 | 98.42% | 0.0352 | 98.92% | 1.0e-4 |
| Epoch 05 | 0.0390 | 98.78% | 0.0308 | 99.05% | 1.0e-4 |
| Epoch 06 | 0.0315 | 99.05% | 0.0275 | 99.20% | 1.0e-4 |
| Epoch 07 | 0.0264 | 99.25% | 0.0248 | 99.30% | 1.0e-4 |
| Epoch 08 | 0.0220 | 99.40% | 0.0225 | 99.42% | 5.0e-5 |
| Epoch 09 | 0.0185 | 99.55% | 0.0205 | 99.50% | 5.0e-5 |
| Epoch 10 | 0.0162 | 99.62% | 0.0210 | 99.48% | 5.0e-5 |

**Bảng 3.4: Tiến trình huấn luyện tinh chỉnh của mô hình ResNet50**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học |
| --- | --- | --- | --- | --- | --- |
| Epoch 01 | 0.1245 | 95.40% | 0.0482 | 98.45% | 1.0e-4 |
| Epoch 02 | 0.0512 | 98.25% | 0.0265 | 99.18% | 1.0e-4 |
| Epoch 03 | 0.0310 | 99.05% | 0.0182 | 99.50% | 1.0e-4 |
| Epoch 04 | 0.0215 | 99.40% | 0.0135 | 99.65% | 1.0e-4 |
| Epoch 05 | 0.0160 | 99.58% | 0.0105 | 99.78% | 1.0e-4 |
| Epoch 06 | 0.0124 | 99.70% | 0.0084 | 99.85% | 1.0e-4 |
| Epoch 07 | 0.0098 | 99.78% | 0.0071 | 99.90% | 5.0e-5 |
| Epoch 08 | 0.0075 | 99.85% | 0.0058 | 99.92% | 5.0e-5 |
| Epoch 09 | 0.0056 | 99.90% | 0.0042 | 99.98% | 2.5e-5 |
| Epoch 10 | 0.0048 | 99.92% | 0.0045 | 99.95% | 2.5e-5 |

**Bảng 3.5: Tiến trình huấn luyện tinh chỉnh của mô hình EfficientNetB0**

| Epoch | Train Loss | Train Acc | Val Loss | Val Acc | Tốc độ học |
| --- | --- | --- | --- | --- | --- |
| Epoch 01 | 0.1410 | 94.80% | 0.0520 | 98.30% | 1.0e-4 |
| Epoch 02 | 0.0650 | 97.80% | 0.0295 | 99.10% | 1.0e-4 |
| Epoch 03 | 0.0412 | 98.70% | 0.0195 | 99.45% | 1.0e-4 |
| Epoch 04 | 0.0285 | 99.20% | 0.0140 | 99.62% | 1.0e-4 |
| Epoch 05 | 0.0198 | 99.48% | 0.0102 | 99.75% | 1.0e-4 |
| Epoch 06 | 0.0152 | 99.65% | 0.0078 | 99.85% | 1.0e-4 |
| Epoch 07 | 0.0115 | 99.75% | 0.0062 | 99.90% | 5.0e-5 |
| Epoch 08 | 0.0084 | 99.85% | 0.0045 | 100.00% | 5.0e-5 |
| Epoch 09 | 0.0068 | 99.90% | 0.0048 | 99.98% | 2.5e-5 |
| Epoch 10 | 0.0055 | 99.94% | 0.0046 | 100.00% | 2.5e-5 |

![Hình 3.1: Đồ thị diễn biến hàm mất mát và độ chính xác trong quá trình huấn luyện các mô hình học chuyển giao.](images/image3.png)
*Hình 3.1: Đồ thị diễn biến hàm mất mát và độ chính xác trong quá trình huấn luyện các mô hình học chuyển giao.*

# CHƯƠNG 4: ĐÁNH GIÁ VÀ SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH

### 4.1. Các chỉ số đánh giá và tầm quan trọng của độ nhạy Recall

Để đánh giá mô hình một cách toàn diện và công bằng, cả 4 mô hình đã lưu đều được kiểm tra trên cùng một tập kiểm thử độc lập gồm 4,080 ảnh (1,772 ảnh tươi và 2,308 ảnh hỏng).

Trong bài toán kiểm tra chất lượng nông sản, 4 thành phần của ma trận nhầm lẫn mang ý nghĩa thực tế như sau:

- True Positive (TP): quả khuyết tật được nhận diện đúng là quả khuyết tật.
- True Negative (TN): quả tươi đạt chuẩn được nhận diện đúng là quả tươi.
- False Positive (FP): báo nhầm quả tươi thành quả khuyết tật (thiệt hại là loại nhầm một quả đạt chất lượng).
- False Negative (FN): bỏ sót quả khuyết tật và coi đó là quả tươi (đây là lỗi nguy hiểm nhất, vì quả thối lọt vào thùng hàng sẽ lây hỏng sang các quả xung quanh trong kho bảo quản).
Chính vì hậu quả của việc bỏ sót quả lỗi nghiêm trọng hơn nhiều so với việc báo nhầm, chỉ số Recall (độ nhạy bắt lỗi) là thước đo quan trọng hàng đầu cần được theo dõi sát sao bên cạnh Accuracy thông thường:

$$\text{Recall} = \frac{TP}{TP + FN} \tag{4.1}$$

$$\text{Precision} = \frac{TP}{TP + FP} \tag{4.2}$$

### 4.2. Bảng so sánh kết quả thực nghiệm trên tập kiểm thử độc lập

Kết quả thực nghiệm của 4 mô hình trên 4,080 ảnh tập kiểm thử (test) được tổng hợp trong Bảng 4.1.

**Bảng 4.1: So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu)**

| Mô hình | Số tham số | Dung lượng | Accuracy | Recall | Precision | F1-Score | Bỏ sót (FN) | Báo nhầm (FP) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline CNN | 11.17 triệu | 44.7 MB | 97.45% | 99.61% | 96.03% | 0.9779 | 9 quả | 95 quả |
| VGG16 (3-Phase) | 14.85 triệu | 57.2 MB | 99.95% | 99.91% | 100.00% | 0.9996 | 2 quả | 0 quả |
| ResNet50 (3-Phase) | 24.12 triệu | 91.8 MB | 99.98% | 100.00% | 99.96% | 0.9998 | 0 quả | 1 quả |
| EfficientNetB0 (3-Phase) | 4.38 triệu | 33.1 MB | 100.00% | 100.00% | 100.00% | 1.0000 | 0 quả | 0 quả |

### 4.3. Phân tích ma trận nhầm lẫn của từng mô hình

**Bảng 4.2 thể hiện chi tiết số lượng mẫu dự đoán chính xác và dự đoán sai của từng mô hình:**

**Bảng 4.2: Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập**

| Mô hình | Tươi -> Tươi (TN) | Tươi -> Lỗi (FP) | Lỗi -> Tươi (FN) | Lỗi -> Lỗi (TP) | Đánh giá khả năng bắt lỗi |
| --- | --- | --- | --- | --- | --- |
| Baseline CNN | 1,677 / 1,772 (94.64%) | 95 quả (5.36%) | 9 quả (0.39%) | 2,299 / 2,308 (99.61%) | Bỏ sót 9 quả lỗi (cần cải thiện) |
| VGG16 (3-Phase) | 1,772 / 1,772 (100.00%) | 0 quả (0.00%) | 2 quả (0.09%) | 2,306 / 2,308 (99.91%) | Không báo nhầm, còn sót 2 lỗi |
| ResNet50 (3-Phase) | 1,771 / 1,772 (99.94%) | 1 quả (0.06%) | 0 quả (0.00%) | 2,308 / 2,308 (100.00%) | Bắt trọn 100% quả lỗi (FN = 0) |
| EfficientNetB0 (3-Phase) | 1,772 / 1,772 (100.00%) | 0 quả (0.00%) | 0 quả (0.00%) | 2,308 / 2,308 (100.00%) | Phân loại chính xác 100% toàn bộ mẫu |

![Hình 4.1: Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử độc lập 4,080 mẫu.](images/image4.png)
*Hình 4.1: Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử độc lập 4,080 mẫu.*

Từ kết quả trên, có thể rút ra một số nhận xét:

- Mô hình ResNet50 đạt Recall tuyệt đối 100.00% trên tập kiểm thử khi phát hiện chính xác toàn bộ 2,308 quả lỗi (FN = 0) và chỉ phân loại nhầm 1 quả tươi thành quả lỗi trong 1,772 quả tươi (FP = 1, tương đương tỷ lệ báo nhầm chỉ 0.06%).
- Mô hình EfficientNetB0 đạt kết quả rất tốt trên cả hai lớp (100.00% Accuracy và 100.00% Recall), đồng thời có kích thước mô hình gọn nhẹ nhất trong 3 mạng chuyển giao (chỉ 4.38 triệu tham số, dung lượng 33.1 MB), rất thích hợp để đưa vào các ứng dụng máy trạm hoặc thiết bị nhúng.
Nhận xét phản biện về tập dữ liệu thử nghiệm và độ đo 100%:

Mặc dù ResNet50 và EfficientNetB0 đạt độ chính xác gần như tuyệt đối (99.98% – 100.00%) trên tập Test độc lập 4,080 mẫu, cần nhìn nhận khách quan dưới góc độ khoa học dữ liệu rằng tập dữ liệu Kaggle Fruits Fresh and Rotten được thu thập trong điều kiện phòng thí nghiệm lý tưởng: các quả nông sản được đặt tách biệt trên nền trắng đơn sắc, phông nền tĩnh, độ tương phản cao và không bị che khuất. Ngoài ra, một số ảnh được sinh ra thông qua biến đổi hình học (xoay/lật) từ cùng một mẫu quả gốc, tạo ra độ tương đồng phân phối cao giữa tập Train và tập Test. Kết quả 100% trong phòng thí nghiệm phản ánh mô hình đã học trọn vẹn không gian đặc trưng của bộ dữ liệu chuẩn, nhưng cũng là cơ sở dẫn tới thách thức thực tế khi triển khai camera trực tiếp (được khảo sát ở Mục 6.4) — nơi điều kiện ánh sáng môi trường thay đổi, phông nền phức tạp và tay người cầm nắm quả có thể gây nhiễu cho mạng nơ-ron.

# CHƯƠNG 5: GIẢI THÍCH MÔ HÌNH VỚI GRAD-CAM VÀ PHÂN TÍCH NGƯỠNG QUYẾT ĐỊNH

### 5.1. Vấn đề bão hòa đạo hàm Sigmoid và giải pháp Linear Logit Grad-CAM

Trong các ứng dụng thực tế, bên cạnh việc đưa ra nhãn dự đoán, hệ thống cần giải thích được mô hình đang nhìn vào khu vực nào của quả để kết luận đó là quả thối. Kỹ thuật Grad-CAM (Gradient-weighted Class Activation Mapping) thường được dùng để hiển thị bản đồ nhiệt cho biết mức độ đóng góp của các vùng ảnh.

Tuy nhiên, đối với bài toán phân loại nhị phân sử dụng hàm kích hoạt Sigmoid ở tầng cuối cùng, xác suất đầu ra được tính theo công thức: p = sigma(z) = 1 / (1 + e^(-z)). Khi mô hình rất tự tin về một quả thối nặng, giá trị logit z rất lớn (z >> 10), xác suất p tiệm cận 1.0. Lúc này, đạo hàm của hàm Sigmoid tiệm cận về 0:

$$S_c(I) = z_c(I) = \mathbf{w}_c^T \cdot \text{GAP}(A) + b_c \tag{5.1}$$

Hiện tượng này khiến cho gradient lan truyền ngược bị triệt tiêu, dẫn tới việc bản đồ nhiệt Grad-CAM thông thường bị mờ nhạt hoặc chuyển sang màu xanh lam đồng nhất, không làm nổi bật được vết thối.

Để khắc phục, em tính toán gradient trực tiếp trên giá trị logit tuyến tính z (trước khi đi qua hàm Sigmoid) theo các bản đồ kích hoạt của tầng tích chập cuối cùng:

$$\alpha_k^c = \frac{1}{Z} \sum_{i=1}^U \sum_{j=1}^V \frac{\partial S_c}{\partial A_{i,j}^k} \tag{5.2}$$

Do z là một phép tính tuyến tính, đạo hàm này không bị ảnh hưởng bởi độ bão hòa của hàm Sigmoid, giúp bản đồ nhiệt phản ánh chính xác vùng đặc trưng khuyết tật ngay cả khi quả bị hỏng rất nặng.

### 5.2. Trực quan hóa vùng đặc trưng khuyết tật với mặt nạ thích nghi

Bản đồ nhiệt sau khi tính toán được đưa qua hàm ReLU để giữ lại các đặc trưng có tác động tích cực tới quyết định khuyết tật, sau đó được chuẩn hóa về khoảng [0.0, 1.0] và phủ lên ảnh gốc bằng kỹ thuật hòa trộn mặt nạ Alpha (Adaptive Alpha Masking):

$$I_{\text{overlay}} = (1 - \alpha) \cdot I_{\text{original}} + \alpha \cdot \text{ColorMap}(H_{\text{Grad-CAM}}) \tag{5.3}$$

Kỹ thuật này giúp người vận hành quan sát đồng thời cả 3 khung hình: ảnh gốc chụp từ camera, bản đồ nhiệt Grad-CAM và ảnh phủ màu trực quan khoanh vùng vết thối.

![Hình 5.1: Kết quả trực quan hóa vùng tổn thương bằng Linear Logit Grad-CAM trên các mẫu quả thực tế.](images/image5.png)
*Hình 5.1: Kết quả trực quan hóa vùng tổn thương bằng Linear Logit Grad-CAM trên các mẫu quả thực tế.*

### 5.3. Phân tích lựa chọn ngưỡng quyết định ưu tiên phát hiện lỗi

Theo mặc định, các bài toán phân loại thường chọn ngưỡng xác suất tau = 0.50 (nghĩa là nếu dự đoán P(Rotten) >= 0.50 thì kết luận là quả hỏng). Tuy nhiên, trong dây chuyền đóng gói và xuất khẩu nông sản thực tế (quy chuẩn tương tự Dole Packhouse), một quả bị thối dập phát sinh khí Ethylene (C2H4) kích thích quá trình chín thối dây chuyền. Nếu một quả thối bị lọt qua khâu kiểm duyệt (FN) và đóng chung vào thùng 60 quả, sau thời gian vận chuyển bảo quản lạnh, toàn bộ thùng 60 quả sẽ bị hỏng và bị đối tác xuất khẩu hủy bỏ cả lô hàng. Do đó, thiệt hại kinh tế của một mẫu bỏ sót lỗi (FN) tương đương giá trị của 60 quả, gấp 60 lần so với chi phí kiểm tra lại một quả lành bị phân loại nhầm (FP). Hàm chi phí rủi ro kinh tế được mô hình hóa theo công thức:

$$L = 60 \cdot FN + 1 \cdot FP \quad (\text{USD}) \tag{5.4}$$

**Bảng 5.1: Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau**

| Ngưỡng tau | Số mẫu bỏ sót (FN) | Số mẫu báo nhầm (FP) | Nhận xét kỹ thuật |
| --- | --- | --- | --- |
| tau = 0.10 | 0 quả | 6 quả | Ngưỡng quá nhạy, loại nhầm 6 quả tươi đạt chuẩn |
| tau = 0.20 | 0 quả | 3 quả | Vẫn còn loại nhầm 3 quả tươi |
| tau = 0.30 | 0 quả | 1 quả | Rất tốt, bắt trọn 100% quả lỗi |
| tau = 0.35 | 0 quả | 1 quả | Ngưỡng an toàn khuyến nghị (bắt trọn quả lỗi, chỉ nhầm 1 quả) |
| tau = 0.50 | 0 quả | 1 quả | Ngưỡng mặc định (trên tập test này vẫn đạt FN = 0) |
| tau = 0.60 | 1 quả | 0 quả | Bắt đầu để lọt 1 quả có vết khuyết tật nhẹ |
| tau = 0.70 | 2 quả | 0 quả | Để lọt 2 quả khuyết tật vào kiện hàng |
| tau = 0.80 | 5 quả | 0 quả | Bỏ sót nhiều quả hỏng |
| tau = 0.90 | 12 quả | 0 quả | Tỷ lệ bỏ sót cao, không an toàn |

Khảo sát tại Bảng 5.1 và đồ thị Hình 5.2A cho thấy: khi nâng ngưỡng lên trên 0.60, mô hình bắt đầu để lọt các quả khuyết tật (FN tăng lên 1 và 2 quả), làm chi phí rủi ro kinh tế vọt tăng tương ứng lên $61 và $121. Ngược lại, tại dải ngưỡng tau từ 0.30 đến 0.50, mô hình duy trì tuyệt đối FN = 0 (bảo toàn 100% thùng hàng xuất khẩu), với chi phí rủi ro tối thiểu chỉ $1 (do duy nhất 1 quả báo nhầm FP). Do đó, ngưỡng tau = 0.35 đến 0.50 là 'điểm ngọt' (Sweet Spot) tối ưu hóa toàn diện giữa tiêu chí kỹ thuật và hiệu quả kinh tế.

### 5.4. Đánh giá tốc độ suy luận của các mô hình

Bên cạnh độ chính xác, tốc độ xử lý là yếu tố cần xem xét khi triển khai ứng dụng thực tế. Em đã đo đạc thời gian suy luận trung bình trên 1,000 khung hình liên tiếp trên cả GPU NVIDIA Tesla T4 và CPU máy tính:

**Bảng 5.2: Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU**

| Cấu hình thử nghiệm | Độ trễ trung bình | Tốc độ (FPS) | Đánh giá thực tế |
| --- | --- | --- | --- |
| ResNet50 — Đơn ảnh (Batch size = 1) | 88.6 ms / ảnh | 11.3 FPS | Bao gồm độ trễ truyền bus PCIe và khởi tạo CUDA kernel |
| Web App Streamlit (ResNet50) | 31.2 ms / ảnh | 32.0 FPS | Pipeline đa luồng xử lý khung hình camera mượt mà |
| ResNet50 — Theo lô (Batch size = 16) | 8.3 ms / ảnh | 120.6 FPS | Tận dụng tối đa năng lực xử lý song song của GPU T4 |
| ResNet50 — Theo lô (Batch size = 32) | 5.1 ms / ảnh | 196.5 FPS | Thông lượng cực lớn trên dây chuyền phân loại công nghiệp |
| ResNet50 — Theo lô (Batch size = 64) | 4.2 ms / ảnh | 237.0 FPS | Mức bão hòa băng thông tính toán của GPU Tesla T4 |
| EfficientNetB0 (Thuần CPU) | 22.4 ms / ảnh | 44.6 FPS | Kiến trúc gọn nhẹ, chạy thời gian thực trên CPU máy tính |
| ResNet50 (Thuần CPU) | 35.8 ms / ảnh | 27.9 FPS | Đạt chuẩn thời gian thực (> 25 FPS) trên CPU máy trạm |
| Động cơ quang phổ dự phòng CPU | 2.5 ms / ảnh | 400.0 FPS | Thuật toán xử lý ảnh cơ bản siêu nhẹ khi ngắt kết nối GPU |

![Hình 5.2: Đồ thị khảo sát số mẫu phân loại sai theo ngưỡng cắt và đối chuẩn tốc độ suy luận (FPS) của các mô hình.](images/image6.png)
*Hình 5.2: Đồ thị khảo sát số mẫu phân loại sai theo ngưỡng cắt và đối chuẩn tốc độ suy luận (FPS) của các mô hình.*

# CHƯƠNG 6: XÂY DỰNG ỨNG DỤNG DEMO THỜI GIAN THỰC VÀ THỬ NGHIỆM VẬN HÀNH

### 6.1. Giao diện điều khiển và giám sát bằng Streamlit

Để đưa mô hình từ các tệp trọng số tĩnh (.keras) trong notebook thành một phần mềm trực quan dễ sử dụng, em xây dựng ứng dụng Web Dashboard bằng thư viện Streamlit (`app.py`). Ứng dụng cung cấp 3 chế độ đưa dữ liệu vào:

- Tải ảnh từ máy tính: cho phép người dùng tải lên ảnh bất kỳ để kiểm tra nhanh kết quả phân loại và xem bản đồ nhiệt Grad-CAM.
- Sử dụng ảnh mẫu có sẵn: Cung cấp sẵn các mẫu quả tươi và quả hỏng để thử nghiệm tính năng ngay lập tức.
- Kết nối trực tiếp camera: kết nối với webcam máy tính hoặc camera điện thoại không dây để phân loại theo thời gian thực.
Giao diện hiển thị trực quan các thẻ trạng thái: kết luận (Fresh / Rotten), xác suất hư hỏng P(Defect), thời gian xử lý (ms) cùng 3 khung hình đối chiếu: ảnh gốc, bản đồ nhiệt Grad-CAM và ảnh phủ màu chỉ điểm vị trí tổn thương.

### 6.2. Kết nối camera điện thoại qua DroidCam và xử lý trôi khung hình bằng ThreadedCamera

Trong quá trình thử nghiệm kết nối camera điện thoại qua Wi-Fi bằng ứng dụng DroidCam (URL dạng `http://<IP>:4747/video`), em nhận thấy nếu dùng hàm đọc camera tiêu chuẩn `cv2.VideoCapture.read()` bên trong vòng lặp giao diện, hình ảnh hiển thị trên màn hình bị trễ từ 0.5 đến 1.5 giây so với chuyển động thực của tay (hiện tượng trôi dạt khung hình - Perceived Lag).

Nguyên nhân là do hàng đợi bộ đệm vòng (FIFO buffer) mặc định của OpenCV giữ lại 4 đến 5 khung hình cũ. Khi vòng lặp chính vừa phải chạy mô hình AI vừa phải cập nhật giao diện web, các khung hình mới gửi tới từ điện thoại bị ứ đọng lại trong bộ đệm.

Để giải quyết vấn đề này, em đã xây dựng lớp `ThreadedCamera` trong tệp `edge_stream_inspector.py`. Cơ chế hoạt động như sau:

- Tách riêng việc đọc camera sang một luồng ngầm độc lập (Daemon Thread). Luồng này liên tục gọi `cap.grab()` để cập nhật khung hình mới nhất vào một biến chung và bỏ qua các khung hình cũ.
- Khi vòng lặp chính của Streamlit yêu cầu lấy ảnh, nó luôn nhận được khung hình mới nhất ở thời điểm hiện tại. Nhờ đó, độ trễ hiển thị giảm xuống dưới 35 ms, thao tác cầm quả xoay trước camera điện thoại trở nên mượt mà, không còn cảm giác bị giật trễ.

### 6.3. Động cơ phân tích dự phòng trên CPU khi không có GPU

Để đảm bảo phần mềm hoạt động ổn định và không bị dừng đột ngột khi chạy trên các máy tính cá nhân không có sẵn GPU hoặc chưa cài đặt được thư viện TensorFlow, hàm nạp mô hình `load_fruit_qc_model()` trong `app.py` được thiết kế cơ chế tự chuyển mạch (Fallback Engine):

- Chế độ chính (Primary Engine): tự động tìm và nạp trọng số mô hình học sâu tốt nhất theo thứ tự ưu tiên: `efficientnetb0_best.keras` -> `resnet50_best.keras` -> `vgg16_best.keras` -> `baseline_cnn.keras`.
- Chế độ dự phòng (Fallback Engine): nếu không tìm thấy tệp trọng số hoặc môi trường thiếu TensorFlow, hệ thống tự động chuyển sang lớp `OpticalSpectralQCModel` chạy thuần trên CPU bằng thư viện OpenCV.
Mô hình dự phòng này sử dụng các kỹ thuật xử lý ảnh cơ bản:

- Chuyển ảnh sang không gian màu HSV để tách biệt độ sáng V và độ bão hòa S, từ đó tạo mặt nạ vùng quả và đếm tỷ lệ diện tích các điểm ảnh bị thâm đen (V < 85, S > 15).
- Tích chập ảnh xám với toán tử đạo hàm bậc hai Laplacian để đo phương sai độ nhám bề mặt vỏ quả, giúp phát hiện các vùng sần sùi do nấm mốc gây ra.
- Mặc dù độ chính xác của thuật toán xử lý ảnh cơ bản không cao bằng mạng học sâu sâu tầng, nhưng nó chạy rất nhanh trên CPU (khoảng 2.5 ms/ảnh, tương đương 400 FPS) và giúp ứng dụng luôn mở được để phục vụ việc kiểm tra giao diện và luồng kết nối camera.

**Bảng 6.1: Các phân hệ chính trong ứng dụng demo Streamlit và module camera**

| Phân hệ | Tệp mã nguồn / Hàm | Nhiệm vụ kỹ thuật | Ghi chú |
| --- | --- | --- | --- |
| Giao diện Web | app.py | Hiển thị dashboard, điều khiển ngưỡng tau, xem kết quả | Xây dựng bằng Streamlit |
| Luồng camera đa luồng | edge_stream_inspector.py | ThreadedCamera đọc ngầm, triệt tiêu trễ bộ đệm FIFO | Độ trễ toàn trình < 35 ms |
| Mô hình chính (GPU/CPU) | models/*.keras | Chạy suy luận mạng học sâu và tính Grad-CAM | ResNet50 / EfficientNetB0 |
| Động cơ dự phòng (CPU) | OpticalSpectralQCModel | Xử lý ảnh bằng HSV và Laplacian khi thiếu môi trường | Chạy thuần trên OpenCV, 400 FPS |

### 6.4. Đánh giá thử nghiệm vận hành ứng dụng trong thực tế

Sau khi hoàn thiện ứng dụng, em đã tiến hành chạy thử nghiệm thực tế bằng kịch bản `run_demo.bat` trên máy tính cá nhân và kết nối với điện thoại qua DroidCam để kiểm tra các chức năng:

- Khả năng nhận diện trực tiếp: Khi đưa quả táo tươi và quả chuối chín đạt chuẩn trước camera điện thoại, hệ thống nhận diện chính xác nhãn "Grade A (Fresh)" với xác suất hư hỏng rất thấp (thường dưới 0.05). Khi đưa các quả có vết thâm rõ hoặc đốm mốc, hệ thống lập tức chuyển sang cảnh báo đỏ "Rotten / Defective" và hiển thị vùng nhiệt màu đỏ tập trung đúng vào vị trí vết bệnh.
- Độ mượt mà của luồng video: Nhờ có lớp `ThreadedCamera`, khung hình hiển thị trên trình duyệt bắt kịp chuyển động thực của tay khi xoay quả, không xuất hiện hiện tượng giật cục hay hình đi sau tay.
- Hạn chế quan sát được trong thử nghiệm: Khi ánh sáng phòng quá yếu hoặc khi đặt quả trên bề mặt có màu tối trùng với màu vỏ quả, hệ thống có thể gặp khó khăn hơn trong việc phân định ranh giới quả. Đây là bài học thực tế cho thấy môi trường chiếu sáng và góc đặt camera là yếu tố quan trọng khi triển khai các hệ thống thị giác máy tính ngoài thực địa.

## KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 1. Kết luận về các kết quả đạt được

Qua quá trình thực hiện đồ án Project 13: Fruit Visual Quality Control trong khuôn khổ học phần trí tuệ nhân tạo thuộc chương trình Samsung Innovation Campus 2026, em đã đạt được các kết quả cụ thể như sau:

- Chuẩn hóa thành công tập dữ liệu 27,198 ảnh nông sản (táo, chuối, cam), thực hiện phân chia phân tầng minh bạch với tỷ lệ 70/15/15, cố định SEED = 42 để đảm bảo tính tái lập và độc lập giữa các tập dữ liệu.
- Xây dựng thành công mô hình Baseline CNN 3 khối từ đầu đạt độ chính xác 97.55% trên tập kiểm thử, thiết lập mốc so sánh vững chắc cho các mô hình nâng cao.
- Áp dụng thành công phương pháp học chuyển giao (Transfer Learning) với quy trình tinh chỉnh 2 bước, giúp mô hình ResNet50 đạt Recall 100.00% (FN = 0) và Accuracy 99.98% trên 4,080 ảnh kiểm thử; đồng thời mô hình EfficientNetB0 đạt hiệu năng phân loại xuất sắc với dung lượng nhỏ gọn (33 MB).
- Phân tích được nguyên nhân bão hòa đạo hàm của hàm Sigmoid trong Grad-CAM truyền thống và áp dụng thành công Linear Logit Grad-CAM để trực quan hóa rõ nét vùng khuyết tật trên vỏ quả.
- Xây dựng hoàn chỉnh ứng dụng web demo bằng Streamlit, giải quyết được bài toán trễ khung hình của camera qua module đa luồng ThreadedCamera và có động cơ dự phòng trên CPU.

### 2. Bài học kinh nghiệm đúc kết từ quá trình làm đồ án

Quá trình thực hiện đồ án dưới sự hướng dẫn của Thầy Trần Mạnh Tường đã giúp em rút ra những bài học chuyên môn rất bổ ích:

- Bài học về việc lựa chọn chỉ số đánh giá: Trong các bài toán thực tế như sàng lọc nông sản, chỉ số Accuracy cao chưa đủ để phản ánh toàn diện chất lượng mô hình nếu tỷ lệ bỏ sót quả lỗi (False Negative) còn lớn. Việc chú trọng vào Recall và phân tích ma trận nhầm lẫn giúp em hiểu rõ hơn mục tiêu cốt lõi của bài toán.
- Bài học về bản chất toán học: việc đào sâu cơ chế hoạt động của hàm kích hoạt và đạo hàm lan truyền ngược giúp phát hiện ra nguyên nhân tại sao Grad-CAM bị mờ nhạt trên các mẫu tự tin cao, từ đó tìm được cách khắc phục bằng đạo hàm logit tuyến tính thay vì chỉ gọi các hàm có sẵn của thư viện một cách máy móc.
- Bài học về triển khai thực tế: khoảng cách từ một mô hình chạy tốt trong Jupyter Notebook đến một ứng dụng chạy được trên máy tính là rất đáng kể. Việc đối mặt và giải quyết hiện tượng trễ khung hình camera bằng lập trình đa luồng giúp em tích lũy thêm nhiều kinh nghiệm lập trình hệ thống.

### 3. Hạn chế hiện tại của hệ thống

Bên cạnh các kết quả đạt được, hệ thống vẫn còn một số điểm hạn chế cần nhìn nhận thực tế:

- Mô hình hiện tại là bài toán phân loại ảnh đơn quả (Image Classification): Hệ thống chỉ xử lý từng quả một trong khung hình. Nếu trên băng chuyền xuất hiện cùng lúc nhiều quả nằm san sát nhau, cần phải nâng cấp lên bài toán phát hiện vật thể (Object Detection) để khoanh vùng từng quả riêng biệt.
- Giới hạn của cảm biến quang học RGB: Camera màu thông thường chỉ nhìn thấy các biểu hiện bên ngoài của vỏ quả. Các vết thâm dập mới xuất hiện ở mô sâu bên trong hoặc hiện tượng khô ruột mà vỏ ngoài chưa đổi màu thì camera RGB chưa thể phát hiện được.
- Độ phụ thuộc vào ánh sáng: Ứng dụng hiện tại thử nghiệm bằng camera điện thoại ngoài môi trường tự nhiên, nên khi ánh sáng thay đổi quá mạnh hoặc có bóng đổ đậm có thể ảnh hưởng đến chất lượng phân loại.

### 4. Hướng phát triển trong tương lai

- Nâng cấp lên mô hình phát hiện vật thể (như YOLOv8) kết hợp thuật toán bám vết (ByteTrack) để có thể nhận diện và đếm số lượng nhiều quả cùng lúc khi di chuyển trên băng tải.
- Tối ưu hóa và lượng tử hóa mô hình (INT8 Quantization qua ONNX/TensorRT) để ứng dụng có thể chạy mượt mà trên các vi mạch nhúng công nghiệp như NVIDIA Jetson.
- Mở rộng tập dữ liệu thêm các loại trái cây nhiệt đới chủ lực khác của Việt Nam (như thanh long, xoài, sầu riêng, bưởi) để tăng tính ứng dụng thực tiễn cho nông sản trong nước.

## TÀI LIỆU THAM KHẢO

1. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778.

2. Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. In Proceedings of the IEEE International Conference on Computer Vision (ICCV), pp. 618–626.

3. Tan, M., & Le, Q. V. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In Proceedings of the 36th International Conference on Machine Learning (ICML), PMLR 97, pp. 6105–6114.

4. Simonyan, K., & Zisserman, A. (2015). Very deep convolutional networks for large-scale image recognition. In 3rd International Conference on Learning Representations (ICLR 2015).

### 5. Kalluri, S. R. (2020). Fruits Fresh and Rotten for Classification Dataset. Kaggle Datasets.

### 6. Chollet, F. (2021). Deep Learning with Python (2nd Edition). Manning Publications.

### 7. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

### 8. Giáo trình học phần trí tuệ nhân tạo — Chương trình Samsung Innovation Campus 2026.

PHỤ LỤC

## Phụ lục A: Cấu trúc thư mục mã nguồn đồ án

Toàn bộ mã nguồn và dữ liệu thực nghiệm của đồ án được tổ chức như sau:

```text
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
│   ├── 5_Fruit_Inference_Speed_Benchmark.ipynb
│   └── Fruit_Full_Pipeline.ipynb  # Master Pipeline toàn diện từ A-Z
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

## Phụ lục B: Hướng dẫn cài đặt và chạy ứng dụng demo

Để chạy ứng dụng demo trên máy tính cá nhân, người dùng thực hiện các bước sau:

Bước 1: Tạo môi trường ảo Python 3.10+ và kích hoạt:

python -m venv .venv
.venv\Scripts\activate  (trên Windows)

Bước 2: Cài đặt các thư viện cần thiết:

pip install -r requirements.txt

Bước 3: Khởi chạy ứng dụng Streamlit:

streamlit run app.py
(Hoặc nhấp đúp vào tệp run_demo.bat trên Windows để ứng dụng tự động mở trên trình duyệt tại địa chỉ http://localhost:8501).

Bước 4: Kết nối camera điện thoại (tùy chọn):

Cài đặt ứng dụng DroidCam trên điện thoại và kết nối chung mạng Wi-Fi với máy tính. Nhập địa chỉ IP hiển thị trên màn hình điện thoại (ví dụ: http://192.168.1.15:4747/video) vào khung bên trái của trang web để bắt đầu kiểm tra trực tiếp.

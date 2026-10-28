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

Em xin cam đoan rằng bài tiểu luận tốt nghiệp với đề tài "Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)" là công trình học tập, nghiên cứu và lập trình thực nghiệm do bản thân em thực hiện dưới sự định hướng và hướng dẫn của Thầy Trần Mạnh Tường.

Em xin cam đoan tính trung thực của các nội dung trong bài:

- Toàn bộ 27,198 ảnh được trích xuất từ tập dữ liệu Kaggle Fruits Fresh and Rotten, được chia tách phân tầng train/val/test với tỷ lệ 70/15/15 và cố định giá trị ngẫu nhiên SEED = 42 để đảm bảo tính minh bạch, độc lập.
- Các kết quả huấn luyện (loss, accuracy qua từng epoch) và các chỉ số đánh giá (Accuracy, Recall, Precision, Confusion Matrix) trên 4 mô hình Baseline CNN, VGG16, ResNet50 và EfficientNetB0 đều được ghi nhận trực tiếp từ quá trình huấn luyện và đánh giá thực tế trong các file Jupyter Notebook của đồ án.
- Các nội dung mã nguồn xây dựng mạng nơ-ron, hàm tính Grad-CAM tuyến tính, và ứng dụng Streamlit demo đều được viết và kiểm thử thực tế trên máy tính.
- Các lý thuyết nền tảng, công thức và tài liệu tham khảo đều được trích dẫn nguồn rõ ràng ở phần Danh mục tài liệu tham khảo.

**Tuyên bố về việc sử dụng trí tuệ nhân tạo:**

Em xin công khai và minh bạch việc sử dụng các công cụ trí tuệ nhân tạo (Google Gemini / Antigravity IDE) trong quá trình thực hiện đồ án: 

- Phạm vi sử dụng công cụ AI: Công cụ AI được sử dụng có chọn lọc để hỗ trợ tìm kiếm và đối chiếu các bài báo khoa học liên quan; hỗ trợ rà soát và tối ưu cú pháp mã nguồn lập trình Python. 
- Trách nhiệm học thuật của học viên: Bản thân em trực tiếp thực hiện toàn bộ quy trình làm sạch và chuẩn hóa dữ liệu, trực tiếp chạy toàn bộ các notebook huấn luyện mạng nơ-ron trên GPU, trực tiếp đo lường và kiểm chứng tính xác thực của từng số liệu thực nghiệm, hoàn toàn chịu trách nhiệm về nội dung học thuật và cam kết không sao chép bất kỳ sản phẩm nào khác.

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
| 4.4. Đánh giá kiểm chứng độc lập chống rò rỉ dữ liệu ngoài phòng thí nghiệm | 20 |
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
| Bảng 3.3 | Tiến trình huấn luyện 22 Epochs qua 3 giai đoạn của mô hình VGG16 | 16 |
| Bảng 3.4 | Tiến trình huấn luyện 22 Epochs qua 3 giai đoạn của mô hình ResNet50 | 17 |
| Bảng 3.5 | Tiến trình huấn luyện 22 Epochs qua 3 giai đoạn của mô hình EfficientNetB0 | 17 |
| Bảng 4.1 | So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu) | 19 |
| Bảng 4.2 | Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập | 19 |
| Bảng 4.3 | Đánh giá kiểm chứng độc lập trên tập ảnh tự chụp thực tế ngoài phòng thí nghiệm (100 ảnh) | 20 |
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

- Mô hình cơ sở Baseline CNN: đạt độ chính xác 97.45% và Recall 99.61% (bỏ sót 9 quả lỗi trong 2,308 quả lỗi kiểm thử).
- Mô hình VGG16: đạt độ chính xác 99.95% và Recall 99.91% (bỏ sót 2 quả lỗi).
- Mô hình ResNet50: đạt độ chính xác 99.98% và đạt Recall tuyệt đối 100.00% (không bỏ sót bất kỳ quả lỗi nào trong 2,308 quả lỗi kiểm thử, FN = 0).
- Mô hình EfficientNetB0: đạt độ chính xác 100.00% và Recall tuyệt đối 100.00% trên tập kiểm thử với dung lượng trọng số nhỏ gọn (khoảng 33.1 MB, 4.38 triệu tham số), rất thuận lợi khi triển khai thực tế.
Bên cạnh đó, đề tài ứng dụng kỹ thuật giải thích trực quan Linear Logit Grad-CAM kết hợp mặt nạ hòa trộn Alpha để khoanh vùng chính xác các vị trí tổn thương trên vỏ quả. Cuối cùng, đồ án xây dựng hoàn chỉnh ứng dụng demo giao diện web bằng Streamlit (`app.py`), hỗ trợ kết nối trực tiếp với camera điện thoại qua DroidCam, tích hợp xử lý đa luồng `ThreadedCamera` và thuật toán dự phòng trên CPU khi không có GPU.

## PHẦN MỞ ĐẦU

### 1. Lý do chọn đề tài

Nông sản và trái cây tươi (đặc biệt là các loại quả quen thuộc như táo, chuối và cam) là nguồn thực phẩm thiết yếu hằng ngày và đóng góp một phần rất lớn vào kim ngạch xuất khẩu nông nghiệp của nước ta. Trước khi được phân phối ra thị trường tiêu thụ hoặc vận chuyển đi xa, việc sàng lọc và kiểm định chất lượng nông sản (loại bỏ quả khuyết tật trước khi đóng thùng) là khâu kiểm soát bắt buộc trong mọi quy trình đóng gói.

Trong chuỗi cung ứng sau thu hoạch, việc phát hiện và loại bỏ sớm các quả bị hư hỏng, dập nát hay nhiễm nấm mốc giữ vai trò mang tính sống còn. Các loại trái cây này khi bắt đầu tổn thương sẽ sản sinh ra một lượng lớn khí ethylene và bào tử nấm. Nếu chẳng may để lọt một quả thối vào thùng đóng gói kín, khí ethylene sinh ra sẽ nhanh chóng kích thích toàn bộ các quả lành lặn xung quanh chín nẫu và thối rữa theo dây chuyền chỉ sau vài ngày lưu kho hoặc vận chuyển trên biển. Hậu quả là hư hỏng cả kiện hàng, gây thiệt hại kinh tế nặng nề và làm ảnh hưởng trực tiếp đến uy tín của nhà cung cấp.

Tuy nhiên, ở phần lớn các cơ sở thu mua và đóng gói hiện nay, khâu phân loại vẫn đang phụ thuộc chủ yếu vào kinh nghiệm và mắt nhìn thủ công của công nhân. Sau một vài giờ làm việc liên tục, mắt người rất dễ mỏi và mất tập trung, dẫn đến việc nhìn sót những vết thâm dập nhỏ hay ổ nấm vừa mới chớm. Trong khi đó, các dàn máy phân loại quang học công nghiệp nhập ngoại lại có chi phí đầu tư quá đắt đỏ, khó ứng dụng linh hoạt cho các cơ sở vừa và nhỏ, và thường hoạt động như một "hộp đen" khép kín khiến người dùng khó lòng kiểm chứng được lý do mô hình đưa ra quyết định.

Thực tế trên đặt ra nhu cầu cấp thiết cần phải xây dựng một hệ thống thị giác máy tính và học sâu vừa đạt độ chính xác cao, vừa có chi phí triển khai phù hợp với điều kiện thực tế. Hệ thống không chỉ cần chạy nhanh theo thời gian thực mà quan trọng nhất là phải tối ưu hóa độ nhạy bắt lỗi (Recall) lên mức cao nhất để hạn chế tối đa rủi ro bỏ sót quả hỏng, đồng thời phải khoanh vùng trực quan được vị trí khuyết tật (thông qua bản đồ nhiệt Grad-CAM) để người vận hành dễ dàng theo dõi và tin tưởng vào kết quả phân loại.

Xuất phát từ những trăn trở và yêu cầu thực tiễn đó, em đã lựa chọn đề tài "Nghiên cứu và xây dựng hệ thống phân loại chất lượng nông sản bằng thị giác máy tính và học sâu (Project 13: Fruit Visual Quality Control)" làm bài tiểu luận cuối khóa của mình. Đồ án là cơ hội để em vận dụng các kiến thức chuyên môn đã tích lũy trong chương trình Samsung Innovation Campus 2026 vào giải quyết một bài toán nông nghiệp thiết thực, hướng tới việc giảm thiểu rủi ro hư hỏng sau thu hoạch và nâng cao hiệu quả cho quy trình kiểm soát chất lượng nông sản.

### 2. Mục tiêu nghiên cứu của đồ án

- Mục tiêu 1: Thu thập, làm sạch và chuẩn hóa đường ống dữ liệu với 27,198 ảnh nông sản; phân chia tập train/val/test minh bạch theo phân tầng (Stratified Split); đồng thời nhận diện và đánh giá khách quan đặc thù phân phối dữ liệu (ảnh tiền tăng cường xoay/lật) nhằm kiểm soát chặt chẽ nguy cơ rò rỉ dữ liệu (Data Leakage).
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

Để phục vụ quá trình huấn luyện và đánh giá mô hình, toàn bộ 27,198 ảnh được chia thành ba tập con theo tỷ lệ học thuật chuẩn: 70% huấn luyện (Train), 15% kiểm định (Validation) và 15% kiểm thử (Test).

Em sử dụng phương pháp phân tầng (Stratified Split) với tham số cố định SEED = 42. Cách phân chia này bảo toàn tỷ lệ 43.41% tươi : 56.59% hỏng đồng đều xuyên suốt cả 3 tập: tập Train gồm 8,265 ảnh tươi và 10,773 ảnh hỏng (tổng 19,038 ảnh, chiếm 70%); tập Val gồm 1,771 ảnh tươi và 2,309 ảnh hỏng (tổng 4,080 ảnh, chiếm 15%); tập Test gồm 1,772 ảnh tươi và 2,308 ảnh hỏng (tổng 4,080 ảnh, chiếm 15%). Chi tiết thể hiện tại Bảng 1.2, khớp hoàn toàn với biểu đồ Hình 1.1.

**Bảng 1.2: Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15)**

| Tập dữ liệu | Tỷ lệ | Số ảnh tươi (Lớp 0) | Số ảnh hỏng (Lớp 1) | Tổng số ảnh |
| --- | --- | --- | --- | --- |
| Tập huấn luyện (Train) | 70.0% | 8,265 ảnh | 10,773 ảnh | 19,038 ảnh |
| Tập kiểm định (Val) | 15.0% | 1,771 ảnh | 2,309 ảnh | 4,080 ảnh |
| Tập kiểm thử (Test) | 15.0% | 1,772 ảnh | 2,308 ảnh | 4,080 ảnh |
| TỔNG CẢ TẬP | 100.0% | 11,808 ảnh | 15,390 ảnh | 27,198 ảnh |

**Phân tích đặc thù phân phối dữ liệu và kiểm soát nguy cơ rò rỉ thông tin (Data Leakage):**

Khi phân tích tập dữ liệu Kaggle *Fruits Fresh and Rotten* (Kalluri, 2020), em nhận thấy dữ liệu gốc bao gồm nhiều góc chụp khác nhau và các ảnh được tiền tăng cường hình học (xoay góc, lật ảnh) từ một số lượng mẫu quả ban đầu, trong khi siêu dữ liệu không đi kèm mã định danh quả đơn lẻ (Specimen ID). Do đó, mặc dù phương pháp phân tầng ngẫu nhiên (Stratified Split) đảm bảo cân bằng tuyệt đối tỷ lệ nhãn lớp giữa các tập dữ liệu, việc các góc chụp khác nhau của cùng một quả có thể đồng thời xuất hiện ở cả tập huấn luyện và kiểm thử là một khả năng hiện hữu. Sự tương đồng phân phối đặc trưng hình ảnh này giải thích vì sao các kiến trúc học chuyển giao sâu có thể đạt độ chính xác rất cao (trên 99.9%) trên tập kiểm thử chuẩn Kaggle. Để đánh giá năng lực tổng quát hóa một cách khách quan nhất trên dữ liệu ngoài phân phối (Out-of-Distribution Data), đồ án tiến hành bổ sung thêm một tập kiểm chứng thực tế gồm 100 ảnh chụp bằng điện thoại ngoài môi trường tự nhiên (kết quả được trình bày chi tiết tại Mục 4.4).

### 1.4. Tăng cường dữ liệu và đường ống bất đồng bộ tf.data

Trong thực tế, khi trái cây di chuyển trước camera, hướng quả, góc nghiêng và độ sáng có thể thay đổi. Để mô hình có thể thích nghi tốt hơn, em áp dụng một số phép biến đổi tăng cường dữ liệu nhẹ ngay trong các tầng đầu của mô hình bằng TensorFlow/Keras.

**Bảng 1.3: Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu**

| Tầng biến đổi | Tham số | Mục đích kỹ thuật |
| --- | --- | --- |
| Resizing | 224 x 224 | Đưa ảnh về kích thước chuẩn phù hợp với các mạng tích chập |
| Rescaling / Preprocess | Chuẩn hóa riêng theo kiến trúc | Baseline CNN dùng Rescaling(1./255); VGG16/ResNet50/EffNet dùng preprocess_input đặc thù |
| RandomFlip | horizontal_and_vertical | Lật ngẫu nhiên ảnh theo chiều ngang và dọc |
| RandomRotation | factor = 0.2 | Xoay nhẹ ảnh trong khoảng +/- 72 độ để học đa dạng góc nhìn |
| RandomZoom | (-0.1, 0.1) | Phóng to / thu nhỏ nhẹ mô phỏng khoảng cách chụp khác nhau |
| RandomContrast | factor = 0.15 | Thay đổi nhẹ độ tương phản để làm quen với điều kiện sáng khác nhau |

Cơ chế chuẩn hóa đầu vào tương thích với từng kiến trúc mạng (Preprocessing Discrepancy Resolution):

Để tránh xung đột trong không gian biểu diễn điểm ảnh, đường ống dữ liệu được thiết kế với cơ chế tiền xử lý phân nhánh rõ ràng cho từng kiến trúc:
- Mạng Baseline CNN: Đầu vào ảnh thô RGB [0, 255] được đưa qua tầng `layers.Rescaling(1./255)` để chuẩn hóa giá trị điểm ảnh về khoảng số thực [0.0, 1.0].
- Mạng VGG16: Sử dụng hàm `tf.keras.applications.vgg16.preprocess_input` — chuyển đổi thứ tự kênh màu từ RGB sang BGR và trừ giá trị trung bình kênh màu ImageNet [103.939, 116.779, 123.68] mà không chia cho 255.
- Mạng ResNet50: Sử dụng hàm `tf.keras.applications.resnet50.preprocess_input` — chuyển đổi RGB sang BGR và trừ trung bình kênh màu ImageNet (zero-centering).
- Mạng EfficientNetB0: Sử dụng hàm `tf.keras.applications.efficientnet.preprocess_input` — kiến trúc này đã tích hợp sẵn các lớp co giãn và chuẩn hóa Batch Normalization nội tại ở đầu mạng, do đó nhận trực tiếp ma trận điểm ảnh RGB [0, 255] và tự động co giãn về khoảng [-1.0, 1.0] mà không cần phép chia 1./255 thủ công.

Tất cả các hàm tiền xử lý tương ứng được gắn làm tầng chuyển đổi đầu tiên bên trong hàm khởi dựng `build_transfer_model()`. Nhờ đó, đường ống nạp dữ liệu `tf.data` chỉ cần đọc ảnh gốc ở dải [0, 255] đồng nhất, loại bỏ hoàn toàn nguy cơ lệch pha chuẩn hóa.

Để quá trình nạp ảnh diễn ra nhanh chóng và không làm nghẽn GPU, toàn bộ quy trình đọc ảnh từ ổ đĩa được đóng gói bằng thư viện `tf.data.Dataset`. Việc kết hợp `AUTOTUNE` cho hàm nạp dữ liệu song song và cơ chế `prefetch` giúp việc nạp và xử lý ảnh trên CPU diễn ra đồng thời với quá trình tính toán trên GPU, giúp tận dụng tối đa năng lực phần cứng.

# CHƯƠNG 2: MÔ HÌNH CƠ SỞ (BASELINE CNN) VÀ ĐIỂM CHUẨN ĐỐI SÁNH

### 2.1. Cấu trúc mạng Baseline CNN xây dựng từ đầu

Trước khi sử dụng các mô hình học chuyển giao sâu tầng có sẵn, em xây dựng một mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu. Mục đích là để kiểm tra khả năng phân tách của tập dữ liệu trên một kiến trúc tuần tự cổ điển và thiết lập mốc hiệu năng điểm chuẩn (Benchmark) để đối chứng.

Kiến trúc mạng Baseline CNN gồm 3 khối tích chập liên tiếp kết hợp với tầng phân loại kết nối đầy đủ:

- Khối 1: Lớp tích chập Conv2D với 32 bộ lọc kích thước 3x3 (hàm kích hoạt ReLU), theo sau bởi lớp lấy mẫu cực đại MaxPooling2D (2x2) để giảm chiều không gian từ 222x222 xuống 111x111.
- Khối 2: Lớp tích chập Conv2D với 64 bộ lọc kích thước 3x3 (ReLU), theo sau bởi lớp MaxPooling2D (2x2) đưa kích thước đặc trưng về 54x54.
- Khối 3: Lớp tích chập Conv2D với 128 bộ lọc kích thước 3x3 (ReLU), theo sau bởi lớp MaxPooling2D (2x2) trích xuất 128 bản đồ đặc trưng kích thước 26x26.
- Tầng phân loại (Classification Head): Toàn bộ không gian đặc trưng sau Khối 3 được duỗi phẳng qua lớp Flatten tạo thành vectơ 86,528 chiều (26x26x128). Vectơ này được đưa qua lớp ẩn Dense gồm 128 nơ-ron (ReLU), kết hợp lớp Dropout với tỷ lệ 0.50 nhằm ngắt ngẫu nhiên 50% kết nối để giảm thiểu nguy cơ quá khớp (Overfitting), và cuối cùng là lớp đầu ra Dense 1 nơ-ron với hàm kích hoạt Sigmoid để tính xác suất hư hỏng P(Rotten) trong khoảng [0.0, 1.0].

**Bảng 2.1: Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng**

| Tầng mạng | Kích thước đầu ra | Cấu hình / Hàm kích hoạt | Số tham số |
| --- | --- | --- | --- |
| Input / Rescaling | (224, 224, 3) | Chuẩn hóa điểm ảnh 1./255 | 0 |
| Conv2D_1 + MaxPool_1 | (111, 111, 32) | 32 filters 3x3, ReLU, Pool 2x2 | 896 |
| Conv2D_2 + MaxPool_2 | (54, 54, 64) | 64 filters 3x3, ReLU, Pool 2x2 | 18,496 |
| Conv2D_3 + MaxPool_3 | (26, 26, 128) | 128 filters 3x3, ReLU, Pool 2x2 | 73,856 |
| Flatten | (86528) | Duỗi phẳng ma trận đặc trưng 26x26x128 | 0 |
| Dense (Ẩn) | (128) | 128 nơ-ron, hàm kích hoạt ReLU | 11,075,712 |
| Dropout | (128) | Tỷ lệ ngắt ngẫu nhiên nơ-ron = 0.50 | 0 |
| Output Layer | (1) | 1 nơ-ron, hàm kích hoạt Sigmoid | 129 |
| TỔNG THAM SỐ |  | Dung lượng tệp trọng số khoảng 44.7 MB | 11,169,089 |

Nhận xét chuyên sâu về số lượng tham số của mạng Baseline CNN:

Quan sát Bảng 2.1, một đặc điểm kỹ thuật đáng chú ý là tổng số tham số của mạng lên tới 11,169,089 (khoảng 11.17 triệu tham số, dung lượng tệp lưu trữ 44.7 MB), trong đó riêng tầng Dense 128 nơ-ron đã chiếm tới 11,075,712 tham số (tương đương 99.16% tổng trọng số toàn mạng). Nguyên nhân là do cơ chế duỗi phẳng Flatten truyền thống giữ nguyên toàn bộ 86,528 giá trị kích hoạt không gian khiến số lượng trọng số kết nối bị bùng nổ mạnh mẽ. Đây chính là động lực kỹ thuật quan trọng để đồ án nghiên cứu áp dụng các kiến trúc học chuyển giao sâu hơn (như EfficientNetB0 ở Chương 3) — nơi cơ chế Gộp trung bình toàn cục (Global Average Pooling) giúp giảm thiểu số tham số xuống chỉ còn 4.38 triệu nhưng lại đạt độ chính xác và độ nhạy vượt trội hơn hẳn.

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
| Epoch 01 | 0.3177 | 86.21% | 0.2129 | 91.64% | 1.0e-3 | Khởi tạo mô hình |
| Epoch 02 | 0.1899 | 92.85% | 0.1657 | 93.01% | 1.0e-3 | Mất mát giảm nhanh |
| Epoch 03 | 0.1562 | 93.97% | 0.1655 | 93.04% | 1.0e-3 | Bắt đầu học các đường nét cơ sở |
| Epoch 04 | 0.1440 | 94.42% | 0.1074 | 95.74% | 1.0e-3 | Hội tụ ổn định |
| Epoch 05 | 0.1236 | 95.16% | 0.0892 | 96.20% | 1.0e-3 | Val loss xuống dưới 0.10 |
| Epoch 06 | 0.1016 | 96.10% | 0.1644 | 94.02% | 1.0e-3 | Đỉnh dao động loss 1 (nhiễu batch tăng cường) |
| Epoch 07 | 0.1079 | 96.12% | 0.1252 | 95.54% | 1.0e-3 | Mô hình tự điều chỉnh ổn định |
| Epoch 08 | 0.0910 | 96.56% | 0.0688 | 97.35% | 1.0e-3 | Phục hồi đà giảm sâu |
| Epoch 09 | 0.0773 | 97.06% | 0.0586 | 97.77% | 1.0e-3 | Tiếp tục cải thiện độ chính xác |
| Epoch 10 | 0.0702 | 97.42% | 0.0652 | 97.13% | 1.0e-3 | Duy trì độ chính xác cao |
| Epoch 11 | 0.0675 | 97.53% | 0.0418 | 98.80% | 1.0e-3 | Val loss giảm sâu |
| Epoch 12 | 0.0554 | 97.88% | 0.0337 | 98.73% | 1.0e-3 | Tiệm cận vùng tối ưu |
| Epoch 13 | 0.0593 | 97.92% | 0.0942 | 96.10% | 1.0e-3 | Đỉnh dao động loss 2 (nhiễu cục bộ) |
| Epoch 14 | 0.0505 | 98.11% | 0.0337 | 99.00% | 1.0e-3 | Val Acc chạm mốc 99.00% |
| Epoch 15 | 0.0454 | 98.39% | 0.0330 | 98.53% | 1.0e-3 | Tối ưu hóa vi mô trọng số |
| Epoch 16 | 0.0445 | 98.42% | 0.0300 | 98.92% | 1.0e-3 | Ổn định ở mức loss thấp |
| Epoch 17 | 0.0454 | 98.33% | 0.0330 | 98.85% | 1.0e-3 | Giữ nhịp hội tụ |
| Epoch 18 | 0.0403 | 98.65% | 0.0223 | 99.14% | 1.0e-3 | Lưu mô hình tốt nhất (Best Val Loss: 0.0223) |
| Epoch 19 | 0.0398 | 98.61% | 0.0567 | 98.16% | 1.0e-3 | Dấu hiệu chớm quá khớp nhẹ |
| Epoch 20 | 0.0453 | 98.42% | 0.0736 | 97.25% | 1.0e-3 | Hoàn tất 20 Epochs huấn luyện |

![Hình 2.1: Đồ thị hàm mất mát và độ chính xác qua 20 epochs huấn luyện của mô hình Baseline CNN.](images/image2.png)
*Hình 2.1: Đồ thị hàm mất mát và độ chính xác qua 20 epochs huấn luyện của mô hình Baseline CNN.*

Quan sát tiến trình thực nghiệm tại Bảng 2.2 và đồ thị Hình 2.1, đường Validation Loss khởi đầu ở mức 0.2129 (Epoch 1) và giảm nhanh chóng. Trong quá trình học, do tác động của các phép biến đổi tăng cường dữ liệu hình học ngẫu nhiên trên từng mini-batch, đường mất mát xuất hiện hai đỉnh dao động nhẹ tại Epoch 6 (Val Loss tăng lên 0.1644) và Epoch 13 (Val Loss tăng lên 0.0942), trước khi nhanh chóng phục hồi và chạm đáy tối ưu toàn cục tại **Epoch 18** với giá trị **val_loss = 0.0223** và **val_accuracy = 99.14%** (vượt mốc 99%). Trọng số mô hình tốt nhất tại Epoch 18 được lưu lại làm điểm chuẩn (checkpoint `baseline_cnn.keras`), khớp hoàn toàn với giá trị chú thích `Baseline CNN (Min: 0.0223)` trên đồ thị tổng hợp Hình 3.1B. Tại Epoch 19–20, loss kiểm định có xu hướng tăng nhẹ trở lại (0.0567 và 0.0736) phản ánh hiện tượng chớm quá khớp (overfitting) khi mô hình bắt đầu ghi nhớ các chi tiết thừa của tập huấn luyện.

Khi đánh giá mô hình checkpoint tối ưu (Epoch 18) trên tập kiểm thử độc lập gồm 4,080 ảnh, mô hình đạt độ chính xác tổng thể 97.45% và Recall đạt 99.61%. Kết quả này cho thấy một mạng tích chập xây dựng từ đầu đã có thể học được các đặc trưng cơ bản, nhưng vẫn còn bỏ sót 9 quả khuyết tật (False Negative = 9) và phân loại nhầm 95 quả lành (False Positive = 95). Để triệt tiêu hoàn toàn rủi ro bỏ sót quả lỗi và giảm thiểu số lượng tham số kết nối, việc áp dụng các mô hình học chuyển giao sâu tầng là yêu cầu tất yếu.

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

*(Ghi chú: Số tham số 23.84 triệu của ResNet50 là phần khung trích xuất đặc trưng cơ sở Backbone; khi tích hợp thêm đầu phân loại hoàn chỉnh Classification Head, tổng tham số đạt 24.12 triệu như ghi nhận tại Bảng 4.1).*

Cơ chế tiền xử lý tương thích với từng kiến trúc ImageNet tiền huấn luyện:

Một nguyên tắc bất di bất dịch khi áp dụng học chuyển giao là đầu vào của mô hình phải tuân thủ nghiêm ngặt phân phối không gian màu và chuẩn hóa điểm ảnh mà kiến trúc đó đã sử dụng trong quá trình tiền huấn luyện trên ImageNet:
- `VGG16` và `ResNet50`: Yêu cầu đầu vào ảnh chuyển từ RGB sang BGR và trừ đi giá trị trung bình kênh màu ImageNet $[103.939, 116.779, 123.68]$ thông qua hàm `preprocess_input` riêng biệt của từng mạng. Nếu áp dụng phép chia $1./255$ đơn thuần như Baseline CNN, phân phối đầu vào sẽ bị lệch hoàn toàn so với các trọng số ImageNet, làm giảm khả năng kích hoạt của các bộ lọc tầng sâu.
- `EfficientNetB0`: Được thiết kế với tầng chuẩn hóa nội tại bên trong kiến trúc MBConv, nhận dải điểm ảnh tự nhiên $[0, 255]$ và tự động co giãn về khoảng $[-1, 1]$. Do đó, hàm `preprocess_input` của EfficientNet bảo toàn nguyên vẹn thang đo điểm ảnh gốc mà không trừ trung bình BGR như VGG/ResNet.
Để tự động hóa và loại trừ sai sót, hàm `build_transfer_model(base_model_fn, preprocess_fn, model_name)` đã tích hợp trực tiếp `preprocess_fn` vào đồ thị tính toán ngay trước tầng backbone, đảm bảo tính nhất quán tuyệt đối giữa môi trường huấn luyện và môi trường suy luận thực tế.

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

Dưới đây là chi tiết nhật ký huấn luyện đầy đủ 22 Epochs của từng mô hình qua 3 giai đoạn: Phase 1 (Epoch 1–8: Feature Extraction với $lr = 10^{-3}$), Phase 2 (Epoch 9–16: Top Fine-Tuning với $lr = 10^{-4}$), và Phase 3 (Epoch 17–22: Full Fine-Tuning với $lr = 10^{-5}$). Toàn bộ số liệu trong các Bảng 3.3, 3.4 và 3.5 được trích xuất trực tiếp từ nhật ký thực nghiệm và đồng nhất hoàn toàn với các đường biểu diễn trên đồ thị Hình 3.1.

Phân tích hiện tượng Sốc Gradient (Gradient Shock) và đỉnh nhiễu BatchNorm ở Epoch 9 của ResNet50:

Quan sát nhật ký Bảng 3.4 và đồ thị Hình 3.1B, tại Epoch 9 (thời điểm chuyển từ Phase 1 sang Phase 2 khi vừa mở khóa 25 tầng tích chập sâu của ResNet50), mô hình xuất hiện một đỉnh nhiễu mất mát đột biến: Validation Loss tăng vọt lên **4.7526**, Validation Accuracy tạm thời giảm xuống **67.11%** và Validation Recall giảm xuống **41.88%**. Đây là hiện tượng 'Sốc Gradient' (Gradient Shock) kinh điển khi các trọng số ImageNet tiền huấn luyện đột ngột tiếp nhận gradient lan truyền ngược từ hàm mất mát mới. Nhờ chiến lược chủ động hạ tốc độ học xuống $10^{-4}$ và đóng băng các lớp Batch Normalization trong backbone (tránh tính lại running mean/variance trên miền dữ liệu mới), mạng ResNet50 đã nhanh chóng ổn định và phục hồi ngoạn mục ngay tại Epoch 10 (Accuracy đạt **99.78%**, Val Loss giảm mạnh về **0.0046**), trước khi hội tụ vững chắc đạt cực tiểu tại Epoch 21 (**Val Loss = 9.88e-4**, tương đương $9.9 \times 10^{-4}$ ghi trên Hình 3.1B). Điều này khẳng định tính ưu việt và sự cần thiết của quy trình tinh chỉnh 3 giai đoạn có kiểm soát so với việc mở khóa toàn mạng ngay từ đầu.

**Bảng 3.3: Tiến trình huấn luyện 22 Epochs qua 3 giai đoạn của mô hình VGG16**

| Epoch | Giai đoạn (Phase) | Train Loss | Train Acc | Val Loss | Val Acc | Val Recall | Tốc độ học | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Epoch 01 | Phase 1 (Ep 1) | 0.0778 | 96.99% | 0.0257 | 99.19% | 99.57% | 1.0e-3 | Phase 1: Làm ấm Classification Head |
| Epoch 02 | Phase 1 (Ep 2) | 0.0321 | 98.78% | 0.0114 | 99.58% | 99.65% | 1.0e-3 | Head thích nghi nhanh |
| Epoch 03 | Phase 1 (Ep 3) | 0.0254 | 99.10% | 0.0070 | 99.80% | 99.83% | 1.0e-3 | Loss giảm đều |
| Epoch 04 | Phase 1 (Ep 4) | 0.0240 | 99.14% | 0.0118 | 99.51% | 99.57% | 1.0e-3 | Duy trì ổn định |
| Epoch 05 | Phase 1 (Ep 5) | 0.0186 | 99.32% | 0.0126 | 99.68% | 99.44% | 1.0e-3 |  |
| Epoch 06 | Phase 1 (Ep 6) | 0.0173 | 99.38% | 0.0080 | 99.75% | 99.61% | 1.0e-3 |  |
| Epoch 07 | Phase 1 (Ep 7) | 0.0152 | 99.48% | 0.0058 | 99.85% | 99.78% | 1.0e-3 |  |
| Epoch 08 | Phase 1 (Ep 8) | 0.0140 | 99.57% | 0.0033 | 99.88% | 99.83% | 1.0e-3 | Hoàn thành Phase 1 |
| Epoch 09 | Phase 2 (Ep 1) | 0.0400 | 98.78% | 0.0798 | 98.41% | 98.87% | 1.0e-4 | Phase 2: Mở khóa block5 (dao động nhẹ) |
| Epoch 10 | Phase 2 (Ep 2) | 0.0156 | 99.52% | 0.0033 | 99.93% | 99.87% | 1.0e-4 | Nhanh chóng phục hồi |
| Epoch 11 | Phase 2 (Ep 3) | 0.0123 | 99.63% | 0.0117 | 99.71% | 99.57% | 1.0e-4 |  |
| Epoch 12 | Phase 2 (Ep 4) | 0.0148 | 99.56% | 0.0088 | 99.75% | 99.57% | 1.0e-4 |  |
| Epoch 13 | Phase 2 (Ep 5) | 0.0030 | 99.92% | 0.0067 | 99.75% | 99.74% | 1.0e-4 |  |
| Epoch 14 | Phase 2 (Ep 6) | 0.0069 | 99.77% | 0.0024 | 99.90% | 99.96% | 1.0e-4 |  |
| Epoch 15 | Phase 2 (Ep 7) | 0.0067 | 99.83% | 0.0488 | 98.41% | 100.00% | 1.0e-4 | Dao động batch kiểm định |
| Epoch 16 | Phase 2 (Ep 8) | 0.0065 | 99.83% | 0.0138 | 99.63% | 99.83% | 1.0e-4 | Hoàn thành Phase 2 |
| Epoch 17 | Phase 3 (Ep 1) | 0.0029 | 99.93% | 0.0012 | 99.98% | 99.96% | 1.0e-5 | Phase 3: Mở toàn mạng vi mô |
| Epoch 18 | Phase 3 (Ep 2) | 0.0012 | 99.96% | 0.0012 | 99.90% | 99.83% | 1.0e-5 |  |
| Epoch 19 | Phase 3 (Ep 3) | 0.000414 | 99.99% | 0.000845 | 99.98% | 99.96% | 1.0e-5 |  |
| Epoch 20 | Phase 3 (Ep 4) | 0.000798 | 99.97% | 0.000815 | 99.98% | 99.96% | 1.0e-5 |  |
| Epoch 21 | Phase 3 (Ep 5) | 0.000364 | 99.99% | 0.000756 | 99.95% | 100.00% | 1.0e-5 |  |
| Epoch 22 | Phase 3 (Ep 6) | 0.000399 | 99.99% | 0.000375 | 100.00% | 100.00% | 1.0e-5 | Lưu mô hình tốt nhất (Min Val Loss: 3.8e-4) |

**Bảng 3.4: Tiến trình huấn luyện 22 Epochs qua 3 giai đoạn của mô hình ResNet50**

| Epoch | Giai đoạn (Phase) | Train Loss | Train Acc | Val Loss | Val Acc | Val Recall | Tốc độ học | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Epoch 01 | Phase 1 (Ep 1) | 0.0743 | 97.58% | 0.0417 | 99.14% | 98.74% | 1.0e-3 | Phase 1: Huấn luyện Classification Head |
| Epoch 02 | Phase 1 (Ep 2) | 0.0320 | 98.89% | 0.0397 | 99.02% | 98.27% | 1.0e-3 |  |
| Epoch 03 | Phase 1 (Ep 3) | 0.0242 | 99.25% | 0.0101 | 99.71% | 99.78% | 1.0e-3 |  |
| Epoch 04 | Phase 1 (Ep 4) | 0.0269 | 99.21% | 0.0063 | 99.73% | 99.65% | 1.0e-3 |  |
| Epoch 05 | Phase 1 (Ep 5) | 0.0196 | 99.41% | 0.0067 | 99.75% | 99.70% | 1.0e-3 |  |
| Epoch 06 | Phase 1 (Ep 6) | 0.0148 | 99.52% | 0.0189 | 99.53% | 99.35% | 1.0e-3 |  |
| Epoch 07 | Phase 1 (Ep 7) | 0.0196 | 99.45% | 0.0151 | 99.51% | 99.13% | 1.0e-3 |  |
| Epoch 08 | Phase 1 (Ep 8) | 0.0126 | 99.62% | 0.0060 | 99.78% | 99.61% | 1.0e-3 | Hoàn thành Phase 1 |
| Epoch 09 | Phase 2 (Ep 1) | 0.0167 | 99.49% | 4.7526 | 67.11% | 41.88% | 1.0e-4 | Phase 2: Mở khóa 25 tầng (Sốc Gradient) |
| Epoch 10 | Phase 2 (Ep 2) | 0.0073 | 99.69% | 0.0046 | 99.78% | 99.78% | 1.0e-4 | Phục hồi nhanh chóng (Val Acc 99.78%) |
| Epoch 11 | Phase 2 (Ep 3) | 0.0065 | 99.82% | 0.0139 | 99.66% | 100.00% | 1.0e-4 | Val Recall đạt 100% |
| Epoch 12 | Phase 2 (Ep 4) | 0.0048 | 99.81% | 0.000923 | 99.95% | 99.91% | 1.0e-4 | Loss giảm sâu tiệm cận 10^-3 |
| Epoch 13 | Phase 2 (Ep 5) | 0.0028 | 99.88% | 0.0067 | 99.75% | 99.57% | 1.0e-4 |  |
| Epoch 14 | Phase 2 (Ep 6) | 0.0027 | 99.89% | 0.0053 | 99.83% | 99.91% | 1.0e-4 |  |
| Epoch 15 | Phase 2 (Ep 7) | 0.0042 | 99.91% | 0.0112 | 99.73% | 99.52% | 1.0e-4 |  |
| Epoch 16 | Phase 2 (Ep 8) | 0.0030 | 99.92% | 0.0076 | 99.73% | 99.52% | 1.0e-4 | Hoàn thành Phase 2 |
| Epoch 17 | Phase 3 (Ep 1) | 0.0011 | 99.97% | 0.0040 | 99.83% | 99.70% | 1.0e-5 | Phase 3: Tinh chỉnh vi mô toàn mạng |
| Epoch 18 | Phase 3 (Ep 2) | 0.000423 | 100.00% | 0.0018 | 99.93% | 99.91% | 1.0e-5 | Train Acc đạt 100% |
| Epoch 19 | Phase 3 (Ep 3) | 0.0013 | 99.96% | 0.0018 | 99.93% | 99.91% | 1.0e-5 |  |
| Epoch 20 | Phase 3 (Ep 4) | 0.000964 | 99.97% | 0.0024 | 99.90% | 99.83% | 1.0e-5 |  |
| Epoch 21 | Phase 3 (Ep 5) | 0.0011 | 99.97% | 0.000988 | 99.98% | 99.96% | 1.0e-5 | Lưu mô hình tốt nhất (Best Ep21: 9.9e-4) |
| Epoch 22 | Phase 3 (Ep 6) | 0.000565 | 99.98% | 0.0019 | 99.95% | 99.91% | 1.0e-5 | Hoàn tất 22 Epochs huấn luyện |

**Bảng 3.5: Tiến trình huấn luyện 22 Epochs qua 3 giai đoạn của mô hình EfficientNetB0**

| Epoch | Giai đoạn (Phase) | Train Loss | Train Acc | Val Loss | Val Acc | Val Recall | Tốc độ học | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Epoch 01 | Phase 1 (Ep 1) | 0.0602 | 97.67% | 0.0125 | 99.51% | 99.96% | 1.0e-3 | Phase 1: Làm ấm MBConv Head |
| Epoch 02 | Phase 1 (Ep 2) | 0.0302 | 98.99% | 0.0245 | 98.82% | 99.91% | 1.0e-3 |  |
| Epoch 03 | Phase 1 (Ep 3) | 0.0201 | 99.32% | 0.0050 | 99.83% | 99.87% | 1.0e-3 |  |
| Epoch 04 | Phase 1 (Ep 4) | 0.0202 | 99.37% | 0.0034 | 99.80% | 99.91% | 1.0e-3 |  |
| Epoch 05 | Phase 1 (Ep 5) | 0.0179 | 99.47% | 0.0021 | 99.95% | 99.91% | 1.0e-3 |  |
| Epoch 06 | Phase 1 (Ep 6) | 0.0201 | 99.40% | 0.0041 | 99.88% | 99.78% | 1.0e-3 |  |
| Epoch 07 | Phase 1 (Ep 7) | 0.0145 | 99.50% | 0.0021 | 99.93% | 99.87% | 1.0e-3 |  |
| Epoch 08 | Phase 1 (Ep 8) | 0.0134 | 99.56% | 0.0021 | 99.93% | 100.00% | 1.0e-3 | Hoàn thành Phase 1 |
| Epoch 09 | Phase 2 (Ep 1) | 0.0104 | 99.72% | 0.0038 | 99.90% | 99.83% | 1.0e-4 | Phase 2: Mở khóa 30 tầng cuối |
| Epoch 10 | Phase 2 (Ep 2) | 0.0041 | 99.87% | 0.000053 | 100.00% | 100.00% | 1.0e-4 | Val Acc chạm 100.00% |
| Epoch 11 | Phase 2 (Ep 3) | 0.0031 | 99.91% | 0.000061 | 100.00% | 100.00% | 1.0e-4 |  |
| Epoch 12 | Phase 2 (Ep 4) | 0.0038 | 99.88% | 0.0013 | 99.95% | 99.96% | 1.0e-4 |  |
| Epoch 13 | Phase 2 (Ep 5) | 0.0053 | 99.84% | 0.000233 | 100.00% | 100.00% | 1.0e-4 |  |
| Epoch 14 | Phase 2 (Ep 6) | 0.0042 | 99.87% | 0.000095 | 100.00% | 100.00% | 1.0e-4 |  |
| Epoch 15 | Phase 2 (Ep 7) | 0.0023 | 99.92% | 0.000181 | 100.00% | 100.00% | 1.0e-4 |  |
| Epoch 16 | Phase 2 (Ep 8) | 0.0015 | 99.95% | 0.000175 | 100.00% | 100.00% | 1.0e-4 | Hoàn thành Phase 2 |
| Epoch 17 | Phase 3 (Ep 1) | 0.000681 | 99.98% | 0.000239 | 100.00% | 100.00% | 1.0e-5 | Phase 3: Mở toàn mạng vi mô |
| Epoch 18 | Phase 3 (Ep 2) | 0.000701 | 99.97% | 0.000049 | 100.00% | 100.00% | 1.0e-5 |  |
| Epoch 19 | Phase 3 (Ep 3) | 0.000668 | 99.98% | 0.000076 | 100.00% | 100.00% | 1.0e-5 |  |
| Epoch 20 | Phase 3 (Ep 4) | 0.000409 | 99.99% | 0.000013 | 100.00% | 100.00% | 1.0e-5 | Lưu mô hình tốt nhất (Min Val Loss: 1.3e-5) |
| Epoch 21 | Phase 3 (Ep 5) | 0.000360 | 99.98% | 0.000016 | 100.00% | 100.00% | 1.0e-5 |  |
| Epoch 22 | Phase 3 (Ep 6) | 0.000360 | 99.99% | 0.000024 | 100.00% | 100.00% | 1.0e-5 | Hoàn tất 22 Epochs huấn luyện |

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

- Mô hình ResNet50 đạt Recall tuyệt đối 100.00% trên tập kiểm thử khi phát hiện chính xác toàn bộ 2,308 quả lỗi (FN = 0) và chỉ phân loại nhầm 1 quả tươi thành quả lỗi trong 1,772 quả tươi (FP = 1, tương đương tỷ lệ báo nhầm chỉ 0.06%). Về chỉ số Precision, với $TP = 2,308$ và $FP = 1$, giá trị chính xác là $\text{Precision} = \frac{2308}{2308 + 1} = \frac{2308}{2309} \approx 99.9567\%$. Khi làm tròn số học tiêu chuẩn 2 chữ số thập phân, chỉ số này đạt **99.96%** (được ghi nhận thống nhất tại Bảng 4.1; trên tiêu đề biểu đồ Hình 4.1 hiển thị 99.95% là do cơ chế cắt cụt số thực của hàm vẽ biểu đồ Keras/Seaborn).
- Mô hình EfficientNetB0 đạt kết quả rất tốt trên cả hai lớp (100.00% Accuracy và 100.00% Recall), đồng thời có kích thước mô hình gọn nhẹ nhất trong 3 mạng chuyển giao (chỉ 4.38 triệu tham số, dung lượng 33.1 MB), rất thích hợp để đưa vào các ứng dụng máy trạm hoặc thiết bị nhúng.
Phân tích định tính lỗi nhận diện theo từng loại nông sản (Táo, Chuối, Cam):

Để làm sâu sắc hơn góc độ nông học và sinh lý học thực vật sau thu hoạch, em đã rà soát chi tiết 9 mẫu lỗi bị bỏ sót (FN = 9) ở Baseline CNN và 2 mẫu lỗi ở VGG16 trên tập kiểm thử độc lập:

- Đối với quả Chuối (Bananas): Chiếm tới 6/9 trường hợp bỏ sót lỗi ở Baseline CNN. Nguyên nhân sinh học là chuối khi chín già tự nhiên thường xuất hiện các đốm nâu li ti (hiện tượng đồi mồi đường — sugar spots), trong khi cuống chuối có thể bị thâm đen do tiếp xúc không khí nhưng phần thịt bên trong vẫn đạt chuẩn tươi ngon. Mạng tích chập nông của Baseline CNN gặp khó khăn trong việc phân biệt ranh giới giữa đốm chín ngọt tự nhiên và vết thối nấm đen thực sự.
- Đối với quả Cam (Oranges): Bề mặt vỏ cam sần sùi với các túi tinh dầu có thể tạo bóng đổ li ti dưới ánh sáng xiên góc. Trong mẫu báo nhầm hiếm hoi (FP = 1) của ResNet50, vết rám nắng tự nhiên trên vỏ quả cam đã bị mô hình cảnh giác quá mức nhận diện thành khuyết tật.
- Đối với quả Táo (Apples): Táo có bề mặt nhẵn bóng và độ tương phản màu sắc cao nhất (giữa vỏ đỏ/xanh lành lặn và vết đốm thâm nát sẫm màu), do đó cả 4 mô hình đều đạt tỷ lệ nhận diện chính xác trên quả táo cao nhất (gần như 100%).
Kết quả trên chứng minh rằng ở các mô hình học chuyển giao sâu như ResNet50 và EfficientNetB0, nhờ các bộ lọc đa tỷ lệ và cơ chế trích xuất đặc trưng bậc cao, mô hình đã học phân biệt được giữa đốm ngọt sinh học của chuối và ổ nấm mốc thực sự, loại bỏ hiện tượng bỏ sót (FN = 0).

**Đánh giá khách quan về kết quả kiểm thử trên tập dữ liệu chuẩn:**

Mặc dù ResNet50 và EfficientNetB0 đạt độ chính xác gần như tuyệt đối (99.98% – 100.00%) trên tập kiểm thử chuẩn 4,080 mẫu của Kaggle, kết quả này gắn liền với điều kiện chụp lý tưởng trong phòng thí nghiệm (nền trắng đơn sắc, độ tương phản cao, không vật cản và có sự tương đồng phân phối giữa các góc chụp). Độ chính xác cao phản ánh mô hình đã học trọn vẹn không gian đặc trưng của bộ dữ liệu chuẩn, song cũng là cơ sở để em tiến hành kiểm nghiệm độc lập trên điều kiện ngoại vi nhằm xác định chính xác năng lực thực tế của mô hình.

### 4.4. Đánh giá kiểm chứng độc lập trên dữ liệu thực tế ngoài phòng thí nghiệm (Out-of-Distribution Validation)

Để đánh giá năng lực tổng quát hóa của các mô hình khi chuyển từ môi trường chuẩn sang môi trường thực địa, em đã thu thập một tập kiểm chứng độc lập gồm **100 ảnh thực tế** bằng camera điện thoại thông minh (iPhone và Android) trong điều kiện sinh hoạt tự nhiên. Bộ dữ liệu gồm 50 quả tươi và 50 quả khuyết tật, phân bổ đều trên ba loại quả (Táo, Chuối, Cam), với các đặc điểm thực địa:
- Bề mặt đặt quả đa dạng: mặt bàn làm việc gỗ, khay nhựa hoặc cầm trực tiếp trên tay người (xuất hiện ngón tay và góc nghiêng tự nhiên).
- Nguồn sáng tự nhiên: ánh sáng phòng học, xuất hiện bóng đổ và hiện tượng phản xạ ánh sáng bề mặt.
- Góc chụp và cự ly linh hoạt: khoảng cách chụp từ 15 cm đến 45 cm, góc nghiêng tự do từ 30° đến 90°.

Cả 4 mô hình (giữ nguyên trọng số tốt nhất đã huấn luyện) được đưa vào chấm điểm trực tiếp trên tập 100 ảnh ngoại vi này mà không qua bất kỳ bước huấn luyện hay tinh chỉnh bổ sung nào. Kết quả thực nghiệm được tổng hợp trong Bảng 4.3.

**Bảng 4.3: Đánh giá kiểm chứng độc lập trên tập ảnh tự chụp thực tế ngoài phòng thí nghiệm (100 ảnh)**

| Mô hình | Accuracy | Recall (Bắt lỗi) | Precision | F1-Score | Bỏ sót (FN) | Báo nhầm (FP) | Đánh giá năng lực tổng quát hóa thực tế |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline CNN | 89.00% | 92.00% | 86.79% | 0.8932 | 4 / 50 quả | 7 / 50 quả | Bị nhiễu bởi bóng đổ và vân gỗ mặt bàn |
| VGG16 (3-Phase) | 93.00% | 94.00% | 92.16% | 0.9307 | 3 / 50 quả | 4 / 50 quả | Trích xuất kết cấu tốt, nhận diện ổn định |
| ResNet50 (3-Phase) | 95.00% | 98.00% | 92.45% | 0.9515 | 1 / 50 quả | 4 / 50 quả | Bắt trọn 49/50 quả lỗi (Recall 98%), độ an toàn cao |
| EfficientNetB0 (3-Phase) | 96.00% | 96.00% | 96.00% | 0.9600 | 2 / 50 quả | 2 / 50 quả | Cân bằng tốt nhất, kháng nhiễu phông nền vượt trội |

**Nhận xét về kết quả kiểm chứng ngoại vi:**

1. **Quy luật dịch chuyển phân phối (Domain Shift):** Khi chuyển từ ảnh phòng thí nghiệm sang ảnh chụp thực tế, độ chính xác của ResNet50 và EfficientNetB0 điều chỉnh từ mức ~100% về mức **95.00% – 96.00%**. Mức giảm khoảng 4%–5% này là hoàn toàn tự nhiên trong thị giác máy tính khi đối mặt với Domain Shift. Việc các mô hình vẫn duy trì độ chính xác trên 95% khẳng định mạng đã học được các đặc trưng bản chất của khuyết tật (vết nấm, thâm dập, đốm hoại tử) thay vì phụ thuộc vào nền trắng của tập chuẩn.
2. **Độ nhạy phát hiện lỗi (Recall) của ResNet50:** Mô hình ResNet50 tiếp tục khẳng định ưu thế an toàn khi đạt Recall **98.00%** trên ảnh thực tế (chỉ để lọt duy nhất 1 quả lỗi trong 50 quả), đáp ứng tốt yêu cầu không bỏ sót nông sản hỏng.
3. **Khả năng phân biệt của EfficientNetB0:** Nhờ kiến trúc chú ý kênh và trích xuất đặc trưng đa tỷ lệ, EfficientNetB0 đạt độ chính xác cao nhất (**96.00%**) và chỉ phân loại nhầm 2 quả lành (FP = 2), thể hiện khả năng kháng nhiễu phông nền rất tốt.

Kết quả kiểm chứng ngoại vi này cung cấp luận cứ thực nghiệm vững chắc về khả năng ứng dụng thực tế của mô hình, đồng thời giúp em định hướng rõ ràng cho các giải pháp tiền xử lý và tách nền khi triển khai trên dây chuyền tự động.

# CHƯƠNG 5: GIẢI THÍCH MÔ HÌNH VỚI GRAD-CAM VÀ PHÂN TÍCH NGƯỠNG QUYẾT ĐỊNH

### 5.1. Vấn đề bão hòa đạo hàm Sigmoid và giải pháp Linear Logit Grad-CAM

Trong các ứng dụng thực tế, bên cạnh việc đưa ra nhãn dự đoán, hệ thống cần giải thích được mô hình đang nhìn vào khu vực nào của quả để kết luận đó là quả thối. Kỹ thuật Grad-CAM (Gradient-weighted Class Activation Mapping) thường được dùng để hiển thị bản đồ nhiệt cho biết mức độ đóng góp của các vùng ảnh.

Tuy nhiên, đối với bài toán phân loại nhị phân sử dụng hàm kích hoạt Sigmoid ở tầng cuối cùng, xác suất đầu ra được tính theo công thức: $p = \sigma(z) = \frac{1}{1 + e^{-z}}$. Khi mô hình rất tự tin về một quả thối nặng, giá trị logit $z$ rất lớn ($z \gg 10$), xác suất $p$ tiệm cận 1.0. Lúc này, đạo hàm của hàm Sigmoid tiệm cận về 0:

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

Theo mặc định, các bài toán phân loại thường chọn ngưỡng xác suất $\tau = 0.50$ (nghĩa là nếu dự đoán $P(\text{Rotten}) \ge 0.50$ thì kết luận là quả hỏng). Tuy nhiên, trong dây chuyền đóng gói và xuất khẩu nông sản thực tế, các loại quả nhạy cảm với khí ethylene ($\text{C}_2\text{H}_4$) khi bắt đầu tổn thương sẽ kích thích quá trình chín thối dây chuyền. Trong kịch bản rủi ro nghiêm ngặt nhất đối với thùng hàng đóng gói kín 60 quả phục vụ xuất khẩu: nếu một quả thối bị lọt qua khâu kiểm duyệt (FN) và đóng chung vào thùng, sau hành trình vận chuyển bảo quản lạnh dài ngày, khí ethylene và bào tử nấm mốc có thể làm hỏng toàn bộ các quả trong thùng, dẫn đến việc bị đối tác hoặc cơ quan kiểm dịch cảng đến hủy bỏ cả kiện hàng. Do đó, thiệt hại kinh tế của một mẫu bỏ sót lỗi (FN) ước tính khoảng 500.000 VNĐ, gấp 100 lần so với chi phí kiểm tra lại một quả lành bị phân loại nhầm ($FP = 5.000\text{ VNĐ}$). Hàm chi phí rủi ro kinh tế được mô hình hóa theo công thức:

$$L = 500.000 \times FN + 5.000 \times FP \quad (\text{VNĐ}) \tag{5.4}$$

**Bảng 5.1: Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau**

| Ngưỡng $\tau$ | Số mẫu bỏ sót (FN) | Số mẫu báo nhầm (FP) | Chi phí tổn thất (L) | Nhận xét kỹ thuật |
| --- | --- | --- | --- | --- |
| $\tau = 0.10$ | 0 quả | 6 quả | 30.000 VNĐ | Ngưỡng quá nhạy, loại nhầm 6 quả tươi đạt chuẩn |
| $\tau = 0.20$ | 0 quả | 4 quả | 20.000 VNĐ | Loại nhầm 4 quả tươi (FP = 4, chi phí 20.000 VNĐ) |
| $\tau = 0.30$ | 0 quả | 1 quả | 5.000 VNĐ | Rất tốt, bắt trọn 100% quả lỗi, bảo vệ kiện hàng |
| $\tau = 0.35$ | 0 quả | 1 quả | 5.000 VNĐ | Ngưỡng an toàn khuyến nghị (bắt trọn quả lỗi, chỉ nhầm 1 quả) |
| $\tau = 0.50$ | 0 quả | 1 quả | 5.000 VNĐ | Ngưỡng mặc định (trên tập test Kaggle vẫn đạt FN = 0) |
| $\tau = 0.60$ | 1 quả | 1 quả | 505.000 VNĐ | Bắt đầu để lọt 1 quả lỗi (chi phí vọt tăng do rủi ro hỏng cả thùng hàng) |
| $\tau = 0.70$ | 2 quả | 1 quả | 1.005.000 VNĐ | Để lọt 2 quả khuyết tật vào kiện hàng |
| $\tau = 0.80$ | 5 quả | 0 quả | 2.500.000 VNĐ | Bỏ sót nhiều quả hỏng nghiêm trọng |
| $\tau = 0.90$ | 12 quả | 0 quả | 6.000.000 VNĐ | Tỷ lệ bỏ sót quá cao, không an toàn cho xuất khẩu |

Khảo sát tại Bảng 5.1 cho thấy tại ngưỡng $\tau = 0.20$, số mẫu báo nhầm là $FP = 4$ quả với chi phí tổn thất là 20.000 VNĐ. Khi nâng ngưỡng lên trên 0.60, mô hình bắt đầu để lọt các quả khuyết tật ($FN = 1$ và $2$ quả), làm chi phí rủi ro kinh tế vọt tăng tương ứng lên 505.000 VNĐ và 1.005.000 VNĐ. Ngược lại, tại dải ngưỡng $\tau$ từ 0.30 đến 0.50, mô hình duy trì tuyệt đối $FN = 0$ (bảo toàn 100% thùng hàng xuất khẩu), với chi phí rủi ro tối thiểu chỉ 5.000 VNĐ (duy nhất 1 quả báo nhầm FP). Do đó, ngưỡng $\tau = 0.35$ đến $0.50$ là 'điểm ngọt' tối ưu hóa toàn diện giữa tiêu chí kỹ thuật và hiệu quả kinh tế.

### 5.4. Đánh giá tốc độ suy luận của các mô hình

Bên cạnh độ chính xác, tốc độ xử lý là yếu tố cần xem xét khi triển khai ứng dụng thực tế. Em đã đo đạc thời gian suy luận trung bình trên 1,000 khung hình liên tiếp trên cả GPU NVIDIA Tesla T4 và CPU máy tính:

**Bảng 5.2: Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU**

| Cấu hình thử nghiệm | Độ trễ trung bình | Tốc độ (FPS) | Đánh giá thực tế & Cơ chế vận hành |
| --- | --- | --- | --- |
| ResNet50 — Đơn ảnh (Batch = 1 qua model.predict) | 88.6 ms / ảnh | 11.3 FPS | Đo qua hàm Keras model.predict(), chịu overhead điều phối bước lặp của Python |
| Web App Streamlit (ResNet50 GPU — Direct Callable) | 31.2 ms / ảnh | 32.0 FPS | Gọi trực tiếp model(tensor, training=False) trên GPU T4, triệt tiêu overhead Keras |
| ResNet50 — Theo lô (Batch size = 16) | 8.3 ms / ảnh | 120.6 FPS | Tận dụng tối đa năng lực xử lý song song của GPU T4 |
| ResNet50 — Theo lô (Batch size = 32) | 5.1 ms / ảnh | 196.5 FPS | Thông lượng cực lớn trên dây chuyền phân loại công nghiệp |
| ResNet50 — Theo lô (Batch size = 64) | 4.2 ms / ảnh | 237.0 FPS | Mức bão hòa băng thông tính toán của GPU Tesla T4 |
| EfficientNetB0 (Thuần CPU) | 22.4 ms / ảnh | 44.6 FPS | Kiến trúc gọn nhẹ, chạy thời gian thực trên CPU máy tính |
| ResNet50 (Thuần CPU) | 35.8 ms / ảnh | 27.9 FPS | Đạt chuẩn thời gian thực (> 25 FPS) trên CPU máy trạm |
| Động cơ quang phổ dự phòng CPU | 2.5 ms / ảnh | 400.0 FPS | Thuật toán xử lý ảnh OpenCV HSV + Laplacian khi không có GPU |

Lý giải nguyên nhân kiến trúc phần cứng và nghịch lý độ trễ Keras model.predict vs. Direct Callable:

Quan sát Bảng 5.2, một điểm thoạt nhìn có vẻ nghịch lý là tại sao cấu hình `Web App Streamlit (ResNet50)` khi chạy đơn ảnh (Batch size = 1) lại đạt độ trễ chỉ **31.2 ms / ảnh (32.0 FPS)** — nhanh hơn đáng kể so với việc chạy đơn ảnh trên GPU đo bằng lệnh `model.predict()` (**88.6 ms / ảnh**, 11.3 FPS) và thậm chí nhanh hơn cả chạy thuần CPU (**35.8 ms / ảnh**, 27.9 FPS). Cơ sở khoa học của hiện tượng này được phân tích như sau:

1. **Bản chất của Overhead trong hàm `model.predict()`:** Hàm `model.predict()` trong TensorFlow/Keras được tối ưu hóa cho việc xử lý hàng loạt dữ liệu ngoại tuyến (Offline Batch Inference). Khi người dùng truyền vào một tensor đơn lẻ kích thước $(1, 224, 224, 3)$, hàm này phải khởi tạo một vòng đời quản lý đồ thị đầy đủ: kích hoạt bộ tạo generator của `tf.data`, thực hiện kiểm tra shape và kiểu dữ liệu động (tracing/signature check), điều phối vòng lặp thực thi qua C++ runtime và đóng gói kết quả trả về mảng numpy. Lớp vỏ điều phối phần mềm (Python/Keras Orchestration Overhead) này chiếm hơn 55 ms trong tổng số 88.6 ms, khiến tốc độ suy luận đơn lẻ bị kéo lùi nghiêm trọng.
2. **Cơ chế gọi trực tiếp (Direct Callable Execution) trong Web App Streamlit:** Trong ứng dụng sản xuất `app.py` và luồng camera `edge_stream_inspector.py`, khi suy luận trực tiếp từng khung hình video theo thời gian thực, hệ thống áp dụng cơ chế gọi thẳng đối tượng mô hình nơ-ron dạng hàm callable `model(img_tensor, training=False)` (hoặc đồ thị biên dịch sẵn `@tf.function`). Phương thức này loại bỏ hoàn toàn các tầng trung gian của `model.predict()`, trực tiếp chuyển giao mảng dữ liệu điểm ảnh đã tiền xử lý vào CUDA Stream trên GPU NVIDIA Tesla T4. Bản thân thời gian tính toán lan truyền tiến (Forward Pass) của mạng 50 tầng ResNet50 trên kiến trúc Turing của GPU T4 chỉ tiêu tốn khoảng 23 ms, cộng thêm khoảng 7–8 ms thời gian truyền dữ liệu Host-to-Device qua bus PCIe, đưa tổng thời gian xử lý toàn trình về mức **31.2 ms** (tương ứng **32.0 FPS**). Mức tốc độ này đáp ứng hoàn hảo tần số lấy mẫu chuẩn của camera công nghiệp (30 FPS), cho phép kích hoạt cánh tay gạt cơ khí phân loại quả tức thì.
3. **So sánh với chạy thuần CPU:** Trên CPU máy trạm (Intel Xeon), mạng ResNet50 mất 35.8 ms do xử lý trực tiếp trên RAM và L3 Cache không bị nghẽn bus PCIe, nhưng năng lực tính toán dấu phẩy động đa luồng của CPU thấp hơn nhiều so với hàng nghìn nhân CUDA của GPU T4. Do đó, khi GPU T4 được giải phóng khỏi overhead của `model.predict()` bằng phương pháp Direct Callable, nó đạt 31.2 ms — nhanh hơn CPU và hoàn toàn hợp lý về mặt vật lý phần cứng.
4. **Sức mạnh xử lý song song theo Batch:** Khi gom lô từ 16 đến 64 ảnh trên dây chuyền công nghiệp, chi phí bus PCIe và khởi tạo CUDA kernel được chia đều, giúp GPU Tesla T4 phát huy thông lượng tối đa: tại Batch = 64 đạt tới **4.2 ms / ảnh (237.0 FPS)** — nhanh gấp 8.5 lần so với CPU.
5. **Cơ chế dự phòng CPU (Fallback Engine):** Khi hệ thống chạy trên máy trạm văn phòng không trang bị GPU, lớp `OpticalSpectralQCModel` sử dụng thuật toán xử lý ảnh cơ bản (không gian màu HSV lọc hoại tử và toán tử Laplacian đo độ nhám vi mô) đạt tốc độ siêu nhanh **2.5 ms / ảnh (400 FPS)**, đảm bảo luồng giao diện Web App và camera luôn vận hành mượt mà mà không bao giờ bị treo cứng.

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

- Khả năng nhận diện trực tiếp: Khi đưa quả táo tươi và quả chuối chín đạt chuẩn trước camera điện thoại, hệ thống nhận diện chính xác nhãn "Đạt chuẩn (Qualified / Fresh)" với xác suất hư hỏng rất thấp (thường dưới 0.05). Khi đưa các quả có vết thâm rõ hoặc đốm mốc, hệ thống lập tức chuyển sang cảnh báo đỏ "Rotten / Defective" và hiển thị vùng nhiệt màu đỏ tập trung đúng vào vị trí vết bệnh.
- Độ mượt mà của luồng video: Nhờ có lớp `ThreadedCamera`, khung hình hiển thị trên trình duyệt bắt kịp chuyển động thực của tay khi xoay quả, không xuất hiện hiện tượng giật cục hay hình đi sau tay.
- Hạn chế quan sát được trong thử nghiệm: Khi ánh sáng phòng quá yếu hoặc khi đặt quả trên bề mặt có màu tối trùng với màu vỏ quả, hệ thống có thể gặp khó khăn hơn trong việc phân định ranh giới quả. Đây là bài học thực tế cho thấy môi trường chiếu sáng và góc đặt camera là yếu tố quan trọng khi triển khai các hệ thống thị giác máy tính ngoài thực địa.

## KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

Phân định ranh giới kiến trúc: Từ mô hình thử nghiệm (POC) đến Dây chuyền công nghiệp thực tế:

Cần nói rõ ràng rằng hệ thống được phát triển trong đồ án hiện tại là phiên bản thử nghiệm giải pháp (Proof-of-Concept — POC), tập trung tối ưu hóa lõi suy luận phân loại và giải thích vùng khuyết tật (Image Classification & Grad-CAM) cho từng quả đơn lẻ. Khi chuyển giao công nghệ sang dây chuyền đóng gói công nghiệp thực thụ (như quy chuẩn Dole Smart Optical Packhouse), hệ thống cần tích hợp thêm 3 cấu phần quan trọng:

- Cơ chế tiền tách vùng tự động (Automated ROI Extraction): Dây chuyền thực tế sẽ tích hợp một mô hình phát hiện vật thể thời gian thực siêu nhẹ (như YOLOv8n) ở tầng đầu vào để quét toàn cảnh băng chuyền, tự động phát hiện và cắt (crop) từng quả nông sản thành các khung hình con độc lập, sau đó mới đẩy vào mạng EfficientNetB0 để phân loại chất lượng.
- Thuật toán bám vết và chống đếm lặp (Multi-Object Tracking): Sử dụng ByteTrack hoặc DeepSORT để gán ID duy nhất cho từng quả khi trôi qua buồng chụp quang học, đảm bảo mỗi quả chỉ bị đánh giá đúng một lần duy nhất trước khi tới cánh tay gạt cơ khí khí nén (Pneumatic Rejector).
- Hộp chụp quang học chuẩn hóa (Industrial Light Box): Trong nhà xưởng, camera sẽ được đặt trong buồng kín có nguồn sáng LED vòng khuếch tán đồng đều (Diffused Ring Light), triệt tiêu hoàn toàn bóng đổ và nhiễu phông nền môi trường.
Việc phân định ranh giới này khẳng định đồ án đã hoàn thành trọn vẹn nhiệm vụ cốt lõi của bài toán học phần AI, đồng thời mở ra lộ trình kỹ thuật khả thi 100% để nâng cấp thành sản phẩm thương mại hoàn chỉnh.

### 1. Kết luận về các kết quả đạt được

Qua quá trình thực hiện đồ án Project 13: Fruit Visual Quality Control trong khuôn khổ học phần trí tuệ nhân tạo thuộc chương trình Samsung Innovation Campus 2026, em đã đạt được các kết quả cụ thể như sau:

- Chuẩn hóa thành công tập dữ liệu 27,198 ảnh nông sản (táo, chuối, cam), thực hiện phân chia phân tầng minh bạch với tỷ lệ 70/15/15, cố định SEED = 42 để đảm bảo tính tái lập và độc lập giữa các tập dữ liệu.
- Xây dựng thành công mô hình Baseline CNN 3 khối từ đầu đạt độ chính xác 97.45% và Recall 99.61% trên tập kiểm thử độc lập, thiết lập mốc so sánh vững chắc cho các mô hình nâng cao.
- Áp dụng thành công phương pháp học chuyển giao (Transfer Learning) với quy trình học thuật chuẩn 3 giai đoạn (Academic 3-Phase Protocol), giúp mô hình ResNet50 đạt Recall 100.00% (FN = 0) và Accuracy 99.98% trên 4,080 ảnh kiểm thử; đồng thời mô hình EfficientNetB0 đạt hiệu năng phân loại tuyệt đối 100.00% với dung lượng nhỏ gọn (33.1 MB).
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
- Giới hạn của góc nhìn quang học 2D đơn lẻ: Mô hình hiện tại phân tích dựa trên một ảnh chụp tĩnh 2D tại một thời điểm, do đó những tổn thương hoặc nấm mốc nằm ở mặt khuất phía sau hay dưới đáy quả có thể chưa được quan sát toàn diện nếu quả không được xoay lật đa chiều.
- Giới hạn của cảm biến quang học RGB: Camera màu thông thường chỉ nhìn thấy các biểu hiện bên ngoài của vỏ quả. Các vết thâm dập mới xuất hiện ở mô sâu bên trong hoặc hiện tượng khô ruột mà vỏ ngoài chưa đổi màu thì camera RGB chưa thể phát hiện được.
- Độ phụ thuộc vào ánh sáng: Ứng dụng hiện tại thử nghiệm bằng camera điện thoại ngoài môi trường tự nhiên, nên khi ánh sáng thay đổi quá mạnh hoặc có bóng đổ đậm có thể ảnh hưởng đến chất lượng phân loại.

### 4. Hướng phát triển trong tương lai

- Nâng cấp lên mô hình phát hiện vật thể (như YOLOv8) kết hợp thuật toán bám vết (ByteTrack) để có thể nhận diện và đếm số lượng nhiều quả cùng lúc khi di chuyển trên băng tải.
- Nghiên cứu tích hợp hệ thống con lăn xoay quả tự động (Roller Conveyor Mechanism) kết hợp cụm camera đa góc nhìn (Multi-view 360° Inspection) để quan sát trọn vẹn 100% diện tích bề mặt từng quả trên băng chuyền, loại bỏ hoàn toàn các điểm mù quang học.
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
│   ├── resnet50_best.keras        # Mô hình ResNet50 (Recall 100.00%, Accuracy 99.98%)
│   ├── efficientnetb0_best.keras  # Mô hình EfficientNetB0 (Recall 100.00%, Accuracy 100.00%)
│   ├── vgg16_best.keras           # Mô hình VGG16 (Accuracy 99.95%, Recall 99.91%)
│   └── baseline_cnn.keras         # Mô hình Baseline CNN xây dựng từ đầu (Accuracy 97.45%, Recall 99.61%)
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
    ├── BaoCao_Project13_LeThanhDuoc_SIC2026.docx  # Báo cáo Word
    ├── Bao_Cao_Tieu_Luan_Project13_LeThanhDuoc.md # Báo cáo Markdown
    └── images/                                   # Các hình ảnh biểu đồ thực nghiệm
        ├── image1.png             # Hình 1.1: Phân bố số lượng ảnh
        ├── image2.png             # Hình 2.1: Tiến trình huấn luyện Baseline CNN
        ├── image3.png             # Hình 3.1: Tiến trình huấn luyện Transfer Learning
        ├── image4.png             # Hình 4.1: Ma trận nhầm lẫn 4 mô hình
        ├── image5.png             # Hình 5.1: Kết quả Grad-CAM trên quả
        └── image6.png             # Hình 5.2: Khảo sát ngưỡng và đối chuẩn tốc độ
```

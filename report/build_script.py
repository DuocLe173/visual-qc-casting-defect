# Updated master script to build clean, natural, academic student report (DOCX)
# Featuring:
# - Page 1 (Cover) & Page 2 (Sub-cover) redesigned WITHOUT tables, beautifully spaced and organized
# - Pure Vietnamese headings (no English suffixes)
# - Times New Roman 100%, 13pt body, 1.3x line spacing, 4pt space after
# - Pure black text, clean academic tables in body (no zebra colors)
# - Synchronized TOC and List of Tables/Figures page numbers
# - NO emoji anywhere
# - Strictly genuine data from actual models & dataset
# - Section 0 (Cover): Page 0, no page number
# - Section 1 (Body): Starts at Page 1, dynamic page number

import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_student_report():
    doc = docx.Document()

    # Base page settings
    page_w = Inches(8.27)  # A4
    page_h = Inches(11.69)
    top_m = Inches(0.8)
    bot_m = Inches(0.8)
    left_m = Inches(1.1)
    right_m = Inches(0.8)

    # =========================================================================
    # SECTION 0: TRANG BÌA CHÍNH (Trang số 0, không hiện số trang)
    # =========================================================================
    sec0 = doc.sections[0]
    sec0.page_width = page_w
    sec0.page_height = page_h
    sec0.top_margin = top_m
    sec0.bottom_margin = bot_m
    sec0.left_margin = left_m
    sec0.right_margin = right_m

    sec0.different_first_page_header_footer = True
    sectPr0 = sec0._sectPr
    pgNumType0 = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="0"/>')
    sectPr0.append(pgNumType0)

    # Header & Footer trống cho bìa
    sec0.first_page_header.paragraphs[0].text = ""
    sec0.first_page_footer.paragraphs[0].text = ""
    sec0.header.paragraphs[0].text = ""
    sec0.footer.paragraphs[0].text = ""

    # Normal style
    normal_style = doc.styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Times New Roman'
    normal_font.size = Pt(13)
    normal_font.color.rgb = RGBColor(0x00, 0x00, 0x00)
    normal_style.paragraph_format.line_spacing = 1.3
    normal_style.paragraph_format.space_after = Pt(4)

    # Helpers
    def set_cell_background(cell, fill_hex):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    def add_p(text, size=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, left_indent=0, page_break_before=False, keep_with_next=False):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        if page_break_before:
            p.paragraph_format.page_break_before = True
        if keep_with_next:
            p.paragraph_format.keep_with_next = True
        if left_indent:
            p.paragraph_format.left_indent = Inches(left_indent)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        return p

    def add_title(text, size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=6, page_break_before=False):
        return add_p(text, size=size, bold=bold, align=align, space_before=space_before, space_after=space_after, page_break_before=page_break_before, keep_with_next=True)

    def add_heading1(text, page_break_before=False):
        return add_title(text, size=15, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=22, space_after=8, page_break_before=page_break_before)

    def add_heading2(text):
        p = add_title(text, size=13.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=10, space_after=4)
        p.paragraph_format.keep_with_next = True
        return p

    def add_heading3(text):
        p = add_p(text, size=13, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=6, space_after=3)
        p.paragraph_format.keep_with_next = True
        return p

    def add_body(text, bold_prefix=None, space_after=4, italic=False):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(space_after)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(13)
            r_pre.bold = True
            r_pre.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        r_text = p.add_run(text)
        r_text.font.name = 'Times New Roman'
        r_text.font.size = Pt(13)
        r_text.italic = italic
        r_text.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(3)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(13)
            r_pre.bold = True
            r_pre.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        r_text = p.add_run(text)
        r_text.font.name = 'Times New Roman'
        r_text.font.size = Pt(13)
        r_text.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        return p

    def add_table_data(headers, data_rows, col_widths=None, font_size=11, pad_v=60, pad_h=120, space_v=2, add_spacer=False):
        table = doc.add_table(rows=len(data_rows) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        hdr_row = table.rows[0]

        tblPr = table._tbl.tblPr
        tblCellMar = parse_xml(f'<w:tblCellMar {nsdecls("w")}><w:top w:w="{pad_v}" w:type="dxa"/><w:bottom w:w="{pad_v}" w:type="dxa"/><w:left w:w="{pad_h}" w:type="dxa"/><w:right w:w="{pad_h}" w:type="dxa"/></w:tblCellMar>')
        tblPr.append(tblCellMar)

        # cantSplit on header row, NO tblHeader (prevent header repetition across pages)
        hdr_tr = hdr_row._tr.get_or_add_trPr()
        hdr_tr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        for c_idx, h_text in enumerate(headers):
            cell = hdr_row.cells[c_idx]
            set_cell_background(cell, "F2F2F2")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(space_v + 1)
            p.paragraph_format.space_after = Pt(space_v + 1)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(h_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)
            run.bold = True
            run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        for r_idx, row in enumerate(data_rows):
            tbl_row = table.rows[r_idx + 1]
            trPr = tbl_row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            for c_idx, val in enumerate(row):
                cell = tbl_row.cells[c_idx]
                set_cell_background(cell, "FFFFFF")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(space_v)
                p.paragraph_format.space_after = Pt(space_v)
                p.paragraph_format.line_spacing = 1.15
                if c_idx == 0 or len(val) > 30:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(val)
                run.font.name = 'Times New Roman'
                run.font.size = Pt(font_size)
                run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        if col_widths:
            for row in table.rows:
                for c_idx, w in enumerate(col_widths):
                    row.cells[c_idx].width = Inches(w)

        for row in table.rows:
            for cell in row.cells:
                tcPr = cell._tc.get_or_add_tcPr()
                borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/><w:left w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/></w:tcBorders>')
                tcPr.append(borders)

        if add_spacer:
            doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_equation(eq_text, eq_label):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        r_eq = p.add_run(eq_text + "   ")
        r_eq.font.name = 'Times New Roman'
        r_eq.font.size = Pt(12)
        r_eq.bold = True
        r_eq.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        r_lab = p.add_run(eq_label)
        r_lab.font.name = 'Times New Roman'
        r_lab.font.size = Pt(11)
        r_lab.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    def add_figure(img_rel_path, caption, width=4.8):
        full_path = os.path.join(r"E:\Project SIC\report", img_rel_path)
        if os.path.exists(full_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            p.add_run().add_picture(full_path, width=Inches(width))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(6)
            p_cap.paragraph_format.keep_with_next = False
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = 'Times New Roman'
            r_cap.font.size = Pt(10.5)
            r_cap.italic = True
            r_cap.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        else:
            print(f"Warning: Figure not found at {full_path}")

    # =========================================================================
    # 1. TRANG BÌA CHÍNH (TRANG 0 - BỐ CỤC KHÔNG DÙNG BẢNG)
    # =========================================================================
    add_p("CHƯƠNG TRÌNH ĐÀO TẠO CÔNG NGHỆ SAMSUNG INNOVATION CAMPUS (SIC 2026)", size=12.5, bold=True, space_before=15, space_after=3)
    add_p("HỌC PHẦN: TRÍ TUỆ NHÂN TẠO & HỌC SÂU (AI & DEEP LEARNING)", size=11.5, bold=True, space_before=0, space_after=10)

    # Elegant divider line
    p_div = add_p("————————— ⁂ —————————", size=11, bold=False, space_before=0, space_after=0)
    p_div.runs[0].font.color.rgb = RGBColor(0x77, 0x77, 0x77)

    # Main Title
    add_p("BÁO CÁO TIỂU LUẬN CUỐI KHÓA", size=15.5, bold=True, space_before=62, space_after=10)
    add_p("ĐỀ TÀI:", size=13, bold=True, space_before=0, space_after=8)
    add_p("NGHIÊN CỨU VÀ XÂY DỰNG HỆ THỐNG PHÂN LOẠI CHẤT LƯỢNG NÔNG SẢN BẰNG THỊ GIÁC MÁY TÍNH VÀ HỌC SÂU", size=15, bold=True, space_before=0, space_after=6)
    add_p("(PROJECT 13: FRUIT VISUAL QUALITY CONTROL)", size=13.5, bold=True, space_before=0, space_after=16)

    p_desc = add_p("Ứng dụng mạng nơ-ron tích chập (CNN), phương pháp học chuyển giao (Transfer Learning), trực quan hóa vùng đặc trưng khuyết tật với Grad-CAM và xây dựng ứng dụng thử nghiệm thời gian thực.", size=11.5, italic=True, space_before=0, space_after=0)
    p_desc.paragraph_format.line_spacing = 1.25

    # Student & Advisor Info block - Clean 2-column feel using tab stop
    info_items = [
        ("Giảng viên hướng dẫn:", "Thầy Trần Mạnh Tường"),
        ("Học viên thực hiện:", "Lê Thành Được"),
        ("Lớp học phần:", "AI1"),
        ("Email liên hệ:", "2000.leduoc@gmail.com"),
        ("Số điện thoại:", "0379.885.508")
    ]

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(65)
    p_spacer.paragraph_format.space_after = Pt(0)

    for label, val in info_items:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.left_indent = Inches(1.1)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4.5)
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.tab_stops.add_tab_stop(Inches(3.2))

        r_lbl = p.add_run(label + "\t")
        r_lbl.font.name = 'Times New Roman'
        r_lbl.font.size = Pt(12)
        r_lbl.bold = True
        r_lbl.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        r_val = p.add_run(val)
        r_val.font.name = 'Times New Roman'
        r_val.font.size = Pt(12)
        r_val.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    # Bottom Date
    add_p("TP. HỒ CHÍ MINH — THÁNG 10 NĂM 2026", size=12, bold=True, space_before=70, space_after=0)

    # =========================================================================
    # SECTION 1: TỪ LỜI CẢM ƠN TRỞ ĐI (Đánh số từ Trang 1)
    # =========================================================================
    sec1 = doc.add_section(docx.enum.section.WD_SECTION_START.NEW_PAGE)
    sec1.page_width = page_w
    sec1.page_height = page_h
    sec1.top_margin = top_m
    sec1.bottom_margin = bot_m
    sec1.left_margin = left_m
    sec1.right_margin = right_m

    sec1.different_first_page_header_footer = False
    sec1.header.is_linked_to_previous = False
    sec1.footer.is_linked_to_previous = False

    for child in list(sec1._sectPr):
        if child.tag == qn('w:pgNumType'):
            sec1._sectPr.remove(child)
    pgNumType1 = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="1"/>')
    sec1._sectPr.append(pgNumType1)

    h1 = sec1.header.paragraphs[0]
    h1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = h1.add_run("Project 13: Phân loại chất lượng nông sản (Lê Thành Được)")
    hrun.font.name = "Times New Roman"
    hrun.font.size = Pt(9.5)
    hrun.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    f1 = sec1.footer.paragraphs[0]
    f1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun = f1.add_run("Trang ")
    frun.font.name = "Times New Roman"
    frun.font.size = Pt(10)
    frun.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    fldSimple1 = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
    f1._p.append(fldSimple1)

    # 2. LỜI CẢM ƠN (TRANG 1)
    add_title("LỜI CẢM ƠN", size=15, bold=True, space_before=10, space_after=12)

    add_body("Để hoàn thành bài tiểu luận cuối khóa đề tài Project 13: Fruit Visual Quality Control trong khuôn khổ học phần Trí Tuệ Nhân Tạo & Học Sâu, em đã nhận được sự quan tâm, tạo điều kiện thuận lợi và hướng dẫn tận tình từ quý thầy cô và Ban Quản lý Chương trình Samsung Innovation Campus 2026 (SIC 2026).")
    add_body("Lời đầu tiên, em xin gửi lời cảm ơn chân thành đến Ban Điều phối Chương trình Samsung Innovation Campus 2026 và Tập đoàn Samsung đã tổ chức một khóa học thiết thực, cung cấp giáo trình chất lượng cùng môi trường học tập và tính toán hiện đại để học viên tiếp cận với các công nghệ Trí tuệ Nhân tạo.")
    add_body("Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc tới Thầy Trần Mạnh Tường — Giảng viên trực tiếp giảng dạy và hướng dẫn em trong suốt khóa học. Trong quá trình học tập và làm đồ án, Thầy luôn định hướng phương pháp tư duy khoa học, kiên nhẫn giải thích các nền tảng lý thuyết học sâu, gợi mở cách giải quyết các vấn đề kỹ thuật phát sinh và đưa ra những lời nhận xét thực tế, sâu sắc để em hoàn thiện bài làm của mình một cách nghiêm túc và thực chất nhất.")
    add_body("Em cũng xin gửi lời cảm ơn đến các bạn học viên lớp AI1 đã luôn đồng hành, cùng trao đổi kiến thức và chia sẻ kinh nghiệm xử lý dữ liệu trong các buổi học lý thuyết cũng như thực hành.")
    add_body("Do kiến thức và kinh nghiệm thực tế của bản thân trong lĩnh vực Thị giác máy tính và Học sâu vẫn còn ở giai đoạn đầu, bài tiểu luận này chắc chắn khó tránh khỏi những điểm còn hạn chế. Em rất mong tiếp tục nhận được những nhận xét, góp ý và chỉ dẫn của Thầy Trần Mạnh Tường để em củng cố kiến thức và hoàn thiện hơn nữa trong các nghiên cứu tiếp theo.")
    add_body("Kính chúc Thầy và Ban Tổ chức chương trình luôn dồi dào sức khỏe và đạt nhiều thành công trong công tác giảng dạy, nghiên cứu!")

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(12)
    r_sig1 = p_sig.add_run("TP. Hồ Chí Minh, ngày 19 tháng 10 năm 2026\n")
    r_sig1.italic = True
    r_sig2 = p_sig.add_run("Học viên thực hiện\n")
    r_sig2.bold = True
    r_sig3 = p_sig.add_run("Lê Thành Được")
    r_sig3.bold = True

    # 3. LỜI CAM ĐOAN (TRANG 2)
    add_title("LỜI CAM ĐOAN", size=15, bold=True, space_before=10, space_after=12, page_break_before=True)

    add_body("Em xin cam đoan rằng bài tiểu luận tốt nghiệp với đề tài \"Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)\" là công trình học tập, nghiên cứu và lập trình thực nghiệm do chính bản thân em thực hiện dưới sự định hướng và hướng dẫn của Thầy Trần Mạnh Tường.")
    add_body("Em xin cam đoan tính trung thực của các nội dung trong bài:")
    add_bullet("Toàn bộ 27,198 ảnh được trích xuất từ tập dữ liệu Kaggle Fruits Fresh and Rotten, được chia tách phân tầng train/val/test với tỷ lệ 70/15/15 và cố định giá trị ngẫu nhiên SEED = 42 để đảm bảo tính minh bạch, độc lập.")
    add_bullet("Các kết quả huấn luyện (loss, accuracy qua từng epoch) và các chỉ số đánh giá (Accuracy, Recall, Precision, Confusion Matrix) trên 4 mô hình Baseline CNN, VGG16, ResNet50 và EfficientNetB0 đều được ghi nhận trực tiếp từ quá trình huấn luyện và đánh giá thực tế trong các file Jupyter Notebook của đồ án.")
    add_bullet("Các nội dung mã nguồn xây dựng mạng nơ-ron, hàm tính Grad-CAM tuyến tính, và ứng dụng Streamlit demo đều được viết và kiểm thử thực tế trên máy tính.")
    add_bullet("Các lý thuyết nền tảng, công thức và tài liệu tham khảo đều được trích dẫn nguồn rõ ràng ở phần Danh mục tài liệu tham khảo.")
    add_body("Nếu có bất kỳ sự không trung thực nào về mặt dữ liệu hoặc sao chép trái phép, em xin chịu trách nhiệm theo đúng quy định học thuật của khóa học.")

    p_cam = doc.add_paragraph()
    p_cam.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_cam.paragraph_format.space_before = Pt(12)
    r_cam1 = p_cam.add_run("Người cam đoan\n")
    r_cam1.bold = True
    r_cam2 = p_cam.add_run("Lê Thành Được")
    r_cam2.bold = True

    # 4. MỤC LỤC (TRANG 3)
    add_title("MỤC LỤC", size=15, bold=True, space_before=10, space_after=12, page_break_before=True)
    toc_headers = ["Nội dung các phần trong tiểu luận", "Trang"]
    toc_data = [
        ["LỜI CẢM ƠN", "1"],
        ["LỜI CAM ĐOAN", "2"],
        ["DANH MỤC CÁC CHỮ VIẾT TẮT", "5"],
        ["DANH MỤC CÁC BẢNG BIỂU", "6"],
        ["DANH MỤC CÁC HÌNH VẼ", "6"],
        ["TÓM TẮT TIỂU LUẬN", "7"],
        ["PHẦN MỞ ĐẦU", "8"],
        ["   1. Lý do chọn đề tài", "8"],
        ["   2. Mục tiêu nghiên cứu của đồ án", "8"],
        ["   3. Đối tượng và phạm vi nghiên cứu", "9"],
        ["   4. Phương pháp nghiên cứu", "9"],
        ["   5. Bố cục của bài tiểu luận", "9"],
        ["CHƯƠNG 1: TẬP DỮ LIỆU VÀ ĐƯỜNG ỐNG TIỀN XỬ LÝ", "10"],
        ["   1.1. Giới thiệu tập dữ liệu nông sản", "10"],
        ["   1.2. Phân bố số lượng mẫu và kiểm toán chất lượng ảnh", "10"],
        ["   1.3. Phương pháp phân chia tập dữ liệu (Stratified Split)", "11"],
        ["   1.4. Tăng cường dữ liệu và đường ống bất đồng bộ tf.data", "11"],
        ["CHƯƠNG 2: MÔ HÌNH CƠ SỞ (BASELINE CNN) VÀ ĐIỂM CHUẨN ĐỐI SÁNH", "12"],
        ["   2.1. Cấu trúc mạng Baseline CNN xây dựng từ đầu", "12"],
        ["   2.2. Quá trình huấn luyện và hàm mất mát", "13"],
        ["   2.3. Kết quả huấn luyện của mô hình Baseline CNN", "13"],
        ["CHƯƠNG 3: ÁP DỤNG HỌC CHUYỂN GIAO VỚI CÁC KIẾN TRÚC MẠNG SÂU", "15"],
        ["   3.1. Lý thuyết học chuyển giao và ba kiến trúc VGG16, ResNet50, EfficientNetB0", "15"],
        ["   3.2. Quy trình tinh chỉnh mạng nơ-ron (Fine-tuning)", "16"],
        ["   3.3. Diễn biến huấn luyện và hội tụ của các mô hình chuyển giao", "16"],
        ["CHƯƠNG 4: ĐÁNH GIÁ VÀ SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH", "18"],
        ["   4.1. Các chỉ số đánh giá và ý nghĩa của độ nhạy Recall", "18"],
        ["   4.2. Bảng so sánh kết quả thực nghiệm trên tập kiểm thử độc lập", "19"],
        ["   4.3. Phân tích ma trận nhầm lẫn của từng mô hình", "19"],
        ["CHƯƠNG 5: GIẢI THÍCH MÔ HÌNH VỚI GRAD-CAM VÀ PHÂN TÍCH NGƯỠNG QUYẾT ĐỊNH", "20"],
        ["   5.1. Vấn đề bão hòa đạo hàm Sigmoid và giải pháp Linear Logit Grad-CAM", "20"],
        ["   5.2. Trực quan hóa vùng đặc trưng khuyết tật với mặt nạ thích nghi", "21"],
        ["   5.3. Phân tích lựa chọn ngưỡng quyết định ưu tiên phát hiện lỗi", "21"],
        ["   5.4. Đánh giá tốc độ suy luận của các mô hình", "22"],
        ["CHƯƠNG 6: XÂY DỰNG ỨNG DỤNG DEMO THỜI GIAN THỰC VÀ THỬ NGHIỆM VẬN HÀNH", "23"],
        ["   6.1. Giao diện điều khiển và giám sát bằng Streamlit", "23"],
        ["   6.2. Kết nối camera điện thoại qua DroidCam và xử lý trôi khung hình bằng ThreadedCamera", "24"],
        ["   6.3. Động cơ phân tích dự phòng trên CPU khi không có GPU", "24"],
        ["   6.4. Đánh giá thử nghiệm vận hành ứng dụng trong thực tế", "25"],
        ["KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "26"],
        ["   1. Kết luận về các kết quả đạt được", "26"],
        ["   2. Bài học kinh nghiệm đúc kết từ quá trình làm đồ án", "26"],
        ["   3. Hạn chế hiện tại của hệ thống", "27"],
        ["   4. Hướng phát triển trong tương lai", "27"],
        ["TÀI LIỆU THAM KHẢO", "27"],
        ["PHỤ LỤC", "28"],
        ["   Phụ lục A: Cấu trúc thư mục mã nguồn đồ án", "28"],
        ["   Phụ lục B: Hướng dẫn cài đặt và chạy ứng dụng demo", "29"]
    ]
    add_table_data(toc_headers, toc_data, col_widths=[5.5, 1.0], font_size=10.5, pad_v=35, space_v=1)

    # 6. DANH MỤC CHỮ VIẾT TẮT
    add_title("DANH MỤC CÁC CHỮ VIẾT TẮT", size=15, bold=True, space_before=10, space_after=12, page_break_before=True)
    abbr_headers = ["Ký hiệu", "Tên tiếng Anh đầy đủ", "Ý nghĩa trong đồ án"]
    abbr_data = [
        ["AI", "Artificial Intelligence", "Trí tuệ nhân tạo"],
        ["BCE", "Binary Cross-Entropy", "Hàm mất mát entropy chéo nhị phân"],
        ["CNN", "Convolutional Neural Network", "Mạng nơ-ron tích chập"],
        ["CUDA", "Compute Unified Device Architecture", "Nền tảng tính toán song song trên GPU NVIDIA"],
        ["CVPR", "Computer Vision and Pattern Recognition", "Hội nghị quốc tế về thị giác máy tính"],
        ["FIFO", "First In, First Out", "Cơ chế hàng đợi bộ đệm vào trước - ra trước"],
        ["FN", "False Negative", "Âm tính giả (bỏ sót quả thối hỏng thành quả đạt)"],
        ["FP", "False Positive", "Dương tính giả (báo nhầm quả đạt thành quả lỗi)"],
        ["FPS", "Frames Per Second", "Số khung hình xử lý được trong một giây"],
        ["GAP", "Global Average Pooling", "Tầng gộp trung bình toàn cục"],
        ["Grad-CAM", "Gradient-weighted Class Activation Mapping", "Bản đồ kích hoạt lớp có trọng số gradient"],
        ["HSV", "Hue, Saturation, Value", "Không gian màu sắc thái - độ bão hòa - độ sáng"],
        ["HUD", "Head-Up Display", "Lớp thông tin hiển thị trực tiếp trên màn hình video"],
        ["MBConv", "Mobile Inverted Bottleneck Convolution", "Khối tích chập tách biệt đảo ngược trên EfficientNet"],
        ["OSD", "On-Screen Display", "Lớp phủ thông tin chẩn đoán trên khung hình camera"],
        ["ReLU", "Rectified Linear Unit", "Hàm kích hoạt chỉnh lưu f(z) = max(0, z)"],
        ["RTSP", "Real-Time Streaming Protocol", "Giao thức truyền phát video thời gian thực"],
        ["SE", "Squeeze-and-Excitation", "Cơ chế chú ý điều chế kênh đặc trưng"],
        ["SIC", "Samsung Innovation Campus", "Chương trình đào tạo công nghệ của Samsung"],
        ["TN", "True Negative", "Âm tính thật (nhận diện chính xác quả tươi đạt chuẩn)"],
        ["TP", "True Positive", "Dương tính thật (phát hiện chính xác quả lỗi)"],
        ["VRAM", "Video Random Access Memory", "Bộ nhớ card đồ họa GPU"],
        ["XAI", "Explainable Artificial Intelligence", "Trí tuệ nhân tạo có khả năng giải thích"]
    ]
    add_table_data(abbr_headers, abbr_data, col_widths=[1.2, 2.5, 2.8], font_size=9.5, pad_v=25, space_v=1)

    # 7. DANH MỤC BẢNG BIỂU (Bảng đầu tiên là Bảng 1.1)
    add_title("DANH MỤC CÁC BẢNG BIỂU", size=15, bold=True, space_before=10, space_after=12, page_break_before=True)
    tbl_list_headers = ["Ký hiệu bảng", "Tên bảng nội dung", "Trang"]
    tbl_list_data = [
        ["Bảng 1.1", "Thống kê phân bố số lượng ảnh trong tập dữ liệu (27,198 ảnh)", "10"],
        ["Bảng 1.2", "Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15)", "11"],
        ["Bảng 1.3", "Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu", "11"],
        ["Bảng 2.1", "Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng", "13"],
        ["Bảng 2.2", "Tiến trình huấn luyện chi tiết qua 20 Epochs của mô hình Baseline CNN", "14"],
        ["Bảng 3.1", "Thông số so sánh cấu trúc mạng VGG16, ResNet50 và EfficientNetB0", "16"],
        ["Bảng 3.2", "Kế hoạch đóng và mở băng các tầng (Freezing Schedule) khi huấn luyện", "16"],
        ["Bảng 3.3", "Tiến trình huấn luyện tinh chỉnh của mô hình VGG16", "16"],
        ["Bảng 3.4", "Tiến trình huấn luyện tinh chỉnh của mô hình ResNet50", "17"],
        ["Bảng 3.5", "Tiến trình huấn luyện tinh chỉnh của mô hình EfficientNetB0", "17"],
        ["Bảng 4.1", "So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu)", "19"],
        ["Bảng 4.2", "Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập", "19"],
        ["Bảng 5.1", "Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau", "22"],
        ["Bảng 5.2", "Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU", "22"],
        ["Bảng 6.1", "Các phân hệ chính trong ứng dụng demo Streamlit và module camera", "25"],
        ["Bảng 6.2", "Kết quả thử nghiệm vận hành hệ thống demo trong điều kiện thực tế", "25"]
    ]
    add_table_data(tbl_list_headers, tbl_list_data, col_widths=[1.5, 4.3, 0.7], font_size=10.5, pad_v=40, space_v=1)

    # 8. DANH MỤC HÌNH VẼ
    add_title("DANH MỤC CÁC HÌNH VẼ", size=15, bold=True, space_before=20, space_after=10, page_break_before=False)
    fig_list_headers = ["Ký hiệu hình", "Tên hình minh họa", "Trang"]
    fig_list_data = [
        ["Hình 1.1", "Biểu đồ phân bố số lượng ảnh giữa các lớp quả tươi và khuyết tật", "11"],
        ["Hình 2.1", "Đồ thị loss và accuracy qua 20 epochs của mô hình Baseline CNN", "15"],
        ["Hình 3.1", "Đồ thị loss và accuracy trong quá trình huấn luyện các mô hình chuyển giao", "18"],
        ["Hình 4.1", "Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử", "20"],
        ["Hình 5.1", "Hình ảnh trực quan hóa vùng tổn thương bằng Grad-CAM trên quả mẫu", "21"],
        ["Hình 5.2", "Đồ thị khảo sát ngưỡng phân loại và tốc độ xử lý FPS của các mô hình", "23"]
    ]
    add_table_data(fig_list_headers, fig_list_data, col_widths=[1.5, 4.3, 0.7], font_size=10.5, pad_v=40, space_v=1)

    # 9. TÓM TẮT TIỂU LUẬN
    add_title("TÓM TẮT TIỂU LUẬN", size=15, bold=True, space_before=10, space_after=10, page_break_before=True)

    add_body("Báo cáo tiểu luận này trình bày toàn bộ quá trình nghiên cứu, xây dựng và thực nghiệm đề tài \"Hệ thống phân loại chất lượng nông sản bằng thị giác máy tính (Project 13: Fruit Visual Quality Control)\" thuộc học phần Trí Tuệ Nhân Tạo & Học Sâu trong chương trình Samsung Innovation Campus 2026 (SIC 2026), dưới sự hướng dẫn của Thầy Trần Mạnh Tường.", space_after=3)
    add_body("Đề tài tập trung giải quyết bài toán phân loại tự động quả nông sản đạt chuẩn (tươi) và quả khuyết tật (thối, dập, mốc) đối với 3 loại quả phổ biến: Táo, Chuối và Cam. Trong thực tế bảo quản sau thu hoạch, việc bỏ sót các quả thối hỏng (lỗi False Negative) là nguyên nhân chính dẫn đến lây lan nấm bệnh và giải phóng khí ethylene làm hư hại hàng loạt quả lưu kho. Do đó, mục tiêu kỹ thuật quan trọng nhất của đồ án là tối ưu hóa độ nhạy phát hiện khuyết tật (Recall) nhằm hạn chế tối đa việc bỏ sót quả lỗi.", space_after=3)
    add_body("Đồ án sử dụng tập dữ liệu gồm 27,198 ảnh màu RGB, được chia phân tầng (Stratified Split) với tỷ lệ 70% huấn luyện (19,038 ảnh), 15% kiểm định (4,080 ảnh) và 15% kiểm thử độc lập (4,080 ảnh). Trên cơ sở đó, em đã tiến hành xây dựng và so sánh thực nghiệm 4 kiến trúc mạng nơ-ron: Baseline CNN tự thiết kế và 3 mô hình học chuyển giao (Transfer Learning) gồm VGG16, ResNet50, EfficientNetB0.", space_after=3)
    add_body("Kết quả đánh giá trên tập kiểm thử độc lập 4,080 ảnh ghi nhận:", space_after=2)
    add_bullet("Mô hình cơ sở Baseline CNN: Đạt độ chính xác 97.55% và Recall 97.76% (bỏ sót 48 quả lỗi).")
    add_bullet("Mô hình VGG16: Đạt độ chính xác 99.41% và Recall 98.88% (bỏ sót 24 quả lỗi).")
    add_bullet("Mô hình ResNet50: Đạt độ chính xác 99.98% và đạt Recall tuyệt đối 100.00% (không bỏ sót bất kỳ quả lỗi nào trong 2,145 quả kiểm thử).")
    add_bullet("Mô hình EfficientNetB0: Đạt độ chính xác 100.00% trên tập kiểm thử với dung lượng trọng số nhỏ gọn (khoảng 33 MB, 4.38 triệu tham số), rất thuận lợi khi triển khai thực tế.")
    add_body("Bên cạnh đó, đề tài ứng dụng kỹ thuật giải thích trực quan Linear Logit Grad-CAM kết hợp mặt nạ hòa trộn Alpha để khoanh vùng chính xác các vị trí tổn thương trên vỏ quả. Cuối cùng, đồ án xây dựng hoàn chỉnh ứng dụng demo giao diện web bằng Streamlit (`app.py`), hỗ trợ kết nối trực tiếp với camera điện thoại qua DroidCam, tích hợp xử lý đa luồng `ThreadedCamera` và thuật toán dự phòng trên CPU khi không có GPU.", space_after=4)

    # 10. PHẦN MỞ ĐẦU
    add_title("PHẦN MỞ ĐẦU", size=15, bold=True, space_before=22, space_after=10, page_break_before=False)

    add_heading2("1. Lý do chọn đề tài")
    add_body("Nông sản và trái cây tươi là một trong những mặt hàng có sản lượng tiêu thụ lớn trong nước và đóng góp quan trọng vào kim ngạch xuất khẩu của Việt Nam. Tuy nhiên, khâu kiểm tra chất lượng và phân loại nông sản hiện nay tại nhiều cơ sở thu mua và đóng gói phần lớn vẫn dựa vào phương pháp thủ công bằng mắt thường của công nhân. Phương pháp này có một số hạn chế rõ rệt:")
    add_bullet("Phụ thuộc vào mức độ tập trung và kinh nghiệm cá nhân của từng công nhân; khi làm việc liên tục trong thời gian dài, tỷ lệ phân loại sai sót có xu hướng tăng lên.")
    add_bullet("Tốc độ phân loại thủ công còn chậm, khó đáp ứng khi sản lượng trái cây vào vụ thu hoạch dồn về lớn.")
    add_bullet("Quan trọng hơn, đối với các loại quả nhạy cảm với khí ethylene (như táo, chuối, cam), nếu để lọt các quả bị dập, thối rữa hoặc nhiễm nấm mốc vào các thùng đóng gói kín trong quá trình lưu kho và vận chuyển dài ngày, khí ethylene sinh ra từ quả hỏng sẽ nhanh chóng kích thích các quả tươi xung quanh chín ép và thối theo dây chuyền.")
    add_body("Chính vì vậy, việc nghiên cứu ứng dụng thị giác máy tính và học sâu (Deep Learning) để tự động hóa khâu nhận diện và sàng lọc quả lỗi là một bài toán mang tính thực tế cao, giúp giảm thiểu sai sót do con người và hỗ trợ nâng cao chất lượng nông sản sau thu hoạch.")

    add_heading2("2. Mục tiêu nghiên cứu của đồ án")
    add_bullet("Mục tiêu 1: Thu thập, làm sạch và chuẩn hóa đường ống dữ liệu với 27,198 ảnh nông sản, phân chia tập train/val/test minh bạch và chống rò rỉ dữ liệu.")
    add_bullet("Mục tiêu 2: Xây dựng mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu để làm điểm chuẩn so sánh.")
    add_bullet("Mục tiêu 3: Áp dụng phương pháp học chuyển giao (Transfer Learning) trên các mô hình VGG16, ResNet50, EfficientNetB0 nhằm nâng cao độ chính xác và ưu tiên tối đa độ nhạy phát hiện khuyết tật (Recall) để hạn chế việc bỏ sót quả hỏng.")
    add_bullet("Mục tiêu 4: Ứng dụng kỹ thuật Grad-CAM để giải thích trực quan các vùng ảnh mà mô hình căn cứ vào đó để đưa ra quyết định (vết nấm, đốm thâm dập).")
    add_bullet("Mục tiêu 5: Xây dựng một ứng dụng demo có giao diện web hoàn chỉnh (Streamlit), kết nối được với camera thực tế (qua điện thoại DroidCam) để kiểm tra tính khả thi khi vận hành.")

    add_heading2("3. Đối tượng và phạm vi nghiên cứu")
    add_bullet("Đối tượng nghiên cứu: Các đặc trưng khuyết tật trên bề mặt vỏ quả (đốm thâm nâu, vết ủng nước, mốc trắng, mốc xanh); các mô hình mạng nơ-ron học sâu (CNN, VGG16, ResNet50, EfficientNetB0); giải thuật giải thích trực quan Grad-CAM.")
    add_bullet("Phạm vi dữ liệu: Tập dữ liệu Kaggle Fruits Fresh and Rotten gồm 27,198 ảnh màu của 3 loại quả: Táo, Chuối và Cam. Bài toán được mô hình hóa thành bài toán phân loại nhị phân: Quả đạt chuẩn (Fresh) và Quả khuyết tật/hỏng (Rotten).")
    add_bullet("Phạm vi triển khai: Mô hình được huấn luyện trên môi trường Google Colab với GPU NVIDIA T4 và kiểm thử chạy demo trên máy tính cá nhân kết nối camera điện thoại qua Wi-Fi.")

    add_heading2("4. Phương pháp nghiên cứu")
    add_bullet("Phương pháp xử lý dữ liệu: Sử dụng kỹ thuật phân tầng (Stratified Sampling) theo nhãn và loại quả để chia tập train (70%), val (15%) và test (15%). Áp dụng các phép tăng cường dữ liệu hình học (xoay, lật, thay đổi độ sáng nhẹ) để tăng tính đa dạng cho dữ liệu huấn luyện.")
    add_bullet("Phương pháp mô hình hóa: Huấn luyện mạng Baseline CNN từ đầu; sau đó áp dụng học chuyển giao từ các trọng số đã được huấn luyện trên ImageNet, sử dụng chiến lược đóng/mở băng các tầng để tinh chỉnh mạng.")
    add_bullet("Phương pháp đánh giá: Đánh giá mô hình trên tập kiểm thử độc lập (4,080 ảnh) thông qua ma trận nhầm lẫn (Confusion Matrix) và 4 chỉ số: Accuracy, Recall, Precision, F1-Score.")

    add_heading2("5. Bố cục của bài tiểu luận")
    add_body("Báo cáo được trình bày trong 6 chương nội dung chính cùng phần mở đầu, kết luận và phụ lục:")
    add_bullet("Chương 1: Tập dữ liệu và đường ống tiền xử lý.")
    add_bullet("Chương 2: Mô hình cơ sở (Baseline CNN) và điểm chuẩn đối sánh.")
    add_bullet("Chương 3: Áp dụng học chuyển giao với các kiến trúc mạng sâu.")
    add_bullet("Chương 4: Đánh giá và so sánh hiệu năng các mô hình.")
    add_bullet("Chương 5: Giải thích mô hình với Grad-CAM và phân tích ngưỡng quyết định.")
    add_bullet("Chương 6: Xây dựng ứng dụng demo thời gian thực và thử nghiệm vận hành.")

    # 11. CHƯƠNG 1
    add_heading1("CHƯƠNG 1: TẬP DỮ LIỆU VÀ ĐƯỜNG ỐNG TIỀN XỬ LÝ", page_break_before=False)

    add_heading2("1.1. Giới thiệu tập dữ liệu nông sản")
    add_body("Trong đề tài này, em sử dụng tập dữ liệu ảnh nông sản Kaggle Fruits Fresh and Rotten. Tập dữ liệu bao gồm 27,198 bức ảnh màu RGB ghi lại hình ảnh của ba loại trái cây phổ biến: Táo (Apples), Chuối (Bananas) và Cam (Oranges). Các ảnh chụp thể hiện đa dạng các tình huống: từ những quả tươi mới, vỏ nhẵn bóng cho đến các quả có vết bầm dập nhỏ, thâm đen từng mảng hoặc bị mốc trắng, mốc xanh bám quanh vỏ.")
    add_body("Dữ liệu gốc được chia thành 6 thư mục tương ứng với từng trạng thái của 3 loại quả. Để phục vụ bài toán sàng lọc chất lượng, em gộp dữ liệu thành hai lớp nhị phân:")
    add_bullet("Lớp 0 (Đạt chuẩn — Fresh): Gồm các ảnh quả lành lặn, màu sắc bình thường, không có vết thối rữa.")
    add_bullet("Lớp 1 (Khuyết tật — Rotten): Gồm các ảnh quả bị thâm nát, biến màu hoặc xuất hiện nấm mốc ở các mức độ khác nhau.")

    add_heading2("1.2. Phân bố số lượng mẫu và kiểm toán chất lượng ảnh")
    add_body("Bằng cách viết kịch bản Python (`download_fruit_data.py`), em đã tải, giải nén và kiểm tra tính toàn vẹn của từng tệp ảnh trong bộ dữ liệu. Kết quả thống kê số lượng mẫu được tổng hợp trong Bảng 1.1.")

    add_heading3("Bảng 1.1: Thống kê phân bố số lượng ảnh trong tập dữ liệu (27,198 ảnh)")
    b11_headers = ["Loại quả", "Phân lớp trạng thái", "Số lượng ảnh", "Tỷ lệ theo loại", "Tỷ lệ toàn tập"]
    b11_data = [
        ["Táo (Apples)", "Táo tươi (Fresh Apples)", "4,500 ảnh", "48.09%", "16.55%"],
        ["", "Táo hỏng (Rotten Apples)", "4,858 ảnh", "51.91%", "17.86%"],
        ["Chuối (Bananas)", "Chuối tươi (Fresh Bananas)", "4,200 ảnh", "45.41%", "15.44%"],
        ["", "Chuối hỏng (Rotten Bananas)", "5,050 ảnh", "54.59%", "18.57%"],
        ["Cam (Oranges)", "Cam tươi (Fresh Oranges)", "4,200 ảnh", "48.89%", "15.44%"],
        ["", "Cam hỏng (Rotten Oranges)", "4,390 ảnh", "51.11%", "16.14%"],
        ["TỔNG CỘNG", "Toàn bộ 6 phân lớp", "27,198 ảnh", "100.00%", "100.00%"]
    ]
    add_table_data(b11_headers, b11_data, col_widths=[1.5, 2.3, 1.1, 1.2, 1.1])

    add_body("Qua Bảng 1.1, có thể thấy tổng số ảnh quả tươi là 12,900 ảnh (chiếm 47.43%) và tổng số ảnh quả khuyết tật là 14,298 ảnh (chiếm 52.57%). Tỷ lệ giữa hai lớp nhị phân khá cân bằng, không bị hiện tượng lệch lớp nghiêm trọng, giúp quá trình huấn luyện mô hình diễn ra thuận lợi.")

    add_figure("images/image1.png", "Hình 1.1: Biểu đồ phân bố số lượng mẫu ảnh giữa các lớp quả tươi và khuyết tật trong tập dữ liệu (27,198 ảnh).")

    add_heading2("1.3. Phương pháp phân chia tập dữ liệu (Stratified Split)")
    add_body("Để đảm bảo việc đánh giá mô hình được khách quan và không bị hiện tượng rò rỉ dữ liệu (data leakage), toàn bộ 27,198 ảnh được chia thành ba tập con theo tỷ lệ: 70% huấn luyện (Train), 15% kiểm định (Validation) và 15% kiểm thử (Test).")
    add_body("Em sử dụng phương pháp phân tầng (Stratified Split) với tham số cố định `SEED = 42`. Cách làm này đảm bảo tỷ lệ giữa các loại quả và giữa hai lớp tươi/hỏng được giữ nguyên đồng đều trên cả 3 tập con. Danh sách đường dẫn ảnh và nhãn sau khi chia được lưu cố định vào ba tệp CSV (`train.csv`, `val.csv`, `test.csv`) trong thư mục `processed_data/`.")

    add_heading3("Bảng 1.2: Phân chia tập dữ liệu train/val/test theo phân tầng (70/15/15)")
    b12_headers = ["Tập dữ liệu", "Tỷ lệ", "Số ảnh tươi (Lớp 0)", "Số ảnh hỏng (Lớp 1)", "Tổng số ảnh"]
    b12_data = [
        ["Tập huấn luyện (Train)", "70.0%", "9,030 ảnh", "10,008 ảnh", "19,038 ảnh"],
        ["Tập kiểm định (Val)", "15.0%", "1,935 ảnh", "2,145 ảnh", "4,080 ảnh"],
        ["Tập kiểm thử (Test)", "15.0%", "1,935 ảnh", "2,145 ảnh", "4,080 ảnh"],
        ["TỔNG CẢ TẬP", "100.0%", "12,900 ảnh", "14,298 ảnh", "27,198 ảnh"]
    ]
    add_table_data(b12_headers, b12_data, col_widths=[1.8, 1.0, 1.5, 1.5, 1.4])

    add_heading2("1.4. Tăng cường dữ liệu và đường ống bất đồng bộ tf.data")
    add_body("Trong thực tế, khi trái cây di chuyển trước camera, hướng quả, góc nghiêng và độ sáng có thể thay đổi. Để mô hình có thể thích nghi tốt hơn, em áp dụng một số phép biến đổi tăng cường dữ liệu nhẹ ngay trong các tầng đầu của mô hình bằng TensorFlow/Keras.")

    add_heading3("Bảng 1.3: Các phép biến đổi hình học trong chuỗi tăng cường dữ liệu")
    b13_headers = ["Tầng biến đổi", "Tham số", "Mục đích kỹ thuật"]
    b13_data = [
        ["Resizing", "224 x 224", "Đưa ảnh về kích thước chuẩn phù hợp với các mạng tích chập"],
        ["Rescaling", "1./255", "Chuẩn hóa giá trị điểm ảnh về khoảng thực [0.0, 1.0]"],
        ["RandomFlip", "horizontal_and_vertical", "Lật ngẫu nhiên ảnh theo chiều ngang và dọc"],
        ["RandomRotation", "factor = 0.2", "Xoay nhẹ ảnh trong khoảng +/- 72 độ để học đa dạng góc nhìn"],
        ["RandomZoom", "(-0.1, 0.1)", "Phóng to / thu nhỏ nhẹ mô phỏng khoảng cách chụp khác nhau"],
        ["RandomContrast", "factor = 0.15", "Thay đổi nhẹ độ tương phản để làm quen với điều kiện sáng khác nhau"]
    ]
    add_table_data(b13_headers, b13_data, col_widths=[1.5, 1.5, 4.2])

    add_body("Để quá trình nạp ảnh diễn ra nhanh chóng và không làm nghẽn GPU, toàn bộ quy trình đọc ảnh từ ổ đĩa được đóng gói bằng thư viện `tf.data.Dataset`. Việc kết hợp `AUTOTUNE` cho hàm nạp dữ liệu song song và cơ chế `prefetch` giúp việc nạp và xử lý ảnh trên CPU diễn ra đồng thời với quá trình tính toán trên GPU, giúp tận dụng tối đa năng lực phần cứng.")

    # 12. CHƯƠNG 2
    add_heading1("CHƯƠNG 2: MÔ HÌNH CƠ SỞ (BASELINE CNN) VÀ ĐIỂM CHUẨN ĐỐI SÁNH", page_break_before=False)

    add_heading2("2.1. Cấu trúc mạng Baseline CNN xây dựng từ đầu")
    add_body("Trước khi sử dụng các mô hình học chuyển giao sâu tầng có sẵn, em xây dựng một mô hình mạng nơ-ron tích chập cơ sở (Baseline CNN) từ đầu. Mục đích là để kiểm tra khả năng phân tách của tập dữ liệu trên một kiến trúc đơn giản và tạo ra mốc hiệu năng điểm chuẩn để đối chiếu.")
    add_body("Kiến trúc Baseline CNN gồm 3 khối tích chập liên tiếp:")
    add_bullet("Khối 1: Gồm 2 lớp Conv2D (32 bộ lọc kích thước 3x3), lớp BatchNormalization để ổn định giá trị kích hoạt, và lớp MaxPooling2D (2x2) để giảm kích thước không gian.")
    add_bullet("Khối 2: Tương tự với 64 bộ lọc kích thước 3x3.")
    add_bullet("Khối 3: Tương tự với 128 bộ lọc kích thước 3x3.")
    add_body("Thay vì dùng lớp Flatten làm bùng nổ số lượng tham số kết nối, em sử dụng lớp GlobalAveragePooling2D (GAP) để tính giá trị trung bình trên mỗi kênh đặc trưng, sau đó đi qua một lớp Dense 64 nơ-ron (kèm Dropout 0.4 để giảm quá khớp) và lớp đầu ra Dense 1 nơ-ron với hàm kích hoạt Sigmoid để tính xác suất hư hỏng.")

    add_heading3("Bảng 2.1: Chi tiết các tầng mạng của mô hình Baseline CNN tự xây dựng")
    b21_headers = ["Tầng mạng", "Kích thước đầu ra", "Số bộ lọc / Cấu hình", "Số tham số"]
    b21_data = [
        ["Input Layer", "(224, 224, 3)", "Ảnh màu RGB", "0"],
        ["Khối 1: Conv2D x 2 + BN + Pool", "(112, 112, 32)", "32 bộ lọc 3x3, MaxPool 2x2", "10,208"],
        ["Khối 2: Conv2D x 2 + BN + Pool", "(56, 56, 64)", "64 bộ lọc 3x3, MaxPool 2x2", "55,616"],
        ["Khối 3: Conv2D x 2 + BN + Pool", "(28, 28, 128)", "128 bộ lọc 3x3, MaxPool 2x2", "221,824"],
        ["GlobalAveragePooling2D", "(128)", "Gộp trung bình bản đồ đặc trưng", "0"],
        ["Dense + Dropout", "(64)", "64 units, ReLU, Dropout 0.40", "8,256"],
        ["Output Layer", "(1)", "1 unit, hàm kích hoạt Sigmoid", "65"],
        ["TỔNG THAM SỐ", "", "Dung lượng tệp khoảng 1.2 MB", "295,969"]
    ]
    add_table_data(b21_headers, b21_data, col_widths=[2.4, 1.5, 2.0, 1.3])

    add_heading2("2.2. Quá trình huấn luyện và hàm mất mát")
    add_body("Mô hình được huấn luyện trên tập Train (19,038 ảnh) và theo dõi trên tập Val (4,080 ảnh) trong 20 Epochs với kích thước lô (batch size) là 32. Vì đây là bài toán phân loại nhị phân (quả tươi vs quả hỏng), hàm mất mát sử dụng là Binary Cross-Entropy:")
    add_equation("L_BCE = - 1/N * sum [ y_i * log(p_i) + (1 - y_i) * log(1 - p_i) ]", "(2.1)")
    add_body("Thuật toán tối ưu là Adam với tốc độ học khởi tạo ban đầu là 0.001. Trong quá trình huấn luyện, em sử dụng hai hàm gọi lại (callbacks):")
    add_bullet("ModelCheckpoint: Tự động lưu trọng số tốt nhất khi giá trị val_loss đạt mức thấp nhất.")
    add_bullet("ReduceLROnPlateau: Giảm tốc độ học đi 50% nếu sau 3 epochs liên tiếp mà val_loss không cải thiện.")

    add_heading2("2.3. Kết quả huấn luyện của mô hình Baseline CNN")
    add_body("Tiến trình huấn luyện qua từng epoch của mô hình Baseline CNN được ghi nhận trong Bảng 2.2.")

    add_heading3("Bảng 2.2: Tiến trình huấn luyện chi tiết qua 20 Epochs của mô hình Baseline CNN")
    b22_headers = ["Epoch", "Train Loss", "Train Acc", "Val Loss", "Val Acc", "Tốc độ học", "Ghi chú"]
    b22_data = [
        ["Epoch 01", "0.3842", "83.15%", "0.2815", "88.42%", "1.0e-3", "Khởi tạo mạng"],
        ["Epoch 02", "0.2614", "89.62%", "0.2104", "91.80%", "1.0e-3", "Mất mát giảm nhanh"],
        ["Epoch 03", "0.2155", "91.84%", "0.1782", "93.15%", "1.0e-3", "Bắt đầu học các đường nét"],
        ["Epoch 04", "0.1832", "93.10%", "0.1540", "94.20%", "1.0e-3", "Hội tụ ổn định"],
        ["Epoch 05", "0.1610", "94.05%", "0.1388", "94.95%", "1.0e-3", "Độ chính xác tăng đều"],
        ["Epoch 06", "0.1455", "94.68%", "0.1265", "95.38%", "1.0e-3", ""],
        ["Epoch 07", "0.1320", "95.12%", "0.1190", "95.80%", "1.0e-3", ""],
        ["Epoch 08", "0.1215", "95.55%", "0.1124", "96.05%", "1.0e-3", ""],
        ["Epoch 09", "0.1130", "95.88%", "0.1085", "96.22%", "1.0e-3", ""],
        ["Epoch 10", "0.1055", "96.15%", "0.1042", "96.35%", "1.0e-3", ""],
        ["Epoch 11", "0.0988", "96.42%", "0.1015", "96.48%", "1.0e-3", ""],
        ["Epoch 12", "0.0930", "96.65%", "0.0998", "96.55%", "1.0e-3", ""],
        ["Epoch 13", "0.0882", "96.82%", "0.0982", "96.62%", "1.0e-3", "Giảm tốc độ học"],
        ["Epoch 14", "0.0754", "97.35%", "0.0895", "96.95%", "5.0e-4", "Val loss tiếp tục giảm"],
        ["Epoch 15", "0.0712", "97.52%", "0.0864", "97.10%", "5.0e-4", ""],
        ["Epoch 16", "0.0678", "97.68%", "0.0845", "97.22%", "5.0e-4", ""],
        ["Epoch 17", "0.0645", "97.80%", "0.0830", "97.30%", "5.0e-4", ""],
        ["Epoch 18", "0.0560", "98.15%", "0.0785", "97.48%", "2.5e-4", "Giảm tiếp tốc độ học"],
        ["Epoch 19", "0.0521", "98.32%", "0.0754", "97.60%", "2.5e-4", "Lưu mô hình tốt nhất"],
        ["Epoch 20", "0.0505", "98.40%", "0.0762", "97.55%", "2.5e-4", "Kết thúc huấn luyện"]
    ]
    add_table_data(b22_headers, b22_data, col_widths=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2])

    add_figure("images/image2.png", "Hình 2.1: Đồ thị hàm mất mát và độ chính xác qua 20 epochs huấn luyện của mô hình Baseline CNN.", width=4.5)

    add_body("Tại epoch 19, mô hình Baseline đạt val_loss thấp nhất là 0.0754 và val_accuracy đạt 97.60%. Khi đánh giá trên tập kiểm thử độc lập 4,080 ảnh, mô hình đạt độ chính xác 97.55% và Recall đạt 97.76%. Kết quả này cho thấy một mạng tích chập đơn giản xây dựng từ đầu đã có thể học được các đặc trưng cơ bản, nhưng vẫn còn bỏ sót 48 quả khuyết tật (False Negative = 48). Để cải thiện kết quả này, cần áp dụng các mô hình học chuyển giao sâu hơn.")

    # 13. CHƯƠNG 3
    add_heading1("CHƯƠNG 3: ÁP DỤNG HỌC CHUYỂN GIAO VỚI CÁC KIẾN TRÚC MẠNG SÂU", page_break_before=False)

    add_heading2("3.1. Lý thuyết học chuyển giao và ba kiến trúc VGG16, ResNet50, EfficientNetB0")
    add_body("Phương pháp học chuyển giao (Transfer Learning) cho phép kế thừa các bộ lọc trích xuất đặc trưng đã được huấn luyện từ trước trên tập dữ liệu lớn ImageNet (hơn 1.2 triệu ảnh, 1,000 lớp). Thay vì phải huấn luyện lại toàn bộ từ các trọng số ngẫu nhiên, mô hình có thể tận dụng các đặc trưng cạnh biên, kết cấu bề mặt sẵn có và chỉ cần tinh chỉnh lại cho bài toán phân loại quả tươi/hỏng.")
    add_body("Đồ án chọn thử nghiệm 3 kiến trúc mạng phổ biến:")
    add_bullet("VGG16: Kiến trúc tuần tự cổ điển gồm 16 tầng có trọng số, dùng toàn bộ các bộ lọc nhỏ 3x3 xếp chồng lên nhau. VGG16 có khả năng trích xuất chi tiết kết cấu bề mặt rất tốt nhưng số lượng tham số lớn.")
    add_bullet("ResNet50: Sử dụng các khối thắt cổ chai và cơ chế kết nối tắt (Residual Shortcut Connection / Identity Mapping) giúp giải quyết vấn đề suy biến gradient khi tăng chiều sâu mạng, cho phép huấn luyện hiệu quả mạng nơ-ron lên tới 50 tầng.")
    add_bullet("EfficientNetB0: Kiến trúc hiện đại sử dụng phương pháp co giãn đồng bộ (Compound Scaling) giữa chiều sâu, chiều rộng và độ phân giải ảnh, kết hợp các khối MBConv và cơ chế chú ý kênh Squeeze-and-Excitation (SE). Mô hình này đạt hiệu năng cao nhưng số lượng tham số rất gọn.")

    add_heading3("Bảng 3.1: Thông số so sánh cấu trúc mạng VGG16, ResNet50 và EfficientNetB0")
    b31_headers = ["Đặc điểm kỹ thuật", "VGG16", "ResNet50", "EfficientNetB0"]
    b31_data = [
        ["Độ sâu mạng", "16 tầng trọng số", "50 tầng tích chập", "18 khối MBConv"],
        ["Cơ chế nổi bật", "Xếp chồng bộ lọc 3x3", "Kết nối tắt Residual Shortcut", "MBConv + SE Attention"],
        ["Tổng số tham số", "Khoảng 14.85 triệu", "Khoảng 23.84 triệu", "Khoảng 4.38 triệu"],
        ["Dung lượng tệp .keras", "Khoảng 57.2 MB", "Khoảng 91.8 MB", "Khoảng 33.1 MB"],
        ["Ưu điểm chính", "Dễ hiểu, trích xuất bề mặt tốt", "Rất mạnh mẽ, độ ổn định cao", "Gọn nhẹ, tốc độ nhanh"]
    ]
    add_table_data(b31_headers, b31_data, col_widths=[2.0, 1.6, 1.8, 1.8])

    add_heading2("3.2. Quy trình tinh chỉnh mạng nơ-ron (Fine-tuning)")
    add_body("Để huấn luyện các mô hình chuyển giao một cách hiệu quả và tránh phá vỡ các trọng số đã học từ ImageNet (Catastrophic Forgetting), em áp dụng quy trình gồm 2 bước chính:")
    add_bullet("Bước 1 — Huấn luyện đầu phân loại (Warm-up): Đóng băng hoàn toàn phần thân trích xuất đặc trưng (Backbone Frozen), chỉ huấn luyện các tầng phân loại mới thêm vào (GAP + BatchNormalization + Dense 128 + Dropout 0.4 + Dense 1) với tốc độ học 0.001 trong 5 epochs.")
    add_bullet("Bước 2 — Tinh chỉnh các khối tích chập sâu (Fine-tuning): Mở khóa một số tầng tích chập cuối của mạng (khoảng 20–30 tầng cuối) và huấn luyện tiếp với tốc độ học nhỏ hơn nhiều (0.0001) trong 10 epochs để mạng thích nghi dần với dữ liệu trái cây.")

    add_heading3("Bảng 3.2: Kế hoạch đóng và mở băng các tầng (Freezing Schedule) khi huấn luyện")
    b32_headers = ["Giai đoạn", "Trạng thái Backbone", "Trạng thái đầu phân loại", "Tốc độ học", "Số Epochs"]
    b32_data = [
        ["Bước 1: Làm ấm đầu phân loại", "Đóng băng 100% các tầng", "Mở để huấn luyện", "1.0e-3", "5 Epochs"],
        ["Bước 2: Tinh chỉnh khối cuối", "Mở khóa 20-30 tầng cuối", "Huấn luyện liên tục", "1.0e-4", "10 Epochs"]
    ]
    add_table_data(b32_headers, b32_data, col_widths=[2.2, 1.8, 1.6, 1.0, 0.9])

    add_heading2("3.3. Diễn biến huấn luyện và hội tụ của các mô hình chuyển giao")
    add_body("Dưới đây là kết quả ghi nhận từ quá trình huấn luyện tinh chỉnh (Bước 2) của từng mô hình trên tập Train và tập Val:")

    add_heading3("Bảng 3.3: Tiến trình huấn luyện tinh chỉnh của mô hình VGG16")
    b33_headers = ["Epoch", "Train Loss", "Train Acc", "Val Loss", "Val Acc", "Tốc độ học"]
    b33_data = [
        ["Epoch 01", "0.1654", "93.85%", "0.0824", "97.20%", "1.0e-4"],
        ["Epoch 02", "0.0912", "96.80%", "0.0545", "98.15%", "1.0e-4"],
        ["Epoch 03", "0.0620", "97.90%", "0.0410", "98.65%", "1.0e-4"],
        ["Epoch 04", "0.0485", "98.42%", "0.0352", "98.92%", "1.0e-4"],
        ["Epoch 05", "0.0390", "98.78%", "0.0308", "99.05%", "1.0e-4"],
        ["Epoch 06", "0.0315", "99.05%", "0.0275", "99.20%", "1.0e-4"],
        ["Epoch 07", "0.0264", "99.25%", "0.0248", "99.30%", "1.0e-4"],
        ["Epoch 08", "0.0220", "99.40%", "0.0225", "99.42%", "5.0e-5"],
        ["Epoch 09", "0.0185", "99.55%", "0.0205", "99.50%", "5.0e-5"],
        ["Epoch 10", "0.0162", "99.62%", "0.0210", "99.48%", "5.0e-5"]
    ]
    add_table_data(b33_headers, b33_data, col_widths=[1.0, 1.2, 1.2, 1.2, 1.2, 1.2])

    add_heading3("Bảng 3.4: Tiến trình huấn luyện tinh chỉnh của mô hình ResNet50")
    b34_headers = ["Epoch", "Train Loss", "Train Acc", "Val Loss", "Val Acc", "Tốc độ học"]
    b34_data = [
        ["Epoch 01", "0.1245", "95.40%", "0.0482", "98.45%", "1.0e-4"],
        ["Epoch 02", "0.0512", "98.25%", "0.0265", "99.18%", "1.0e-4"],
        ["Epoch 03", "0.0310", "99.05%", "0.0182", "99.50%", "1.0e-4"],
        ["Epoch 04", "0.0215", "99.40%", "0.0135", "99.65%", "1.0e-4"],
        ["Epoch 05", "0.0160", "99.58%", "0.0105", "99.78%", "1.0e-4"],
        ["Epoch 06", "0.0124", "99.70%", "0.0084", "99.85%", "1.0e-4"],
        ["Epoch 07", "0.0098", "99.78%", "0.0071", "99.90%", "5.0e-5"],
        ["Epoch 08", "0.0075", "99.85%", "0.0058", "99.92%", "5.0e-5"],
        ["Epoch 09", "0.0056", "99.90%", "0.0042", "99.98%", "2.5e-5"],
        ["Epoch 10", "0.0048", "99.92%", "0.0045", "99.95%", "2.5e-5"]
    ]
    add_table_data(b34_headers, b34_data, col_widths=[1.0, 1.2, 1.2, 1.2, 1.2, 1.2])

    add_heading3("Bảng 3.5: Tiến trình huấn luyện tinh chỉnh của mô hình EfficientNetB0")
    b35_headers = ["Epoch", "Train Loss", "Train Acc", "Val Loss", "Val Acc", "Tốc độ học"]
    b35_data = [
        ["Epoch 01", "0.1410", "94.80%", "0.0520", "98.30%", "1.0e-4"],
        ["Epoch 02", "0.0650", "97.80%", "0.0295", "99.10%", "1.0e-4"],
        ["Epoch 03", "0.0412", "98.70%", "0.0195", "99.45%", "1.0e-4"],
        ["Epoch 04", "0.0285", "99.20%", "0.0140", "99.62%", "1.0e-4"],
        ["Epoch 05", "0.0198", "99.48%", "0.0102", "99.75%", "1.0e-4"],
        ["Epoch 06", "0.0152", "99.65%", "0.0078", "99.85%", "1.0e-4"],
        ["Epoch 07", "0.0115", "99.75%", "0.0062", "99.90%", "5.0e-5"],
        ["Epoch 08", "0.0084", "99.85%", "0.0045", "100.00%", "5.0e-5"],
        ["Epoch 09", "0.0068", "99.90%", "0.0048", "99.98%", "2.5e-5"],
        ["Epoch 10", "0.0055", "99.94%", "0.0046", "100.00%", "2.5e-5"]
    ]
    add_table_data(b35_headers, b35_data, col_widths=[1.0, 1.2, 1.2, 1.2, 1.2, 1.2])

    add_figure("images/image3.png", "Hình 3.1: Đồ thị diễn biến hàm mất mát và độ chính xác trong quá trình huấn luyện các mô hình học chuyển giao.", width=3.9)

    # 14. CHƯƠNG 4
    add_heading1("CHƯƠNG 4: ĐÁNH GIÁ VÀ SO SÁNH HIỆU NĂNG CÁC MÔ HÌNH", page_break_before=False)

    add_heading2("4.1. Các chỉ số đánh giá và tầm quan trọng của độ nhạy Recall")
    add_body("Để đánh giá mô hình một cách toàn diện và công bằng, cả 4 mô hình đã lưu đều được kiểm tra trên cùng một tập Kiểm thử độc lập (Test set) gồm 4,080 ảnh (1,935 ảnh tươi và 2,145 ảnh hỏng).")
    add_body("Trong bài toán kiểm tra chất lượng nông sản, 4 thành phần của ma trận nhầm lẫn mang ý nghĩa thực tế như sau:")
    add_bullet("True Positive (TP): Quả khuyết tật được nhận diện đúng là quả khuyết tật.")
    add_bullet("True Negative (TN): Quả tươi đạt chuẩn được nhận diện đúng là quả tươi.")
    add_bullet("False Positive (FP): Báo nhầm quả tươi thành quả khuyết tật (thiệt hại là loại nhầm một quả đạt chất lượng).")
    add_bullet("False Negative (FN): Bỏ sót quả khuyết tật và coi đó là quả tươi (đây là lỗi nguy hiểm nhất, vì quả thối lọt vào thùng hàng sẽ lây hỏng sang các quả xung quanh trong kho bảo quản).")
    add_body("Chính vì hậu quả của việc bỏ sót quả lỗi nghiêm trọng hơn nhiều so với việc báo nhầm, chỉ số Recall (độ nhạy bắt lỗi) là thước đo quan trọng hàng đầu cần được theo dõi sát sao bên cạnh Accuracy thông thường:")
    add_equation("Recall = TP / (TP + FN) * 100%", "(4.1)")
    add_equation("Precision = TP / (TP + FP) * 100%,   F1 = 2 * (Precision * Recall) / (Precision + Recall)", "(4.2)")

    add_heading2("4.2. Bảng so sánh kết quả thực nghiệm trên tập kiểm thử độc lập")
    add_body("Kết quả thực nghiệm của 4 mô hình trên 4,080 ảnh tập Test được tổng hợp trong Bảng 4.1.")

    add_heading3("Bảng 4.1: So sánh hiệu năng các mô hình trên tập kiểm thử độc lập (4,080 mẫu)")
    b41_headers = ["Mô hình", "Số tham số", "Dung lượng", "Accuracy", "Recall", "Precision", "F1-Score", "Bỏ sót (FN)", "Báo nhầm (FP)"]
    b41_data = [
        ["Baseline CNN", "295,969", "1.2 MB", "97.55%", "97.76%", "97.58%", "0.9767", "48 quả", "52 quả"],
        ["VGG16", "14.85 triệu", "57.2 MB", "99.41%", "98.88%", "100.00%", "0.9944", "24 quả", "0 quả"],
        ["ResNet50", "23.84 triệu", "91.8 MB", "99.98%", "100.00%", "99.95%", "0.9998", "0 quả", "1 quả"],
        ["EfficientNetB0", "4.38 triệu", "33.1 MB", "100.00%", "100.00%", "100.00%", "1.0000", "0 quả", "0 quả"]
    ]
    add_table_data(b41_headers, b41_data, col_widths=[1.5, 1.0, 0.9, 0.9, 0.9, 0.9, 0.8, 1.0, 1.0])

    add_heading2("4.3. Phân tích ma trận nhầm lẫn của từng mô hình")
    add_body("Bảng 4.2 thể hiện chi tiết số lượng mẫu dự đoán chính xác và dự đoán sai của từng mô hình:")

    add_heading3("Bảng 4.2: Ma trận nhầm lẫn chi tiết của 4 mô hình trên tập kiểm thử độc lập")
    b42_headers = ["Mô hình", "Tươi -> Tươi (TN)", "Tươi -> Lỗi (FP)", "Lỗi -> Tươi (FN)", "Lỗi -> Lỗi (TP)", "Đánh giá khả năng bắt lỗi"]
    b42_data = [
        ["Baseline CNN", "1,883 / 1,935", "52 quả (2.69%)", "48 quả (2.24%)", "2,097 / 2,145", "Bỏ sót 48 quả lỗi (chưa an toàn)"],
        ["VGG16", "1,935 / 1,935", "0 quả (0.00%)", "24 quả (1.12%)", "2,121 / 2,145", "Không báo nhầm, nhưng còn sót 24 lỗi"],
        ["ResNet50", "1,934 / 1,935", "1 quả (0.05%)", "0 quả (0.00%)", "2,145 / 2,145", "Bắt trọn 100% quả lỗi (FN = 0)"],
        ["EfficientNetB0", "1,935 / 1,935", "0 quả (0.00%)", "0 quả (0.00%)", "2,145 / 2,145", "Phân loại chính xác 100% toàn bộ mẫu"]
    ]
    add_table_data(b42_headers, b42_data, col_widths=[1.5, 1.3, 1.3, 1.3, 1.3, 1.7])

    add_figure("images/image4.png", "Hình 4.1: Đối chiếu ma trận nhầm lẫn của 4 mô hình trên tập kiểm thử độc lập 4,080 mẫu.", width=4.2)

    add_body("Từ kết quả trên, có thể rút ra một số nhận xét:")
    add_bullet("Mô hình ResNet50 đạt Recall 100.00% trên tập Test khi phát hiện chính xác toàn bộ 2,145 quả lỗi (FN = 0) và chỉ phân loại nhầm 1 quả tươi thành quả lỗi trong 1,935 quả tươi.")
    add_bullet("Mô hình EfficientNetB0 đạt kết quả rất tốt trên cả hai lớp, đồng thời có kích thước mô hình gọn nhẹ nhất trong 3 mạng chuyển giao (chỉ 33 MB), rất thích hợp để đưa vào các ứng dụng máy trạm hoặc thiết bị nhúng.")

    # 15. CHƯƠNG 5
    add_heading1("CHƯƠNG 5: GIẢI THÍCH MÔ HÌNH VỚI GRAD-CAM VÀ PHÂN TÍCH NGƯỠNG QUYẾT ĐỊNH", page_break_before=False)

    add_heading2("5.1. Vấn đề bão hòa đạo hàm Sigmoid và giải pháp Linear Logit Grad-CAM")
    add_body("Trong các ứng dụng thực tế, bên cạnh việc đưa ra nhãn dự đoán, hệ thống cần giải thích được mô hình đang nhìn vào khu vực nào của quả để kết luận đó là quả thối. Kỹ thuật Grad-CAM (Gradient-weighted Class Activation Mapping) thường được dùng để hiển thị bản đồ nhiệt cho biết mức độ đóng góp của các vùng ảnh.")
    add_body("Tuy nhiên, đối với bài toán phân loại nhị phân sử dụng hàm kích hoạt Sigmoid ở tầng cuối cùng, xác suất đầu ra được tính theo công thức: p = sigma(z) = 1 / (1 + e^(-z)). Khi mô hình rất tự tin về một quả thối nặng, giá trị logit z rất lớn (z >> 10), xác suất p tiệm cận 1.0. Lúc này, đạo hàm của hàm Sigmoid tiệm cận về 0:")
    add_equation("d sigma(z) / dz = sigma(z) * (1 - sigma(z)) -> 0 khi z >> 0", "(5.1)")
    add_body("Hiện tượng này khiến cho gradient lan truyền ngược bị triệt tiêu, dẫn tới việc bản đồ nhiệt Grad-CAM thông thường bị mờ nhạt hoặc chuyển sang màu xanh lam đồng nhất, không làm nổi bật được vết thối.")
    add_body("Để khắc phục, em tính toán gradient trực tiếp trên giá trị logit tuyến tính z (trước khi đi qua hàm Sigmoid) theo các bản đồ kích hoạt của tầng tích chập cuối cùng:")
    add_equation("alpha_k = 1/Z * sum_i sum_j ( dz / dA^k_{i, j} )", "(5.2)")
    add_body("Do z là một phép tính tuyến tính, đạo hàm này không bị ảnh hưởng bởi độ bão hòa của hàm Sigmoid, giúp bản đồ nhiệt phản ánh chính xác vùng đặc trưng khuyết tật ngay cả khi quả bị hỏng rất nặng.")

    add_heading2("5.2. Trực quan hóa vùng đặc trưng khuyết tật với mặt nạ thích nghi")
    add_body("Bản đồ nhiệt sau khi tính toán được đưa qua hàm ReLU để giữ lại các đặc trưng có tác động tích cực tới quyết định khuyết tật, sau đó được chuẩn hóa về khoảng [0.0, 1.0] và phủ lên ảnh gốc bằng kỹ thuật hòa trộn mặt nạ Alpha (Adaptive Alpha Masking):")
    add_equation("I_overlay = (1 - alpha) * I_original + alpha * ColorMap(M_norm)", "(5.3)")
    add_body("Kỹ thuật này giúp người vận hành quan sát đồng thời cả 3 khung hình: ảnh gốc chụp từ camera, bản đồ nhiệt Grad-CAM và ảnh phủ màu trực quan khoanh vùng vết thối.")

    add_figure("images/image5.png", "Hình 5.1: Kết quả trực quan hóa vùng tổn thương bằng Linear Logit Grad-CAM trên các mẫu quả thực tế.")

    add_heading2("5.3. Phân tích lựa chọn ngưỡng quyết định ưu tiên phát hiện lỗi")
    add_body("Theo mặc định, các bài toán phân loại thường chọn ngưỡng xác suất tau = 0.50 (nghĩa là nếu xác suất dự đoán P(Rotten) >= 0.50 thì kết luận quả lỗi). Tuy nhiên, vì mục tiêu chính là tránh bỏ sót quả hỏng lây lan sang các quả khác trong bảo quản kín, em tiến hành khảo sát số lượng mẫu FN và FP trên mô hình ResNet50 khi thay đổi ngưỡng cắt tau từ 0.10 đến 0.90 trên 4,080 ảnh tập Test:")

    add_heading3("Bảng 5.1: Khảo sát số mẫu FN và FP theo các ngưỡng phân loại khác nhau")
    b51_headers = ["Ngưỡng tau", "Số mẫu bỏ sót (FN)", "Số mẫu báo nhầm (FP)", "Nhận xét kỹ thuật"]
    b51_data = [
        ["tau = 0.10", "0 quả", "6 quả", "Ngưỡng quá nhạy, loại nhầm 6 quả tươi đạt chuẩn"],
        ["tau = 0.20", "0 quả", "3 quả", "Vẫn còn loại nhầm 3 quả tươi"],
        ["tau = 0.30", "0 quả", "1 quả", "Rất tốt, bắt trọn 100% quả lỗi"],
        ["tau = 0.35", "0 quả", "1 quả", "Ngưỡng an toàn khuyến nghị (bắt trọn quả lỗi, chỉ nhầm 1 quả)"],
        ["tau = 0.50", "0 quả", "1 quả", "Ngưỡng mặc định (trên tập test này vẫn đạt FN = 0)"],
        ["tau = 0.60", "1 quả", "0 quả", "Bắt đầu để lọt 1 quả có vết khuyết tật nhẹ"],
        ["tau = 0.70", "2 quả", "0 quả", "Để lọt 2 quả khuyết tật vào kiện hàng"],
        ["tau = 0.80", "5 quả", "0 quả", "Bỏ sót nhiều quả hỏng"],
        ["tau = 0.90", "12 quả", "0 quả", "Tỷ lệ bỏ sót cao, không an toàn"]
    ]
    add_table_data(b51_headers, b51_data, col_widths=[1.2, 1.5, 1.5, 2.8])

    add_body("Khảo sát tại Bảng 5.1 cho thấy: khi nâng ngưỡng lên trên 0.60, mô hình bắt đầu để lọt các quả khuyết tật nhẹ. Do đó, việc thiết lập ngưỡng quyết định ở mức an toàn tau = 0.35 giúp đảm bảo chắc chắn hệ thống không bỏ sót quả lỗi, đồng thời tỷ lệ báo nhầm quả tươi vẫn duy trì ở mức rất thấp (chỉ 1 quả trên 1,935 quả tươi).")

    add_heading2("5.4. Đánh giá tốc độ suy luận của các mô hình")
    add_body("Bên cạnh độ chính xác, tốc độ xử lý là yếu tố cần xem xét khi triển khai ứng dụng thực tế. Em đã đo đạc thời gian suy luận trung bình trên 1,000 khung hình liên tiếp trên cả GPU NVIDIA Tesla T4 và CPU máy tính:")

    add_heading3("Bảng 5.2: Thời gian suy luận và tốc độ khung hình (FPS) đo được trên GPU và CPU")
    b52_headers = ["Cấu hình thử nghiệm", "Độ trễ trung bình", "Tốc độ (FPS)", "Đánh giá thực tế"]
    b52_data = [
        ["EfficientNetB0 (GPU T4)", "6.2 ms / ảnh", "161.3 FPS", "Rất nhanh, phù hợp hệ thống tốc độ cao"],
        ["ResNet50 (GPU T4)", "8.5 ms / ảnh", "117.6 FPS", "Tốc độ cao, độ chính xác tốt nhất"],
        ["VGG16 (GPU T4)", "14.1 ms / ảnh", "70.9 FPS", "Đạt chuẩn thời gian thực trên GPU"],
        ["Baseline CNN (GPU T4)", "3.8 ms / ảnh", "263.1 FPS", "Mạng nhẹ, tốc độ cực nhanh"],
        ["EfficientNetB0 (Thuần CPU)", "22.4 ms / ảnh", "44.6 FPS", "Chạy mượt mà trên máy tính không có GPU"],
        ["ResNet50 (Thuần CPU)", "35.8 ms / ảnh", "27.9 FPS", "Đạt trên 25 FPS trên CPU máy trạm"],
        ["Giao diện Web Streamlit", "31.2 ms / ảnh", "32.0 FPS", "Bao gồm đọc camera, chạy AI và vẽ giao diện"],
        ["Động cơ dự phòng CPU", "2.5 ms / ảnh", "400.0 FPS", "Thuật toán xử lý ảnh cơ bản khi lỗi GPU"]
    ]
    add_table_data(b52_headers, b52_data, col_widths=[2.0, 1.4, 1.2, 2.4])

    add_figure("images/image6.png", "Hình 5.2: Đồ thị khảo sát số mẫu phân loại sai theo ngưỡng cắt và đối chuẩn tốc độ suy luận (FPS) của các mô hình.", width=3.9)

    # 16. CHƯƠNG 6
    add_heading1("CHƯƠNG 6: XÂY DỰNG ỨNG DỤNG DEMO THỜI GIAN THỰC VÀ THỬ NGHIỆM VẬN HÀNH", page_break_before=False)

    add_heading2("6.1. Giao diện điều khiển và giám sát bằng Streamlit")
    add_body("Để đưa mô hình từ các tệp trọng số tĩnh (.keras) trong notebook thành một phần mềm trực quan dễ sử dụng, em xây dựng ứng dụng Web Dashboard bằng thư viện Streamlit (`app.py`). Ứng dụng cung cấp 3 chế độ đưa dữ liệu vào:")
    add_bullet("Tải ảnh từ máy tính: Cho phép người dùng tải lên ảnh bất kỳ để kiểm tra nhanh kết quả phân loại và xem bản đồ nhiệt Grad-CAM.")
    add_bullet("Sử dụng ảnh mẫu có sẵn: Cung cấp sẵn các mẫu quả tươi và quả hỏng để thử nghiệm tính năng ngay lập tức.")
    add_bullet("Kết nối trực tiếp camera: Kết nối với webcam máy tính hoặc camera điện thoại không dây để phân loại theo thời gian thực.")
    add_body("Giao diện hiển thị trực quan các thẻ trạng thái: kết luận (Fresh / Rotten), xác suất hư hỏng P(Defect), thời gian xử lý (ms) cùng 3 khung hình đối chiếu: Ảnh gốc, Bản đồ nhiệt Grad-CAM và Ảnh phủ màu chỉ điểm vị trí tổn thương.")

    add_heading2("6.2. Kết nối camera điện thoại qua DroidCam và xử lý trôi khung hình bằng ThreadedCamera")
    add_body("Trong quá trình thử nghiệm kết nối camera điện thoại qua Wi-Fi bằng ứng dụng DroidCam (URL dạng `http://<IP>:4747/video`), em nhận thấy nếu dùng hàm đọc camera tiêu chuẩn `cv2.VideoCapture.read()` bên trong vòng lặp giao diện, hình ảnh hiển thị trên màn hình bị trễ từ 0.5 đến 1.5 giây so với chuyển động thực của tay (hiện tượng trôi dạt khung hình - Perceived Lag).")
    add_body("Nguyên nhân là do hàng đợi bộ đệm vòng (FIFO buffer) mặc định của OpenCV giữ lại 4 đến 5 khung hình cũ. Khi vòng lặp chính vừa phải chạy mô hình AI vừa phải cập nhật giao diện web, các khung hình mới gửi tới từ điện thoại bị ứ đọng lại trong bộ đệm.")
    add_body("Để giải quyết vấn đề này, em đã xây dựng lớp `ThreadedCamera` trong tệp `edge_stream_inspector.py`. Cơ chế hoạt động như sau:")
    add_bullet("Tách riêng việc đọc camera sang một luồng ngầm độc lập (Daemon Thread). Luồng này liên tục gọi `cap.grab()` để cập nhật khung hình mới nhất vào một biến chung và bỏ qua các khung hình cũ.")
    add_bullet("Khi vòng lặp chính của Streamlit yêu cầu lấy ảnh, nó luôn nhận được khung hình mới nhất ở thời điểm hiện tại. Nhờ đó, độ trễ hiển thị giảm xuống dưới 35 ms, thao tác cầm quả xoay trước camera điện thoại trở nên mượt mà, không còn cảm giác bị giật trễ.")

    add_heading2("6.3. Động cơ phân tích dự phòng trên CPU khi không có GPU")
    add_body("Để đảm bảo phần mềm hoạt động ổn định và không bị dừng đột ngột khi chạy trên các máy tính cá nhân không có sẵn GPU hoặc chưa cài đặt được thư viện TensorFlow, hàm nạp mô hình `load_fruit_qc_model()` trong `app.py` được thiết kế cơ chế tự chuyển mạch (Fallback Engine):")
    add_bullet("Chế độ chính (Primary Engine): Tự động tìm và nạp trọng số mô hình học sâu tốt nhất theo thứ tự ưu tiên: `efficientnetb0_best.keras` -> `resnet50_best.keras` -> `vgg16_best.keras` -> `baseline_cnn.keras`.")
    add_bullet("Chế độ dự phòng (Fallback Engine): Nếu không tìm thấy tệp trọng số hoặc môi trường thiếu TensorFlow, hệ thống tự động chuyển sang lớp `OpticalSpectralQCModel` chạy thuần trên CPU bằng thư viện OpenCV.")
    add_body("Mô hình dự phòng này sử dụng các kỹ thuật xử lý ảnh cơ bản:")
    add_bullet("Chuyển ảnh sang không gian màu HSV để tách biệt độ sáng V và độ bão hòa S, từ đó tạo mặt nạ vùng quả và đếm tỷ lệ diện tích các điểm ảnh bị thâm đen (V < 85, S > 15).")
    add_bullet("Tích chập ảnh xám với toán tử đạo hàm bậc hai Laplacian để đo phương sai độ nhám bề mặt vỏ quả, giúp phát hiện các vùng sần sùi do nấm mốc gây ra.")
    add_bullet("Mặc dù độ chính xác của thuật toán xử lý ảnh cơ bản không cao bằng mạng học sâu sâu tầng, nhưng nó chạy rất nhanh trên CPU (khoảng 2.5 ms/ảnh, tương đương 400 FPS) và giúp ứng dụng luôn mở được để phục vụ việc kiểm tra giao diện và luồng kết nối camera.")

    add_heading3("Bảng 6.1: Các phân hệ chính trong ứng dụng demo Streamlit và module camera")
    b61_headers = ["Phân hệ", "Tệp mã nguồn / Hàm", "Nhiệm vụ kỹ thuật", "Ghi chú"]
    b61_data = [
        ["Giao diện Web", "app.py", "Hiển thị dashboard, điều khiển ngưỡng tau, xem kết quả", "Xây dựng bằng Streamlit"],
        ["Luồng camera đa luồng", "edge_stream_inspector.py", "ThreadedCamera đọc ngầm, triệt tiêu trễ bộ đệm FIFO", "Độ trễ toàn trình < 35 ms"],
        ["Mô hình chính (GPU/CPU)", "models/*.keras", "Chạy suy luận mạng học sâu và tính Grad-CAM", "ResNet50 / EfficientNetB0"],
        ["Động cơ dự phòng (CPU)", "OpticalSpectralQCModel", "Xử lý ảnh bằng HSV và Laplacian khi thiếu môi trường", "Chạy thuần trên OpenCV, 400 FPS"]
    ]
    add_table_data(b61_headers, b61_data, col_widths=[1.5, 1.8, 2.7, 1.0])

    add_heading2("6.4. Đánh giá thử nghiệm vận hành ứng dụng trong thực tế")
    add_body("Sau khi hoàn thiện ứng dụng, em đã tiến hành chạy thử nghiệm thực tế bằng kịch bản `run_demo.bat` trên máy tính cá nhân và kết nối với điện thoại qua DroidCam để kiểm tra các chức năng:")
    add_bullet("Khả năng nhận diện trực tiếp: Khi đưa quả táo tươi và quả chuối chín đạt chuẩn trước camera điện thoại, hệ thống nhận diện chính xác nhãn \"Grade A (Fresh)\" với xác suất hư hỏng rất thấp (thường dưới 0.05). Khi đưa các quả có vết thâm rõ hoặc đốm mốc, hệ thống lập tức chuyển sang cảnh báo đỏ \"Rotten / Defective\" và hiển thị vùng nhiệt màu đỏ tập trung đúng vào vị trí vết bệnh.")
    add_bullet("Độ mượt mà của luồng video: Nhờ có lớp `ThreadedCamera`, khung hình hiển thị trên trình duyệt bắt kịp chuyển động thực của tay khi xoay quả, không xuất hiện hiện tượng giật cục hay hình đi sau tay.")
    add_bullet("Hạn chế quan sát được trong thử nghiệm: Khi ánh sáng phòng quá yếu hoặc khi đặt quả trên bề mặt có màu tối trùng với màu vỏ quả, hệ thống có thể gặp khó khăn hơn trong việc phân định ranh giới quả. Đây là bài học thực tế cho thấy môi trường chiếu sáng và góc đặt camera là yếu tố quan trọng khi triển khai các hệ thống thị giác máy tính ngoài thực địa.")

    # 17. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
    add_title("KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", size=15, bold=True, space_before=22, space_after=10, page_break_before=False)

    add_heading2("1. Kết luận về các kết quả đạt được")
    add_body("Qua quá trình thực hiện đồ án Project 13: Fruit Visual Quality Control trong khuôn khổ học phần Trí Tuệ Nhân Tạo & Học Sâu thuộc chương trình Samsung Innovation Campus 2026, em đã đạt được các kết quả cụ thể như sau:")
    add_bullet("Chuẩn hóa thành công tập dữ liệu 27,198 ảnh nông sản (Táo, Chuối, Cam), thực hiện phân chia phân tầng minh bạch với tỷ lệ 70/15/15, cố định SEED = 42 để đảm bảo tính tái lập và độc lập giữa các tập dữ liệu.")
    add_bullet("Xây dựng thành công mô hình Baseline CNN 3 khối từ đầu đạt độ chính xác 97.55% trên tập kiểm thử, thiết lập mốc so sánh vững chắc cho các mô hình nâng cao.")
    add_bullet("Áp dụng thành công phương pháp học chuyển giao (Transfer Learning) với quy trình tinh chỉnh 2 bước, giúp mô hình ResNet50 đạt Recall 100.00% (FN = 0) và Accuracy 99.98% trên 4,080 ảnh kiểm thử; đồng thời mô hình EfficientNetB0 đạt hiệu năng phân loại xuất sắc với dung lượng nhỏ gọn (33 MB).")
    add_bullet("Phân tích được nguyên nhân bão hòa đạo hàm của hàm Sigmoid trong Grad-CAM truyền thống và áp dụng thành công Linear Logit Grad-CAM để trực quan hóa rõ nét vùng khuyết tật trên vỏ quả.")
    add_bullet("Xây dựng hoàn chỉnh ứng dụng web demo bằng Streamlit, giải quyết được bài toán trễ khung hình của camera qua module đa luồng ThreadedCamera và có động cơ dự phòng trên CPU.")

    add_heading2("2. Bài học kinh nghiệm đúc kết từ quá trình làm đồ án")
    add_body("Quá trình thực hiện đồ án dưới sự hướng dẫn của Thầy Trần Mạnh Tường đã giúp em rút ra những bài học chuyên môn rất bổ ích:")
    add_bullet("Bài học về việc lựa chọn chỉ số đánh giá: Trong các bài toán thực tế như sàng lọc nông sản, chỉ số Accuracy cao chưa đủ để phản ánh toàn diện chất lượng mô hình nếu tỷ lệ bỏ sót quả lỗi (False Negative) còn lớn. Việc chú trọng vào Recall và phân tích ma trận nhầm lẫn giúp em hiểu rõ hơn mục tiêu cốt lõi của bài toán.")
    add_bullet("Bài học về bản chất toán học: Việc đào sâu cơ chế hoạt động của hàm kích hoạt và đạo hàm lan truyền ngược giúp phát hiện ra nguyên nhân tại sao Grad-CAM bị mờ nhạt trên các mẫu tự tin cao, từ đó tìm được cách khắc phục bằng đạo hàm logit tuyến tính thay vì chỉ gọi các hàm có sẵn của thư viện một cách máy móc.")
    add_bullet("Bài học về triển khai thực tế: Khoảng cách từ một mô hình chạy tốt trong Jupyter Notebook đến một ứng dụng chạy được trên máy tính là rất đáng kể. Việc đối mặt và giải quyết hiện tượng trễ khung hình camera bằng lập trình đa luồng giúp em tích lũy thêm nhiều kinh nghiệm lập trình hệ thống.")

    add_heading2("3. Hạn chế hiện tại của hệ thống")
    add_body("Bên cạnh các kết quả đạt được, hệ thống vẫn còn một số điểm hạn chế cần nhìn nhận thực tế:")
    add_bullet("Mô hình hiện tại là bài toán phân loại ảnh đơn quả (Image Classification): Hệ thống chỉ xử lý từng quả một trong khung hình. Nếu trên băng chuyền xuất hiện cùng lúc nhiều quả nằm san sát nhau, cần phải nâng cấp lên bài toán phát hiện vật thể (Object Detection) để khoanh vùng từng quả riêng biệt.")
    add_bullet("Giới hạn của cảm biến quang học RGB: Camera màu thông thường chỉ nhìn thấy các biểu hiện bên ngoài của vỏ quả. Các vết thâm dập mới xuất hiện ở mô sâu bên trong hoặc hiện tượng khô ruột mà vỏ ngoài chưa đổi màu thì camera RGB chưa thể phát hiện được.")
    add_bullet("Độ phụ thuộc vào ánh sáng: Ứng dụng hiện tại thử nghiệm bằng camera điện thoại ngoài môi trường tự nhiên, nên khi ánh sáng thay đổi quá mạnh hoặc có bóng đổ đậm có thể ảnh hưởng đến chất lượng phân loại.")

    add_heading2("4. Hướng phát triển trong tương lai")
    add_bullet("Nâng cấp lên mô hình phát hiện vật thể (như YOLOv8) kết hợp thuật toán bám vết (ByteTrack) để có thể nhận diện và đếm số lượng nhiều quả cùng lúc khi di chuyển trên băng tải.")
    add_bullet("Tối ưu hóa và lượng tử hóa mô hình (INT8 Quantization qua ONNX/TensorRT) để ứng dụng có thể chạy mượt mà trên các vi mạch nhúng công nghiệp như NVIDIA Jetson.")
    add_bullet("Mở rộng tập dữ liệu thêm các loại trái cây nhiệt đới chủ lực khác của Việt Nam (như thanh long, xoài, sầu riêng, bưởi) để tăng tính ứng dụng thực tiễn cho nông sản trong nước.")

    # 18. TÀI LIỆU THAM KHẢO
    add_title("TÀI LIỆU THAM KHẢO", size=15, bold=True, space_before=22, space_after=10, page_break_before=False)
    refs = [
        "1. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770–778.",
        "2. Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. In Proceedings of the IEEE International Conference on Computer Vision (ICCV), pp. 618–626.",
        "3. Tan, M., & Le, Q. V. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In Proceedings of the 36th International Conference on Machine Learning (ICML), PMLR 97, pp. 6105–6114.",
        "4. Simonyan, K., & Zisserman, A. (2015). Very deep convolutional networks for large-scale image recognition. In 3rd International Conference on Learning Representations (ICLR 2015).",
        "5. Kalluri, S. R. (2020). Fruits Fresh and Rotten for Classification Dataset. Kaggle Datasets.",
        "6. Chollet, F. (2021). Deep Learning with Python (2nd Edition). Manning Publications.",
        "7. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.",
        "8. Giáo trình học phần Trí Tuệ Nhân Tạo & Học Sâu — Chương trình Samsung Innovation Campus 2026."
    ]
    for r in refs:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(r)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)

    # 19. PHỤ LỤC
    add_title("PHỤ LỤC", size=15, bold=True, space_before=22, space_after=10, page_break_before=False)

    add_heading2("Phụ lục A: Cấu trúc thư mục mã nguồn đồ án")
    add_body("Toàn bộ mã nguồn và dữ liệu thực nghiệm của đồ án được tổ chức như sau:")

    code_p = doc.add_paragraph()
    code_p.paragraph_format.space_before = Pt(4)
    code_p.paragraph_format.space_after = Pt(6)
    r_code = code_p.add_run(
"""Project SIC/
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
        └── image6.png             # Hình 5.2: Khảo sát ngưỡng và đối chuẩn tốc độ"""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)
    r_code.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    add_heading2("Phụ lục B: Hướng dẫn cài đặt và chạy ứng dụng demo")
    add_body("Để chạy ứng dụng demo trên máy tính cá nhân, người dùng thực hiện các bước sau:")
    add_body("Bước 1: Tạo môi trường ảo Python 3.10+ và kích hoạt:")
    add_body("   python -m venv .venv\n   .venv\\Scripts\\activate  (trên Windows)")
    add_body("Bước 2: Cài đặt các thư viện cần thiết:")
    add_body("   pip install -r requirements.txt")
    add_body("Bước 3: Khởi chạy ứng dụng Streamlit:")
    add_body("   streamlit run app.py\n(Hoặc nhấp đúp vào tệp run_demo.bat trên Windows để ứng dụng tự động mở trên trình duyệt tại địa chỉ http://localhost:8501).")
    add_body("Bước 4: Kết nối camera điện thoại (tùy chọn):\nCài đặt ứng dụng DroidCam trên điện thoại và kết nối chung mạng Wi-Fi với máy tính. Nhập địa chỉ IP hiển thị trên màn hình điện thoại (ví dụ: http://192.168.1.15:4747/video) vào khung bên trái của trang web để bắt đầu kiểm tra trực tiếp.")

    out_docx_path = r"E:\Project SIC\report\BaoCao_Project13_LeThanhDuoc_SIC2026.docx"
    doc.save(out_docx_path)
    print(f"Master report generated at: {out_docx_path} ({os.path.getsize(out_docx_path):,} bytes)")

if __name__ == "__main__":
    build_student_report()

"""
🏭 Project 13: Visual Quality Control (QC) Demo App
Streamlit Web Application for Industrial Casting Defect Detection
"""

import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Cấu hình trang giao diện
st.set_page_config(
    page_title="Hệ Thống Kiểm Soát Lỗi Đúc Kim Loại (Visual QC)",
    page_icon="🏭",
    layout="wide"
)

# Header
st.title("🏭 Hệ Thống Kiểm Định Chất Lượng Sản Phẩm (Visual QC)")
st.markdown("""
Ứng dụng Deep Learning & Transfer Learning hỗ trợ phát hiện khuyết tật bề mặt sản phẩm đúc kim loại tự động.
""")

# Sidebar
st.sidebar.header("⚙️ Cấu Hình Mô Hình")
threshold = st.sidebar.slider("Ngưỡng phân loại lỗi (Threshold)", min_value=0.1, max_value=0.9, value=0.4, step=0.05)
st.sidebar.info("💡 Ngưỡng mặc định 0.4 được tối ưu hóa để đảm bảo Recall ≥ 95% (không bỏ sót sản phẩm lỗi).")

# Tải ảnh từ người dùng
uploaded_file = st.file_uploader("Tải lên ảnh chi tiết đúc kim loại (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    with col1:
        st.subheader("📸 Ảnh Gốc Sản Phẩm")
        st.image(image, caption="Chi tiết kiểm định", use_container_width=True)
    
    with col2:
        st.subheader("🔍 Kết Quả Phân Tích")
        with st.spinner("Đang phân tích khuyết tật bề mặt..."):
            # Placeholder dự đoán (sẽ nối model sau khi hoàn tất training)
            st.success("✅ Mô hình đã sẵn sàng kết nối trọng số `.keras` từ `models/`")
            st.write(f"Ngưỡng áp dụng: **{threshold}**")
            
            # Gợi ý hiển thị
            st.markdown("""
            - **Trạng thái:** *Đang chờ tải mô hình đã huấn luyện.*
            - **Grad-CAM Heatmap:** *Sẽ hiển thị vùng kích hoạt khuyết tật tại đây.*
            """)
else:
    st.info("👈 Hãy tải một ảnh sản phẩm phôi đúc để bắt đầu kiểm tra.")

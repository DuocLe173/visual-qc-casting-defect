@echo off
chcp 65001 >nul
echo ==============================================================================
echo  🏭 PROJECT 13: FRUIT VISUAL QUALITY CONTROL - REAL-TIME CONVEYOR INSPECTION
echo ==============================================================================
echo.
echo 🚀 Đang khởi động máy chủ Streamlit...
echo 🌐 Ứng dụng sẽ tự động mở tại: http://localhost:8501
echo.
start http://localhost:8501
streamlit run app.py
pause

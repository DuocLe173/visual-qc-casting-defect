"""
📥 Tự Động Tải Dataset Nông Sản Xuất Khẩu (Fruits Fresh & Rotten)
Nguồn: Kaggle (sriramr/fruits-fresh-and-rotten-for-classification)
Quy mô: 13,599 ảnh RGB (Apple, Banana, Orange)
"""

import os
import sys
import subprocess
import shutil

DATASET_SLUG = "sriramr/fruits-fresh-and-rotten-for-classification"
TARGET_DIR = "data"

def download_dataset():
    print("=" * 70)
    print(f"🍎 BẮT ĐẦU TẢI DỮ LIỆU NÔNG SẢN: {DATASET_SLUG}")
    print("=" * 70)
    
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # Kiểm tra lệnh kaggle
    try:
        cmd = ["kaggle", "datasets", "download", "-d", DATASET_SLUG, "--unzip", "-p", TARGET_DIR]
        print(f"Đang thực thi: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print("✅ Tải và giải nén thành công!")
        print(result.stdout)
    except FileNotFoundError:
        print("⚠️ Không tìm thấy công cụ Kaggle CLI trên máy của bạn.")
        print("💡 Hướng dẫn cài đặt:")
        print("   1. Chạy: pip install kaggle")
        print("   2. Tải API token 'kaggle.json' từ tài khoản Kaggle của bạn.")
        print("   3. Đặt vào thư mục: ~/.kaggle/kaggle.json (Linux/Mac) hoặc %USERPROFILE%\\.kaggle\\kaggle.json (Windows)")
        print("\nHoặc tải trực tiếp bằng trình duyệt tại link:")
        print(f"   https://www.kaggle.com/datasets/{DATASET_SLUG}")
    except subprocess.CalledProcessError as e:
        print("❌ Lỗi trong quá trình tải:")
        print(e.stderr)

if __name__ == "__main__":
    download_dataset()

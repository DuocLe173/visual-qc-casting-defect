"""
📥 TRÌNH TẢI DỮ LIỆU NÔNG SẢN ĐA NGUỒN (FRUIT VISUAL QC - 3 NGUỒN DOANH NGHIỆP)
Hỗ trợ tải và giải nén cả 3 bộ dữ liệu chuẩn công nghiệp từ Kaggle:
  1. Nguồn chính (Primary): sriramr/fruits-fresh-and-rotten-for-classification (~13,599 ảnh)
  2. Nguồn dự phòng 1:     raghavrbi/fruit-freshness-dataset (~10,000 ảnh)
  3. Nguồn dự phòng 2:     khandakerdipro/fruit-quality-classification (~8,000 ảnh)

Cách sử dụng:
  - Tải tất cả 3 bộ:   python download_fruit_data.py --all
  - Tải nguồn cụ thể:  python download_fruit_data.py 1  (hoặc 2, 3)
  - Chạy tương tác:     python download_fruit_data.py
"""

import os
import sys
import subprocess
import argparse

DATASETS = {
    1: {
        "name": "Nguồn 1 (Chính thức) — Fruits Fresh and Rotten",
        "slug": "sriramr/fruits-fresh-and-rotten-for-classification",
        "target_dir": "data",
        "size": "~13,599 ảnh RGB",
        "classes": "freshapples, rottenapples, freshbanana, rottenbanana, freshoranges, rottenoranges",
        "desc": "Bộ dữ liệu chuẩn mực nhất thế giới cho bài toán phân loại độ tươi nông sản."
    },
    2: {
        "name": "Nguồn 2 (Dự phòng 1) — Fruit Freshness Dataset",
        "slug": "raghavrbi/fruit-freshness-dataset",
        "target_dir": "data_backup1",
        "size": "~10,000 ảnh",
        "classes": "Fresh & Rotten (Apple, Banana, Orange, Tomato)",
        "desc": "Dữ liệu đa dạng góc chụp và ánh sáng thực tế tại nông trường và chợ đầu mối."
    },
    3: {
        "name": "Nguồn 3 (Dự phòng 2) — Fruit Quality Classification",
        "slug": "khandakerdipro/fruit-quality-classification",
        "target_dir": "data_backup2",
        "size": "~8,000 ảnh",
        "classes": "Good Fruit vs Bad Fruit (Đốm thâm, dập vỏ, nấm mốc hoại tử)",
        "desc": "Tập trung phân loại sâu các mức độ thương tổn mô tế bào và nấm bệnh."
    }
}

def download_single(idx):
    ds = DATASETS[idx]
    print("\n" + "=" * 75)
    print(f"📦 [{idx}/3] {ds['name'].upper()}")
    print(f"🔗 Kaggle Slug: {ds['slug']}")
    print(f"📁 Thư mục lưu: {ds['target_dir']}/")
    print(f"📊 Quy mô:      {ds['size']}")
    print(f"🍎 Các lớp:     {ds['classes']}")
    print("=" * 75)
    
    os.makedirs(ds['target_dir'], exist_ok=True)
    
    cmd = ["kaggle", "datasets", "download", "-d", ds['slug'], "--unzip", "-p", ds['target_dir']]
    print(f"🚀 Đang tải và tự động giải nén...")
    
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(f"✅ Hoàn tất tải {ds['name']} vào thư mục '{ds['target_dir']}'!")
        if result.stdout.strip():
            print(result.stdout.strip())
        return True
    except FileNotFoundError:
        print("⚠️ Chưa tìm thấy công cụ Kaggle CLI trên máy tính của bạn.")
        print("💡 Hướng dẫn nhanh:")
        print("   1. Cài đặt: pip install kaggle")
        print("   2. Lấy file token 'kaggle.json' từ tài khoản Kaggle của bạn.")
        print("   3. Đặt vào thư mục: %USERPROFILE%\\.kaggle\\kaggle.json (Windows)")
        print(f"\n🌐 Link tải thủ công bằng trình duyệt web:")
        print(f"   https://www.kaggle.com/datasets/{ds['slug']}")
        return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi khi tải bộ dữ liệu {ds['slug']}:")
        print(e.stderr.strip() if e.stderr else e)
        print(f"👉 Bạn có thể tải thủ công tại: https://www.kaggle.com/datasets/{ds['slug']}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Tải dữ liệu nông sản Fruit Visual QC từ Kaggle.")
    parser.add_argument("choice", nargs="?", default=None, help="Chọn nguồn (1, 2, 3) hoặc 'all' để tải tất cả.")
    parser.add_argument("--all", action="store_true", help="Tải đồng loạt cả 3 bộ dữ liệu.")
    args = parser.parse_args()

    print("🍎 HỆ THỐNG QUẢN LÝ DỮ LIỆU NÔNG SẢN — PROJECT 13 (FRUIT VISUAL QC)")
    print("Danh sách 3 bộ dữ liệu chuẩn doanh nghiệp:")
    for k, v in DATASETS.items():
        print(f"  [{k}] {v['name']} ({v['size']}) -> {v['target_dir']}/")
    print("  [4] Tải CẢ 3 BỘ DỮ LIỆU CÙNG LÚC")

    choice = None
    if args.all or (args.choice and str(args.choice).lower() in ["all", "4"]):
        choice = "all"
    elif args.choice and args.choice in ["1", "2", "3"]:
        choice = int(args.choice)
    else:
        # Chế độ tương tác nếu chạy thẳng
        try:
            user_input = input("\n👉 Nhập lựa chọn của bạn (1, 2, 3 hoặc 'all'/4 để tải cả 3): ").strip().lower()
            if user_input in ["all", "4", "a"]:
                choice = "all"
            elif user_input in ["1", "2", "3"]:
                choice = int(user_input)
            else:
                print("Mặc định: Tải CẢ 3 BỘ DỮ LIỆU.")
                choice = "all"
        except (EOFError, KeyboardInterrupt):
            print("\nMặc định tải cả 3 bộ dữ liệu...")
            choice = "all"

    if choice == "all":
        print("\n🚀 BẮT ĐẦU TẢI ĐỒNG LOẠT CẢ 3 BỘ DỮ LIỆU NÔNG SẢN...")
        for i in [1, 2, 3]:
            download_single(i)
    else:
        download_single(choice)

    print("\n🏁 QUÁ TRÌNH TẢI DỮ LIỆU ĐÃ KẾT THÚC!")

if __name__ == "__main__":
    main()

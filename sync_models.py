"""
Fruit QC Model & Results Synchronizer (sync_models.py)
------------------------------------------------------
Tự động tìm kiếm file 'fruit_qc_artifacts.zip' tải về từ Google Colab,
giải nén an toàn vào thư mục models/ và results/, đồng thời kiểm tra tính toàn vẹn.
"""

import os
import sys
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"

# Đảm bảo in tiếng Việt có dấu và emoji an toàn trên Windows Console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Các vị trí tìm kiếm file nén tải về từ Colab
CANDIDATE_ZIP_PATHS = [
    PROJECT_ROOT / "fruit_qc_artifacts.zip",
    Path.home() / "Downloads" / "fruit_qc_artifacts.zip",
    PROJECT_ROOT / "fruit_qc_colab_artifacts.zip",
    Path.home() / "Downloads" / "fruit_qc_colab_artifacts.zip",
    PROJECT_ROOT / "artifacts.zip",
    Path.home() / "Downloads" / "artifacts.zip",
]

def format_size(num_bytes: int) -> str:
    """Định dạng byte sang KB / MB thân thiện"""
    if num_bytes < 1024:
        return f"{num_bytes} B"
    elif num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    else:
        return f"{num_bytes / (1024 * 1024):.1f} MB"

def find_colab_zip() -> Path:
    for p in CANDIDATE_ZIP_PATHS:
        if p.exists() and p.is_file():
            return p
    return None

def sync_artifacts(zip_path: Path):
    print("=" * 70)
    print("🚀 BỘ ĐỒNG BỘ HÓA MODEL & KẾT QUẢ TỰ ĐỘNG TỪ GOOGLE COLAB")
    print("=" * 70)
    print(f"📦 Đã phát hiện gói nén: {zip_path}")
    print(f"📏 Dung lượng: {format_size(zip_path.stat().st_size)}")
    print(f"🕒 Thời gian tạo: {datetime.fromtimestamp(zip_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 70)

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    extracted_files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # Chỉ cho phép giải nén vào models/ hoặc results/ để đảm bảo an toàn
            if member.startswith("models/") or member.startswith("results/"):
                zip_ref.extract(member, PROJECT_ROOT)
                extracted_files.append(member)
            elif not member.endswith("/"):
                # Nếu file nén lưu trực tiếp không có thư mục cha
                if member.endswith(".keras"):
                    target = MODELS_DIR / os.path.basename(member)
                    with zip_ref.open(member) as source, open(target, "wb") as dest:
                        shutil.copyfileobj(source, dest)
                    extracted_files.append(f"models/{os.path.basename(member)}")
                elif member.endswith(".csv") or member.endswith(".png"):
                    target = RESULTS_DIR / os.path.basename(member)
                    with zip_ref.open(member) as source, open(target, "wb") as dest:
                        shutil.copyfileobj(source, dest)
                    extracted_files.append(f"results/{os.path.basename(member)}")

    print(f"✅ Đã giải nén thành công {len(extracted_files)} tệp vào dự án:")
    for f in sorted(extracted_files):
        p = PROJECT_ROOT / f
        sz = format_size(p.stat().st_size) if p.exists() else "N/A"
        print(f"   ├── 📄 {f} ({sz})")

    print("-" * 70)
    print("🎯 KIỂM TRA TÍNH TOÀN VẸN TRỌNG SỐ MÔ HÌNH:")
    expected_models = [
        "resnet50_best.keras",
        "efficientnetb0_best.keras",
        "vgg16_best.keras"
    ]
    all_ok = True
    for m in expected_models:
        mp = MODELS_DIR / m
        if mp.exists() and mp.stat().st_size > 1024 * 1024:
            print(f"   [OK] {m:<30} -> {format_size(mp.stat().st_size):>10} (Đầy đủ trọng số)")
        else:
            print(f"   [CẢNH BÁO] {m:<30} -> Chưa tìm thấy hoặc file rỗng!")
            all_ok = False

    print("=" * 70)
    if all_ok:
        print("🎉 ĐỒNG BỘ HÓA THÀNH CÔNG 100%! Web App đã sẵn sàng phân tích bằng Deep Learning.")
        print("💡 Ứng dụng Streamlit (http://localhost:8501) sẽ tự động nạp mô hình mới nhất.")
    else:
        print("⚠️ Vui lòng kiểm tra lại các file nén trong Colab.")
    print("=" * 70)

if __name__ == "__main__":
    found_zip = find_colab_zip()
    if not found_zip:
        print("=" * 70)
        print("❌ KHÔNG TÌM THẤY TỆP NÉN 'fruit_qc_artifacts.zip'")
        print("=" * 70)
        print("👉 Hướng dẫn:")
        print("1. Chạy ô code đóng gói trên Google Colab để tải file 'fruit_qc_artifacts.zip' về máy.")
        print(f"2. Đảm bảo file được tải về thư mục 'Downloads' hoặc copy vào: {PROJECT_ROOT}")
        print("3. Sau đó chạy lại: py sync_models.py")
        print("=" * 70)
        sys.exit(1)
    else:
        sync_artifacts(found_zip)

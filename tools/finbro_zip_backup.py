import os
import zipfile
from datetime import datetime

LOG_DIR = "C:/FINBRO/logs"
REPORT_DIR = "C:/FINBRO/reports"
BACKUP_DIR = "C:/FINBRO/backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
zip_path = os.path.join(BACKUP_DIR, f"finbro_backup_{today}.zip")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for folder in [LOG_DIR, REPORT_DIR]:
        for root, _, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, "C:/FINBRO")
                zipf.write(full_path, arcname)

print(f"✅ Backup created at: {zip_path}")

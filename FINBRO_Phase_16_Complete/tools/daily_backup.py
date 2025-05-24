import os
from zipfile import ZipFile
from datetime import datetime

def create_daily_backup():
    backup_name = f"backup_FINBRO_{datetime.now().strftime('%Y-%m-%d_%H%M')}.zip"
    backup_path = os.path.join("backups", backup_name)

    os.makedirs("backups", exist_ok=True)
    folders_to_backup = ["logs", "reports", "signals"]

    with ZipFile(backup_path, "w") as zipf:
        for folder in folders_to_backup:
            if os.path.exists(folder):
                for root, _, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_path = os.path.relpath(file_path, ".")
                        zipf.write(file_path, arcname=arc_path)

    print(f"📦 Backup created at {backup_path}")

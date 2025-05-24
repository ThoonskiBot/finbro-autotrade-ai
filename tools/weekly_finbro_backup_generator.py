
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import zipfile
from datetime import datetime
from core.config import LOG_PATH, REPORTS_PATH, SIGNALS_PATH

def create_weekly_backup():
    print("💾 Creating FINBRO Weekly Backup Zip...")

    now = datetime.now()
    backup_name = f"FINBRO_WeeklyBackup_{now.strftime('%Y-%m-%d')}.zip"
    backup_path = os.path.join(REPORTS_PATH, backup_name)

    with zipfile.ZipFile(backup_path, "w") as zipf:
        for base_folder in [LOG_PATH, REPORTS_PATH, SIGNALS_PATH]:
            for root, _, files in os.walk(base_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=os.path.dirname(base_folder))
                    zipf.write(file_path, arcname=arcname)

    print(f"✅ Weekly backup saved to: {backup_path}")

create_weekly_backup()

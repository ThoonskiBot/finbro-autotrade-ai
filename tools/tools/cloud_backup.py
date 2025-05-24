# tools/cloud_backup.py

import shutil
from datetime import datetime
from pathlib import Path

def backup_logs_to_local_cloud(log_dir="logs", cloud_dir="cloud_backup"):
    src = Path(log_dir)
    dst = Path(cloud_dir) / datetime.now().strftime("%Y-%m-%d")
    dst.mkdir(parents=True, exist_ok=True)
    for file in src.glob("log_*.txt"):
        shutil.copy(file, dst)
    return str(dst)
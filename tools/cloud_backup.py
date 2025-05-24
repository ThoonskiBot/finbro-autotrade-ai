
import shutil
import os
from datetime import datetime

def backup_to_folder(source_dir, backup_dir="D:/FINBRO_CloudBackup"):
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    dest = os.path.join(backup_dir, f"backup_{ts}")
    shutil.copytree(source_dir, dest)
    print(f"✅ Backed up FINBRO data to: {dest}")

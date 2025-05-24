# Script: auto_file_cleaner.py
# Deletes files older than 30 days from reports/, logs/, backups/

import os, time
from pathlib import Path

def clean_old_files(base_dirs, days_old=30):
    cutoff = time.time() - days_old * 86400
    for base in base_dirs:
        for root, _, files in os.walk(base):
            for f in files:
                path = Path(root) / f
                if path.stat().st_mtime < cutoff:
                    try:
                        path.unlink()
                        print(f"🗑️ Deleted: {path}")
                    except Exception as e:
                        print(f"⚠️ Failed to delete {path}: {e}")

if __name__ == "__main__":
    clean_old_files(["reports", "logs", "backups"])
import os
import time
from datetime import datetime, timedelta

def cleanup_old_files(folder, days=30, extensions=None):
    if not os.path.exists(folder):
        return

    now = time.time()
    cutoff = now - days * 86400  # days in seconds

    for root, _, files in os.walk(folder):
        for f in files:
            if extensions and not any(f.lower().endswith(ext) for ext in extensions):
                continue
            full_path = os.path.join(root, f)
            if os.path.getmtime(full_path) < cutoff:
                print(f"🧹 Removing old file: {full_path}")
                os.remove(full_path)

def run_cleanup():
    print("🧼 Starting FINBRO file cleanup...")
    folders = ["logs", "reports", "signals", "backups"]
    extensions = [".txt", ".pdf", ".csv", ".zip"]
    for folder in folders:
        cleanup_old_files(folder, days=30, extensions=extensions)
    print("✅ Cleanup complete.")

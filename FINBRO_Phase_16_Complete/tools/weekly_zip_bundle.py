import os
from zipfile import ZipFile
from datetime import datetime, timedelta

def create_weekly_zip():
    week = datetime.now().strftime("%Y-%m-%d")
    bundle_name = f"weekly_bundle_{week}.zip"
    os.makedirs("backups", exist_ok=True)
    bundle_path = os.path.join("backups", bundle_name)

    folders = ["logs", "reports", "signals"]

    with ZipFile(bundle_path, "w") as zipf:
        for folder in folders:
            if os.path.exists(folder):
                for root, _, files in os.walk(folder):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, ".")
                        zipf.write(full_path, arcname=arcname)

    print(f"📦 Weekly bundle created at {bundle_path}")

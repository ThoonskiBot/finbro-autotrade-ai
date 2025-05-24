# Script: weekly_zip_bundler.py
# Bundles weekly reports and logs into a timestamped ZIP

import zipfile
from pathlib import Path
import datetime

def bundle_weekly():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    out_zip = Path("backups") / f"weekly_bundle_{date}.zip"
    with zipfile.ZipFile(out_zip, "w") as z:
        for folder in ["reports", "logs"]:
            for path in Path(folder).rglob("*.*"):
                z.write(path, arcname=path.relative_to("."))
    print(f"📦 Created: {out_zip}")

if __name__ == "__main__":
    bundle_weekly()
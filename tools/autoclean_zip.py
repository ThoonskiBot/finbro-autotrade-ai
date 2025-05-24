import os, zipfile, datetime
logs_dir, reports_dir, bundle_dir = "C:\\FINBRO\\logs", "C:\\FINBRO\\reports", "C:\\FINBRO\\bundles"
os.makedirs(bundle_dir, exist_ok=True)
cutoff = datetime.datetime.now() - datetime.timedelta(days=30)
for folder in [logs_dir, reports_dir]:
    if os.path.exists(folder):
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path) and datetime.datetime.fromtimestamp(os.path.getmtime(path)) < cutoff:
                os.remove(path)
today = datetime.datetime.now().strftime("%Y-%W")
zip_name = os.path.join(bundle_dir, f"weekly_bundle_{today}.zip")
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for folder in [logs_dir, reports_dir]:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                path = os.path.join(folder, file)
                zipf.write(path, arcname=os.path.join(os.path.basename(folder), file))
with open(os.path.join(logs_dir, "autoclean_log.txt"), "a") as log:
    log.write(f"{datetime.datetime.now()}: Cleaned & zipped to {zip_name}\n")
os.startfile(bundle_dir)
print(f"✅ Cleaned and zipped to {zip_name}")

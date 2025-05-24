import os
import shutil
from datetime import datetime

BASE_DIR = r"C:\FINBRO"
LOG_FILE = os.path.join(BASE_DIR, "organize_log.txt")

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def date_folder():
    return datetime.now().strftime("%Y-%m-%d")

def log_action(original, renamed):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp()}] {original} ➜ {renamed}\n")

def auto_rename_and_move_files():
    print(f"\n📁 Base Directory: {BASE_DIR}")

    source_folder = input("👉 Enter the source subfolder (e.g. 'signals'): ").strip()
    dest_folder = input("📦 Enter the destination root (e.g. 'archive'): ").strip()

    source_path = os.path.join(BASE_DIR, source_folder)
    dated_subfolder = os.path.join(BASE_DIR, dest_folder, date_folder())

    os.makedirs(dated_subfolder, exist_ok=True)

    if not os.path.exists(source_path):
        print(f"❌ Source folder not found: {source_path}")
        return

    files = os.listdir(source_path)
    if not files:
        print("⚠️ No files found in the source folder.")
        return

    print(f"\n🔄 Renaming & moving {len(files)} files...")

    for filename in files:
        if filename == "__init__.py":
            print(f"⏭️ Skipped: {filename}")
            continue

        src_file = os.path.join(source_path, filename)
        if os.path.isfile(src_file):
            name, ext = os.path.splitext(filename)
            new_name = f"{name}_{timestamp()}{ext}"
            dest_file = os.path.join(dated_subfolder, new_name)

            shutil.move(src_file, dest_file)
            log_action(filename, os.path.relpath(dest_file, BASE_DIR))
            print(f"✅ Moved: {filename} ➜ {new_name}")

    print(f"\n📓 Log written to: {LOG_FILE}")
    print("🎉 Done! All files renamed, moved, and logged.\n")

if __name__ == "__main__":
    auto_rename_and_move_files()

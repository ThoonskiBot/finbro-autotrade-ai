
# tools/log_sender.py

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
LOG_DIR = os.getenv("LOG_PATH", "logs")

def get_latest_log_file():
    log_files = sorted(Path(LOG_DIR).glob("log_*.txt"))
    return log_files[-1] if log_files else None

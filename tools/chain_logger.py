import os
from datetime import datetime

log_file = "C:/FINBRO/chain_log.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_line = f"[{timestamp}] ✅ FINBRO 6PM Chain ran successfully.\n"

with open(log_file, "a", encoding="utf-8") as f:
    f.write(log_line)

print(log_line.strip())

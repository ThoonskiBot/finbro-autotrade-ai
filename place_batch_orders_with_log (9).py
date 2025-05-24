import sys, os, glob
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from core.config import *

# Find the latest signal file
signal_files = glob.glob("signals/*.csv")
if not signal_files:
    raise FileNotFoundError("No signal files found in 'signals/'")

SIGNAL_FILE = max(signal_files, key=os.path.getctime)
print(f"📊 Loaded signals from: {SIGNAL_FILE}")

os.makedirs(LOG_PATH, exist_ok=True)
df = pd.read_csv(SIGNAL_FILE)

for _, row in df.iterrows():
    print(f"📝 Logged Order: {row['Ticker']} | {row['Signal']} | accepted")

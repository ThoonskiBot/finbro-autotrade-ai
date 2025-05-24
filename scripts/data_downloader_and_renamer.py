import os
import sys
import pandas as pd
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.utils import fetch_signals_from_api

SAVE_DIR = os.path.join(os.getcwd(), 'signals')
os.makedirs(SAVE_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"signals_{timestamp}.csv"
filepath = os.path.join(SAVE_DIR, filename)

df = fetch_signals_from_api()
df.to_csv(filepath, index=False)

print(f"[✅] Signals saved to: {filepath}")

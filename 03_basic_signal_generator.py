
# Phase 3: Basic Signal Generator (Final header fix with correct row parsing)

import pandas as pd
import os
import io
from datetime import datetime

DATA_DIR = "data"
SIGNALS_DIR = "signals"
os.makedirs(SIGNALS_DIR, exist_ok=True)

def generate_signals(file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        # Line 0 is the real header
        header_line = lines[0].strip()
        headers = header_line.split(",")

        # Line 3 onward = actual data
        data_lines = lines[3:]

        corrected_csv = [",".join(headers)] + data_lines
        csv_text = "\n".join(corrected_csv)

        df = pd.read_csv(io.StringIO(csv_text))

        # Rename and parse date column
        if "Price" in df.columns:
            df.rename(columns={"Price": "Date"}, inplace=True)
        else:
            print(f"[❌] Actual columns found: {df.columns.tolist()}")
            return

        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.dropna(subset=["Date"], inplace=True)
        df.set_index("Date", inplace=True)

        if "Close" not in df.columns:
            print(f"[❌] 'Close' column not found. Columns are: {df.columns.tolist()}")
            return

        df["SMA_10"] = df["Close"].rolling(window=10).mean()
        df["SMA_50"] = df["Close"].rolling(window=50).mean()

        df["Signal"] = 0
        df.loc[df["SMA_10"] > df["SMA_50"], "Signal"] = 1
        df.loc[df["SMA_10"] < df["SMA_50"], "Signal"] = -1

        output_file = os.path.join(SIGNALS_DIR, f"signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        df.to_csv(output_file)
        print(f"[✅] Signals saved to {output_file}")

    except Exception as e:
        print(f"[❌] Error generating signals: {e}")

if __name__ == "__main__":
    try:
        files = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
        if not files:
            print("[⚠️] No data files found in /data")
        else:
            latest_file = max(files, key=os.path.getctime)
            generate_signals(latest_file)
    except Exception as e:
        print(f"[❌] Error loading files: {e}")

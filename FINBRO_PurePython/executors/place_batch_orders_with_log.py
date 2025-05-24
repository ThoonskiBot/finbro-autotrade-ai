import os, glob
import pandas as pd
import core.config as cfg

def place_orders():
    signal_files = glob.glob("signals/*.csv")
    if not signal_files:
        raise FileNotFoundError("No signal files found.")
    latest = max(signal_files, key=os.path.getctime)

    print(f"📊 Loaded signals from: {latest}")
    df = pd.read_csv(latest)
    for _, row in df.iterrows():
        print(f"📝 Logged Order: {row['Ticker']} | {row['Signal']} | accepted")

if __name__ == "__main__":
    place_orders()

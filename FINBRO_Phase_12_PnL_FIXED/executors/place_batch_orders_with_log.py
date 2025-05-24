import os, glob
import pandas as pd
from datetime import datetime
import core.config as cfg
import random

def simulate_price(ticker):
    # Mock price simulator
    return round(random.uniform(100, 500), 2)

def place_orders():
    signal_files = glob.glob("signals/*.csv")
    if not signal_files:
        raise FileNotFoundError("No signal files found.")
    latest = max(signal_files, key=os.path.getctime)

    print(f"📊 Loaded signals from: {latest}")
    df = pd.read_csv(latest)
    os.makedirs("ledger", exist_ok=True)

    ledger_entries = []

    for _, row in df.iterrows():
        ticker = row['Ticker']
        signal = row['Signal']
        price = simulate_price(ticker)
        executed = cfg.LIVE_MODE
        action = f"{ticker} | {signal} | {'executed' if executed else 'simulated'} @ ${price}"
        print(f"📝 Logged Order: {action}")
        ledger_entries.append({
            "Time": datetime.now().isoformat(),
            "Ticker": ticker,
            "Signal": signal,
            "Price": price,
            "Executed": executed
        })

    ledger_df = pd.DataFrame(ledger_entries)
    if os.path.exists(cfg.TRADE_LEDGER_PATH):
        ledger_df.to_csv(cfg.TRADE_LEDGER_PATH, mode='a', header=False, index=False)
    else:
        ledger_df.to_csv(cfg.TRADE_LEDGER_PATH, index=False)

if __name__ == "__main__":
    place_orders()


# Phase 4: Alpaca Paper Trade Executor

import pandas as pd
import os
from datetime import datetime
import alpaca_trade_api as tradeapi

# Alpaca Paper credentials
ALPACA_API_KEY = os.getenv("APCA_API_KEY_ID", "YOUR_API_KEY_HERE")
ALPACA_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY", "YOUR_SECRET_KEY_HERE")
ALPACA_ENDPOINT = os.getenv("APCA_API_BASE_URL", "https://paper-api.alpaca.markets")

# Connect to Alpaca API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_ENDPOINT)

SIGNALS_DIR = "signals"
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

def execute_trades(signal_file):
    df = pd.read_csv(signal_file, index_col=0, parse_dates=True)
    df = df.dropna(subset=["Signal"])

    symbol = "SPY"  # Hardcoded for now; can be parameterized later

    for index, row in df.iterrows():
        signal = row["Signal"]
        if signal == 1:
            print(f"[📈] BUY signal on {index.date()}")
            api.submit_order(
                symbol=symbol,
                qty=1,
                side="buy",
                type="market",
                time_in_force="gtc"
            )
        elif signal == -1:
            print(f"[📉] SELL signal on {index.date()}")
            api.submit_order(
                symbol=symbol,
                qty=1,
                side="sell",
                type="market",
                time_in_force="gtc"
            )

    log_file = os.path.join(LOGS_DIR, f"executed_trades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    with open(log_file, "w") as f:
        f.write(f"Executed trades for: {symbol}\n")
        f.write(f"Source signal file: {signal_file}\n")
        for index, row in df.iterrows():
            if row["Signal"] == 1:
                f.write(f"BUY on {index.date()}\n")
            elif row["Signal"] == -1:
                f.write(f"SELL on {index.date()}\n")

    print(f"[✅] Trades logged to {log_file}")

if __name__ == "__main__":
    try:
        files = [os.path.join(SIGNALS_DIR, f) for f in os.listdir(SIGNALS_DIR) if f.endswith(".csv")]
        if not files:
            print("[⚠️] No signal files found in /signals")
        else:
            latest_file = max(files, key=os.path.getctime)
            print(f"[🔄] Executing trades from: {latest_file}")
            execute_trades(latest_file)
    except Exception as e:
        print(f"[❌] Error executing trades: {e}")

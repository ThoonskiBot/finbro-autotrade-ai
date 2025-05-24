import os, glob
import pandas as pd
from datetime import datetime
import core.config as cfg
from executors.price_feed_yahoo_lite import get_price

def load_positions():
    if os.path.exists(cfg.POSITIONS_FILE):
        return pd.read_csv(cfg.POSITIONS_FILE, index_col="Ticker").to_dict(orient="index")
    return {}

def save_positions(positions):
    df = pd.DataFrame.from_dict(positions, orient="index")
    df.index.name = "Ticker"
    df.to_csv(cfg.POSITIONS_FILE)

def place_orders():
    signal_files = glob.glob("signals/*.csv")
    if not signal_files:
        raise FileNotFoundError("No signal files found.")
    latest = max(signal_files, key=os.path.getctime)

    print(f"📊 Loaded signals from: {latest}")
    df = pd.read_csv(latest)
    os.makedirs("ledger", exist_ok=True)

    positions = load_positions()
    ledger_entries = []

    for _, row in df.iterrows():
        ticker = row["Ticker"]
        signal = row["Signal"]
        price = get_price(ticker) or 0.0
        executed = cfg.LIVE_MODE

        if signal == "buy":
            positions[ticker] = {"Signal": "buy", "Price": price, "Timestamp": datetime.now().isoformat()}
            action = f"{ticker} | buy | {'executed' if executed else 'simulated'} @ ${price}"
        elif signal == "sell":
            if ticker in positions and positions[ticker]["Signal"] == "buy":
                buy_price = positions[ticker]["Price"]
                pnl = round(price - buy_price, 2)
                action = f"{ticker} | sell | {'executed' if executed else 'simulated'} @ ${price} | PnL = ${pnl}"
                del positions[ticker]
            else:
                action = f"{ticker} | sell | skipped (no open position)"
        else:
            action = f"{ticker} | unknown signal"

        print(f"📝 {action}")
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

    save_positions(positions)

if __name__ == "__main__":
    place_orders()

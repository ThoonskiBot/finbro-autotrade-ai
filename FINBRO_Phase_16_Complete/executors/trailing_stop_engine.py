import os
import pandas as pd
import core.config as cfg
from executors.price_feed_yahoo_lite import get_price
from datetime import datetime

def check_trailing_stop_losses(trail_pct=5):
    if not os.path.exists(cfg.POSITIONS_FILE):
        print("🟢 No open positions to check trailing stops.")
        return

    df = pd.read_csv(cfg.POSITIONS_FILE)
    if df.empty:
        print("🟢 Position file is empty.")
        return

    exits = []
    for _, row in df.iterrows():
        ticker = row["Ticker"]
        entry_price = float(row["Price"])
        current_price = get_price(ticker)
        if current_price == 0.0:
            continue

        trailing_trigger = entry_price * (1 + trail_pct / 100)
        if current_price >= trailing_trigger:
            print(f"📉 Trailing Stop Triggered: {ticker} has risen and now qualifies for trailing exit at ${current_price}")
            exits.append({
                "Time": datetime.now().isoformat(),
                "Ticker": ticker,
                "Signal": "trailing-stop",
                "Price": current_price,
                "Executed": cfg.LIVE_MODE
            })

    if exits:
        log_df = pd.DataFrame(exits)
        if os.path.exists(cfg.TRADE_LEDGER_PATH):
            log_df.to_csv(cfg.TRADE_LEDGER_PATH, mode="a", header=False, index=False)
        else:
            log_df.to_csv(cfg.TRADE_LEDGER_PATH, index=False)
        print(f"📉 {len(exits)} trailing stop(s) logged.")
    else:
        print("✅ No trailing stop exits triggered.")

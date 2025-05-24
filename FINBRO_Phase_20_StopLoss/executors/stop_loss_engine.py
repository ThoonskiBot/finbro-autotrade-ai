import pandas as pd
import core.config as cfg
from executors.price_feed_yahoo_lite import get_price
from datetime import datetime

def check_stop_losses(threshold_pct=5):
    if not os.path.exists(cfg.POSITIONS_FILE):
        print("🟢 No open positions to check stop-losses on.")
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

        loss_pct = ((entry_price - current_price) / entry_price) * 100
        if loss_pct >= threshold_pct:
            print(f"❌ Stop-loss triggered on {ticker}: Entry ${entry_price} → Now ${current_price} (-{loss_pct:.2f}%)")
            exits.append({
                "Time": datetime.now().isoformat(),
                "Ticker": ticker,
                "Signal": "stop-loss",
                "Price": current_price,
                "Executed": cfg.LIVE_MODE
            })

    if exits:
        log_df = pd.DataFrame(exits)
        if os.path.exists(cfg.TRADE_LEDGER_PATH):
            log_df.to_csv(cfg.TRADE_LEDGER_PATH, mode="a", header=False, index=False)
        else:
            log_df.to_csv(cfg.TRADE_LEDGER_PATH, index=False)

        print(f"📉 {len(exits)} stop-loss trade(s) logged.")
    else:
        print("✅ No stop-loss exits triggered.")


import os
import pandas as pd
from core.config import LOG_PATH, SIGNALS_PATH
from datetime import datetime

def run_trading_logic():
    signal_file = os.path.join(SIGNALS_PATH, 'test_signal.csv')
    signals = pd.read_csv(signal_file)
    print(f"📊 Loaded signals from: {signal_file}")

    log_lines = []
    for _, row in signals.iterrows():
        action = row.get("Action", "HOLD")
        ticker = row.get("Ticker", "UNKNOWN")
        strategy = row.get("Strategy", "Unknown")
        log_line = f"[{datetime.now().strftime('%Y-%m-%d')}] {ticker} | {action.upper()} | Strategy: {strategy}"
        print(log_line)
        log_lines.append(log_line)

    os.makedirs(LOG_PATH, exist_ok=True)
    log_file = os.path.join(LOG_PATH, f"order_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(log_file, "w", encoding="utf-8") as f:
        for line in log_lines:
            f.write(line + "\n")
    print(f"✅ Orders logged to: {log_file}")


import os
import pandas as pd
from datetime import datetime
from core.config import LOG_PATH

df = pd.read_csv(LOG_PATH)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
today = datetime.now().strftime('%Y-%m-%d')
df_today = df[df['Timestamp'].dt.strftime('%Y-%m-%d') == today]

if df_today.empty:
    print("⚠️ No trades today.")
else:
    total = len(df_today)
    avg_entry = df_today['EntryPrice'].mean()
    avg_tp = df_today['TakeProfit'].mean()
    avg_sl = df_today['StopLoss'].mean()
    rr_ratio = round((avg_tp - avg_entry) / (avg_entry - avg_sl), 2) if avg_entry != avg_sl else "N/A"

    print(f"📊 Trade Summary for {today}")
    print(f"Trades: {total}")
    print(f"Avg Entry: ${avg_entry:.2f} | TP: ${avg_tp:.2f} | SL: ${avg_sl:.2f} | R:R Ratio: {rr_ratio}")

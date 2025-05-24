
# Phase 2: Historical Data Collector
import yfinance as yf
import os
from datetime import datetime

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

def fetch_and_save_data(ticker="SPY", period="1y", interval="1d"):
    print(f"[📥] Fetching data for {ticker} ({period}, {interval})...")
    data = yf.download(ticker, period=period, interval=interval)

    if data.empty:
        print("[❌] No data found.")
        return

    filename = f"data/{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    data.to_csv(filename)
    print(f"[✅] Data saved to {filename}")

if __name__ == "__main__":
    fetch_and_save_data()

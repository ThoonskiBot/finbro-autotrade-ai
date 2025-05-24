import os
import time
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

symbol = "AAPL"
url = f"https://data.alpaca.markets/v2/stocks/{symbol}/bars"
params = {
    "timeframe": "1Hour",
    "start": "2024-05-01T00:00:00Z",
    "end": "2024-05-20T00:00:00Z",
    "limit": 1000
}

print(f"📡 Fetching {symbol} 1H bars from Alpaca...")
response = requests.get(url, headers=HEADERS, params=params)
if response.status_code != 200:
    print("❌ Failed to fetch data:", response.status_code, response.text)
    exit()

bars = response.json().get("bars", [])
if not bars:
    print("⚠️ No bars returned.")
    exit()

df = pd.DataFrame(bars)
df.rename(columns={"t": "Timestamp", "o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"}, inplace=True)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df.to_csv("C:/FINBRO/data/AAPL_1h.csv", index=False)
print("✅ Saved to C:/FINBRO/data/AAPL_1h.csv")

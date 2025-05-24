import yfinance as yf
import time

price_cache = {}

def get_price(ticker):
    now = time.time()
    if ticker in price_cache:
        price, timestamp = price_cache[ticker]
        if now - timestamp < 30:
            return price

    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        latest_price = info.get("regularMarketPrice", 0.0)
        if latest_price:
            price_cache[ticker] = (latest_price, now)
            return float(latest_price)
        else:
            print(f"⚠️ No valid price data in info for {ticker}")
    except Exception as e:
        print(f"❌ Failed to fetch price for {ticker}: {e}")

    return 0.0

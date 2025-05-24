import yfinance as yf
import time

price_cache = {}

def get_price(ticker):
    # Use cached price if available (for 30 seconds)
    now = time.time()
    if ticker in price_cache:
        price, timestamp = price_cache[ticker]
        if now - timestamp < 30:
            return price

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d", interval="1m")
        if not hist.empty:
            latest_price = hist['Close'].iloc[-1]
            price_cache[ticker] = (latest_price, now)
            return float(latest_price)
        else:
            print(f"⚠️ No recent data for {ticker}")
    except Exception as e:
        print(f"❌ Failed to fetch price for {ticker}: {e}")

    return 0.0  # Safe fallback

import pandas as pd

df = pd.read_csv('data/AAPL_1h.csv')
df['RSI'] = df['Close'].rolling(14).mean()
df['MA20'] = df['Close'].rolling(20).mean()
df['MA50'] = df['Close'].rolling(50).mean()
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
df.dropna().to_csv('data/AAPL_features.csv', index=False)
print("✅ Features generated and saved to AAPL_features.csv")

import os
import pandas as pd
from datetime import datetime

os.makedirs("signals", exist_ok=True)
now = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"signals/signals_{now}.csv"

# Dummy DataFrame for demo
df = pd.DataFrame({
    'Ticker': ['AAPL', 'MSFT'],
    'Signal': ['buy', 'sell']
})
df.to_csv(filename, index=False)
print(f"[✅] Signals saved to: {filename}")

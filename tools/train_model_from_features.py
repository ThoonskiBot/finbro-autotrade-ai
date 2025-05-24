import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('data/AAPL_features.csv')
X = df[['RSI', 'MA20', 'MA50']]
y = df['Target']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
joblib.dump(model, 'models/aapl_model.pkl')
print("✅ Model trained and saved to models/aapl_model.pkl")

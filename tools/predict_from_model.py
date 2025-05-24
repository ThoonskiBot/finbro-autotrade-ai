import pandas as pd
import joblib

df = pd.read_csv('data/AAPL_features.csv')
model = joblib.load('models/aapl_model.pkl')

X = df[['RSI', 'MA20', 'MA50']]
df['Prediction'] = model.predict(X)
df[['Close', 'Prediction']].to_csv('data/AAPL_predictions.csv', index=False)
print("✅ Predictions saved to AAPL_predictions.csv")

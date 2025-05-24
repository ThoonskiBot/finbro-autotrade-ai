# tools/ml_lightgbm_trainer.py

import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

print("🚀 Training LightGBM Model...")

# Load your preprocessed data (you'll want to update this path)
DATA_PATH = 'signals/signals_cleaned.csv'
MODEL_PATH = 'models/lightgbm_trade_model.joblib'

# Ensure the data file exists
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ Data file not found at: {DATA_PATH}")

# Load and preview data
df = pd.read_csv(DATA_PATH)
print(f"📊 Loaded dataset with shape: {df.shape}")

# Drop any rows with missing target or features
df = df.dropna(subset=['target'])

# Define features and target
X = df.drop(columns=['target'])
y = df['target']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LightGBM classifier
model = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy:.4f}")

# Save the model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"💾 Model saved to: {MODEL_PATH}")

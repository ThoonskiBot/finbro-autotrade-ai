# tools/ml_xgboost_exit_trainer.py

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

print("🚀 Training XGBoost Exit Optimizer...")

# Load your labeled exit signal data
DATA_PATH = 'signals/exit_signals_labeled.csv'
MODEL_PATH = 'models/xgboost_exit_model.joblib'

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ Exit signals file not found: {DATA_PATH}")

# Load and prepare the data
df = pd.read_csv(DATA_PATH)
print(f"📊 Loaded dataset with shape: {df.shape}")

df = df.dropna(subset=['exit_label'])  # ensure labeled
X = df.drop(columns=['exit_label'])
y = df['exit_label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42, use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Exit model accuracy: {accuracy:.4f}")

# Save model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"💾 Model saved to: {MODEL_PATH}")

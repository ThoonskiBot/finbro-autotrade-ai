# -*- coding: utf-8 -*-
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load features and labels
X = pd.read_csv("data/features.csv")
y = pd.read_csv("data/labels.csv").values.ravel()

print(f"📊 Features loaded: {X.shape}")
print(f"🏷 Labels loaded: {y.shape}")

# Auto-check for stratify safety
unique_counts = pd.Series(y).value_counts()
if all(unique_counts >= 2):
    stratify_option = y
    print("✅ Using stratify=y")
else:
    stratify_option = None
    print("⚠️ Not enough samples to stratify — skipping it")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, stratify=stratify_option, random_state=42
)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained with accuracy: {accuracy:.2%}")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/trained_model.pkl")
print("💾 Model saved to: models/trained_model.pkl")

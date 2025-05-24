import os
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score

data = pd.read_csv('data/training_data.csv')
X = data.drop('label', axis=1)
y = data['label']

best_model = None
best_acc = 0
model_folder = 'models/'

for file in os.listdir(model_folder):
    if file.endswith('.pkl'):
        with open(os.path.join(model_folder, file), 'rb') as f:
            model = pickle.load(f)
        acc = accuracy_score(y, model.predict(X))
        if acc > best_acc:
            best_model = model
            best_acc = acc
            best_file = file

with open(os.path.join(model_folder, 'live_model.pkl'), 'wb') as f:
    pickle.dump(best_model, f)

print(f"🧠 Best model selected: {best_file} with accuracy {best_acc:.2f}")
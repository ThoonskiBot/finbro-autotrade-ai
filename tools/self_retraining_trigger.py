import os
os.system("py tools\ml_feature_generator.py")
os.system("py tools\train_model_sl.py")
os.system("py tools\model_live_swapper.py")
print("✅ Self-retraining executed based on log trigger.")
@echo off
py tools\ml_feature_generator.py
py tools\train_model_sl.py
py tools\evaluate_model_results.py
py tools\model_live_swapper.py
py tools\gpu_train_launcher.py
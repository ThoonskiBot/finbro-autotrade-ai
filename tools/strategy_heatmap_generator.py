import os
LOG_DIR = 'D:/FINBRO_CLEAN_BASE/logs'
files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith('order_log') and f.endswith('.txt')])
print(f'✅ strategy_heatmap_generator.py done — {len(files)} log(s) loaded')

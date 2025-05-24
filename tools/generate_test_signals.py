from datetime import datetime
import os
path = 'C:/FINBRO/signals'
os.makedirs(path, exist_ok=True)
now = datetime.now().strftime('%Y%m%d')
with open(f'{path}/signals_{now}.csv', 'w') as f:
    f.write('ticker,signal\\nAAPL,buy\\nMSFT,sell\\nTSLA,buy')
print('✅ Test signals generated.')


import os
from core.config import REPORTS_PATH

def get_latest_pnl_chart():
    chart_file = "live_pnl_chart_latest.png"
    chart_path = f"/static/{chart_file}"
    return f'<h3>📉 PnL Chart</h3><img src="{chart_path}" width="600">'

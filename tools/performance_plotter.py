
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from tools.pnl_data_parser import parse_logs_for_strategy_pnl

def generate_strategy_chart():
    pnl_data = parse_logs_for_strategy_pnl()
    if not pnl_data:
        return None

    strategies = list(pnl_data.keys())
    profits = list(pnl_data.values())

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(strategies, profits, color='skyblue')
    ax.set_title("📈 PnL by Strategy")
    ax.set_ylabel("Simulated Profit")
    ax.set_xlabel("Strategy")
    ax.grid(axis='y')
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return f'data:image/png;base64,{base64.b64encode(buf.read()).decode("utf-8")}'

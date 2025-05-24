import pandas as pd

def log_order(order, response):
    print(f"📝 Logged Order: {order['symbol']} | {order['side']} | {response.status}")

def read_logs(log_path):
    try:
        with open(log_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "No logs found."

def create_pdf_report(log_data, output_dir):
    from fpdf import FPDF
    import os
    from datetime import datetime

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in log_data.splitlines():
        pdf.cell(200, 10, txt=line, ln=True)

    filename = f"daily_trade_digest_{datetime.now().strftime('%Y%m%d')}.pdf"
    filepath = os.path.join(output_dir, filename)
    pdf.output(filepath)
    return filepath

def fetch_signals_from_api():
    # Dummy signals
    data = {
        'Ticker': ['AAPL', 'MSFT', 'GOOGL'],
        'Signal': ['BUY', 'SELL', 'HOLD']
    }
    return pd.DataFrame(data)

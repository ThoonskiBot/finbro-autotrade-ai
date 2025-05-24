
import os
import pandas as pd
from fpdf import FPDF
from datetime import datetime
from core.config import LOG_PATH, PDF_OUTPUT_DIR

df = pd.read_csv(LOG_PATH)
today = datetime.now().strftime('%Y-%m-%d')
df_today = df[df['Timestamp'].str.startswith(today)]

if df_today.empty:
    print("⚠️ No trades found today.")
else:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"FINBRO Trade Digest - {today}", ln=True, align='C')
    pdf.ln(10)
    for _, row in df_today.iterrows():
        line = f"{row['Ticker']} | Entry: ${row['EntryPrice']} | TP: ${row['TakeProfit']} | SL: ${row['StopLoss']} | ID: {row['OrderID']}"
        pdf.cell(200, 10, txt=line, ln=True)
    output_path = os.path.join(PDF_OUTPUT_DIR, f"trade_digest_{today}.pdf")
    pdf.output(output_path)
    print(f"✅ Digest saved to {output_path}")

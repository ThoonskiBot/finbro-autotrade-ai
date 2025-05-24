from flask import Flask, render_template_string
import pandas as pd
import os

app = Flask(__name__)

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>FINBRO Dashboard</title>
  <style>
    body { font-family: Arial; margin: 20px; }
    h1 { color: #007acc; }
    table, th, td { border: 1px solid #ccc; border-collapse: collapse; padding: 8px; }
    th { background-color: #f2f2f2; }
  </style>
</head>
<body>
  <h1>📊 FINBRO Portfolio PnL Tracker</h1>
  {% if positions %}
    <h2>Open Positions</h2>
    <table>
      <tr><th>Ticker</th><th>Entry Price</th><th>Current Price</th><th>Unrealized PnL</th></tr>
      {% for p in positions %}
        <tr>
          <td>{{ p['Ticker'] }}</td>
          <td>${{ p['Entry'] }}</td>
          <td>${{ p['Current'] }}</td>
          <td style="color: {% if p['PnL'] >= 0 %}green{% else %}red{% endif %}">${{ p['PnL'] }}</td>
        </tr>
      {% endfor %}
    </table>
  {% else %}
    <p>No open positions.</p>
  {% endif %}

  <h2>Recent Trades</h2>
  {% if trades %}
    <table>
      <tr><th>Time</th><th>Ticker</th><th>Signal</th><th>Price</th><th>Executed</th></tr>
      {% for t in trades %}
        <tr>
          <td>{{ t['Time'] }}</td>
          <td>{{ t['Ticker'] }}</td>
          <td>{{ t['Signal'] }}</td>
          <td>${{ t['Price'] }}</td>
          <td>{{ t['Executed'] }}</td>
        </tr>
      {% endfor %}
    </table>
  {% else %}
    <p>No recent trades logged.</p>
  {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    positions = []
    trades = []

    try:
        if os.path.exists("ledger/positions.csv"):
            pos_df = pd.read_csv("ledger/positions.csv")
            for _, row in pos_df.iterrows():
                ticker = row["Ticker"]
                entry_price = float(row["Price"])
                # Mock price for now
                current_price = entry_price * 1.03  # simulate +3%
                pnl = round(current_price - entry_price, 2)
                positions.append({
                    "Ticker": ticker,
                    "Entry": round(entry_price, 2),
                    "Current": round(current_price, 2),
                    "PnL": pnl
                })

        if os.path.exists("ledger/trade_log.csv"):
            trade_df = pd.read_csv("ledger/trade_log.csv")
            trades = trade_df.tail(10).to_dict(orient="records")

    except Exception as e:
        return f"<p>Error loading dashboard: {e}</p>"

    return render_template_string(TEMPLATE, positions=positions, trades=trades)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template_string
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import os
from datetime import datetime
import random

app = Flask(__name__)

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>FINBRO Live Dashboard</title>
  <meta http-equiv="refresh" content="30">
  <style>
    body { font-family: Arial; margin: 20px; }
    h1 { color: #007acc; }
    table, th, td { border: 1px solid #ccc; border-collapse: collapse; padding: 8px; }
    th { background-color: #f2f2f2; }
  </style>
</head>
<body>
  <h1>📊 FINBRO Live Portfolio Tracker</h1>
  {% if positions %}
    <h2>Open Positions (Live)</h2>
    <table>
      <tr><th>Ticker</th><th>Entry Price</th><th>Live Price</th><th>Unrealized PnL</th></tr>
      {% for p in positions %}
        <tr>
          <td>{{ p['Ticker'] }}</td>
          <td>${{ p['Entry'] }}</td>
          <td>${{ p['Live'] }}</td>
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

  <h2>📈 PnL Overview</h2>
  {{ chart_html | safe }}

</body>
</html>
"""

def generate_pnl_chart():
    if not os.path.exists("ledger/trade_log.csv"):
        return "<p>No trade log for chart.</p>"

    df = pd.read_csv("ledger/trade_log.csv")
    if df.empty or "Ticker" not in df or "Price" not in df:
        return "<p>Insufficient trade data for chart.</p>"

    df['Time'] = pd.to_datetime(df['Time'])
    pnl_data = []

    for ticker in df['Ticker'].unique():
        symbol_df = df[df['Ticker'] == ticker]
        symbol_df = symbol_df.sort_values(by='Time')
        prices = symbol_df['Price'].tolist()
        time_labels = symbol_df['Time'].dt.strftime('%Y-%m-%d %H:%M').tolist()
        pnl_data.append(go.Scatter(x=time_labels, y=prices, mode='lines+markers', name=ticker))

    layout = go.Layout(title='Trade Price Timeline', xaxis=dict(title='Time'), yaxis=dict(title='Price ($)'))
    fig = go.Figure(data=pnl_data, layout=layout)
    return pyo.plot(fig, output_type='div', include_plotlyjs='cdn')

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
                # Simulated live price: small random change
                live_price = round(entry_price * random.uniform(0.97, 1.05), 2)
                pnl = round(live_price - entry_price, 2)
                positions.append({
                    "Ticker": ticker,
                    "Entry": round(entry_price, 2),
                    "Live": live_price,
                    "PnL": pnl
                })

        if os.path.exists("ledger/trade_log.csv"):
            trade_df = pd.read_csv("ledger/trade_log.csv")
            trades = trade_df.tail(10).to_dict(orient="records")

    except Exception as e:
        return f"<p>Error loading dashboard: {e}</p>"

    chart_html = generate_pnl_chart()
    return render_template_string(TEMPLATE, positions=positions, trades=trades, chart_html=chart_html)

if __name__ == "__main__":
    app.run(debug=True)

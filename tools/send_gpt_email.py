import smtplib
from email.mime.text import MIMEText
with open("reports/gpt_trade_summary_2025-05-21_2102.txt", "r", encoding="utf-8") as f:
    content = f.read()
msg = MIMEText(content)
msg["Subject"] = "FINBRO GPT Daily Summary"
msg["From"] = "you@example.com"
msg["To"] = "you@example.com"
with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login("you@example.com", "yourpassword")
    server.send_message(msg)
print("✅ GPT Summary sent via email.")
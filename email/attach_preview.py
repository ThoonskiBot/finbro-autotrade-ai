# Email Attachment: Attach JPG preview to email message
from email.mime.image import MIMEImage

def attach_preview_to_email(msg, preview_path="reports/previews/daily_trade_summary_chart_2025-05-21_preview.jpg"):
    try:
        with open(preview_path, "rb") as img:
            mime_img = MIMEImage(img.read())
            mime_img.add_header('Content-Disposition', 'attachment', filename="trade_preview.jpg")
            msg.attach(mime_img)
            print("📎 Preview image attached to email.")
    except Exception as e:
        print(f"⚠️ Failed to attach preview: {e}")

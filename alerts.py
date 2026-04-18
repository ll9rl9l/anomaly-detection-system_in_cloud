import requests
import smtplib
import os
from dotenv import load_dotenv

# تحميل المتغيرات من .env
load_dotenv()

# ==============================
# 📡 Telegram Alert
# ==============================
def send_telegram(message):
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not bot_token or not chat_id:
        print("❌ Telegram credentials not set")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        response = requests.post(url, data={
            "chat_id": chat_id,
            "text": message
        }, timeout=5)

        # تحقق إذا نجح الإرسال
        if response.status_code != 200:
            print("❌ Failed to send Telegram message:", response.text)

    except Exception as e:
        print(f"❌ Telegram Error: {e}")


# ==============================
# 📧 Email Alert
# ==============================
def send_email(message):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    if not sender or not password or not receiver:
        print("❌ Email credentials not set")
        return

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()

    except Exception as e:
        print(f"❌ Email Error: {e}")


# ==============================
# 🚨 Alert System
# ==============================
def alert_system(df):
    anomalies = df[df["status"] == "🔴 ALERT"]

    if len(anomalies) > 0:

        msg = f"""
🚨 ANOMALY DETECTED

Total Alerts: {len(anomalies)}

Top Suspicious Activity:
{anomalies[['IP','Requests','CPU']].head().to_string(index=False)}
"""

        send_telegram(msg)
        # send_email(msg)
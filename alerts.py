import requests
import smtplib
import streamlit as st

# ==============================
# 📡 Telegram Alert
# ==============================
def send_telegram(message):
    bot_token = st.secrets["BOT_TOKEN"]
    chat_id = st.secrets["CHAT_ID"]

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    requests.post(url, data={
        "chat_id": chat_id,
        "text": message
    })


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

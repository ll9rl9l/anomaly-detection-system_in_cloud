import streamlit as st
import time
import pandas as pd

from auth import login, check_login
from realtime_logs import stream_logs
from ml_model import SOCModel
from alerts import alert_system

st.set_page_config(page_title="ANOMALY DETECTION SYSTEM", layout="wide")

login()

if check_login():

    st.title("🧠 ANOMALY DETECTION SYSTEM")

    model = SOCModel()
    placeholder = st.empty()

    while True:

        df = stream_logs()

        model.train(df)
        result = model.predict(df)

        with placeholder.container():

            st.subheader("📡 LIVE TRAFFIC")
            st.dataframe(result)

            st.subheader("⚠️ THREAT LEVEL")
            st.bar_chart(result["status"].value_counts())

            st.subheader("🔥 HIGH RISK EVENTS")
            st.dataframe(result[result["risk_score"] >= 2])

            st.subheader("🌍 IP ACTIVITY")
            st.dataframe(result[["IP", "Requests", "CPU", "status"]])

        alert_system(result)

        time.sleep(2)

else:
    st.warning("🔐 Login required")
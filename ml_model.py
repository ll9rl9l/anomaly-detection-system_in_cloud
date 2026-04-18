import pandas as pd
from sklearn.ensemble import IsolationForest
from features import add_features

class SOCModel:

    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def train(self, df):
        df = add_features(df)

        features = df[
            ["Requests", "CPU", "Failed_Logins",
             "suspicious_ip", "high_requests",
             "high_cpu", "failed_login_risk"]
        ]

        self.model.fit(features)

    def predict(self, df):
        df = add_features(df)

        features = df[
            ["Requests", "CPU", "Failed_Logins",
             "suspicious_ip", "high_requests",
             "high_cpu", "failed_login_risk"]
        ]

        df["anomaly"] = self.model.predict(features)

        df["risk_score"] = (
            df["suspicious_ip"] +
            df["high_requests"] +
            df["high_cpu"] +
            df["failed_login_risk"]
        )

        df["status"] = df["anomaly"].apply(
            lambda x: "🔴 ALERT" if x == -1 else "🟢 NORMAL"
        )

        return df
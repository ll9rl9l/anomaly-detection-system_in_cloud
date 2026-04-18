def add_features(df):

    df["suspicious_ip"] = df["IP"].apply(
        lambda x: 1 if x in ["8.8.8.8", "185.200.100.5"] else 0
    )

    df["high_requests"] = df["Requests"].apply(
        lambda x: 1 if x > 3000 else 0
    )

    df["high_cpu"] = df["CPU"].apply(
        lambda x: 1 if x > 85 else 0
    )

    df["failed_login_risk"] = df["Failed_Logins"].apply(
        lambda x: 1 if x > 5 else 0
    )

    return df
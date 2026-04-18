import random
import time
import pandas as pd

def generate_log():
    ips = [
        "192.168.1.10",
        "192.168.1.20",
        "10.0.0.5",
        "8.8.8.8",
        "185.200.100.5"
    ]

    return {
        "IP": random.choice(ips),
        "CPU": random.randint(10, 100),
        "Requests": random.randint(50, 5000),
        "Failed_Logins": random.randint(0, 10),
        "Time": time.strftime("%H:%M:%S")
    }

def stream_logs(n=30):
    data = [generate_log() for _ in range(n)]
    return pd.DataFrame(data)
import time
import random
import requests

API_URL = "http://localhost:8000/ingest"

while True:
    payload = {
        "pressure": random.uniform(40, 80),
        "temperature": random.uniform(20, 60),
        "flow": random.uniform(10, 30)
    }

    try:
        r = requests.post(API_URL, json=payload)
        print("Sent:", payload, r.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(2)

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import numpy as np

app = FastAPI(title="AquilaSense API")

sensor_buffer = []

class SensorData(BaseModel):
    pressure: float
    temperature: float
    flow: float

@app.post("/ingest")
def ingest_data(data: SensorData):
    record = {
        "time": datetime.utcnow(),
        "pressure": data.pressure,
        "temperature": data.temperature,
        "flow": data.flow
    }
    sensor_buffer.append(record)

    if len(sensor_buffer) > 200:
        sensor_buffer.pop(0)

    return {"status": "ok", "message": "data received"}

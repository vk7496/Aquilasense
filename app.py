import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="AquilaSense", layout="wide")
st.title("AquilaSense – AI Industrial Monitoring")
st.caption("Developed by Vista Kaviani – AI Solution Developer")

API_URL = "http://localhost:8000/data"

@st.cache_data(ttl=5)
def load_data():
    r = requests.get(API_URL)
    return pd.DataFrame(r.json())

df = load_data()

if df.empty:
    st.warning("Waiting for sensor data...")
    st.stop()

features = df[["pressure", "temperature", "flow"]]
model = IsolationForest(contamination=0.05)
df["anomaly"] = model.fit_predict(features)

col1, col2 = st.columns(2)

with col1:
    fig = px.line(df, y="pressure", title="Pressure")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(df, y="flow", title="Flow")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Detected Anomalies")
st.dataframe(df[df["anomaly"] == -1])

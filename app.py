import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import IsolationForest
from datetime import datetime

st.set_page_config(page_title="AquilaSense", layout="wide")
st.title("AquilaSense – AI Industrial Monitoring")
st.caption("Developed by Vista Kaviani – AI Solution Developer")

# -------- DEMO MODE DATA --------
def generate_data(n=200):
    return pd.DataFrame({
        "time": pd.date_range(end=datetime.utcnow(), periods=n, freq="S"),
        "pressure": np.random.normal(60, 5, n),
        "temperature": np.random.normal(40, 3, n),
        "flow": np.random.normal(20, 2, n)
    })

df = generate_data()

# -------- AI MODEL --------
features = df[["pressure", "temperature", "flow"]]
model = IsolationForest(contamination=0.05)
df["anomaly"] = model.fit_predict(features)

# -------- DASHBOARD --------
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        px.line(df, x="time", y="pressure", title="Pressure"),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        px.line(df, x="time", y="flow", title="Flow"),
        use_container_width=True
    )

st.subheader("Detected Anomalies")
st.dataframe(df[df["anomaly"] == -1])

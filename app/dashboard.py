# app/dashboard.py

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from prophet import Prophet

# Title
st.title("🛍️ Retail Sales Forecasting Dashboard")

# Load cleaned and aggregated data
@st.cache_data
def load_data():
    df = pd.read_csv("./data/processed/monthly_sales.csv", parse_dates=['InvoiceMonth'])
    return df

data = load_data()

# Show raw data
if st.checkbox("Show Raw Monthly Sales Data"):
    st.write(data)

# Plot time series
st.subheader("📈 Monthly Sales Trend")
fig, ax = plt.subplots()
ax.plot(data['InvoiceMonth'], data['TotalPrice'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Total Sales (£)")
ax.set_title("Monthly Retail Sales Trend")
ax.grid(True)
st.pyplot(fig)

# Forecasting section
st.subheader("🔮 Forecast Next 6 Months")

# Prepare data for Prophet
prophet_df = data.rename(columns={"InvoiceMonth": "ds", "TotalPrice": "y"})
model = Prophet()
model.fit(prophet_df)

# Forecast future
future = model.make_future_dataframe(periods=6, freq='M')
forecast = model.predict(future)

# Plot forecast
fig_forecast = model.plot(forecast)
st.pyplot(fig_forecast)

# Show forecasted values
st.write("Forecasted Sales:")
st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(6))

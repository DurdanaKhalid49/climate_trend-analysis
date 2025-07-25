import streamlit as st
import pandas as pd
import joblib
# import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the dataset (ensure you have the correct path)
df = pd.read_csv("D:/Portfolio Projects/Climate Trend Analysis – Monthly Temperature Patterns/Data_/average_monthly_temperature_by_state_1950-2022.csv")
# Drop Unnecessary column
df.drop(columns=['Unnamed: 0'], inplace=True)

# 🔹 Ensure datetime column is in correct format
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
df.set_index('date', inplace=True)

import joblib
import requests
import tempfile

# Download the file from Hugging Face
url = "https://huggingface.co/durdanakhalid/climate-trend-model/resolve/main/climate_sarimax.joblib"
response = requests.get(url)

# Save it to a temp file and load
with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(response.content)
    model = joblib.load(tmp.name)

# Streamlit App Title
st.title("🌍 Climate Trend Analysis: Temperature Forecast")

# Sidebar for user input
st.sidebar.header("User Input")
st.sidebar.subheader("Select a Location")

# Extract available locations (assuming 'State' column exists)
states = df["state"].unique().tolist()
selected_state = st.sidebar.selectbox("Choose a State", states)

# Filter data for the selected state
state_data = df[df["state"] == selected_state]

# Plot historical trends
st.subheader(f"📊 Historical Temperature Trends in {selected_state}")
fig = px.line(state_data, x=state_data.index, y="average_temp", title=f"Temperature Trends in {selected_state}")
st.plotly_chart(fig)

# Forecasting Future Temperatures
st.subheader(f"🔮 Forecasting Future Temperatures for {selected_state}")
forecast_period = st.sidebar.slider("Select Forecast Period (Months)", 1, 24, 12)

# Predict future values
future_dates = pd.date_range(start=state_data.index[-1], periods=forecast_period + 1, freq='MS')[1:]
forecast = model.get_forecast(steps=forecast_period)
predicted_mean = forecast.predicted_mean

# Create a DataFrame for forecast results
forecast_df = pd.DataFrame({"date": future_dates, "Predicted Temperature": predicted_mean})
forecast_df.set_index("date", inplace=True)

# Plot predictions
fig2 = px.line(forecast_df, x=forecast_df.index, y="Predicted Temperature", title=f"Predicted Temperatures for {selected_state}")
st.plotly_chart(fig2)

# Show data
st.subheader("📋 Forecasted Data")
st.write(forecast_df)

st.success("✅ Climate trend dashboard is ready!")

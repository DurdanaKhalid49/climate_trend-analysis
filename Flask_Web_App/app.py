from flask import Flask, render_template, request
import pandas as pd
import joblib
import plotly.express as px
import numpy as np
import os
import requests
import tempfile
app = Flask(__name__)
# Load trained SARIMAX model
# Download the file from Hugging Face
url = "https://huggingface.co/durdanakhalid/climate-trend-model/resolve/main/climate_sarimax.joblib"
response = requests.get(url)

# Save it to a temp file and load
with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(response.content)
    model = joblib.load(tmp.name)
# Load the dataset (ensure you have the correct path)
df = pd.read_csv("Data_/average_monthly_temperature_by_state_1950-2022.csv")
# Drop Unnecessary column
df.drop(columns=['Unnamed: 0'], inplace=True)

# 🔹 Ensure datetime column is in correct format
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
df.set_index('date', inplace=True)

# Get available states/regions from dataset
states = df["state"].unique().tolist()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        selected_state = request.form["state"]
        months = int(request.form["month"])

        # Filter data for the selected state
        state_data = df[df["state"] == selected_state]["average_temp"]

        # Generate future dates
        last_date = state_data.index[-1]
        future_dates = pd.date_range(last_date, periods=months+1, freq="M")[1:]

        # Forecast future temperatures
        forecast = model.forecast(steps=months)
        forecast_df = pd.DataFrame({"date": future_dates, "Predicted Temperature": forecast})
        
        # Plotly Visualization
        fig = px.line(state_data, x=state_data.index, y=state_data.values, title=f"Temperature Trend for {selected_state}")
        fig.add_scatter(x=future_dates, y=forecast, mode='lines', name="Forecasted Temperature")

        # Convert plot to JSON for rendering
        graph_json = fig.to_json()

        return render_template("results.html", state=selected_state, forecast_df=forecast_df, graph_json=graph_json)

    return render_template("index.html", states=states)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # use Railway port or default to 8080
    app.run(host="0.0.0.0", port=port)        


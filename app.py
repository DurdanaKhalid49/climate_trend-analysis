from flask import Flask, render_template, request
import pandas as pd
import joblib
import plotly.express as px
import numpy as np

app = Flask(__name__)

# Load trained SARIMAX model
model = joblib.load("climate_sarimax.pkl")
# Load the dataset (ensure you have the correct path)
df = pd.read_csv("D:/Portfolio Projects/Climate Trend Analysis – Monthly Temperature Patterns/Data_/average_monthly_temperature_by_state_1950-2022.csv")
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
    app.run(debug=True)

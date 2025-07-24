# 🌍 Climate Trend Analysis – Flask Web App

A Flask-based web application that allows users to forecast monthly average temperatures for different Indian states using a SARIMAX time series model. The app includes an interactive Plotly chart and a summary table for future temperature trends.

---

## 📌 Project Overview

This project is part of a broader climate analytics initiative to analyze and forecast temperature patterns. The model is trained using historical temperature data and leverages **SARIMAX** for seasonal forecasting.

### 🔍 Features:
- Forecast temperature trends for 1 to 24 months.
- Select any Indian state from a dropdown.
- View an interactive Plotly chart.
- See tabular predictions with rounded temperature values.
- Clean, modern UI built with HTML/CSS.

---

## 🛠️ Tech Stack

| Component        | Description                           |
|------------------|---------------------------------------|
| Python           | Programming Language                  |
| Flask            | Web Framework                         |
| SARIMAX (Statsmodels) | Time Series Forecasting Model   |
| Pandas           | Data Processing                       |
| Plotly           | Visualization                         |
| HTML/CSS         | Frontend Styling                      |
| Railway          | Deployment Platform                   |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/climate-trend-analysis.git
cd climate-trend-analysis
```
### 2️⃣ Create a Virtual Environment (Python 3.10)
```
python -m venv venv
```
### On Windows
```
venv\Scripts\activate
```
### On Mac/Linux
```
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Run the Flask App Locally
```
python app.py
Visit: http://127.0.0.1:5000/ in your browser.
```
🚀 Deployment (Railway)
The app is deployed on Railway using Nixpacks for environment setup.

Railway Deployment Steps:
Push your code to GitHub.

Connect the repo to Railway.

Set the startup command to:
```
python app.py
```
Add a requirements.txt and optionally a Procfile:

```
web: python app.py
```
## 📁 Project Structure
```
climate-trend-analysis/
│
├── app.py                     # Flask main app
├── model.py                   # SARIMAX training + saving script
├── climate_sarimax.pkl        # Saved SARIMAX model
├── templates/
│   ├── index.html             # Input form (styled)
│   └── results.html           # Output plot + table
├── static/                    # (Optional) For styling/images
├── requirements.txt
└── README.md
📊 Dashboard (Optional)
A companion Streamlit dashboard is also available for users who prefer a dashboard-style UI. It allows users to explore temperature patterns with filtering and visual exploration.
```
🙋‍♀️ Author
Durdana Khalid
Data Science Enthusiast | Time Series | Forecasting | Flask & Streamlit Apps
Portfolio Website | LinkedIn

📜 License
This project is open-source and available under the MIT License.

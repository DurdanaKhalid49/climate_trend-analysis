# Climate Trend Analysis and Forecasting

This project predicts customer churn using a machine learning model. It includes:
- A trained SARIMAX model (`model.py`)
- A **Streamlit dashboard** (`dashboard.py`) for interactive predictions
- A **Flask API** (`app.py`) to serve the model
- All necessary files to deploy and run the project

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/DurdanaKhalid49/climate-trend-analysis.git
   cd climate-trend-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Model

Train and save the model:
```sh
python model.py
```

## Running the Streamlit Dashboard
```sh
streamlit run dashboard.py
```

## Running the Flask API
```sh
python app.py
```

## API Usage
Send a POST request with climate features:
```sh
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"features": [state,months]}'
```

## Folder Structure
```
📂 climate-trend-analysis
│── model.py            # Train & save model
│── dashboard.py        # Streamlit dashboard
│── app.py              # Flask API
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── model.pkl           # Saved model
│── scaler.pkl          # Saved scaler
│── Data_            # average_monthly_temperature_by_state_1950-2022.csv and merged_temperature_data.csv
│── .gitignore          # Ignore unnecessary files
```

## License
This project is open-source under the MIT License.


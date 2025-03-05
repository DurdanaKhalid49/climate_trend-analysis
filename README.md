# Customer Churn Prediction

This project predicts customer churn using a machine learning model. It includes:
- A trained Random Forest model (`model.py`)
- A **Streamlit dashboard** (`app.py`) for interactive predictions
- A **Flask API** (`flask_app.py`) to serve the model
- All necessary files to deploy and run the project

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/customer-churn-prediction.git
   cd customer-churn-prediction
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
streamlit run app.py
```

## Running the Flask API
```sh
python flask_app.py
```

## API Usage
Send a POST request with customer features:
```sh
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"features": [value1, value2, value3, value4]}'
```

## Folder Structure
```
📂 customer-churn-prediction
│── model.py            # Train & save model
│── app.py              # Streamlit dashboard
│── flask_app.py        # Flask API
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── model.pkl           # Saved model
│── scaler.pkl          # Saved scaler
│── data.csv            # Dataset (add your own)
│── .gitignore          # Ignore unnecessary files
```

## License
This project is open-source under the MIT License.


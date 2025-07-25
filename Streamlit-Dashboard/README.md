# 🌡️ Climate Trend Analysis Dashboard

An interactive **Streamlit** dashboard for exploring **monthly average temperature trends** across U.S. states and predicting future climate patterns using a **SARIMAX** time series model.

Hosted Model: [Hugging Face Repo 🔗](https://huggingface.co/durdanakhalid/climate-trend-model)  
Dashboard Built With: `Streamlit`, `Pandas`, `Plotly`, `Statsmodels`, `Joblib`

---

## 📌 Key Features

✅ Visualize long-term monthly temperature changes across U.S. states  
✅ Predict future trends using SARIMAX forecasting  
✅ Clean, responsive UI powered by Streamlit  
✅ Load model directly from Hugging Face using `requests` and `joblib`

---

## 📊 Dashboard Preview

![Dashboard Screenshot](preview_image.png)  
> _Forecasting monthly average temperatures with state-wise filtering_

---

## 🚀 Quick Start

To run this dashboard locally:

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/durdanakhalid/climate-trend-dashboard.git
cd climate-trend-dashboard
```
## 2️⃣ Create a Virtual Environment & Activate It
```
python -m venv venv
```
### Windows
```
venv\Scripts\activate
```
### Mac/Linux
```
source venv/bin/activate
```
## 3️⃣ Install the Dependencies
```
pip install -r requirements.txt
```
## 4️⃣ Run the Dashboard
```
streamlit run app.py
Streamlit will launch at:
📍 http://localhost:8501
```
## 📂 Project Structure
```
Streamlit-Dashboard/
│
├── app.py                 # Streamlit app code
├── requirements.txt       # Python dependencies
└── README.md
└── Data_
```
## Model Details
The SARIMAX model was trained on monthly temperature data from 1950–2022 and saved as a .joblib file.

Model hosted on Hugging Face:
📦 climate_sarimax.joblib → View Model

Sample code to load model:

```
import requests
from io import BytesIO
from joblib import load

url = "https://huggingface.co/durdanakhalid/climate-trend-model/resolve/main/climate_sarimax.joblib"
model = load(BytesIO(requests.get(url).content))
```
🧠 Tech Stack
Tool	Purpose
Streamlit	Web app interface
Pandas	Data manipulation
Plotly	Interactive charts & visuals
Statsmodels	SARIMAX model (time series)
Joblib	Model serialization
Hugging Face	Model hosting (LFS)

👤 Author
Durdana Khalid
🎯 Aspiring Data Scientist | Portfolio Projects
📫 Email me | 🌐 Portfolio

📄 License
This project is licensed under the MIT License.

For questions, contributions, or feedback — feel free to open an issue or pull request!

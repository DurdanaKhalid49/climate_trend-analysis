import pandas as pd
import joblib
import statsmodels.api as sm

# 🔹 Load dataset
df = pd.read_csv("D:/Portfolio Projects/Climate Trend Analysis – Monthly Temperature Patterns/Data_/average_monthly_temperature_by_state_1950-2022.csv")  # Update with your actual dataset path

# Drop Unnecessary column
df.drop(columns=['Unnamed: 0'], inplace=True)

# 🔹 Ensure datetime column is in correct format
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
df.set_index('date', inplace=True)

# 🔹 Drop or aggregate duplicate dates
df = df[~df.index.duplicated(keep='first')]  # Removes duplicates
# OR df = df.groupby(df.index).mean()  # Aggregates duplicates using mean

# 🔹 Automatically infer frequency
df = df.asfreq(df.index.inferred_freq)

# If frequency is still None, manually set it (e.g., 'MS' for monthly)
if df.index.freq is None:
    df = df.asfreq("MS")

# 🔹 Handle missing values (forward fill, adjust if needed)
df.fillna(method="ffill", inplace=True)

# 🔹 Select target variable (e.g., temperature)
target_column = "average_temp"  # Adjust based on dataset
y = df[target_column]

# 🔹 Differencing (to make series stationary if needed)
y_diff = y.diff().dropna()

# 🔹 Fit SARIMAX model (adjust order based on ADF test & ACF/PACF plots)
sarimax_order = (1, 1, 1)  # (p, d, q) - Change based on best parameters
seasonal_order = (1, 1, 1, 12)  # (P, D, Q, S) for seasonality

model = sm.tsa.statespace.SARIMAX(
    y_diff, order=sarimax_order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False
)

results = model.fit()

# 🔹 Save model
joblib.dump(results, "climate_sarimax.pkl")

print("✅ SARIMAX Model trained and saved successfully!")

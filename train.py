import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# Load dataset
data = pd.read_csv("car data.csv")

# Create Car Age feature
data["Car_Age"] = 2025 - data["Year"]

# Drop unnecessary columns
data.drop(["Car_Name", "Year"], axis=1, inplace=True)

# Convert categorical data into numerical form
data = pd.get_dummies(data, drop_first=True)

# Features and target
X = data.drop("Selling_Price", axis=1)
y = data["Selling_Price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
score = r2_score(y_test, predictions)

print("Model Accuracy (R² Score):", round(score * 100, 2), "%")

# Save model
joblib.dump(model, "car_price_model.pkl")

print("Model saved successfully as car_price_model.pkl")
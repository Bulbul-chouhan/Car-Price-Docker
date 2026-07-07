from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("car_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        present_price = float(request.form["present_price"])
        kms_driven = int(request.form["kms_driven"])
        fuel_type = request.form["fuel_type"]
        seller_type = request.form["seller_type"]
        transmission = request.form["transmission"]
        owner = int(request.form["owner"])
        year = int(request.form["year"])

        car_age = 2025 - year

        input_data = pd.DataFrame({
            "Present_Price": [present_price],
            "Kms_Driven": [kms_driven],
            "Owner": [owner],
            "Car_Age": [car_age],
            "Fuel_Type_Diesel": [1 if fuel_type == "Diesel" else 0],
            "Fuel_Type_Petrol": [1 if fuel_type == "Petrol" else 0],
            "Seller_Type_Individual": [1 if seller_type == "Individual" else 0],
            "Transmission_Manual": [1 if transmission == "Manual" else 0]
        })

        prediction = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction_text=f"Estimated Car Price: ₹ {prediction:.2f} Lakhs"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)
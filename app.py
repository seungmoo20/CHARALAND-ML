from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)


pipeline = joblib.load("model/pipeline_house_price.joblib")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/estimate", methods=["GET", "POST"])
def estimate():
    prediction = None


    if request.method == "POST":
        input_data = {
            "building_size_m2": float(request.form.get("building_size_m2", 0)),
            "land_size_m2": float(request.form.get("land_size_m2", 0)),
            "bedrooms": float(request.form.get("bedrooms", 0)),
            "bathrooms": float(request.form.get("bathrooms", 0)),
            "carports": float(request.form.get("carports", 0)),
            "garages": float(request.form.get("garages", 0)),
            "floors": float(request.form.get("floors", 1)),
            "lat": float(request.form.get("lat", -6.2)),
            "long": float(request.form.get("long", 106.8)),
            "city": request.form.get("city", "Unknown"),
            "district": request.form.get("district", "Unknown"),
            "certificate": request.form.get("certificate", "Unknown"),
            "furnishing": request.form.get("furnishing", "Unknown"),
            "property_condition": request.form.get("property_condition", "Unknown"),
            "property_type": request.form.get("property_type", "Unknown"),
            "electricity": request.form.get("electricity", "Unknown"),
        }

        df_input = pd.DataFrame([input_data])

        # PREDICT (ingat: model log!)
        log_result = pipeline.predict(df_input)[0]
        result = np.expm1(log_result)

        prediction = f"{int(result):,}".replace(",", ".")

    return render_template("estimate.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

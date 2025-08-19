from flask import Flask, request, jsonify
import pandas as pd
import joblib
from utils import get_data_path

app = Flask(__name__)

# Load the trained model
model_path = get_data_path("iris_model.pkl")
model = joblib.load(model_path)

# Define required input fields
REQUIRED_FIELDS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Check if JSON is provided
        if not data:
            return jsonify({"error": "No JSON payload provided"}), 400

        # Validate required fields
        for field in REQUIRED_FIELDS:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
            # Validate numeric types
            if not isinstance(data[field], (int, float)):
                return jsonify({"error": f"Field '{field}' must be a number"}), 400

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(df)

        return jsonify({"prediction": int(prediction[0])}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "message": "API is running!"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

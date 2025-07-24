from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")

# Extract options from encoders
dropdown_options = {col: le.classes_.tolist() for col, le in encoders.items()}

@app.route('/')
def index():
    return render_template('index.html', options=dropdown_options)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []
        for field in ['product_name', 'brand', 'category', 'adulterant', 'detection_method', 'severity', 'health_risk']:
            value = request.form[field]
            encoder = encoders[field]
            input_data.append(encoder.transform([value])[0])

        prediction = model.predict([input_data])
        result = target_encoder.inverse_transform(prediction)[0]

        return jsonify({'action': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

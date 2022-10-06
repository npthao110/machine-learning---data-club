from flask import Flask
from flask import request
from flask import jsonify

import pickle

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model.bin')

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    card = request.get_json()

    X = dv.transform([card])
    y_pred = model.predict_proba(X)[0, 1]
    card = y_pred >= 0.5

    result = {
        'credit_probability': float(y_pred),
        'credit': bool(card)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
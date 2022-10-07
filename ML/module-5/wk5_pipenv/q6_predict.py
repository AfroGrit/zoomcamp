import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model2.bin'
dv_file = 'dv.bin'

with ( 
  open(model_file, 'rb') as model,
  open(dv_file, 'rb') as dv):
  model = pickle.load(model)
  dv = pickle.load(dv)

app = Flask('Credit card issuing predictor!')

@app.route('/q6_predict', methods=['POST'])
def predict():
  client = request.get_json()
  X = dv.transform([client])
  prediction = model.predict_proba(X)[0,1]
  credit_card = prediction >= 0.5

  result = {
      'Client credibilty': float(prediction),
      'issue Credit Card': bool(credit_card)
  }

  return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9697)  
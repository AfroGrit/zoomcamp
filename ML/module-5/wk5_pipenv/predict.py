import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
dv_file = 'dv.bin'

with ( 
  open(model_file, 'rb') as model,
  open(dv_file, 'rb') as dv):
  model = pickle.load(model)
  dv = pickle.load(dv)

app = Flask('issue_CC')

@app.route('/predict', methods=['POST'])
def predict():
  client = request.get_json()
  # transform client into feature matrix
  X = dv.transform([client])
  prediction = model.predict_proba(X)[0,1]
  churn = prediction >= 0.5

  result = {
      'issue_CC_probability': float(prediction),
      'issue_CC': bool(churn)
  }

  return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)  
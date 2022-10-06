import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with ( 
  open(model_file, 'rb') as model,
  open(dv_file, 'rb') as dv):
  model = pickle.load(model)
  dv = pickle.load(dv)

q3_client = {
  "reports": 0, 
  "share": 0.001694, 
  "expenditure": 0.12, 
  "owner": "yes"
  }

# transform client into feature matrix
X = dv.transform([q3_client])
print(X)
print(model.predict_proba(X)[0,1])

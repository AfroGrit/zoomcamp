import bentoml
from bentoml.io import JSON, NumpyNdarray

model_ref = bentoml.xgboost.get('uv_radiation_model:latest')
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service('uvradiation', runners=[model_runner])

# payload = {
#   'max_ground_temp': -9.0,
#   'min_ground_temp': -77.0,
#   'max_air_temp': -3.0,
#   'min_air_temp': -81.0,
#   'mean_pressure': 863.0,
#   'weather': 'Sunny'
# }

# @svc.api(input=NumpyNdarray(), output=NumpyNdarray())
@svc.api(input=JSON(), output=NumpyNdarray())
def classify(application_data):
  """
  This function generates predictions from API calls.
  """
  # prediction = model_runner.predict.run(application_data)
  payload = dv.transform(application_data)
  # print(f'prediction:" {model_runner.predict.run(data)}')
  return model_runner.predict.run(payload)
  # return { 'radiotion': 'hot'}
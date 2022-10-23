import bentoml
from bentoml.io import JSON, NumpyNdarray

# model_ref = bentoml.sklearn.get('mlzoomcamp_homework:qtzdz3slg6mwwdu5')
model_ref = bentoml.sklearn.get('mlzoomcamp_homework:jsi67fslz6txydu5')
model_runner = model_ref.to_runner()
svc = bentoml.Service('coolmodel', runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(application_data):
  """
  description: Model service: classifier
  This function generates predictions from API calls.
  parameters:
  - data: User data
    description: User data
    required: true
    type: NumpyNdarray    
  """
  # prediction = model_runner.predict.run(application_data)
  return model_runner.predict.run(application_data)
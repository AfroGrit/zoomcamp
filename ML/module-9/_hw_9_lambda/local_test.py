import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# url = 'https://qjf5yrg691.execute-api.us-east-1.amazonaws.com/wear-test/predict' # serving on AWS

data = {'url': 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'}

result = requests.post(url, json=data).json()
print(result)
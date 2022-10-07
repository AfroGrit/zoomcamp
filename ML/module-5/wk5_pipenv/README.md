
### Wk5 homework

- please run q6 as follows:

`url = 'http://0.0.0.0:9697/q6_predict'
client = {'reports': 0, 'share': 0.245, 'expenditure': 3.438, 'owner': 'yes'}
requests.post(url, json=client).json()
`
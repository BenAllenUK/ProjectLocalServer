import urllib.request
import requests, time
import json
import copy

enviroId = 1

habUrl = 'http://localhost:8080/rest/items?recursive=false'
serverUrl = 'http://35.231.193.82:3000/update'

headers = dict(
    Accept='application/json'
)

# while True:
resp = requests.get(url=habUrl, headers=headers)
data = resp.json()
headers2 = {'content-type': 'application/json'}
params = {
    'enviroId': enviroId
}
requests.post(serverUrl, params=params, data=json.dumps(data), headers=headers2)
print("request sent")
    # time.sleep(5)

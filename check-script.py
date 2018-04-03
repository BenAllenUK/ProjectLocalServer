import urllib.request
import requests, time
import json
import copy

habUrl = 'http://192.168.0.95:8080/rest/items?recursive=false'
serverUrl = 'http://localhost:3000/update'

headers = dict(
    Accept='application/json'
)

# while True:
resp = requests.get(url=habUrl, headers=headers)
data = resp.json()
headers2 = {'content-type': 'application/json'}
requests.post(serverUrl, data=json.dumps(data), headers=headers2)
print("request sent")
    # time.sleep(5)

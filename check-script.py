import urllib.request
import requests, time
import json
import copy
import datetime

enviroId = 1
interval = 5
limit = 720 # 60 * 60 / 5

habUrl = 'http://localhost:8080/rest/items?recursive=false'
serverUrl = 'http://35.231.193.82:3000/update'

headers = dict(
    Accept='application/json'
)

for x in range(0, limit):
    try:
        resp = requests.get(url=habUrl, headers=headers)
        data = resp.json()
        headers2 = {'content-type': 'application/json'}
        params = {
            'enviroId': enviroId
        }
        requests.post(serverUrl, params=params, data=json.dumps(data), headers=headers2)
        print(data)
        print(datetime.datetime.utcnow() + " Request sent")
    except:
        print("request failed")
    time.sleep(interval)

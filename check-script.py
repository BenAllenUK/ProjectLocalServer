import urllib.request
import requests, time
import json
import copy
import datetime
import os
print("=======================")
print(os.getpid())

enviroId = os.environ['ENV_NUM']
interval = 30
limit = 120 # 60 * 60 / 5

#REMOTE:
habUrl = 'http://localhost:8080/rest/items?recursive=false'
serverUrl = 'http://35.231.193.82:3000/update'

#LOCAL:
# habUrl = 'http://192.168.0.108:8080/rest/items?recursive=false'
# serverUrl = 'http://localhost:3000/update'

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
        print("===========")
        for item in data:
            if "RelativeHumidity" in item['name']:
                print(item['name'] + ": " + item['state'])
        for item in data:
            if "SensorTemperature" in item['name']:
                print(item['name'] + ": " + item['state'])



        requests.post(serverUrl, params=params, data=json.dumps(data), headers=headers2)
        print(str(datetime.datetime.utcnow()) + " Request sent for environment: " + str(enviroId))
    except:
        print(str(datetime.datetime.utcnow()) + " Request failed")
    time.sleep(interval)

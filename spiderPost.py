import requests
import json

url = 'http://106.14.212.56:8080/happy/query/'
data = {
    "db": "gouwu",
    "table": "product",
    "jsonMessage": {
    }
}
r = requests.post(url, verify=False, data=json.dumps(data), headers={
    'Content-Type': 'application/json'
})

print(type(r.json()))

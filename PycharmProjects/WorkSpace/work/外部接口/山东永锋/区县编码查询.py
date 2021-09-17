import requests
import json

url = "http://116.228.222.130:28082/areaCode/query"

payload = json.dumps({
    "fatherKeyValue": "保定市",
    "keyValue": "容城县"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

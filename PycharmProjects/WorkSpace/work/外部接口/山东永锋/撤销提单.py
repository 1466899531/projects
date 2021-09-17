import requests
import json

url = "http://10.0.161.37:20002/api/yongfeng/cancel"

payload = json.dumps({
    "loginInfo": {
        "userName": "test",
        "password": "test",
        "platName": "yfwl.com"
    },
    "cancelInfo": {
        "dependId": "403350633442",
        "cancelType": "2"
    }
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests
import json

url = "http://116.228.222.130:28082/api/yongfeng/outWeight"

payload = json.dumps({
    "loginInfo": {
        "userName": "test",
        "password": "test",
        "platName": "yfwl.com"
    },
    "outInfo": [
        {
            "deliveryId": "16489618",
            "dependId": "919254580028",
            "outWeight": "30",
            "outTime": "2020-11-24 14:49:09",
            "entryTime": "2020-11-24 14:41:09"
        }
    ]
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests
import json

url = "http://10.0.161.37:20002/api/yongfeng/modDelivery"

payload = json.dumps({
    "loginInfo": {
        "userName": "test",
        "password": "test",
        "platName": "yfwl.com"
    },
    "modInfo": [
        {
            "deliveryId": "16489633",
            "valuMode": "1",
            "price": "300"
        }
    ]
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

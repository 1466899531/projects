import requests
import json

url = "http://api-v3.wbtech.com/api/yongfeng/code"

payload = "{\r\n    \"loginInfo\":{\r\n        \"userName\":\"sdwb\",\r\n        \"password\":\"sdwb\",\r\n        \"platName\":\"sdwb.com\"\r\n    },\r\n    \"queryInfo\":{\r\n        \"type\":\"1\",\r\n        \"name\":\"山东首科钢铁有限公司(永锋)\",\r\n         \"phone\":\"13256596362\"\r\n    }\r\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests
import json
'''
    接口功能描述: 调度单修改
'''''
def ModDelivery():
    url = 'http://10.0.161.37:20002/api/yongfeng/modDelivery'
    headers = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com.lg"
        },
        "modInfo": [{
            "deliveryId": "17157169",
            "prodDesc": "测试描述",
            "valuMode": "1",
            "price": "120",
            "outWeight": "30",
            "qty": "10000"
        }]
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
ModDelivery()

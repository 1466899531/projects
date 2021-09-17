import requests
import json
'''
    接口功能描述: 永锋撤销提单
'''
def CancelDelivery():
    url = 'http://10.0.161.37:20002/api/yongfeng/cancel'
    head = {'Content-Type': "application/json"}

    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com.lg"
        },
        "cancelInfo": {
            "deliveryId": "17157203",
            "cancelType": "1",
            "dependId": "5580144651610"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=head)
    print(res.status_code)
    print(res.text)
CancelDelivery()

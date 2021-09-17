import requests
import json
'''
    接口功能描述: 外部接口调度单撤销
'''
def CancleDelivery():
    url = 'http://10.0.161.60:20002/api/wubo/cancleDelivery'
    headers = {'Content-Type': "application/json"}
    data ={
        "dataInfo": [{
            "dependNum": "SHD20210126001",
            "deliveryId": 15599780,
            "deliveryNum": "DD210126100089",
            "status": "00",
            "cancelType": "1"
        }],
        "loginInfo": {
            "password": "123456",
            "platName": "kx0001",

            "userName": "dzadmin"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
CancleDelivery()

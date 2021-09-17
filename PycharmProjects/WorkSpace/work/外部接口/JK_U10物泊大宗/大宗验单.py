import requests
import json
'''
    接口功能描述: 外部接口调度单撤销
'''
def validateDelivery():
    url = 'http://10.0.161.60:20002/api/wubo/validateDelivery'
    headers = {'Content-Type': "application/json"}
    data ={
        "dataInfo": [{
            "dependNum": "SHD-102-1606700348942",
            "deliveryId": 14538764,
            "deliveryNum": "DD201130100004",
            "docuType": 10
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
validateDelivery()

import requests
import json
'''
    接口功能描述: 返单量上传-装收货
'''
def returnBill():
    url = 'http://10.0.161.60:20002/api/wubo/returnBill'
    headers = {'Content-Type': "application/json"}
    data = {
        "dataInfo": [
            {
                "dependNum": "CG_904948006",
                "deliveryId": 14538763,
                "outWeight": 30,
                "outQty": 1,
                "outTime": "2020-11-10 10:13:00",
                "zcWeight": 30,
                "zcQty": 1,
                "logisticsMark": "C"
            }
        ],
        "loginInfo": {
            "password": "123456",
            "platName": "kx0001",
            "userName": "dzadmin"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
returnBill()

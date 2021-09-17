import requests
import json
'''
    接口功能描述: 外部接口调度单撤销
'''
def returnStatus():
    url = 'http://10.0.161.60:20002/api/wubo/returnStatus'
    headers = {'Content-Type': "application/json"}
    data ={
        "dataInfo": [
            {
                "deliveryId": "14538764",
                "dependNum": "SHD-102-1606700348942",
                "status": "90"
            }
        ],
        "loginInfo": {
            "password": "123456",
            "platName": "kx0001",
            "userName": "dzAdmin"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
returnStatus()

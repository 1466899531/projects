import requests
import json
import random
'''
    接口功能描述: 物泊大宗货源单上传
'''
def procPublishApi():
    url = 'http://10.0.161.60:20002/api/wubo/procPublishApi'
    headers = {'Content-Type': "application/json"}
    depend = "CG_"+str(random.randint(1, 999999999))
    data = {
        "dataInfo": [
            {
                "amount": 0,
                "dependNum": depend,
                "goodTypeDesc": "线材",
                "goodsPrice": 0,
                "logisticsMark": "C", # C:采购 X:销售
                "platName": "kx0001",
                "qty": 1,
                "sender": "鑫源",
                "senderMobile": "",
                "weight": 3000
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
    print(depend)
procPublishApi()

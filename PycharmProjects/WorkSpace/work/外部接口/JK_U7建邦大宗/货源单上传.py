import requests
import json
import random
'''
    接口功能描述: 大宗货源单上传
'''
def procPublishApi():
    url = 'http://116.228.222.130:28082/jianbang/tmsapi/json/sendCgOrder.jsp'
    headers = {'Content-Type':'application/json'}
    depend = "_"+str(random.randint(1, 999999999))
    data = {
        "loginInfo": {
            "customerId": "jianbang",
            "password": "jianbang"
        },
        "dataInfo": {
            "dependNum": "TZSH20200903104",
            "weight": "3000",
            "qty": "300",
            "goodsPrice": "770",
            "amount": "2310000",
            "goodTypeDesc": "GC50KG",
            "remark": "建邦测试",
            "sender": "XHX",
            "senderMobile": "13838339604",
            "ret1": "test.software",
            "startPlate": "H"
        }
    }
    data1 ={
           "jsonParam":json.dumps(data,ensure_ascii=False)
       }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
procPublishApi()

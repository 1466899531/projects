import requests
import json
import random
'''
    接口功能描述: 大宗返单量上传
'''
def sendReturnAmount():
    url = 'http://116.228.222.130:28082/jianbang/tmsapi/json/sendReturnAmount.jsp'
    headers = {'Content-Type':'application/json'}
    depend = "_"+str(random.randint(1, 999999999))
    data ={
        "loginInfo": {
            "customerId": "jianbang",
            "password": "jianbang"
        },
        "dataInfo": {
            "billId": "TZSH2020070101",
            "deliveryId": "10013550",
            "returnWeight": "29.98",
            "returnQty": "100",
            "ret1": "29.99",
            "ret3": "11S2020051301",
            "returnTime": "2020-09-03 12:56:00",
            "ret4": "建邦铸造磅"
        }
    }
    data1 ={
           "jsonParam":json.dumps(data,ensure_ascii=False)
       }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
sendReturnAmount()

import requests
import json
import random
'''
    接口功能描述: 大宗货源单撤销
'''
def canclePublishApi():
    url = 'http://116.228.222.130:28082/jianbang/tmsapi/json/invalidGoodOrder.jsp'
    headers = {'Content-Type':'application/json'}
    depend = "_"+str(random.randint(1, 999999999))
    data ={
        "loginInfo": {
            "customerId": "jianbang",
            "password": "jianbang"
        },
        "removeInfo": {
            "dependNum": "TZSH20200903103",
            "dependId": "TZSH20200903103"
        }
    }
    data1 ={
           "jsonParam":json.dumps(data,ensure_ascii=False)
       }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
canclePublishApi()

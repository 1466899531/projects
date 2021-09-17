import requests
import json
import random
'''
    接口功能描述: 调度单撤销
'''
def deliveryCancelOrValidate():
    url = 'http://116.228.222.130:28082/jianbang/tmsapi/json/deliveryCancelOrValidate.jsp'
    headers = {'Content-Type':'application/json'}
    depend = "_"+str(random.randint(1, 999999999))
    data ={
        "loginInfo": {
            "customerId": "jianbang",
            "password": "jianbang"
        },
        "deliveryInfo": [{
            "publish_id": "10118440",
            "delivery_id": "10018581",
            "docu_type": "00"
        }]
    }
    data1 ={
           "jsonParam":json.dumps(data,ensure_ascii=False)
       }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
deliveryCancelOrValidate()

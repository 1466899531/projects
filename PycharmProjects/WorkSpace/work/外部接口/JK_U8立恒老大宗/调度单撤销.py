import requests
import json
import random

'''
    接口功能描述: 立恒大宗调度单撤销
'''
def deliveryCancelOrValidate():
    url = 'http://116.228.222.130:28082/tmsapi/json/deliveryCancelOrValidate.jsp'
    headers = {'Content-Type': 'application/json'}
    depend = "_" + str(random.randint(1, 999999999))
    data = {
        "version": "V15.0.0.7",
        'loginInfo': {
            "customerId": "jianbang",
            "password": "jianbang"
        },
        "deliveryInfo": [{
            "publish_id": "10118441",  # 货源单号
            "delivery_id": "10018584",  # 调度单号
            "docu_type": "00"  # 00撤销 10验证
        }],
        "creattime": "2019-11-27 08:10:11.891"
    }
    data1 = {
        "jsonParam": json.dumps(data, ensure_ascii=False)
    }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
deliveryCancelOrValidate()

import requests
import json
import random
'''
    接口功能描述: 立恒大宗返单量上传
'''
def sendReturnAmount():
    url = 'http://116.228.222.130:28082/tmsapi/json/sendReturnAmount.jsp'
    headers = {'Content-Type': 'application/json'}
    depend = "_" + str(random.randint(1, 999999999))
    data = {
        "version": "V15.0.0.7",
        "loginInfo": {
            "customerId": "gaoyi",
            "password": "gaoyi"
        },
        "dataInfo": [{
                         "billId": "10118470",  # 货源单id
                     "deliveryId": "10018615",  #调度单id
    "returnWeight": 30.11, # 销售 装货重量，采购 收货装量
    "returnQty": "0", # 数量
    "returnTime": "20191128081011",
    "ret1": "30.23", # 销售没用，采购 装货重量
    "logisticsMark": "C", # X销售 不填或C采购
    }],
    "creattime": "2019-11-28 08:10:11.891"
    }
    data1 = {
        "jsonParam": json.dumps(data, ensure_ascii=False)
    }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
sendReturnAmount()

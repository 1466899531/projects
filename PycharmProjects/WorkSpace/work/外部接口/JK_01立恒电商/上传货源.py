import json

import requests
""" 立恒电商 (lhds/111111)"""
def uploadPublish():
    url = "http://116.228.222.130:28082/tmsapi/json/goodsUpload2.action"
    payload = {
        "customerId": "C55617",
        "dataInfo": {
            "billSender": "分年矿业",
            "billSenderMobile": "17612175285",
            "billTaker": "立恒厂库取单员-方方",
            "billTakerMobile": "0357-5528141",
            "dependNum": "20210721002",
            "dependNum2": "20210721002",
            "dsGoodsPrice": 4350,
            "dsIfSettle": "0",
            "dszdFlag": "0",
            "getOrderProvince": "山西省",
            "getOrderCity": "临汾市",
            "getOrderPlate": "立恒本部",
            "getOrderPlateLat": "35.709562",
            "getOrderPlateLng": "111.432266",
            "goodTypeDesc": "线材",
            "goodsCode": "XC-300-10",
            "ifTaxTransport": "Y",
            "limitTime": 7,
            "loadingAddrCity": "临汾市",
            "loadingAddrProvince": "山西省",
            "prodDesc": "线材",
            "qty": 3,
            "ret1": "groupxs.jngcxh.com",
            "ret2": "20210721002",
            "ret3": "",
            "sender": "立恒厂库发货人-圆圆",
            "senderMobile": "0357-5528141",
            "startPlate": "立恒西二门",
            "startPlateLat": "35.709562",
            "startPlateLng": "111.432266",
            "takeGoodsType": "PS",
            "weight": 30
        },
        "dwCompanyId": 1001,
        "loginInfo": {
            "zz": "zz"
        },
        "platName": "www.jngcxh.com"
    }
    data1 = {
        "jsonParam": json.dumps(payload, ensure_ascii=False)
    }
    response = requests.post(url=url, data=data1)
    print(data1)
    print(response.text)
uploadPublish()
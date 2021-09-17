import requests
''' 永锋电商上传货源单
'''
def uploadPublish():
    url = 'http://116.228.222.130:28082/api/yongfeng/goodsUpload'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "platName": "yfwl.com",
            "userName": "test",
            "password": "test"
        },
        "dataInfo": [
            {
                "dependNum": "TD202007010011",
                "dependId": "TD202007010011",
                "getOrderCountry": "宝山区",
                "getOrderCountryCode": "310113",
                "getOrderPlate": "华滋奔腾大厦B101",
                "getOrderPlateLng": 111.432266,
                "getOrderPlateLat": 35.709562,
                "billTaker": "万强",
                "billTakerMobile": "15512345678",
                "loadingAddrCountry": "宝山区",
                "loadingAddrCountryCode": "310113",
                "startPlate": "华滋奔腾大厦B101",
                "startPlateLng": 111.432266,
                "startPlateLat": 35.709562,
                "sender": "陈利发单公司",
                "senderMobile": "13123456789",
                "dsCountryName": "曲沃县",
                "dsCountryCode": "141021",
                "dsAddress": "立恒新区",
                "receiver": "万强",
                "receiverMobile": "15512345678",
                "billSender": "李一帆",
                "billSenderMobile": "13212345678",
                "goodTypeDesc": "钢材",
                "prodDesc": "线材",
                "weight": 30,
                "qty": 5,
                "dsTransportPrice": 90,
                "amount": "1",
                "dsGoodsPrice": "1234",
                "appointType": "1",
                "appointCompanyCode": "JHM202002210002",
                "limitTime": "24",
                "ifTaxTransport": "Y",
                "interCode": "JHM200222000001",
                "robDeliveryType": "0",
                "takeGoodsType":"",
                "ifAgency":"0",
                "agencyRemark":"XX发票抬头",
                "ifShortDelivery":"1",
                "ifComplete": "Y",
                "remark": "第三方货主"
            }
        ]
    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
uploadPublish()
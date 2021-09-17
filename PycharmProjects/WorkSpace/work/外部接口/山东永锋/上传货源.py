import requests
import json

url = "http://10.0.161.37:20002/api/yongfeng/goodsUpload"
payload = json.dumps({
    "loginInfo": {
        "userName": "test",
        "password": "test",
        "platName": "yfwl.com"
    },
    "dataInfo": [
        {
            "dependNum": "2324799881997",
            "dependId": "2324799881997",
            "getOrderCountry": "宝山区",
            "getOrderCountryCode": "310113",
            "getOrderPlate": "华滋奔腾大厦",
            "getOrderPlateLng": "121.4090412184",
            "getOrderPlateLat": "31.3986226945",
            "billTaker": "丁前顺",
            "billTakerMobile": "19988886666",
            "loadingAddrCountry": "宝山区",
            "loadingAddrCountryCode": "310113",
            "startPlate": "华滋奔腾大厦",
            "startPlateLng": "121.4090412184",
            "startPlateLat": "31.3986226945",
            "sender": "丁丁丁",
            "senderMobile": 18566663333,
            "dsCountryName": "太原市",
            "dsCountryCode": 140105,
            "dsAddress": "太原小店区小店",
            "receiver": "丁丁",
            "receiverMobile": "18866661111",
            "billSender": "山东物泊测试货主",
            "billSenderMobile": "18500000033",
            "goodTypeDesc": "盘螺",
            "prodDesc": "一级",
            "weight": "30",
            "qty": "10000",
            "detachable": "0",
            "singleCarWeight": "0",
            "dsTransportPrice": "90",
            "amount": "2000",
            "takeMode": "0",
            "quoteLimit": "3",
            "periodTime": "1",
            "maxPrice": "110",
            "dsGoodsPrice": "4500",
            "appointType": "0",
            "appointCompanyCode": "0",
            "limitTime": "100",
            "ifTaxTransport": "Y",
            "interCode": "JHM210607100001",
            "robDeliveryType": "0",
            "takeGoodsType": "PS",
            "ifAgency": "0",
            "agencyRemark": "备注",
            "ifShortDelivery": "1",
            "ifComplete": "N",
            "remark": "保证金测试",
            "depositValidFlag": "1",
            "ifaudit": "谢焕星"
        }
    ]
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

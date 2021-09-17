import requests
''' 永锋电商返单量上传
'''
def outWeight():
    url = 'http://116.228.222.130:28082/api/yongfeng/outWeight'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "platName": "yfwl.com",
            "userName": "test",
            "password": "test"
        },
        "outInfo":[
            {
                "deliveryId":10012411,
                "dependId":"TD202004100000",
                "outWeight":"30",
                "outTime":"2020-04-10 10:34:65"
            }
        ]
    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
outWeight()
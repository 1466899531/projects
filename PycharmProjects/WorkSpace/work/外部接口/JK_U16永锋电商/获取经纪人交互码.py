import requests
''' 
    获取经纪人的交互码
'''
def code():
    url = 'http://116.228.222.130:28082/api/yongfeng/code'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo":{
            "userName":"test",
            "password":"test",
            "platName":"yfwl.com"
        },
        "queryInfo":{
            "type":"2",
            "name":"山东物泊经纪人1",
            "phone":"1391728000"
        }
    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
code()
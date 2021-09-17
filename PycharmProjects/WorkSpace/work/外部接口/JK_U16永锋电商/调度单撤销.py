import requests
''' 
    永锋电商调度单撤销
'''
def cancel():
    url = 'http://116.228.222.130:28082/api/yongfeng/cancel'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo":{
            "userName":"test",
            "password":"test",
            "platName":"yfwl.com"
        },
        "cancelInfo":{
            "dependId":"TD202003200000",
            "cancelType":"2"
        }
    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
cancel()
import requests
import json
''' 
    接口功能描述: 交互码查询
'''
def QueryCodeJHM():
    url = 'http://10.0.161.37:20002/api/yongfeng/code'
    heards = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com"
        },
        "queryInfo": {
            "type": "1",  # 1货主2经纪人
            "name": "山东齐河",
            "phone": "18588987898"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=heards)
    print(res.status_code)
    print(res.text)
QueryCodeJHM()

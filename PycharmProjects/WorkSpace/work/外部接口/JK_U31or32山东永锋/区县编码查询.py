import requests
import json
'''
    接口功能描述: 区县编码查询
'''
def QueryCode():
    url = 'http://10.0.161.37:20002/areaCode/query'
    heards = {'Content-Type': "application/json"}
    data = {
        "fatherKeyValue": "上海市",
        "keyValue": "浦东新区"
    }
    res = requests.post(url=url, data=json.dumps(data), headers=heards)
    print(res.status_code)
    print(res.text)
QueryCode()

import requests
import json
import random
'''
    接口功能描述: 中材电商货源单上传  bu_publish_api
'''
def PublishUpload():
    url = 'http://10.0.161.60:20002/api/zcds/goodsUpload'
    headers = {'Content-Type': "application/json"}
    depend = "CG_"+str(random.randint(1, 999999999))
    data = {
        "loginInfo":{
            "userName":"test",
            "password":"test",
            "platName":"zcds.com"
        },
        "dataInfo":{
            "dependId":depend,
            "dependNum":depend,
            "weight":"1000",
            "qty":"10",
            "sender":"测试谢焕星",
            "senderMobile":"13838339604",
            "goodTypeDesc":"钢材"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
PublishUpload()

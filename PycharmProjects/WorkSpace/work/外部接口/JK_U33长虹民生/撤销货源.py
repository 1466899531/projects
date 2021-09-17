import requests
'''
    接口功能描述: 四川长虹下发运单后，发现运单信息或配车信息有误可调用此接口撤销运单。
    传送数据格式：JSON
'''
def cancelPublish():
    url = 'http://10.0.161.37:20002/api/changhong/publish/cancel'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "changhong",
            "password": "changhong",
            "platName": "changhong.com"
        },
        "dataInfo":
            {
                "dependNum":"20210719004",
                "dependId":"20210719004"
            }

    }
    res = requests.post(url, json=data, headers=header)

    print(res.status_code)
    print(res.text)
cancelPublish()
import requests
import time
'''
    接口描述: 返量 (装收货)
'''
def OutWeight():
    url = 'http://10.0.161.60:20002/api/yongfeng/outWeight'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com.qh"
        },
        "outInfo": [
            {
                "deliveryId": "17157428",
                "dependId": "XS_QH_378078486",
                "outWeight": "34",
                "outTime": time.strftime("%Y-%m-%d %H:%M:%S"),  # 返单时间
                "entryTime": "2021-03-26 05:40:00",  # 进厂时间
                "publishType": "1",  # 1销售2采购默认1销售
                "zcWeight": "30",  # 装车量
                "zcTime": "2021-03-26 05:40:00",  # 装车时间
            }
        ]
    }
    res = requests.post(url, json=data, headers=header)

    print(res.status_code)
    print(res.text)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
OutWeight()

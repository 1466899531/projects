import requests
import json
'''
    接口功能描述: 永锋车辆定位查询
'''
def VehicleGps():
    url = 'http://10.0.161.37:20002/api/yongfeng/vehicle/gps'
    headers = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com"
        },
        "dataInfo": {
            "deliveryId": "17157169",
            "vehicleNum": "豫A00006"
        }
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
VehicleGps()

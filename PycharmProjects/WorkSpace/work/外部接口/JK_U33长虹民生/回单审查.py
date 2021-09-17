import requests
'''
    接口功能描述 :当司机收货信息下发至四川长虹后，四川长虹对收货回单进行抽查不合格会调用此接口修改回单图片。
    传送数据格式：JSON
'''
def updatePic():
    url = 'http://10.0.161.60:20002/api/changhong/delivery/updatePic'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "changhong",
            "password": "changhong",
            "platName": "changhong.com"
        },
        "dataInfo":
            {
                "dependNum":"0000312063",
                "dependId":"0000312063",
                "deliveryId":"18935562",    # 派车单id
                "deliveryPic":"https://jxwy-csoss.oss-cn-hangzhou.aliyuncs.com/202107/ios_c44672cc58f54d80bba3d5cebd3be483.jpg"    # 收货回单 (可空)
            }

    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
updatePic()


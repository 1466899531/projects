import time
import requests

'''
    接口功能描述: 四川长虹物流向物泊物流发起付款指令，支持一单包含N笔支付指令，所有支付金额以长虹物流提供的金额为准。
    传送数据格式：JSON
'''


def payment():
    url = 'http://10.0.161.60:20002/api/changhong/delivery/payment'
    header = {'Content-Type': "application/json"}
    data = {
        "dataInfo": {
            "carNum": 1,
            "deliveryId": "18935376",
            "dependId": "YD202108170048365",
            "dependNum": "0000312063",
            "payAmount": 100,
            "payOrderId": "2c9998b1-814c-4156-8180-c3d1b6faf64f",
            "payType": "1",
            "payeeBankName": "中国农业发展银行",
            "payeeBankNo": "6212262308004263328",
            "payeeName": "高火凤凰",
            "payeeNo": "513436200111088955"
        },
        "loginInfo": {
            "password": "changhong",
            "platName": "changhong.com",
            "userName": "changhong"
        }
    }
    res = requests.post(url, json=data, headers=header)

    print(res.status_code)
    print(res.text)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))


payment()

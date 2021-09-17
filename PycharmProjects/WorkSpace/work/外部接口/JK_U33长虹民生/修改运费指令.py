import time
import requests
'''
    接口功能描述: 四川长虹物流向物泊物流支付指令后，在物泊客服实际支付之前或物泊支付失败后可调用此接口修改本次支付信息。
    传送数据格式：JSON
'''
def updatePayment():
    url = 'http://10.0.161.60:20002/api/changhong/delivery/updatePayment'
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
                "dependId":"YD202108170048365",
                "deliveryId":"18935376",
                "payOrderId":"2c9998b1-814c-4156-8180-c3d1b6faf69f" # 支付唯一ID  (支付金额/收款人姓名/收款人身份证/收款人银行卡/收款人银行名称 可空)

            }

    }
    res = requests.post(url, json=data, headers=header)

    print(res.status_code)
    print(res.text)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
updatePayment()
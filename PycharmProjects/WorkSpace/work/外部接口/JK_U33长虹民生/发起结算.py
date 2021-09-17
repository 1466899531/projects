import requests
'''
    90的调度单才可调用这个接口
    接口功能描述: 四川长虹物流向物泊物流发起结算指令，完结调该调度单，所有支付金额以长虹物流提供的金额为准。
    传送数据格式：JSON
'''
def settle():
    url = 'http://10.0.161.37:20002/api/changhong/delivery/settle'
    header = {'Content-Type': "application/json"}
    data = {
        "loginInfo": {
            "userName": "changhong",
            "password": "changhong",
            "platName": "changhong.com"
        },
        "dataInfo":
            {
                "dependNum":"20210719001",
                "dependId":"20210719001",
                "deliveryId":"18928332",
                "doneAmount":"1000"  # 已支付金额
            }

    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
settle()
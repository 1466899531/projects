import requests
import json
import random
'''
    接口功能描述: 立恒大宗货源单上传
'''
def sendCgOrder():
    url = 'http://116.228.222.130:28082/tmsapi/json/sendCgOrder.jsp'
    headers = {'Content-Type': 'application/json'}
    depend = "_" + str(random.randint(1, 999999999))
    data = {
        "loginInfo": {
            "customerId": "gaoyi",
            "password": "gaoyi"
        },
        "dataInfo": [
            {
                "dependNum": "C-20200904101",  # 业务单号
                "logisticsMark": "C",
                "weight": "300",  # 重量
                "qty": "999.5",  # 数量
                "price": "100",  # 单价
                "amount": "5000",  # 总价
                "goodTypeDesc": "钢管",  # 货物种类
                "prodTypeDesc": "测试发货人",  # 货物描述
                "remark": "立恒老大宗",  # 备注
                "sender": "徐海祥",  # 委托人
                "senderMobile": "17500000049",  # 委托人联系电话
                "ret1": "dzwlgy.software",  # 域名
                "ret2": "产地",  # 产地
                "wlOperatorId": "",  # 操作员id
                "wlOperatorName": "",  # 操作员姓名
                "levelFlag": "",  # 操作员级别
                "ifPayment": "",  # 是否贷款支付
                "goodsPrice": 7000,  # 货物单价
                "ifPayType": "",  # 公私户
                "bankName": "",  # 银行名称
                "bankNo": "",  # 银行卡号
                "bankUserName": "",  # 银行卡姓名
                "bankProvince": "",  # 开户省
                "bankCity": "",  # 开户市
                "bankSubName": "",  # 支行名
                "bankSubNo": ""  # 支行号
            }
        ]
    }
    data1 = {
        "jsonParam": json.dumps(data, ensure_ascii=False)
    }
    res = requests.post(url=url, data=data1, headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
sendCgOrder()

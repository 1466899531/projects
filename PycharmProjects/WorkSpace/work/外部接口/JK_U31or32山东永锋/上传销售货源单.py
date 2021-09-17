import requests
import json
import random
'''
    接口功能描述: 销售货源上传 bu_publish
'''
def XsGoodsUpload():
    url = 'http://10.0.161.37:20002/api/yongfeng/goodsUpload'
    heard = {'Content-Type': "application/json"}
    depend = "XS_LG_"+str(random.randint(1, 999999999))
    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com.qh" # lg:临港,qh:齐河
        }, "dataInfo": [
            {
                "dependNum": depend,  # 电商的业务单据号，可重复 不可空
                "dependId": depend,  # 电商的业务单据唯一识别号，不可重复  不可空
                "getOrderCountry": "宝山区",  # 取单地  不可空
                "getOrderCountryCode": "310113",  # 取单地区县编码 不可空
                "getOrderPlate": "华滋奔腾大厦",  # 取单地 不可空
                "getOrderPlateLng": "121.4090412184",  # 取单地度经 可空
                "getOrderPlateLat": "31.3986226945",  # 取单地纬度 可空
                "billTaker": "丁前顺",  # 取单联系人 不可空
                "billTakerMobile": "19988886666",  # 取单联系人电话  不可空
                "loadingAddrCountry": "宝山区",  # 装货地区县  不可空
                "loadingAddrCountryCode": "310113",  # 装货地区县编码 不可空
                "startPlate": "华滋奔腾大厦",  # 装货地 不可空
                "startPlateLng": "121.4090412184",  # 装货地经度 可空
                "startPlateLat": "31.3986226945",  # 装货地纬度  可空
                "sender": "丁丁丁",  # 装货联系人 不可空
                "senderMobile": "18566663333",  # 装货联系人电话 不可空
                "dsCountryName": "容城县",  # 收货地区县 不可空
                "dsCountryCode": "130629",  # 收货地区县编码 不可空
                "dsAddress": "平王乡",  # 收货地地址 不可空
                "receiver": "丁丁",  # 收货联系人 不可空
                "receiverMobile": "18866661111",  # 收货联系人电话 不可空
                "billSender": "山东物泊测试货主",  # 委托人 不可空
                "billSenderMobile": "18500000033",  # 委托人电话 不可空
                "goodTypeDesc": "盘螺",  # 货物类型 不可空
                "prodDesc": "一级",  # 货物品种描述 不可空
                "weight": "30",  # 重量 不可空
                "qty": "10000",  # 数量 不可空
                "detachable": "0",  # 拆单标记  0不拆单(默认)，1拆单 不可空
                "singleCarWeight": "30",  # 拆单的单车重量 可空
                "dsTransportPrice": "43",  # 单价时为最低价
                "amount": "3000",  # 包车时为最低价
                "takeMode": "1",  # 0抢单，1报价（默认0）（仅支持不可拆单的）
                "quoteLimit": "3",  # 报价次数
                "periodTime": "1",  # 时效（分钟）必须大于等于一分钟（报价模式必填）
                "maxPrice": "150",  # 最高运价
                "dsGoodsPrice": "4500",  # 货物平均单价 不可空
                "appointType": "0",  # 定向类型0：不定向（定向默认组），1:定向经纪人， 3：定向给司机
                "appointCompanyCode": "0",  # 0：不需要该值  1：经纪人的交互码，物泊物流提供 3:司机手机号
                "limitTime": "100",  # 有效时间
                "ifTaxTransport": "Y",  # N：不含税，Y：含税，
                "interCode": "JHM210618100001",  # 委托方交互码
                "robDeliveryType": "0",  # 调度方式 0：按车抢单，1：按量抢单
                "takeGoodsType": "PS",  # 提货方式 PS：配送，ZT：自提
                "ifAgency": "0",  # 是否代收代付 0：否，1：是
                "agencyRemark": "备注",  # 代收代付备注
                "ifShortDelivery": "1",  # 0非短导 1短导
                "ifComplete": "N",  # Y：包车，N：单价
                "remark": "报价测试",  # 备注
                "depositValidFlag": "1",
                "ifAudit": "1",  # 0税率1差价
                "carQuantity": "3"
            }
        ]}
    res = requests.post(url=url, data=json.dumps(data), headers=heard)
    print(res.status_code)
    print(res.text)
    print(depend)
XsGoodsUpload()

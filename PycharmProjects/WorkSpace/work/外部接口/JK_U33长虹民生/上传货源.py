
from common.base import BaseTest

''' 长虹上传货源单 (只有销售货源)
    接口功能描述 : 四川长虹客户做好配载计划后，四川长虹会调用物泊物流的接口，将运单信息发送到物泊物流平台接收，56生成相应的货源单
    传送数据格式：JSON
'''


class UploadPublish(BaseTest):
    """ 上传货源 """

    def uploadPublish(self, dependId, goodTypeDesc):
        url = 'http://10.0.161.60:20002/api/changhong/publish/upload'
        header = {'Content-Type': "application/json"}
        data = {
            "loginInfo": {  # 登录参数
                "userName": "changhong",  # 用户名 bu_api_url
                "password": "changhong",  # 密码   bu_api_url
                "platName": "changhong.com"  # 平台交互域名 bu_api_url
            },
            "dataInfo": [  # 收货单信息
                {
                    "dependNum": dependId,  # 业务单据号 (长虹物流的客户编码，可重复)
                    "dependId": dependId,  # 业务单据ID (长虹物流yd提货单号，唯一识别号，不可重复。抢单时要带至调度单的提货单)
                    "getOrderCountry": "宝山区",  # 取单地区县 (取单地的最后一级区县，例：涵江区)
                    "getOrderCountryCode": "460400",  # 取单地区县编码 (区县对应的国家区划代码，若有将优先使用)
                    "getOrderPlate": "淞南一村",  # 取单地 (取单地的详细地址)
                    "getOrderPlateLng": "31.4102790000",  # 取单地经度 20位
                    "getOrderPlateLat": "121.4965630000",  # 取单地纬度 20位
                    "billTaker": "宋永取单人",  # 取单联系人
                    "billTakerMobile": "15090650001",  # 取单联系人电话
                    "loadingAddrCountry": "宝山区",  # 装货地区县
                    "loadingAddrCountryCode": "620200",  # 装货地区县编码
                    "startPlate": "淞南一村",  # 装货地
                    "startPlateLng": "31.4102790000",  # 装货地经度
                    "startPlateLat": "121.4965630000",  # 装货地纬度
                    "sender": "宋永发货人",  # 装货联系人
                    "senderMobile": "15090650002",  # 装货联系人电话
                    "dsCountryName": "浦东新区",  # 收货地区县
                    "dsCountryCode": "620200",  # 收货地区县编码
                    "dsAddress": "金葵佳苑",  # 收货地的详细地址
                    "receiver": "宋永收货人",  # 收货联系人
                    "receiverMobile": "15090650003",  # 收货联系人电话
                    "billSender": "宋永委托人",  # 委托人 (可以是货主名称)
                    "billSenderMobile": "15090650004",  # 委托人电话 (与装货人一致)
                    "goodTypeDesc": goodTypeDesc,  # 货物类型 (56平台对应的货物分类)
                    "prodDesc": "H型钢",  # 货物品种描述 (具体的货物名称或描述)
                    "weight": "30",  # 重量 (默认1)
                    "price": "10",  # 运费单价 (默认8000)
                    "interCode": "JHM210712100002",  # 委托方交互码 (56平台提供，代表着56平台的货主账号)长虹民生 / 111111
                    "ownerOrgan": "万强部门2",  # 委托方部门 (物泊上委托方的部门名陈)
                    "carrierCarryMode": "0",  # 承运模式 (1代表计划模式，0代表单车模式)
                    "ifComplete": "Y",  # 是否整车 (Y整车计算，N单价计算)
                    "platName": "changhong.com",  # 平台交互域名
                    # "remark":"自定义", # 备注字段
                    "ownerUser": "谢焕星3",  # 操作员
                    "ownerUserPhone": "13838339604"  # 操作员手机号
                }
            ]
        }
        res = self.post_json(url, data, header)
        result = str(res.json()["outResultReason"])

        if result.__eq__("成功!"):
            return dependId
        else:
            print(res.text)

    """ 维护品种 """

    @staticmethod
    def catalog_num():
        catalog_list = ["煤炭及制品", "石油、天然气及制品", "金属矿石", "钢铁", "矿建材料", "水泥", "木材", "非金属矿石", "化肥及农药", "盐", "粮食", "机械、设备、电器",
                        "轻工原料及制品", "有色金属", "轻工医药产品", "鲜活农产品", "冷藏冷冻货物", "商品汽车", "其他"]
        return catalog_list


""" 测试 """
if __name__ == '__main__':
    # depend_list=[]
    # for catalog in UploadPublish.catalog_num():
    #     depend = "YW"+str(random.randint(100000,1000000))
    #     depend_list.append(depend)
    #     UploadPublish().uploadPublish(depend,catalog)
    # print(depend_list)

    # depend = "YW"+str(random.randint(100000,1000000))
    depend = "YW11117"
    catalog = "煤炭及制品"
    print(UploadPublish().uploadPublish(depend, catalog))

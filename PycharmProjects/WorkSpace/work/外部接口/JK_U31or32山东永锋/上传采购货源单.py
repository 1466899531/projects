import requests
import json
import random
'''
    接口功能描述: 山东永锋采购货源单上传  bu_publish_api
'''
def CgPublishUpload():
    url = 'http://10.0.161.37:20002/api/yongfeng/publishUpload'
    headers = {'Content-Type': "application/json"}
    depend = "CG_LG_"+str(random.randint(1, 999999999))
    data = {
        "loginInfo": {
            "userName": "test",
            "password": "test",
            "platName": "sdwb.com.lg" # lg:临港JK_U32,qh:齐河 JK_U31
        },
        "dataInfo": [{
            "dependNum": depend,
            "dependId": depend,
            "weight": "90",
            "qty": "1000",
            "goodsPrice": "4500",
            "price": "100",
            "goodTypeDesc": "钢材",
            "remark": "",
            "sender": "山东供销平台对接",
            "senderMobile": "18599890077",
            "interCode": "JHM210618100001",
            "publishType": "2", # 货源类型 (1销售 2采购)
            "startPlateProvince": "上海市",
            "startPlateCity": "上海市",
            "startPlateCountry": "浦东新区",
            "startPlate": "华虹创新园",
            "dsProvinceName": "北京市",
            "dsCityName": "北京市",
            "dsCountryName": "朝阳区",
            "dsAddress": "天安门广场",
            "receiver": "收货人",
            "receiverMobile": "18599998888",
            "clienter": "委托人",
            "clienterMobile": "18500006655",
        }]
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(res.status_code)
    print(res.text)
    print(depend)
CgPublishUpload()

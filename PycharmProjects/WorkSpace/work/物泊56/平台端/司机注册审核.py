import random
from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.物泊56.app端.安卓.司机注册 import DriverRegister
from work.物泊56.平台端.平台端登录 import ManagerLogin

class DriverAudit(BaseTest):

    """ 平台端-司机注册审核管理数据查询 """
    def query_DriverAudit(self,phone):
        url = self.get_manager_url("/api/user/rgtDriverAudit/queryDriverAudit")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data ={
            "phone":phone,
            "page":0,
            "sizePerPage":10,
            "sort":[
                "loginId"
            ],
            "order":[
                "DESC"
            ]
        }
        response_query_DriverAudit = self.post_json(url,data,header)
        if response_query_DriverAudit.json()["content"]:
            if str(response_query_DriverAudit.json()["content"][0]["phone"]) == phone:
                loginName = str(response_query_DriverAudit.json()["content"][0]["loginName"])
                print("\033[32m司机注册审核列表查询成功,司机登录名为: "+str(loginName))
                return str(loginName)
        else:
            raise Exception("\033[31m司机注册审核列表未查询到该司机")

    """ 平台端-司机车辆审核管理(领用待审核司机) """
    def update_take(self,phone,auditType=1):
        url = self.get_manager_url("/api/user/driver/take")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {"phone":phone,"type":auditType}
        response_update_take = self.post_json(url,data,header)
        if response_update_take.json()["code"] == 0:
            print("\033[32m搜索司机成功: "+phone)
            return True
        else:
            raise print("\033[31m搜索司机失败,失败原因为: "+response_update_take.text)

    """ 平台端-司机车辆审核管理(搜索司机) """
    def query_searchAuditDriver(self,loginName):
        url = self.get_manager_url("/api/user/rgtDriverAudit/searchAuditDriver")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {"loginName":loginName}
        response_query_searchAuditDriver = self.post_json(url,data,header)
        print()
        if response_query_searchAuditDriver:
            return response_query_searchAuditDriver.json()["loginId"]
        else:
            raise print("\033[31m搜索司机失败,失败原因为: "+response_query_searchAuditDriver.text)

    """ 平台端-司机车辆审核管理(保存修改信息) """
    def update_save(self,loginId,phone,auditType=2):
        url = self.get_manager_url("/api/user/driver/new/save")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {
            "loginId":loginId,
            "type":auditType,
            "auditStatus":1,
            "driverMust":{
                "avatarPic":"202107/WBKJ_6977e40469c441679dbc00c0c7a9d65e.jpg",
                "driverName":"陈洲洋",
                "sex":"男",
                "phone":phone,
                "national":"汉",
                "birthDay":583862400000,
                "address":"安徽省宿州市泗县草沟镇沟陈村沟陈庄043号",
                "idNum":"342225198807044915",
                "issueauthority":"泗县公安局",
                "limitBegDate":1156780800000,
                "limitEndDate":1472400000000,
                "quasiDrivingType":"A2",
                "licenceIdNo":"142723198408224115",
                "occupPic":"202107/WBKJ_82d4a2fd0f354e6c9647b2e8a9a2da55.jpg",
                "licencePic":"202107/WBKJ_adb90daa6bcd41fca47771eeed776f2c.jpg",
                "signaturePic":"202107/WBKJ_e9087baac1d3463c886be67ef500fa77.jpg",
                "idFontPic":"202107/WBKJ_9afaea184ed64b90aec2082759168fb4.jpg",
                "idBackPic":"202107/WBKJ_99afd4a9269a492c8f6d9c8b1cf060e8.jpg",
                "occupNum":"14723695"
            },
            "driverOpt":{
                "licenceIssuingAuthority":"Python脚本审核",
                "licenceEffeBegDate":1422028800000,
                "licenceEffeEndDate":1611417600000,
                "licenceDrawDate":1043337600000,
                "licenceFileNo":"888888",
                "occupNum":"14723695",
                "remark":""
            },
            "vehicleMust":{
                "vehicleNum":"豫A8380A",
                "vehicleStyleCode":"Q11",
                "contactPerson":"郑州兆通物流有限公司",
                "tonnage":25,
                "totalTonnage":8805,
                "useNature":"货运",
                "vehicleEnergyType":"B",
                "annualDate":1585670400000,
                "ifHandCar":0,
                "zcCardPic":"202107/WBKJ_b7fc4adb406d42a4ab1b1b225cbbb422.jpg",
                "zcTransPic":"202107/WBKJ_0c0b0a30de1d4da3993f43684fe33118.jpg",
                "vehiclePic":"202107/WBKJ_ec14520183814f2f87c86ce80e7846cc.jpg",
                "vehicleLicenseCode":"2",
                "carAxle":"6*2",
                "roadTransNo":"1466899531",
                "contactMobile":"13838330001",
                "engineNo":"53158189",
                "vehicleIdentificationCode":"LFWSR6PL6KLA05102"
            },
            "vehicleOpt":{
                "vehicleUserPic":"202107/WBKJ_82d4a2fd0f354e6c9647b2e8a9a2da55.jpg",
                "lvesConfigId":"",
                "nuclearTonnage":"40",
                "handCarNo":"",
                "licenseNum":"410101120472",
                "zcRegistrationDate":"2019-04-24",
                "zcCertificationDate":"2019-04-24",
                "zcIssuingAuthority":"河南省信阳市鸡公山",
                "approvePeople":"2",
                "vehicleTonnage":25000,
                "outToOut":"7200×2500×2820mm",
                "meter":7.2,
                "tractionMassTonnage":"",
                "endRetirementRemark":"强制报废期止:2034-04-24",
                "brandModel":"解放牌CA4255K2E5R5T1A9",
                "gcCardPic":"",
                "gcTransPic":"",
                "hazardousVehiclePic":"",
                "hazardousTransPic":""
            }
        }
        response_update_save = self.post_json(url,data,header)
        if response_update_save.json()["code"] == 0:
            print("\033[32m保存修改司机信息成功: "+phone)
            return True
        else:
            raise print("\033[31m保存修改司机信息失败,失败原因为: "+response_update_save.text)

    """ 平台端-司机车辆审核管理(审核通过) """
    def audit_pass(self,loginId,phone,auditStatus,auditType=2): # 司机状态(2待审核,4司机修改,5车辆修改,6司机车辆修改)
        occupNum = random.randint(9999999,100000000) # 随机生成从业资格证号
        url = self.get_manager_url("/api/user/driver/new/pass")
        header = {
        'Content-Type':'application/json',
        'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {
            "loginId":loginId,
            "type":auditType,
            "auditStatus":auditStatus,
            "driverMust":{
                "avatarPic":"202107/WBKJ_6977e40469c441679dbc00c0c7a9d65e.jpg",
                "driverName":"陈洲洋",
                "sex":"男",
                "phone":phone,
                "national":"汉",
                "birthDay":583862400000,
                "address":"安徽省宿州市泗县草沟镇沟陈村沟陈庄043号",
                "idNum":"342225198807044915",
                "issueauthority":"泗县公安局",
                "limitBegDate":1156780800000,
                "limitEndDate":1472400000000,
                "quasiDrivingType":"A2",
                "licenceIdNo":"142723198408224115",
                "occupPic":"202107/WBKJ_82d4a2fd0f354e6c9647b2e8a9a2da55.jpg",
                "licencePic":"202107/WBKJ_adb90daa6bcd41fca47771eeed776f2c.jpg",
                "signaturePic":"202107/WBKJ_e9087baac1d3463c886be67ef500fa77.jpg",
                "idFontPic":"202107/WBKJ_9afaea184ed64b90aec2082759168fb4.jpg",
                "idBackPic":"202107/WBKJ_99afd4a9269a492c8f6d9c8b1cf060e8.jpg",
                "occupNum":occupNum
            },
            "driverOpt":{
                "licenceIssuingAuthority":"Python脚本审核",
                "licenceEffeBegDate":1422028800000,
                "licenceEffeEndDate":1611417600000,
                "licenceDrawDate":1043337600000,
                "licenceFileNo":"888888",
                "occupNum":occupNum,
                "remark":""
            },
            "vehicleMust":{
                "vehicleNum":"豫A8380A",
                "vehicleStyleCode":"Q11",
                "contactPerson":"郑州兆通物流有限公司",
                "tonnage":25,
                "totalTonnage":8805,
                "useNature":"货运",
                "vehicleEnergyType":"B",
                "annualDate":1585670400000,
                "ifHandCar":0,
                "zcCardPic":"202107/WBKJ_b7fc4adb406d42a4ab1b1b225cbbb422.jpg",
                "zcTransPic":"202107/WBKJ_0c0b0a30de1d4da3993f43684fe33118.jpg",
                "vehiclePic":"202107/WBKJ_ec14520183814f2f87c86ce80e7846cc.jpg",
                "vehicleLicenseCode":"2",
                "carAxle":"6*2",
                "roadTransNo":"1466899531",
                "contactMobile":"13838330001",
                "engineNo":"53158189",
                "vehicleIdentificationCode":"LFWSR6PL6KLA05102"
            },
            "vehicleOpt":{
                "vehicleUserPic":"202107/WBKJ_82d4a2fd0f354e6c9647b2e8a9a2da55.jpg",
                "lvesConfigId":"",
                "nuclearTonnage":40,
                "handCarNo":"",
                "licenseNum":"410101120472",
                "zcRegistrationDate":"2019-04-24",
                "zcCertificationDate":"2019-04-24",
                "zcIssuingAuthority":"河南省信阳市鸡公山",
                "approvePeople":"2",
                "vehicleTonnage":25000,
                "outToOut":"7200×2500×2820mm",
                "meter":7.2,
                "tractionMassTonnage":"",
                "endRetirementRemark":"强制报废期止:2034-04-24",
                "brandModel":"解放牌CA4255K2E5R5T1A9",
                "gcCardPic":"",
                "gcTransPic":"",
                "hazardousVehiclePic":"",
                "hazardousTransPic":""
            }
        }
        response_audit_pass = self.post_json(url,data,header)
        if response_audit_pass.json()["code"] == 0:
            print("\033[32m司机审核成功: "+phone)
            driver_val_status = SqlTest.run_query_sql(SqlHome.query_driver_sql(phone))[0]["val_status"]
            if driver_val_status ==1:
                print("\033[32m司机状态变生效 "+ str(driver_val_status))
        else:
            raise print("\033[31m司机审核失败,失败原因为: "+response_audit_pass.text)

    """ 串联业务 """
    @staticmethod
    def auditDriver_all(result_phone):
        driverAudit = DriverAudit()
        if driverAudit.update_take(result_phone):
            login_id = driverAudit.query_searchAuditDriver(driverAudit.query_DriverAudit(result_phone))
            if driverAudit.update_save(login_id,result_phone):
                driverAudit.audit_pass(login_id,result_phone,auditStatus=1) # 审核状态(1审核通过,2审核不通过)

""" 测试 """
if __name__ == '__main__':
    print("\033[34m----------------平台司机注册审核开始-----------------------")
    managerTk = ManagerLogin().managerLogin("admin", "111111")
    DriverAudit.auditDriver_all(DriverRegister.registerDriver_all("13838330001","a12345"))
    print("\033[34m----------------平台司机注册审核结束-----------------------")


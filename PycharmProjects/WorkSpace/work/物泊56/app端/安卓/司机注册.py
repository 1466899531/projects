#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib import parse
from urllib.request import urlopen
from urllib import request
from common.base import BaseTest
from common.fileUtil import FileUtils
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.物泊56.app端.苹果.司机登录 import DriverLogin

""" 司机注册 """
class DriverRegister(BaseTest):

    """ 发送注册短信 """
    def registerDriver_sendMessage(self, mobile):
        url = self.get_app_url("/sendMessage/register")
        payload = {
            "mobile": mobile
        }
        response_send_message = self.post_json(url, payload)
        if response_send_message.text.__contains__("\"code\":0"):
            print("\033[32m注册短信验证码发送成功")
            return True
        else:
            print("\033[31m注册短信验证码发送失败,失败原因 : " + response_send_message.text)

    """ 注册司机 """
    def registerDriver(self, mobile,password,code,plat_source="WBKJ"):
        url = self.get_app_url('/register/registerUser')
        payload = {
            "mobile": mobile,
            "password": password,
            "type": 1,
            "referrer": "Python脚本",
            "verifyCode": code,
            "deviceInfo": {
                "platSource": plat_source
            }
        }
        response_register_user = self.post_json(url, payload)
        if response_register_user.text.__contains__("\"code\":0"):
            print("\033[32m司机注册成功,请完善信息")
            return True
        else:
            print("\033[31m司机注册失败,请重新注册!失败原因: " + response_register_user.text)

    """ 注册密码校验 """
    def registerDriver_checkLoginPassword(self,password):
        url = self.get_app_url('/checkLoginPassword')
        payload = {
            "password": password
        }
        response_registerDriver_checkLoginPassword = self.post_json(url, payload)
        if response_registerDriver_checkLoginPassword.text.__contains__("\"code\":0"):
            print("\033[32m司机两次输入密码一致")
            return True
        else:
            print("\033[31m司机两次输入密码不一致,请重新输入密码!失败原因: " + response_registerDriver_checkLoginPassword.text)

    """ 上传司机注册图片 """
    def registerDriver_uploadPic(self, pic_type, file_path, header, if_hand_car=0,plat_source='WBKJ'):
        url = self.get_app_url('/pro/user/driver/driverUploadPictureRegister')
        payload = {
            "picType": pic_type,
            "deviceInfo.platSource": plat_source,
            "deviceInfo.platform": "3"
        }
        file = {"file": open(file_path, 'rb')}
        if pic_type == "4":
            payload["ifHandCar"] = if_hand_car
        response_registerDriver_uploadPic = self.post(url, data=payload, header=header,file=file)
        if response_registerDriver_uploadPic.status_code == 200:
            print("\033[32m上传图片成功,图片类型为: " + pic_type)
            return response_registerDriver_uploadPic
        else:
            print("\033[31m上传图片失败!失败原因: " + response_registerDriver_uploadPic.text + str("图片种类: " + pic_type))

    """ 保存司机信息 """
    def registerDriver_saveRgtMessage(self, driver_name,id_num,avatarPicUrl,idFontPicUrl,idBackPicUrl,header):
        url = self.get_app_url('/pro/user/driver/saveOrUpdateRgtDriver')
        payload = {
            "referrer": "Python脚本",
            "driverName": driver_name,
            "address": "安徽省宿州市泗县草沟镇沟陈村沟陈庄043号",
            "birthDay": "1988-07-03",
            "issueauthority": "泗县公安局",
            "limitBegDate": "2006-08-29",
            "limitEndDate": "2016-08-29",
            "national": "汉",
            "idNum": id_num,
            "sex": "男",
            "avatarPic": avatarPicUrl,
            "idFontPic": idFontPicUrl,
            "idBackPic": idBackPicUrl
        }
        response_registerDriver_saveRgtMessage = self.post_json(url, payload,header)
        if response_registerDriver_saveRgtMessage.text.__contains__("\"code\":0"):
            print("\033[32m保存司机信息成功")
            return True
        else:
            print("\033[31m保存司机信息失败!失败原因: " + response_registerDriver_saveRgtMessage.text)

    """ 数据宝 """
    @staticmethod
    def cdp_1():
        url = 'http://api.chinadatapay.com/government/traffic/9696'
        payload ={
            "key":"cb56e7089678236c3a1967241d43af52",
            "plateNumber":"豫A8380A",
            "type":""
        }
        params = parse.urlencode(payload).encode('utf-8')
        request1 = request.Request(url, params)
        response = urlopen(request1)
        print(response.read().decode())

    def neibu(self,vehicleNum):
        url = self.get_app_url('/cdp/recognize')
        payload ={
            "vehicleNum":vehicleNum # 车牌号
        }
        response_neibu = self.post(url, data=payload)
        print(response_neibu.json())

    """ 数据宝 """
    def cdp(self,vehicleNum):
        url = 'http://api.chinadatapay.com/government/traffic/9696'
        payload ={
            "key":"cb56e7089678236c3a1967241d43af52", # 您申请的API的key值
            "plateNumber":vehicleNum, # 车牌号
            "type":""  # 不填默认返回所有车辆信息)
        }
        response_cdp = self.post(url, data=payload)
        if response_cdp.json()["code"] == '10000':
            print("\033[32m调用数据宝成功 :"+str(response_cdp.json()))
        else:
            print("\033[31m调用数据宝失败!失败原因: " + response_cdp.text)

    """ 串联业务 """
    @staticmethod
    def registerDriver_all(phone,password):
        data = SqlTest.run_query_sql(SqlHome.queryLoginData_sql(phone))
        if data:
            login_id = str(data.__getitem__(0)["login_id"])
            SqlTest.run_delete_sql(SqlHome.delLoginUser_sql(login_id))
            SqlTest.run_delete_sql(SqlHome.delRgtDriverByLoginID_sql(login_id))
            SqlTest.run_delete_sql(SqlHome.delRgtVehicle_sql(login_id))
            if data.__getitem__(0)["login_name"] == phone:
                SqlTest.run_delete_sql(SqlHome.delLoginUserByLoginName_sql(phone))
        if DriverRegister().registerDriver_sendMessage(phone):
            if DriverRegister().registerDriver_checkLoginPassword(password):
                code = SqlTest.run_queryMessageCode_sql(SqlHome.queryMessageCode_sql(phone))
                SqlTest.run_delete_sql(SqlHome.delDriverByPhone_sql(phone))
                if DriverRegister().registerDriver(phone,password,code):
                    cookie_headers = {
                        "tk":DriverLogin().driver_login(phone,password)  # 司机登录,取Cookie
                    }
                    response_registerDriver_uploadPic_1 = DriverRegister().registerDriver_uploadPic('1', FileUtils.get_FilePath(1),cookie_headers)
                    driverName = (response_registerDriver_uploadPic_1.json()["data"]["driverName"]) # 取司机姓名
                    idNum = (response_registerDriver_uploadPic_1.json()["data"]["idNum"]) # 取司机身份证号
                    avatarPicUrl = (response_registerDriver_uploadPic_1.json()["data"]["avatarPic"]) # 取司机身份证小头像
                    idFontPicUrl = response_registerDriver_uploadPic_1.json()["data"]["idFontPic"] # 取司机身份正面
                    response_registerDriver_uploadPic_2 =DriverRegister().registerDriver_uploadPic('2', FileUtils.get_FilePath(2),cookie_headers)
                    idBackPicUrl = response_registerDriver_uploadPic_2.json()["data"]["idBackPic"] # 取司机身份反面
                    DriverRegister().registerDriver_uploadPic('3', FileUtils.get_FilePath(3),cookie_headers)
                    DriverRegister().registerDriver_uploadPic('4', FileUtils.get_FilePath(4),cookie_headers)
                    data = SqlTest.run_query_sql(SqlHome.queryLoginData_sql(phone))
                    vehicleNum = SqlTest.run_query_sql(SqlHome.query_rgtVehicleNum_sql(data[0]["login_id"]))[0]["vehicle_num"]
                    # DriverRegister().neibu(vehicleNum)
                    DriverRegister().cdp(vehicleNum)
                    DriverRegister().registerDriver_uploadPic('5', FileUtils.get_FilePath(5),cookie_headers)
                    DriverRegister().registerDriver_uploadPic('6', FileUtils.get_FilePath(6),cookie_headers)
                    DriverRegister().registerDriver_uploadPic('11', FileUtils.get_FilePath(11),cookie_headers)
                    DriverRegister().registerDriver_uploadPic('13', FileUtils.get_FilePath(13),cookie_headers)
                    SqlTest.run_delete_sql(SqlHome.delRgtDriver_sql(idNum, driverName))
                    SqlTest.run_delete_sql(SqlHome.delDriver_cert_d_sql(idNum))
                    SqlTest.run_delete_sql(SqlHome.delDriver_cert_sql(idNum))
                    SqlTest.run_delete_sql(SqlHome.delDriverByIdNum_sql(idNum))
                    DriverRegister().registerDriver_saveRgtMessage(driverName,idNum,avatarPicUrl,idFontPicUrl,idBackPicUrl,cookie_headers)
                    # DriverRegister().registerDriver_uploadPic('9',File.get_FilePath(9,1),1) # 挂车道路运输证
                    # DriverRegister().registerDriver_uploadPic('10',File.get_FilePath(10,1),1)# 挂车行驶证
                    data = SqlTest.run_query_sql(SqlHome.query_auditStatus_sql(phone))
                    if data.__getitem__(0)["audit_status"] ==1 and data.__getitem__(0)["audited_status"] ==1:
                        print("\033[32m注册完成,登录平台进行司机审核,手机号为: "+phone)
                        return phone
                    else:
                        raise print("\033[31m司机或者车辆的审核状态不正确")

""" 测试 """
if __name__ == '__main__':
    print("\033[34m------------------------司机注冊开始-----------------------------------")
    DriverRegister.registerDriver_all("13838330001","a12345")
    DriverRegister().cdp("豫A8380A")
    print("\033[34m------------------------注冊完成,开始审核----------------------------")
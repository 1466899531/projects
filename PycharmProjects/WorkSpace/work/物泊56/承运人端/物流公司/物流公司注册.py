from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome


class LogisRegister(BaseTest):
    """ 发送注册短信 """
    def send_message(self,phone):
        url = self.get_app_url("/sendMessage/operatorRegister")
        payload = {
            "mobile": phone
        }
        response_send_message = self.post_json(url, payload)
        if response_send_message.text.__contains__("\"code\":0"):
            print("\033[32m注册短信验证码发送成功")
            return True
        else:
            raise print("\033[31m注册短信验证码发送失败,失败原因 : " + response_send_message.text)
    """ 判断用户名是否被注册 """
    def check_loginName(self, loginName):
        url = self.get_app_url("/register/checkLoginNameFlag")
        payload = {
            "loginName": loginName,
            "type": "3"
        }
        response_check_loginName = self.post_json(url, payload)
        if response_check_loginName.text.__contains__("\"code\":0"):
            print("\033[32m用户名合法")
            return True
        else:
            raise print("\033[31m用户名不合法,失败原因 : " + response_check_loginName.text)
    """ 提交物流公司注册请求 """
    def register_logis(self, logisName,loginName,password,phone,verifyCode):
        url = self.get_app_url("/register/registerLogis")
        payload = {
            "logisName": logisName,
            "taxNum": "1234567",
            "contactPerson": "谢焕星",
            "mobile": phone,
            "verifyCode": verifyCode,
            "provinceCode": "河北省",
            "cityCode": "唐山市",
            "countryCode": "路南区",
            "address": "逸仙路",
            "businessLicensePic": "201911/app_821375fbf5f14f79bf9058e7c6528a7b.jpg",
            "roadTransPic": "201911/app_3a39faa9256c437fa2e122aa44bd4b3e.jpg",
            "roadTrasnsNum": "12345678",
            "loginName": loginName,
            "password": password,
            "type": 3
        }
        response_register_logis = self.post_json(url,payload)
        if response_register_logis.text.__contains__("\"code\":0"):
            print("\033[32m物流公司注册成功-------"+ logisName+"----登录名: "+loginName)
            return True
        else:
            raise print("\033[31m物流公司注册失败,失败原因 : " + response_register_logis.text)
    """ 物流公司注册 """
    @staticmethod
    def registerLogis_all():
        phone = '13838330002'
        logisName = '巴乐兔'
        loginName = 'xhxwlgs'
        password = '111111'
        if LogisRegister().send_message(phone):
            SqlTest.run_delete_sql(SqlHome.delRgtLogisByLoginName_sql(loginName))
            SqlTest.run_delete_sql(SqlHome.delRgtLogisByLogisName_sql(logisName))
            SqlTest.run_delete_sql(SqlHome.delLoginUserByLoginName_sql(loginName))
            SqlTest.run_delete_sql(SqlHome.delLogis_sql(logisName))
        if LogisRegister().check_loginName(loginName):
            if LogisRegister().register_logis(logisName, loginName, password, phone, SqlTest.run_queryMessageCode_sql(SqlHome.queryMessageCode_sql(phone))):
                audit_status = SqlTest.run_query_sql(SqlHome.queryLogisAuditStatus__sql(logisName))[0]['audit_status']
                if audit_status == 1:
                    print("\033[34m------------------------物流公司注冊完成,开始审核-----------------------------------")
                    return logisName
                else:
                    raise print("\033[31m物流公司不是待审核状态")
if __name__ == '__main__':
    print("\033[34m------------------------物流公司注冊开始-----------------------------------")
    LogisRegister.registerLogis_all()

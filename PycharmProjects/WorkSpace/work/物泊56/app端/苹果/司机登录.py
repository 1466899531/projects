from common.base import BaseTest

class DriverLogin(BaseTest):

    """ 司机登录 """
    def driver_login(self,username,password):
        url = self.get_app_url("/login")
        header = {
            'Content-Type': 'application/json'
        }
        data = {
            "authType":0,
            "username":username,
            "password":password,
            "deviceInfo":{
                "latitude":31.25072419,
                "longitude":121.63090162,
                "platform":2,
                "model":"iPhone XR",
                "sdkVersion":"14.6",
                "language":"ch",
                "brand":"iPhone",
                "cameraAuthorized":0,
                "version":"3.2.4",
                "locationAuthorized":0,
                "imeiCode":"C8B5495A-04C0-406B-A88B-92774E0195BB"
            }
        }
        response_driverLogin = self.post_json(url, data, header)
        if response_driverLogin.json()["data"]:
            print("\033[32m司机登录成功-----------------------------"+username+"")
            return response_driverLogin.json()["data"]["tk"]
        else:
            raise print("\033[31m司机登录失败,失败原因: "+response_driverLogin.text)

""" 测试 """
if __name__ == '__main__':
    print("\033[34m--------------------司机开始登录-----------------------")
    driverTk = DriverLogin().driver_login("16630702259","111111")
    print(driverTk)

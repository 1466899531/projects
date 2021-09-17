from common.base import BaseTest

class CarrierLogin(BaseTest):

    """ 经纪人登录 """
    def carrier_login(self,username,password):
        url = self.get_carrier_url("/login")
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
        response_carrierLogin = self.post_json(url, data, header)
        if response_carrierLogin.json()["data"]:
            print("\033[32m经纪人登录成功----------------------"+username)
            return response_carrierLogin.json()["data"]["tk"]
        else:
            raise print("\033[31m经纪人登录失败,失败原因: "+response_carrierLogin.text)


if __name__ == '__main__':
    print("\033[34m--------------------经纪人开始登录-----------------------")
    carrierTk = CarrierLogin().carrier_login("谢焕星-JJR","111111")
    print(carrierTk)

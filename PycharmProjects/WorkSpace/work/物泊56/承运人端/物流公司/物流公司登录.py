from common.base import BaseTest

class LogisLogin(BaseTest):

    """ 物流公司登录 """
    def logis_login(self,username,password):
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
        response_logisLogin = self.post_json(url, data, header)
        if response_logisLogin.json()["data"]:
            print("\033[32m物流公司登录成功----------------------"+username)
            return response_logisLogin.json()["data"]["tk"]
        else:
            raise print("\034[31m物流公司登录失败,失败原因: "+response_logisLogin.text)


if __name__ == '__main__':
    print("\033[34m--------------------物流公司开始登录-----------------------")
    logisTk = LogisLogin().logis_login("xhxwlgs","111111")
    print(logisTk)

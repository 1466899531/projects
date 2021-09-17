from common.base import BaseTest

class OwnerLogin(BaseTest):

    """ 货主登录 """
    def ownerLogin(self,username,password):
        url = self.get_consignor_url("/api/login")
        header = {
            'Content-Type':'application/json'
        }
        data = {
            'username':username,
            'password':password,
            'verKey':'36131246-6d97-4d88-ba06-a3e03c1096b9',
            'verCode':'1'
        }
        response_ownerLogin = self.post_json(url,data,header)
        if response_ownerLogin.json():
            print("\033[32m货主登录成功-----"+username)
            return response_ownerLogin.json()["id"]
        else:
            raise print("\033[31m货主登录失败,失败原因为: "+response_ownerLogin.text)


if __name__ == '__main__':
    print("\033[34m--------------------货主开始登录-----------------------")
    ownerTk = OwnerLogin().ownerLogin("hxhz","111111")
    print(ownerTk)
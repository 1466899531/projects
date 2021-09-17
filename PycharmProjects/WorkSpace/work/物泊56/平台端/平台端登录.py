from common.base import BaseTest

class ManagerLogin(BaseTest):
    """ 参数初始化 """
    def __init__(self):
        self.username = "admin"
        self.password = "111111"
    """ 平台端登录 """
    def managerLogin(self,username,password):
        url = self.get_manager_url("/api/login")
        header = {
            'Content-Type':'application/json'
        }
        data = {
            'username':username,
            'password':password,
            'verKey':'36131246-6d97-4d88-ba06-a3e03c1096b9',
            'verCode':'1'
        }
        response_managerLogin = self.post_json(url,data,header)
        if response_managerLogin.json():
            print("\033[32m平台登录成功")
            return response_managerLogin.json()["id"]
        else:
            raise print("\033[31m平台登录失败,失败原因为: "+response_managerLogin.text)


if __name__ == '__main__':
    print("\033[34m--------------------平台开始登录-----------------------")
    managerTk = ManagerLogin().managerLogin("admin","111111")
    print(managerTk)
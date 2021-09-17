import requests

""" 公用基类 """
class BaseTest:
    session = requests.session()
    app_url = 'http://10.0.161.60:9980/v1'
    manager_url = "http://test-web-manager.ubor56.com"
    consignor_url = "http://test-web-consignor.ubor56.com"
    carrier_url = "http://test-web-carrier.ubor56.com"

    """ 获取APP接口URL """
    def get_app_url(self, url):
        return self.app_url + url

    """ 获取平台端接口URL """
    def get_manager_url(self, url):
        return self.manager_url + url

    """ 获取货主端接口URL """
    def get_consignor_url(self, url):
        return self.consignor_url + url

    """ 获取承运人端接口URL """
    def get_carrier_url(self, url):
        return self.carrier_url + url

    """ post请求-上传文件 """
    def post(self, url, data=None, header=None, file=None, timeout=10):
        response = self.session.post(url, data=data, headers=header, files=file, timeout=timeout)
        if response:
            return response
        else:
            raise Exception("\033[31m请求出错,响应为空!!!")

    """ post请求-json格式 """
    def post_json(self, url, data=None, header=None, file=None, timeout=10):
        response = self.session.post(url, json=data, headers=header, files=file, timeout=timeout)
        if response.status_code == 200 or response.status_code == 400:
            return response
        else:
            raise Exception("\033[31m请求出错,响应为空!!!"+str(url))

    """ get请求 """
    def get(self, url, data=None, header=None, time=10):
        response = self.session.get(url, params=data, headers=header, timeout=time, stream=True)
        if response:
            return response
        else:
            raise Exception("\033[31m请求出错,响应为空!!!")


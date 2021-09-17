import os
import pickle
import requests

from jd_spider_config.SpiderConfig import global_config

"""
    Session相关操作
"""
class SpiderSession:

    def __init__(self):
        self.cookies_dir_path = "E:\jd_maotai\jd_spider_session\jd_spider.cookies"
        self.user_agent = global_config.getRaw('config', 'DEFAULT_USER_AGENT')
        self.session = self._init_session()

    """
        初始化session
    """
    def _init_session(self):
        session = requests.session()
        session.headers = self.get_headers()
        return session

    """
        获取请求头配置信息
    """
    def get_headers(self):
        return {"User-Agent": self.user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;"
                          "q=0.9,image/webp,image/apng,*/*;"
                          "q=0.8,application/signed-exchange;"
                          "v=b3",
                "Connection": "keep-alive"}
    """
        获取请求头配置信息 -userAgent
    """
    def get_user_agent(self):
        return self.user_agent

    """
        获取当前Session
    """
    def get_session(self):
        return self.session

    """
        获取当前Cookies
    """
    def get_cookies(self):
        return self.session.cookies

    """
        设置传入cookies
    """
    def set_cookies(self, cookies):
        self.session.cookies.update(cookies)

    """
        从本地加载Cookie
    """
    def load_cookies_from_local(self):
        cookies_file = ''
        if not os.path.exists(self.cookies_dir_path):
            return False
        for name in os.listdir(self.cookies_dir_path):
            if name.endswith(".cookies"):
                cookies_file = '{}{}'.format(self.cookies_dir_path, name)
                break
        if cookies_file == '':
            return False
        with open(cookies_file, 'rb') as f:
            local_cookies = pickle.load(f)
        self.set_cookies(local_cookies)

    """
        保存Cookie到本地。cookie_file_name: 存放Cookie的文件名称
    """
    def save_cookies_to_local(self, cookie_file_name):
        cookies_file = '{}{}.cookies'.format(self.cookies_dir_path, cookie_file_name)
        directory = os.path.dirname(cookies_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(cookies_file, 'wb') as f:
            pickle.dump(self.get_cookies(),f)
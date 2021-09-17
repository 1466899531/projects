import os
import configparser

"""
    配置类,获取配置信息 。该类的作用是使用配置文件生效，配置文件的格式和windows的INI文件的格式相同
"""


class AppiumConfig(object):
    def __init__(self, config_file='E:\\PycharmProjects\\WorkSpace\\work\\APPIUM自动化\\appium_config\\config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("找不到指定文件: config.ini")
        # 这两行代码和下面两行代码实现的功能相同
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')

        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    """
        根据key取配置文件的value
    """

    def get(self, section, name):
        return self._config.get(section, name)

    """
       根据key取配置文件的value
   """

    def get_raw(self, section, name):
        return self._configRaw.get(section, name)


# 生成全局配置类对象
global_config = AppiumConfig()

# -*- coding:utf-8 -*-
import time
import requests

from datetime import datetime
from jd_spider_config.SpiderConfig import global_config
from jd_spider_logger.SpiderLogger import logger
from jd_spider_util.SpiderUtil import num_to_str_data, str_data_to_num


class SpiderTime(object):
    def __init__(self, sleep_interval=0.5):
        self.buy_time = global_config.getRaw('config', 'buy_time').__str__()
        # 本地时间
        self.sleep_interval = sleep_interval
        self.local_jd_time_diff = self.get_local_jd_time_diff()
        self.local_time = self.get_local_time()
        self.jd_time = self.get_jd_time()


    """
        从京东服务器获取时间毫秒
    """
    @staticmethod
    def get_jd_time():
        return int(requests.get(global_config.getRaw('jdSpiderUrl','jd_serverTimeUrl')).json()["currentTime2"])
    """
        获取本地毫秒时间
    """
    @staticmethod
    def get_local_time():
        return int(round(time.time() * 1000))

    """
        获取本地毫秒时间和京东服务器毫秒时间差
    """
    def get_local_jd_time_diff(self):
        return self.get_local_time() - self.get_jd_time()

    """
        定时开始执行抢货
    """
    def start(self):
        logger.info('正在等待到达设定时间:{}，检测本地时间与京东服务器时间误差为【{}】毫秒'.format(self.buy_time, self.local_jd_time_diff))
        while True:
            if (self.local_time + 1000) >= self.jd_time and self.local_time >= str_data_to_num(self.buy_time):
                logger.info('时间到达, 开始执行……')
                break
            else:
                logger.info('抢购时间未到达, 请耐心等待……')
                time.sleep(self.sleep_interval)

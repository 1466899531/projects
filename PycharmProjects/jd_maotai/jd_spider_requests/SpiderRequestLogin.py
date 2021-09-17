import json
import random
import time

import requests
from jd_spider_config.SpiderConfig import global_config
from jd_spider_exception.SpiderException import SpiderException
from jd_spider_logger.SpiderLogger import logger
from jd_spider_session.SpiderSession import SpiderSession
from jd_spider_util.SpiderUtil import response_status, save_image, open_image, parse_json

class SpiderRequestLogin:
    """
        扫码登录
    """
    def __init__(self,spider_session: SpiderSession):
        """
        初始化扫码登录
        大致流程：
            1、访问登录二维码页面，获取Token
            2、使用Token获取票据
            3、校验票据
        """
        self.qrcode_img_file = 'E:\PycharmProjects\jd_maotai\jd_spider_pic\jd_登录二维码.jpg'
        self.spider_session = spider_session
        self.session = self.spider_session.get_session()
        self.is_login = False  # 默认是未登录
        self.refresh_login_status()
    """
        刷新是否登录状态
    """
    def refresh_login_status(self):
        self.is_login = self._validate_cookies()

    """
        验证cookies是否有效（是否登陆）通过访问用户订单列表页进行判断：若未登录，将会重定向到登陆页面。cookies是否有效 True/False
    """
    def _validate_cookies(self):
        url = global_config.getRaw('jdSpiderUrl','jd_orderListUrl')
        payload = {
            'rid': str(int(time.time() * 1000)),
        }
        try:
            # 不允许重定向
            resp = self.session.get(url=url, params=payload, allow_redirects=False)
            if resp.status_code == requests.codes.OK:
                return True
        except Exception as e:
            logger.error("验证cookies是否有效发生异常", e)
        return False
    """
        获取PC端登录页面
    """
    def _get_login_page(self):
        url = global_config.getRaw('jdSpiderUrl','jd_loginUrl')
        page = self.session.get(url, headers=self.spider_session.get_headers())
        return page

    """
       缓存并展示登录二维码
    """
    def _get_qrcode(self):
        url = global_config.getRaw('jdSpiderUrl','jd_loginQrCodeUrl')
        payload = {
            'appid': 133,
            'size': 147,
            't': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': global_config.getRaw('config','DEFAULT_USER_AGENT'),
            'Referer': global_config.getRaw('jdSpiderUrl','jd_loginUrl')
        }
        resp = self.session.get(url=url, headers=headers, params=payload)
        if not response_status(resp):
            logger.info('获取二维码失败')
            return False
        save_image(resp, self.qrcode_img_file)
        logger.info('二维码获取成功，请打开京东APP扫描')
        open_image(self.qrcode_img_file)
        return True
    """
        通过token获取票据，校验二维码
    """
    def _get_qrcode_ticket(self):
        url = global_config.getRaw('jdSpiderUrl','jd_loginQrCodeCheckUrl')
        payload = {
            'appid': '133',
            'callback': 'jQuery{}'.format(random.randint(1000000, 9999999)),
            'token': self.session.cookies.get('wlfstk_smdl'),
            '_': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': self.spider_session.get_user_agent(),
            'Referer': global_config.getRaw('jdSpiderUrl','jd_loginUrl')
        }
        resp = self.session.get(url=url, headers=headers, params=payload)
        if not response_status(resp):
            logger.error('获取二维码扫描结果异常')
            return False
        resp_json = parse_json(resp.text)
        if resp_json['code'] != 200:
            logger.info('Code: %s, Message: %s', resp_json['code'], resp_json['msg'])
            return None
        else:
            logger.info('已完成手机客户端确认')
            return resp_json['ticket']
    """
        通过已获取的票据进行校验。ticket: 已获取的票据
    """
    def _validate_qrcode_ticket(self, ticket):
        url = global_config.getRaw('jdSpiderUrl','jd_ValidationUrl')
        headers = {
            'User-Agent': self.spider_session.get_user_agent(),
            'Referer': global_config.getRaw('jdSpiderUrl','jd_logoutUrl')
        }
        response = self.session.get(url=url, headers=headers, params={'t': ticket})
        if not response_status(response):
            return False
        resp_json = json.loads(response.text)
        if resp_json['returnCode'] == 0:
            return True
        else:
            logger.info('票据校验失败：'+str(resp_json))
            return False

    """
       二维码登陆
    """
    def login_by_qrcode(self):
        self._get_login_page()
        # 下载京东登录二维码
        if not self._get_qrcode():
            raise SpiderException('京东登录二维码下载失败')
        # 获取登录票据
        ticket = None
        retry_times = 85
        for _ in range(retry_times):
            ticket = self._get_qrcode_ticket()
            if ticket:
                break
            time.sleep(2)
        else:
            raise SpiderException('京东登录二维码过期，请重新获取扫描')

        # 对获取到的票据进行校验
        if not self._validate_qrcode_ticket(ticket):
            raise SpiderException('京东登录二维码信息校验失败')
        self.refresh_login_status()
        logger.info('二维码登录成功')

if __name__ == '__main__':
    SpiderRequestLogin(SpiderSession()).login_by_qrcode()
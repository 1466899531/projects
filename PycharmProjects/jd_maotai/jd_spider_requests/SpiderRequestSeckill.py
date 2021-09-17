import datetime
import functools
import random
import time
from concurrent.futures import ProcessPoolExecutor

from dateutil.parser import parse
from lxml import etree
from jd_spider_config.SpiderConfig import global_config
from jd_spider_exception.SpiderException import SpiderException
from jd_spider_logger.SpiderLogger import logger
from jd_spider_requests.SpiderRequestLogin import SpiderRequestLogin
from jd_spider_session.SpiderSession import SpiderSession
from jd_spider_time.SpiderTime import SpiderTime
from jd_spider_util.SpiderUtil import parse_json, wait_some_time, send_wechat, response_status, str_data_to_num, \
    num_to_str_data, getDiffTime, compareTime, splitTime


class SpiderRequestSeckill(object):

    def __init__(self):
        self.spider_session = SpiderSession()
        self.spider_session.load_cookies_from_local()
        self.qrCodeLogin = SpiderRequestLogin(self.spider_session)
        # 初始化信息
        self.sku_id = global_config.getRaw('config', 'sku_id')
        self.seckill_num = 2
        self.seckill_init_info = dict()
        self.seckill_url = dict()
        self.seckill_order_data = dict()
        self.spiderTime = SpiderTime()
        self.session = self.spider_session.get_session()
        self.user_agent = self.spider_session.user_agent
        self.nick_name = None
    """
        二维码登陆
    """
    def login_by_qrcode(self):
        if self.qrCodeLogin.is_login:
            logger.info('登录成功')
            return
        self.qrCodeLogin.login_by_qrcode()
        if self.qrCodeLogin.is_login:
            self.nick_name = self.get_username()
            self.spider_session.save_cookies_to_local(self.nick_name)
        else:
            raise SpiderException("二维码登录失败！")
    """
        获取用户信息
    """
    def get_username(self):
        url = global_config.getRaw('jdSpiderUrl', 'jd_getUserInfoUrl')
        payload = {
            'callback': 'jQuery{}'.format(random.randint(1000000, 9999999)),
            '_': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': self.user_agent,
            'Referer': global_config.getRaw('jdSpiderUrl', 'jd_orderListUrl')
        }
        resp = self.session.get(url=url, params=payload, headers=headers)
        try_count = 5
        while not resp.text.startswith("jQuery"):
            try_count = try_count - 1
            if try_count > 0:
                resp = self.session.get(url=url, params=payload, headers=headers)
            else:
                break
            wait_some_time()
        # 响应中包含了许多用户信息，现在在其中返回昵称
        # jQuery2381773({"imgUrl":"//storage.360buyimg.com/i.imageUpload/xxx.jpg","lastLoginTime":"","nickName":"xxx","plusStatus":"0","realName":"xxx","userLevel":x,"userScoreVO":{"accountScore":xx,"activityScore":xx,"consumptionScore":xxxxx,"default":false,"financeScore":xxx,"pin":"xxx","riskScore":x,"totalScore":xxxxx}})
        return parse_json(resp.text).get('nickName')
    """
       用户登陆态校验装饰器。若用户未登陆，则调用扫码登陆
    """
    def check_login(func):
        @functools.wraps(func)
        def new_func(self, *args, **kwargs):
            if not self.qrCodeLogin.is_login:
                logger.info("{0} 需登陆后调用，开始扫码登陆".format(func.__name__))
                self.login_by_qrcode()
            return func(self, *args, **kwargs)
        return new_func

    @check_login
    def reserve(self):
        self._reserve()
    """
       预约
    """
    def _reserve(self):
        while True:
            try:
                self.make_reserve()
                break
            except Exception as e:
                logger.info('预约发生异常!', e)
            wait_some_time()
    """
        商品预约
    """
    def make_reserve(self):
        logger.info('商品名称:{}'.format(self.get_sku_title()))
        url = global_config.getRaw("jdSpiderUrl", "jd_yuShouUrl")
        payload = {
            'callback': 'fetchJSON',
            'sku': self.sku_id,
            '_': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': self.user_agent,
            'Referer': (global_config.getRaw("jdSpiderUrl", "jd_getItemTitleUrl")).format(self.sku_id),
        }

        resp = self.session.get(url=url, params=payload, headers=headers)
        resp_json = parse_json(resp.text)
        reserve_url = resp_json.get('url')  # 预约URL
        reserve_info = resp_json.get('info')  # 预约状态
        reserve_yueStime = resp_json.get('yueStime')  # 预约开始时间
        reserve_yueEtime = resp_json.get('yueEtime')  # 预约结束时间
        while True:
            now = splitTime(num_to_str_data(self.spiderTime.local_time))[1]
            yueEndTime = splitTime(reserve_yueEtime)[1]
            if compareTime(now,yueEndTime):
                logger.info('今天预约时间已过，请明天【'+splitTime(reserve_yueEtime)[0]+'】号再进行预约')
                break
            else:
                while True:
                    if self.spiderTime.local_time < str_data_to_num(reserve_yueStime):
                        nowTime = num_to_str_data(self.spiderTime.local_time)
                        logger.info(
                            "预约状态【" + reserve_info + "】,预约开始时间为【" + reserve_yueStime + "】,当前时间为【" + nowTime + "】,【" + str(getDiffTime(
                                nowTime, reserve_yueStime)) + "】分钟后开始预约。继续等待预约,每0.5毫秒循环一次判断直至预约时间到达")
                        time.sleep(0.5)
                    else:
                        logger.info('预约开始时间【' + reserve_yueStime + '】已到，开始预约')
                        # self.spiderTime.start()
                        self.reserve_goods(reserve_url)
                        break
    """
        循环预约商品
    """
    def reserve_goods(self, reserve_url):
        while True:
            try:
                response = self.session.get(url='https:' + reserve_url, allow_redirects=False)
                if response_status(response):
                    logger.info('预约成功，已获得抢购资格 / 您已成功预约过了，无需重复预约')
                    if global_config.getRaw('messenger', 'enable') == 'true':
                        success_message = "预约成功，已获得抢购资格 / 您已成功预约过了，无需重复预约"
                        send_wechat(success_message)
                    break
            except Exception as e:
                logger.error('预约失败正在重试...', e)
                time.sleep(0.5)
    """
        获取商品名称
    """
    def get_sku_title(self):
        url = (global_config.getRaw("jdSpiderUrl", "jd_getItemTitleUrl")).format(
            global_config.getRaw('config', 'sku_id'))
        resp_content = self.session.get(url).content
        x_data = etree.HTML(resp_content)
        sku_title = x_data.xpath('/html/head/title/text()')
        return sku_title[0]

    @check_login
    def seckill(self):
        self._seckill()
    """
       抢购
    """
    def _seckill(self):
        while True:
            try:
                self.request_seckill_url()
                while True:
                    self.request_seckill_checkout_page()
                    self.submit_seckill_order()
            except Exception as e:
                logger.info('抢购发生异常，稍后继续执行！', e)
            wait_some_time()
    """
        访问商品的抢购链接（用于设置cookie等
    """
    def request_seckill_url(self):
        logger.info('用户:{}'.format(self.get_username()))
        logger.info('商品名称:{}'.format(self.get_sku_title()))
        self.spiderTime.start()
        self.seckill_url[self.sku_id] = self.get_seckill_url()
        logger.info('访问商品的抢购连接...')
        headers = {
            'User-Agent': self.user_agent,
            'Host': 'marathon.jd.com',
            'Referer': (global_config.getRaw("jdSpiderUrl", "jd_getItemTitleUrl")).format(self.sku_id),
        }
        self.session.get(
            url=self.seckill_url.get(
                self.sku_id),
            headers=headers,
            allow_redirects=False)

    """
        获取商品的抢购链接
        点击"抢购"按钮后，会有两次302跳转，最后到达订单结算页面
        这里返回第一次跳转后的页面url，作为商品的抢购链接
        :return: 商品的抢购链接
    """
    def get_seckill_url(self):
        url = global_config.getRaw('jdSpiderUrl', 'jd_seckillUrl')
        payload = {
            'callback': 'jQuery{}'.format(random.randint(1000000, 9999999)),
            'skuId': self.sku_id,
            'from': 'pc',
            '_': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': self.user_agent,
            'Host': 'itemko.jd.com',
            'Referer': (global_config.getRaw("jdSpiderUrl", "jd_getItemTitleUrl")).format(self.sku_id),
        }
        while True:
            resp = self.session.get(url=url, headers=headers, params=payload)
            resp_json = parse_json(resp.text)
            if resp_json.get('url'):
                # https://divide.jd.com/user_routing?skuId=8654289&sn=c3f4ececd8461f0e4d7267e96a91e0e0&from=pc
                router_url = 'https:' + resp_json.get('url')
                # https://marathon.jd.com/captcha.html?skuId=8654289&sn=c3f4ececd8461f0e4d7267e96a91e0e0&from=pc
                seckill_url = router_url.replace(
                    'divide', 'marathon').replace(
                    'user_routing', 'captcha.html')
                logger.info("抢购链接获取成功: %s", seckill_url)
                return seckill_url
            else:
                logger.info("抢购链接获取失败，稍后自动重试")
                wait_some_time()
    """
        访问抢购订单结算页面
    """
    def request_seckill_checkout_page(self):
        logger.info('访问抢购订单结算页面...')
        url = global_config.getRaw("jdSpiderUrl", "jd_settleBillUrl")
        payload = {
            'skuId': self.sku_id,
            'num': self.seckill_num,
            'rid': int(time.time())
        }
        headers = {
            'User-Agent': self.user_agent,
            'Host': 'marathon.jd.com',
            'Referer': (global_config.getRaw("jdSpiderUrl", "jd_getItemTitleUrl")).format(self.sku_id),
        }
        self.session.get(url=url, params=payload, headers=headers, allow_redirects=False)
    """
        提交抢购（秒杀）订单
       :return: 抢购结果 True/False
    """
    def submit_seckill_order(self):
        url = global_config.getRaw("jdSpiderUrl", "jd_submitSeckillUrl")
        payload = {
            'skuId': self.sku_id,
        }
        try:
            self.seckill_order_data[self.sku_id] = self._get_seckill_order_data()
        except Exception as e:
            logger.info('抢购失败，无法获取生成订单的基本信息，接口返回:【{}】'.format(str(e)))
            return False

        logger.info('提交抢购订单...')
        headers = {
            'User-Agent': self.user_agent,
            'Host': 'marathon.jd.com',
            'Referer': (global_config.getRaw('jdSpiderUrl', 'jd_submitSeckillRefererUrl')).format(
                self.sku_id, self.seckill_num, int(time.time())),
        }
        resp = self.session.post(
            url=url,
            params=payload,
            data=self.seckill_order_data.get(
                self.sku_id),
            headers=headers)
        resp_json = None
        try:
            resp_json = parse_json(resp.text)
        except Exception as e:
            logger.info('抢购失败，返回信息:{}'.format(resp.text[0: 128]), e)
            return False
        # 返回信息
        # 抢购失败：
        # {'errorMessage': '很遗憾没有抢到，再接再厉哦。', 'orderId': 0, 'resultCode': 60074, 'skuId': 0, 'success': False}
        # {'errorMessage': '抱歉，您提交过快，请稍后再提交订单！', 'orderId': 0, 'resultCode': 60017, 'skuId': 0, 'success': False}
        # {'errorMessage': '系统正在开小差，请重试~~', 'orderId': 0, 'resultCode': 90013, 'skuId': 0, 'success': False}
        # 抢购成功：
        # {"appUrl":"xxxxx","orderId":820227xxxxx,"pcUrl":"xxxxx","resultCode":0,"skuId":0,"success":true,"totalMoney":"xxxxx"}
        if resp_json.get('success'):
            order_id = resp_json.get('orderId')
            total_money = resp_json.get('totalMoney')
            pay_url = 'https:' + resp_json.get('pcUrl')
            logger.info('抢购成功，订单号:{}, 总价:{}, 电脑端付款链接:{}'.format(order_id, total_money, pay_url))
            if global_config.getRaw('messenger', 'enable') == 'true':
                success_message = "抢购成功，订单号:{}, 总价:{}, 电脑端付款链接:{}".format(order_id, total_money, pay_url)
                send_wechat(success_message)
            return True
        else:
            logger.info('抢购失败，返回信息:{}'.format(resp_json))
            if global_config.getRaw('messenger', 'enable') == 'true':
                error_message = '抢购失败，返回信息:{}'.format(resp_json)
                send_wechat(error_message)
            return False
    """
        生成提交抢购订单所需的请求体参数
        :return: 请求体参数组成的dict
    """
    def _get_seckill_order_data(self):
        logger.info('生成提交抢购订单所需参数...')
        # 获取用户秒杀初始化信息
        self.seckill_init_info[self.sku_id] = self._get_seckill_init_info()
        init_info = self.seckill_init_info.get(self.sku_id)
        default_address = init_info['addressList'][0]  # 默认地址dict
        invoice_info = init_info.get('invoiceInfo', {})  # 默认发票信息dict, 有可能不返回
        token = init_info['token']
        data = {
            'skuId': self.sku_id,
            'num': self.seckill_num,
            'addressId': default_address['id'],
            'yuShou': 'true',
            'isModifyAddress': 'false',
            'name': default_address['name'],
            'provinceId': default_address['provinceId'],
            'cityId': default_address['cityId'],
            'countyId': default_address['countyId'],
            'townId': default_address['townId'],
            'addressDetail': default_address['addressDetail'],
            'mobile': default_address['mobile'],
            'mobileKey': default_address['mobileKey'],
            'email': default_address.get('email', ''),
            'postCode': '',
            'invoiceTitle': invoice_info.get('invoiceTitle', -1),
            'invoiceCompanyName': '',
            'invoiceContent': invoice_info.get('invoiceContentType', 1),
            'invoiceTaxpayerNO': '',
            'invoiceEmail': '',
            'invoicePhone': invoice_info.get('invoicePhone', ''),
            'invoicePhoneKey': invoice_info.get('invoicePhoneKey', ''),
            'invoice': 'true' if invoice_info else 'false',
            'password': global_config.get('account', 'payment_pwd'),
            'codTimeType': 3,
            'paymentType': 4,
            'areaCode': '',
            'overseas': 0,
            'phone': '',
            'eid': global_config.getRaw('config', 'eid'),
            'fp': global_config.getRaw('config', 'fp'),
            'token': token,
            'pru': ''
        }
        return data
    """
        获取秒杀初始化信息（包括：地址，发票，token）
        :return: 初始化信息组成的dict
    """
    def _get_seckill_init_info(self):
        logger.info('获取秒杀初始化信息...')
        url = global_config.getRaw('jdSpiderUrl', 'jd_getSeckillInfoUrl')
        data = {
            'sku': self.sku_id,
            'num': self.seckill_num,
            'isModifyAddress': 'false',
        }
        headers = {
            'User-Agent': self.user_agent,
            'Host': 'marathon.jd.com',
        }
        resp = self.session.post(url=url, data=data, headers=headers)

        resp_json = None
        try:
            resp_json = parse_json(resp.text)
        except Exception:
            raise SpiderException('抢购失败，返回信息:{}'.format(resp.text[0: 128]))

        return resp_json
    """
        多进程进行抢购
        work_count：进程数量
    """
    @check_login
    def seckill_by_proc_pool(self, work_count=5):
        with ProcessPoolExecutor(work_count) as pool:
            for i in range(work_count):
                pool.submit(self.seckill)

if __name__ == '__main__':
    SpiderRequestSeckill().login_by_qrcode()

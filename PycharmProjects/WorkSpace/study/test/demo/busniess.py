import datetime
import unittest

import Send_email as Send_email

from study.test.demo.testcase import *

class MyTestSuite(unittest.TestCase):
    # 获取sessionId
    def querySession(self):
        pass
    # 获取查询状态
    def queryStatus(self):
        pass
        # 具体写逻辑判断，单元测试代码
    def test_interface(self):
        # 初始化测试起始时间
        start_time = datetime.datetime.now()

        # 构造测试集
        suite = unittest.TestSuite()
        suite.addTest(MyTestSuite("querysession"))   # 获取sessionId
        suite.addTest(MyTestSuite("querystatus"))  # 获取登录状态


        # 执行测试
        runner = unittest.TextTestRunner()
        runner.run(suite)

        # 测试执行时间计算
        end_time = datetime.datetime.now()
        total_use_case = u"执行用例总数:" + str(num_success + num_fail) + \
                         u"\t通过数:" + str(num_success) + \
                         u"\t不通过数:" + str(num_fail)
        total_time = u"\t总共耗时：" + str((end_time-start_time).seconds) + u"秒"
        print_out(total_use_case + total_time)

        # 发生邮件测试报告
        Send_email.send_email(text)
from common.base import BaseTest
from work.APPIUM自动化.appium_log.AppiumLogger import logger


class UpdateCreatedDate(BaseTest):
    """修改调度单创建时间"""
    def update_created_date(self, delivery_id):
        url = self.get_app_url('/updateCreatedDate')
        payload = {
            "deliveryId": delivery_id
        }
        response = self.get(url, payload)
        logger.info("修改结果："+str(response.text))
# UpdateCreatedDate().update_created_date('18935376')

from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.物泊56.承运人端.物流公司.物流公司登录 import LogisLogin


class LogisController(BaseTest):

    """ 物流公司收纳车辆和司机 """
    def acceptDriverAndVehicle(self,driverId,vehicleId):
        url = self.get_app_url('/pro/user/broker/driver/acceptDriverAndVehicle')
        payload = {
            "driverId":driverId,
            "vehicleId": vehicleId
        }
        header = {
            'tk': logisTk
        }
        response_acceptVehicleAndDriver = self.post_json(url, payload,header)
        if response_acceptVehicleAndDriver.text.__contains__("\"code\":0"):
            print("\033[32m收纳成功")
        else:
            raise print("\033[31m"+response_acceptVehicleAndDriver.text)

    """ 串联业务 """
    @staticmethod
    def all():
        logisController =LogisController()
        data = SqlTest.run_query_sql(SqlHome.query_driverAndVehicle_sql(3))
        for result in data:
            driverId = result["driver_id"]
            vehicleId= result["vehicle_id"]
            logisController.acceptDriverAndVehicle(driverId,vehicleId)


if __name__ == '__main__':
    print("\033[34m------------------------物流公司开始操作-----------------------------------")
    logisTk = LogisLogin().logis_login("xhxwlgs","111111")
    LogisController.all()
    print("\033[34m------------------------物流公司操作完成-----------------------------------")

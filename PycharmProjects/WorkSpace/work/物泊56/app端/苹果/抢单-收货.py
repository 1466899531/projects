#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.物泊56.app端.苹果.司机登录 import DriverLogin


class DriverController(BaseTest):
    """ 查询登录司机信息 """
    def query_driverMessage(self):
        url = self.get_app_url("/userInfo")
        payload = {
            "deviceInfo": {
                "latitude": 0,
                "longitude": 0,
                "platform": 2,
                "model": "iPhone XR",
                "sdkVersion": "14.6",
                "language": "ch",
                "brand": "iPhone",
                "cameraAuthorized": 0,
                "version": "3.2.4",
                "locationAuthorized": 0,
                "imeiCode": "C8B5495A-04C0-406B-A88B-92774E0195BB"
            }
        }
        header = {
            'tk':driverTk
        }
        response = self.post_json(url, payload,header)
        if response.text.__contains__("\"code\":0"):
            print("\033[32m司机信息获取成功")
            return response.json()["data"]["userId"]
        else:
            raise print("\033[31m司机信息获取获取失败,失败原因 : " + response.text)

    """ 司机抢单确认页 """
    def driver_grabConfirmInfo(self,publishId):
        url = self.get_app_url("/pro/business/publish/carrier/grabConfirmInfo")
        payload = {
            "publishId":publishId,
            "deviceInfo":{
                "latitude":0,
                "longitude":0,
                "platform":2,
                "model":"iPhone XR",
                "sdkVersion":"14.6",
                "language":"ch",
                "brand":"iPhone",
                "cameraAuthorized":0,
                "version":"3.2.4",
                "locationAuthorized":0,
                "imeiCode":"C8B5495A-04C0-406B-A88B-92774E0195BB"
            }
        }
        header = {
            'tk':driverTk
        }
        response = self.post_json(url, payload,header)
        if response.text.__contains__("\"code\":0"):
            print("\033[32m抢单确认页信息获取成功")
            return response.json()["data"]["vehicleId"]
        else:
            print("\033[31m抢单确认页信息获取失败,失败原因 : " + response.text)

    """ 司机抢单 """
    def driver_grabBill(self,publishId,vehicleId):
        url = self.get_app_url("/pro/business/publish/carrier/grabBill")
        payload = {
            "vehicleId":vehicleId,
            "operateType":"APP",
            "ifZntsFlag":"0",
            "deviceInfo":{
                "latitude":0,
                "longitude":0,
                "platform":2,
                "model":"iPhone XR",
                "sdkVersion":"14.6",
                "language":"ch",
                "brand":"iPhone",
                "cameraAuthorized":0,
                "version":"3.2.4",
                "locationAuthorized":0,
                "imeiCode":"C8B5495A-04C0-406B-A88B-92774E0195BB"
            },
            "publishId":publishId,
            "specialVersion":1
        }
        header = {
            'tk':driverTk
        }
        response = self.post_json(url, payload,header)
        if response.text.__contains__("\"code\":0"):
            deliveryId =response.json()["data"]["deliveryId"]
            val_status = SqlTest.run_query_sql(SqlHome.query_delivery_valStatus_sql(deliveryId))[0]["val_status"]
            print("\033[32m司机抢单成功,调度单ID为 "+str(deliveryId)+" 状态为: "+str(val_status))
            return deliveryId
        else:
            raise print("\033[31m司机抢单失败,失败原因 : " + response.text)

    """ 收货之前修改调度单创建时间"""
    def update_delivery_createdTime(self,deliveryId):
        url = self.get_app_url('/updateCreatedDate')
        payload = {
            "deliveryId": deliveryId
        }
        response = self.get(url, payload)
        if response.text == "true":
            print("\033[32m修改时间成功"+response.text)
        else:
            raise print("\033[31m修改时间失败"+response.text)

    """ 司机取单 status:[ 20 取单,30 装车 ,90收货 ]"""
    def driver_changeStatus(self,status,deliveryId,picURl=None):
        url = self.get_app_url("/pro/business/delivery/changeStatus")
        payload = {
            "status":status,
            "deliveryId":deliveryId,
            "picType":"2",
            "deviceInfo":{
                "latitude":0,
                "longitude":0,
                "platform":2,
                "model":"iPhone XR",
                "sdkVersion":"14.6",
                "language":"ch",
                "brand":"iPhone",
                "cameraAuthorized":0,
                "version":"3.2.4",
                "locationAuthorized":0,
                "imeiCode":"C8B5495A-04C0-406B-A88B-92774E0195BB"
            },
            "picUrl":picURl
        }
        header = {
            'tk':driverTk
        }
        response = self.post_json(url, payload,header)
        if response.text.__contains__("\"code\":0"):
            if status == 20:
                val_status = SqlTest.run_query_sql(SqlHome.query_delivery_valStatus_sql(deliveryId))[0]["val_status"]
                print("\033[32m司机取单成功,状态为: "+str(val_status))
            if status == 30:
                val_status = SqlTest.run_query_sql(SqlHome.query_delivery_valStatus_sql(deliveryId))[0]["val_status"]
                print("\033[32m司机装车成功,状态为: "+str(val_status))
            if status == 90:
                val_status = SqlTest.run_query_sql(SqlHome.query_delivery_valStatus_sql(deliveryId))[0]["val_status"]
                print("\033[32m司机收货成功,状态为: "+str(val_status))
        else:
            if status == 20:
                raise print("\033[31m司机取单失败,失败原因 : " + response.text)
            if status == 30:
                raise print("\033[31m司机装车失败,失败原因 : " + response.text)
            if status == 90:
                raise print("\033[31m司机收货失败,失败原因 : " + response.text)

    """ 调度单回单上传 """
    def driver_upload_pic(self,file_path):
        url = self.get_app_url("/oss/uploadFile?platform=ios")
        payload = {}
        file = {
            "file": open(file_path,'rb')
        }
        header = {
                'tk':driverTk
            }
        response = self.post(url,payload,header,file)
        if response.text.__contains__("\"code\":0"):
            print("\033[32m回单图片地址: "+response.json()["data"])
            return response.json()["data"]
        else:
            raise print("\033[31m回单图片上传失败,失败原因为: "+response.text)

    """ 查询可以做业务的司机 """
    @staticmethod
    def query_driver():
        return SqlTest.run_query_sql(SqlHome().query_UseDriver_sql())

    """ 串联业务 """
    @staticmethod
    def graBill_to_take_all(publishId):
        driverController = DriverController()
        vehicleId = driverController.driver_grabConfirmInfo(publishId)
        driverId =driverController.query_driverMessage()
        SqlTest.run_update_sql(SqlHome.update_delivery_valStatus_byDriverId(driverId)) # 00已取消，05已终止，08预调度，10待取单，20待装货，30待收货，90已完成
        deliveryId = driverController.driver_grabBill(publishId,vehicleId)
        driverController.update_delivery_createdTime(deliveryId)
        driverController.driver_changeStatus(20,deliveryId) # 取单
        driverController.driver_changeStatus(30,deliveryId) # 装车
        picUrl =driverController.driver_upload_pic('C:/Users/xhx14/Desktop/所有文档/00-公司/00-02-脚本/脚本/python/WorkSpace/common/pic/qm.jpg')
        driverController.driver_changeStatus(90,deliveryId,picUrl) # 收货
""" 测试 """
if __name__ == '__main__':
    for driver in DriverController.query_driver():
        driverTk = DriverLogin().driver_login(driver["login_name"],driver["passwd"])
        DriverController.graBill_to_take_all("11713562")

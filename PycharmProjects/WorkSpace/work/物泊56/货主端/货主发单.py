from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.物泊56.货主端.货主登录 import OwnerLogin

class OwnerController(BaseTest):
    """ 货主发单 """
    # appointTeamType定向类型：1代表司机，2代表经纪人，3代表物流公司，4代表定向组，5代表不定向，6代表定向车辆
    # 1,appointTeamId传driverId
    # 2,appointTeamId传brokerID
    # 3,appointTeamId传logisID
    # 4,appointTeamId传定向组ID
    # 5,appointTeamId传0
    # detachable拆单标记：0代表不拆单，1代表需拆单
    # goods_insurance_flag货物险标记:0无，1有
    # goodsInsuranceFlagIf货物险是否收 : 0不收,1收
    # if_audit 0代表不需要平台审核(税率模式)，1代表需要平台审核(差价模式)
    def doPublish(self,detachable=1,appointTeamType=2,appointTeamId=10000053,goodsInsuranceFlag=0,goodsInsuranceFlagIf=1,if_audit=0):
        url = self.get_consignor_url("/api/business/publish/doPublish")
        header = {
            'Content-Type': "application/json",
            'Cookie':'CONSIGNOR-SESSION='+ownerTk
        }
        data = {
            "billPlate":"天安门",
            "startPlate":"颐和园",
            "endPlate":"大洋路市场",
            "billPlateLng":116.4038471062,
            "billPlateLat":39.9155256325,
            "startPlateLng":116.4224009777,
            "startPlateLat":39.9348272724,
            "endPlateLng":116.5189380081,
            "endPlateLat":39.8667819322,
            "biller":"毛泽东",
            "billerMobile":"13838339604",
            "sender":"八国联军",
            "senderMobile":"13838339604",
            "receiver":"高二",
            "receiverMobile":"13838339604",
            "catalogId":"10000003",
            "prodDesc":"槽钢",
            "goodPrice":3000,
            "weight":100,
            "qty":10,
            "startTakeDeliveryDate":1626785685000,
            "takeDeliveryDate":1626785686000,
            "detachable":detachable,
            "singleCarWeight":10,
            "valuMode":1,
            "price":500,
            "pickUpGoodsName":"不收服务费",
            "estimateKm":14.627,
            "sendDis":10000,
            "prepayFlag":0,
            "prepayAmount":0,
            "takeMode":0,
            "quoteType":1,
            "quoteAutoFlag":0,
            "ifTaxTransport":1,
            "lossType":2,
            "lossRatio":0.005,
            "transAmount":0,
            "dependNum":"",
            "contractNumber":"",
            "pickupDate":1690732800000,
            "clienter":"谢焕星-货主端",
            "clienterMobile":"13838339604",
            "sendGroup":4,
            "carrierCarryMode":"",
            "appointTeamType":appointTeamType,
            "appointTeamId":appointTeamId,
            "isAutoDisplay":1,
            "antiCrossingGoodsFlag":0,
            "remark":"拆单+定向经纪人",
            "lvesFlag":0,
            "pickupStartDate":1626785983000,
            "createdTime":1626785773000,
            "goodsInsuranceFlagIf":goodsInsuranceFlagIf,
            "goodsInsuranceFlag":goodsInsuranceFlag,
            "goodsInsurancePayerType":3,
            "additionalInsuranceFlag":0,
            "goodsInsuranceCompanyName":"中国人民财产保险股份有限公司上海市分公司",
            "goodsInsuranceCompanyCode":"PICCSH",
            "tpsCatalogCode":"BXPZ210301000461",
            "goodsInsuranceMainRate":0.00022,
            "goodsInsuranceAdditionalRate":0,
            "ifDefault":1,
            "billPlateProvince":"北京市",
            "billPlateCity":"北京市",
            "billPlateCountry":"东城区",
            "startPlateProvince":"北京市",
            "startPlateCity":"北京市",
            "startPlateCountry":"东城区",
            "endPlateProvince":"北京市",
            "endPlateCity":"北京市",
            "endPlateCountry":"西城区",
            "ifAudit":if_audit
        }
        response_doPublish = self.post_json(url,data,header)
        if response_doPublish.text.__contains__("\"code\":0"):
            publish_id = SqlTest.run_query_sql(SqlHome.queryPublish_sql())[0]['publish_id']
            return publish_id
        else:
            raise print("\033[31m货主发单失败!失败原因: " + response_doPublish.text)

    """ 查询货源单信息 """
    @staticmethod
    def queryPublishBySql():
        ownerController = OwnerController()
        publish_id = ownerController.doPublish()
        data = SqlTest.run_query_sql(SqlHome.query_publishByPublishId_sql(publish_id))
        print("货源单id:"+str(data[0]["publish_id"]))
        print("是否拆单:"+str(data[0]["detachable"]))
        print("定向类型:"+str(data[0]["appoint_team_type"]))
        print("定向ID:"+str(data[0]["appoint_team_id"]))
        print("是否收服务费:"+str(data[0]["fee_flag"]))
        print("是否收保险费:"+str(data[0]["goods_insurance_flag"]))
        print("0税率,1差价: "+str(data[0]["if_audit"]))

if __name__ == '__main__':
    print("\033[34m------------------------货主开始操作-----------------------------------")
    loinName = '谢焕星-货主端'
    ownerTk = OwnerLogin().ownerLogin(loinName,"111111")
    OwnerController.queryPublishBySql()
    print("\033[34m------------------------货主操作完成-----------------------------------")


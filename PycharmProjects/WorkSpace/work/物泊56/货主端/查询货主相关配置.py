from common.sql import SqlTest
from common.sqlHome import SqlHome


class OwnerConfig(SqlTest):
    """ 查询ownerId """
    @staticmethod
    def query_ownerId(loinName):
        data = SqlTest.run_query_sql(SqlHome.query_ownerId_sql(loinName))
        if data:
            return data[0]["owner_id"]
        else:
            raise print("\033[31m未查询到该货主")

    """ 查询税率模式服务费配置 """
    @staticmethod
    def query_ownerTax_fee(loinName):
        data = SqlTest.run_query_sql(SqlHome.query_ownerTax_fee_sql(OwnerConfig.query_ownerId(loinName)))
        if data:
            val_status = data[0]["val_status"]
            print("\033[32m该货主有税率模式服务费配置,状态为: "+str(val_status) +"\r\n数据为 :"+ str(data))
        else:
            raise print("\033[31m该货主没有税率模式服务费配置")

    """ 查询税率模式服务费配置 """
    @staticmethod
    def query_owner_goods_insurance(loinName):
        data = SqlTest.run_query_sql(SqlHome.query_owner_goods_insurance_sql(OwnerConfig.query_ownerId(loinName)))
        if data:
            val_status = data[0]["val_status"]
            print("\033[32m该货主有货运险配置,状态为: "+str(val_status) +"\r\n数据为 :"+ str(data))
        else:
            raise print("\033[31m该货主没有货运险配置")

    """ 查询委托方最高补助金配置 """
    @staticmethod
    def query_owner_max_rebate_amount(loinName):
        data = SqlTest.run_query_sql(SqlHome.query_owner_max_rebate_amount_sql(OwnerConfig.query_ownerId(loinName)))
        if data:
            val_status = data[0]["val_status"]
            print("\033[32m该货主有最高补助金配置,状态为: "+str(val_status) +"\r\n数据为 :"+ str(data))
        else:
            raise print("\033[31m该货主没有最高补助金配置")
OwnerConfig.query_owner_max_rebate_amount("谢焕星-货主端")
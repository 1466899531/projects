import pymongo
import pymysql
from common.db import DBConnect


class SqlTest:
    """ 获取验证码 """

    @staticmethod
    def run_queryMessageCode_sql(sql):
        collection = DBConnect.test_connect_mongodb("10.0.161.62", 27017, "wbmongo123", "1fe23e4b56")
        results = collection.find(sql, {"_id": 0, "message": 1, "created_time": 1}).sort("created_time",
                                                                                         pymongo.DESCENDING).limit(1)
        for result in results:
            messageCode = (result['message'] + str(result['created_time'])).split('：')[1].split("，")[0]
            if messageCode:
                print("\033[32m注册验证码为: " + str(messageCode))
                return messageCode
            else:
                print("\033[31m未查询到注册验证码")

    """ 增加 """

    @staticmethod
    def run_insert_sql(sql):
        db_collection = DBConnect.test_connect_mysqldb("10.0.161.63", 3309, "wb_allcenter100", "ege125nh#$po",
                                                       "usercenter")
        cursor = db_collection.cursor()
        try:
            rows = cursor.execute(sql)  # executemany
            db_collection.commit()
            print("\033[32m数据添加成功, 受影响的行数为 : 【" + str(rows) + "】")
        except Exception as e:
            # 有异常，回滚事务
            print("\033[32m数据添加失败, 执行sql为 : 【" + sql + "】")
            print(e)
            db_collection.rollback()
        cursor.close()
        db_collection.close()

    """ 查询 """

    @staticmethod
    def run_query_sql(sql):
        db_collection = DBConnect.test_connect_mysqldb("10.0.161.63", 3309, "wb_allcenter100", "ege125nh#$po",
                                                       "usercenter")
        cursor = db_collection.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        if data:
            return data
        else:
            print("\033[31m未查询到数据 : 【" + sql + "】")

    """ 删除 """

    @staticmethod
    def run_delete_sql(sql):
        db_collection = DBConnect.test_connect_mysqldb("10.0.161.63", 3309, "wb_allcenter100", "ege125nh#$po",
                                                       "usercenter")
        cursor = db_collection.cursor()
        try:
            # 执行SQL语句
            rows = cursor.execute(sql)
            # 提交事务
            db_collection.commit()
            print("\033[32m数据清理成功, 受影响的行数为 : 【" + str(rows) + "】")
        except Exception as e:
            # 有异常，回滚事务
            print("\033[31m数据清理失败, 执行sql为 : 【" + sql + "】")
            print(e)
            db_collection.rollback()
        cursor.close()
        db_collection.close()

    """ 修改 """

    @staticmethod
    def run_update_sql(sql):
        db_collection = DBConnect.test_connect_mysqldb("10.0.161.63", 3309, "wb_allcenter100", "ege125nh#$po",
                                                       "usercenter")
        cursor = db_collection.cursor()
        try:
            rows = cursor.execute(sql)  # executemany
            db_collection.commit()
            print("\033[32m数据修改成功, 受影响的行数为 : 【" + str(rows) + "】")
        except Exception as e:
            # 有异常，回滚事务
            print("\033[31m数据修改失败, 执行sql为 : 【" + sql + "】")
            print(e)
            db_collection.rollback()
        cursor.close()
        db_collection.close()

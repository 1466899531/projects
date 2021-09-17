import pymongo
import pymysql

""" 获取数据库连接基类 """
class DBConnect:

    """ 获取MongoDb数据库连接 """
    @staticmethod
    def test_connect_mongodb(host,port,username,password):
        # client = MongoClient('mongodb://root:666@localhost:27017') # 连接MongoDB数据库(mongodb://用户名:密码@localhost(ip地址):port端口)
        # mongoDB_collection = client['wbmongo']['bs_short_message_2021'] # client['数据库']['所形成的的表名']
        client = pymongo.MongoClient(host,port) # 建立客户端对象
        db = client.wbmongo # 连接MongoDB数据库
        db.authenticate(username,password) # 输入用户名和密码
        # db.collection_names() # 查看当前数据库所有集合名称
        mongoDB_collection = db.bs_short_message_2021   # 连接MongoDB数据库中的集合
        if mongoDB_collection:
            return mongoDB_collection
        else:
            raise Exception("\033[31m获取mongoDB数据库连接异常!!!")

    """ 获取MySqlDb数据库连接 """
    @staticmethod
    def test_connect_mysqldb(host,port,username,password,dbName):
        db_collection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=dbName,
            charset='utf8'
        )
        if db_collection:
            return db_collection
        else:
            raise Exception("\033[31m获取mysqlDB数据库连接异常!!!")



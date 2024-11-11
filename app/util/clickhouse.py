from clickhouse_driver import Client

ck_client = Client(host='127.0.0.1', port='9000', user="default", password="") # 连接数据库
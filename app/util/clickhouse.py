from clickhouse_driver import Client

ck_client = Client(host='10.200.48.58', port='9000', user="default", password="") # 连接数据库
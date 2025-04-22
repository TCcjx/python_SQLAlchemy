import sqlalchemy

# 连接数据库的引擎
engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb',echo=True)

connect = engine.connect()

query = sqlalchemy.text('SELECT * FROM students')
result_set = connect.execute(query)

for row in result_set: # 查询打印每一行
    print(row)

connect.close() # 关闭连接
engine.dispose() # 销毁数据库引擎
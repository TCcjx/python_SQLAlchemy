from MySQLdb import Date
import sqlalchemy

# 连接数据库的引擎
engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb', echo=True)

# 存储表的结构信息
meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key= True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=True),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.String(255), nullable=True)
)

meta_data.create_all(engine)
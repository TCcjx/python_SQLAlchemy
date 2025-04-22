import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb',echo=True)

meta_data = sqlalchemy.MetaData()
# 创建表结构
person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column('name', sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column('birthday',sqlalchemy.Date, nullable=False)
)

meta_data.create_all(engine) 


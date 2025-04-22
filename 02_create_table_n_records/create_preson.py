import sqlalchemy
import sqlite3

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb',echo=True)

meta_data = sqlalchemy.MetaData()
# 创建表结构
person = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column('name', sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column('birthday',sqlalchemy.Date, nullable=False)
)

meta_data.create_all(engine)

# insert a record
# 插入单条数据
person_insert = person.insert()
# print(person_insert)
insert_tom = person_insert.values(name='syj',birthday='2000-10-10') # 其实背后就是生成相应的sql语句

with engine.connect() as conn:
    result = conn.execute(insert_tom) # 执行插入语句
    print(result.inserted_primary_key)
    conn.commit()



# insert multiple records
# 插入多条数据
person_insert = person.insert()
with engine.connect() as conn:
    conn.execute(person_insert,[
        {
            "name": "Jack",
            "birthday": "2000-6-15",

        },
        {
            "name": "jax",
            "birthday": "2001-10-13",
            
        },
        {
            "name": "Java",
            "birthday": "2002-10-12",
            
        }
    ])
    conn.commit()

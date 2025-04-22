import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb', echo=True)

meta_data = sqlalchemy.MetaData() # 存储表结构信息

# one to many（一对多的关联关系）
department = sqlalchemy.Table(
    'department', meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(255), nullable=True, unique=True)
)

employee = sqlalchemy.Table(
    'employee', meta_data,
    sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name',sqlalchemy.String(128),nullable=False),
    sqlalchemy.Column('department_id',sqlalchemy.Integer, sqlalchemy.ForeignKey('department.id'), nullable=False)
)



meta_data.create_all(engine)
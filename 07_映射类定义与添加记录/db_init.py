from tkinter import E
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # 建立session

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb', echo=True)
Base = declarative_base()

class Person(Base): # 表的映射类
    __tablename__ = 'person' # 数据库表名

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable = True) 
    birthday = Column(Date, nullable=False)
    address = Column(String(255), nullable=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine) # 创建数据库会话

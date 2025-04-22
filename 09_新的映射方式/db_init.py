import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column # 建立session
import datetime
from typing_extensions import Annotated

engine = sqlalchemy.create_engine('mysql://root:123456@localhost/testdb', echo=True)
Base = declarative_base()

int_pk = Annotated[int,mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
timestamp_default_now = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=func.now())]

class Customer(Base): # 表的映射类
    __tablename__ = 'customers' # 数据库表名

    # id: Mapped[int] = mapped_column(primary_key=True)
    # name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    # birthday: Mapped[datetime.datetime] 
    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    birthday: Mapped[datetime.datetime]
    city: Mapped[str] = mapped_column(String(128), nullable=True)
    create_time: Mapped[timestamp_default_now]

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine) # 创建数据库会话

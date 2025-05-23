import datetime

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from typing_extensions import Annotated
from typing import List


engine = create_engine('mysql://root:123456@localhost/testdb', echo=True)
Base = declarative_base()


# 在 SQLAlchemy 2.0 中，Annotated 是一个类型注解工具，用于在类型注解中添加额外的元数据。
int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    # create_time: Mapped[timestamp_not_null]

    # 1.可使用backref进行双向关联
    # 2.可以使用back_populates的方式进行双向关联
    employees: Mapped[List["Employee"]] = relationship(back_populates="department")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'  
    

class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int_pk]
    dep_id: Mapped[int] = mapped_column(ForeignKey('department.id'))
    name: Mapped[required_unique_name]
    birthday:  Mapped[datetime.datetime] = mapped_column(nullable=False)

    department: Mapped[Department] = relationship(lazy=False, back_populates='employees')

    def __repr__(self):
        return f'id: {self.id}, dep_id: {self.dep_id}, name: {self.name}, birthday: {self.birthday}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
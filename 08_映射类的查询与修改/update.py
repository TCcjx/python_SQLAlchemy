from db_init import Person, Session

session = Session()

# 更新单挑记录信息 方式一
person = session.query(Person).filter(Person.id == 1).one()
person.address = 'BaZhong'


# 更新单挑记录信息 方式二
session.query(Person).filter(Person.id == 1).update({
    Person.address : "YaAn"
}) 

# 批量信息修改(更改过滤条件即是 修改多条信息)
session.query(Person).filter(Person.id > 1).update({
    Person.address : 'BeiJing'
})
session.commit()
from db_init import Session, Person

session = Session()

# 往数据库中添加信息
# p = Person(name = "Amy", birthday = '2000-05-11', address = 'unknown')

# 往数据库中添加多条信息
person_list = [
    Person(name = "cc", birthday = '2020-05-11', address = 'unknown'),
    Person(name = "dmy", birthday = '2001-05-11', address = 'unknown'),
    Person(name = "jj", birthday = '2030-05-11', address = 'unknown')
]


session.add_all(person_list)
session.commit()


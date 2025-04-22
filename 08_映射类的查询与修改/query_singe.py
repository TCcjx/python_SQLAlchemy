from db_init import Person, Session

session = Session()
result = session.query(Person).filter(Person.name == 'cjx').first()
# result = session.query(Person).filter(Person.name == 'cjx').one() # 要求查出来的记录只有一条
# result = session.query(Person).filter(Person.name == 'cjx').scalar() # 背后也是调用one()

print(f'name: {result.name}, birthday: {result.birthday}')   
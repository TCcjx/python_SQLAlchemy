from db_init import Session, Employee, Computer

def insert(session):
    c1 = Computer(model = "Dell", number='1111')
    c2 = Computer(model = 'Surface', number='2222')
    c3 = Computer(model = 'Macboom', number='3333')

    e1 = Employee(name = 'Jack', computer = c1)
    e2 = Employee(name = 'Mary', computer = c2)
    e3 = Employee(name = 'Tom', computer = c3)

    session.add_all([e1, e2, e3])
    session.commit()


def select(session): # one to one
    c = session.query(Computer).filter(Computer.id == 1).one()
    if c:
        print(c)
        print(c.employee) 
    e = session.query(Employee).filter(Employee.id == 2).one()
    if e:
        print(e)
        print(e.computer)

def update_1(session):
    session.query(Employee).filter(Employee.id == 1).update({Employee.computer_id: 1})
    session.commit()

def update_2(session): # 使用类关联关系进行更新
    c = session.query(Computer).filter(Computer.id == 1).scalar()
    e = session.query(Employee).filter(Employee.id == 2).scalar()
    if c and e:
        e.computer = c
        session.commit()

session = Session()
# insert(session)
# select(session)
# update_1(session)
update_2(session)
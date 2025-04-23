from db_init import Session, Department, Employee


def insert_records(session):
    d1 = Department(name = 'hr')
    # session.add(d1) 
    # session.flush() # flush 方法将当前会话中所有待处理的数据库操作发送到数据库中，但不会提交事务。

    e1 = Employee(department=d1, name='Tom', birthday='2000-05-09')
    session.add(e1)
    session.commit()
 

def select_employee(session):
    result = session.query(Employee).filter(Employee.id == 1).one()
    print(result)
    print(result.department)

def select_department(session):
    dep = session.query(Department).filter(Department.id == 2).one()
    
    print(dep)
    print(dep.employees)


session = Session()
# insert_records(session)
select_employee(session)
# select_department(session)

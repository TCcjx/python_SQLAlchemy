from db_init import engine, department, employee
import sqlalchemy

with engine.connect() as conn:
    join = employee.join(department, employee.c.department_id == department.c.id) # 连接两张表
    # query = sqlalchemy.select(join).where(department.c.name == 'hr') 
    # query = sqlalchemy.select(employee).select_from(join).where( # 只查询员工信息
    #     department.c.name == 'hr'
    # )
    query = sqlalchemy.select(department).select_from(join).where(employee.c.name ==  'cjx') #  查询‘cjx’员工所在的部门信息


    result_set = conn.execute(query)
    result = result_set.fetchall()
    print(result)
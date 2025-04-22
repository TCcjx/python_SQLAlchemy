from db_init import engine, department, employee

with engine.connect() as conn:
    conn.execute(department.insert(),[
        {'name': 'hr'},{'name': 'IT'}

    ])
    conn.execute(employee.insert(),[
        {'department_id': 1, 'name':"jack"},
        {'department_id': 2, 'name': 'cjx'},
        {'department_id': 1, 'name': 'syj'}
    ])
    conn.commit()
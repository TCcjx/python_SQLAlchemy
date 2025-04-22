from db_init import engine, person_table

# 查询所有记录
with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)  

    # 循环查询记录
    # for row in result_set:
    #     print(row[0])
    #     print(row.name)

    # 查询所有记录并放在内存里，如果记录过多的话，不推荐采用这种方式
    print(result_set.fetchone())
    result = result_set.fetchall() 
    print(result)

# 条件查询
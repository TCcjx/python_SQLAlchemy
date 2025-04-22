from db_init import engine, person_table


# 删除记录
with engine.connect() as conn:
    delete_query =  person_table.delete().where(person_table.c.id == 2)
    conn.execute(delete_query)
    conn.commit()
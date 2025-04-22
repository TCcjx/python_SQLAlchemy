from db_init import engine, person_table

# 更新表信息
with engine.connect() as conn:
    # update_query = person_table.update().values(address='enyang')
    update_query = person_table.update().values(address='城奥大厦').where(person_table.c.id == 2)
    conn.execute(update_query)
    conn.commit()
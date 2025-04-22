from unittest import result
from db_init import engine, person_table
from sqlalchemy.sql import and_, or_

with engine.connect() as conn:
    # query = person_table.select().where(person_table.c.birthday > '2000-10-13').where(person_table.c.id < 10) #  条件查询
    query = person_table.select().where(
        or_(
            person_table.c.name == 'cjx',
            and_(
                person_table.c.name == 'syj',
                person_table.c.id < 4
            )
        )
    )
    # 查出来两条数据
    result_set = conn.execute(query)

    for row in result_set:
        print(row)

    # result = result_set.fetchall()
    # print(result)
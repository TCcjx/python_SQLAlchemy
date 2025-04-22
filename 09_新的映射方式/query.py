from db_init import Session, Customer

session = Session()

c = Customer(name='cjx', birthday = "2002-9-10",city='BZ')

session.add(c)
session.commit() 
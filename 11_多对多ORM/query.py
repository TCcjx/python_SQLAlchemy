from db_init import Session, User, Role


def insert_records(session):
    role1 = Role(name='Admin')
    role2 = Role(name="Operator")

    user1 = User(name='Jack', password='111')
    user2 = User(name='Tom', password='111')
    user3 = User(name='Cjx', password='111')

    user1.roles.append(role1)
    user1.roles.append(role2)

    user2.roles.append(role1)
    user3.roles.append(role2)

    session.add_all([user1, user2, user3])
    session.commit()


def select_user(session):

    user = session.query(User).filter(User.id == 3).one()
    print(user)
    print(user.roles) 


def select_role(session):
    role = session.query(Role).filter(Role.id == 1).one()
    print(role)
    print(role.users)


session = Session()
# insert_records(session)
# select_user(session)
select_role(session)

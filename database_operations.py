import json
import contextlib
from orm import UserModel, TicketModel, OrganizationModel
from sqlalchemy.orm import sessionmaker
from app import Base, engine
from orm.dictionaries import ClassTypeEnum, UserDict, OrganizationDict, TicketDict

import orm.User

Base.metadata.bind = engine
Base.metadata.create_all(engine, checkfirst=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def json_to_database():
    with open('./JsonStore/users.json') as f:
        data = json.load(f)
        for p in data:
            user = UserModel(**p)
            session.add(user)
        session.commit()
    with open('./JsonStore/tickets.json') as f:
        data = json.load(f)
        for p in data:
            ticket = TicketModel(**p)
            session.add(ticket)
        session.commit()
    with open('./JsonStore/organizations.json') as f:
        data = json.load(f)
        for p in data:
            org = OrganizationModel(**p)
            session.add(org)
        session.commit()


def get_data(className, fieldName, value):
    if value is "":
        value = None
    if className == ClassTypeEnum.Users.value:
        if (UserDict.get(fieldName)) is not None:
            return session.query(UserModel).filter(UserDict[fieldName] == value).all()
        else:
            raise Exception('Invalid User search term, please list and check the searchable fields')
    elif className == ClassTypeEnum.Tickets.value:
        if (TicketDict.get(fieldName)) is not None:
            return session.query(TicketModel).filter(TicketDict[fieldName] == value).all()
        else:
            raise Exception('Invalid Ticket search term, please list and check the searchable fields')
    elif className == ClassTypeEnum.Organizations.value:
        if (OrganizationDict.get(fieldName)) is not None:
            return session.query(OrganizationModel).filter(OrganizationDict[fieldName] == value).all()
        else:
            raise Exception('Invalid Organization search term, please list and check the searchable fields')
    else:
        raise Exception('Invalid selection. Enter a number between 1-3 ')


def clear_database():
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(Base.metadata.sorted_tables):
            con.execute(table.delete())
        trans.commit()

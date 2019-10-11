from orm.dictionaries.UserDict import UserDict
from orm.dictionaries.OrganizationDict import OrganizationDict
from orm.dictionaries.TicketDict import TicketDict

import enum


class ClassTypeEnum(enum.Enum):
    Users = 1
    Tickets = 2
    Organizations = 3


def print_keys(d):
    for key in d.keys():
        print(key)

from orm.dictionaries import print_keys, UserDict, TicketDict, OrganizationDict
from database_operations import get_data

INSTRUCTIONS_STRING = 'Type \'quit\' to exit at any time, Press \'Enter\' to continue\n\n' \
                      '\t\tSelect search options:\n' \
                      '\t\t* Press 1 to search\n' \
                      '\t\t* Press 2 to view a list of searchable fields\n' \
                      '\t\t* Type \'quit\' to exit\n'
BODER_STRING = '-------------------------------------------------------------------------'


def print_searchable():
    print(BODER_STRING)
    print("Search Users with")
    print_keys(UserDict)
    print(BODER_STRING)
    print("Search Tickets with")
    print_keys(TicketDict)
    print(BODER_STRING)
    print("Search Organizations with")
    print_keys(OrganizationDict)


def print_data(className, searchTerm, res):
    try:
        res = get_data(className, searchTerm, res)
        if not res:
            print('No results found')
        else:
            for p in res:
                print(p)
    except Exception as e:
        print(e)


def input_loop():
    run = True
    while run:
        res = select_option()
        if not check_continue():
            break


def enter_search_val(className, searchTerm):
    res = input('Enter search value\n')
    if res == 'quit':
        return False
    else:
        print_data(className, searchTerm, res)
        return True


def select_term(className):
    res = input('Enter search term\n')
    if res == 'quit':
        return False
    else:
        return enter_search_val(className, res)


def select_class():
    res = input('Select 1) Users or 2) Tickets or 3) Organizations\n')
    if res == 'quit':
        return False
    elif res == '1' or res == '2' or res == '3':
        return select_term(int(res))
    else:
        print('Invalid selection, Select again')
        select_class()


def select_option():
    print(INSTRUCTIONS_STRING)
    res = input()
    if res == '1':
        return select_class()
    elif res == '2':
        print_searchable()
        return True
    elif res == 'quit':
        return False
    else:
        print('Invalid Option selection, Enter 1 or 2\n')
        select_option()


def check_continue():
    res = input('\nPress \'Enter\'to continue search or type \'quit\' to quit :')
    if res == 'quit':
        return False
    else:
        return True

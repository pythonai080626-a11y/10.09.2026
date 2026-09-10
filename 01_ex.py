
# 1
# password check
# function which gets a user_dict and name, password

# def check_password(user_dict, name, password)
#     if name does not exist in dict - return 'user name {name} does not exist'
#     if name exit but password not match - return 'wrong password'
#     if name exist + password correct - return 'success'

# test the function
# { 'danny': 'Danny1999', 'sharon': 'Password1!' }
# print(check_password('yossi', 'the-king')) #  --> 'user name yossi does not exist'
# print(check_password('danny', 'the-king'))  # --> 'wrong password'
# print(check_password('sharon', 'Password1!'))  # --> 'success'

# 2
# dic_swap
# function which gets a dict and return dict

# { 'a': 1, 'd': 'hi' } --> { 1: 'a', 'hi': 'd'}
# BONUS
# { 'a': 1, 'd': 1, 'c': 3 } --> { 1: ['a', 'd'], 3: 'c' }
# { 'a': 1, 'd': 1, 'c': 3 , 'f': 1} --> { 1: ['a', 'd', 'f'], 3: 'c' }
# def dict_swap(dict_input):
#   return (1) dict swapped key-value
#          (2) BONUS-- on same key return list
#  test
# print(dict_swap({ 'a': 1, 'd': 'hi' }))  # { 1: 'a', 'hi': 'd'}
# print(dict_swap({ 'a': 1, 'd': 1, 'c': 3 , 'f': 1}))  # { 1: ['a', 'd', 'f'], 3: 'c' }
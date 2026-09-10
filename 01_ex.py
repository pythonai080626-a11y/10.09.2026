
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
# ***BONUS***
# { 'a': 1, 'd': 1, 'c': 3 } --> { 1: ['a', 'd'], 3: 'c' }
# { 'a': 1, 'd': 1, 'c': 3 , 'f': 1} --> { 1: ['a', 'd', 'f'], 3: 'c' }
# def dict_swap(dict_input):
#   return (1) dict swapped key-value
#          (2) ***BONUS*** on same key return list
#  test
# print(dict_swap({ 'a': 1, 'd': 'hi' }))  # { 1: 'a', 'hi': 'd'}
# print(dict_swap({ 'a': 1, 'd': 1, 'c': 3 , 'f': 1}))  # { 1: ['a', 'd', 'f'], 3: 'c' }

# 3
# find pair sum
# function which gets a list and a sum_number
# the function should return tuple of 2 numbers which sum of them equals sum_number
#   if there are none --> return None

# def pair_sum(list1, sum_number)
#    return (a, b) or None

# print(pair_sum([1, 2, 3, 4, 5], 9))  # (4, 5)
# print(pair_sum([1, 2, 3, 4, 5], 40))  # None
# print(pair_sum([0, -2, 18, 39], 37))  # (-2, 39)

# **BONUS** : run without nested only 1 time on the numbers





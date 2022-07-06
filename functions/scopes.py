'''         Scopes - Область видимости и пространство имен '''

'''
Built-in (встроенная) - print, len, max, int ...

Global (глобальная)

Enclosed or nonlocal (нелокальная)

Local (локальная область видимости)
'''

# def print_list(some_list):
#     for element in some_list: 
#         print(element)

# element = 'q'
# print_list([1,2,3,4,5])
# print(element)

# a = 10          # global
# print           # built-in
# def hello():    #global   
#     a = 'Hello world'  # local
#     print(a, 'local inside of function')

# hello()
# print(a, 'global')


# x = 'global'
# print(x) # 1

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x) # 3
#     print(x) # 2
#     local() 
#     print(x) # 4
# enclosed()
# print(x) # 5

# num = 10
# def func():
#     def inner_func():
#         num = 11
#         print(num)
#     inner_func()
# func()


# var  = 100 # global variable

# def increment():
#     var = var + 1 # trying to update a global variable(using increment -> var += 1)
#     print(var)      """выведет ошибку"""
# increment()


'''
Global -> Позволяет менять значение глобальной переменной, 
находясь в локальной области видимости'''


""" nonlocal -> позволяет менять значение локальной переменной,
находясь в локальной области видимости """



# var  = 100 # global variable

# def increment():
#     global var 
#     var += 1
#     # print(var)
# print(var)
# increment()
# increment()
# increment()
# print(var)

# =====================================================================================================

# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer
# c = counter()
# print(c)     # <function counter.<locals>.incrementer at 0x7f3583b4c0d0>
# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# c = counter()
# print(c()) # 1

# ===========================================================================================

# print(dir(__builtins__))
# print(len(dir(__builtins__)))



# print(abs(-15)) # Стандартный вызов встроенной функции
# abs = 15  # Переопределение встроенной имени abs в глобальной облвсти
# # print(abs(-15))

# del abs
# print(abs(-16))




'''================================================================================================='''

# # 1 variant

# list_ = [[1,2,3],[3,3,5]]
# max_digit = sum(list_[0])
# for i in range(len(list_)):
#     if sum(list_[i]) > max_digit:
#         max_digit = sum(list_[i])
# print(max_digit)
        


# # 2 variant

# list_ = [[1,2,4], [3,5,6], [1,12,4]] 
# sums = list()
# for i in list_:
#     sums.append(sum(i))
# print(sums)
# print(max(sums))


# # 3 variant

# list_ = [[1,2,4], [3,5,6], [1,12,4]] 
# res = max([sum(i) for i in list_])
# print(res)
'''==========================================================================================='''

# alice = [13, 15, 38]
# john = [5, 15, 50]
# john_count = 0
# alice_count = 0
# for i in range(len(alice)):
#     if alice[i]> john[i]:
#         alice_count += 1
#     elif alice[i] == john[i]:
#         pass
#     else:
#         john_count += 1
# res = {
#     'Alice': alice_count,
#     'John': john_count
# }
# print(res)


# alice = [13, 15, 38]
# john = [5, 15, 50]

# def compareScores(a,j):
#     score_a = 0
#     score_j = 0
#     for i in range(len(a)):
#         if a[i] > j[i]:
#             score_a += 1
#         elif a[i] < j[i]:
#             score_j += 1
#         else:
#             pass
#     return {'Alice': score_a, 'John': score_j}

# print(compareScores(alice, john))
# print(compareScores([54,20,10], [10, 35, 15]))



'''====================================================================================='''

#  mine

# str_ = 'Pythoniiiist'

# def dict_count(s):
#     dict_ = {}
#     for i in s:
#         dict_[i] = s.count(i)
#     return dict_
# print(dict_count(str_))



#  cours

# str_ = 'Pythoniiiist'

# dict_ = {key: str_.count(key) for key in str_}
# print(dict_)

'''=================================================================================='''
# from random import choice

# list_ = list()
# def add(*names):
#   for name in names:
#     list_.append(name)
# def remove(num):
#   # global list_
#   del list_[num]
  
# funcs = [add('aibek', 'ramazan', 'nurma', 'beka', 'syoma'), remove()]
# for _ in range(10):
#   print(random.choice(funcs))
  
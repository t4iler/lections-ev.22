'''
                            Встроенные функции:
input()
print()
str()
sum()
list()
len()
divmod()
globals()
locals()
min()
max() etc...                            
'''
# ===================================================================================================
'''
                                map()
                                filter()
                                lambda
                                enumerate()

Анонимные функции - lambda(такие же функции только без названия)
lambda функции могут принимать сколько угодно аргументов,
но всегда возвращают только одно выражение.
'''


# def sum_args(a, b):
#     result = a + b
#     return result

# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_arg = lambda a, b: a + b
# print(sum_arg(1, 2))

# x = lambda a, b, c: a + b + c
# print(x(5,6,7))


'''====================================================================================='''

# def myFunc(n):
#     return lambda a: a * n

# my_doubler = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(11))
# print(my_tripler(22))

'''====================================================================================='''

# ls = ['def', 'Ivan', 'john', '', ' ']
# new_list = sorted(ls)
# print(new_list)
# new_list2 = sorted(ls, key = len)
# print(new_list2)


'''====================================================================================='''

# import random

# ls = ['Плов', 'Манты', 'Куурдак', 'Лагман', 'Дымдама']

# p = 0
# m = 0
# k = 0
# l = 0
# d = 0

# for i in range(10000):
#     choice = random.choice(ls)
#     # print(choice)
#     if choice.lower() == 'плов':
#         p += 1
#     elif choice.lower() == 'манты':
#         m += 1
#     elif choice.lower() == 'куурдак':
#         k += 1
#     elif choice.lower() == 'лагман':
#         l += 1
#     elif choice.lower() == 'дымдама':
#         d += 1
# # print(dir(random))
# dict1 = {
#     'Плов': p, 
#     'Манты': m, 
#     'Куурдак': k, 
#     'Лагман': l,
#     'Дымдама': d
# }
# # print(dict1)
# result = sorted(dict1.items(), key=lambda x: x[1])
# print(result)
# winner = result[-1]
# print(f'Победило блюдо: {winner[0]}, оно набрало: {winner[1]}')


'''======================================================================================================='''

'''
map(function, Interable object) -> применяет функцию к каждому элементу последовательности
и возвращает mapobject(итератор) с результатами.

Например, с помощью map можно выполнять преобразование элементов. 
Перевести все строки в верхний регистр:
'''

# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)
# result2 = list(map(len, list_of_words))
# print(result2)

# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# result2 = [int(i) for i in ls]
# print(result)
# print(result2)
'''====================================================================================='''

# names = ['John', 'Jamie', 'Santa', 'Tailer', 'Sanzhar']
# #  ['Hello mr/mrs John', 'Hello mr/mrs Jamie', ...]
# result = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(result)


# nums = [1, 2, 3, 4, 5]
# nums2 = [100, 200, 300, 400, 500]
# # 100, 400, 900, 1600, 2500
# result = list(map(lambda x, y: x*y, nums, nums2))
# print(result)


# dict_ = {
#     1: 2,
#     3: 4,
#     5: 6
# }
# # {1: '2', 3: '4', 5: '6'}
# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)

'''====================================================================================='''

'''
                                        filter
set, dict, range, list, tuple, str ... (interable)

filter(function, Interable) - применяет ко всем элементам interable функцию, 
которую мы передаем и возвращает filterobject(итератор) с теми объектами,
для которых функция вернула True.
'''

# list_of_str = ['one', 'two', 'list', '', '100', '1', '50', 'John99']
# result = list(filter(str.isdigit, list_of_str))
# # print(list(result))
# print(result)
# for i in result: print(i)


# ls = [10, 11, 102, 113, 314, 515]
# new_list = list(filter(lambda i: i%2!=0, ls))
# odds = [i for i in ls if i%2!=0]
# print(new_list)
# print(odds)


# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ono', 'ev.22']
# new_list = list(filter(lambda i: len(i)>=4, list_of_words))
# x = lambda i: len(i)>=4
# new_list2 = list(filter(x, list_of_words))
# print(new_list)
# print(new_list2)

'''====================================================================================='''

'''
                                    enumerate
'''
# # without enumerate
# ls = ['str1', 'str2', 'str3']
# i = 0
# for x in ls:
#     print(f'Element: {x}, index: {i}')
#     i += 1

# # with enumerate
# ls = ['str1', 'str2', 'str3']
# for i, x in enumerate(ls):
#     print(f'Element: {x}, index: {i}')

# new_list = list(enumerate(ls))
# print(new_list)


""" 
Функция высшего порядка - это функция, 
которая может принимать в качестве аргумента другую функцию 
и/или возвращать функцию как результат работы.
"""








'''
zip(2 interable object) - она соединяет каждый элемент интерируемых элементов между
собой в тип данных tuple и возвращает это
'''


# list1 = [1, 2, 3]
# list2 = [100, 200, 300]
# result = zip(list1, list2)
# result2 = list(zip(list1, list2))
# print(result2)
# print(result)
# print(list(result))


# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40]
# c = [100, 200, 300]
# result = list(zip(a, b, c))
# print(result)


'''
zip для создания словарей
'''

# d_keys = ['hostname', 'location', 'vandor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Blode Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
# dict_r1  = dict(zip(d_keys, d_values))
# print(dict_r1)

# =======================================================================

# d_keys = ['hostname', 'location', 'vandor', 'model', 'IOS', 'IP']
# data = {
#     'r1': ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2': ['london_r2', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.2'],
#     'sw1': ['london_sw1', '21 New Globe Walk', 'Cisco', '3850', '3.6.XE', '10.255.0.101']
#     }

# london_data = {}
# for key in data.keys():
#     london_data[key] = dict(zip(d_keys, data[key]))

# print(london_data)



'''
                                all & any

all -> возвращает True если все элементы объекта являются истиной(или объект пустой)
Чаще всего эта функция используетя для проверки
'''

# ls = [False, 1, 'stroka', True]
# print(all(ls))
# ls2 = [[1, 2], 1, 'stroka', True]
# print(all(ls2))
# ls3 = []
# print(all(ls3))
# ============================================================================================

# ip = '10.255.0.0.1'
# result1 = all(i.isdigit() for i in ip.split('.'))
# print(result1)
# ip2 = '10.255.0.a.0.1'
# result2 = all(i.isdigit() for i in ip2.split('.'))
# print(result2)


'''
                                 any
any -> возвращает True если хотя бы один элемент является истинной
Чаще всего эта функция используетя для проверки
'''

# ls1 = [0, 0, '', False]
# print(any(ls1))

# ls2 = [0, 0, '', 'a', False]
# print(any(ls2))

'''                            without (any)'''
# def ignore_command(command):
#     '''
#     Функция проверяет есть ли в command слово из списка ignore. 
#     True - если есть, False - если нет такого слова. 
#     '''
#     ignore = ['rm -rf', 'alias', 'reset']
#     for word in ignore:
#         if word in command:
#             return True
#     return False

# # print(ignore_command('sudo rm -rf user'))
# command = 'sudo reset configurations'
# if ignore_command(command):
#     raise Exception('Invalid command')
# print('Все Ок')

'''                            with (any) - встроенная функция'''

# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo rset configurations'
# if any([word in command for word in ignore]):
#     raise Exception('Invalid command')
# print('Все Ок')

'''====================================================================================='''
'''
                                генератор паролей в одну строку
'''

# from random import choices 
# from string import ascii_letters, digits
# from itertools import repeat

# print({
#     f(choices(ascii_letters, k=10), choices(digits, k=5)) 
#     for f in repeat(lambda x, y: ''.join(set(x+y)), 
#     int(input('Введите количество паролей: ')))
# })


# from random import choices 
# from string import ascii_letters, digits
# from itertools import repeat

# print({
#     f(choices(ascii_letters, k=10), choices(digits, k=5)) 
#     for f in repeat(lambda x, y: ''.join(set(x+y)), 
#     int(input('Введите количество паролей: ')))
# })




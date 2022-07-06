'''
Tuple - это структура данных 
неизменяемый
индексируемый
упорядоченный
'''

# string1 = str('Hello AttackPython')
# string2 = 'Hello world'
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set1 = {}
# dict1 = {'key': 'value'}

# tuple1 = (1,2,3)
# print(type(tuple1)) # -> tuple class

# tuple1 = 1,2,3,4,5,6
# print(type(tuple1))
# print(tuple1)
# print(dir(tuple1))


# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(5))


# emails = ("Python@gmail.com", "Aibek@mail.ru")

# emails1 = ["Python@gmail.com", "Aibek@mail.ru"]
# ''' разница размеров тюпла и листа '''

# print(emails.__sizeof__(), emails1.__sizeof__(), sep=' | ')


# emails = ("Python@gmail.com", "Aibek@mail.ru", 3, 4, [1, 3, 'apple'])
# print(type(emails[-1]))
# last_object = emails[-1] #list
# last_object.append('tomato')
# print(emails)
# print(len(emails))


# tuple_sequance_first = (2, 2, 4, 3)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first

# print(tuple_sequance)
# # print(tuple_sequance.count(2))
# print(tuple_sequance.index(3,))
# indx = tuple_sequance.index(3, 6) 
# print(tuple_sequance[indx])


# for value in tuple_sequance:
    # print(value)


# names = ('Aibek', 'Tima', 'Zhanylai', 'bermet', 'Aidana', 'Ermek')

# name_enter = ['Tima', 'Aidana', 'Bermet']

# # for name in names:
# #     print(f'hello {name.capitalize()}!!!', len(name), sep= '\n')

# for name in names:
#     if name.capitalize() in name_enter:
#         print(f'hello {name.capitalize()}!!!')
#     else:
#         print(f'{name} go home!!!')


# first_step_names = []
# names = input('enter names: ').split(' ')
# for enter in names:
#     if len(enter) > 4: 
#         first_step_names.append(enter)
#     else:
#         pass
# print(first_step_names)

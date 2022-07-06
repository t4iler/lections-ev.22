'''
dict() - Словарь -> это упорядоченная коллекция элементов (python 3.7 -> ordered). 
Каждый элемент в словаре содержится в паре  *ключ:значение*  
Ключи должны быть уникальными и неизменяемым типом данных(str, int, tuple, etc...)
Тогда как значениями могут быть любые типы данных. 
'''
'''
dict() -> изменяемый, упорядоченный, неиндексируемый
'''

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }

# print(thisdict)
# print(type(thisdict))

# Hash tables, ассоциативный массив, dictionary(python), object(js) == dictionary

# some_dict = {}
# print(type(some_dict))
# key_value = {
#     'key': 'value',
#     'key1': 'value1'
# }
# print(type(key_value))
# dict_created_with_function = dict()
# print(type(dict_created_with_function))

# dict_ = dict((('key', 'value'), ('key1', 'value1')))
# print(dict_)
# print(type(dict_))


'''**********************************************************************************************************'''

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow24@gmail.com',
#     'role': 'moderator',
#     'list': [1, 2, 3],
#     # [1, 2, 3] : 'list' #error (key cannot be mutable)
#     # 'first_name': 'Raychel'
# }
# print(dir(dict))
# # print(user_info)
# print(user_info['first_name'])
# print(user_info.get('age')) # получение значения

# print(user_info.items())  # получаем все ключи и значения
# for item in user_info.items():
#     print(item)

# print(user_info.keys())  #получаем только ключи
# print(user_info.keys())

# user_info['height'] = 185

# print(user_info.keys())
# print(user_info)
# for key in user_info.keys():
#     print(key)
# print(user_info.values())      #получаем только значения

# for value in user_info.values():
#     print(value)

'''
pop() -> удаляет элемент по определенному ключу
popitem() -> удаляет последнюю пару в словаре
'''

# print(user_info)
# user_info.pop('email')  # удаление по ключу
# user_info.popitem()   # удаление последнего
# deleted = user_info.pop('role') # удаление элемента и сохранение удаленного элемента в deleted 
# print(user_info)
# print(deleted)



'''
setdefault(key, [default value]) -> Работает также как и метод get(),
но если такого ключа не существует, то он создает новую пару значений
'''

# # 1 способ применения, получение значений
# dict_ = {
#     'name': 'John',
#     'age': 23
# }
# result = dict_.setdefault('age')
# print(result)

# # 2 способ применения, получение значений
# dict_ = {
#     'name': 'John',
#     'age': 23
# }
# result = dict_.setdefault('address', 'Toktogula street')
# print(dict_)
# print(result)

''' 
update() -> '''

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow24@gmail.com',
#     'role': 'moderator',
#     'list': [1, 2, 3],
# }
# print(user_info)
# # user_info.update({'first_name': 'Raychel'})
# # user_info.update({'height': 185})
# '''same as'''
# user_info['age'] = 30
# user_info['height'] = 185
# print(user_info)


'''********************************************************************************************************'''

# roles = {
#     0: 'Admin',
#     1: 'Moderator',
#     2: 'Vendor',
#     3: 'Customer',
#     4: 'Guest'
# }

# users = [
#     {
#         'id': 0,
#         'name': 'John',
#         'role': roles[0]
#     },
#     {
#         'id': 1,
#         'name': 'Raychel',
#         'role': roles[3]
#     },
#     {
#         'id': 2,
#         'name': 'Aibek',
#         'role': roles[4]
#     }
# ]

# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy S20',
#     'discription': 'Lorem Ipsum',
#     'price': 10000
# }

# print(users)
# print(product)

# user_id = int(input('Введите ваш id: '))

# if users[user_id]['role'] == roles[0]:
#     product['discription'] = input('Введите новое описание продукта: ')
# else:
#     raise Exception ('У вас нет прав!!!')
# print(product)


'''**************************************************************************************************'''
# # task1
# list1 = list(range(0, 101, 2))
# print(list1)
# # task2

# list2 = list() 
# for i in range(201):
#     if i % 2 == 0 and i % 3 == 0:
#         list2.append(i)
# print(list2)

# # task3
# list3 = list()
# for i in range(101):
#     if i % 2 == 0:
#         list3.append(i**2)
#     else:
#         list3.append(i)
# print(list3)
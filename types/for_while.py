# types = (str, int, float, list, tuple)

# for value in types:
#     print(value, True if '__iter__' in dir(value) else False)


# names_list = ['Ermek', 'Aidana', 'Tima', 'Bermet', 'Zhanylai']

# for name in names_list:
#     if name.lower() == 'aidana':
#         continue
#     print(f'Hi {name}!')


# names_list = ['Ermek', 'Aidana', 'Tima', 'Bermet', 'Zhanylai']
# sred = len(names_list) // 2
# names_list.insert(sred, 'Ramazan')
# for name in names_list:
#     if name ==  'Ramazan':
#         break
#     print(f'Hi {name}!')



# a = bool(23)
# while a:
#     if input('enter message: ') ==  'war drags black'.split(' '):
#         print("You'r BLOKED")
#         break


# 1)input(Email)  2) Show Emails
# test@test.com test@mail.ru Test@gmail.ru


# CRUD - Create Read Update Delete
# DB_EMAILS = []

# while True:
#     print("1) Input Gmail   2) Show db_emails   3) Delete Gmail in DB   4) Stop   5) Rename your Gmail")
#     choices = int(input('enter choice: '))
    
#     if choices == 1:
#         email = input('enter email: ')
#         if email.endswith('@gmail.com'):
#             if email in DB_EMAILS:
#                 print('такой gmail уже существует!!!')
#                 continue
#             DB_EMAILS.append(email)
#         # email = input('enter email: ')
#         # if '@gmail.com' in email:
#             # DB_EMAILS.append(email)
#             continue
#         print('invalid email, only GMAIL.COM!!!')
    
#     elif choices == 2:
#         print(DB_EMAILS)
    
#     elif choices == 3:
#         email = input('enter email: ')
#         if email in DB_EMAILS:
#             # index = DB_EMAILS.index(email)
#             # DB_EMAILS.pop(index)
#             DB_EMAILS.remove(email)
#         else:
#             print(f'{email} не существует!!!')
    
#     elif choices == 4:
#         break

#     elif choices == 5:
#         old_email = input('enter old_email: ')
#         if old_email in DB_EMAILS:
#             new_email = input('enter new email: ')
#             if email.endswith('@gmail.com'):
#                 DB_EMAILS.remove(old_email)
#                 DB_EMAILS.append(new_email)
#     else:
#         print('Error !!!')




'''******************************************************************************************************'''
'''                                      Tasks                                                '''
# # 1 task
# name_of_friends = ['Mura', 'Tima', 'Nurma', 'Sancho', 'Beka']
# for i in name_of_friends:
#     print(i)

# # 2 task
# labels = ['BMW', 'Mercedes', 'Audi']
# for i in labels:
#     print(f'I like brand {i}')

#  3 task
# from math import ceil

# name_of_list = ['Helloworld!']
# string = name_of_list[0]

# mid = ceil(len(string) / 2)
# result = list(string[mid:] + string[:mid])

# print(result)

# 4 task
# list_ = ['world', 'hello']
# new_list = list()
# new_list.append(list_[-1])
# new_list.append(list_[0])
# print(new_list)

# 5 task
# suitcase = list()
# suitcase.append('шорты')
# suitcase.append('футболка')
# suitcase.append('полотенце')
# suitcase.append('одеяло')
# suitcase.append('балон')
# suitcase.pop()
# suitcase.insert(0, 'слансы')
# print(suitcase)

# 6 task
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = list()
# for i in nums:
#     if i < 5:
#         res.append(i)
# print(res)

# 7 task
# list_ = list()
# nums = input().split(',')
# for i in nums:
#     list_.append(i)
# tuple_ = tuple(nums)
# print(list_)
# print(tuple_)

# 8 task
# list_ = list(range(11))
# new_list = list()
# for i in list_:
#     new_list.append(str(i))
# print(new_list)

# 9 task
# list_ = list(range(11))
# new_list = list()
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)

# 10 task
# list_ = list(range(20))
# print(list_)

# 11 task
# list_ = list(range(0, 101, 2))
# print(list_)

# 12 task
# list1 = list(range(0, 10, 3))
# list2 = list(range(5,31, 8))
# list1.extend(list2)
# print(sum(list1))

# 13 task
# asd = input().split(',')
# list_ = list()
# for i in asd:
#     list_.append(i)
# list_.sort()
# print(list_)

# 14 task
# list_ = [1,1,7,3,1,1]
# for i in list_:
#     result = list_.count(i)
#     if result > 1:
#         print('yes')
#         break
# if result == 1:
#     print('ERROR')

# 15 task
# list_ = list()
# for i in range(54, 9184):
#     if i % 5 == 0:
#         list_.append(i)
# print(list_)


'''    
Обработка исключений
Операторы try ... except


                                            ОШИБКИ В КОДЕ(ОШИБКИ)
SyntaxError ->


IndentationalError -> ошибка табуляции(tab)

TabError






                                            ОШИБКИ ПЕРЕДАЧИ ДАННЫХ(ИСКЛЮЧЕНИЯ)
ZeroDivisionError
ArithmeticError
NameError
IndexError
KeyError
ValueError
# Type error
ImportError
# BaseException  #прородитель всех ошибок

'''


# ===========================================================================================================


'''                                              Try ... Except
try:
    <body try>
except:
    <body except>
'''

# num1 = int(input("Введите число: "))
# print(num1)
# print('очень важная строчка кода')


# try:
#     num1 = int(input("Введите число: "))
#     print(num1)
# except:
#     print('Вы ввели некоректные данные. Нужно ввести число!!!')
# print('очень важная строчка кода')


# 1.  import sys

# list_ = [1, 2, 3, 4, 5]
# index = (int(input('Введите индекс: ')))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error')

# 2 Exception as e
# list_ = [1, 2, 3, 4, 5]
# index = (int(input('Введите индекс: ')))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops, we catched {e.__class__} error')

# list_ = [1, 2, 3, 4, 5]
# try:
#     index = (int(input('Введите индекс: ')))
#     res = list_[index]
#     print(res)
# except IndexError:
#     print('Вы ввели некоректный индекс(IndexError!!!)')
# except:
#     print('Вы ввели некоректный символ(ValueError!!!)')


'''Else в Try ... Except
Finaly в Try ... Except'''
'''
try:
    <body>
except:
    <body>
else:
    <body>  # Сработает если в операторе TRY не случилась ошибка
finally:
    <body>  # Сратотает при любом исходе
'''
# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     res = num1 / num2
# except ZeroDivisionError:
#     print('на ноль(0) делить нельзя!!!')
# except ValueError:
#     print('неправильный символ!!!')
# else:
#     res = num1 / num2
#     print(res)
# finally:
#     print('Код завершился')

# cash = int(input())

# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(int(cash))




# try:
#     cash = int(input())
# except ValueError:
#     print('Вы ввели некорректные данные')
# else:
#     if cash < 0:
#         print('Сумма не может быть отрицательной!')
#     else:
#         print(cash)


# try:
#     age = int(input('Введите ваш возраст: '))
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     if age < 18:
#         print('Доступ запрещён')
#     else:
#         print('Спасибо')
# finally:
#     print('До свидания!')

# 1
# try:
#     input1 = input().split()
#     list_ = [int(i)  for i in input1]
#     print(list_)
# except:
#     print('Данный элемент не является числом!')

# 2
# try:
#     input1 = input().split()
#     list_ = list()#[int(i) for i in input1 if i.isdigit()]
# except:
#     for i in input1:
#         if not i.isdigit():
#             print(f'{i} элемент не является числом!')
# else:
#     for i in input1:
#         if i.isdigit():
#             list_.append(i)
#         else:
#             print(f'{i} элемент не является числом!')
#     print(list_)

# 3
# try:
#     input1 = input().split()
#     list_ = [int(i) for i in input1 if i.isdigit()]
#     print(f'{i} is not digit' for i in input1 if not(not i.isdigit()))
#     print(list_)

# except:
#     print('Данный элемент не является числом!')

# a = ['asd','12','sadgw','21','12r','fwq']
# for i in a:
#     if not i.isdigit():
#         print(i)
#     else:
#         print(f'{int(i)} is digit')

# решение сайта
# inp1 = input()

# try:
#     list_ = [int(num) for num in list(inp1.split())]
#     print(list_)
# except:
#     raise TypeError('Данный элемент не является числом!')



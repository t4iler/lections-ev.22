'''                     Фуникция - это именованный блок кода.

def <name_of_function>([<a,b> #параметры]):
    <body> # некий код, некая логика
    <return #возвращаем что-то

<name_of_function>([<5, 6> #аргументы]) 


# Параметры функции -> переменные которые будет принимать наша функция,
для того чтобы мы смогли работать с данными которые передаются в эту функцию


# Аргументы -> данные которые мы передаем для параметров при вызове функции


# return -> нужен для того чтобы функция что-то возвращала
 и для того чтобы мы могли работать с результатом действия функции, 
return является необязательным оператором (возвращает None - если не указать return)
return - срабатывает только 1 раз и функция завершается
'''


# ls = []
# result = ls.append(1)
# print(ls)
# print('Результат действия:',result)

# result1 = ls.pop()
# print(ls)
# print('Результат действия:',result1)

# def sumTwoNums(num1, num2):  #параметры
#     result = num1 + num2
#     # print(result)
#     return result

# print(sumTwoNums(12, 324))  #аргументы


''' без аннотации'''

# def isEven(object):
#     if object % 2 == 0:
#         return True
#     else:
#         return False

# a = 10
# b = int(input('Enter object: '))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b))


"""с аннотацией"""

# def isEven1(object: int) -> bool:
#     '''
#     Наша функция проверяет является ли число, типа int, четным.
#     '''
#     if object % 2 == 0:
#         return True
#     return False

# print(isEven1(5))




# def get_polindrom(words: list) -> list:
#     '''
#     Функция возвращает список из полиндромов
#     '''
#     result = list()
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result
# some_words = ['asdsa', 'Ono', 'asfd', 'baby', 'Kazak', 'pikO', 'aNa', 'LEMAmel']
# print(get_polindrom(some_words))


# def func():
#     print('Hello world')

# func()


# =======================================================================================

# default parameters

# def print_welcome(name: str = 'User') -> str:
#     print(f'Welcome, {name}!')

# # print_welcome('Aibek')
# print_welcome() # (name: str = 'User') #Высвечиваются если аргумент не передали(default parameter)

'''Напишите функцию которая будет возвращать ваш депозит через определенное время
с процентом 10%, возвращать финальное количество денег.Минимальный период вложения 3 года.
Минимальная ставка 30 000 сомов'''

# def get_percentage(money : float, period : int) -> float:
#     '''
#     Return final amount of money!
#     '''
#     if money < 30000:
#         raise Exception(f'Вы не можете заложить {money} сомов! Минимальная ставка 30000 сом')
#     if period < 3:
#         raise Exception('Вы не можете заложить эти деньги на срок меньше 3 лет ')
#     i = 0
#     while i < period:
#         money = money + (money * 0.1)
#         # money = money * 1.1
#         i += 1
#     return money
# money = float(input('Введите сумму денег: '))
# period = int(input("Введите на какой срок хотите заложить ваши деньги: "))
# print(get_percentage(money, period))


'''
"Hello world! My name is John, last name is Snow. Nice to meet you!"
'''


# def get_reversed(string : str) -> str:
#     '''return reversed string.'''
#     spisok = string.split(' ')
#     result = ' '.join(spisok[::-1])
#     print(result)
# string = input()
# get_reversed(string)


# def get_reversed(string : str) -> str:
#     ls = list(string.split(' '))
#     print(*ls[::-1])
# string = input()
# get_reversed(string)




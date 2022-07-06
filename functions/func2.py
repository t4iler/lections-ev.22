# def sum_of_args(a: int, b: int,c: int,d: int) -> int:   #a,b,c,d  Параметры
#     """returns sum of all parameters"""
#     return a + b + c + d
# result = sum_of_args
# print(type(result))
# print(result(5, 10, 15, 20))


# =========================================================================================================

'''                    Позиционные и именованные аргументы
'''

# def printParams(a = None,b = None,c = None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(c = 2, a = 234)


# def sum_of_args(a: int, b: int,c: int,d: int) -> int:   #a,b,c,d  Параметры
#     """returns sum of all parameters"""
#     return a + b + c + d

# print(sum_of_args(1,2,3,4))  # Позиционные аргументы(arguments)
# print(sum_of_args(b = 5, a = 6, d = 234, c = 23)) # Именованные аргументы(keyword arguments)

# print(sum_of_args(5, 2, d = 15, c= 12)) #Смешанные (1:позиционные, 2:именованные)




"""                            Оператор '*'                       """
# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [*a, *b]
# print(c)
# print(*c, end='*')
# print(*c, sep='*')

'''                     *args **kwargs in functions                '''
#                              *args

# def print_scores(student, *scores):
#     print(f'Student name: {student}')
#     # print(scores)
#     for i in scores:
#         print(f'Оценка:',i)

# print_scores('John Snow', 100, 90, 80, 70, 88, 96)


#                             **kwargs

# def print_pet_names(owner, **pets): # **kwargs always dict
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         print(f'{pet}: {name}')
        
# print_pet_names('John Snow', dog = 'Rex', cat = 'Larry', fishes = ['Nemo', 'Dori', 'Alex'], turtle = 'Leonardo')



# def get_some_data(a, b, *args, **kwargs):
#     print('Параметры a и b:', a, b)
#     print(args[0])
#     print(args[1])
#     print(args[-1])
#     print(kwargs['name'])
#     print('Аргументы:', args)
#     print('Именованные аргументы:', kwargs)

# get_some_data(1,2,3,4,5, lang = 'Python', name = 'John Snow', car = 'BMW M5')



# =============================================================================================


# def conc_two_string(str1, str2):
#     import random
#     res = random.randint(1, 10)
#     return str1 + str2 + str(res)

# result = conc_two_string('Hello', 'world')
# print(result)
# ==========================================================================================

# def generate_password(name, last_name):
#     import random
#     random_num = random.randint(100000, 999999)
#     return name + last_name + '_' + str(random_num)

# def get_info():
#     name = input('Enter your name: ')
#     last_name = input('Enter your last_name: ')
#     return generate_password(name, last_name)
# result = get_info()
# print(result)

# =====================================================================================

# def generate_random_string(len_):
#     import string as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_lowercase + s.digits) for i in range(len_)
#         )
#     return random_str

# print(generate_random_string(15))

# =========================================================================================


# def add(num1, num2): return num1 + num2

# def subtrack(num1, num2): return num1 - num2

# def multiply(num1, num2): return num1 * num2

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except:
#         return 'На ноль делить нельзя!!!'
# def main():
#     try:
#         num1 = float(input('Введите первое число: '))
#         num2 = float(input('Введите второе число: '))
#     except:
#         print('Вы ввели некоректные данные')
#         main()
#     operator = input("Введите оператор(+, -, *, .): ")
#     result = None
#     if operator == '+': result = add(num1,num2)
#     elif operator == '-': result = subtrack(num1, num2)
#     elif operator == '*': result = multiply(num1, num2)
#     elif operator == '/': result = divide(num1, num2)
#     else: print('Вы ввели некоректный оператор!!!')

#     print(f'Result: {result}')

#     question = input('Хотите продолжить?(Yes/No): ')
#     if question.lower() == 'yes': main()
#     else: print('Спасибо, что пользовались нашим калькулятором, пока!')

# main()


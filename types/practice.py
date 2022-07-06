'''Логические операторы'''
# задание №1
# number = int(input())
# if number > 0:
#     print(True)
# else:
#     print(False)

# задание №2
# string = input()
# if len(string) > 5:
#     print(True)
# else:
#     print(False)

# задание №3
# mark = int(input())
# if mark >= 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, Ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')

# задание №4
# number = int(input())
# if number > 0:
#     print('positive')
# elif number < 0:
#     print('negative')
# elif number == 0:
#     print('zero')
# else:
    # print('Try again')

# задание №5
# x = 42
# y = 24
# if x > y:
#     print(y)
# else:
#     print(x)

# задание №6
# x = 102
# y = 36
# z = 90
# if x > y and y < z:
#     print(y)
# elif y > x and z > x:
#     print(x)
# else:
#     print(z)

# задание №7
# x = 32
# y = 32
# z = 100
# if x == y and y == z:
#     print(3)
# elif x == y and y != z:
#     print(2)
# else:
#     print(0)

# задание №8
# x = int(input())
# y = int(input())
# if x % y != 0:    
#     print('x не делится на y')
#     print('Частное:', x//y)
#     print('Остаток:', x%y)
# else:
#     print('x делится на y')
#     print('Частное:', x//y)

# задание №9
# year = int(input())
# if year % 4 == 0 and year % 100 !=0:
#     print('YES')
# else:
#     print('NO')

# задание №10
# nums = [1, 15, 36, 88]
# target = 15
# if target in nums:
#     print('Да')
# else:
#     print('Нет')

# задание №11
# num = int(input())
# if 64 < num < 91 or 96 < num < 123:
#     print(f'Это буква "{chr(num)}"')
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')

# задание №12
# greeting = input()
# if greeting == 'Hi':
#     print('Привет!')
# else:
#     print('NO')

# задание №13
# count = 0
# number = input()
# if number.isdigit():
#   count = int(number)
# else:
#   count = 0
# print(count)



# import random

# ls = ['Плов', 'Манты', 'Куурдак', 'Лагман']

# p = 0
# m = 0
# k = 0
# l = 0

# for i in range(10000):
#     choice = random.choice(ls)
#     # print(choice)
#     if choice.lower() == 'плов':
#         p += 1
#     elif choice.lower() == 'манты':
#         m += 1
#     elif choice.lower() == 'куурдак':
#         k += 1
#     else:
#         l += 1
# # print(dir(random))
# dict1 = {
#     'Плов': p, 
#     'Манты': m, 
#     'Куурдак': k, 
#     'Лагман': l
# }
# print(dict1)


'''====================================================================================='''

def count_(steps, path):
    sea_level = 0
    count_valleys = 0
    for i in path:
        if i.lower() == 'u':
            sea_level += 1
            if sea_level == 0:
                count_valleys += 1
        elif i.lower() == 'd':
            sea_level -= 1
        
    return count_valleys

print(count_(10, 'dduudduduu'))

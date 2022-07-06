# String - Строки
'''
Строки - это набор последовательных символов, 
которые мы используем для хранения и представления текстовой информации.
'''
# name = 'John'
# name1 = '''
# John
# Snow
# '''
# name2 = str("John Snow")
# print(name, name1, name2, sep='\n')
# print(type(name))
# print(type(name1))
# print(type(name2))


'''Экранирование - это маханизм при помощи которого можно вставлять символы,
 которые сложно ввести с клавиатуры.

#  \n -> перенос строки
#  \t -> горизонтальная табуляция
#  \f -> перевод страницы
#  \r -> возврат указателя(коретки)
#  \v -> вертикальная табуляция
'''

# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'
# print(name)
# print(lastName)
# print(last_name)


''' Индексация символов в строке'''

# name = 'John'

# print(name[0])   #j
# print(name[-1])  #n
# print(name[2])   #h


''' Срезы по индексам

string[start: end: step] '''

# text = 'Hello world! My name is John Snow!'
# print(text[0:5])
# print(text[13:-1])
# print(text[13:])

# print(text[::2])
# print(text[::-1])
# print(text[::-2])
# print(text[:12:-1])

''' len() - выводит длину строки'''

# print(len('hello world'))
# name = 'John Snow'
# print(len(name))



'''Конкатенация строк(соединение)'''

# word1 = 'Hello'
# word2 = 'world'
# probel = ' '

# result = word1 + probel + word2 + '!'

# print(result)
# print(word1 + probel + word2 + '!!!')


'''Форматирование строк'''

# 1.  с помощью %
# 2. с помощью .format()
# 3. Интерполяция строк (f-строки)


# 1. (%)

# name = input('Enter your name: ')
# last_name = input('Enter your surname: ')
# print('Hello, mr/mrs %s %s!' %(name, last_name))

# 2. (.format)

# name = input('Enter your name: ')
# last_name = input('Enter your surname: ')
# print('Hello, mr/mrs {} {}!'.format(name, last_name))


# 3. f-строки

# name = input('Enter your name: ')
# last_name = input('Enter your surname: ')
# print(f'Hello, mr/mrs {name} {last_name}!')
# print('Hello, mr/mrs', name, last_name)
# print('Hello, mr/mrs ' + name + ' ' + last_name)
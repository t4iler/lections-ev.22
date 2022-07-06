# Методы строк 

'''dir() - Функция которая вытаскивает методы типов данных.'''

# print(dir(str))

''' '<соединитель>'.join(<массив который нужно соединить>) - соединяет массив строк по соединителю в одну строку '''

# ls = ['Milk', 'Bread', 'Water', 'Apple']

# joined = '!'.join(ls)
# print(joined)
# print(joined, end='!\n')


'''split(разделитель) -> Дробит строку по разделителю и возвращает тип данных list().'''

# text = 'Milk, Bread, Water, Apple'
# spliter = text.split(', ')
# print(spliter)
# joined = ', '.join(spliter)
# print(joined)


'''replace(<old value>, <new value>, [count])
-> Меняет в строке значение old на new value, если вы укажете countб то он заменит count раз'''


# text = 'ha ha ha ha ha'
# result1 = text.replace('ha', 'La')
# result2 = text.replace('ha', 'La', 3)
# print(result1)
# print(result2)

# text = 'ha ha ha ha ha'
# result = text[:3] + text.replace('ha', 'La', 1)

# print(result)


'''strip() - Убирает пробельные символы в начале и конце строки.'''

# rstrip() - В конце удаляет
# lstrip() - В начале удаляет

# text = input('Введите ФИО: ')
# result = text.lstrip()
# print(text.strip())
# print(text)
# print(result)


'''count('<simbol>') -> Считает количество вхождений <simbol> в строку'''

# text = "Hello world! I\'m from Earth"
# text = 'Hello world! I\'m from Earth'

# result = text.count('l')

# print(result)


''' index('<value>', [start], [end]) -> выводит индекс значения value в нашей строке. '''

# text = 'Hello world! This is Makers!'
# result = text.index('!')
# print(result)
# print(len(text))
# print(text.find('h'))


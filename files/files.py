"""
                                    Работа с файлами
"""
'''
Каретка - Указатель |
'''


'''
file = open(<путь до нашего файла(абсолютный путь, относительный)>)
'''
# file = open('/home/hello/Desktop/ev.22/files/files.py') # Абсолютный путь
# file = open('files.py') # Относительный путь

# print(file)     

'''
Режимы для работы с файлами:

1. r/ r+ (read)  
2. w/ w+ (write)     Если открыть не существующий файл, то создастся новый
3. a/ a+ (append)
    t, b, x
4.
...
'''
'''                                                 R                                               '''
# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))
# file.close()

# file = open('/home/hello/Desktop/ev.22/files/files.py')
# data = file.readlines()
# print(data)
# file.close()

# file = open('/home/hello/Desktop/ev.22/files/text.txt')
# data = file.readlines()
# print(data)
# file.close()

'''                                         W                                                   '''
# file = open('text.txt', 'w')
# file.write('Hello world!\nMy names is John Snow!\nI\'m North King!')
# file.close()



# file = open('text.txt', 'w+')
# file.write('Hello world!\nMy names is John Snow!\nI\'m North King!')
# file.close()

'''                                         A                                                   '''

# file = open('text.txt', 'a')
# file.write('\nJohn Snow bastard and King')
# file.close()

'''Контекстный менеджер'''

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)
# print(data) # Ошибка


''' write vs writelines'''

# ls = ['Hello world', 'My name is John', 'I\'m 35 years old']
# with open('text.txt', 'w') as f:
#     f.writelines(line+'\n' for line in ls)

'''
file.tell() -> возвращает индекс где находится каретка(указатель)

file.seek() -> Перемещает каретку(указатель) на указанный индекс(int(index))
'''

# =============================================================================================================

from PIL import Image
import pytesseract
import re

def get_imei_codes(list_images):
    list_of_imei = list()
    for image in list_images:
        string = pytesseract.image_to_string(image)
        print(string)
        list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
        print(list_of_imei)

        with open('imeicodes.txt', 'w') as file:
            for x in list_of_imei:
                for i in x:
                    file.write(f'{i}\n')

list_images = ['imei.jpg']
get_imei_codes(list_images)
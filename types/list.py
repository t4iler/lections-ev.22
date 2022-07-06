''' list()(список, массив) - изменяемый, последовательный тип данных,
 который представляет из себя коллекцию каких либо объектов'''

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# 1. -->  list(<interable>)
# my_list = list('Hello world')
# print(my_list)

# tuple_ = ('banana', 'apple', 'cherry')
# print(tuple_)
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))


# 2. range() -> возвращает последовательность элементов (числа)

# a = list(range(1, 100, 2))
# print(a)


# 3. -> []
# my_list = []
# print(type(my_list))
# print(my_list)
'''
print(dir(list))
'''
# append(element) - Добавляет element в конец списка

# list_ = [1, 2, 3, 4]
# print(list_)
# list_.append(5)
# list_.append([1, 2, 3, 4])
# print(list_) 


# extend(element[iterable]) -> расширяет список добавляя element в конец.
# list_ = [1, 2, 3, 4]
# list_.extend('hello')
# print(list_)
# list_.extend([1, 2, 3])
# print(list_)

# insert(<index>, <element>) -> добавляет element по указанному index

# list_ = ['string', 2, 3, False]
# print(list_)
# list_.insert(1, [1, 2, 3 ,None])
# print(list_)
# list_.insert(2, 1)
# print(list_)
# print(list_[-1])
# print(list_[1][3])
# print(list_[2:5])
# print(len(list_))

# index(element, [start], [end]) - возвращает индекс elementa
# ls = [1, 2, 33, 3, 4, 5, 5, 7, 2, 'hello']
# print(ls.index(5, 6))

# if 'hello' in ls:
#     print(f'"hello" is in list:{ls.index("hello")}')


# count(element) -> возвращает количество вхождений element в списке

# ls = [1, 2, 3, 5, 3, 5, 4, 5, 1]
# result = ls.count(5)
# print(result)

# remove(element) - удаляет element, но если такого elementa нет в списке, то выводит ошибку
# pop([index]) - удаляет и возвращяет element по index, но если index не указан,
#  то удаляет последний element 

# ls = [5, 3, 2, 5, 2, 4, 5, 3, 2]
# ls.remove(5)
# ls.remove(5)
# ls.remove(2)
# print(ls)
# del ls[-1]
# print(ls)
# deleted = ls.pop(3)
# print(deleted)


'''
sort([reverse=True/False], [key=<>]) -> сортирует список. Если в аргументах передан reverse=True, 
то список будет отсорирован в убывающем порядке. 
'''

# ls = [5, 0, -2, -101, 102, 23, 1]
# print(ls)
# ls.sort()
# print(ls)
# ls.sort(reverse = True)
# print(ls)

# ls = ['hello', 'john', 'London', 'a']
# ls.sort()
# print(ls)

# ls = ['hello', 'john', 'London', 'a']
# ls.sort(key=len)
# print(ls)
# ls = ['hello', 'john', 'London', 'a']
# ls.sort(key=len, reverse=True)
# print(ls)

'''Изменение списка'''

# ls = [1, 'h', 3]
# ls[1] = 2
# print(ls)
# print(dir(tuple))
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
#         list3.append(i**3)
# print(list3)


                                # list comprehenssion
# list3 = [i**2 if i%2==0 else i**3 for i in range(101)] 
# print(list3)

'''*********************************************************************************************************


list comprehenssions -> генераторы списка
'''

# newlist = [expression for item in interable  <if condition == True > ]

'''
list comprehenssions - это упрощщенный подход к созданию списка, который задействует цикл "for",
a также конструкции "if-else" для определения того, что в итоге окажется добавлено в наш список.
 "for  +++speed"
'''
# ls = list()
# for i in range(0, 101, 2):
#     ls.append(i)                  # обычная операция                      
# print(ls)


# new_list1 = [i for i in range(0, 101, 2)]
# print(new_list)                                     
# new_list2 = list(range(0, 101, 2))                #list comprehenssions
# print(new_list2)




                                        # EXAMPLES:

# ls = [i**2 for i in range(11)]
# print(ls)


# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon', 'cherry']
#                 #capitalize words
# ls = [x.capitalize() for x in fruits]
# print(ls)
#                 #another operation
# ls = [i for i in fruits if 'a' in i]
# print(ls)
#                 #another operation, if i == cherry
# ls = [i for i in fruits if i == 'cherry']
# print(ls)
#                 #another operation, without apple
# ls = [i for i in fruits if i != 'apple']
# print(ls)

'''======================================================================================================='''

                    #USUALL OPERATION
# list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ls = []
# for inner_list in list_:
#     for num in inner_list:
#         ls.append(num)
# print(ls)

                    #list comprehenssion
# list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ls = [num for inner_list in list_ for num in inner_list]
# print(ls)

#                                 # посмотреть время выполнения  обычной операции
# import datetime
# ls = list()
# start = datetime.datetime.now()
# for i in range(1, 100_000_000):
#     ls.append(i)
# finish = datetime.datetime.now()
# print(finish - start)

#                                 # посмотреть время выполнения list(range)
# import datetime
# start = datetime.datetime.now()
# ls = list(range(1, 100_000_000))
# finish = datetime.datetime.now()
# print(finish - start)

#                                 # посмотреть время выполнения list comprehenssion
# import datetime
# start = datetime.datetime.now()
# ls = [i for i in range(1, 100_000_000)]
# finish = datetime.datetime.now()
# print(finish - start)

'''==================================================================================================='''


# ls = [x+10 if x == 8 else x + 1 for x in range(10)]
# print(ls)

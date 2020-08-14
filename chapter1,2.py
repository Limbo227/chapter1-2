# #1
# a = [1, 2, 2, 4, 11, 2, 3, 1]
# print(set(a))
# #2
# a = ['John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom']
# a.pop(0)
# a.pop(3)
# a.pop(3)
# print(a)
# #3
# a = [1,2,3,4,5,6,7,8,9]
# a.reverse()
# print(a)
# #4
# a = [1,2,3,4,5,6,7,8,9]
# a.pop(4)
# a.insert(4,7)
# print(a)
# #5
words = input('words').split()
#6
# dict = {'name':'имя','pen':'ручка','lastname': 'фамилия','age':'возраст'}
# word = input('word')
# if word == 'name':
#     print('word is in the dict')
# elif word == 'pen':
#     print('word is in the dict')
# elif word == 'lastname':
#     print('word is in the dict')
# elif word == 'age':
#     print('word is in the dict')
# else:
#     print('word is not in dict')
# #7
# dict = {'name':'имя', 'lastname':'фамилия','work':'работа'}
# dict2 = {'Aito':'IT','Bakai':'games'}
# dict3=dict.copy(),dict2.copy()
# print(dict3)
#8
# #9
# dict = {'Hello':'Privet'}
# if dict == {}:
#     print('empty,retry')
# else:
#     print('dict has a value')
#10
# list = ['Bakai','Bogdan','Aito','Kirill']
# list.append('Arsen')
# list.append('Alex')
# list.append('Turat')
# list = tuple(list)
# print(list)
#11
# login = input('login:')
# password = input('password:')
# data = {'login':login,'password':password}
# print(data)
#12
# soglasnye = 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф','х', 'ц', 'ч', 'ш', 'щ'
# glasnye = 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'
# letter = input('букву:')
# for x in soglasnye:
#     for y in glasnye:
#         if letter == x:
#             print(letter,'буква согласная')
#         if letter == y:
#             print(letter,'буква гласная')
# 13
# apples = int(input('numbers of apple'))
# students = int(input('numbers of students'))
# if apples>=students:
#     applesleft = apples-students
#     print('enough apples for students')
#     print(applesleft,'apples left')
# else:
#     print('not enough apples')
#14
# students = int(input('students:'))
# desks = (students//2 + students%2)
# print(desks)
#15
# dogage = int(input('dog age:'))
# dogsize = input('size')
# if dogsize == 'small':
#     print(dogage*9)
# elif dogsize == 'medium':
#     print(dogage*10.5)
# elif dogsize == 'large':
#     print(dogage*12.5)
# #16
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# num3 = int(input('num3:'))
# if num1 > 10 and num2>10 and num3>10:
#     print('yes')
# else:
#     print('no')
#17
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# num3 = int(input('num3:'))
# count = 0
# if num1 > 0:
#     count = count +1
#     print('positive')
# elif num1 < 0:
#     print('negative')
# if num2 > 0:
#     count = count +1
#     print('positive')
# elif num2 < 0:
#     print('negative')
# if num3 > 0:
#     count = count +1
#     print('positive')
# elif num3 < 0:
#     print('negative')
# print('положительных чисел:',count)
#18
# num = int(input('num:'))
# step = int(input('step:'))
# if num < 100:
#     print('num is okay')
#     result = num**step
#     print(result)
# else:
#     print('num is too big')
#19
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c
# print(m)
#20
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# if c > a > b or b > a > c :
#     print(a)
# elif a > b > c or c > b > a:
#     print(b)
# else:
#     print(c)
'''Задание 1. Среднее'''

'''from random import randint
number_1 = (randint(0, 100))
number_2 = (randint(0, 100))
number_3 = (randint(0, 100))
result = ((number_1+ number_2+ number_3)/3)
print('Рандомные числа:',number_1 , number_2 ,number_3,'\nСреднее значение: ' ,result)'''

'''Задание 2. Деление и еще раз деление'''

'''from random import randint
number_1 = (randint(0, 100))
number_2 = (randint(0, 100))

print('Рандомные числа:',number_1 ,number_2 ,'\n', number_1//number_2, number_1%number_2)'''


'''Задание 3. Округление'''
'''import random
random_number = 14.321
print('{0:=.2f}'.format(random_number))
print('{0:=.0f}'.format(random_number))
print(f'{random_number:0{11}}')'''


'''Задание 4. Число "наоборот'''
print(int(str(input('Введите число: '))[::-1]))


'''Задание 5. Число "наоборот"(усложненное)'''
a = int(input("Введите число: "))
if a < 0:
print("-" + str(a)[:0:-1])

elif a == 0:
print(a)

else:
print(str(a)[::-1])

"""1 задание"""
'''name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
print('Hello, ' + name, surname +'! You just delved into Python. Great start!')'''

"""2 задание"""

'''thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
'''

"""3 задание"""
'''text = "hello world"
print(text.title())'''


"""4 задание"""

'''
amount = 100500.157
print('{:7,.2f}'.format(amount))  '1 вариант'
print(f'{amount:7,.2f}')  '2 вариант'
'''

"""5 задание"""

'''height = int(input('Введите ширину коврика: '))
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('Макет коврика'.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))
'''


"""6 задание"""

'''
value = input('Введите число: ')
result = 1
for i in range(len(value)):
    if int(value[i]) == 0:
        pass
    else:
        result = result * int(value[i])
print(result)
'''


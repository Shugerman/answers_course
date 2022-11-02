"Задание 1. Fizz Buzz "

"""number = int (input('Введите число: '))

if number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(str(number))
"""

"Задание 2. Оценка числа "

"""x = int (input('Введите число: '))

if x % 2 != 0:
    print('Плохо')
elif 2 <= x <= 5 and x % 2 == 0:
    print('Неплохо')
elif 6 <= x <= 20 and x % 2 == 0:
    print('Так себе')
elif x >= 20 and x % 2 == 0:
    print('Отлично')"""

"Задание 3. Последовательность "

"""N = int(input())

for i in range(1,N+1):
    print(i, end='')"""

'''"Задание 4. Секретное сообщение "
text = str(input('Введите кусок текста: '))
for i in text:
    if i.istitle():
        print(i, end='')
    else:
        pass
'''

"Задание 5. Три слова"
'''text = input('Введите строку ').split(' ')
print(text)
count = 0
for word in text:
    if word.isdigit():
        count = 0
    elif not word.isdigit():
        count += 1
        if count >= 3:
            print(True)
            break

if count < 3:
    print(False)
'''
"Задание 6. Мир захватили левши"

input = ["bright aright", "ok"]
print(",".join(input).replace("right","left"))
from random import randint
import time
#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
n=input('Введите количество партий ')
sum1=0
sum2=0

for i in range(int(n)):
    print('Номер партии: ', i+1)
    print('Кубик бросает', igrok1)
    time.sleep(1)
    n1 = randint(1, 6)
    sum1 = sum1+n1
    print('Выпало:', n1, 'Сумма1=', sum1)

    print('Кубик бросает', igrok2)
    time.sleep(1)
    n2 = randint(1, 6)
    sum2 =sum2 +n2
    print('Выпало:', n2, 'Сумма2=', sum2)

if sum1 > sum2:
    print('Выиграл', igrok1)
    print('Сумма баллов', sum1)
elif sum1 < sum2:
    print('Выиграл', igrok2)
    print('Сумма баллов', sum2)
else:
    print('Ничья')
    print('Сумма баллов', sum1)
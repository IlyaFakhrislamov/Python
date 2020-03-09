#1
a = 1
b = 3
c = input('Введите строку или цифру\n')
d = input('Введите строку или цифру\n')
print('Результат: ', a, ',', b, ',', c, ',', d)


#2
a = input('Введите время в секундах\n')
if not a.isdigit():
    print('Нужно указать число')
else:
    a = int(a)
    hour = a // 3600
    minute = (a // 60) % 60
    sec = a % 60
    print(f'{hour:>02}:{minute:>02}:{sec:>02}')


#3
a = input('Введите число\n')
if not a.isdigit():
    print('Нужно указать число')
else:
    b = a + a
    c = a + a + a
    print(int(a) + int(b) + int(c))


#4
a = input('Введите целое положительное число\n')
if not a.isdigit():
    print('Нужно указать число')
else:
    a = int(a)
    b = a % 10
    a = a // 10
    while a > 0:
        if a % 10 > b:
            b = a % 10
        a = a // 10
    print(b)


#5
a = input('Введите выручку\n')
b = input('Введите издердки\n')
a = int(a)
b = int(b)
if a > b:
    print('Фирма отработала c прибылью.', 'Рентабельность - ', (a - b) / a)
    c = input('Введите количетсво сотрудников\n')
    c = int(c)
    print('Прибыль на одного сотрудника - ', (a - b) / c )
elif a < b:
    print('Фирма отработала в убыток')
else:
    print('Фирма отработала в ноль')


#6
a = input('Введите количество километров в первый день\n')
b = input('Введите сколько километров должен пробежать\n')
a = int(a)
b = int(b)
c = 1
while a < b:
    a *= 1.1
    c += 1
print('Ответ: на', c, '-й день спортсмен достиг результата — не менее', b,'км')
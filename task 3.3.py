'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
def my_func(*args):
    a = input('Введите число а:  ')
    b = input('Введите число b:  ')
    c = input('Введите число c:  ')
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and a < c:
        return a + c
    elif a >= c and b >= c:
        return a + b
    else:
        return b + c

print(my_func())
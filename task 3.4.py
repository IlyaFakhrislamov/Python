'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
def my_func(*args):
    x = input('Введите действительное положительное число ')
    y = input('Введите целое отрицательное число ')
    x = float(x)
    y = int(y)
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return print(result)
    else:
        return print(1 / result)

my_func()
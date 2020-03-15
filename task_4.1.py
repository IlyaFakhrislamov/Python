'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv

def my_salary (job, t, bonus):
    return (job * t) + bonus

_, t, job, bonus, *a = argv

try:
    job, bonus = float(job), float(bonus)
    t = int(t)
except TypeError as e:
    print(e)
    raise TypeError

print(my_salary(job, t, bonus))

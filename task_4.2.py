'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''
import random

my_list = [random.randint(1, 20) for _ in range(10)]
result = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(my_list)
print(result)
'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from os import path

file_name = 'task_5.5.txt'
file_path = path.join(path.dirname(__file__), file_name)

list_num = []
while True:
    try:
        num = input('Введите число: ')
        num = float(num)
        list_num.append(str(num))
    except ValueError:
        print('Введено не число')
        break

with open(file_path, 'w', encoding='utf-8') as file_write:
    print(f'{" ".join(list_num)}', file=file_write)

with open(file_path, 'r', encoding='utf-8') as file_read:
    num_list = file_read.readline().split()
    nums_sum = 0
    for _ in num_list:
        nums_sum += float(_)

print(f'Сумма: {nums_sum}')
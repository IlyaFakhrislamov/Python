'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
from os import path

file_name = 'task_5.3.txt'
file_path = path.join(path.dirname(__file__), file_name)
file = open(file_path, 'r',  encoding='utf-8')

lines = file.readlines()
sum = 0
for _ in lines:
    line = _.split()
    if (float(line[1]) < 20000):
        print(f'У {line[0]} оклад менее 20 тыс р.')
    sum += float(line[1])

sum = sum / len(lines)
print(f'Средняя зп: {sum} р.')
file.close()

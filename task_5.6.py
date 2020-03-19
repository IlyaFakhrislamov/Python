'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
from os import path
from re import sub

file_name = 'task_5.6.txt'
file_path = path.join(path.dirname(__file__), file_name)

def hours(line: str):
    line_hours = sub(r"\D", ' ', line)
    sum = 0
    for _ in line_hours.split():
        sum += float(_)
    return sum

my_dict = {}
with open(file_path, 'r', encoding='utf-8') as file_read:
    for _ in file_read.readlines():
        lines = _.split(': ')
        my_dict[lines[0]] = hours(lines[1])

print(f'Результат: {my_dict}')
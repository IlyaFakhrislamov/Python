'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
from os import path

file_name = 'task_5.4.txt'
file_name2 = 'task_5.4_rus.txt'
file_path = path.join(path.dirname(__file__), file_name)
file_path2 = path.join(path.dirname(__file__), file_name2)
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(file_path, 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open(file_path2, 'a', encoding='utf-8') as file_write:
    for _ in lines:
        row = _.split()
        row[0] = my_dict[row[0]]
        print(' '.join(row), file=file_write)
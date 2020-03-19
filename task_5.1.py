'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
from os import path

file_name = 'task_5.1.txt'
file_path = path.join(path.dirname(__file__), file_name)
file = open(file_path, 'a',  encoding='utf-8')

while True:
    string = input('Введите строку: ')

    if not string:
        file.close()
        print('Выход')
        break

    file.write(f'{string}\n')


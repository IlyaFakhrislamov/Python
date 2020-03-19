'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''
from os import path

file_name = 'task_5.2.txt'
file_path = path.join(path.dirname(__file__), file_name)
file = open(file_path, 'r',  encoding='utf-8')
lines = file.readlines()

print(f'В файле {len(lines)} строк(и)')
i = 1
for _ in lines:
    print(f'В {i}-й строке: {len(_.split())} слов')
    i+=1
file.close()
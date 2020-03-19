'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
from os import path
from json import dump

file_name = 'task_5.7.txt'
file_name2 = 'task_5.7.json'
file_path = path.join(path.dirname(__file__), file_name)
file_path2 = path.join(path.dirname(__file__), file_name2)

result = []
profit = {}
average = []

with open(file_path, 'r', encoding='utf-8') as file_read:
    while True:
        line = file_read.readline().split()
        if not line:
            break
        profit[line[0]] = float(line[2]) - float(line[3])
        if profit[line[0]] > 0:
            average.append(profit[line[0]])

result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_path2, 'w', encoding='utf-8') as file_write:
    dump(result, file_write)
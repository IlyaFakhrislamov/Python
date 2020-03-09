# 1
my_list = [3, 2, 'тип', 2.4, True]
i = 0
for i in my_list:
    print(i, ': ', type(i))


# 2
my_list = input('Введите элементы списка через пробел\n')
my_list = my_list.split()
tmp = 0
for i in range(int(len(my_list) / 2)):
    my_list[tmp], my_list[tmp + 1] = my_list[tmp + 1], my_list[tmp]
    tmp += 2
print(my_list)


# 3
while True:
    month = input('Введите месяц\n')
    if month.isdigit():
        month = int(month)
        months_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
        months_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',
                       9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
        if 1 <= month <= 12:
            print('List:', months_list[month - 1], 'Dict:', months_dict.get(month))
        else:
            print('В году 12 месяцев. Указано число вне диапазона')
        break
    else:
        print('Введено не число\n')


# 4
my_list = input('Введите элементы списка через пробел\n')
my_list = my_list.split()
for ind, my_list in enumerate(my_list, 1):
    print(ind, my_list[:10])


# 5
my_list = [7, 5, 3, 3, 2]
# print(my_list, my_list.index(3) + my_list.count(3))
value = input('Введите новый элемент рейтинга\n')
value = int(value)
for i in range(len(my_list)):
    if my_list[i] == value:
        my_list.insert(my_list.index(value) + my_list.count(value), value)
        break
    elif my_list[0] < value:
        my_list.insert(0, value)
    elif my_list[-1] > value:
        my_list.append(value)
    elif my_list[i] > value and my_list[i + 1] < value:
        my_list.insert(i + 1, value)
        break
print(my_list)


# 6
goods = input("Введите количество товаров ")
goods = int(goods)
n = 1
my_dict = {}
my_list = []
my_analytic = {'название': [], 'цена': [], 'количество': [], 'eд': []}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    for i in my_dict.keys():
        my_analytic[i].append(my_dict[i])
    n += 1
print(my_analytic)


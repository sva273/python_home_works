"""
1. Прогрессия увеличения
Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке. Добавить в него
только элементы, которые больше всех предыдущих значений в исходном кортеже.
Данные:
numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)
"""
from itertools import count
#
# numbers = (3, 7, 2, 8, 5, 10, 1)
#
# res = [numbers[0]]
# max_nummer = numbers[0]
#
# for nummer in numbers[1:]:
#     if nummer > max_nummer:
#         res += [nummer]
#         max_nummer = nummer
# result = tuple(res)
# print("Ascending tuple:", result)

"""
2. Повторяющиеся элементы
Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. Вывести сами элементы 
и их индексы.
Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9
Индексы элемента 3: 2 6
Индексы элемента 4: 3 8
"""
# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# index_num = []
# index_res = []
#
# for i in range(len(numbers)):
#     actual = numbers[i]
#     if actual not in index_num:
#         count = numbers.count(actual)
#         if count > 1:
#             indexes = []
#             for k in range(len(numbers)):
#                 if numbers[k] == actual:
#                     indexes += [k]
#             index_res += [(actual, indexes)]
#         index_num += [actual]
#
# for value, indexes_list in index_res:
#     index_str = ' '.join([str(i) for i in indexes_list])
#     print(f"Индексы элемента {value}: {index_str}")


# так улучшил ChatGpt

# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# index_num = []      # элементы, которые уже обработали
# index_res = []       # список кортежей вида (число, [индексы])
#
# # Перебор с использованием enumerate для получения индекса и значения
# for idx, num in enumerate(numbers):
#     if num not in index_num:
#         if numbers.count(num) > 1:
#             # Список индексов, где встречается num, через списковое включение
#             indexes = [i for i, value in enumerate(numbers) if value == num]
#             index_res += [(num, indexes)]
#         # Помечаем число как уже обработанное
#         index_num += [num]
#
# # Вывод результата, конструируя строку индексов через генераторное выражение
# for value, indexes in index_res:
#     indexes_str = ' '.join(str(i) for i in indexes)
#     print(f"Индексы элемента {value}: {indexes_str}")
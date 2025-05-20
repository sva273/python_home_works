"""
1. Не уникальные числа
Напишите программу, которая находит все числа, встречающиеся более одного раза в списке, и выводит их в порядке убывания.

Данные:
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

Пример вывода:
Числа, встречающиеся более одного раза: [7, 4, 3, 8]
"""

from collections import Counter

numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]


# Подсчитываем количество вхождений каждого числа
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Отбираем числа, которые встречаются более одного раза
repeated = [num for num, count in frequency.items() if count > 1]

sorted_keys = sorted(repeated, reverse=True)
print("Числа, встречающиеся более одного раза:", sorted_keys)


n = len(repeated)
for i in range(n):
    for j in range(i + 1, n):
        a = repeated[i]
        b = repeated[j]
        if frequency[a] < frequency[b] or (frequency[a] == frequency[b] and a < b):
            repeated[i], repeated[j] = repeated[j], repeated[i]

print("Числа, встречающиеся более одного раза:", repeated)

"""
2. Проверка подмножества Задача:
Напишите программу, которая проверяет, является ли один словарь подмножеством другого 
(т.е. все его пары "ключ-значение" содержатся в другом словаре).
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

Пример вывода:
Первый словарь является подмножеством второго.
"""
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

# Проверка: dict2 и dict1 (по парам ключ-значение)
is_dict2_subset = True
for key in dict2:
    if key not in dict1 or dict2[key] != dict1[key]:
        is_dict2_subset = False
        break

# Проверка: dict1 и dict2 (по парам ключ-значение)
is_dict1_subset = True
for key in dict1:
    if key not in dict2 or dict1[key] != dict2[key]:
        is_dict1_subset = False
        break

if is_dict2_subset:
    print("Второй словарь является подмножеством первого.")
elif is_dict1_subset:
    print("Первый словарь является подмножеством второго.")
else:
    print("Ни первый, ни второй не являются подмножеством друг друга.")


"""
3. Из чисел в слова
Напишите программу, которая заменяет числовые значения в словаре на их строковое представление (например, 1 → "один").
Используйте заранее подготовленный словарь чисел.

Данные:
Словарь сопоставлений
number_to_word = {1: "один", 2: "два", 3: "три"}
Исходные данные
data = {"x": 1, "y": 2, "z": 3}
Пример вывода:
{'x': 'один', 'y': 'два', 'z': 'три'}

"""
number_to_word = {1: "один", 2: "два", 3: "три"}
data = {"x": 1, "y": 2, "z": 3}

rev_dict ={}

for key in data:
    rev_dict[key] = number_to_word[data[key]]

print(rev_dict)




number_to_word = {1: "один", 2: "два", 3: "три", 4: "четыре"}
data = {"x": 1, "y": 2, "z": 3}

new_paar = {}

if len(number_to_word) != len(data):
    print("Несоответствие по количеству")
else:
    for key in data:
        num = data[key]
        if num in number_to_word:
            new_paar[key] = number_to_word[num]

    number_to_word.clear()
    number_to_word.update(new_paar)

    print(number_to_word)




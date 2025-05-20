"""
1. Объединение данных в строку
Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари) и возвращает их
строковое представление, объединённое через " | ". Добавьте документацию и аннотации типов для всех параметров и
возвращаемого значения.

Данные:

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

Пример вывода:

42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
"""
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

from typing import Any

def join_dates(data: list[Any]) -> str:
    """
    Convert the list items into a string and join them using " | ".

    :param data:List[Any]: List of elements of various types (numbers, strings, lists, dictionaries).
    :return: String with elements separated by " | ".
    """
    return " | ".join(str(item) for item in data)

print(join_dates(data))

"""
2. Сумма вложенных чисел
Напишите функцию, которая принимает список словарей, где каждый словарь содержит имя пользователя и список баллов. 
Функция должна вернуть сумму всех чисел. Добавьте документацию и аннотации типов для всех параметров и возвращаемого 
значения.

Данные:

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

Пример вывода:

Итоговый балл: 156
"""

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

def sum_scores(data: list[dict[str, list[int]]]) -> int:
    """
     Counts the sum of all the values in the nested "scores" lists in the dictionary.

    :param data:list[dict[str, list[int]]] List of dictionaries, each containing the keys "name" and "scores".
    :return: The sum of all the numbers in the 'scores' list.
    """

    return sum(score for user in data for score in user["scores"])
total = sum_scores(data)
print(f"Final score: {total}")


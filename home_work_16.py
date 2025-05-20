"""
1. Оценки текстом
Напишите программу, которая преобразует список оценок по системе от 1 до 5 в текстовое представление.
Нужно сохранить в списках числовой результат и текстовое представление. Где, 5 — "отлично", 3-4 — "хорошо",
а 2 и ниже — "неудовлетворительно".

Данные:
grades = [5, 3, 4, 2, 1, 5, 3]

Пример вывода:

[[5, 'отлично'], [3, 'хорошо'], [4, 'хорошо'], [2, 'неудовлетворительно'], [1, 'неудовлетворительно'],
[5, 'отлично'], [3, 'хорошо']]
"""
from inspect import stack
from selectors import SelectSelector

# grades = [5, 3, 4, 2, 1, 5, 3]
#
# # С циклом for
#
# grades = [5, 3, 4, 2, 1, 5, 3]
# modified_grades = []
# for grade in grades:
#     if grade == 5:
#         modified_grades.append([grade, 'отлично'])
#     elif grade == 2 or grade == 1:
#         modified_grades.append([grade, 'неудовлетворительно'])
#     else:
#         modified_grades.append([grade, 'хорошо'])
#
# print(modified_grades)
# #
# # # List comprehension
#
# grades = [5, 3, 4, 2, 1, 5, 3]
# modified_grades = [
#     [grade, 'отлично'] if grade == 5 else
#     [grade, 'неудовлетворительно'] if grade in [1, 2] else
#     [grade, 'хорошо']
#     for grade in grades]
# print(modified_grades)

"""
2. Правильные скобки
Напишите программу, которая принимает строку, содержащую любые виды скобок — круглые (), квадратные [] и фигурные {}.
Необходимо проверить, правильно ли они расставлены. Скобки считаются правильно расставленными, если:
Каждая открывающая скобка имеет соответствующую закрывающую.
Скобки закрываются в правильном порядке.
Пример данных:

string = "({[}])"

Пример вывода:

Скобки: ({[}])
Валидны: False

Скобки: ([({}()){}])
Валидны: True
"""

string = "([({}()){}])"
stack = []
pairs = "()", "[]", "{}"

print(f"Скобки: {string}")

for c in string:
    if c in "([{":
        stack.append(c)
    elif c in ")]}":
        if not stack or stack[-1] + c not in pairs:
            print("Валидны:", False)
            break
        stack.pop()
else:
    print("Валидны:", True)



"""
1. Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.
Данные:
text = "Programming is fun!"

Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""
def count_letters(text):
    res = {}
    for char in text.lower():
        if char.isalpha():
            res[char] = res.get(char, 0) + 1
    return res

text = "Programming is fun!"

print(count_letters(text))

from collections import Counter
def count_letters(text):
    return Counter(char for char in text.lower() if char.isalpha())

text = "Programming is fun!"

print(dict(count_letters(text)))


"""
2. Группировка студентов по классам
Создайте структуру для группировки студентов по классам. Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
"""

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

classes = {}

for class_name, student_name in students:
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].append(student_name)

print(classes)

# с функцией

def group_students_class(students):
    classes = {}
    for class_name, student_name in students:
        if class_name not in classes:
            classes[class_name] = []
        classes[class_name].append(student_name)
    return classes

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
grouped = group_students_class(students)
print(grouped)

# defaultdict

from collections import defaultdict

students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy"),
]
# Группируем студентов по классам
class_groups = defaultdict(list)
for class_name, student in students:
    class_groups[class_name].append(student)

print(dict(class_groups))
'''Таблица умножения
Напишите программу, которая выводит таблицу умножения для чисел от 1 до n. Где n это число, которое введет пользователь.
Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)
Пример вывода:
Введите число: 5
'''
# # Вводим число n=5
# n = int(input('Введите число: '))
# # Вывод название таблица
# print("Таблица умножения от 1 до", n)
# # i = 1, потом с новой строки 2, и т.д. до 5
# for i in range(1, n+1):
# # j = 1,2,3,4,5
#     for j in range(1, n+1):
#         # Вывод в строку результата умножения  i * j, меняется только j от 1 до 5
#         print((i*j), end="\t")
#         # Вывод новой пустой строки
#     print()

'''2. Лестница чисел
Напишите программу, которая принимает число n и выводит "лестницу" из чисел. Каждая строка лестницы содержит 
числа от 1 до номера строки.
Пример вывода:
Введите число: 5  
'''
# # Вводим число n=5
# n = int(input("Введите число: "))
# # i=1, потом с новой строки 2, и т.д. до 5
# for i in range(1, n + 1):
#     # j=1, потом с новой строки 1,2, и т.д. до 1,2,3,4,5
#     for j in range(1, i + 1):
#         # Вывод j, между цифрами пробел,
#         print(j, end=" ")
#         # Вывод новой пустой строки
#     print()

'''3. Удаление всех повторяющихся символов
Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы, сохраняя только первые их 
вхождения.
Пример вывода:
Введите строку: Python programming  
Результат: Python prgami
'''
# # Вводим текст
# txt = input("Введите строку: ")
# # Собирает результат по значению
# result = ""
#
# for char in txt:
#     # сравниваем есть ли символ в результате
#     if char not in result:
#         # Если  нет симвом под этим номером добавляется в результат, если есть сработает условие if
#         result += char
#
# print("Результат:", result)



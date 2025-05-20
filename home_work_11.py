# 1. Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

txt = "My number is 121-456-789"
print(txt)
result = ""
for i in txt:      # цикл проверки по символам
    if i.isdigit():    # если в цикле имеется числовое значение
        result += i.replace(i, "*")    #если числовое заменяем на *
    else:
        result += i
print("Результат:", result)

# 2. Количество символов
#
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы,
# которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только
# один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

# txt = "Programming in python"
# print(txt)
## переводим всю строку в нижний регистр
# txt = txt.lower()
# result = ""
##  цикл проверки по символам в строке
# for i in txt:
#     if txt.count(i) > 1 and i not in result:
#         print("Cимвол", "'" + i + "'", "встречается", txt.count(i), "раз(а)")
#         result += i

# 3.Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

# #  Разделяем строку на части списка
# txt = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()
# new_txt = ""
# #   Цикл проверки по символам в строке
# for i in txt:
#     if i.replace('.', '', 1).isdigit():  # Проверяем, можно ли считать это числом (включая десятичные)
#         k = float(i) * 10
#         new_txt += str(k) + " "
#     else:
#         new_txt += i + " "
# print("Результат:", new_txt.strip())


# text = "My number is 121-454-787"
# print("Строка:", text)
# result = text
# for char in text:
#     if char.isdigit():
#         result = result.replace(char, "*")
# print("Результат:", result)


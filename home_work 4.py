# 1. Логические операции
# Напишите программу, которая получит два логических значения от пользователя и выведет результат логических
# операций and, or, not для этих значений, а также сравнение на равенство и неравенство. Для операции not
# используйте первое число. Продумайте в каком виде получать ввод от пользователя для логического значения.
# Пример вывода:
# Enter first value: <value1>
# Enter second value: <value1>
# and: True
# or: True
# not: False
# equal: False
# not equal: True

# Получаем ввод от пользователя и приводим к логическому типу
# first_value = input("Enter first value (True/False): ") == "True"
# second_value = input("Enter second value (True/False): ") == "True"
#
# # Выполняем логические операции
# print("and:", first_value and second_value)                    # Сравниваем через оператор and
# print("or:", first_value or second_value)                      # Сравниваем через оператор or
# print("not:", not first_value)                                 # прогоняем через оператор not
# print("equal:", first_value == second_value)                   # Сравниваем равны ли значения
# print("not equal:", first_value != second_value)               # Сравниваем не равны ли значения

# 2. Проверка условий
# Напишите программу, которая принимает на вход логические значения двух переменных (свет включён и окно открыто)
# и проверяет:
# Оба ли условия выполнены.
# Хотя бы одно из условий выполнено.
# Пример вывода:
# Свет включён? True
# Окно открыто? False
# Оба условия выполнены? False
# Хотя бы одно условие выполнено? True

# first_value = input("Свет включён? (True/False):")=="True"
# second_value = input("Окно открыто? (True/False):")=="True"
#
# # Выполняем логические операции
# print("Оба условия выполнены?:", first_value and second_value)           # Сравниваем через оператор and
# print("Хотя бы одно условие выполнено?:", first_value or second_value)   # Сравниваем через оператор or

# 3. Стоимость мобильного тарифа
# Напишите программу для расчёта стоимости использования мобильного тарифа:
# Базовая стоимость: 30 евро.
# Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро.
# Программа должна запросить у пользователя количество использованных мегабайтов и вывести сколько всего он заплатил
# (базовый и переплата).
# Пример вывода:
# Введите использованные мегабайты: 510
# Общая стоимость: 32.0

# Получаем ввод от пользователя
user_mb = int(input("Введите использованные мегабайты: "))
# Определяем базовые параметры тарифа
base_price = 30
limit_mb = 500
extra_price_mb = 0.2

# Рассчитываем дополнительную плату
extra_cost = (user_mb - limit_mb) * extra_price_mb * (user_mb >= limit_mb)

# Общая стоимость
total_price = base_price + extra_cost

# Вывод результата
print("Общая стоимость:", total_price, "Euro")

def calculate_mobile_tariff(user_mb):
    base_price = 30
    limit_mb = 500
    extra_price_mb = 0.2

    if user_mb > limit_mb:
        extra_cost = (user_mb - limit_mb) * extra_price_mb
    else:
        extra_cost = 0

    total_price = base_price + extra_cost
    return total_price

# Ввод данных от пользователя
user_mb = int(input("Введите использованные мегабайты: "))
total = calculate_mobile_tariff(user_mb)
print("Общая стоимость:", total, "Euro")



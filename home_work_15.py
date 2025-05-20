"""
1. Одно слово

Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова,
а также преобразует оставшиеся строки к нижнему регистру.

Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# filtred_list = []
#
# print("Пример вывода:")
# for s in text_list:
#     if len(s.split()) == 1:
#         filtred_list += [s.lower(),]
# print(f"Обработанный список: {filtred_list}")


""" 2. Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с 
новой ценой. В конце вывести таблицу с новой ценой.

Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

Пример вывода:

Введите скидку (в процентах): 17

Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse               25.00$        20.75$
Keyboard            75.00$        62.25$
Monitor            200.00$       166.00$

"""

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

n = float(input("Введите скидку (в процентах): "))

print(f"{'Product':<10} {'Old price':>15} {'New price':>15}\n{"-"*42}")

for product in products:
    product_name, old_price = product
    new_price = old_price *(1 - n/100)
    print(f"{product_name:<10} {old_price:>14.2f}$ {new_price:>14.2f}$")
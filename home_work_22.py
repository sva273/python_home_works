"""
1. Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.

Данные:
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
Пример вывода:
['Chair', 'Laptop']
"""
def filter_product(orders):
    sort_price = [order["product"] for order in orders if order["price"] > 500]
    return sorted(sort_price)

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

result = filter_product(orders)
print(result)

# через lambda

def filter_product(orders):
    filtered = filter(lambda x: x["price"] > 500, orders)
    sorted_products = sorted(map(lambda x: x["product"], filtered))
    return sorted_products

result = filter_product(orders)
print(result)


"""
2. Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:
Вычисляет общую выручку для каждого товара.
Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
Данные:

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

Пример вывода:

{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
"""
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

sorted_rev = dict(
    sorted(
        ((item, quantity * price) for item, quantity, price in sales),
        key=lambda x: x[1],
        reverse=True
    )
)

print(sorted_rev)

# c функцией

def function_sorted_rev(sales):
    sorted_rev = dict(
        sorted(
            ((item, quantity * price) for item, quantity, price in sales),
            key=lambda x: x[1],
            reverse=True
        )
    )
    return sorted_rev

print(function_sorted_rev(sales))

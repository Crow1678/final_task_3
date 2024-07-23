from collections import defaultdict
import matplotlib.pyplot as plt


# Чтения данных о продажах из файла
def read_sales_data(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    sale = file.read().splitlines()
    sale_all = []
    for line in sale:
        product_n, quantity_dict, price_dict, date_dict = line.split(',')
        sale_dec = {'product_name': product_n, 'quantity': int(quantity_dict), 'price': float(price_dict),
                    'date': date_dict}
        sale_all.append(sale_dec)
    return sale_all


# Вычисление общей суммы продаж по каждому продукту
def total_sales_per_product(sales_data):
    sales_per_product = defaultdict(float)
    for sale in sales_data:
        total_sale = sale['quantity'] * sale['price']
        sales_per_product[sale['product_name']] += total_sale
    return sales_per_product


# Вычисление общей суммы продаж по датам
def sales_over_time(sales_data):
    sales_per_date = defaultdict(float)
    for sale in sales_data:
        total_sale = sale['quantity'] * sale['price']
        sales_per_date[sale['date']] += total_sale
    return sales_per_date


# Основная функция для анализа данных и построения графиков
def main(file_path):
    # Чтение данных
    sales_data = read_sales_data(file_path)

    # Анализ данных
    sales_per_product = total_sales_per_product(sales_data)
    sales_per_date = sales_over_time(sales_data)

    # Определение продукта с наибольшей выручкой
    max_product = max(sales_per_product, key=sales_per_product.get)
    max_product_value = sales_per_product[max_product]

    # Определение даты с наибольшей суммой продаж
    max_date = max(sales_per_date, key=sales_per_date.get)
    max_date_value = sales_per_date[max_date]

    # Вывод результатов
    print(f"Продукт с наибольшей выручкой: {max_product} ({max_product_value} руб.)")
    print(f"Дата с наибольшей суммой продаж: {max_date} ({max_date_value} руб.)")

    # График общей суммы продаж по каждому продукту
    plt.figure(figsize=(10, 5))
    plt.bar(sales_per_product.keys(), sales_per_product.values())
    plt.xlabel('Продукты')
    plt.ylabel('Сумма продаж (руб.)')
    plt.title('Общая сумма продаж по продуктам')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # График общей суммы продаж по датам
    plt.figure(figsize=(10, 5))
    plt.plot(list(sales_per_date.keys()), list(sales_per_date.values()), marker='o')
    plt.xlabel('Дата')
    plt.ylabel('Сумма продаж (руб.)')
    plt.title('Общая сумма продаж по датам')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Запуск программы с указанием пути к файлу
file_path = 'sale.txt'  # Укажите путь к вашему файлу
main(file_path)

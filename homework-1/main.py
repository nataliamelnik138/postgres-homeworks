"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


# Создаем список словарей содержащий данные сотрудников для добавления в БД
employees_data = []
with open('north_data/employees_data.csv', 'rt', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for line in data:
        employees_data.append({'employee_id': line['employee_id'], 'first_name': line['first_name'],
                               'last_name': line['last_name'],'title': line['title'], 'birth_date': line['birth_date'],
                               'notes': line['notes']})

# Создаем список словарей содержащий данные клиентов для добавления в БД
customers_data = []
with open('north_data/customers_data.csv', 'rt', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for line in data:
        customers_data.append({'customer_id': line['customer_id'],
                               'company_name': line['company_name'],
                               'contact_name': line['contact_name']})

# Создаем список словарей содержащий данные заказов для добавления в БД
orders_data = []
with open('north_data/orders_data.csv', 'rt', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for line in data:
        orders_data.append({'order_id': line['order_id'], 'customer_id': line['customer_id'],
                            'employee_id': line['employee_id'], 'order_date': line['order_date'],
                            'ship_city': line['ship_city']})

# Заполняем таблицы БД данными из списков словарей
with psycopg2.connect(host="localhost", database="north", user="postgres", password="123456") as conn:
    with conn.cursor() as cur:
        for customer in customers_data:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (customer['customer_id'], customer['company_name'],
                                                                      customer['contact_name']))

        for employee in employees_data:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (employee['employee_id'],
                                                                                  employee['first_name'],
                                                                                  employee['last_name'],
                                                                                  employee['title'],
                                                                                  employee['birth_date'],
                                                                                  employee['notes']))

        for order in orders_data:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order['order_id'],
                                                                           order['customer_id'],
                                                                           order['employee_id'],
                                                                           order['order_date'],
                                                                           order['ship_city']))
conn.close()

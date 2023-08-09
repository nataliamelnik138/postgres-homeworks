"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


# Заполняем таблицы БД данными из файлов
with psycopg2.connect(host="localhost", database="north", user="postgres", password="123456") as conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', 'rt', encoding='utf-8') as csvfile:
            data = csv.DictReader(csvfile, delimiter=',')
            for line in data:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (line['customer_id'], line['company_name'],
                                                                      line['contact_name']))

        with open('north_data/employees_data.csv', 'rt', encoding='utf-8') as csvfile:
            data = csv.DictReader(csvfile, delimiter=',')
            for line in data:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (line['employee_id'],
                                                                                  line['first_name'],
                                                                                  line['last_name'],
                                                                                  line['title'],
                                                                                  line['birth_date'],
                                                                                  line['notes']))

        with open('north_data/orders_data.csv', 'rt', encoding='utf-8') as csvfile:
            data = csv.DictReader(csvfile, delimiter=',')
            for line in data:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (line['order_id'],
                                                                           line['customer_id'],
                                                                           line['employee_id'],
                                                                           line['order_date'],
                                                                           line['ship_city']))
conn.close()

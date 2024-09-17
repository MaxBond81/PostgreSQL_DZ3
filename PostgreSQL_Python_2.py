import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
postgres_password = os.getenv("postgres_password")


with psycopg2.connect(database = "clientinfo_db", user = "postgres", password = postgres_password) as conn:
# Создаем таблицы БД
    def create_table(conn):
        with conn.cursor() as cur:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS clients(
                    client_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(40),
                    last_name VARCHAR(40),
                    email VARCHAR(80) UNIQUE NOT NULL
            ); 
            ''')

            cur.execute('''
            CREATE TABLE IF NOT EXISTS client_phones(
                    client_phones_id SERIAL PRIMARY KEY,
                    client_id INTEGER NOT NULL REFERENCES clients(client_id),
                    phone VARCHAR(10) UNIQUE
            ); 
            ''')
            print("Таблицы созданы")

    #create_table(conn)

    #Добавляем клиентов
    def add_client(conn, first_name, last_name, email):
        with conn.cursor() as cur:
            cur.execute('''
            INSERT INTO clients(first_name, last_name, email) VALUES(%s,%s,%s);
             ''', (first_name, last_name, email))

    #add_client(conn, "Иван", "Пупкин","ipup@mail.ru")
    #add_client(conn, "Иван", "Петров","ipetr@mail.ru")

    # Добавляем телефоны
    def add_phone(conn, client_id, phone):
        with conn.cursor() as cur:
            cur.execute('''
            INSERT INTO client_phones(client_id, phone) VALUES(%s,%s);
             ''', (client_id, phone))


    #add_phone(conn, 1 , "9280000255")
    #add_phone(conn, 2 , "9280000111")


    # Изменяем данные о клиенте
    def change_client(conn,client_id, first_name = None, last_name = None, email = None):
        with conn.cursor() as cur:
            cur.execute("""
                    SELECT * from clients
                    WHERE client_id = %s
                    """, (client_id,))
            result = cur.fetchone()
            if first_name is None:
                first_name = result[1]
            if last_name is None:
                last_name = result[2]
            if email is None:
                email = result[3]
            cur.execute("""
                    UPDATE clients
                    SET first_name = %s, last_name = %s, email =%s 
                    WHERE client_id = %s
                    """, (first_name, last_name, email, client_id))
            print("Данные изменены")

    #change_client(conn, 1, first_name = "Василий", email= "vask@mail.ru")
    #change_client(conn,4, client_phones_id = 16, phone = "9281111111")


    # Удаляем телефон клиента
    def delete_phone(conn, phone):
        with conn.cursor() as cur:
            cur.execute('''
            DELETE FROM client_phones
            WHERE phone = %s;
            ''', (phone,))

    #delete_phone(conn,'9280000002')

    # Удаляем клиента
    def delete_client(conn, client_id):
        with conn.cursor() as cur:
            cur.execute('''
            DELETE FROM client_phones
            WHERE client_id = %s;
            ''', (client_id,))
        with conn.cursor() as cur:
            cur.execute('''
            DELETE FROM clients
            WHERE client_id = %s;
            ''', (client_id,))

    #delete_client(conn, 5)

    # Функция поиска клиента
    def find_client(conn, first_name = None, last_name = None, email = None, phone = None):
        with conn.cursor() as cur:
            if first_name is None:
                first_name = '%'
            else:
                first_name = '%' + first_name + '%'
            if last_name is None:
                last_name = '%'
            else:
                last_name = '%' + last_name + '%'
            if email is None:
                email = '%'
            else:
                email = '%' + email + '%'
            if phone is None:
                cur.execute("""
                        SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone FROM clients c
                        LEFT JOIN client_phones p ON c.client_id = p.client_id
                        WHERE c.first_name LIKE %s AND c.last_name LIKE %s
                        AND c.email LIKE %s
                        """, (first_name, last_name, email))
            else:
                cur.execute("""
                        SELECT c.client_id, c.first_name, c.last_name, c.email, p.phone FROM clients c
                        LEFT JOIN client_phones p ON c.client_id = p.client_id
                        WHERE c.first_name LIKE %s AND c.last_name LIKE %s
                        AND c.email LIKE %s AND p.phone LIKE %s
                        """, (first_name,last_name,email,phone))

            result = cur.fetchall()
            for client in result:
                print(f"id: {client[0]}, имя: {client[1]}, фамилия: {client[2]}, email: {client[3]}, телефон: {client[4]}")

    #find_client(conn, last_name="Пуп")
    #find_client(conn, email="vask@mail.ru", first_name="Василий")


conn.close()
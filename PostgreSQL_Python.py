import psycopg2


conn = psycopg2.connect(database = "clientinfo_db", user = "postgres", password = "123")

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
        conn.commit()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS client_phones(
                client_phones_id SERIAL PRIMARY KEY,
                client_id INTEGER NOT NULL REFERENCES clients(client_id),
                phone VARCHAR(10) UNIQUE
        ); 
        ''')
        conn.commit()
    conn.close()

#create_table(conn)

#Добавляем клиентов
def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        cur.execute('''
        INSERT INTO clients(first_name, last_name, email) VALUES(%s,%s,%s);
         ''', (first_name, last_name, email))
        conn.commit()
    conn.close()

#add_client(conn, "Иван", "Пупкин","ipup@mail.ru")
#add_client(conn, "Иван", "Петров","ipetr@mail.ru")

# Добавляем телефоны
def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute('''
        INSERT INTO client_phones(client_id, phone) VALUES(%s,%s);
         ''', (client_id, phone))
        conn.commit()
    conn.close()

#add_phone(conn, 4, "9280000001")
#add_phone(conn, 5 , "9280000002")


# Изменяем данные о клиенте
def change_client(conn,client_id, email = None, client_phones_id = None, phone = None):
    if email != None:
        with conn.cursor() as cur:
            cur.execute('''
            UPDATE clients
            SET email = %s
            WHERE client_id = %s;
            ''', (email,client_id))
            conn.commit()
    if phone != None:
        with conn.cursor() as cur:
            cur.execute('''
            UPDATE client_phones
            SET phone = %s
            WHERE client_phones_id = %s;
            ''', (phone, client_phones_id))
            conn.commit()
    conn.close()

#change_client(conn, 4, email = "ipupkin@mail.ru")
#change_client(conn,4, client_phones_id = 16, phone = "9281111111")


# Удаляем телефон клиента
def delete_phone(conn, phone):
    with conn.cursor() as cur:
        cur.execute('''
        DELETE FROM client_phones
        WHERE phone = %s;
        ''', (phone,))
        conn.commit()
    conn.close()

#delete_phone(conn,'9280000002')

# Удаляем клиента
def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute('''
        DELETE FROM client_phones
        WHERE client_id = %s;
        ''', (client_id,))
        conn.commit()
    with conn.cursor() as cur:
        cur.execute('''
        DELETE FROM clients
        WHERE client_id = %s;
        ''', (client_id,))
        conn.commit()
    conn.close()

#delete_client(conn, 5)

# Функция поиска клиента с учетом нахождения в базе тезок и однофамильцев
def find_client(conn, first_name = None, last_name = None, email = None, phone = None):
    with conn.cursor() as cur:
        cur.execute('''
        SELECT c.client_id,c.first_name, c.last_name, c.email, cp.phone  FROM clients c
        JOIN client_phones cp on c.client_id = cp.client_id
        WHERE c.first_name  = %s;
        ''', (first_name,))
        result = cur.fetchall()
        if first_name != None:
            if result != []:
                for client in result:
                    print(f"id: {client[0]},имя: {client[1]}, фамилия: {client[2]}, email: {client[3]}, телефон: {client[4]}")
            else:
                print("такого имени нет в базе")
    with conn.cursor() as cur:
        cur.execute('''
        SELECT c.client_id,c.first_name, c.last_name, c.email, cp.phone  FROM clients c
        JOIN client_phones cp on c.client_id = cp.client_id
        WHERE c.last_name  = %s;
        ''', (last_name,))
        result = cur.fetchall()
        if last_name != None:
            if result != []:
                for client in result:
                    print(f"id: {client[0]},имя: {client[1]}, фамилия: {client[2]}, email: {client[3]}, телефон: {client[4]}")
            else:
                print("такой фамилии нет в базе")
    with conn.cursor() as cur:
        cur.execute('''
        SELECT c.client_id,c.first_name, c.last_name, c.email, cp.phone  FROM clients c
        JOIN client_phones cp on c.client_id = cp.client_id
        WHERE c.email  = %s;
        ''', (email,))
        result = cur.fetchone()
        if email != None:
            if result != None:
                print(f"id: {result[0]},имя: {result[1]}, фамилия: {result[2]}, email: {result[3]}, телефон: {result[4]}")
            else:
                print("такого email нет в базе")
    with conn.cursor() as cur:
        cur.execute('''
        SELECT c.client_id,c.first_name, c.last_name, c.email, cp.phone  FROM clients c
        JOIN client_phones cp on c.client_id = cp.client_id
        WHERE cp.phone  = %s;
        ''', (phone,))
        result = cur.fetchone()
        if phone != None:
            if result != None:
                print(f"id: {result[0]},имя: {result[1]}, фамилия: {result[2]}, email: {result[3]}, телефон: {result[4]}")
            else:
                print("такого телефона нет в базе")
    conn.close()

#find_client(conn, first_name = "Иван")
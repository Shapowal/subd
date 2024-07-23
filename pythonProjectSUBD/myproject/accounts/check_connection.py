import psycopg2

try:
    # Попытка подключения к базе данных
    conn = psycopg2.connect(
        dbname='task1',
        user='postgres',
        password='3330067',
        host='localhost',
        port='5432',
        client_encoding='UTF8'
    )
    print("Подключение успешно")
except psycopg2.Error as e:
    print(f"Ошибка подключения: {e}")
except UnicodeDecodeError as e:
    print(f"Ошибка декодирования Unicode: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("Соединение закрыто")

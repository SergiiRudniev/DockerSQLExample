import mysql.connector

# Подключение к базе данных
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="mydatabase"
)

# Выполнение запроса
cursor = conn.cursor()
cursor.execute("SELECT * FROM my_table")

# Получение результатов
for row in cursor.fetchall():
    print(row)

# Закрытие соединения
conn.close()

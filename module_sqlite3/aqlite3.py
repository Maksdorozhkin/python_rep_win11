import sqlite3
DB_NAME = "sqlite_db.db"

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)
# courses = [
#     (351, "JavaScript course", 415, 100),
#     (614, "C++ course", 100, 23),
#     (721, "Java full course", 614, 400)
# ]

# создаем подключение к базе данных
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))
#     sqlite_conn.commit()
# создаем подключение с помощью цикла for
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()


# создание новой таблицы
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     student_qty integer,
#     reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

# чтение таблицы с помощью sqlite3
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=30"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)

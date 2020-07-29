import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plot
import matplotlib.dates as mdates
import matplotlib.style as style

# INSERT, UPDATE and DELETE need to be commit() ed
# with is a context manager and allows for automatic resource closing

class SQLiteConnectionManager():
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect('tutorial.db')
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
# can do sqlite3.connect(':memory:') to have the db in memory. Very awesome indeed.
cursor = conn.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS stuff(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    with conn:
        cursor.execute("INSERT INTO stuff VALUES(1451235422, '2016-01-01', 'Python', 8)")
    conn.commit()

    cursor.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H: %M %S"))
    keyword = "Python"
    value = random.randrange(0, 10)
    # cursor.execute("INSERT INTO stuff (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
    #                (unix, date, keyword, value))

    cursor.execute("INSERT INTO stuff VALUES (:unix, :datestamp, :keyword, :value)",
                   {"unix": unix, "datestamp": date, "keyword": keyword, "value": value})
    conn.commit()

def read_from_db():
    # case sensitive. "Python" not "Python" works.
    cursor.execute("SELECT * FROM stuff WHERE unix > 1596040192 and unix < 1596540192 ")
    # data = cursor.fetchall()
    # print(data)

    # There is also a fetchmany() and fetchone(), very awesome and handy.
    for row in cursor.fetchall():
        print(row[0]) # Since unix is the first column, it is [0]

def graph_data():
    cursor.execute("SELECT unix, value FROM stuff")
    dates = []
    values = []

    for row in cursor.fetchall():
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plot.plot_date(dates, values, '-')
    plot.show()

def del_update():
    cursor.execute("SELECT * FROM stuff")
    [print(row) for row in cursor.fetchall()]

    # cursor.execute("UPDATE stuff SET value = 99 WHERE value = 4")
    # conn.commit()
    #
    # cursor.execute("SELECT * FROM stuff")
    # [print(row) for row in cursor.fetchall()]
    print(cursor.rowcount, end = " | ")

    print('#' * 35)

    cursor.execute("SELECT * FROM stuff LIMIT 2")
    [print(row) for row in cursor.fetchall()]

    print(cursor.rowcount, end = " | ")

    print('#' * 35)

    cursor.execute("DELETE FROM stuff WHERE value = 4")
    # cursor.rowcount == 0 when nothing found for execute
    print(cursor.rowcount, end = " | ")
    conn.commit()

    print('#' * 35)

    cursor.execute("SELECT * FROM stuff")
    [print(row) for row in cursor.fetchall()]

    print('#' * 35)

    # ? can be filled in by a tuple even if 1 element
    cursor.execute("UPDATE stuff SET value = 99 WHERE value = ?", (4,))
    conn.commit()

# create_table()
# data_entry()

def del_all():
    pause = input("Enter input so database purge may commence...")
    cursor.execute("DELETE FROM stuff")
    conn.commit()

for i in range(10):
    dynamic_data_entry()
    time.sleep(.1)

# read_from_db()
# graph_data()
del_update()
del_all()
cursor.close()
conn.close()
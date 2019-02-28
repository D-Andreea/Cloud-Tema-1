import sqlite3

#conn = sqlite3.connect('example.db')
#database = conn.cursor()


def initialize_database():
    conn = sqlite3.connect('metrics.db')
    database = conn.cursor()
    database.execute('''DROP TABLE metrics''')
    database.execute('''CREATE TABLE metrics
             (api text, content text, status_code text, time text)''')


def insert_metrics(api, content, status, time):
    conn = sqlite3.connect('metrics.db')
    database = conn.cursor()
    values = (api, content, status, time)
    database.execute("INSERT INTO metrics VALUES (?,?,?,?)", values)
    #database.execute("INSERT INTO metrics VALUES (" + api + ", " + content + ", " + status + ", " + time + ")")
    conn.commit()
    conn.close()
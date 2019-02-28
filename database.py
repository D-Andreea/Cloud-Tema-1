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


def select_metrics():
    conn = sqlite3.connect('metrics.db')
    database = conn.cursor()
    t = ()
    database.execute('SELECT * FROM metrics', t)
    count = 0
    status_code_count = 0
    avg = 0
    max = 0
    min = 999
    info = database.fetchall()
    print(info)
    for tuple in info:
        print(tuple)
        aux = float(tuple[3])
        count += 1
        if max < aux:
            max = aux
        if min > aux:
            min = aux
        if int(tuple[2]) == 200:
            status_code_count += 1
        avg += aux
    aux /= count
    answer = """Min time: """ + str(min) + """
            <br> Max time: """ + str(max) + """
            <br> Avg time: """ + str(avg) + """
            <br> Status code 200: """ + str(status_code_count) 
    conn.close()
    return answer

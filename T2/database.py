import sqlite3

table_doctori = '''CREATE TABLE IF NOT EXISTS doctori (
                        doctorid integer PRIMARY KEY,
                        nume text NOT NULL,
                        prenume text NOT NULL,
                        specializare text NOT NULL
                    )'''

table_programari = '''CREATE TABLE IF NOT EXISTS programari (
                        programareid integer PRIMARY KEY,
                        costconsultatie integer NOT NULL,
                        doctorid integer NOT NULL,
                        pacientid integer NOT NULL,
                        FOREIGN KEY (doctorid) REFERENCES doctori (doctorid)
                        FOREIGN KEY (pacientid) REFERENCES pacienti (pacientid)
                    )'''

table_pacienti = '''CREATE TABLE IF NOT EXISTS pacienti (
                        pacientid integer PRIMARY KEY,
                        nume text NOT NULL,
                        prenume text NOT NULL,
                        adresa text NOT NULL
                    )'''

doctor = "INSERT INTO doctori VALUES (?, ?, ?, ?)"
doctor_1_values = (111, "Popescu", "Constantin", "medicina generala")
doctor_2_values = (112, "Margarescu", "Maria", "dermatologie")
doctor_3_values = (113, "Bostan", "Radu", "stomatologie")

pacient = "INSERT INTO pacienti VALUES (?, ?, ?, ?)"
pacient_1_values = (221, "Pop", "Claudia", "splai bahlui numarul 3")
pacient_2_values = (222, "Dante", "Marin", "strada Ion Creanga numarul 7A")
pacient_3_values = (223, "Columb", "Vasile", "cuza voda numarul 90E")

programare = "INSERT INTO programari VALUES (?, ?, ?, ?)"
programare_1_values = (331, 100, 111, 221)
programare_2_values = (332, 150, 112, 221)
programare_3_values = (333, 200, 113, 222)
programare_4_values = (334, 100, 112, 223)


def initialize_database():
    connection = sqlite3.connect('database.db')
    database = connection.cursor()
    database.execute(table_doctori)
    database.execute(table_pacienti)
    database.execute(table_programari)


def insert_record_new():
    connection = sqlite3.connect('database.db')
    db = connection.cursor()
    # db.execute(doctor, doctor_1_values)
    # connection.commit()
    # db.execute(doctor, doctor_2_values)
    # connection.commit()
    # db.execute(doctor, doctor_3_values)
    # connection.commit()
    #
    # db.execute(pacient, pacient_1_values)
    # connection.commit()
    # db.execute(pacient, pacient_2_values)
    # connection.commit()
    # db.execute(pacient, pacient_3_values)
    # connection.commit()
    #
    # db.execute(programare, programare_1_values)
    # connection.commit()
    # db.execute(programare, programare_2_values)
    # connection.commit()
    # db.execute(programare, programare_3_values)
    # connection.commit()
    # db.execute(programare, programare_4_values)
    # connection.commit()

    db.execute('SELECT * FROM doctori')
    doctori = db.fetchall()

    db.execute('SELECT * FROM pacienti')
    pacienti = db.fetchall()

    db.execute('SELECT * FROM programari')
    programari = db.fetchall()

    print('---------------------------------------------')
    print(doctori)
    print(pacienti)
    print(programari)
    print('---------------------------------------------')
    connection.close()


def insert_record(query, values):
    try:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute(query, values)
        connection.commit()
        connection.close()
    except Exception as e:
        return 409


def db_main():
    initialize_database()
    insert_record_new()
    print('db initialized')


def interogate_database(query):
    try:
        connection = sqlite3.connect('database.db')
        db = connection.cursor()
        db.execute(query)
        result_set = db.fetchall()
        connection.close()
        return result_set
    except Exception as e:
        return 400



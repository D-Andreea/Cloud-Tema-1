def build_post_select(parameters):
    if len(parameters) == 1:
        if parameters[0] == 'doctori':
            return 'SELECT * FROM ' + parameters[0], 'doctori'
        elif parameters[0] == 'pacienti':
            return 'SELECT * FROM ' + parameters[0], 'pacienti'
        elif parameters[0] == 'programari':
            return 'SELECT * FROM ' + parameters[0], 'programari'
        else:
            return 0, 0
    elif len(parameters) == 2:
        if parameters[0] == 'doctori':
            return 'SELECT * FROM doctori WHERE doctorid=' + parameters[1], 'doctori'
        elif parameters[0] == 'pacienti':
            return 'SELECT * FROM pacienti WHERE pacientid=' + parameters[1], 'pacienti'
        elif parameters[0] == 'programari':
            return 'SELECT * FROM programari WHERE programareid=' + parameters[1], 'programari'
        else:
            return 0, 0
    elif len(parameters) == 3:
        if parameters[0] == 'programari':
            query = 'SELECT * FROM programari p '
            if parameters[2] == 'doctori':
                query += ' JOIN doctori d ON d.doctorid=p.doctorid WHERE programareid=' + parameters[1]
                table = 'prog-doctori'
            elif parameters[2] == 'pacienti':
                query += ' JOIN pacienti pp ON pp.pacientid=p.pacientid WHERE programareid=' + parameters[1]
                table = 'prog-pacienti'
            else:
                return 0, 0
            return query, table
        else:
            return 0, 0
    else:
        return 0, 0


def build_post_insert_query(arguments, table):
    if table == 'doctori':
        doctor = "INSERT INTO doctori VALUES (?, ?, ?, ?)"
        values = tuple()
        for value in arguments.values():
            values += (value,)
        return doctor, values
    elif table == 'pacienti':
        pacient = "INSERT INTO pacienti VALUES (?, ?, ?, ?)"
        values = tuple()
        for value in arguments.values():
            values += (value,)
        return pacient, values
    elif table == 'programari':
        programare = "INSERT INTO programari VALUES (?, ?, ?, ?)"
        values = tuple()
        for value in arguments.values():
            values += (value,)
        return programare, values
    else:
        return 'Bad request', 400
def build_get_select(parameters):
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
        elif parameters[1] == 'pacienti':
            return 'SELECT * FROM pacienti WHERE pacientid=' + parameters[1], 'pacienti'
        elif parameters[1] == 'programari':
            return 'SELECT * FROM programari WHERE programari=' + parameters[1], 'programari'
        else:
            return 0, 0
    elif len(parameters) == 3:
        if parameters[0] == 'programari':
            query = 'SELECT * FROM programari p '
            if parameters[2] == 'doctori':
                query += ' JOIN doctori d ON d.doctorid=p.doctorid WHERE programareid=' + parameters[1]
                table = 'prog-doctori'
            elif parameters[2] == 'pacienti':
                query += ' JOIN pacienti p ON p.pacientid=p.pacientid WHERE programareid=' + parameters[1]
                table = 'prog-pacienti'
            else:
                return 0, 0
            return query, table
        else:
            return 0, 0
    else:
        return 0, 0


def transform_array_to_dict(array, table):
    dictionary = dict()
    print(array)
    if table == 'doctori':
        dictionary['doctorid'] = array[0]
        dictionary['nume'] = array[1]
        dictionary['prenume'] = array[2]
        dictionary['specializare'] = array[3]
    elif table == 'pacienti':
        dictionary['pacientid'] = array[0]
        dictionary['nume'] = array[1]
        dictionary['prenume'] = array[2]
        dictionary['adresa'] = array[3]
    elif table == 'programari':
        dictionary['programareid'] = array[0]
        dictionary['costconsultatie'] = array[1]
        dictionary['doctorid'] = array[2]
        dictionary['pacientid'] = array[3]
    elif table == 'prog-doctori':
        dictionary['programareid'] = array[0]
        dictionary['costconsultatie'] = array[1]
        dictionary['doctorid'] = array[2]
        dictionary['pacientid'] = array[3]
        dictionary['doctorid'] = array[0]
        dictionary['nume'] = array[1]
        dictionary['prenume'] = array[2]
        dictionary['specializare'] = array[3]
    elif table == 'prog-pacienti':
        dictionary['programareid'] = array[0]
        dictionary['costconsultatie'] = array[1]
        dictionary['doctorid'] = array[2]
        dictionary['pacientid'] = array[3]
        dictionary['pacientid'] = array[0]
        dictionary['nume'] = array[1]
        dictionary['prenume'] = array[2]
        dictionary['adresa'] = array[3]
    else:
        dictionary['ERROR: '] = 'Something went wrong'
    return dictionary

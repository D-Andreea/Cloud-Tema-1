def transform_dict_to_tuples(dictionary):
    rows = ()
    values = ()
    string = ''
    for x, y in dictionary.items():
        string += x + ' = \'' + str(y) + '\', '
    return string[0:-2]


def build_update_query(dictionary, table, id):
    string = transform_dict_to_tuples(dictionary)
    if table == 'doctori':
        return 'UPDATE doctori SET ' + string + ' WHERE doctorid=' + id
    elif table == 'pacienti':
        return 'UPDATE pacienti SET ' + string + ' WHERE pacientid=' + id
    elif table == 'programari':
        return 'UPDATE programari SET ' + string + ' WHERE programareid=' + id
    else:
        return 0


def build_put_select(parameters):
    if len(parameters) == 2:
        if parameters[0] == 'doctori':
            return 'SELECT * FROM doctori WHERE doctorid=' + parameters[1], 'doctori'
        elif parameters[0] == 'pacienti':
            return 'SELECT * FROM pacienti WHERE pacientid=' + parameters[1], 'pacienti'
        elif parameters[0] == 'programari':
            return 'SELECT * FROM programari WHERE programareid=' + parameters[1], 'programari'
        else:
            return 0, 0
    else:
        return 0, 0

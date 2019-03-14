def build_delete_select(parameters):
    if len(parameters) == 2:
        if parameters[0] == 'doctori':
            return 'DELETE FROM doctori WHERE doctorid=(?)', (parameters[1],)
        elif parameters[0] == 'pacienti':
            return 'DELETE FROM pacienti WHERE pacientid=(?)', (parameters[1],)
        elif parameters[0] == 'programari':
            return 'DELETE FROM programari WHERE programareid=(?)', (parameters[1],)
        else:
            return 0, 0
    else:
        return 0, 0

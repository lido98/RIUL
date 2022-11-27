def send_consult(consult):
    '''Buscar los ducumentos y por cada documento recuperado devolver un formato como este'''
    return documents_to_json_list('uwu')

def document_to_json(consult,passage,link,tittle):
    return {'consult':consult,
            'passage':passage,
            'link':link,
            'tittle': tittle}

def documents_to_json_list(documents):
    result = []
    # for document in documents:
    #     result.append(document_to_json(lo del documento))
    
    for i in range (3):
        result.append(document_to_json('Las palabras a marcar','un pedazo del texto donde esten varias palabras','link del documento','titulo del documento'))
    
    return result       

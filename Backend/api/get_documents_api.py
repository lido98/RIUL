import environment
def send_consult(consult):
    '''Buscar los documentos y por cada documento recuperado devolver un formato como este'''
    rank = environment.Environment.search_engine(consult)
    documents = []
    for document in rank:
        documents.append(document)

    return documents_to_json_list(documents,consult)

def document_to_json(consult,passage,link,tittle):
    return {'consult':consult,
            'passage':passage,
            'link':"cran"+"/"+ link,
            'tittle': tittle}

def documents_to_json_list(documents,consult):
    result = []
    for document in documents:
        result.append(document_to_json(consult,document.body,str(document.id) + ".html","["+str(document.id) +"]  "+document.title ))
    return result       

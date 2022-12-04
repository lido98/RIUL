import environment
def send_consult(consult):
    '''Buscar los ducumentos y por cada documento recuperado devolver un formato como este'''
    rank  = environment.Environment.matrix.get_rank_of_query(consult)
    documents = []
    for document in rank:
        if rank[document] < 0.04: break
        documents.append(document)

    return documents_to_json_list(documents,consult)

def document_to_json(consult,passage,link,tittle):
    return {'consult':consult,
            'passage':passage,
            'link':link,
            'tittle': tittle}

def documents_to_json_list(documents,consult):
    result = []
    for document in documents:
        result.append(document_to_json(consult,document.body,"link.pdf",document.title))
    return result       

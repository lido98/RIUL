from cmath import nan
import environment
def send_consult(consult):
    '''Buscar los ducumentos y por cada documento recuperado devolver un formato como este'''
    rank = environment.Environment.search_engine(consult)
    # rank  = environment.Environment.search_engine.vectors.get_rank_of_query(consult)
    documents = []
    for document in rank:
        # if rank[document] < 0.04 or rank[document] == nan: break
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
        result.append(document_to_json(consult,document.body,str(document.id) + ".txt","["+str(document.id) +"]  "+document.title ))
    return result       

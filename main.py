from Corpus.CRAN.cran_parser import CRANParser
from Corpus.Reuters.reut_parser import ReutersParser
from Models.Vector_Model import vector_indexer, vector_parse_query, vector_search_engine

#from ranking_manager import Ranking
from indexer import BaseInvertedIndex
from search_engine import BaseSearchEngine
from query_parser import BaseQuery
from corpus_manager import Collection, Document


def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')

    docs: Collection
    corpus = 'cran'
    match corpus:
        case 'cran':
            #docs = CRANParser()()
            docs = Collection([Document(1, 'doc 1', 'leon leon leon'),Document(2, 'doc 2', 'leon leon leon zorro'),Document(3, 'doc 3', 'leon zorro nutria'),Document(4, 'doc 4', 'leon leon leon zorro zorro zorro'),Document(5, 'doc 5', 'nutria')])
    
    model = 'vector'   
    search_engine: BaseSearchEngine     
    match model:
        case 'vector':
            index = vector_indexer.VectorIndexer(docs)()
            search_engine = vector_search_engine.VectorSearchEngine(index,docs)

    #query = 'an empirical evaluation of the destalling effects was made for the specific configuration of the experiment'
    query = 'leon zorro'
    recovered = search_engine(query)    


   
    
    #docs = ReutersParser()()       
    #ranking = Ranking(0.1)
    #print('Por favor, introduzca la consulta:')
    #query = input()    
    #query = 
    #recovered = ranking.rec_files(docs, query)
    
    print('----------------------------------------------------------------------\nLos documentos recuperados, junto a su ranking, son:\n')
    #print(len(recovered))
    for r in recovered:
        print(str(docs[r[0]].id) + ' ' + docs[r[0]].title + ' ' + str(round(r[1],5))   + '\n')
    
      
    
if __name__ == '__main__':
    main()





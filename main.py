from Corpus.CRAN.cran_parser import CRANParser
from Models.Vector_Model.vector_search_engine import VectorSearchEngine
from indexer import Indexer
from search_engine import BaseSearchEngine
from corpus_manager import Collection
import time


def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')

    docs: Collection
    corpus = 'cran'
    match corpus:
        case 'cran':
            docs = CRANParser()()
            #docs = Collection([Document(1, 'doc 1', 'leon leon leon'),Document(2, 'doc 2', 'leon leon leon zorro'),Document(3, 'doc 3', 'leon zorro nutria'),Document(4, 'doc 4', 'leon leon leon zorro zorro zorro'),Document(5, 'doc 5', 'nutria')])
    
    model = 'vector'   
    search_engine: BaseSearchEngine     
    match model:
        case 'vector':            
            index = Indexer(docs)()
            search_engine = VectorSearchEngine(index,docs)

    #query = ''an empirical evaluation of the destalling effects was made for the specific configuration of the experiment
    #query = 'leon zorro'

    print('Por favor, introduzca la consulta:')
    query = input()    
    recovered = search_engine(query, 0.05) 
    
    #docs = ReutersParser()()       
    #ranking = Ranking(0.1)
    
    #query = input()    
    #query = 
    #recovered = ranking.rec_files(docs, query)
    
    c = 0
    print('----------------------------------------------------------------------\nLos documentos recuperados, junto a su ranking, son:\n')
    #print(len(recovered))
    for r in recovered:
        print(str(r.id) + ' ' + str(r.title) + ' ' + str(round(recovered[r],5))   + '\n')
        c+=1
    print(c)
    
      
    
if __name__ == '__main__':
    main()





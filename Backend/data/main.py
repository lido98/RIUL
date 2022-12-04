from data.Corpus.CRAN.cran_parser import CRANParser
from data.Models.Vector_Model.vector_search_engine import VectorSearchEngine
from data.indexer import Indexer
from data.search_engine import BaseSearchEngine
from data.corpus_manager import Collection
import environment 

import time


def main():
    print('\n Sistema de recuperación de información RIUL !!!')
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
            environment.Environment.index = index
            environment.Environment.search_engine = VectorSearchEngine(index,docs)
   
if __name__ == '__main__':
    main()





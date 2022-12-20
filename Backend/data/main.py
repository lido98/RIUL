from ast import Mod
from data.Corpus.CRAN.cran_parser import CRANParser
from data.Models.Vector_Model.vector_search_engine import VectorSearchEngine
from data.Models.Latent_Semantic_Indexing_Model.latent_semantic_search_engine import LatentSemanticSearchEngine
from data.indexer import Indexer
from data.search_engine import BaseSearchEngine
from data.corpus_manager import Collection, Document
from data.Metrics.testing import test_cases
from data.interactive import select
import environment 

import time



def main():
    print('\n Sistema de recuperación de información RIUL !!!')
    
    selection = select()
    corpus = selection[0]
    model = selection[1]   

    docs: Collection
    match corpus:
        case 'CRAN':
            docs = CRANParser()()
            # docs = Collection([Document(1, 'doc 1', 'leon leon leon'),Document(2, 'doc 2', 'leon leon leon zorro'),Document(3, 'doc 3', 'leon zorro nutria'),Document(4, 'doc 4', 'leon leon leon zorro zorro zorro'),Document(5, 'doc 5', 'nutria')])
    
    index = Indexer(docs)()
    environment.Environment.index = index
    
    match model:
        case 'VECTORIAL':            
            environment.Environment.search_engine = VectorSearchEngine(index,docs)
        case 'LSI':
            environment.Environment.search_engine = LatentSemanticSearchEngine(index,docs,200)

    if selection[2] == True:
        test_cases()
    # q = 'what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft'
    # rank = environment.Environment.search_engine(q)
    # a = 9





if __name__ == '__main__':
    main()





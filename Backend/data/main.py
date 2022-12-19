from data.Models.Latent_Semantic_Indexing_Model.matrixLatent import MatrixLatent
from data.corpus_manager import Document
from data.trie import Trie
from data.Corpus.CRAN.cran_parser import CRANParser
from data.Models.Vector_Model.vector_search_engine import VectorSearchEngine
from data.indexer import Indexer
from data.search_engine import BaseSearchEngine
from data.corpus_manager import Collection
import environment 
from data.Models.Boolean_Model.base import BoolMatrix


def main():
    print('\n Sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')
    
    docs: Collection
    corpus = 'cran'
    match corpus:
        case 'cran':
            docs = CRANParser()()

    trie = Trie(root=True)
    trie(docs)
    matrix = MatrixLatent(trie)
    a = ""
    #region Vector Model
    # model = 'vector'   
    # search_engine: BaseSearchEngine     
    # match model:
    #     case 'vector':            
    #         index = Indexer(docs)()
    #         environment.Environment.index = index
    #         environment.Environment.search_engine = VectorSearchEngine(index,docs)
    #endregion
   
if __name__ == '__main__':
    main()





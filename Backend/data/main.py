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
    
    # docs: Collection
    # corpus = 'cran'
    # match corpus:
    #     case 'cran':
    #         docs = CRANParser()()


    #region Boolean Model
    #Documentos de prueba para el booleano
    text1 = open("Backend\data\Models\Boolean_Model\\tests\\test1.txt","r").read()
    text2 = open("Backend\data\Models\Boolean_Model\\tests\\test2.txt","r").read()
    text3 = open("Backend\data\Models\Boolean_Model\\tests\\test3.txt","r").read()
    text4 = open("Backend\data\Models\Boolean_Model\\tests\\test4.txt","r").read()
    docs_list = [Document(1,"title",text1),Document(2,"title",text2),Document(3,"title",text3),Document(4,"title",text4)]
    docs = Collection(docs_list)

    trie = Trie(root=True)
    trie(docs)
    BoolMatrix(trie)
    #endregion

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





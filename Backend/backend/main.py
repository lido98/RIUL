from backend.Corpus.CRAN.cran_parser import CRANParser
from backend.Corpus.Reuters.reut_parser import ReutersParser
from backend.ranking_manager import Ranking
from backend.corpus_manager import Collection, Document
from backend.Trie.trie import Trie, VectorialMatrix

from environment import Environment

def main():
    print('\n Sistema de Recuperación de Información RIUL !!!\n')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')
    print('El proceso de crear las estructuras de almacenamiento esta ejecucion, este proceso puede tardar unos segundos.\n')

    Environment.trie = Trie(root = True)
    collection = CRANParser()()
    import time
    t0 = time.time()
    #region create trie
    docs = Collection([Document(1, 'doc 1', 'leon leon leon'),Document(2, 'doc 2', 'leon leon leon zorro'),Document(3, 'doc 3', 'leon zorro nutria'),Document(4, 'doc 4', 'leon leon leon zorro zorro zorro'),Document(5, 'doc 5', 'nutria')])

    Environment.trie.insert_collection(collection)
    # Environment.trie.insert_collection(docs)
    print("\nEl trie ha sido creado correctamente.  [" +str(time.time()-t0)+"s]") 

    t1 = time.time()
    Environment.matrix = VectorialMatrix(Environment.trie)
    print("\nLa matriz del modelo vectorial ha sido creada correctament.e  [" +str(time.time()-t1)+"s]")

    print("\nEl environment ha sido creado correctamente.  [" +str(time.time()-t0)+"s]") 
    
    # rank = Environment.matrix.get_rank_of_query("an empirical evaluation of the destalling effects was made for the specific configuration of the experiment")

    # for doc,i in zip(rank,range(50)):
    #     print(str(i)+". ___["+str(doc.id) +"] >>>> rank = " + str(rank[doc]))        

    
    

if __name__ == '__main__':
    main()





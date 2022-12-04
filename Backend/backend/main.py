from backend.Corpus.CRAN.cran_parser import CRANParser
from backend.Corpus.Reuters.reut_parser import ReutersParser
from backend.ranking_manager import Ranking
from backend.corpus_manager import Collection, Document
from backend.Trie.trie import Trie, VectorialMatrix

from environment import Environment

def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')
    Environment.trie = Trie(root = True)
    collection = CRANParser()()
    import time
    t0 = time.time()
    #region create trie
    
    Environment.trie.insert_collection(collection)
    print("\nTarda " +str(time.time()-t0)+" para crear el trie.") 

    t1 = time.time()
    Environment.matrix = VectorialMatrix(Environment.trie)
    print("\nTarda " +str(time.time()-t1)+" para crear la matriz.")

    print("\nTarda " +str(time.time()-t0)+" para crear todo.") 
    
    
    

if __name__ == '__main__':
    main()





from Trie.collection import Document
from Trie.trie import Trie, Collection, VectorialMatrix
from Corpus.CRAN.cran_parser import CRANParser

def main ():
    test_cases_trie()

def test_cases_trie():
    trie = Trie(root = True)
    collection = CRANParser()()
    import time
    t0 = time.time()
    #region create trie
    
    trie.insert_collection(collection)
    print("\nTarda " +str(time.time()-t0)+" para crear el trie.") 

    t1 = time.time()
    matrix = VectorialMatrix(trie)
    print("\nTarda " +str(time.time()-t1)+" para crear la matriz.")

    print("\nTarda " +str(time.time()-t0)+" para crear todo.") 
    
    while(True):
      print("Entre la consulta:\n")    
      consult = input()
      t2 = time.time()
      rank = matrix.get_rank_of_query(consult)
      print("\nTarda " +str(time.time()-t2)+" para crear el rank.") 


      print ("\nRANK\n")  
      for doc,i in zip(rank, range(10)):
            print (str(i)+". ___[id:"+str(doc.id)+"]"+ " >>> rank = " + str(rank[doc]))
      print("\n")

main()

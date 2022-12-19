from math import log10
from data.trie import Trie
import numpy as np
class MatrixLatent:
    def __init__(self,trie:Trie):
        self.trie = trie
        self.index_document = trie.index_document
        self.matrix = []
        self.full_matrix()
        T, S, D = np.linalg.svd(self.matrix)
        a = 1        

    def full_matrix(self):
        print("Se esta creando la matriz del modelo Semantica Latente, este proceso puede tardar unos segundos...")
        import time
        t0 = time.time()    
       


        trie = self.trie

        for i in range(trie.total_documents):
            self.matrix.append([0]*len(trie.words))

        for word,i in zip(trie.words, range(len(trie.words))):
            gi = self.gi(word)
            for document in trie.documents_of_word(word):
                wij = gi* log10(self.tf(word,document)+1)
                self.matrix[self.index_document[document]][i] = wij

        print ("La matriz ha sido creada satisfactoriamente.  ["+ str(time.time()-t0)+" s]")
    
    def gi(self,word):
        gf = self.trie.get_total_count(word)
        sum = 0
        for document in self.trie.documents_of_word(word):
            tf = self.tf(word,document)
            value =self.pij(tf,gf) 
            sum += (value*log10(value))
        return 1 + sum/log10(self.trie.total_documents)

    def pij(self, tf,gf): return tf/gf

    def tf(self,word,document):    
        n = self.trie.word_count_in_document(word,document)    
        d = self.trie.max_count_in_document[document]
        return n/d
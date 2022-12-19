from data.search_engine import BaseSearchEngine
from data.indexer import InvertedIndex
from data.corpus_manager import Collection, Document
import numpy as np
from data.trie import Trie
from math import log10
import time


class LatentSemanticSearchEngine(BaseSearchEngine):
    def __init__(self, index: InvertedIndex, docs: Collection, k: int):
        self.index = index
        self.docs = docs
        self.matrix = LatentSemanticMatrix(self.index.trie).matrix

        D, S, T = np.linalg.svd(self.matrix, full_matrices = False)

        D_k = T[:, :k]
        S_k = np.diag(S[:k])
        T_k = D[:k, :]

        self.matrix = np.dot(np.dot(D_k, S_k), T_k)
        a = 5

    def __call__(self, raw_query: str, top: int = 0.050) -> dict[Document: float]:
        
        sim = self.vectors.get_rank_of_query(raw_query)  
              
        result = {}               
        for doc in sim:
            if sim[doc]<=top:
                break
            result[doc] = sim[doc]        
        return result   

          

class LatentSemanticMatrix:
    def __init__(self,trie:Trie):
        self.trie = trie
        self.index_document = trie.index_document
        self.matrix = []
        self.full_matrix() 
                

    def full_matrix(self):
        trie = self.trie

        for i in range(trie.total_documents):
            self.matrix.append([0]*len(trie.words))

        for i,word in enumerate(trie.words):            
            docs = trie.documents_of_word(word)
            gi = self.gi(word)
            for document in docs:
                wij = gi * log10(self.tf(word,document)+1)
                self.matrix[self.index_document[document]][i] = wij
    
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

    def freqs_in_query(self, query):
        result = {}
        max_count = 1
        for term in query.split(" "):
            try: 
                result[term] +=1
                max_count = max(max_count,result[term])
            except: result [term] = 1
            
        return [result,max_count]    
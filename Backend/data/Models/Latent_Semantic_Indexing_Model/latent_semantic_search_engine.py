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
        self.latent = LatentSemanticMatrix(self.index.trie)
        self.matrix = self.latent.matrix

        D, S, T = np.linalg.svd(self.matrix, full_matrices = False)

        D_k = T[:, :k]
        S_k = np.diag(S[:k])
        T_k = D[:k, :]

        self.matrix = np.dot(np.dot(D_k, S_k), T_k)
        a = 5

    def __call__(self, raw_query: str, top: int = 0.050) -> dict[Document: float]:
        
        sim = self.latent.get_rank_of_query(raw_query)  
              
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
        self.index_word = {}
        self.full_matrix_and_norms() 

         
    def full_matrix_and_norms(self):
        print("Se esta creando la matriz del modelo vectorial y las normas de cada vector, este proceso puede demorar unos segundos...")
        import time
        t0 = time.time()    
        
        self.full_matrix()
        self.norms = {}
        self.full_norms()

        print ("La matriz y la normas han sido creadas satisfactoriamente.  ["+ str(time.time()-t0)+" s]")            

    def full_matrix(self):
        trie = self.trie

        for i in range(trie.total_documents):
            self.matrix.append([0]*len(trie.words))

        for i,word in enumerate(trie.words):
            self.index_word[word] = i            
            docs = trie.documents_of_word(word)
            gi = self.gi(word)
            for document in docs:
                wij = gi * log10(self.tf(word,document)+1)
                self.matrix[self.index_document[document]][i] = wij
    
    def gi(self,word, q = 0,f = 0):
        '''f is freqs by word in query, q is 1 if gi is used for query'''
        gf = self.trie.get_total_count(word) + q
        sum = 0
        for document in self.trie.documents_of_word(word):
            tf = self.tf(word,document)
            value =self.pij(tf,gf) 
            sum += (value*log10(value))
        if f != 0:
           tf = f
           value =self.pij(tf,gf) 
           sum += (value*log10(value))
        return 1 + sum/log10(self.trie.total_documents+q)

    def pij(self, tf,gf): return tf/gf

    def tf(self,word,document):    
        return self.trie.word_count_in_document(word,document)    
        d = self.trie.max_count_in_document[document]
        return n/d


    def freqs_in_query(self, query):
        result = {}
        for term in query.split(" "):
            try: 
                result[term] +=1
                max_count = max(max_count,result[term])
            except: result [term] = 1
            
        return result

    def sim_list(self, query):
        freqs = self.freqs_in_query(query)
        
        vector_query = []
        N = self.trie.total_documents

        query_list_index_value = []
        by_norm_query = []
        for word in freqs:
            try:
                lij = log10(freqs[word]+1)
                gi = self.gi(word,1,freqs[word])
                by_norm_query.append(lij*gi)
                word_index_value = self.index_word[word]
                query_list_index_value.append(word_index_value)
                vector_query.append(lij*gi)
            except: pass

        rank = {}
        
        norm_query = np.linalg.norm(by_norm_query)
        new_matrix = []
        for i in range(self.trie.total_documents):
            new_matrix.append([])
            for index in query_list_index_value:
                value = self.matrix[i][index]
                new_matrix[i].append(value)

    
        for document,d in zip(new_matrix, range(len(self.matrix))):
            doc = self.trie.documents[d]
            norm_doc = self.norms[doc]
                
            rank[doc]= self.sim(document, vector_query,norm_doc, norm_query) 
        return rank

    def sim (self, doc, query, norm_doc, norm_query):
        num = np.dot(doc, query)
        sim = num/(norm_doc*norm_query)
        return sim
    
    def full_norms(self):
        for doc,vector in zip(self.trie.documents, self.matrix):
            self.norms[doc] = np.linalg.norm(vector)

    def get_rank_of_query(self,query):
        result = sorted(self.sim_list(query).items(), key=lambda item: item[1])
        result = dict(reversed(list(result)))
        return result
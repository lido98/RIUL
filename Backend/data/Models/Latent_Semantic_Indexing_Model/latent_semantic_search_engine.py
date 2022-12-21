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
        self.matrix = np.transpose(self.latent.matrix)

        T, S, D = np.linalg.svd(self.matrix, full_matrices = False)

        self.T_k = T[:, :k]
        self.S_k = np.diag(S[:k])
        self.D_k = D[:k, :]

        #self.matrix = np.dot(np.dot(self.T_k, self.S_k), self.D_k)
        self.matrix = np.transpose(self.D_k)
        self.norms = self.full_norms()
        

    def __call__(self, raw_query: str, top: int = 0.050) -> dict[Document: float]:
        
        query_vector = self.latent.get_query_vector(raw_query)  
        
        q_k = np.dot(np.dot(np.linalg.inv(self.S_k), np.transpose(self.T_k)), np.transpose(query_vector))

        sim = self.get_rank_of_query(np.transpose(q_k))


        result = {}               
        for doc in sim:
            if sim[doc]<=top:
                break
            result[doc] = sim[doc]        
        return result   

    def sim_list(self, query):
        rank = {}

        norm_query = np.linalg.norm(query)
            
        for i, doc_vector in enumerate(self.matrix):
            doc = self.index.trie.documents[i]
            norm_doc = self.norms[i]                
            rank[doc]= self.sim(doc_vector, query, norm_doc, norm_query) 
        return rank

    def sim (self, doc, query, norm_doc, norm_query):
        num = np.dot(doc, query)
        sim = num/(norm_doc*norm_query)
        return sim

    def get_rank_of_query(self,query):
        result = sorted(self.sim_list(query).items(), key=lambda item: item[1])
        result = dict(reversed(list(result)))
        return result

    def full_norms(self):
        norms = []
        for doc in self.matrix:
            norms.append(np.linalg.norm(doc))
        return norms

          

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
        #self.norms = {}
        #self.full_norms()

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
    
    # def gi(self,word):        
    #     gf = self.trie.get_total_count(word)
    #     sum = 0
    #     for document in self.trie.documents_of_word(word):
    #         tf = self.tf(word,document)
    #         pij =self.pij(tf,gf) 
    #         sum += (pij*log10(pij))        
    #     return 1 + sum/log10(self.trie.total_documents)

    def pij(self, tf,gf): return tf/gf

    def tf(self,word,document):    
        return self.trie.word_count_in_document(word,document)    
        


    def freqs_in_query(self, query):
        result = {}
        for term in query.split(" "):
            try: 
                result[term] +=1
                max_count = max(max_count,result[term])
            except: result [term] = 1
            
        return result

    def get_query_vector(self, query):
        freqs = self.freqs_in_query(query)
        
        query_vector = [0] * len(self.trie.words)       
        
        for i,word in enumerate(self.trie.words):
            try:
                lij = log10(freqs[word]+1)
                gi = self.gi(word,1,freqs[word])                
                query_vector[i] = lij*gi
            except:
                continue
        return query_vector        
        
    
    

    
from data.search_engine import BaseSearchEngine
from data.indexer import InvertedIndex
from data.corpus_manager import Collection
import numpy as np
from data.trie import Trie
from math import log10
import time
class VectorSearchEngine(BaseSearchEngine):
    def __init__(self, index: InvertedIndex, docs: Collection):
        self.index = index
        self.docs = docs
        self.vectors = VectorMatrix(self.index.trie)

    def __call__(self, raw_query: str, top: int = 0.50, a: int = 0.5) -> dict[Collection: float]:
        #query = VectorQuery(raw_query)
        #query_index = query.query_index
                 
        sim = self.vectors.get_rank_of_query(raw_query)  
              
        result = {}               
        for doc in list(filter(lambda t: sim[t] > top, sim)):
            result[doc] = sim[doc]        
        return result        
        
    
class VectorMatrix:
    def __init__(self,trie:Trie):
        self.trie = trie
        self.words = trie.words
        self.total_documents = trie.total_documents
        self.index_word = {}
        self.rank = {}
        self.full_matrix_and_norms()
        
    def full_matrix_and_norms(self):
        print("Se esta creando la matriz del modelo vectorial y las normas de cada vector, este proceso puede demorar unos segundos...")
        import time
        t0 = time.time()    
        
        self.matrix = self.full_matrix(self.trie)
        self.norms = {}
        self.full_norms()

        print ("La matriz y la normas han sido creadas satisfactoriamente.  ["+ str(time.time()-t0)+" s]")

    def full_matrix(self,trie:Trie):
        words = self.words

        matrix = []
        
        for i in range(trie.total_documents):
            matrix.append([0] * len(words))

        for word,w in zip(words, range(len(words))):
            self.index_word[word] = w
            documents = trie.documents_of_word(word)
            for document in documents:
                d = trie.index_document[document]
                matrix[d][w] = trie.weight(word,document) 
        return matrix        
    
    def get_matrix(self):
        return self.matrix
    
    def freqs_in_query(self, query):
        result = {}
        max_count = 1
        for term in query.split(" "):
            try: 
                result[term] +=1
                max_count = max(max_count,result[term])
            except: result [term] = 1
            
        return [result,max_count]

    def sim_list(self, query):
        freqs = self.freqs_in_query(query)
        
        vector_query = []
        a = 0.5
        N = self.total_documents

        query_list_index_value = []
        by_norm_query = []
        for word in freqs[0]:
            n_i = len(self.trie.documents_of_word(word))
            try:
                by_norm_query.append((a +((1-a)*(freqs[0][word]/freqs[1])))* (log10(N/n_i)))
                word_index_value = self.index_word[word]
                query_list_index_value.append(word_index_value)
                vector_query.append((a +((1-a)*(freqs[0][word]/freqs[1])))* (log10(N/n_i)))
            except: pass

        rank = {}
        
        norm_query = np.linalg.norm(by_norm_query)
        new_matrix = []
        for i in range(self.total_documents):
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


    

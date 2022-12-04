from search_engine import BaseSearchEngine
from Models.Vector_Model.vector_indexer import VectorInvertedIndex
from Models.Vector_Model.vector_parse_query import VectorQuery
from corpus_manager import Collection, Document
import numpy as np

class VectorSearchEngine(BaseSearchEngine):
    def __init__(self, index: VectorInvertedIndex, docs: Collection):
        self.index = index
        self.docs = docs

    def __call__(self, raw_query: str, top: int = 0.05, a: int = 0.5) -> Collection:
        query = VectorQuery(raw_query)
        query_index = query.query_index
        
        docs_vec = []        
        for i in range(len(self.docs)):                     
            docs_vec.append([0] * len(self.index))
        
        query_vec = [0] * len(self.index)
        
        for i, term in enumerate(self.index.__iter__()):
            for j in range(len(self.docs)):
                try:                
                    docs_vec[j][i] = self.index.get_weight(term, self.docs[j])
                except:
                    continue
            try:
                query_vec[i] = (a + (1-a)*query_index.get_tf(term, query.doc))*self.index.get_idf(term)
            except:
                continue
            
            
        #print(time.time()-t0)
             
        
        
        #t0 = time.time()   
        sim = []        
        
        #print(query_vec)
        for i in range(len(self.docs)):   
            #print(docs_vec[i])         
            sim.append((i, self.sim(docs_vec[i],query_vec)))      
        
        sorted_filtered_doc_sim = sorted(list(filter(lambda t: t[1] > top, sim)), key= lambda x: x[1])
        list.reverse(sorted_filtered_doc_sim) #
        #print(time.time()-t0)
        return sorted_filtered_doc_sim                                 
        
    def sim(self, doc, query):
        return np.dot(doc, query)/(np.linalg.norm(doc)*np.linalg.norm(query))

    

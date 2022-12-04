from backend.corpus_manager import Collection, Document
#from indexer import BaseIndexer, BaseInvertedIndex
from backend.Models.Vector_Model.vector_indexer import VectorIndexer, VectorInvertedIndex
from backend.query_parser import QueryIndexer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Ranking():
    def __init__(self, top):
        self.top = top
        
    

    def rec_files(self, docs: Collection, query, a = 0.5):
        query_doc = Document(0, 'query', query)
        #docs.__add__(query_doc)        
        si = VectorIndexer(docs)
        index = si()     
        
        docs_vec = []
        for i in range(len(docs)):                     
            docs_vec.append([0] * len(index))
        
        qd = Document(0,'query',query)
        qi = VectorIndexer(Collection([qd]))()
        query_vec = [0] * len(index)
        
        for i, term in enumerate(index.__iter__()):
            for j in range(len(docs)):
                try:                
                    docs_vec[j][i] = index.get_weight(term, docs[j])
                except:
                    continue
            try:
                query_vec[i] = (a + (1-a)*qi.get_tf(term, qd))*index.get_idf(term)
            except:
                continue
        
             
        
        
           
        sim = []        
        
        #print(query_vec)
        for i in range(len(docs)):   
            #print(docs_vec[i])         
            sim.append((i, self.sim(docs_vec[i],query_vec)))      
        
        sorted_filtered_doc_sim = sorted(list(filter(lambda t: t[1] > self.top, sim)), key= lambda x: x[1])
        list.reverse(sorted_filtered_doc_sim) #
        return sorted_filtered_doc_sim                                 
        
    def sim(self, doc, query):
        return np.dot(doc, query)/(np.linalg.norm(doc)*np.linalg.norm(query))

    


         
        

    
    


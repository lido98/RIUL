from corpus_manager import Collection, Document
from indexer import Indexer, InvertedIndex
from query_parser import QueryIndexer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Ranking():
    def __init__(self, top):
        self.top = top
        
    def __call__(self, docs, query, a = 0.5):
        si = Indexer(docs)
        doc_w = si()                       
         
        query_w = QueryIndexer(si.vocabulary , a)(query) 
        
        cos = cosine_similarity(doc_w, query_w.reshape(1, -1))

        
        doc_sim = []
        for i in range(len(docs)):
            doc_sim.append((i, cos[i]))            
        sorted_filtered_doc_sim = sorted(list(filter(lambda t: t[1] > self.top, doc_sim)), key= lambda x: x[1])
        list.reverse(sorted_filtered_doc_sim)
        return sorted_filtered_doc_sim

    def rec_files(self, docs: Collection, query, a = 0.5):
        query_doc = Document(0, 'query', query)
        docs.__add__(query_doc)        
        si = Indexer(docs)
        index = si.build_index()
        
        
        docs_vec = []
        for i in range(len(docs)-1):
            #print(docs[i].title + ' ' + index.max_freq[docs[i]])
            
            docs_vec.append([0] * len(index))
        query_vec = [0] * len(index)

        
        for i, term in enumerate(index.__iter__()):
            for j in range(len(docs)-1):
                try:                
                    docs_vec[j][i] = index.get_weight(term, docs[j])
                except:
                    continue
            try:
                query_vec[i] = (a + (1-a)*index.get_tf(term, docs[len(docs)-1]))*index.get_idf(term) 
            except:
                continue   
            
            
        sim = []        
        
        #print(query_vec)
        for i in range(len(docs)-1):   
            #print(docs_vec[i])         
            sim.append((i, self.sim(docs_vec[i],query_vec)))      
        
        sorted_filtered_doc_sim = sorted(list(filter(lambda t: t[1] > self.top, sim)), key= lambda x: x[1])
        list.reverse(sorted_filtered_doc_sim) #
        return sorted_filtered_doc_sim                                 
        
    def sim(self, doc, query):
        return np.dot(doc, query)/(np.linalg.norm(doc)*np.linalg.norm(query))

    


         
        

    
    



from .corpus_manager import Collection, Document
from .indexer import Indexer, InvertedIndex
from .query_parser import QueryIndexer
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
        #relevant_terms = docs[len(docs)-1].body.split( )
        #print(relevant_terms)
        docs_vec = [[0] * len(index)] * (len(docs)-1)
        query_vec = [0] * len(index)

        
        for i, term in enumerate(index.__iter__()):
            for j in range(len(docs)-1):
                if docs[j] in index.vocabulary[term]:
                    docs_vec[j][i] = index.get_weight(term, docs[j])
            if docs[len(docs)-1] in index.vocabulary[term]:
                query_vec[i] = (a + (1-a)*index.get_tf(term, docs[len(docs)-1]))*index.get_idf(term)        
            
        print(index.max_freq)
        sim = []
        
        
        for i in range(len(docs_vec)-1):            
            sim.append((i, self.sim(docs_vec[i],query_vec)))
      
        
        sorted_filtered_doc_sim = sorted(sim, key= lambda x: x[1])
        list.reverse(sorted_filtered_doc_sim) #list(filter(lambda t: t[1] > self.top, sim))
        return sorted_filtered_doc_sim       

                            
        
    def sim(self, doc, query):
        #doc, query = np.array(doc, dtype=np.float32), np.array(query, dtype=np.float32)
        return np.dot(doc, query)/(np.linalg.norm(doc)*np.linalg.norm(query))

    


         
        

    
    



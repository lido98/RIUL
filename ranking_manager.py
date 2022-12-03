from .indexer import Indexer
from .query_parser import QueryIndexer
from sklearn.metrics.pairwise import cosine_similarity

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
    
    



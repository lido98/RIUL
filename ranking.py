from indexer import BasicIndexer,QueryIndexer
import math

class Ranking():
    def __init__(self, top = 0.1):
        self.top = top
        
    def __call__(self, docs, query, a = 0.5):
        doc_indices = BasicIndexer()(docs)               
        doc_vectors = []        
        for doc in doc_indices:
            doc_vectors.append([word_w[1] for word_w in doc])

        query_index = QueryIndexer(query, a)(docs) 
        query_vector = [word_w[1] for word_w in query_index]
        doc_sim = []
        for i in range(len(doc_vectors)):
            doc_sim.append((i, Ranking.sim(doc_vectors[i],query_vector)))
        sorted_filtered_doc_sim = sorted(list(filter(lambda t: t[1] > self.top, doc_sim)), key= lambda x: x[1])
        list.reverse(sorted_filtered_doc_sim)
        return sorted_filtered_doc_sim
    
    def sim(doc, query):
        return Ranking.scalar_product(doc, query) / (Ranking.norm(doc)*Ranking.norm(query))     
    def scalar_product(vec1, vec2):
        sp = 0
        for i in range(len(vec1)):
            sp += vec1[i] * vec2[i]
        return sp    
    def norm(vec):
        n = 0
        for comp in vec:
            n += comp ** 2
        return math.sqrt(n)



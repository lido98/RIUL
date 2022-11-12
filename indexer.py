from abc import ABC, abstractmethod
import math

class BaseIndexer(ABC):

    def __call__(self, docs_bodie):        
        
        vocabulary, tokenized_docs = self.select_keywords(docs_bodie)
        N = len(vocabulary)
        n = [0] * N       
        tf = []
        
        for doc in tokenized_docs:
            freq = [0] * N
            max_freq = 0
            mask_n = [False] * N

            for word in doc:        

                word_index = vocabulary.index(word)
                if not mask_n[word_index]:
                    n[word_index] += 1
                    mask_n[word_index] = True
                
                freq[word_index] += 1
                max_freq = max(max_freq, freq[word_index])
            
            tf_doc = [freq_i_doc / max_freq for freq_i_doc in freq]
            tf.append(tf_doc)

        idf = [math.log10(len(docs_bodie) / n_i) for n_i in n]   
        
        indices = [None] * len(docs_bodie)
        for i in range(len(docs_bodie)):
            indices[i] = [None]*N
            for j in range(N):
                w = self.calculate_weight(tf[i][j], idf[j])
                indices[i][j] = (vocabulary[j],w)
        return indices      
    
    @abstractmethod
    def select_keywords(self, docs_bodie) -> list[str]:
        pass

    @abstractmethod
    def calculate_weight(self, tf, idf):
        pass



class BasicIndexer(BaseIndexer):
    def select_keywords(self, docs_bodie):
        keywords: set[str] = set()
        tokenized_docs = []
        for doc in docs_bodie:
            tokenized_doc = doc.split()
            tokenized_docs.append(tokenized_doc)
            for keyword in tokenized_doc:
                keywords.add(keyword)
        return list(keywords), tokenized_docs
    
    def calculate_weight(self, tf, idf):
        return tf * idf

class QueryIndexer(BasicIndexer):
    def __init__(self, query, a = 0.5):
        self.query = query
        self.a = a

    def select_keywords(self, docs_bodie):
        docs_bodie.append(self.query)
        return super().select_keywords(docs_bodie)        

    def calculate_weight(self, tf, idf):
        return (self.a + (1 - self.a) * tf) * idf
    
    def __call__(self, docs_bodie):
        docs_w = super().__call__(docs_bodie)
        return docs_w[len(docs_w)-1]




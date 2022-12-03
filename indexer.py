from .corpus_manager import Collection, Document
from abc import ABC, abstractmethod
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import math

class InvertedIndex:
    def __init__(self):
        self.vocabulary: dict[str: dict[Document: int]] = {} 
        self.max_freq: dict[Document: int] = {} 

    def get_tf(self, term, doc):
        return self.vocabulary[term][doc]/self.max_freq[doc]

    def get_idf(self, term):
        return math.log(len(self.max_freq) / len(self.vocabulary[term]))

    def get_weight(self, term, doc):
        return self.get_tf(term, doc) * self.get_idf(term)

    def __len__(self) -> int:
        return len(self.vocabulary)

    def __iter__(self):           
        return self.vocabulary



class Indexer: 
    def __init__(self, docs: Collection):
        self.docs = docs            

    
    def build_index(self) -> InvertedIndex:
        index = InvertedIndex()
        vocabulary: dict[str: dict[Document: int]] = {}
        max_freq: dict[Document: int] = {} 

        stop_words = set(stopwords.words('english'))
        
        for i in range(len(self.docs)):
            doc = self.docs[i]
            term_bag, self.docs.docs[i] = self.extract_keywords(doc, stop_words)

            for term in term_bag:                
                if term in vocabulary: 
                    term_dict = vocabulary[term]  
                    if doc in term_dict:             
                        term_dict[doc] += 1
                        max_freq[doc] = max(max_freq[doc], term_dict[doc])
                    else:                      
                        term_dict[doc] = 1
                        max_freq[doc] = 1                                             
                else:
                    vocabulary[term] = {doc : 1}
                    max_freq[doc] = 1  
        index.vocabulary = vocabulary         
        index.max_freq = max_freq       
        return index

    def extract_keywords(self, doc: Document, stop_words: set) -> tuple[list[str], Document]:
        id, title, body = doc.id, doc.title, doc.body.lower()
        tokenized_body = word_tokenize(body)
        tokenized_body = [WordNetLemmatizer().lemmatize(w) for w in tokenized_body]
        tokenized_body = [token for token in tokenized_body if not token in stop_words]
        doc = Document(id, title, " ".join(tokenized_body))
        return tokenized_body, doc
        
    def __call__(self) -> InvertedIndex: 
        self.vocabulary, tok_docs = self.extract_vocabulary(self.docs.doc_bodies())           
        vectorize = TfidfVectorizer(vocabulary=self.vocabulary)
        weight = vectorize.fit_transform(tok_docs)
        return weight

    def extract_vocabulary(self, docs_text: list[str]) -> list[str]:
        stop_words = set(stopwords.words('english'))
        words = set()
        tokenized_docs = []
        for doc in docs_text:
            tokenized = word_tokenize(doc.lower())
            tokenized = [WordNetLemmatizer().lemmatize(w) for w in tokenized]
            tokenized = [token for token in tokenized if not token in stop_words]
            for token in tokenized:
                words.add(token)
            tokenized_docs.append(" ".join(tokenized))            
        return list(words), tokenized_docs

        







    






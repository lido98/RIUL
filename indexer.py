from abc import ABC, abstractmethod
import math
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

class BaseIndexer(ABC): 
    def __call__(self, docs_bodie):        
        
        self.vocabulary = self.select_keywords(docs_bodie)
        vectorize = TfidfVectorizer(vocabulary=self.vocabulary)
        weight = vectorize.fit_transform(docs_bodie)
        
        return weight
    
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
        return list(keywords)
    
    def calculate_weight(self, tf, idf):
        return tf * idf

class SmartIndexer(BaseIndexer):
    def __init__(self) -> None:
        self.vocabulary = []

    def select_keywords(self, docs_bodie) -> list[str]:
        stop_words = set(stopwords.words('english'))
        keywords: set[str] = set()
        tokenized_docs = []
        for doc in docs_bodie:
            doc = doc.lower()
            tokenized_doc = word_tokenize(doc)
            tokenized_doc = [WordNetLemmatizer().lemmatize(w) for w in tokenized_doc]
            tokenized_doc = [token for token in tokenized_doc if not token in stop_words]
            tokenized_docs.append(tokenized_doc)
            for keyword in tokenized_doc:
                keywords.add(keyword)
        return list(keywords)

    def calculate_weight(self, tf, idf):
        return tf * idf


class QueryIndexer():
    def __init__(self, vocabulary, a = 0.5):
        self.a = a
        self.vocabulary = vocabulary

    
    def calculate_weight(self, tf, idf):
        return (self.a + (1 - self.a) * tf) * idf

    def select_keywords(self, query) -> list[str]:
        stop_words = set(stopwords.words('english'))
        tokenized = word_tokenize(query)
        tokenized = [WordNetLemmatizer().lemmatize(w) for w in tokenized]
        tokenized = [token for token in tokenized if not token in stop_words]

        return " ".join(tokenized)
        
    
    def __call__(self, query):
        query = query.lower()
        query = self.select_keywords(query)
        vectorize = TfidfVectorizer(vocabulary=self.vocabulary)
        weight = vectorize.fit_transform([query])
        return weight



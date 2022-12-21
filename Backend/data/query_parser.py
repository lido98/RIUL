from abc import ABC, abstractmethod
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

class BaseQueryParser(ABC):
    def __init__(self, raw_query: str):
        prepocessed_query = self.preprocessing_query(raw_query)
        self.query = self.parse_query(prepocessed_query)
     
    @abstractmethod
    def parse_query(self, raw_query):
        pass
    
    def preprocessing_query(self, raw_query: str) -> str:
        stop_words = set(stopwords.words('english'))
        tokenized_query = raw_query.lower().split()
        tokenized_query = [word for word in tokenized_query if not word in stop_words]
        tokenized_query = [PorterStemmer().stem(word) for word in tokenized_query]
        return " ".join(tokenized_query)
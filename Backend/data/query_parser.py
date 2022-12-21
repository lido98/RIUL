from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from abc import ABC, abstractmethod


class BaseQuery(ABC):
    def __init__(self, raw_query: str):
        self.parse_query(raw_query)
     
    @abstractmethod
    def parse_query(self, raw_quey):
        pass


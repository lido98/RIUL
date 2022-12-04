from corpus_manager import Collection, Document
from abc import ABC, abstractmethod
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import math



class BaseInvertedIndex(ABC):    
    @abstractmethod
    def __getitem__(self, term: str) -> Collection:
        pass      



class BaseIndexer(ABC): 
    def __init__(self, docs: Collection):
        self.docs = docs        

    @abstractmethod
    def __call__(self) -> BaseInvertedIndex:
        pass

    
    
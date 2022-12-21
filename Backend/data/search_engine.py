from data.indexer import InvertedIndex
from data.query_parser import BaseQuery
from data.corpus_manager import Document, Collection
from abc import ABC, abstractmethod

class BaseSearchEngine(ABC):
    @abstractmethod
    def __init__(self, index: InvertedIndex):
        self.index = index
        

    @abstractmethod  
    def __call__(raw_query: str, top: int = 0.1) -> dict[Collection: float]:        
        pass




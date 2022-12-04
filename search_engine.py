from indexer import BaseInvertedIndex
from query_parser import BaseQuery
from corpus_manager import Document, Collection
from abc import ABC, abstractmethod

class BaseSearchEngine(ABC):
    @abstractmethod
    def __init__(self, index: BaseInvertedIndex):
        self.index = index
        

    @abstractmethod  
    def __call__(raw_query: str, top: int = 0.05) -> Collection:        
        pass




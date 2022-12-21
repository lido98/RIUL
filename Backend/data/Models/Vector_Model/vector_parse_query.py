from query_parser import BaseQuery
from corpus_manager import Document
from indexer import InvertedIndex

class VectorQuery(BaseQuery):
    def __init__(self, raw_query: str):
        self.doc = Document(-1,'query',raw_query)
        self.query_index = InvertedIndex([self.doc])()
        
    
        

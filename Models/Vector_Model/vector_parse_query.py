from query_parser import BaseQuery
from Models.Vector_Model.vector_indexer import VectorIndexer, VectorInvertedIndex
from corpus_manager import Document,Collection

class VectorQuery(BaseQuery):
    def __init__(self, raw_query: str):
        self.doc = Document(-1,'query',raw_query)
        self.query_index = VectorIndexer([self.doc])()
        
    
        

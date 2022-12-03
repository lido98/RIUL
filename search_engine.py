from .indexer import InvertedIndex
from .query_parser import Query
from .corpus_manager import Document

class SearchEngine:
    def __call__(index: InvertedIndex, query: Query) -> dict[Document: int]:
        # ...
        pass


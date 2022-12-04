from corpus_manager import Collection
from trie import Trie
from abc import ABC, abstractmethod
from nltk import word_tokenize
from nltk.corpus import stopwords
import math


class InvertedIndex: 
    def __init__(self):
        self.trie = Trie(root=True)       

class Indexer: 
    def __init__(self, docs: Collection):
        self.docs = docs        
    
    def __call__(self) -> InvertedIndex:
        index = InvertedIndex()
        index.trie(self.docs)
        return index

    
    
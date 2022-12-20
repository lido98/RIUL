<<<<<<< HEAD
from data.corpus_manager import Collection, Document
from data.trie import Trie
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import time
=======
from data.corpus_manager import Collection
from data.trie import Trie
from abc import ABC, abstractmethod
from nltk import word_tokenize
from nltk.corpus import stopwords
import math

>>>>>>> 1e37b91fa2a650aaca6f4ca2152989406facd410

class InvertedIndex: 
    def __init__(self):
        self.trie = Trie(root=True)
class Indexer: 
    def __init__(self, docs: Collection):
<<<<<<< HEAD
        t0 = time.time()
        self.docs = self.select_keywords(docs)  
        t = time.time() - t0
        a = 2
=======
        self.docs = docs        
>>>>>>> 1e37b91fa2a650aaca6f4ca2152989406facd410
    
    def __call__(self) -> InvertedIndex:
        index = InvertedIndex()
        index.trie(self.docs)
        return index
<<<<<<< HEAD
    
    def select_keywords(self, docs: Collection) -> Collection:
        stop_words = set(stopwords.words('english'))
        new_docs = []
        for doc in docs.__iter__():
            tokenized_body = word_tokenize(doc.body.lower())
            tokenized_body = [WordNetLemmatizer().lemmatize(w) for w in tokenized_body]
            tokenized_body = [token for token in tokenized_body if not token in stop_words]
            new_doc = Document(doc.id, doc.title, " ".join(tokenized_body))
            new_docs.append(new_doc)
        return Collection(new_docs)
    
    def select_nouns(self, docs: Collection):
        #stop_words = set(stopwords.words('english'))
        is_noun = lambda pos: pos == 'NN'
        new_docs = []
        for doc in docs.__iter__():
            tokenized_body = word_tokenize(doc.body.lower())
            tokenized_body = [WordNetLemmatizer().lemmatize(w) for w in tokenized_body]            
            tokenized_body = [token for (token, pos) in pos_tag(tokenized_body) if is_noun(pos)]
             
            new_doc = Document(doc.id, doc.title, " ".join(tokenized_body))
            new_docs.append(new_doc)
        return Collection(new_docs)
=======

>>>>>>> 1e37b91fa2a650aaca6f4ca2152989406facd410
    
    
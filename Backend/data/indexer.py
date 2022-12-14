from data.corpus_manager import Collection, Document
from data.trie import Trie
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import time

class InvertedIndex: 
    def __init__(self):
        self.trie = Trie(root=True)
class Indexer: 
    def __init__(self, docs: Collection):
        print ("haciendo stemming, esta accion puede tardar varios segundos. ")
        t0 = time.time()
        self.docs = self.select_keywords(docs)  
        print ("stemming success [" + str(time.time() - t0)+ "s]")
        
        a = 2
    
    def __call__(self) -> InvertedIndex:
        index = InvertedIndex()
        index.trie(self.docs)
        return index
    
    def select_keywords(self, docs: Collection) -> Collection:
        stop_words = set(stopwords.words('english'))
        new_docs = []
        for doc in docs.__iter__():
            tokenized_body = word_tokenize(doc.body.lower())
            tokenized_body = [PorterStemmer().stem(w) for w in tokenized_body]
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
            tokenized_body = [PorterStemmer().stem(w) for w in tokenized_body]            
            tokenized_body = [token for (token, pos) in pos_tag(tokenized_body) if is_noun(pos)]
             
            new_doc = Document(doc.id, doc.title, " ".join(tokenized_body))
            new_docs.append(new_doc)
        return Collection(new_docs)
    
    
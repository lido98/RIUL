from backend.corpus_manager import Collection, Document
from backend.indexer import BaseIndexer, BaseInvertedIndex
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import math



class VectorInvertedIndex(BaseInvertedIndex):   

    def __init__(self):
        self.vocabulary: dict[str: dict[Document: int]] = {} 
        self.max_freq: dict[Document: int] = {} 

    def get_tf(self, term, doc):
        tf = self.vocabulary[term][doc]/self.max_freq[doc]
        return tf

    def get_idf(self, term):
        idf = math.log10(len(self.max_freq) / len(self.vocabulary[term]))
        return idf

    def get_weight(self, term, doc):        
        return self.get_tf(term, doc) * self.get_idf(term)

    def __len__(self) -> int:
        return len(self.vocabulary)

    def __iter__(self):           
        return self.vocabulary

    def __getitem__(self, term: str) -> Collection:
        return Collection(list(self.vocabulary[term].__iter__()))



class VectorIndexer(BaseIndexer): 
    def __init__(self, docs: Collection):
        self.docs = docs        

    def __call__(self) -> VectorInvertedIndex:
        index = VectorInvertedIndex()
        vocabulary: dict[str: dict[Document: int]] = index.vocabulary
        max_freq: dict[Document: int] = index.max_freq

        stop_words = set(stopwords.words('english'))
        
        for i in range(len(self.docs)):
            doc = self.docs[i]
            term_bag, _ = self.extract_keywords(doc, stop_words)
            
            for term in term_bag:                
                if term in vocabulary: 
                    term_dict = vocabulary[term]  
                    try:             
                        term_dict[doc] += 1                        
                    except:                     
                        term_dict[doc] = 1
                        max_freq[doc] = 1                                             
                else:
                    vocabulary[term] = {doc : 1}                    
                try:
                    max_freq[doc] = max(max_freq[doc], term_dict[doc])
                except:
                    max_freq[doc] = 1 
        
        return index
        

    def extract_keywords(self, doc: Document, stop_words: set) -> tuple[list[str], Document]:
        id, title, body = doc.id, doc.title, doc.body.lower()
        tokenized_body = word_tokenize(body)
        tokenized_body = [WordNetLemmatizer().lemmatize(w) for w in tokenized_body]
        tokenized_body = [token for token in tokenized_body if not token in stop_words]
        doc = Document(id, title, " ".join(tokenized_body))
        return tokenized_body, doc
        
from .corpus_manager import Collection
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

class InvertedIndex:
    pass

class Indexer: 
    def __init__(self, docs: Collection):
        self.docs = docs   
        self.vocabulary, self.doc_bodies = self.select_keywords(self.docs.doc_bodies())    

    def __call__(self) -> InvertedIndex:          
        vectorize = TfidfVectorizer(vocabulary=self.vocabulary)
        weight = vectorize.fit_transform(self.doc_bodies)
        return weight

    def select_keywords(self, docs: list[str]) -> list[str]:
        stop_words = set(stopwords.words('english'))
        keywords: set[str] = set()
        tokenized_docs = []
        for doc in docs:
            doc = doc.lower()
            tokenized_doc = word_tokenize(doc)
            tokenized_doc = [WordNetLemmatizer().lemmatize(w) for w in tokenized_doc]
            tokenized_doc = [token for token in tokenized_doc if not token in stop_words]            
            for keyword in tokenized_doc:
                keywords.add(keyword)
            tokenized_docs.append(" ".join(tokenized_doc))
        return list(keywords), tokenized_docs







    






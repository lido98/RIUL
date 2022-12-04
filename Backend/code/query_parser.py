from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


class Query:
    pass

class QueryIndexer:
    def __init__(self, vocabulary, a = 0.5):
        self.a = a
        self.vocabulary = vocabulary

    
    def calculate_weight(self, tf, idf):
        return (self.a + (1 - self.a) * tf) * idf

    def select_keywords(self, query) -> list[str]:
        stop_words = set(stopwords.words('english'))
        tokenized = word_tokenize(query)
        tokenized = [WordNetLemmatizer().lemmatize(w) for w in tokenized]
        tokenized = [token for token in tokenized if not token in stop_words]

        return " ".join(tokenized)
        
    
    def __call__(self, query):
        query = query.lower()
        query = self.select_keywords(query)
        vectorize = TfidfVectorizer(vocabulary=self.vocabulary)
        weight = vectorize.fit_transform([query])
        return weight


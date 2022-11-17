from abc import ABC, abstractmethod
from pathlib import Path
from os import path
import re

class BaseDocument:
    def __init__(self,id,name,bodie):  
        self.id = id
        self.name = name      
        self.text = bodie
        

class BaseParser(ABC):    
    @abstractmethod
    def __call__(self, text):
        pass

 
class CRANParser(BaseParser):
    def __init__(self) -> None:
        self.re_title = re.compile("\.T")
        self.re_autor = re.compile("\.A")
        self.re_B = re.compile("\.B")
        self.re_body = re.compile("\.W")

    def __call__(self, text):
        docs_tokenized = self.tokenize_documents(text)
        docs = []
        for i, elem in enumerate(docs_tokenized):
            doc = BaseDocument(i+1,elem[0],elem[1])
            docs.append(doc)
        return docs
    
    def tokenize_documents(self, text):        
        
        docs_splitted = re.split("\.I [0-9]*", text)[1:]
        docs_tokenized = []
        for doc in docs_splitted:
            doc = re.split(self.re_title, doc)[1]
            title, doc = re.split(self.re_autor, doc, 1)
            _, doc = re.split(self.re_B, doc, 1)
            _, body = re.split(self.re_body, doc, 1)

            title = title.replace("\n", "")
            body = body.replace("\n", "")
            docs_tokenized.append((title, body))
        return docs_tokenized

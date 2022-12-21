from abc import ABC, abstractmethod


class Document:
    def __init__(self, id: int, title: str, body: str):  
        self.id = id
        self.title = title     
        self.body = body


class Collection:
    def __init__(self, docs: list[Document]):
        self.docs = docs
    
    def __iter__(self) -> list[Document]:
        return self.docs

    def __getitem__(self, i: int) -> Document:
        return self.docs[i]
 
    def __len__(self) -> int:
        return len(self.docs)

    def doc_bodies(self) -> list[str]:
        return list(map(lambda doc: doc.body, self.docs))  

    def __add__(self, doc: Document):
        self.docs.append(doc)  


class BaseCorpusParser(ABC):
    @abstractmethod
    def get_raw_docs(self) -> list[str]:
        pass

    @abstractmethod
    def tokenize_docs(self, raw_docs: list[str]) -> list[(int,str,str)]:
        pass
        
    def __call__(self) -> Collection:
        raw_docs = self.get_raw_docs()
        tokenized_docs = self.tokenize_docs(raw_docs)
        docs = []
        for doc in tokenized_docs:
            docs.append(Document(doc[0], doc[1], doc[2]))
        return Collection(docs)



 


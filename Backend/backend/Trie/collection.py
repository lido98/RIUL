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
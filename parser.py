from abc import ABC, abstractmethod
from pathlib import Path
from os import path

class BaseDocument:
    def __init__(self,name,bodie):  
        self.name = name      
        self.text = bodie
        

class BaseParser(ABC):    
    @abstractmethod
    def __call__(self, text: str) -> list[BaseDocument]:
        pass

class DirectoryParser():
    def __call__(self, text: str = './TestCollection') -> list[BaseDocument]:   # text contiene la direccion de la coleccion de documentos
        directory = text
        docs = []
        pathlist = Path(directory).glob('*.txt')
        
        for doc_path in pathlist:            
            bodie = doc_path.read_text()
            _, doc_name = path.split(doc_path)
            docs.append(BaseDocument(doc_name, bodie))
        return docs      


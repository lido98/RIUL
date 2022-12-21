import pathlib

class ConsultTest:
    docs_by_id = {}
    consults = []
    def __init__(self, id, text) -> None:
        self.text = text
        self.id = id
        self.r_documents = []
        ConsultTest.docs_by_id[id] = []
        ConsultTest.consults.append(self)

    def append(self,document):
        self.r_documents.append(document)
        ConsultTest.docs_by_id[id].append(document)    
        
    staticmethod    
    def read(qrels,queries):
        path = str(pathlib.Path(__file__).parent.absolute()) + queries
        text = open(path).read().split("\n")
        
        i = 0
        while(i <len(text)):
            ConsultTest(int(text[i]),text[i+1])
            i+=2

        path = str(pathlib.Path(__file__).parent.absolute()) + qrels
        data = open(path).read().split("\n")
        
        
        return [file.read()]

ConsultTest.read('/files Vaswani/qrels.txt','/files Vaswani/queries.txt')
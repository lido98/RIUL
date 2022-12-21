from corpus_manager import BaseCorpusParser
import pathlib
import re


class ReutersParser(BaseCorpusParser):
    
    def get_raw_docs(self) -> list[str]:
        path = str(pathlib.Path(__file__).parent.absolute()) + '\\files'
        directory = pathlib.Path(path)
        raw_docs = []
        for file in directory.iterdir():
            raw_docs.append(open(file).read())
        return raw_docs

    
    def tokenize_docs(self, raw_docs: list[str]) -> list[(int,str,str)]: 
        tokenized_docs = []

        for docs_file in raw_docs:
            splitted_docs = re.split("</REUTERS>", docs_file)
            splitted_docs = splitted_docs[:len(splitted_docs)-1]
            for doc in splitted_docs:
                doc = re.split("NEWID=\"", doc)[1]
                id, doc = re.split("\"", doc, 1)
                if "<TITLE>" in doc:
                    doc = re.split("<TITLE>", doc,1)[1]
                    title, doc = re.split("</TITLE>", doc, 1)
                else:
                    title = 'UNTITLED DOCUMENT'
                
                if "<BODY>" in doc:
                    doc = re.split("<BODY>", doc, 1)[1]
                    body = re.split("Reuter", doc, 1)[0]
                else:
                    body = re.split("</TEXT>", doc, 1)[0]

                title = title.replace("\n", "")
                tokenized_docs.append((int(id),  title, body))                  
        
        return tokenized_docs
    
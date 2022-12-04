from backend.corpus_manager import BaseCorpusParser
import pathlib
import re


class CRANParser(BaseCorpusParser):

    def get_raw_docs(self) -> list[str]:
        path = str(pathlib.Path(__file__).parent.absolute()) + '\\files\\cran_all_1400.txt'
        file = open(path)
        return [file.read()]     
        
    def tokenize_docs(self, raw_docs: list[str]) -> list[(int,str,str)]: 
        raw_docs = raw_docs[0]         
        tokenized_docs = []
        splitted_docs = re.split("\.I [0-9]*", raw_docs)[1:]
        
        for i, doc in enumerate(splitted_docs):
            doc = re.split("\.T", doc)[1]
            title, doc = re.split("\.A", doc, 1)
            doc = re.split("\.B", doc, 1)[1]
            body = re.split("\.W", doc, 1)[1]

            title = title.replace("\n", "")
            body = body.replace("\n", "")
            tokenized_docs.append((i+1,  title, body))
        return tokenized_docs
    
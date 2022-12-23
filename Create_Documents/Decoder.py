from RIUL.Backend.data.Corpus.Vaswani.vaswani_parser import VaswaniParser
from RIUL.Backend.data.Corpus.CRAN.cran_parser import CRANParser

"""Este .py debe copiarse en paralelo con el proyecto y tener en paralelo al mismo una carpeta 
llamada documents, dentro de la misma deben existir las subcarpetas vaswani y cran"""

import os

def VaswaniCreateFiles():
    docs = VaswaniParser()()
    create_files(docs,"vaswani")

def CranCreateFiles():
    docs = CRANParser()()
    create_files(docs,"cran")

def create_files(docs, folder):    
    for doc in docs.docs:
        id = doc.id
        title = doc.title
        p = doc.body

        file = open("documents/"+folder+"/"+str(id)+".html", "w")
        file. write('<title id = "tittle">'+title+'</title>' + os.linesep)
        file. write('<h1>'+ title +'</h1>' + os.linesep)
        file. write(p)
        file. close()

VaswaniCreateFiles()
CranCreateFiles()

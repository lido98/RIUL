from ast import Mod
from data.Corpus.CRAN.cran_parser import CRANParser
from data.Corpus.Vaswani.vaswani_parser import VaswaniParser
from data.Models.Vector_Model.vector_search_engine import VectorSearchEngine
from data.Models.Latent_Semantic_Indexing_Model.latent_semantic_search_engine import LatentSemanticSearchEngine
from data.indexer import Indexer
from data.search_engine import BaseSearchEngine
from data.corpus_manager import Collection, Document
from data.interactive import select
import environment 

def main():
    selection = select()
    corpus = selection[0]
    model = selection[1]   
    
    docs: Collection
    match corpus:
        case 'CRAN':
            docs = CRANParser()()
            environment.Environment.corpus = "cran"
        case 'VASWANI':
            docs = VaswaniParser()()
            environment.Environment.corpus = "vaswani"
    
    index = Indexer(docs)()
    environment.Environment.index = index
    
    match model:
        case 'VECTORIAL':            
            environment.Environment.search_engine = VectorSearchEngine(index,docs)
        case 'LSI':
            environment.Environment.search_engine = LatentSemanticSearchEngine(index,docs,200)

if __name__ == '__main__':
    main()

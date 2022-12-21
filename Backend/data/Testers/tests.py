import pathlib
import math
from data.Testers import selects

from data.Corpus.CRAN.cran_parser import CRANParser
from data.Corpus.Vaswani.vaswani_parser import VaswaniParser
from data.Models.Vector_Model.vector_search_engine import VectorSearchEngine
from data.Models.Latent_Semantic_Indexing_Model.latent_semantic_search_engine import LatentSemanticSearchEngine
from data.corpus_manager import Collection
from data.indexer import Indexer
from data.search_engine import BaseSearchEngine
from data.metrics import Precission, Recall, F1Mean


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
    def reset():
        ConsultTest.docs_by_id = {}
        ConsultTest.consults = []

    staticmethod    
    def read(qrels,queries):
        ConsultTest.reset()
        path = str(pathlib.Path(__file__).parent.absolute()) + queries
        text = open(path).read().split("\n")
        
        i = 0
        while(i <len(text)):
            ConsultTest(int(text[i]),text[i+1])
            i+=2

        path = str(pathlib.Path(__file__).parent.absolute()) + qrels
        data = open(path).read().split("\n")
        for q in data:
            temp = q.split(" ")
            ConsultTest.docs_by_id[int(temp[0])].append(int(temp[1]))


class Testing:
    def get_rel_docs(consult_id):
        return ConsultTest.docs_by_id[consult_id]

    def set_corpus(corpus):
        ConsultTest.read('/'+corpus+'/qrels.txt','/'+corpus+'/queries.txt')
    
    def docs_to_list(docs):
        r_docs = []
        for doc in docs:
            r_docs.append(doc.id)
        return r_docs    

    def start():
        model = selects.select_model()
        corpus = selects.select_corpus()
        Testing.set_corpus(corpus)

        docs: Collection
        match corpus:
            case 'files Cran':
                docs = CRANParser()()
            case 'files Vaswani':
                docs = VaswaniParser()()

        index = Indexer(docs)()
        search_engine: BaseSearchEngine
        
        match model:
            case 'VECTORIAL':            
                search_engine = VectorSearchEngine(index,docs)
            case 'LSI':
                search_engine = LatentSemanticSearchEngine(index,docs,200)

        a = 0.05    
        while(True):
            total_precission = 0
            total_recall = 0
            total_F1Mean = 0

            for consult in ConsultTest.consults:
                RR = Testing.docs_to_list(search_engine(consult.text,a))
                REL = Testing.get_rel_docs(consult.id)

                current_presition = Precission()(RR,REL)
                if not math.isnan(current_presition):   
                    total_precission+=current_presition
                
                current_recall = Recall()(RR,REL)
                if not math.isnan(current_recall):   
                    total_recall+=current_recall

                current_F1Mean = F1Mean()(RR,REL)
                if not math.isnan(current_F1Mean):   
                    total_F1Mean+=current_F1Mean


            total_precission /=len(ConsultTest.consults)
            total_F1Mean /= len(ConsultTest.consults)
            total_recall /= len(ConsultTest.consults)

            print("\>ntop = "+str(round(a,2)))
            print("     total precission: " + str(round(total_precission,5)))
            print("     total recall: " + str(round(total_recall,5)))
            print("     total F1Mean: " + str(round(total_F1Mean,5)))
            
            a +=0.05
            if a >=1: break
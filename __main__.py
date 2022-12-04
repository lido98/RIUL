from Corpus.CRAN.cran_parser import CRANParser
from Corpus.Reuters.reut_parser import ReutersParser
from ranking_manager import Ranking
from corpus_manager import Collection, Document


def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')
    
    docs = Collection([Document(1, 'doc 1', 'leon leon leon'),Document(2, 'doc 2', 'leon leon leon zorro'),Document(3, 'doc 3', 'leon zorro nutria'),Document(4, 'doc 4', 'leon leon leon zorro zorro zorro'),Document(5, 'doc 5', 'nutria')])
    #docs = CRANParser()()
    #docs = ReutersParser()()       
    ranking = Ranking(-1)
    print('Por favor, introduzca la consulta:')
    #query = input()
    query = "leon leon leon perro zorro gato gato"
    recovered = ranking.rec_files(docs, query)
    
    print('----------------------------------------------------------------------\nLos documentos recuperados, junto a su ranking, son:\n')
    #print(len(recovered))
    for r in recovered:
        print(str(docs[r[0]].id) + ' ' + docs[r[0]].title + ' ' + str(round(r[1],5))   + '\n')
    
      
    
if __name__ == '__main__':
    main()





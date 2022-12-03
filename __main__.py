from .Corpus.CRAN.cran_parser import CRANParser
from .Corpus.Reuters.reut_parser import ReutersParser
from .ranking_manager import Ranking


def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')
    
    docs = CRANParser()()
    #docs = ReutersParser()()       
    ranking = Ranking(0.1)
    print('Por favor, introduzca la consulta:')
    query = input()
    recovered = ranking(docs, query)
    print('----------------------------------------------------------------------\nLos documentos recuperados, junto a su ranking, son:\n')
    for r in recovered:
        print(str(docs[r[0]].id) + ' ' + docs[r[0]].title + ' ' + str(round(r[1][0],3))   + '\n')
      
    
if __name__ == '__main__':
    main()





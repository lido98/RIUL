from document_parser import CRANParser
from ranking_manager import Ranking
#from Test_Collections.CRAN.cran_document_parser import CRANParser
import os

def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección CRAN para recuperar la información.\n')
    cran = open(os.getcwd() + '\\Test_Collections\\cran_all_1400.txt')
    text = cran.read()
    docs = CRANParser()(text)
    docs_bodie = [doc.text for doc in docs]
    ranking = Ranking(0.1)
    print('Por favor, introduzca la consulta:')
    query = input()
    recovered = ranking(docs_bodie, query)
    print('----------------------------------------------------------------------\nLos documentos recuperados, junto a su ranking, son:\n')
    for r in recovered:
        print(str(docs[r[0]].id) + ' ' + docs[r[0]].name + ' ' + str(round(r[1][0],3))   + '\n')
      
    
if __name__ == '__main__':
    main()





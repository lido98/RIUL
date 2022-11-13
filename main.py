from parser import DirectoryParser, BaseDocument
from ranking import Ranking

def main():
    print('Bienvenido al sistema de recuperación de información RIUL !!!')
    print('RIUL utiliza la colección de documentos contenidos en \'./TestCollection\' para recuperar la información.\nSu umbral de recobrado es 0.1 y su factor de suavizado 0.5.\n')
    docs = DirectoryParser()()
    docs_bodie = [doc.text for doc in docs]
    ranking = Ranking()
    print('Por favor, introduzca la consulta:')
    query = input()
    recovered = ranking(docs_bodie, query)
    print('----------------------------------------------------------------------\nLos documentos recuperados, junto a su ranking, son:\n')
    for r in recovered:
        print(docs[r[0]].name + ' ' + str(round(r[1],3)) + '\n')

if __name__ == '__main__':
    main()





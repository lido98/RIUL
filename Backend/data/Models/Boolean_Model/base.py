from data.trie import Trie

class BoolMatrix:
    def __init__(self,trie:Trie):
        self.trie = trie
        #Este es el trie que tiene toda la informacion tiza

        self.words = trie.words
        #Lista con todas las palabras, esta es la que define el orden a nivel de columna de las mismas

        self.total_documents = trie.total_documents
        #La cantidad de documentos que existen en total

        self.index_word = {}
        #Le entras una palabra y te devuelve la posicion en que esta (la columna)
        
        self.matrix = self.full_matrix()
        #Aqui lleno una matriz con ceros y uno segun si esta o no esta la palabra en el documento
        
    def full_matrix(self):
        words = self.words
        trie = self.trie

        matrix = []
        
        for i in range(trie.total_documents):
            matrix.append([0] * len(words))

        for word,w in zip(words, range(len(words))):
            self.index_word[word] = w
            documents = trie.documents_of_word(word)
            for document in documents:
                d = trie.index_document[document]
                matrix[d][w] = 1 # si esta la palabra w en el documento d, se pone 1 en esa casilla
        
        return matrix

    def get_rank_of_query(self,query):
        pass
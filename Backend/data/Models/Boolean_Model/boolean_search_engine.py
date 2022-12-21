from data.search_engine import BaseSearchEngine
from data.indexer import InvertedIndex
from data.corpus_manager import Collection, Document
from data.Models.Boolean_Model.boolean_query_parser import BooleanQueryParser
import numpy as np
from data.trie import Trie
from math import log10
from collections import deque



class BooleanSearchEngine(BaseSearchEngine):
    def __init__(self, index: InvertedIndex, docs: Collection):
        self.index = index
        self.docs = docs
        self.boolean_matrix = BooleanMatrix(self.index.trie)
        self.matrix = np.transpose(self.boolean_matrix.matrix)            
        

    def __call__(self, raw_query: str) -> dict[Document: float]:

        query = BooleanQueryParser(raw_query).query
        
        stack = deque()
        
        for token in query:
            if token in ('|', '&'):
                right_operand = stack.pop()
                left_operand = stack.pop()
                new_vector = self.make_operation(left_operand, right_operand, token)
                stack.append(new_vector)
            else:
                stack.append(self.make_vector(token))

        matching_docs = [self.docs[i] for i in np.where(stack[-1])[0]]

        return matching_docs

        

    def make_operation(self, left_operand, right_operand, operator):
        match operator:
            case '|':
                return left_operand | right_operand
            case '&':
                return left_operand & right_operand

    def make_vector(self, word):
        negative = False
        if word[0] == "!":
            negative = True
            word = word[1:]

        if word in self.boolean_matrix.words:
            vector = self.matrix[self.boolean_matrix.index_word[word]]
        else:
            vector = np.zeros(self.boolean_matrix.total_documents, dtype=int)

        if negative:
            vector = [np.abs(n-1) for n in vector]
        return vector

    
            

        

            



              
        

    

          

class BooleanMatrix:
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
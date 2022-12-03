from collection import Document
from trie import Trie, Collection, VectorialMatrix

import re, string

def remove_punctuation ( text ):
  new_text = re.sub('\n', ' ', text)
  return re.sub('[%s]' % re.escape(string.punctuation), ' ', new_text)

def main ():
    test_cases_trie()

def test_cases_trie():
    trie = Trie(root = True)
    text1 = remove_punctuation(open("Trie//texts//text1.txt","r").read().lower())
    text2 = remove_punctuation(open("Trie//texts//text2.txt","r").read().lower())
    text3 = remove_punctuation(open("Trie//texts//text3.txt","r").read().lower())
    text4 = remove_punctuation(open("Trie//texts//text4.txt","r").read().lower())

    documents = [ Document(1,"tittle",text1),
                  Document(2,"tittle",text2),
                  Document(3,"tittle",text3),
                  Document(4,"tittle",text4)]

    trie.insert_collection(Collection(documents))
    matrix = VectorialMatrix(trie)
    
    while (True):
        print ("\nEntre la palabra que desea tener informacion")
        word = input()
        print ("\nEntre el id del documento del cual desea conocer informacion respecto a la palabra anterior")
        doc = input()

        print(word + " aparece: " + str(trie.word_count_in_document(word,int(doc))))
        print(word + " aparece en los documentos: "+str(str(trie.documents_of_word(word))))
        
        print ("cantidad de documentos del trie: " + str(trie.documents)+"["+str(trie.total_documents)+"]")
        print ("Maximas repeticiones del trie: " + str(trie.max_count_in_document))
        print("\n")

main()

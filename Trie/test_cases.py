from trie import Trie

import re, string

def remove_punctuation ( text ):
  new_text = re.sub('\n', ' ', text)
  return re.sub('[%s]' % re.escape(string.punctuation), ' ', new_text)

def main ():
    test_cases_trie()

def test_cases_trie():
    trie = Trie(root = True)
    text = remove_punctuation(open("Trie//texts//text1.txt","r").read().lower())
    
    import time
    inicio = time.time()
    #region create trie
    trie.insert_text(text,'text1')
    #endregion
    print("\nTarda " +str(time.time()-inicio)+" para crear un trie de "+str(len(text))+" letras.") 

    text = remove_punctuation(open("Trie//texts//text2.txt","r").read().lower())
    trie.insert_text(text,'text2')

    text = remove_punctuation(open("Trie//texts//text3.txt","r").read().lower())
    trie.insert_text(text,'text3')

    text = remove_punctuation(open("Trie//texts//text4.txt","r").read().lower())
    trie.insert_text(text,'text4')

    while (True):
        print ("\nEntre la palabra que desea tener informacion")
        word = input()
        print ("\nEntre el id del documento del cual desea conocer informacion respecto a la palabra anterior")
        doc = input()

        print(word + " aparece: " + str(trie.word_count_in_document(word,doc)))
        print(word + " aparece en los documentos: "+str(str(trie.documents_of_word(word))))
        print(word + " idf: "+str(str(trie.idf_of_word(word))))
        
        print ("cantidad de documentos del trie: " + str(trie.documents)+"["+str(trie.total_documents)+"]")
        print ("Maximas repeticiones del trie: " + str(trie.max_count_in_document))
        print("\n")

main()

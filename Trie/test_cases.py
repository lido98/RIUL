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
   
    text1 = "leon leon leon"
    text2 = 'leon leon leon zorro'
    text3 = 'leon zorro nutria'
    text4 =  'leon leon leon zorro zorro zorro'
    text5 =   'nutria'
    text6 =   'nutria perro leon leon tiburon sandia omnitorrinco azul zorro verde'

    d1 = Document(1,"doc1",text1)
    d2 = Document(2,"doc2",text2)
    d3 = Document(3,"doc3",text3)
    d4 = Document(4,"doc4",text4)
    d5 = Document(5,"doc5",text5)
    d6 = Document(6,"doc6",text6)

    documents = [ d1,d2,d3,d4,d5]

    trie.insert_collection(Collection(documents))
    matrix = VectorialMatrix(trie)
    rank = matrix.get_rank_of_query("leon leon leon perro zorro gato gato")
    for doc in rank:
          print (doc.title +" [id:"+str(doc.id)+"]"+ " >>> rank = " + str(rank[doc]))
main()

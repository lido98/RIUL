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
    # text1 = remove_punctuation(open("Trie//texts//text1.txt","r").read().lower())
    # text2 = remove_punctuation(open("Trie//texts//text2.txt","r").read().lower())
    # text3 = remove_punctuation(open("Trie//texts//text3.txt","r").read().lower())
    # text4 = remove_punctuation(open("Trie//texts//text4.txt","r").read().lower())

    text1 = "leon leon leon"
    text2 = 'leon leon leon zorro'
    text3 = 'leon zorro nutria'
    text4 =  'leon leon leon zorro zorro zorro'
    text5 =   'nutria'

    d1 = Document(1,"tittle",text1)
    d2 = Document(2,"tittle",text2)
    d3 = Document(3,"tittle",text3)
    d4 = Document(4,"tittle",text4)
    d5 = Document(5,"tittle",text5)

    documents = [ d1,d2,d3,d4,d5]

    trie.insert_collection(Collection(documents))
    matrix = VectorialMatrix(trie)
    rank = matrix.get_rank_of_query("leon leon leon perro zorro gato gato")
    for doc in rank:
          print (str(doc.id) + " >>> rank = " + str(rank[doc]))
main()

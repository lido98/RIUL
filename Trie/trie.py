from collection import Collection, Document
class Trie:
    last_word = ""
    
    def __init__(self, value = "^", root = False, document_id = 'default', parent = None):
        '''Create new Trie with `root = True`. Create simple node with `root = False`'''
        self.value = value
        self.childs = {}
        
        if root == True: 
            self.root = self
            self.words = []
            self.index_document = {}
            self.documents = []
            self.max_count_in_document = {}
            self.total_documents = 0
        else:
            self.root = parent.root
    
    def insert_collection(self,collection:Collection):
        for document in collection.docs:
            self.insert_document(document, by_id = True)
    
    def insert_document(self, document:Document, by_id = False):
        if by_id == True:
            self.insert_text(document.body, document.id)
        else:
            self.insert_text(document.body, document)

    def insert_text(self,text,document_id = 'default'):
        '''Insert new docuement whit params `text` and a specified `document_id` if you want use many documents, without any document in another case,
        if you do not specify a 'document id', it is assumed to be a single document'''
        words = text.split(" ") 
        for word,pos in zip(words,range(len(words))):
            Trie.last_word = word
            self.insert_word(word,pos,document_id)

    def insert_word(self,word,pos,document_id):
        '''Insert a word in a specified `document_id`'''
        if len(word) > 0:
            self.insert_char_in_children(word[0],word,pos,document_id)

    def insert_char_in_children(self,char,word,pos,document_id):
        if self.root.documents.__contains__(document_id) == False : 
            self.root.documents.append(document_id)
            self.root.index_document[document_id] = self.root.total_documents
            self.root.total_documents += 1
        try : 
            node = self.childs[char]
            if len(word) == 1:
                try: node.count_in_document[document_id]+=1
                except: 
                    try: 
                        node.count_in_document[document_id]=1
                    except: # was a normal node, create all property
                        node.count_in_document = {document_id:1}
                        node.documents = [document_id]
                        node.total_documents = 1

                # Max Frec In Document
                self.new_max_count(document_id,node.count_in_document[document_id])
            
                if node.documents.__contains__(document_id) == False:  
                    node.documents.append(document_id)
                    node.total_documents += 1

            self.childs[char] = node
            self.childs[char].insert_word(word[1:],pos,document_id) #rec

        except:
            node = Trie(char,False,document_id,self)
            if len(word) == 1:
                node.count_in_document = {document_id:1}
                node.documents = [document_id]
                node.total_documents = 1
                self.root.words.append(Trie.last_word)

                # Max Frec In Document
                self.new_max_count(document_id,node.count_in_document[document_id])
                
            self.childs[char] = node
            self.childs[char].insert_word(word[1:],pos,document_id) #rec
            
    def new_max_count(self, document, new_max):
        try:
            max_count = self.root.max_count_in_document[document]
            self.root.max_count_in_document[document] = max(max_count,new_max)
        except:
            self.root.max_count_in_document[document] = 1
            
    def last_node(self,word):
        '''returns the last node of a word in the trie'''
        node = self
        for char in word:
            try: node = node.childs[char]    
            except: return None
        return node 

    def word_count_in_document(self,word,document_id = 'default'):
        '''returns the number of times a word appears as whole word in a document'''
        node = self.last_node(word)
        if node != None:
            try: return node.count_in_document[document_id] 
            except: return 0 
        return 0 
    
    def documents_of_word(self,word):
        node = self.last_node(word)
        if node != None:
            try: return node.documents
            except: return []
        else:
            return []

    def weight (self,word, document):
        from math import log10
        node = self.last_node(word)
        if node != None:
            try:
                idf = log10(node.root.total_documents/node.total_documents)
                tf = node.count_in_document[document]/node.root.max_count_in_document[document]
                return idf*tf
            except: return 0
        else:
            return 0    
class VectorialMatrix:
    def __init__(self,trie:Trie):
        self.trie = trie
        self.words = trie.words
        self.total_documents = trie.total_documents
        self.index_word = {}
        self.rank = {}
        self.matrix = self.full_matrix(trie)
        self.sim_list("leon leon leon perro zorro gato gato")

    def full_matrix(self,trie:Trie):
        words = self.words

        matrix = []
        
        for i in range(trie.total_documents):
            matrix.append([0] * len(words))

        for word,w in zip(words, range(len(words))):
            self.index_word[word] = w
            documents = trie.documents_of_word(word)
            for document in documents:
                d = trie.index_document[document]
                matrix[d][w] = trie.weight(word,document) 
        return matrix        
    
    def get_matrix(self):
        return self.matrix
    
    def freqs_in_query(self, query):
        result = {}
        max_count = 1
        for term in query.split(" "):
            try: 
                result[term] +=1
                max_count = max(max_count,result[term])
            except: result [term] = 1
            
        return [result,max_count]

    def sim_list(self, query):
        freqs = self.freqs_in_query(query)
        
        from math import log10
        vector_query = [0] * len(self.words) 
        
        a = 0.5
        N = self.total_documents + 1

        # for word in self.words:
        #     n_i = len(self.trie.documents_of_word(word)) + 1
        #     vector_query.append( a * log10(N/n_i))

        for word in freqs[0]:
            n_i = len(self.trie.documents_of_word(word)) + 1

            try: 
                vector_query[self.index_word[word]] = (a *((1-a)*(freqs[0][word]/freqs[1])))* (log10(N/n_i))
            except: pass

        for document,d in zip(self.matrix, range(len(self.matrix))):
            self.rank[self.trie.documents[d]]= self.sim(document, vector_query)

    def sim (self, doc, query):
        import numpy as np 
        return np.dot(doc, query)/(np.linalg.norm(doc)*np.linalg.norm(query))    
    
    def get_rank(self):
        return self.rank

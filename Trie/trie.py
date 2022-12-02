class Trie:
    def __init__(self, value = "^", root = False, document_id = 'default', parent = None):
        '''Create new Trie with `root = True`. Create simple node with `root = False`'''
        self.value = value
        self.position_in_document = {}
        self.position_in_document_as_word = {}
        self.count_as_prefix_in_document = {}
        self.count_as_word_in_document = {}
        self.documents = [document_id]
        self.childs = {}
        self.max_count_in_document = {}
        
        if root == True: 
            self.count_as_prefix_in_document = {}
            self.root = self
        else:
            self.root = parent.root
    
    def insert_text(self,text,document_id = 'default'):
        '''Insert new docuement whit params `text` and a specified `document_id` if you want use many documents, without any document in another case,
        if you do not specify a 'document id', it is assumed to be a single document'''
        words = text.split(" ") 
        for word,pos in zip(words,range(len(words))):
            self.insert_word(word,pos,document_id)

    def insert_word(self,word,pos,document_id):
        '''Insert a word in a specified `document_id`'''
        if len(word) > 0:
            self.insert_char_in_children(word[0],word,pos,document_id)

    def insert_char_in_children(self,char,word,pos,document_id):
        try : 
            node = self.childs[char]
            if len(word) == 1:
                try: node.count_as_word_in_document[document_id]+=1
                except: node.count_as_word_in_document[document_id]=1
            
                try:node.position_in_document_as_word[document_id].append(pos)
                except:node.position_in_document_as_word[document_id]=[pos]
                
                # Max Frec In Document
                self.new_max_count(document_id,node.count_as_word_in_document[document_id])
            
            try: node.count_as_prefix_in_document[document_id]+=1
            except: node.count_as_prefix_in_document[document_id]=1
            
            try:node.position_in_document[document_id].append(pos)
            except:node.position_in_document[document_id]=[pos]
            
            if node.documents.__contains__(document_id) == False:  node.documents.append(document_id)
            
            self.childs[char] = node
            self.childs[char].insert_word(word[1:],pos,document_id) #rec

        except:
            node = Trie(char,False,document_id,self)
            if len(word) == 1:
                node.count_as_word_in_document[document_id] = 1
                node.position_in_document_as_word[document_id] = [pos]   
                
                # Max Frec In Document
                self.new_max_count(document_id,node.count_as_word_in_document[document_id])
             
            node.count_as_prefix_in_document[document_id] = 1
            node.position_in_document[document_id] = [pos]    
            
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
    
    def prefix_count_in_document(self,word,document_id = 'default'):
        '''returns the number of times a word appears as prefix in a document'''
        node = self.last_node(word)
        if node != None:
            try: return node.count_as_prefix_in_document[document_id] 
            except: return 0
        return 0    

    def word_count_in_document(self,word,document_id = 'default'):
        '''returns the number of times a word appears as whole word in a document'''
        node = self.last_node(word)
        if node != None:
            try: return node.count_as_word_in_document[document_id] 
            except: return 0 
        return 0 

    def prefix_position_in_document(self,word,document_id = 'default'):
        '''returns the all positions of a word as prefix in a document'''
        node = self.last_node(word)
        if node != None:
            try: return node.position_in_document[document_id] 
            except: return []
        return []
    
    def word_position_in_document(self,word,document_id = 'default'):
        '''returns the all positions of a word as whole word in a document'''
        node = self.last_node(word)
        if node != None:
            try: return node.position_in_document_as_word[document_id] 
            except: return []
        return []

    def documents_of_word(self,word):
        node = self.last_node(word)
        if node != None:
            return node.documents
        else:
            return []    
from collections import deque
from data.query_parser import BaseQueryParser

class BooleanQueryParser(BaseQueryParser):
    def __init__(self, raw_query: str):
        super().__init__(raw_query)
              
    
    def parse_query(self, query: str):
        tokenized_query = self.adding_and(query.split())
        return self.get_postfix_notation(tokenized_query)    

    def is_a_word(self, token):
        return token not in ('&', '|', '(', ')')  

    def adding_and(self, query):
        last_token_was_word = False
        i = 0
        while i < len(query):        
            token = query[i]
            current_token_is_a_word = self.is_a_word(token)
            if last_token_was_word and current_token_is_a_word:
                query.insert(i, '&')
                i += 1
            last_token_was_word = current_token_is_a_word
            i += 1
        return query


    def get_postfix_notation(self, tokenized_query):        
        stack = deque()
        postfix_query = []

        for token in tokenized_query:
            match token:
                case '(':
                    stack.append(token)
                case ')':
                    while len(stack)!=0 and stack[-1] != '(':
                        item = stack.pop()
                        postfix_query.append(item)
                    if len(stack)!=0 and stack[-1] != '(':
                        raise ValueError("The query format is wrong.")
                    else:
                        stack.pop()                    
                case '&':
                    while len(stack) != 0 and stack[-1] not in ('(',')'):
                        postfix_query.append(stack.pop())
                    stack.append(token)
                case '|':
                    while len(stack) != 0 and stack[-1] not in ('(',')'):
                        postfix_query.append(stack.pop())
                    stack.append(token)
                case _:
                    postfix_query.append(token)
            
        while len(stack)!=0:
            postfix_query.append(stack.pop())

        return postfix_query





                    



        

    


    

